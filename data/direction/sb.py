# shared storyboard helpers. Times "@n.f" = sentence n (0-based within the shot) + fraction f.
import json, os
B = []
def S(lines, set_, actors=(), items=(), **kw):
    d = {"lines": [lines] if isinstance(lines, int) else list(lines), "set": set_.split(":")[0], "actors": list(actors), "items": list(items)}
    if ":" in set_: d["smood"] = set_.split(":")[1]
    d.update(kw); B.append(d)
def A(id_, x, pose="relaxed", expr="neutral", **kw):
    d = {"id": id_, "who": id_, "x": x, "pose": pose if isinstance(pose, list) else [[0, pose]], "expr": expr if isinstance(expr, list) else [[0, expr]]}
    d.update(kw); return d
def card(big, small=None, at=0.12, **kw): d = {"big": big, "small": small, "at": at}; d.update(kw); return d
def prop(p, x, size=0.5, up=0.0, **kw): d = {"k": "prop", "p": p, "x": x, "size": size, "up": up}; d.update(kw); return d
def door(x, **kw): d = {"k": "door", "x": x}; d.update(kw); return d
def T(s, x=0.5, y=0.2, at=0.1, **kw): d = {"s": s, "x": x, "y": y, "at": at}; d.update(kw); return d
def P(k, x, y, r=50, at=0.1, disc=True): return {"k": k, "x": x, "y": y, "r": r, "at": at, "disc": disc}
def save(n, total):
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"long_{n}.json")
    cov = sorted(i for b in B for i in b["lines"])
    assert cov == list(range(total)), f"coverage problem: missing {sorted(set(range(total)) - set(cov))} dupes {[i for i in cov if cov.count(i) > 1][:5]}"
    json.dump(B, open(out, "w"), indent=0, ensure_ascii=False); print(len(B), "shots ->", out)

# ---------------------------------------------------------------------------------------------------
# split long shots into several cuts (one or two sentences each) and vary the framing between cuts.
# Times on a board are fractions of the shot (0..1) or "@n.f" (sentence n + fraction f). Inside a shot of
# n sentences a plain fraction t is treated as sentence position t*n.
import re as _re
def _u(t, n):
    if isinstance(t, str) and _re.fullmatch(r"@\d+(\.\d+)?", t): return float(t[1:])
    return float(t) * n
def _at(u):   # sentence position -> "@n.f"
    u = max(0.0, u); return "@%d.%03d" % (int(u), min(999, round((u - int(u)) * 1000)))
def _is_keys(v): return isinstance(v, list) and v and all(isinstance(k, list) and len(k) == 2 for k in v)
def _remap_keys(keys, n, s0, L):
    ks = [(_u(t, n), v) for t, v in keys]
    if all(isinstance(v, (int, float)) and not isinstance(v, bool) for _, v in ks):
        def val(u):
            if u <= ks[0][0]: return ks[0][1]
            for (u0, v0), (u1, v1) in zip(ks, ks[1:]):
                if u < u1: return v0 + (v1 - v0) * (u - u0) / max(1e-6, u1 - u0)
            return ks[-1][1]
        out = [[0, round(val(s0), 4)]] + [[_at(u - s0), v] for u, v in ks if s0 < u < s0 + L]
        ve = round(val(s0 + L), 4)
        if ve != out[-1][1]: out.append([_at(L - 0.001), ve])
        return out
    last = [v for u, v in ks if u <= s0 + 1e-6]; out = [[0, last[-1] if last else ks[0][1]]]
    out += [[_at(u - s0), v] for u, v in ks if s0 + 1e-6 < u < s0 + L]
    return out
def _scal(t, n, s0, L, before=-0.5):   # a one-off time ('at', 'from', 'drop'): None when it falls after this cut
    u = _u(t, n)
    if u >= s0 + L: return None
    return _at(u - s0) if u >= s0 else before
TRACK_KEYS = ("x", "pose", "expr", "alpha", "up", "rot", "yk", "facing", "open", "a", "dx", "upk", "bx", "bup", "level", "ghost", "tx", "lamp", "lever", "reach")
def _remap_obj(o, n, s0, L):
    o = dict(o)
    for k in TRACK_KEYS:
        if k in o and _is_keys(o[k]): o[k] = _remap_keys(o[k], n, s0, L)
    if "talk" in o and o["talk"]:
        a0, a1 = _u(o["talk"][0], n), _u(o["talk"][1], n); a0, a1 = max(a0, s0), min(a1, s0 + L)
        if a1 > a0: o["talk"] = [_at(a0 - s0), _at(a1 - s0) if a1 < s0 + L else 1]
        else: o.pop("talk")
    if "dribble" in o:
        a0, a1 = _u(o["dribble"][0], n), _u(o["dribble"][1], n); a0, a1 = max(a0, s0), min(a1, s0 + L)
        if a1 > a0: o["dribble"] = [_at(a0 - s0), _at(a1 - s0) if a1 < s0 + L else 1] + o["dribble"][2:]
        else: o.pop("dribble")
    if "at" in o and "id" not in o and isinstance(o["at"], (str, int, float)) and not isinstance(o["at"], bool):
        u = _u(o["at"], n); o["at"] = -1 if u < s0 else (9 if u >= s0 + L else _at(u - s0))
    if "spill" in o:
        u = _u(o["spill"], n); o["spill"] = 0 if u < s0 else (9 if u >= s0 + L else _at(u - s0))
    if "hold" in o and isinstance(o["hold"], dict):
        h = dict(o["hold"])
        if "from" in h:
            v = _scal(h["from"], n, s0, L, 0)
            if v is None: o.pop("hold"); h = None
            else: h["from"] = v
        if h is not None and "to" in h:
            if _u(h["to"], n) <= s0: o.pop("hold"); h = None
            else: v = _scal(h["to"], n, s0, L); h["to"] = 1 if v is None else v
        if h is not None and "drop" in h:
            u = _u(h["drop"], n)
            if u < s0: o.pop("hold"); h = None
            else: v = _scal(h["drop"], n, s0, L); h["drop"] = 2 if v is None else v
        if h is not None and "glow" in h:
            a0, a1 = _u(h["glow"][0], n), _u(h["glow"][1], n); a0, a1 = max(a0, s0), min(a1, s0 + L)
            if a1 > a0: h["glow"] = [_at(a0 - s0), _at(a1 - s0) if a1 < s0 + L else 1]
            else: h.pop("glow")
        if h is not None: o["hold"] = h
    if "enter" in o:
        if s0 > 0: o.pop("enter"); o.pop("enterUntil", None)
        else: o["enterUntil"] = min(0.9, o.get("enterUntil", 0.18) * n / L)
    if "exit" in o:
        u = o.get("exitFrom", 0.8) * n
        if u >= s0 + L: o.pop("exit"); o.pop("exitFrom", None)
        else: o["exitFrom"] = max(0.0, (u - s0) / L)
    return o
def _pop_list(lst, n, s0, L, key="at"):
    out = []
    for e in lst or []:
        e = dict(e); t = e.get(key, 0.1); u = _u(t, n)
        if u >= s0 + L: continue
        e[key] = -1 if u < s0 else _at(u - s0); out.append(e)
    return out
def split_board(b, chunks):
    n = len(b["lines"]); res = []; s0 = 0
    for L in chunks:
        c = {k: v for k, v in b.items()}
        c["lines"] = b["lines"][s0:s0 + L]
        c["actors"] = [_remap_obj(a, n, s0, L) for a in b["actors"]]
        c["items"] = [_remap_obj(i, n, s0, L) for i in b["items"]]
        if "extra" in b: c["extra"] = [_remap_obj(i, n, s0, L) for i in b["extra"]]
        for k in ("text", "props"):
            if k in b: c[k] = _pop_list(b[k], n, s0, L)
        for k in ("card", "thought", "inset"):
            if k in b:
                v = _pop_list([b[k]], n, s0, L)
                if v: c[k] = v[0]
                else: c.pop(k)
        if "cam" in b:
            cam = {}
            for k, v in b["cam"].items():
                if isinstance(v, list): a0, a1 = v; cam[k] = [round(a0 + (a1 - a0) * s0 / n, 3), round(a0 + (a1 - a0) * (s0 + L) / n, 3)]
                else: cam[k] = v
            c["cam"] = cam
        if s0 > 0:
            c.pop("sfx", None); c["fx"] = [f for f in (b.get("fx") or []) if f != "flash"]; c.pop("in", None)
        res.append(c); s0 += L
    return res
def plan_chunks(n, lens):
    """group n sentences into cuts of about 1-2 sentences (short sentences pair up)"""
    out, i = [], 0
    while i < n:
        if i + 1 < n and lens[i] + lens[i + 1] <= 9: out.append(2); i += 2
        else: out.append(1); i += 1
    if len(out) >= 2 and out[-1] == 1 and out[-2] == 1 and lens[-1] <= 3: out[-2:] = [2]
    return out

# ---- v3 pass used for videos 31-40: talkers change gesture each sentence, nobody paces aimlessly,
# long shots are cut into 1-2 sentence shots with varied framing (wide / medium on the speaker / alternate)
V3_VAR = {"relaxed": ["think", "crossArms", "shrug"], "think": ["relaxed", "crossArms"], "crossArms": ["think", "relaxed"], "sad": ["facepalm", "chest"], "nervous": ["handsOnHead", "think"],
          "talk": ["explain", "point"], "explain": ["talk", "point"], "worried": ["think", "handsOnHead"], "point": ["explain", "relaxed"], "shrug": ["relaxed", "think"]}
def _xs(a):
    v = a["x"]; return [k[1] for k in v] if isinstance(v, list) else [v]
def _frame(c, j):
    if j == 0 or c.get("tpl") or c["set"] in ("face", "space", "map") or "cam" in c or not c["actors"]: return
    acts = c["actors"]
    if any(a.get("up") or a.get("rot") or a.get("alpha") or a.get("clip") is not None or a.get("fly") for a in acts): return
    if len(c.get("text") or []) >= 2 or c.get("thought") or c.get("card"): return   # text-heavy shots keep the wide frame so the words never sit on a face
    f = ([a for a in acts if a.get("talk")] or [a for a in acts if a["id"] == "rio"] or acts)[0]; X = _xs(f)
    if not all(isinstance(v, (int, float)) for v in X) or max(X) - min(X) > 0.15: return
    xm = sum(X) / len(X)
    if j % 2 == 1: c["cam"] = {"z": [1.34, 1.42], "x": [max(-520, min(520, (xm - 0.5) * 1920))] * 2, "y": [-40, -40]}
    else: c["cam"] = {"z": [1.12, 1.16], "x": [max(-300, min(300, (xm - 0.5) * 960))] * 2, "y": [-10, -10]}
def v3_pass(n):
    import sys
    here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, "..", "..", "pipeline"))
    from build import split_sentences
    item = next(x for x in json.load(open(os.path.join(here, "..", "scripts.json")))["long"] if x["stt"] == n)
    lens = [len(x.split()) for x in split_sentences(item["script"])]
    for b in B:
        b.setdefault("actors", []); b.setdefault("items", []); b.setdefault("set", "home")
        if b.get("tpl") or b["set"] in ("face", "space"): continue
        m = len(b["lines"])
        for a in b["actors"]:
            a.pop("pace", None)
            poses = a["pose"]; p0 = poses[0][1]
            if len(poses) == 1 and p0 in V3_VAR and m > 1 and (a.get("talk") or len(b["actors"]) == 1) and not a.get("rot") and not a.get("up") and not a.get("hold") and not a.get("fly"):
                v = V3_VAR[p0]; a["pose"] = [[0, p0]] + [[f"@{i}", v[(i - 1) % len(v)] if i % 2 else p0] for i in range(1, m)]
    NB = []
    for b in B:
        m = len(b["lines"])
        if m < 2 or b.get("tpl") or b["set"] == "face": NB.append(b); continue
        ch = plan_chunks(m, [lens[i] for i in b["lines"]])
        if len(ch) == 1: NB.append(b); continue
        parts = split_board(b, ch)
        empty = lambda c: not c["actors"] and not c.get("items") and not c.get("card") and not c.get("text") and not c.get("props") and not c.get("thought") and not c.get("inset")
        if any(empty(c) for c in parts): NB.append(b); continue   # never cut to an empty frame
        for j, c in enumerate(parts): _frame(c, j); NB.append(c)
    B[:] = NB
