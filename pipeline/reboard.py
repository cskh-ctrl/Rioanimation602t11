# Re-apply data/direction/<slug>.json to an already-voiced project (no new TTS) and refresh scenes code.
import json, sys, os, re, shutil
slug = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(HERE, '..', 'studio', 'projects', slug)
sinfo = json.load(open(P + '/timeline/sentences.json')); story = json.load(open(P + '/story/shots.json')); total = story['duration']
src = open(os.path.join(HERE, 'build.py')).read(); i0 = src.index('    dpath = os.path.join(ROOT, "data", "direction"'); i1 = src.index('    shots[-1]["end"] = total')
ns = {'os': os, 'json': json, 're': re, 'ROOT': os.path.abspath(os.path.join(HERE, '..')), 'slug': slug, 'sinfo': sinfo, 'total': total, 'shots': []}
exec('def _f():\n' + src[i0:i1] + '    return shots\n', ns); shots = ns['_f']()
shots[-1]['end'] = total; story['shots'] = shots; json.dump(story, open(P + '/story/shots.json', 'w'), indent=1, ensure_ascii=False)
shutil.rmtree(P + '/scenes'); shutil.copytree(os.path.join(HERE, 'scenes'), P + '/scenes'); print(slug, len(shots), 'shots')
