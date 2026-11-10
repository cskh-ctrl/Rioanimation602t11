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
