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
TRACK_KEYS = ("x", "pose", "expr", "alpha", "up", "rot", "yk", "facing", "open", "a", "dx", "upk", "bx", "bup", "level")
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
