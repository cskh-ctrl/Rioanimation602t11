"""pipeline/captions.py - accurate word timings + phrase-aware caption groups + clean SRT.

1. refine_words(): run faster-whisper on the real voice track and map its word timings onto the
   exact script words (sentence windows from TTS stay exact; only in-sentence timing is refined).
2. phrase_groups(): split each sentence into readable phrases that break at punctuation or before
   conjunctions, never across sentences, never ending on a weak word like "the" or "a".
3. srt_from_words(): subtitle cues built from those phrases (max 2 lines x 42 chars), timed on words.
"""
import difflib, re

WEAK = {"a", "an", "the", "to", "of", "in", "on", "at", "for", "with", "your", "my", "his", "her", "their", "our",
        "and", "but", "or", "is", "are", "was", "be", "from", "by", "into", "than", "as", "that", "this", "it's", "you're", "i'm", "very", "just", "not", "its", "an", "some", "every", "each", "no", "can", "will", "would", "could", "should", "might", "must", "doesn't", "don't", "didn't", "isn't", "aren't", "wasn't", "weren't", "can't", "won't", "wouldn't", "couldn't", "shouldn't", "haven't", "hasn't", "has", "have", "had"}
CONJ = {"and", "but", "or", "so", "because", "when", "while", "then", "until", "before", "after", "if", "which", "who", "where", "though", "unless", "since"}


def norm(w):
    return re.sub(r"[^\w']+", "", w.lower())


def refine_words(audio_path, words, sents, model_name="base.en"):
    """Return words with Whisper-measured timings, clamped to each sentence window. Falls back to input."""
    try:
        from faster_whisper import WhisperModel
    except Exception as e:  # noqa
        print("captions: faster-whisper missing, keeping estimated timings", e)
        return words
    try:
        import numpy as np, soundfile as sf
        from scipy.signal import resample_poly
        from math import gcd
        au, sr = sf.read(audio_path, dtype="float32")
        if au.ndim > 1: au = au.mean(axis=1)
        g = gcd(sr, 16000); au = resample_poly(au, 16000 // g, sr // g).astype(np.float32)
        model = WhisperModel(model_name, device="cpu", compute_type="int8")
        segs, _ = model.transcribe(au, language="en", word_timestamps=True, vad_filter=False, beam_size=1,
                                   condition_on_previous_text=False)
        ww = [{"w": norm(x.word), "s": x.start, "e": x.end} for s in segs for x in (s.words or []) if norm(x.word)]
    except Exception as e:  # noqa
        print("captions: whisper failed, keeping estimated timings:", repr(e)); return words
    a = [norm(w["word"]) for w in words]
    b = [x["w"] for x in ww]
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    times = [None] * len(words)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            times[blk.a + k] = (ww[blk.b + k]["s"], ww[blk.b + k]["e"])
    matched = sum(t is not None for t in times)
    print(f"captions: whisper matched {matched}/{len(words)} words ({100 * matched / max(1, len(words)):.0f}%)")
    # sentence index of every word (words were produced sentence by sentence, in order)
    sid, k = [], 0
    for i, s in enumerate(sents):
        for _ in s["text"].split():
            sid.append(i); k += 1
    if len(sid) != len(words):
        print("captions: word/sentence count mismatch, keeping estimated timings"); return words
    out = [dict(w) for w in words]
    # clamp matched words into their sentence window, drop outliers
    for i, t in enumerate(times):
        if t is None: continue
        s = sents[sid[i]]
        if t[0] < s["start"] - 0.3 or t[0] > s["end"] + 0.3: times[i] = None
    # per sentence: keep matched, interpolate unmatched by letter weight between anchors
    i = 0
    n = len(words)
    while i < n:
        j = i
        while j < n and sid[j] == sid[i]: j += 1
        s = sents[sid[i]]
        idx = list(range(i, j))
        anchors = [(s["start"], i - 1)] + [(times[q][0], q) for q in idx if times[q]] + [(s["end"], j)]
        # make anchor times monotonic
        fixed = []
        for t, q in anchors:
            if fixed and t < fixed[-1][0]: t = fixed[-1][0]
            fixed.append((t, q))
        for (t0, q0), (t1, q1) in zip(fixed, fixed[1:]):
            gap = [q for q in range(q0 + 1, q1)]
            if gap:
                # start after previous anchor word's end when known
                if q0 >= i and times[q0]: t0 = max(t0, min(times[q0][1], t1))
                wt = [max(2, len(norm(words[q]["word"]))) for q in gap]; tot = sum(wt); acc = t0
                for q, k2 in zip(gap, wt):
                    d = (t1 - t0) * k2 / tot; out[q]["start"] = round(acc, 3); out[q]["end"] = round(acc + d * 0.9, 3); acc += d
            if q1 < j and times[q1]:
                out[q1]["start"] = round(max(t1, s["start"]), 3)
                out[q1]["end"] = round(min(max(times[q1][1], t1 + 0.08), s["end"] + 0.05), 3)
        i = j
    # monotonic + no overlap
    for q in range(1, n):
        if out[q]["start"] < out[q - 1]["start"]: out[q]["start"] = out[q - 1]["start"]
        if out[q - 1]["end"] > out[q]["start"] and sid[q] == sid[q - 1]: out[q - 1]["end"] = out[q]["start"]
        if out[q]["end"] < out[q]["start"] + 0.05: out[q]["end"] = round(out[q]["start"] + 0.05, 3)
    return out


PREP = {"in", "on", "at", "to", "from", "with", "for", "into", "across", "down", "above", "below", "over", "under", "through",
        "toward", "towards", "around", "behind", "past", "without", "like", "inside", "outside", "onto", "off", "about", "against"}
SUBJ = {"you", "i", "he", "she", "they", "we", "it", "there", "nobody", "everyone", "someone"}
NUM = set("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen "
          "eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand million billion trillion point half "
          "quarter percent".split())


ABBR = {"mr", "mrs", "ms", "dr", "st", "jr", "sr", "prof", "mt"}
_TAGGER = [None]


def _hard_parts(toks):
    """Split tokens at sentence-ending punctuation inside one TTS sentence (e.g. 'roads. Now?')."""
    out, a = [], 0
    for k, w in enumerate(toks[:-1]):
        if re.search(r"[.!?]['\")]*$", w) and not w.endswith("...") and norm(w) not in ABBR:
            out.append((a, k + 1)); a = k + 1
    out.append((a, len(toks)))
    return out


def pos_tags(toks):
    """Penn POS tags for tokens (punctuation stripped); None if NLTK tagger is unavailable."""
    if _TAGGER[0] is None:
        try:
            import nltk
            try: nltk.data.find("taggers/averaged_perceptron_tagger_eng/")
            except LookupError: nltk.download("averaged_perceptron_tagger_eng", quiet=True)
            nltk.pos_tag(["test"]); _TAGGER[0] = nltk.pos_tag
        except Exception as e:  # noqa
            print("captions: POS tagger unavailable:", repr(e)); _TAGGER[0] = False
    if not _TAGGER[0]: return None
    clean = [re.sub(r"^[^\w']+|[^\w']+$", "", w) or w for w in toks]
    return [tg for _, tg in _TAGGER[0](clean)]


def break_cost(toks, k, tags=None):
    """Cost of breaking between toks[k-1] and toks[k] (lower = more natural)."""
    prev, nxt = toks[k - 1], toks[k]
    p, q = norm(prev), norm(nxt)
    c = 6.0
    punct = re.search(r"(\.\.\.|…|[,;:.!?])['\")]*$", prev)
    if tags and not punct:
        P, Q = tags[k - 1], tags[k]
        if P[:2] in ("JJ", "DT", "PR") and P != "PRP" and Q[:2] in ("NN", "JJ", "CD"): c += 14
        if P in ("CD", "POS") and Q[:2] in ("NN", "JJ", "CD"): c += 14
        if P[:2] == "NN" and Q[:2] == "NN": c += 10
        if P in ("MD", "TO") and Q[:2] == "VB": c += 14
        if P[:2] == "VB" and Q == "RP": c += 10
        if P[:2] == "VB" and Q == "TO": c += 8
        if P[:2] == "VB" and q in {"you", "me", "him", "her", "them", "us", "it", "yourself", "himself", "herself"}: c += 12
        if P[:2] == "VB" and q in {"around", "back", "up", "out", "down", "off", "away", "over", "in"} and Q in ("RB", "RP", "IN"): c += 7
        if P[:2] == "RB" and Q[:2] in ("JJ", "RB"): c += 8
        if P[:2] in ("NN", "PR") and P != "PRP$" and Q[:2] in ("VB", "MD"): c -= 3
    if re.search(r"[.!?]['\")]*$", prev) and p not in ABBR: c -= 14
    elif re.search(r"(\.\.\.|…|[,;:])['\")]*$", prev): c -= 12
    else:
        if q in CONJ: c -= 6
        elif q in PREP: c -= 4
        elif q in SUBJ and not (tags and tags[k - 1][:2] == "VB"): c -= 3
        if p in WEAK or p in PREP: c += 18
        if p in NUM and q in NUM | {"and"}: c += 25
        if p in NUM: c += 6          # keep a number with its unit (four / minutes)
        if q in {"'s", "too", "else", "now", "again", "ago", "away", "back", "up", "out"}: c += 6
    return c


def _split_sentence(toks, max_words, max_chars, target=None):
    """Optimal split of one sentence into phrases (dynamic programming). Returns list of (i0, i1)."""
    n = len(toks)
    tags = pos_tags(toks) if n > 1 else None
    if n == 0: return []
    chars = lambda a, b: len(" ".join(toks[a:b]))
    if n <= max_words and chars(0, n) <= max_chars: return [(0, n)]
    target = target or max(2, round(max_words * 0.7))
    INF = 1e18
    best = [INF] * (n + 1); prv = [-1] * (n + 1); best[0] = 0
    for b in range(1, n + 1):
        for a in range(max(0, b - max_words), b):
            if best[a] >= INF: continue
            L = b - a
            if chars(a, b) > max_chars and L > 1: continue
            c = best[a] + 0.8 * (L - target) ** 2
            if L == 1 and not re.search(r"[.!?,;:…]$", toks[a]): c += 10
            if b < n: c += break_cost(toks, b, tags)
            if c < best[b]: best[b], prv[b] = c, a
    out, b = [], n
    while b > 0:
        a = prv[b]; out.append((a, b)); b = a
    return out[::-1]


def phrase_groups(words, sents, max_words=6, max_chars=34):
    """Assign w['g'] (phrase id) to every word; phrases never cross sentences."""
    i, g = 0, 0
    for s in sents:
        n = len(s["text"].split())
        toks = [w["word"] for w in words[i:i + n]]
        for h0, h1 in _hard_parts(toks):
            for a, b in _split_sentence(toks[h0:h1], max_words, max_chars):
                for q in range(i + h0 + a, i + h0 + b): words[q]["g"] = g
                g += 1
        i += n
    return words


def _ts(t):
    h, r = divmod(max(0.0, t), 3600); m, s = divmod(r, 60)
    ms = int(round((s - int(s)) * 1000))
    if ms == 1000: ms = 999
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{ms:03d}"


def _two_lines(text, width=42):
    if len(text) <= width: return text
    ws = text.split(); best, bs = None, 1e9; tags = pos_tags(ws)
    for k in range(1, len(ws)):
        l1, l2 = " ".join(ws[:k]), " ".join(ws[k:])
        if len(l1) > width or len(l2) > width: continue
        sc = break_cost(ws, k, tags) * 2 + abs(len(l1) - len(l2)) * 0.25
        if sc < bs: bs, best = sc, l1 + "\n" + l2
    return best or text


def srt_from_words(words, sents):
    """SRT cues: phrases up to 2 lines x 42 chars, split only at natural breaks, timed from words."""
    cues, i = [], 0
    for s in sents:
        n = len(s["text"].split()); ws = words[i:i + n]; i += n
        if not ws: continue
        toks = [w["word"] for w in ws]
        for h0, h1 in _hard_parts(toks):
            for a, b in _split_sentence(toks[h0:h1], 16, 80):
                a += h0; b += h0
                st, en = ws[a]["start"], ws[b - 1]["end"]
                cues.append([st, max(en, st + 0.7), " ".join(toks[a:b])])
    # minimum display time without overlapping the next cue
    for k in range(len(cues)):
        nxt = cues[k + 1][0] if k + 1 < len(cues) else 9e9
        cues[k][1] = min(max(cues[k][1] + 0.15, cues[k][0] + 1.0), nxt - 0.04)
    return "\n".join(f"{k + 1}\n{_ts(a)} --> {_ts(b)}\n{_two_lines(t)}\n" for k, (a, b, t) in enumerate(cues))
