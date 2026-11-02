"""pipeline/collect.py - build one YouTube info file per big folder from the per-video info_*.txt pieces.

  python pipeline/collect.py --src meta_dl --out collected
Writes collected/<tag>/00_THONG_TIN_DANG_YOUTUBE.txt for every group in pipeline/groups.json.
"""
import argparse, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser(); ap.add_argument("--src", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
groups = json.load(open(os.path.join(ROOT, "pipeline", "groups.json")))
jobs = json.load(open(os.path.join(ROOT, "pipeline", "jobs.json")))
for tag, gname in groups:
    js = sorted([j for j in jobs if j["tag"] == tag], key=lambda j: j["n"])
    parts, missing = [], []
    for j in js:
        f = os.path.join(a.src, f"info_{j['kind']}_{j['n']:02d}.txt")
        if os.path.exists(f): parts.append(open(f, encoding="utf-8").read())
        else: missing.append(j["name"])
    kind = "VIDEO DAI (16:9)" if js[0]["kind"] == "long" else "SHORTS (9:16)"
    head = (f"RIO ANIMATION - BO 2 - THONG TIN DANG YOUTUBE\nThu muc: {gname} - {kind}\n"
            f"Gom {len(parts)}/{len(js)} video. Moi muc ben duoi: tieu de, mo ta (co chapters voi video dai), tags, hashtags, cai dat, ten anh bia, so lieu nen kiem tra.\n")
    if missing: head += "CHUA CO (dang render hoac loi): " + ", ".join(missing) + "\n"
    head += "\n" + "=" * 70 + "\n\n"
    os.makedirs(os.path.join(a.out, tag), exist_ok=True)
    open(os.path.join(a.out, tag, "00_THONG_TIN_DANG_YOUTUBE.txt"), "w", encoding="utf-8").write(head + "".join(parts))
    print(tag, gname, len(parts), "/", len(js), "missing", len(missing))
