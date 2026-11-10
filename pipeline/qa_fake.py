# Build a QA-only project with estimated sentence timing (no TTS) so a storyboard can be checked before the cloud render.
import json, sys, os, re, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
n = int(sys.argv[1]); slug = f"long_{n}"; P = os.path.join(ROOT, 'studio', 'projects', slug + '_qa')
sys.path.insert(0, HERE); from build import split_sentences
item = next(x for x in json.load(open(os.path.join(ROOT, 'data', 'scripts.json')))['long'] if x['stt'] == n)
sents = split_sentences(item['script']); t = 0.25; sinfo = []
for s in sents:
    d = len(s.split()) / 2.6 + 0.15; sinfo.append({"text": s, "start": round(t, 3), "end": round(t + d, 3)}); t += d + 0.32
total = round(t + 0.5, 3)
for d in ('timeline', 'story', 'scenes', 'build', 'out', 'input'): os.makedirs(os.path.join(P, d), exist_ok=True)
json.dump(sinfo, open(P + '/timeline/sentences.json', 'w')); json.dump({"words": []}, open(P + '/timeline/words.json', 'w'))
cfg = json.load(open(os.path.join(ROOT, 'studio', 'projects', 'long_31', 'config.json')))
cfg.update({"title": item['title'], "duration": total, "captions": False, "n": n, "voiceover": None, "music": {"enabled": False}, "sfx": {"enabled": False}})
json.dump(cfg, open(P + '/config.json', 'w'), indent=1)
json.dump({"title": item['title'], "duration": total, "shots": [{"id": "s001", "start": 0, "end": total, "line": "", "scene": "end", "set": "home", "in": {"type": "cut"}, "sfx": [], "params": {"tpl": "end"}}], "music": []}, open(P + '/story/shots.json', 'w'))
src = open(os.path.join(HERE, 'build.py')).read(); i0 = src.index('    dpath = os.path.join(ROOT, "data", "direction"'); i1 = src.index('    shots[-1]["end"] = total')
ns = {'os': os, 'json': json, 're': re, 'ROOT': ROOT, 'slug': slug, 'sinfo': sinfo, 'total': total, 'shots': []}
exec('def _f():\n' + src[i0:i1] + '    return shots\n', ns); shots = ns['_f'](); shots[-1]['end'] = total
json.dump({"title": item['title'], "duration": total, "shots": shots, "music": []}, open(P + '/story/shots.json', 'w'), indent=1)
shutil.rmtree(P + '/scenes'); shutil.copytree(os.path.join(HERE, 'scenes'), P + '/scenes'); print(slug + '_qa', len(shots), 'shots', round(total / 60, 1), 'min')
