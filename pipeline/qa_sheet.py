# render 1 still per shot at fraction F (default 0.6) and tile 5x5 sheets with shot numbers, for full-video QA
import json, subprocess, sys, os, glob
P, F = sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 0.6
shots = json.load(open(f"studio/projects/{P}/story/shots.json"))["shots"]
d = f"studio/projects/{P}/build/stills"; [os.remove(f) for f in glob.glob(d + "/*")] if os.path.isdir(d) else None
ts = [round(s["start"] + (s["end"] - s["start"]) * F, 2) for s in shots]
subprocess.run(["node", "render.mjs", "--project", f"projects/{P}", "--stills", ",".join(map(str, ts)), "--format", "jpeg"], cwd="studio", check=True, capture_output=True)
fs = sorted(glob.glob(d + "/*.jpeg"), key=lambda f: float(os.path.basename(f).split("s_")[0]))
os.makedirs("/tmp/qa", exist_ok=True)
for k in range(0, len(fs), 25):
    grp = fs[k:k + 25]; args = []
    for f in grp: args += ["-i", f]
    flt = "".join(f"[{i}:v]scale=480:270,drawtext=text='{k + i + 1}':x=8:y=8:fontsize=34:fontcolor=yellow:box=1:boxcolor=black@0.6[v{i}];" for i in range(len(grp)))
    flt += "".join(f"[v{i}]" for i in range(len(grp))) + f"xstack=inputs={len(grp)}:layout=" + "|".join(f"{(i % 5) * 480}_{(i // 5) * 270}" for i in range(len(grp))) + ":fill=black"
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args, "-filter_complex", flt, f"/tmp/qa/{P}_{k // 25 + 1}.jpg"], check=True)
print(len(fs), "stills ->", sorted(glob.glob(f"/tmp/qa/{P}_*.jpg")))
