# Storyboard long_32 "What If You Could Change The Whole World With Just One Phone Call?"
from sb import *
def door(x, **kw): d = {"k": "housedoor", "x": x}; d.update(kw); return d
BOOTH = [{"k": "booth", "x": 0.6}, {"k": "booth", "x": 0.6, "part": "front", "front": True}]
def booth_rio(pose="phoneEar", expr="neutral", **kw): return A("rio", 0.6, pose, expr, hold={"k": "phone"}, **kw)
APT = dict(wall="#c8b0a0", wall2="#7a6070", room={"frames": 260, "window": 1250})

S([0, 1, 2], "street", [booth_rio("phoneEar", [[0, "smile"], ["@1", "smirk"], ["@2", "awe"]], talk=["@1", "@1.9"])], BOOTH, fx=[], cam={"z": [1.3, 1.1]}, sfx=[{"at": 2.5, "name": "shimmer", "gain": -12}])
S([3, 4], "park", [A("zoe", 0.3, "relaxed", "surprised"), A("rio", 0.45, "relaxed", "nervous")], [prop("dog", 0.7, 0.6)], fx=["greensky"], text=[T("GREEN SKY?", 0.5, 0.15, 0.05), T("\"WOOF... HELLO\"", 0.72, 0.4, "@1", size=46)])
S([5, 6], "park", [A("zoe", 0.3, [[0, "holdCup"], ["@0.4", "drop"]], "shocked", hold={"k": "cup", "drop": "@0.4"}, talk=["@1", 1]), A("rio", 0.45, "nervous", "nervous")], [], props=[P("bird", 0.62, 0.15, 40, "@1"), P("letter", 0.66, 0.17, 30, "@1")], text=[T("THE MAILMAN?!", 0.65, 0.3, "@1")])
S([7, 8], "street", [booth_rio("phoneEar", [[0, "shocked"], ["@1", "nervous"]])], BOOTH, text=[T("NOT THAT ONE.", at="@1")])
S([9, 10, 11], "studio", [A("rio", 0.5, "talk", "smile", hold={"k": "phone", "to": 0}, talk=[0, 1])], [{"k": "stage", "x": 0.5, "w": 3}], props=[P("mic", 0.56, 0.5, 30, 0)], card=card("RIO", "stand-up comedian... a small one", at="@1", y=0.15, w=760))
S([12, 13], "cafe", [A("rio", 0.5, "talk", "nervous", talk=[0, 1]), A("crowd1", 0.25, "sit", "sleepy", zzz=True), A("crowd2", 0.78, "sit", "sleepy", facing=-1, zzz=True), A("sam", 0.65, "sit", "neutral", facing=-1)], [], card=card("9 PEOPLE", "2 asleep", at=0.05, y=0.14))
S([14, 15], "street", [A("rio", [[0, 0.2], [0.6, 0.45]], "relaxed", [[0, "sad"], ["@1", "surprised"]])], BOOTH, fx=["night"])
S([16, 17], "street", [A("rio", 0.5, "reach", "thinking")], BOOTH + [{"k": "paper", "x": 0.6, "up": 1.5, "s": "SAY WHAT IF..."}], fx=["night"], cam={"z": [1.4, 1.5], "x": [80, 100], "y": [-80, -80]})
S([18, 19], "street", [booth_rio("phoneEar", "thinking")], BOOTH, fx=["night"], text=[T("SAY \"WHAT IF\"", 0.5, 0.15, 0.05), T("THEN SAY ANYTHING", 0.5, 0.25, "@1")])
S([20, 21, 22], "office", [A("crowd1", 0.3, "type", "sleepy"), A("crowd2", 0.62, "type", "sad")], [{"k": "desk", "x": 0.34}, {"k": "desk", "x": 0.66}], card=card("YEARS", "sometimes decades", at="@1"))
S([23, 24], "street", [booth_rio("phoneEar", "smirk")], BOOTH, card=card("ONE CALL", None, at=0.05, x=0.25))
S([25, 26], "street", [booth_rio("phoneEar", "thinking")], BOOTH, card=card("ONE RULE", "one change at a time", at="@1", x=0.28, w=640))
S([27], "street", [booth_rio("phoneEar", "nervous")], BOOTH, card=card("NEW CALL = OLD CHANGE GONE", "forever", x=0.32, w=820, size=56))
S([28, 29, 30], "city", [A("crowd1", 0.25, "relaxed", "neutral"), A("crowd2", 0.4, "relaxed", "neutral"), A("rio", 0.6, "think", [[0, "neutral"], ["@2", "awe"]]), A("sam", 0.8, "relaxed", "neutral", facing=-1)], [], text=[T("EVERYONE FORGETS", 0.5, 0.15, "@1"), T("EXCEPT YOU", 0.5, 0.25, "@2", color="#ff8a5a")])
S([31], "room", [], [], tpl="title", params={"title": "What If One Call Could Change The World?"})
S([32, 33, 34], "street", [booth_rio("phoneEar", [[0, "smile"], ["@2", "happy"]], talk=["@2", "@2.7"])], BOOTH, card=card("CALL 1", "\"what if it never rained on my street?\"", at=0.05, x=0.3, w=760, size=60))
S([35, 36, 37], "park", [A("crowd1", 0.42, [[0, "holdCup"], ["@1", "sip"], ["@1.5", "holdCup"]], "happy", hold={"k": "cup"}), A("zoe", 0.72, "talk", "smile", facing=-1, talk=["@0.3", "@1.6"]), A("crowd2", 0.82, [[0, "relaxed"], ["@1", "cheer"]], "happy", facing=-1), A("rio", [[0, 0.12], ["@0.9", 0.3]], [[0, "carry"], ["@1", "relaxed"]], "joy", walkArms=True)], [{"k": "table", "x": 0.58, "w": 1.6}, {"k": "dish", "x": 0.54, "food": "pizza", "at": -1}, {"k": "dish", "x": 0.62, "food": "taco", "at": -1}, {"k": "dish", "x": 0.31, "food": "cake", "at": "@0.95"}], mood="day", props=[P("sun", 0.85, 0.12, 60, 0), P("balloon", 0.2, 0.22, 40, 0.05)], text=[T("WHAT COULD GO WRONG?", 0.5, 0.15, "@2", size=56)])
S([38, 39, 40], "park", [A("rio", [[0, 0.1], ["@0.8", 0.4], ["@2", 0.4], ["@2.3", 0.52]], [[0, "relaxed"], ["@1", "sad"], ["@2.4", "kneel"]], [[0, "neutral"], ["@0.7", "nervous"], ["@2", "sad"]])], [prop("tree", 0.2, 3.0), prop("tree", 0.75, 3.0), prop("flower", 0.6, 0.5, rot=[[0, 0], [1, 0.9]])], mood="desert", fx=[], card=card("2 WEEKS LATER", None, at=0.05, y=0.14), text=[T("THE LAWNS CRACK", 0.5, 0.3, "@1", size=50)])
S([41, 42], "desert", [A("rio", 0.45, "sad", "sad")], [prop("tree", 0.7, 3.0)], card=card("100s OF LITERS", "a tree can drink on a hot day", at=0.05, w=760), text=[T("A TINY DESERT", 0.5, 0.36, "@1", size=56)])
S([43, 44, 45], "park", [A("zoe", 0.36, [[0, "kneel"], ["@1", "think"], ["@1.4", "explain"]], [[0, "confused"], ["@1", "confused"]], facing=[[0, -1], ["@1", 1]], talk=["@1", "@1.95"]), A("rio", 0.6, [[0, "relaxed"], ["@2", "crossArms"]], [[0, "nervous"], ["@2", "smirk"]], facing=[[0, -1], ["@2", 1]])], [prop("flower", 0.3, 0.5, rot=0.9)], mood="desert", text=[T("~ whistle ~", 0.72, 0.3, "@2", size=46)])
S([46, 47, 48], "street", [booth_rio("phoneEar", "determined", talk=["@2", 1])], BOOTH, card=card("CALL 2", "\"what if everyone spoke the same language?\"", at=0.05, x=0.3, w=800, size=60))
S([49, 50, 51, 52, 53], "home", [A("rio", 0.7, [[0, "phone"], ["@0.8", "remote"]], [[0, "neutral"], ["@2", "surprised"], ["@4", "shocked"]], facing=-1, hold={"k": "remote", "from": "@0.8"})], [{"k": "tvset", "x": 0.33, "on": "@1.1", "show": "news", "who": "crowd2", "s": "EVERY COUNTRY NOW SPEAKS ONE LANGUAGE"}], text=[T("EVERY WORD... ENGLISH", 0.5, 0.15, "@4", size=54)])
S([54, 55], "city", [A("rio", [[0, 0.08], ["@0.9", 0.4]], [[0, "relaxed"], ["@1.1", "talk"]], "smile", hold={"k": "suitcase"}, talk=["@1", "@1.5"]), A("crowd1", 0.55, [[0, "relaxed"], ["@1.4", "point"]], "happy", facing=-1, talk=["@1.4", 1])], [], props=[P("plane", 0.8, 0.15, 50, "@1")], text=[T("IS THAT SO BAD?", 0.5, 0.3, 0.05, size=56), T("TRAVEL IS EASY", 0.5, 0.15, "@1", size=50)])
S([56], "office", [A("investor", 0.455, [[0, "relaxed"], [0.25, "shake"]], "happy"), A("crowd2", 0.545, [[0, "relaxed"], [0.25, "shake"]], "happy", facing=-1)], [{"k": "desk", "x": 0.8}], text=[T("BUSINESS IS EASY", 0.5, 0.18, 0.1, size=56)])
S([57, 58, 59], "home", [A("rio", 0.35, "talk", "smile", talk=["@1", 1]), A("grandma", 0.6, "sit", "smile", facing=-1)], [], props=[P("note", 0.48, 0.3, 40, "@1"), P("baby", 0.7, 0.18, 40, "@2")], text=[T("THE OLD SPANISH LULLABY", 0.5, 0.12, "@2", size=46)])
S([60, 61], "home", [A("rio", 0.35, "relaxed", "worried"), A("grandma", 0.6, "sit", "confused", facing=-1, talk=["@1", 1])], [], text=[T("\"WHAT SONG, MIJO?\"", 0.6, 0.22, "@1", size=54)])
S([62, 63], "space", [], [], props=[P("earth", 0.5, 0.52, 190, 0, False)], card=card("~7,000 LANGUAGES", "songs, jokes, words found nowhere else", at=0.05, w=860, y=0.15))
S([64, 65, 66], "home", [A("rio", 0.45, [[0, "sad"], ["@2", "chest"]], "sad")], [], cam={"z": [1.3, 1.45], "y": [-60, -60]}, text=[T("ALL GONE", 0.5, 0.15, 0.05), T("ONLY YOU REMEMBER", 0.5, 0.25, "@1", size=50)])
S([67, 68, 69], "street", [booth_rio("phoneEar", [[0, "determined"], ["@2", "smile"]], talk=["@2", "@2.6"])], BOOTH, card=card("CALL 3", "\"what if mosquitoes disappeared?\"", at=0.05, x=0.3, w=760, size=60))
S([70, 71], "park", [A("rio", 0.4, "sitBack", "happy"), A("zoe", 0.6, "sitBack", "smile", facing=-1)], [], mood="dusk", thought={"props": ["bee"], "x": 0.5, "y": 0.25, "at": 0.05, "cross": True}, text=[T("NO BUZZING", 0.5, 0.45, "@1", size=50)])
S([72, 73, 74], "hospital", [A("nurse", 0.6, "relaxed", "smile", facing=-1), A("kid", 0.4, "relaxed", "smile")], [], card=card("~600,000", "malaria deaths in 2022... most of them young children", at="@1", w=880, y=0.15))
S([75, 76], "hospital", [A("kid", 0.4, "cheer", "joy"), A("rio", 0.6, "relaxed", "cry", facing=-1)], [], text=[T("FALLING TO ZERO", 0.5, 0.15, 0.05)])
S([77, 78, 79], "home", [A("rio", 0.7, "remote", [[0, "worried"], ["@1", "thinking"]], facing=-1, hold={"k": "remote"})], [{"k": "tvset", "x": 0.33, "show": "news", "who": "doctor", "expr": "worried", "s": "MOSQUITO EXPERTS WARN"}], card=card("~3,500 KINDS", "only a few bite humans", at="@1", x=0.5, y=0.15, w=640))
S([80, 81], "lake", [], [prop("fish", 0.3, 0.5), prop("bird", 0.6, 0.4, up=1.5), prop("flower", 0.8, 0.5)], text=[T("FOOD FOR BIRDS, FROGS AND FISH", 0.5, 0.15, 0.05, size=50), T("SOME EVEN POLLINATE FLOWERS", 0.5, 0.25, "@1", size=46)])
S([82, 83, 84], "home", [A("rio", 0.45, [[0, "think"], ["@2", "crossArms"]], [[0, "thinking"], ["@2", "scared"]])], [], text=[T("MIRACLE?", 0.3, 0.2, 0.05), T("OR A HOLE IN NATURE?", 0.62, 0.3, 0.4, size=50)])
S([85, 86, 87], "street", [booth_rio("phoneEar", [[0, "smirk"], ["@2", "happy"]], talk=["@2", "@2.6"])], BOOTH, card=card("CALL 4", "\"what if gravity were half as strong?\"", at=0.05, x=0.3, w=760, size=60))
S([88], "park", [A("rio", 0.45, "jump", "joy", up=[[0, 0], [0.5, 1.0], [1, 0]])], [], mood="day", card=card("2x HIGHER", None, at=0.3, x=0.75))
S([89], "gym", [A("kid", [[0, 0.22], [0.32, 0.42], [0.62, 0.557], [0.95, 0.6]], [[0, "dribble"], [0.32, "dunk"], [0.85, "cheer"]], "joy", walkArms=True, lockFacing=True, up=[[0, 0], [0.32, 0], [0.62, 1.65], [0.88, 0]]), A("boy", 0.2, [[0, "relaxed"], [0.6, "cheer"]], [[0, "smile"], [0.6, "joy"]])], [{"k": "hoop", "x": 0.62, "dir": -1}, {"k": "bball", "x": 0.25, "bx": [[0, 0.246], [0.32, 0.446], [0.62, 0.578], [0.7, 0.578], [0.9, 0.59]], "bup": [[0, 0], [0.32, 1.1], [0.62, 3.25], [0.7, 2.75], [0.9, 0]], "dribble": [0, 0.3, 0.75]}], cam={"z": 1.12, "x": -100, "y": -70})
S([90], "park", [A("oldman", 0.5, [[0, "relaxed"], [0.15, "tuck"], [0.8, "cheer"]], "joy", up=[[0, 0], [0.15, 0], [0.45, 1.4], [0.75, 0]], rot=[[0, 0], [0.15, 0], [0.75, -6.283]]), A("oldwoman", 0.28, [[0, "relaxed"], [0.75, "cheer"]], [[0, "surprised"], [0.75, "joy"]]), A("crowd2", 0.75, [[0, "relaxed"], [0.75, "cheer"]], "surprised", facing=-1)], [], mood="day", follow=False, cam={"z": 0.9, "y": -80})
S([91], "kitchen", [A("rio", 0.4, "sitTable", [[0, "neutral"], [0.3, "shocked"]])], [{"k": "table", "x": 0.52, "w": 1.2}, {"k": "cereal", "x": 0.445, "spill": 0.25}], cam={"z": [1.6, 1.75], "x": [-115, -115], "y": [140, 150]}, text=[T("SLOW MOTION", 0.5, 0.15, 0.05)])
S([92, 93, 94], "space", [], [], props=[P("astronaut", 0.35, 0.5, 110, 0), P("bone", 0.68, 0.5, 80, "@1")], card=card("-1% BONE MASS", "per month for astronauts in space", at="@1", w=760, y=0.15))
S([95, 96, 97, 98], "hospital", [A("oldwoman", 0.25, "lie", "sad", rot=-1.5708, dy=41), A("zoe", [[0, 0.36], ["@1.5", 0.36], ["@2", 0.5]], [[0, "relaxed"], ["@2", "explain"]], [[0, "neutral"], ["@1", "worried"]], facing=[[0, -1], ["@1.9", 1]], talk=["@2", 1]), A("rio", [[0, 0.85], ["@1.6", 0.64]], "relaxed", "nervous", facing=-1)], [{"k": "bed", "x": 0.25}], card=card("3 BROKEN HIPS", "this week", at="@2", y=0.15))
S([99], "street", [A("rio", [[0, 0.3], [1, 0.6]], "relaxed", "determined")], BOOTH, fx=["night"])
S([100, 101], "street", [booth_rio("phoneEar", "determined", talk=["@1", "@1.7"])], BOOTH, fx=["night"], card=card("CALL 5", "\"what if nobody ever needed sleep?\"", at=0.05, x=0.3, w=760, size=60))
S([102, 103], "home", [A("rio", 0.6, "sitBack", "happy", facing=-1), A("zoe", 0.74, "sitBack", "happy", facing=-1)], [{"k": "tvset", "x": 0.28, "show": "movie", "bg": "#1a1a2a"}], props=[P("clock", 0.5, 0.15, 40, "@1")], fx=["night"], card=card("24 HOURS AWAKE", "movies at 4 AM", at=0.05, y=0.14))
S([104, 105], "cafe", [A("crowd1", [[0, 0.32], [0.35, 0.44]], [[0, "relaxed"], [0.38, "reach"], ["@1", "shrug"]], "smirk")], [{"k": "sign", "x": 0.5, "y": 0.4, "s": "CLOSED"}], text=[T("WHO NEEDS COFFEE?", 0.5, 0.15, "@1", size=56)])
S([106, 107, 108, 109], "home", [], [], tpl="science", params={"sci": "SLEEP CLEANS", "icon": "brain"})
S([110, 111, 112], "kitchen", [A("rio", 0.3, [[0, "relaxed"], ["@1", "present"]], [[0, "smile"], ["@1.5", "sad"]]), A("zoe", [[0, 0.95], ["@0.7", 0.62], ["@1.4", 0.45], ["@2.6", 0.05]], [[0, "phone"]], "sleepy", hold={"k": "phone"}, facing=-1, lockFacing=False)], [{"k": "table", "x": 0.42, "w": 1.0}, {"k": "dish", "x": 0.42, "food": "cake", "at": -1}], text=[T("CRANKY. FORGETFUL.", 0.5, 0.15, 0.05, size=56)])
S([113, 114, 115], "home", [A("rio", 0.45, "think", "thinking")], [], props=[P("letter", 0.6, 0.35, 60, "@1")], text=[T("EVERY WISH HAS A PRICE TAG", 0.5, 0.15, "@1", size=52)])
S([116, 117], "home", [A("rio", 0.7, "lie", "neutral", rot=-1.5708, dy=38)], [], fx=["night"])
S([118, 119, 120], "street", [booth_rio("phoneEar", [[0, "smirk"], ["@2", "smirk"]], talk=["@2", "@2.8"])], BOOTH, fx=["night"], card=card("CALL 6", "\"what if I were the most famous person on Earth?\"", at="@2", x=0.3, w=880, size=60))
S([121, 122], "rooftop", [A("rio", 0.3, [[0, "cheer"], ["@1", "point"]], "awe")], [{"k": "billboard", "x": 0.72, "sc": 0.55, "up": 3}], text=[T("PENTHOUSE", 0.3, 0.15, 0.05)])
S([123], "kitchen", [A("rio", 0.44, [[0, "relaxed"], [0.35, "point"]], [[0, "neutral"], [0.35, "shocked"]])], [{"k": "table", "x": 0.55, "w": 1.0}, {"k": "cerealbox", "x": 0.55, "on": 0.75}], cam={"z": [1.4, 1.6], "x": [80, 90], "y": [60, 60]})
S([124], "rooftop", [A("rio", 0.45, "phone", "joy", hold={"k": "phone"})], [], props=[P("heart", 0.62, 0.42, 40, 0.2)], card=card("400,000,000", "followers", at=0.15, x=0.7, y=0.2, w=640))
S([125, 126], "stadium", [A("rio", [[0, 0.3], ["@0.6", 0.5]], [[0, "relaxed"], ["@0.7", "cheer"], ["@1", "talk"]], "joy", talk=["@1", 1])], [], props=[P("mic", 0.56, 0.5, 30, "@1")], text=[T("SOLD OUT", 0.5, 0.15, 0.05), T("HA HA HA", 0.5, 0.3, "@1.5", size=60)])
S([127, 128], "rooftop", [A("rio", 0.45, [[0, "cheer"], ["@1", "relaxed"]], [[0, "joy"], ["@1", "thinking"]])], [], text=[T("RIGHT?", 0.55, 0.2, "@1")])
S([129, 130], "rooftop", [A("rio", 0.45, "think", "worried")], [], cam={"z": [1.3, 1.45], "y": [-60, -60]})
S([131, 132], "hospital", [A("zoe", [[0, 0.1], ["@1.6", 0.6]], [[0, "relaxed"], ["@1.7", "explain"]], "determined", talk=["@1.7", 1]), A("oldman", 0.78, "lie", "sad", rot=-1.5708, dy=41)], [{"k": "bed", "x": 0.78}], card=card("12-HOUR SHIFTS", "in the emergency room", at="@1", y=0.15))
S([133, 134], "kitchen", [A("zoe", [[0, 0.88], [0.5, 0.55]], [[0, "relaxed"], [0.6, "sad"]], "sleepy", facing=-1)], [door(0.9)], text=[T("TIRED. HAIR A MESS.", 0.5, 0.15, 0.05, size=56)])
S([135, 136, 137, 138], "kitchen", [A("zoe", 0.553, "stir", "happy", hold={"k": "spoon"}, talk=[0, 1]), A("rio", 0.22, [[0, "sitTable"], ["@3", "facepalm"]], [[0, "neutral"], ["@3", "smirk"]])], [{"k": "stove", "x": 0.59}, {"k": "table", "x": 0.3, "w": 1.0}], props=[P("note", 0.62, 0.3, 40, 0.1), P("note", 0.68, 0.24, 30, 0.3)], text=[T("STAYIN' ALIVE...", 0.6, 0.15, "@1", size=56), T("OVER AND OVER", 0.6, 0.25, "@2", size=46)])
S([139, 140, 141], "kitchen", [A("rio", [[0, 0.22], ["@0.7", 0.42]], [[0, "relaxed"], ["@0.8", "talk"]], "confused", talk=["@0.4", "@0.95"]), A("zoe", 0.553, [[0, "stir"], ["@1", "cheer"], ["@2", "explain"]], "happy", hold={"k": "spoon"}, facing=[[0, 1], ["@0.9", -1]], talk=["@1", 1])], [{"k": "stove", "x": 0.59}], text=[T("\"IT'S THE BEAT FOR CPR\"", 0.5, 0.18, "@2", size=54)])
S([142, 143], "kitchen", [], [], card=card("~104 BEATS / MIN", "the tempo of Stayin' Alive", at=0.05, w=760), props=[P("heart", 0.5, 0.58, 90, "@1")])
S([144, 145, 146], "kitchen", [A("rio", 0.43, "relaxed", [[0, "surprised"], ["@1", "nervous"]], talk=["@1", "@1.9"]), A("zoe", 0.49, [[0, "relaxed"], [0.1, "tap"]], "determined", facing=-1, talk=["@2", 1])], [{"k": "stove", "x": 0.75}], cam={"z": [1.35, 1.45], "y": [-60, -60], "x": [-20, -20]}, text=[T("HARD AND FAST", 0.5, 0.18, "@2")])
S([147, 148, 149], "kitchen", [], [], card=card("5 CM DEEP", "100-120 pushes per minute", at=0.05, w=720), props=[P("heart", 0.5, 0.58, 80, 0.2)])
S([150, 151], "kitchen", [A("rio", 0.42, "shrug", "smirk", talk=["@1", 1]), A("zoe", 0.56, "crossArms", "smile", facing=-1)], [])
S([152, 153, 154], "office", [A("zoe", 0.5, [[0, "crossArms"], ["@2", "explain"]], "smirk", who="zoeRich")], [{"k": "desk", "x": 0.72}], card=card("MANAGER", "a big office", at="@1", y=0.14))
S([155], "street", [A("zoe", [[0, 0.9], [0.6, 0.7]], [[0, "relaxed"], [0.65, "phone"]], "smirk", who="zoeRich", facing=-1, hold={"k": "phone", "from": 0.65})], [{"k": "car", "x": 0.38, "color": "#c8a040", "a": 1}], text=[T("A SHINY CAR", 0.5, 0.15, 0.1)])
S([156], "office", [A("zoe", 0.5, "crossArms", "smirk", who="zoeRich")], [{"k": "desk", "x": 0.72}], cam={"z": [1.5, 1.6], "y": [-90, -90]}, text=[T("SUNGLASSES INDOORS", 0.5, 0.15, 0.1, size=52)])
S([157], "office", [A("zoe", 0.5, "crossArms", "neutral", who="zoeRich")], [{"k": "desk", "x": 0.72}], thought={"props": ["note"], "x": 0.3, "y": 0.25, "at": 0.1, "cross": True}, cam={"z": [1.3, 1.4], "y": [-60, -60]})
S([158, 159, 160, 161], "office", [A("rio", 0.38, "explain", "worried", talk=[0, "@0.9"]), A("zoe", 0.58, "crossArms", "smile", who="zoeRich", facing=-1, talk=["@2", 1])], [{"k": "desk", "x": 0.8}], text=[T("\"WHO WOULD WANT THAT JOB?\"", 0.5, 0.18, "@3", size=50)])
S([162, 163], "office", [A("rio", 0.42, "sad", "sad")], [{"k": "desk", "x": 0.8}], cam={"z": [1.35, 1.5], "y": [-60, -60]}, text=[T("WHAT HAVE YOU DONE?", 0.5, 0.18, "@1", size=56)])
S([164, 165, 166], "hospital", [A("nurse", 0.5, "relaxed", "smile", alpha=[[0, 1], [0.7, 0]])], [], text=[T("YOU WISHED HER AWAY", 0.5, 0.18, "@1", size=56)])
S([167, 168, 169, 170], "stadium", [A("rio", 0.5, "cheer", "smile")], [], card=card("80,000 FANS", "live in 40 countries", at="@1", y=0.14))
S([171, 172], "room", [A("rio", 0.4, "relaxed", "nervous", who="rioSuit"), A("zoe", 0.55, "phone", "neutral", who="zoeRich", facing=-1, hold={"k": "phone"})], [], wall="#3a3040", wall2="#1a1420", card=card("5 MIN", "until showtime", at=0.05, x=0.75))
S([173, 174, 175], "room", [A("guard", [[0, 0.7], ["@0.6", 0.7]], [[0, "relaxed"], ["@0.4", "fall"]], [[0, "neutral"], ["@0.4", "scared"]], facing=-1, rot=[["@0.4", 0], ["@1", 1.5708]], dy=[[0, 0]][0][1]), A("rio", 0.4, "relaxed", [[0, "neutral"], ["@0.5", "shocked"]], who="rioSuit")], [], wall="#3a3040", wall2="#1a1420")
S([176, 177, 178], "room", [A("guard", 0.7, "lie", "sleepy", rot=1.5708, facing=1, dy=136), A("zoe", 0.5, "handsOnHead", "scared", who="zoeRich", talk=["@1", "@1.9"]), A("crowd1", 0.85, "phoneEar", "scared", facing=-1, hold={"k": "phone"}, talk=["@2", 1])], [], wall="#3a3040", wall2="#1a1420", text=[T("CALL AN AMBULANCE!", 0.5, 0.18, "@1", size=56)])
S([179, 180, 181], "city", [], [prop("ambulance", 0.5, 1.6), prop("car", 0.2, 1.2), prop("car", 0.8, 1.2), prop("bus", 0.35, 1.6)], fx=["night"], card=card("12 MINUTES AWAY", "stuck in stadium traffic", at="@1", y=0.15))
S([182], "room", [], [], card=card("4-6 MINUTES", "without blood flow, brain damage can begin", at=0.05, w=860), props=[P("brain", 0.5, 0.6, 90, 0.2)], wall="#3a3040", wall2="#1a1420")
S([183, 184, 185], "room", [A("guard", 0.7, "lie", "sleepy", rot=1.5708, facing=1, dy=136), A("crowd1", 0.88, "handsOnHead", "scared", facing=-1), A("zoe", 0.5, "crossArms", "worried", who="zoeRich"), A("rio", 0.35, "relaxed", [[0, "scared"], ["@2", "determined"]], who="rioSuit")], [], wall="#3a3040", wall2="#1a1420", text=[T("NOBODY KNOWS WHAT TO DO", 0.5, 0.15, "@1", size=50)])
S([186, 187, 188], "room", [A("rio", 0.45, "think", "determined", who="rioSuit")], [], wall="#3a3040", wall2="#1a1420", inset={"who": "zoe", "label": "ZOE (MEMORY)", "talk": True, "at": 0, "x": 0.25}, text=[T("HARD AND FAST", 0.62, 0.2, "@1"), T("5 CM DEEP", 0.62, 0.32, "@2")])
S([189, 190, 191, 192], "room", [A("rio", 0.45, "relaxed", "worried", who="rioSuit"), A("zoe", 0.32, "reach", "angry", who="zoeRich", talk=["@1", 1])], [], wall="#3a3040", wall2="#1a1420", text=[T("\"YOU'RE ON IN 4 MINUTES\"", 0.55, 0.15, "@1", size=50)])
S([193, 194, 195], "room", [A("rio", 0.45, [[0, "relaxed"], ["@1", "relaxed"]], "worried", who="rioSuit", facing=[[0, -1], ["@1", 1]]), A("guard", 0.7, "lie", "sleepy", rot=1.5708, facing=1, dy=136)], [{"k": "stage", "x": 0.08, "w": 3}], wall="#3a3040", wall2="#1a1420", text=[T("THE SPOTLIGHT...", 0.25, 0.18, "@2", size=50), T("OR THE FLOOR", 0.72, 0.18, "@2.5", size=50)])
S([196, 197], "room", [A("rio", 0.725, [[0, "kneel"], ["@1", "cpr"]], "determined", who="rioSuit"), A("guard", 0.7, "lie", "sleepy", rot=1.5708, facing=1, dy=136)], [], wall="#3a3040", wall2="#1a1420", cam={"z": [1.3, 1.4], "x": [180, 200], "y": [80, 80]})
S([198], "room", [A("rio", 0.725, "cpr", "determined", who="rioSuit"), A("guard", 0.7, "lie", "sleepy", rot=1.5708, facing=1, dy=136)], [], wall="#3a3040", wall2="#1a1420", cam={"z": [1.4, 1.45], "x": [190, 200], "y": [90, 90]}, text=[T("1... 2... 3... 4", 0.62, 0.2, 0.3)])
S([199, 200, 201, 202], "room", [A("rio", 0.725, "cpr", [[0, "determined"], ["@2", "nervous"]], who="rioSuit"), A("guard", 0.7, "lie", "sleepy", rot=1.5708, facing=1, dy=136)], [], wall="#3a3040", wall2="#1a1420", cam={"z": [1.45, 1.55], "x": [200, 210], "y": [100, 100]}, text=[T("KEEP GOING", 0.6, 0.18, "@3")])
S([203, 204, 205, 206, 207], "room", [A("rio", 0.725, "cpr", "determined", who="rioSuit", talk=["@2", 1]), A("guard", 0.7, "lie", "sleepy", rot=1.5708, facing=1, dy=136)], [], wall="#3a3040", wall2="#1a1420", props=[P("note", 0.5, 0.3, 40, "@2"), P("note", 0.55, 0.22, 30, "@2.5")], text=[T("WHAT WAS THE SONG?", 0.5, 0.15, 0.05, size=50), T("STAYIN' ALIVE", 0.5, 0.25, "@3", size=60)])
S([208, 209, 210], "room", [A("rio", 0.725, "cpr", "determined", who="rioSuit"), A("sam", 0.45, [[0, "kneel"]], "worried", talk=["@1", "@1.9"]), A("guard", 0.7, "lie", "sleepy", rot=1.5708, facing=1, dy=136)], [], wall="#3a3040", wall2="#1a1420", text=[T("\"SHOW ME\"", 0.45, 0.2, "@1")])
S([211, 212, 213], "room", [A("sam", 0.725, "cpr", "determined"), A("rio", 0.48, "kneel", "determined", who="rioSuit", talk=[0, 1]), A("guard", 0.7, "lie", "sleepy", rot=1.5708, facing=1, dy=136)], [], wall="#3a3040", wall2="#1a1420", card=card("2 MIN EACH", "take turns", at=0.05, x=0.3, y=0.15))
S([214, 215, 216], "stadium", [], [], card=card("10... 9... 8...", None, at=0.05), text=[T("RIO! RIO! RIO!", 0.5, 0.4, "@1", size=70)])
S([217], "room", [A("rio", 0.725, "cpr", "determined", who="rioSuit"), A("guard", 0.7, "lie", "sleepy", rot=1.5708, facing=1, dy=136)], [], wall="#3a3040", wall2="#1a1420", card=card("2-3x", "survival chance with bystander CPR", at=0.05, x=0.32, w=660))
S([218, 219], "room", [A("rio", 0.725, "cpr", "determined", who="rioSuit"), A("guard", 0.7, "lie", "sleepy", rot=1.5708, facing=1, dy=136)], [], wall="#3a3040", wall2="#1a1420", props=[P("heart", 0.3, 0.3, 60, 0), P("brain", 0.3, 0.55, 50, "@1")], cam={"z": [1.4, 1.5], "x": [200, 200], "y": [90, 90]})
S([220, 221, 222], "room", [A("doctor", [[0, 1.0], [0.4, 0.82]], [[0, "relaxed"], [0.42, "kneel"]], "determined", facing=-1), A("nurse", [[0, 1.08], [0.45, 0.9]], [[0, "relaxed"], ["@2", "kneel"]], "worried", facing=-1), A("rio", [[0, 0.725], [0.3, 0.725], [0.45, 0.55]], [[0, "cpr"], [0.3, "kneel"]], "sleepy", who="rioSuit"), A("guard", 0.7, "lie", "sleepy", rot=1.5708, facing=1, dy=136)], [door(0.96)], wall="#3a3040", wall2="#1a1420", card=card("11 MINUTES LATER", None, at=0.05, y=0.14))
S([223, 224], "room", [A("nurse", 0.68, "kneel", "smile", facing=-1, talk=["@1", 1]), A("rio", 0.5, "kneel", "cry", who="rioSuit"), A("guard", 0.7, "lie", "neutral", rot=1.5708, facing=1, dy=136)], [], wall="#3a3040", wall2="#1a1420", text=[T("\"YOU KEPT HIM ALIVE\"", 0.5, 0.18, "@1", size=56)])
S([225, 226, 227, 228], "city", [A("rio", 0.45, "relaxed", [[0, "neutral"], ["@3", "smile"]], who="rioSuit")], [], fx=["night"], props=[P("newspaper", 0.7, 0.35, 80, "@1")], text=[T("\"DISASTER!\"", 0.7, 0.2, "@1"), T("NOT ONE BIT", 0.3, 0.2, "@3", size=56)])
S([229, 230, 231], "city", [A("crowd1", 0.3, "photo", "neutral", facing=1, hold={"k": "camera", "flash": 70}), A("crowd2", 0.72, "photo", "neutral", facing=-1, hold={"k": "camera", "flash": 90}), A("rio", [[0, 0.05], [1, 0.95]], "relaxed", "determined", who="rioSuit")], [], fx=["night"], text=[T("NO COMMENT", 0.5, 0.18, "@2", size=50)])
S([232, 233, 234], "street", [A("rio", [[0, 0.02], ["@1.6", 0.38]], [[0, "relaxed"], ["@2", "relaxed"]], [[0, "determined"], ["@2", "awe"]], who="rioSuit")], BOOTH, fx=["night"], text=[T("6 BLOCKS", 0.3, 0.2, "@0.3", size=50)])
S([235, 236, 237, 238], "street", [booth_rio("phoneEar", "thinking", who="rioSuit")], BOOTH, fx=["night"], thought={"props": ["star", "phone", "crown"], "x": 0.3, "y": 0.25, "at": "@1"})
S([239, 240, 241, 242, 243], "street", [booth_rio("phoneEar", [[0, "thinking"], ["@4", "determined"]], who="rioSuit")], BOOTH, fx=["night"], text=[T("KEEP THE FAME...", 0.3, 0.2, "@2", size=50), T("OR ONE LAST CALL", 0.3, 0.3, "@3", size=50)])
S([244], "street", [booth_rio("phoneEar", "determined", who="rioSuit", talk=[0, 0.85])], BOOTH, fx=["night"], card=card("LAST CALL", "\"what if everyone on Earth knew how to save a heart?\"", at=0.05, x=0.32, w=900, size=60), sfx=[{"at": 3.0, "name": "shimmer", "gain": -10}])
S([245, 246, 247], "home", [A("rio", 0.42, "sitBack", "surprised")], [], fx=["flash"], text=[T("NO BILLBOARD", 0.5, 0.18, "@2")])
S([248, 249, 250], "home", [A("rio", 0.42, "phone", [[0, "neutral"], ["@2", "smirk"]], hold={"k": "phone"})], [], card=card("300 FOLLOWERS", "2 are your cousins", at="@1", x=0.68, w=640))
S([251, 252, 253, 254, 255, 256], "kitchen", [A("zoe", 0.553, "stir", "happy", hold={"k": "spoon"}, talk=[0, 1]), A("rio", [[0, 0.05], ["@2.5", 0.4]], "relaxed", [[0, "surprised"], ["@3", "cry"]])], [{"k": "stove", "x": 0.59}], props=[P("note", 0.62, 0.3, 40, 0.05), P("note", 0.68, 0.24, 30, 0.2)], text=[T("STAYIN' ALIVE", 0.6, 0.15, "@1", size=56), T("NURSE SCRUBS", 0.5, 0.25, "@3", size=40)])
S([257, 258, 259], "kitchen", [A("rio", [[0, 0.4], [0.12, 0.47]], "hug", "cry"), A("zoe", 0.53, [[0, "stir"], [0.1, "hug"]], "surprised", facing=-1, hold={"k": "spoon", "drop": 0.14}, talk=["@0.6", "@1.6"])], [{"k": "stove", "x": 0.75}], text=[T("\"RIO!\"", 0.55, 0.2, "@0.6")])
S([260, 261], "cafe", [A("rio", 0.5, "talk", "smile", talk=[0, 1]), A("crowd1", 0.25, "sit", "smile"), A("crowd2", 0.78, "sit", "smile", facing=-1)], [], props=[P("mic", 0.56, 0.5, 30, 0)], card=card("12 PEOPLE", None, at="@1", y=0.14))
S([262], "cafe", [A("rio", 0.7, [[0, "talk"], [0.4, "relaxed"]], [[0, "smile"], [0.4, "shocked"]], facing=-1), A("oldman", 0.36, [[0, "relaxed"], [0.3, "choke"]], [[0, "neutral"], [0.3, "scared"]])], [], props=[P("mic", 0.75, 0.5, 30, 0)], text=[T("CHOKING!", 0.36, 0.2, 0.3)])
S([263, 264, 265], "cafe", [A("crowd1", [[0, 0.12], ["@0.4", 0.325]], [[0, "relaxed"], ["@0.45", "heimlich"]], "determined", lockFacing=True), A("oldman", 0.36, [[0, "choke"], ["@2", "relaxed"]], [[0, "scared"], ["@2", "neutral"]]), A("crowd2", [[0, 0.62], ["@0.5", 0.46]], [[0, "relaxed"], ["@0.6", "explain"]], "determined", facing=-1, talk=["@0.6", "@1.5"]), A("sam", [[0, 0.0], ["@0.6", 0.18]], [[0, "relaxed"], ["@0.7", "phoneEar"]], "determined", hold={"k": "phone", "from": "@0.7"}), A("rio", 0.75, "relaxed", "shocked", facing=-1)], [], cam={"z": [1.45, 1.35], "x": [-260, -200], "y": [-40, -40]}, text=[T("CALM. FAST.", 0.5, 0.15, "@0.6", size=56), T("EVERYONE KNOWS HOW", 0.5, 0.25, "@2", size=50)])
S([266, 267, 268], "cafe", [A("oldman", 0.35, "wave", "happy"), A("rio", 0.62, "talk", "smirk", facing=-1, talk=["@1", 1])], [], props=[P("mic", 0.58, 0.5, 30, 0)], text=[T("\"THAT'S A TOUGH CROWD\"", 0.55, 0.18, "@2", size=50)])
S([269, 270], "cafe", [A("rio", 0.5, "cheer", "joy"), A("crowd1", 0.25, "cheer", "joy"), A("crowd2", 0.78, "cheer", "joy", facing=-1), A("oldman", 0.35, "cheer", "joy")], [], text=[T("HA HA HA", 0.5, 0.18, 0.05, size=70)])
S([271, 272, 273], "kitchen", [A("rio", 0.47, "hug", "happy"), A("zoe", 0.53, "hug", "happy", facing=-1)], [{"k": "stove", "x": 0.75}], text=[T("ONE CALL", 0.5, 0.15, 0.05), T("THE ONE THAT BROUGHT HER BACK", 0.5, 0.25, "@2", size=46)])
S([274], "space", [], [], text=[T("IS IT REAL?", 0.5, 0.45, 0.05, size=110)])
S([275, 276], "space", [], [], card=card("1972", "Edward Lorenz: the butterfly effect", at=0.05, w=780, y=0.15), props=[P("bee", 0.3, 0.55, 50, "@1"), P("storm", 0.72, 0.55, 80, "@1.5")])
S([277, 278, 279], "space", [], [], text=[T("TINY CHANGE", 0.3, 0.45, "@1", size=60), T("HUGE RESULT", 0.72, 0.45, "@1.5", size=70)], props=[P("earth", 0.5, 0.7, 70, "@2")])
S([280, 281, 282], "classroom", [A("crowd1", 0.314, "cpr", "determined"), A("crowd2", 0.664, "cpr", "determined"), A("nurse", 0.5, [[0, "explain"], ["@1", "point"], ["@2", "explain"]], "smile", talk=[0, 1], facing=[[0, -1], ["@1", 1]])], [{"k": "mannequin", "x": 0.35}, {"k": "mannequin", "x": 0.7}], card=card("A FEW HOURS", "to learn CPR", at="@2", y=0.15))
S([283, 284, 285, 286], "kitchen", [A("rio", 0.47, "hug", "happy"), A("zoe", 0.53, "hug", "happy", facing=-1)], [{"k": "stove", "x": 0.75}], text=[T("MAYBE SOMEONE YOU LOVE", 0.5, 0.18, "@1", size=52), T("WOULD YOU?", 0.5, 0.3, "@2.5")])
S([287, 288, 289, 290], "room", [A("rio", [[0, 0.2], ["@1", 0.45]], [[0, "relaxed"], ["@2", "holdFront"]], [[0, "neutral"], ["@2", "surprised"]])], [door(0.8)], props=[P("gift", 0.55, 0.62, 40, "@1"), P("letter", 0.55, 0.35, 50, "@3")], text=[T("NAME ANY FOOD", 0.55, 0.2, "@3")], **APT)
S([291, 292], "face", [], [], who="rio", expr=[[0, "smile"]])
S([293], "end", [], [], tpl="end")


# ---- blocking pass (v3): no aimless pacing. People move only for a reason in the narration (arrive, walk to
# someone or something, leave), talkers change gesture on each sentence, and long shots are cut into 1-2
# sentence shots with changing framing (wide / medium on the speaker / alternate angle).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "pipeline"))
VAR = {"relaxed": ["think", "crossArms", "shrug"], "think": ["relaxed", "crossArms"], "crossArms": ["think", "relaxed"], "sad": ["facepalm", "chest"], "nervous": ["handsOnHead", "think"],
       "talk": ["explain", "point"], "explain": ["talk", "point"], "worried": ["think", "handsOnHead"], "point": ["explain", "relaxed"], "shrug": ["relaxed", "think"]}
CALLSTART = {32, 46, 67, 85, 100, 118, 235, 244}
def actor(b, id_): return next(a for a in b["actors"] if a["id"] == id_)
for b in B:
    if b.get("tpl") in ("title", "end", "science") or b["set"] in ("face", "space"): continue
    n = len(b["lines"]); acts = b["actors"]
    booth = any(i.get("k") == "booth" for i in b["items"])
    if booth and b["lines"][0] in CALLSTART:   # Rio walks up to the booth, opens it, lifts the receiver
        for a in acts:
            if a["id"] == "rio": a["x"] = [[0, 0.3], ["@0.55", 0.6]]; a["pose"] = [[0, "relaxed"], ["@0.6", "phoneEar"]]; a["hold"] = {"k": "phone", "from": "@0.6"}
    for a in acts:
        poses = a["pose"]; p0 = poses[0][1]
        if len(poses) == 1 and p0 in VAR and n > 1 and (a.get("talk") or len(acts) == 1) and not a.get("rot") and not a.get("up"):
            v = VAR[p0]; a["pose"] = [[0, p0]] + [[f"@{i}", v[(i - 1) % len(v)] if i % 2 else p0] for i in range(1, n)]
for b in B:
    L = b["lines"][0]
    if L == 57: r = actor(b, "rio"); r["x"] = [[0, 0.1], ["@0.8", 0.35]]
    if L == 158: r = actor(b, "rio"); r["x"] = [[0, 0.2], ["@0.6", 0.38]]
    if L == 189: z = actor(b, "zoe"); z["x"] = [[0, 0.1], ["@0.6", 0.32]]
    if L == 208: s = actor(b, "sam"); s["x"] = [[0, 0.2], ["@0.6", 0.52]]; s["pose"] = [[0, "relaxed"], ["@0.7", "kneel"]]
    if L == 245: r = actor(b, "rio"); r["pose"] = [[0, "sitBack"], ["@1", "stand"], ["@2", "handsOnHead"]]; r["x"] = [[0, 0.42], ["@1.2", 0.42], ["@2", 0.5]]
    if L in (3, 5): b["fx"] = ["greensky"]
    if L in (38, 43): b["fx"] = ["drought"]

# ---- cut long shots ----
from build import split_sentences
item = next(x for x in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts.json")))["long"] if x["stt"] == 32)
LENS = [len(s.split()) for s in split_sentences(item["script"])]
def xs(a):
    v = a["x"]; return [k[1] for k in v] if isinstance(v, list) else [v]
def frame(c, j):
    if j == 0 or c.get("tpl") or c["set"] in ("face", "space", "map") or "cam" in c or not c["actors"]: return
    acts = c["actors"]
    if any(a.get("up") or a.get("rot") for a in acts): return
    talk = [a for a in acts if a.get("talk")] or [a for a in acts if a["id"] == "rio"] or acts
    f = talk[0]; X = xs(f)
    if max(X) - min(X) > 0.15: return
    xm = sum(X) / len(X)
    if j % 2 == 1: c["cam"] = {"z": [1.34, 1.42], "x": [max(-520, min(520, (xm - 0.5) * 1920))] * 2, "y": [-40, -40]}
    else: c["cam"] = {"z": [1.12, 1.16], "x": [max(-300, min(300, (xm - 0.5) * 960))] * 2, "y": [-10, -10]}
NB = []
for b in B:
    n = len(b["lines"])
    if n < 2 or b.get("tpl") or b["set"] in ("face",): NB.append(b); continue
    ch = plan_chunks(n, [LENS[i] for i in b["lines"]])
    if len(ch) == 1: NB.append(b); continue
    for j, c in enumerate(split_board(b, ch)): frame(c, j); NB.append(c)
B[:] = NB
save(32, 294)
