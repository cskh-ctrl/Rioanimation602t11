# QA a chosen list of shot numbers (1-based) at 2 moments each, tiled 4 wide
import json, subprocess, sys, os, glob
P = sys.argv[1]; nums = [int(x) for x in sys.argv[2].split(',')]; fr = [float(x) for x in (sys.argv[3] if len(sys.argv) > 3 else '0.3,0.8').split(',')]
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
shots = json.load(open(f"{R}/studio/projects/{P}/story/shots.json"))["shots"]
d = f"{R}/studio/projects/{P}/build/stills"; [os.remove(f) for f in glob.glob(d + "/*")] if os.path.isdir(d) else None
ts = [round(shots[n - 1]["start"] + (shots[n - 1]["end"] - shots[n - 1]["start"]) * f, 2) for n in nums for f in fr]
subprocess.run(["node", "render.mjs", "--project", f"projects/{P}", "--stills", ",".join(map(str, ts)), "--format", "jpeg"], cwd=f"{R}/studio", check=True, capture_output=True)
fs = sorted(glob.glob(d + "/*.jpeg"), key=lambda f: float(os.path.basename(f).split("s_")[0]))
lab = [f"{n}" for n in nums for f in fr]; args = []
for f in fs: args += ["-i", f]
flt = "".join(f"[{i}:v]scale=600:338,drawtext=text='{lab[i]}':x=8:y=8:fontsize=34:fontcolor=yellow:box=1:boxcolor=black@0.6[v{i}];" for i in range(len(fs)))
flt += "".join(f"[v{i}]" for i in range(len(fs))) + f"xstack=inputs={len(fs)}:layout=" + "|".join(f"{(i % 4) * 600}_{(i // 4) * 338}" for i in range(len(fs))) + ":fill=black"
subprocess.run(["ffmpeg", "-v", "error", "-y", *args, "-filter_complex", flt, f"/tmp/qa/{P}_pick.jpg"], check=True); print(f"/tmp/qa/{P}_pick.jpg")
