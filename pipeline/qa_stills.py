# QA: render 3 stills per shot (15%, 50%, 85%) and tile them, one row per shot, so every shot can be checked before a full render.
import json, subprocess, sys, os
P = sys.argv[1]; shots = json.load(open(f"studio/projects/{P}/story/shots.json"))["shots"]
ts = [round(s["start"] + (s["end"] - s["start"]) * f, 2) for s in shots for f in (0.15, 0.5, 0.85)]
subprocess.run(["node", "render.mjs", "--project", f"projects/{P}", "--stills", ",".join(map(str, ts)), "--format", "jpeg"], cwd="studio", check=True, capture_output=True)
d = f"studio/projects/{P}/build/stills"; print(len(ts), "stills in", d)
