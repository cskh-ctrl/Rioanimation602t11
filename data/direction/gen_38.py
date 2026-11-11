# Storyboard long_38 "What If You Owned An Invisibility Cloak For 24 Hours?"
# Invisible Rio = ghost 0.06 (only two floating eyes show). In rain he shows as a faint water outline (ghost 0.3).
from sb import *
def door(x, **kw): d = {"k": "housedoor", "x": x}; d.update(kw); return d
INV = 0.03
def inv(x, pose="relaxed", expr="neutral", **kw): kw.setdefault("ghost", INV); return A("rio", x, pose, expr, who="cloak", **kw)
APT = dict(wall="#c8b0a0", wall2="#7a6070", room={"frames": 260, "window": 1250})
HALLW = dict(wall="#b8a890", wall2="#6a5a4a", room={})
STA = dict(wall="#4a4a58", wall2="#22222a", room={})
def platform(tx=2, lamp=0): return {"k": "subway", "x": 0.5, "tx": tx, "lamp": lamp}
CLOCK = {"k": "stationclock", "x": 0.15}
FRIDGE = {"k": "fridge", "x": 0.8}

# ---- cold open: walking through the office ----
S([0, 1, 2, 3], "office", [inv([[0, -0.05], [1, 1.05]]), A("boss", 0.3, "type", "neutral"), A("guard", 0.82, "relaxed", "neutral", facing=-1)], [{"k": "desk", "x": 0.34}], props=[P("coffee", 0.58, 0.45, 40, "@2")], text=[T("PAST YOUR BOSS", 0.3, 0.16, "@1", size=46), T("PAST THE COFFEE MACHINE", 0.58, 0.26, "@2", size=44), T("PAST SECURITY", 0.82, 0.36, "@3", size=44)])
S([4, 5, 6, 7], "office", [A("crowd1", 0.3, "type", "neutral"), A("crowd2", 0.66, "type", "sleepy"), inv([[0, 0.45], [1, 0.55]])], [{"k": "desk", "x": 0.34}, {"k": "desk", "x": 0.7}], text=[T("NOBODY LOOKS UP", 0.5, 0.14, 0.05, size=50), T("WHICH IS NORMAL, HONESTLY", 0.5, 0.24, "@2", size=44), T("TODAY THEY REALLY CAN'T SEE YOU", 0.5, 0.34, "@3", size=44)])

# ---- who you are ----
S([8, 9, 10], "office", [A("rio", 0.42, "type", "neutral"), A("crowd1", 0.7, "talk", "happy", facing=-1, talk=[0, 1]), A("crowd2", 0.82, "relaxed", "smile", facing=-1)], [{"k": "desk", "x": 0.46}], card=card("RIO", "an accountant. quiet. polite.", at=0.05, x=0.28, w=560), text=[T("THE ONE PEOPLE FORGET IS IN THE ROOM", 0.5, 0.42, "@2", size=40)])
S([11, 12, 13], "room", [A("rio", [[0, 0.2], ["@0.6", 0.42]], [[0, "relaxed"], ["@1", "crouch"], ["@2", "holdFront"]], [[0, "neutral"], ["@2", "awe"]])], [{"k": "table", "x": 0.55, "w": 1.0}], props=[P("gift", 0.55, 0.62, 45, 0.1), P("mask", 0.55, 0.42, 50, "@2")], card=card("GRANDMA'S OLD TRUNK", None, at=0.05, x=0.7, w=640), text=[T("A SILVER CLOAK... SOFT AS WATER", 0.5, 0.36, "@2", size=44)], **APT)
S([14, 15, 16, 17, 18], "room", [A("rio", 0.38, "relaxed", [[0, "smile"], ["@2", "shocked"]], who="cloak", ghost=[[0, 1], ["@0.8", 1], ["@1.3", INV]]), A("rio", 0.62, "relaxed", [[0, "smile"], ["@2", "shocked"]], who="cloak", facing=-1, ghost=[[0, 1], ["@0.8", 1], ["@1.3", INV]])], [{"k": "glass", "x": 0.5}], text=[T("NOBODY THERE", 0.5, 0.16, "@2", size=50), T("EXCEPT TWO TINY EYES", 0.5, 0.26, "@3", size=46)], **APT)
S([19, 20], "city", [A("crowd1", 0.3, "cheer", "joy"), A("crowd2", 0.45, "point", "happy"), inv(0.7)], [], text=[T("EVERYONE WANTS TO BE SEEN", 0.5, 0.16, 0.05, size=48), T("YOU: GONE FOR 24 HOURS", 0.5, 0.26, "@1", size=48)])
S([21, 22, 23, 24], "room", [inv(0.42, pose=[[0, "relaxed"], ["@1", "facepalm"]])], [], card=card("ONE RULE", "stay silent", at=0.05, x=0.68), text=[T("SAY ONE WORD... YOU REAPPEAR. FOREVER.", 0.5, 0.42, "@2", size=40), T("JUST A PLAIN SILVER BLANKET", 0.5, 0.52, "@3", size=42)], **APT)
S([25], "room", [], [], tpl="title", params={"title": "What If You Were Invisible For 24 Hours?"})

# ---- hour one: the eyes ----
S([26, 27, 28, 29], "room", [inv(0.42, pose="think")], [{"k": "glass", "x": 0.6}], card=card("HOUR 1", None, at=0.05, x=0.75), text=[T("WHY CAN YOU STILL SEE YOUR EYES?", 0.5, 0.36, "@1", size=42), T("FULLY INVISIBLE = BLIND", 0.5, 0.46, "@3", size=48, color="#ff6a5a")], **APT)
S([30, 31, 32], "room", [], [], tpl="science", params={"sci": "EYES MUST CATCH LIGHT", "icon": "eye"})
S([33, 34, 35], "office", [inv([[0, 0.2], [1, 0.62]]), A("crowd2", 0.82, "type", [[0, "neutral"], ["@2", "scared"]], facing=-1)], [{"k": "desk", "x": 0.86}], cam={"z": [1.3, 1.4], "x": [0, 120], "y": [-60, -60]}, text=[T("TWO TINY HOLES FOR YOUR EYES", 0.5, 0.14, 0.05, size=44), T("CREEPY? VERY.", 0.5, 0.24, "@2", size=50)])

# ---- hour two: the donut ----
S([36, 37, 38], "kitchen", [A("sam", [[0, 0.95], ["@1.5", 0.72]], [[0, "relaxed"], ["@1.6", "reach"]], "neutral", hold={"k": "bagel"}), inv(0.42)], [{"k": "fridge", "x": 0.86}], card=card("HOUR 2", "the break room", at=0.05, x=0.25))
S([39, 40, 41, 42, 43], "kitchen", [A("sam", 0.62, [[0, "holdCup"], ["@1", "holdCup"], ["@4", "drop"]], [[0, "neutral"], ["@1", "confused"], ["@3", "scared"]], hold={"k": "bagel", "drop": "@4.2"}, facing=[[0, 1], ["@1", -1]]), inv(0.5, pose=[[0, "reach"], ["@0.6", "relaxed"]])], [{"k": "fridge", "x": 0.86}],
  props=[P("bite", 0.62, 0.5, 30, 0.4) if False else P("burger", 0.66, 0.32, 30, 0.3)], text=[T("CHOMP", 0.5, 0.3, 0.3, size=50), T("HE STARES AT THE EMPTY ROOM", 0.5, 0.16, "@2", size=44), T("...INTO THE TRASH", 0.5, 0.26, "@4", size=44)])
S([44, 45], "kitchen", [inv(0.45, pose="sad")], [], text=[T("DO YOU FEEL BAD?", 0.5, 0.16, 0.05), T("A LITTLE.", 0.5, 0.26, "@1")])

# ---- hour three: silence ----
S([46, 47, 48, 49, 50, 51], "office", [inv(0.45, pose=[[0, "relaxed"], ["@2", "chest"], ["@3", "facepalm"]]), A("crowd1", 0.25, "type", "neutral"), A("crowd2", 0.7, "talk", "joy", facing=-1, talk=["@3", 1])], [{"k": "desk", "x": 0.29}], card=card("HOUR 3", "problems", at=0.05, x=0.75), text=[T("NO TALKING. NO SNEEZING.", 0.5, 0.36, "@1", size=44), T("NO LAUGHING.", 0.5, 0.46, "@3", size=48), T("TORTURE", 0.5, 0.56, "@5", color="#ff6a5a")])
S([52, 53], "office", [inv([[0, 0.2], [1, 0.62]])], [], text=[T("THE CLOAK DOESN'T HIDE FOOTSTEPS", 0.5, 0.16, 0.05, size=44), T("SQUEAK. SQUEAK.", 0.5, 0.3, "@1", size=56)])
S([54, 55, 56, 57, 58], "office", [A("boss", [[0, 0.75], ["@4", 0.75], [1, 1.1]], [[0, "relaxed"], ["@1", "think"], ["@4", "shrug"]], [[0, "neutral"], ["@1", "confused"]], facing=-1, talk=["@1", "@1.9"]), inv(0.4, pose="relaxed")], [], text=[T("\"IS SOMEONE THERE?\"", 0.7, 0.16, "@1", size=50), T("SQUEAK.", 0.4, 0.3, "@2.4", size=50), T("WILL HE FIND YOU?", 0.5, 0.42, "@3", size=46)])

# ---- hour four: heat and noses ----
S([59, 60, 61, 62], "street", [inv(0.45)], [], card=card("HOUR 4", "what can still find you", at=0.05, x=0.75, w=620), fx=["dark"], text=[T("YOUR BODY: ~37 C", 0.5, 0.36, "@2", size=50)])
S([62], "street", [A("rio", 0.45, "relaxed", "neutral", who="cloak")], [], fx=["dark"], text=[T("THERMAL CAMERA", 0.5, 0.16, 0.05, size=50)]) if False else None
S([63, 64], "park", [], [{"k": "prop", "p": "dog", "x": 0.45, "size": 0.6}], props=[P("nose", 0.62, 0.4, 50, 0.1)], card=card("1,000s OF TIMES", "more sensitive noses than ours", at="@1", w=760))
S([65, 66, 67, 68, 69, 70], "park", [inv([[0, 0.15], [1, 0.7]], expr="smile"), {"id": "dog", "who": "dog", "x": [[0, 0.05], [1, 0.6]], "pose": [[0, "relaxed"]], "expr": [[0, "joy"]], "alpha": 0}, A("oldman", [[0, -0.05], [1, 0.45]], [[0, "relaxed"], ["@5", "talk"]], "confused", talk=["@5", 1])],
  [{"k": "prop", "p": "dog", "x": [[0, 0.07], [1, 0.62]], "size": 0.55, "dx": 0}], text=[T("A GOLDEN RETRIEVER, 3 BLOCKS", 0.5, 0.14, 0.05, size=44), T("WAG WAG", 0.62, 0.26, "@1", size=46), T("\"WHO ARE YOU TALKING TO, BUDDY?\"", 0.5, 0.36, "@5", size=42)])

# ---- hour five: rain ----
S([71, 72, 73, 74], "street", [inv([[0, 0.1], [1, 0.6]], ghost=[[0, INV], ["@1", INV], ["@2", 0.32]])], [], card=card("HOUR 5", None, at=0.05, x=0.75), fx=["rain"], text=[T("A PERSON-SHAPED OUTLINE... OF WATER", 0.5, 0.36, "@3", size=42)])
S([75, 76, 77], "street", [A("boy", 0.25, "point", "shocked", talk=[0, "@1.9"]), A("mom2", 0.15, "relaxed", "confused"), inv([[0, 0.55], ["@2", 0.6], [1, 1.1]], ghost=0.32)], [], fx=["rain"], text=[T("\"MOM! A GHOST!\"", 0.3, 0.16, 0.1), T("SQUEAK. SQUEAK. SPLASH.", 0.6, 0.28, "@2", size=50)])

# ---- hour six: no shadow ----
S([78, 79, 80, 81, 82, 83], "town", [inv(0.62), A("crowd2", 0.85, "relaxed", "neutral")], [{"k": "shop", "x": 0.62, "s": "SHOP", "lit": True}], card=card("HOUR 6", "no shadow, no reflection", at=0.05, x=0.22, w=600), text=[T("LIGHT FLOWS AROUND YOU", 0.25, 0.36, "@2", size=46)])
S([84, 85, 86], "town", [inv(0.45, pose="crossArms", expr="sad")], [{"k": "shop", "x": 0.45, "s": "SHOP", "lit": True}], text=[T("STARING AT NOTHING", 0.5, 0.72, 0.05, size=48), T("A LITTLE LONELY", 0.5, 0.82, "@2", size=48)])

# ---- hour seven: the meeting ----
S([87, 88, 89, 90], "office", [A("boss", 0.3, "explain", "neutral", talk=[0, 1]), A("sam", 0.5, "sit", "neutral"), A("crowd1", 0.62, "sit", "neutral"), inv(0.82)], [{"k": "table", "x": 0.55, "w": 1.6}], card=card("HOUR 7", "meetings you're never invited to", at=0.05, x=0.68, w=640))
S([91, 92], "office", [A("boss", 0.3, "point", "smile", talk=[0, "@0.95"]), A("sam", 0.5, "sit", "surprised"), A("crowd1", 0.62, "sit", "neutral"), inv(0.82, expr="sad")], [{"k": "table", "x": 0.55, "w": 1.6}], text=[T("\"IT WORKED BECAUSE OF SAM\"", 0.4, 0.16, 0.05, size=46), T("YOU DID MOST OF THE WORK", 0.5, 0.26, "@1", size=46)])
S([93, 94, 95, 96], "office", [A("boss", 0.3, "relaxed", "surprised"), A("sam", 0.5, [[0, "sit"], [0.1, "explain"]], "determined", talk=[0, "@1.9"]), A("crowd1", 0.62, "sit", "neutral"), inv(0.82, expr=[[0, "sad"], ["@3", "cry"]])], [{"k": "table", "x": 0.55, "w": 1.6}], text=[T("\"NO. RIO DID MOST OF IT.\"", 0.5, 0.14, 0.05, size=46), T("\"HE ALWAYS DOES.\"", 0.5, 0.24, "@1", size=46), T("NOBODY NOTICES HIM", 0.5, 0.34, "@2", size=44)])

# ---- hour eight: going viral ----
S([97, 98, 99, 100], "city", [A("crowd1", 0.3, "phone", "shocked", hold={"k": "phone"}), A("crowd2", 0.65, "phone", "joy", hold={"k": "phone"}, facing=-1)], [], card=card("HOUR 8", "the world finds out", at=0.05, x=0.5, y=0.14), props=[P("eye", 0.5, 0.42, 50, "@2")], text=[T("20,000,000 VIEWS", 0.5, 0.56, "@3", size=56)])
S([101, 102, 103, 104, 105], "home", [inv(0.42, pose="phone", hold={"k": "phone"})], [], inset={"who": "carla", "label": "CARLA DIAZ, TV", "at": "@3", "x": 0.75}, props=[P("letter", 0.62, 0.55, 40, 0.05)], text=[T("HOW DID SHE FIND YOU?", 0.42, 0.16, "@1", size=46), T("SHE'S FAMOUS", 0.42, 0.26, "@4", size=46)])
S([106, 107, 108, 109, 110, 111, 112, 113], "home", [inv(0.42, pose="phone", hold={"k": "phone"})], [], inset={"who": "carla", "label": "CARLA DIAZ, TV", "at": 0, "x": 0.78, "talk": True},
  text=[T("\"ARE YOU THE INVISIBLE MAN?\"", 0.42, 0.14, "@1", size=44), T("\"PROVE IT ON LIVE TV. 6 PM.\"", 0.42, 0.24, "@2", size=44), T("\"SAY HELLO TO THE WORLD\"", 0.42, 0.34, "@6", size=44)], card=card("$1,000,000", "the first invisible man in history", at="@7", x=0.42, y=0.55, w=700))
S([114, 115, 116, 117, 118, 119], "home", [inv(0.42, pose=[[0, "phone"], ["@4", "cheer"]], hold={"k": "phone", "to": "@3.9"}, expr="joy")], [], text=[T("ONE MILLION.", 0.5, 0.14, 0.05), T("COULD YOU STAY SILENT TILL SIX?", 0.5, 0.26, "@3", size=44), T("EASY. RIGHT?", 0.5, 0.36, "@5")])

# ---- hour nine: Mrs. Rosa ----
S([120, 121, 122], "street", [inv([[0, 0.05], [1, 0.6]], pose="relaxed", expr="thinking")], [], card=card("HOUR 9", "walking home", at=0.05, x=0.75))
S([123, 124, 125, 126, 127], "town", [A("rosa", 0.45, "crouch", "smile", s=1.5), inv(0.75, expr="sad")], [{"k": "prop", "p": "bird", "x": 0.55, "size": 0.25}, {"k": "prop", "p": "bird", "x": 0.6, "size": 0.25}, {"k": "prop", "p": "bird", "x": 0.35, "size": 0.25}], card=card("MRS. ROSA", "81, tiny, feeds the pigeons", at=0.05, x=0.3, w=600), text=[T("5 YEARS NEXT DOOR", 0.62, 0.36, "@2", size=46), T("WORDS SAID: MAYBE 10", 0.62, 0.46, "@3", size=46)])
S([128, 129, 130, 131, 132, 133, 134], "room", [A("rosa", 0.42, [[0, "pour"], ["@2", "sitTable"]], "smile", hold={"k": "pour", "to": "@1.9"}, talk=["@5", 1], s=1.5), inv([[0, 0.92], ["@1", 0.8]])], [{"k": "table", "x": 0.52, "w": 1.0}, {"k": "dish", "x": 0.47, "food": "cocoa", "at": "@2"}, {"k": "dish", "x": 0.58, "food": "cocoa", "at": "@2.3"}, door(0.88, open=1)],
  text=[T("TWO CUPS OF TEA", 0.5, 0.14, "@2", size=46), T("ONE FOR AN EMPTY CHAIR", 0.5, 0.24, "@3", size=46), T("\"THE PIGEONS WERE NAUGHTY, LUIS\"", 0.5, 0.34, "@6", size=42)], wall="#c8b8a0", wall2="#7a6a5a")
S([135, 136, 137, 138], "room", [A("rosa", 0.42, "sitTable", "sad", s=1.5), inv(0.8, expr=[[0, "smile"], ["@1", "sad"]])], [{"k": "table", "x": 0.52, "w": 1.0}, {"k": "dish", "x": 0.58, "food": "cocoa", "at": -1}], cam={"z": [1.3, 1.4], "x": [40, 40], "y": [-60, -60]}, text=[T("LUIS. HER HUSBAND.", 0.5, 0.14, "@1", size=48), T("TEA FOR HIM, EVERY DAY", 0.5, 0.24, "@3", size=46)], wall="#c8b8a0", wall2="#7a6a5a")
S([139, 140, 141, 142], "room", [A("rosa", 0.42, "sitTable", "smile", s=1.5)], [{"k": "table", "x": 0.52, "w": 1.0}], props=[P("family", 0.55, 0.42, 60, 0.05)], card=card("AVA", "her granddaughter... pink rain boots", at="@1", x=0.72, w=620), wall="#c8b8a0", wall2="#7a6a5a")
S([143, 144, 145, 146, 147, 148], "room", [A("rosa", 0.42, "sitTable", "joy", talk=[0, 1], s=1.5), inv(0.8)], [{"k": "table", "x": 0.52, "w": 1.0}, {"k": "dish", "x": 0.58, "food": "cocoa", "at": -1}], text=[T("\"AVA'S COMING TOMORROW\"", 0.5, 0.14, "@2", size=46), T("\"ON THE TRAIN\"", 0.5, 0.24, "@3", size=46), T("\"BY THE BIG CLOCK. LIKE ALWAYS.\"", 0.5, 0.34, "@4", size=44)], wall="#c8b8a0", wall2="#7a6a5a")
S([149, 150, 151, 152], "room", [inv(0.5, pose="sad", expr="sad")], [], cam={"z": [1.4, 1.5], "y": [-60, -60]}, text=[T("INVISIBLE YOUR WHOLE LIFE", 0.5, 0.14, "@1", size=48), T("NOT BECAUSE OF A CLOAK", 0.5, 0.24, "@2", size=46), T("YOU NEVER SAID HELLO", 0.5, 0.34, "@3", size=48)], wall="#c8b8a0", wall2="#7a6a5a")

# ---- hour 23: the station ----
S([153, 154, 155, 156, 157, 158], "room", [inv([[0, 0.05], ["@3", 0.4]]), A("crowd1", 0.6, "relaxed", "neutral"), A("crowd2", 0.75, "phone", "neutral", hold={"k": "phone"}), A("dad", 0.88, "relaxed", "neutral", facing=-1)], [platform(), CLOCK], card=card("HOUR 23", "next day, 5:30 PM, Central Station", at=0.05, x=0.6, w=680), text=[T("TV STUDIO: RIGHT ABOVE", 0.5, 0.36, "@4", size=44), T("30 MIN TO SHOWTIME", 0.5, 0.46, "@5", size=46)], **STA)
S([159, 160, 161], "room", [inv(0.4, pose="phone", hold={"k": "phone"})], [platform(), CLOCK], inset={"who": "carla", "label": "CARLA", "at": 0, "x": 0.75}, text=[T("\"READY? WALK IN AT SIX.\"", 0.45, 0.16, "@1", size=46), T("\"STAY SILENT TILL THE STAGE.\"", 0.45, 0.26, "@2", size=44)], **STA)
S([162, 163, 164, 165], "room", [A("crowd1", 0.12, "relaxed", "neutral"), A("mom2", 0.22, "phone", "neutral", hold={"k": "phone"}), A("dad", 0.32, "relaxed", "neutral"), inv(0.45), A("crowd2", 0.58, "relaxed", "neutral"), A("oldman", 0.7, "relaxed", "neutral"), A("sam", 0.82, "phone", "neutral", hold={"k": "phone"})], [platform(tx=[[0, 1.3], [1, -3.6]]), CLOCK], text=[T("RUSH HOUR. THOUSANDS OF PEOPLE.", 0.5, 0.14, "@1", size=44)], **STA)
S([166, 167, 168, 169, 170], "room", [A("ava", 0.6, "sad", "cry", s=1.6), A("crowd1", 0.2, "relaxed", "neutral"), A("dad", 0.3, "phone", "neutral", hold={"k": "phone"}), inv(0.4, expr=[[0, "neutral"], ["@0.5", "shocked"]])], [platform(), CLOCK], text=[T("PINK RAIN BOOTS", 0.6, 0.16, 0.2, size=48), T("AVA. ALONE. CRYING.", 0.6, 0.26, "@1", size=48), T("HER MOM: NOWHERE", 0.6, 0.36, "@3", size=44)], **STA)
S([171, 172, 173, 174], "room", [A("ava", [[0, 0.6], ["@2", 0.6], [1, 0.66]], [[0, "sad"]], "cry", facing=[[0, -1], ["@1", 1], ["@2", 1]], yk=[[0, 0], ["@2", 0], [1, -0.06]]), inv(0.3, expr="scared")], [platform(), CLOCK], text=[T("TOWARD THE YELLOW LINE", 0.6, 0.16, "@3", size=48, color="#f2c21a")], **STA)
S([175, 176, 177], "room", [A("ava", 0.66, "sad", "scared", yk=-0.06), inv(0.3, expr="scared")], [platform(lamp=[[0, 0.1], [1, 0.4]]), CLOCK], fx=["shake"], text=[T("HOOOONK", 0.85, 0.2, 0.05), T("A TRAIN IS COMING", 0.5, 0.3, "@2", size=50)], **STA)
S([178, 179], "room", [], [platform(lamp=0.5)], card=card("~100 METERS", "for a subway train at speed to stop... maybe more", at=0.05, w=880), **STA)
S([180, 181, 182, 183, 184], "room", [inv(0.25, expr="scared"), A("crowd1", 0.38, "relaxed", "neutral"), A("dad", 0.46, "phone", "neutral", hold={"k": "phone"}), A("ava", [[0, 0.66], ["@3", 0.66], ["@3.5", 0.68]], "sad", "cry", yk=[[0, -0.06], ["@3", -0.06], ["@3.5", -0.09]])], [platform(lamp=[[0, 0.5], [1, 0.7]]), CLOCK],
  text=[T("20 METERS AWAY. INVISIBLE.", 0.5, 0.14, 0.05, size=46), T("A WALL OF COATS AND BAGS", 0.5, 0.24, "@2", size=44), T("WHAT CAN YOU DO?", 0.5, 0.34, "@4")], **STA)
S([185, 186, 187, 188], "room", [inv(0.3, pose="think", expr="worried"), A("ava", 0.68, "sad", "cry", yk=-0.09)], [platform(lamp=0.7), CLOCK], text=[T("SHE CAN'T SEE YOU", 0.5, 0.14, "@2", size=48), T("SHE NEEDS TO HEAR YOU", 0.5, 0.24, "@3", size=48)], **STA)
S([189, 190, 191, 192, 193, 194], "room", [inv(0.3, pose="handsOnHead", expr="scared"), A("ava", 0.68, "sad", "cry", yk=-0.09)], [platform(lamp=[[0, 0.7], [1, 0.85]]), CLOCK], thought={"props": ["tv", "money", "star"], "x": 0.3, "y": 0.28, "at": 0.05}, text=[T("SPEAK NOW = ALL GONE. FOREVER.", 0.6, 0.5, "@4", size=42), T("THE CLOAK... OR THE GIRL", 0.6, 0.6, "@5", size=48)], **STA)
S([195, 196, 197], "room", [inv(0.3, expr="scared"), A("ava", [[0, 0.68], ["@2", 0.68], [1, 0.7]], "sad", "cry", yk=[[0, -0.09], ["@2", -0.09], [1, -0.105]])], [platform(lamp=[[0, 0.85], [1, 1]]), CLOCK], fx=["shake"], text=[T("THE RAILS HUM", 0.5, 0.18, "@1", size=50)], **STA)
S([198, 199], "room", [A("rio", [[0, 0.3], ["@1", 0.45]], [[0, "relaxed"], [0.2, "point"]], "determined", who="cloak", ghost=[[0, INV], ["@1", INV], ["@1.4", 1]], talk=[0.1, "@1.4"]), A("ava", 0.7, "sad", [[0, "cry"], [0.4, "surprised"]], yk=-0.105, facing=[[0, 1], [0.4, -1]])], [platform(lamp=1), CLOCK], fx=["flash"] if False else [], text=[T("\"AVA! STOP!\"", 0.4, 0.16, 0.1), T("\"STAY RIGHT THERE!\"", 0.5, 0.26, "@1"), T("FLASH", 0.45, 0.36, "@1.4", size=50)], **STA)
S([200, 201, 202, 203, 204], "room", [A("rio", 0.45, "relaxed", "determined", who="cloak"), A("crowd1", 0.2, "relaxed", "shocked"), A("dad", 0.3, "point", "shocked"), A("crowd2", 0.85, "relaxed", "shocked", facing=-1), A("ava", 0.7, "relaxed", "surprised", yk=-0.105, facing=-1)], [platform(lamp=1), CLOCK], text=[T("THE CLOAK GOES HEAVY AND GRAY", 0.5, 0.14, 0.05, size=44), T("A MAN IN A SILVER BLANKET", 0.5, 0.24, "@2", size=46), T("EVERYONE TURNS", 0.5, 0.34, "@4", size=46)], **STA)
S([205, 206, 207, 208, 209, 210], "room", [A("rio", [[0, 0.45], ["@2", 0.45], ["@2.7", 0.66], ["@4", 0.66], ["@4.6", 0.5]], [[0, "relaxed"], ["@3", "carry"]], "determined", who="cloak", yk=[[0, 0], ["@2.7", 0], ["@3", -0.09], ["@4", -0.09], ["@4.6", 0]], walkArms=True), A("ava", [[0, 0.7], ["@3", 0.7], ["@4", 0.68], ["@4.6", 0.52]], [[0, "relaxed"], ["@3", "hug"]], "scared", yk=[[0, -0.105], ["@3", -0.105], ["@3.2", -0.2], ["@4", -0.2], ["@4.6", -0.11]], facing=-1)],
  [platform(tx=[[0, 2], ["@4.5", 2], ["@4.6", 1.2], [1, -3]], lamp=1), CLOCK], text=[T("FROZEN ON THE YELLOW LINE", 0.5, 0.14, 0.05, size=44, color="#f2c21a"), T("YOU RUN", 0.5, 0.24, "@2"), T("WHOOSH", 0.6, 0.34, "@4.6", size=70)], **STA)
S([211, 212, 213], "room", [A("rio", 0.5, "carry", "worried", who="cloak"), A("ava", 0.52, "hug", "cry", yk=-0.11, facing=-1, talk=["@1", 1])], [platform(tx=[[0, -1.5], [1, -3.6]]), CLOCK], cam={"z": [1.4, 1.5], "x": [20, 20], "y": [-80, -80]}, text=[T("HALF A METER FROM HER BOOTS", 0.5, 0.14, 0.05, size=44), T("\"WHO ARE YOU? A GHOST?\"", 0.5, 0.24, "@1", size=46)], **STA)
S([214, 215, 216, 217, 218, 219], "room", [A("rio", 0.5, "carry", "smile", who="cloak", talk=[0, "@1.9"]), A("ava", 0.52, "hug", [[0, "cry"], ["@3", "surprised"], ["@5", "joy"]], yk=-0.11, facing=-1, talk=["@3", "@3.9"])], [platform(), CLOCK], cam={"z": [1.4, 1.5], "x": [20, 20], "y": [-80, -80]},
  text=[T("\"I'M YOUR GRANDMA'S NEIGHBOR. RIO.\"", 0.5, 0.14, 0.05, size=42), T("\"GRANDMA'S PIGEONS?\"", 0.5, 0.24, "@3", size=44), T("\"THE NAUGHTY ONES.\"", 0.5, 0.34, "@4", size=44)], **STA)
S([220, 221, 222, 223, 224, 225], "room", [A("rio", [[0, 0.5], ["@3", 0.22]], "carry", "determined", who="cloak", walkArms=True), A("ava", [[0, 0.52], ["@3", 0.24]], "hug", "sad", yk=-0.11, facing=-1), A("worker", 0.1, [[0, "relaxed"], ["@3.5", "talk"]], "smile", talk=["@3.5", 1])], [platform(), CLOCK], card=card("IF A CHILD IS LOST", "stay in one place... find a worker... wait", at="@1", x=0.62, w=760), **STA)
S([226, 227, 228, 229], "room", [A("rio", 0.22, "relaxed", "smile", who="cloak"), A("ava", [[0, 0.26], ["@0.5", 0.4]], [[0, "relaxed"], ["@0.6", "hug"]], "joy", facing=[[0, 1]]), A("mom2", [[0, 0.95], ["@0.5", 0.45]], [[0, "relaxed"], ["@0.6", "hug"]], "cry", facing=-1), A("rosa", [[0, 1.05], ["@3", 0.58]], [[0, "relaxed"], ["@3.2", "hug"]], "cry", facing=-1, s=1.5)], [platform(), CLOCK], text=[T("2 MINUTES LATER", 0.5, 0.14, 0.05, size=48), T("MRS. ROSA... SLOWLY", 0.5, 0.24, "@1", size=46)], **STA)
S([230, 231, 232, 233, 234, 235, 236], "room", [A("rio", 0.34, "relaxed", [[0, "nervous"], ["@6", "smile"]], who="cloak", talk=["@2", "@2.9"]), A("rosa", 0.46, [[0, "relaxed"], ["@3", "point"]], [[0, "surprised"], ["@3", "smirk"], ["@6", "joy"]], facing=-1, talk=["@0.5", "@1.9"], s=1.5)], [platform(), CLOCK], cam={"z": [1.4, 1.5], "x": [-150, -150], "y": [-60, -60]},
  text=[T("\"RIO FROM NEXT DOOR.\"", 0.5, 0.14, "@1", size=46), T("\"5 YEARS. YOU NEVER SAID HELLO.\"", 0.5, 0.24, "@3", size=42), T("\"I'M SORRY... HELLO.\"", 0.5, 0.34, "@6", size=46)], **STA)

# ---- the show that never happens ----
S([237, 238, 239], "studio", [A("carla", 0.5, [[0, "relaxed"], ["@1", "crossArms"]], [[0, "neutral"], ["@1", "angry"]])], [{"k": "stage", "x": 0.5, "w": 4}], props=[P("clock", 0.8, 0.3, 45, 0.05)], text=[T("6 PM. NO INVISIBLE MAN.", 0.5, 0.16, 0.05, size=48), T("CARLA IS NOT HAPPY", 0.5, 0.26, "@1", size=46)])
S([240, 241, 242, 243, 244, 245], "city", [A("crowd1", 0.3, "phone", "shocked", hold={"k": "phone"}), A("crowd2", 0.6, "phone", "cry", hold={"k": "phone"}, facing=-1), A("oldwoman", 0.75, "phone", "joy", hold={"k": "phone"}, facing=-1)], [], props=[P("tv", 0.5, 0.35, 90, 0.05)], card=card("30,000,000", "watch it by morning", at="@4", x=0.5, y=0.6, w=640), text=[T("A MAN APPEARS OUT OF THIN AIR", 0.5, 0.14, "@1", size=42)])
S([245], "city", [], []) if False else None

# ---- tea ----
S([246, 247, 248, 249], "room", [A("rosa", 0.2, "holdFront", "smile", hold={"k": "cup"}, talk=["@3", 1], s=1.5), A("rio", 0.4, "relaxed", "surprised", facing=-1)], [door(0.12, open=1)], text=[T("KNOCK KNOCK", 0.15, 0.16, 0.05, size=48), T("\"SO. TEA?\"", 0.3, 0.26, "@3")], **APT)
S([250, 251, 252, 253, 254, 255, 256], "room", [A("rosa", 0.4, "sitTable", "joy", talk=[0, 1], s=1.5), A("rio", 0.64, "sitTable", [[0, "smile"], ["@6", "joy"]], facing=-1, talk=["@6", 1])], [{"k": "table", "x": 0.52, "w": 1.0}, {"k": "dish", "x": 0.46, "food": "cocoa", "at": -1}, {"k": "dish", "x": 0.58, "food": "cocoa", "at": -1}],
  text=[T("LUIS'S CHAIR", 0.64, 0.16, "@1", size=46), T("PIGEONS. LUIS. PINK BOOTS.", 0.5, 0.26, "@3", size=44), T("MORE THAN TEN WORDS", 0.5, 0.36, "@6", size=46)], wall="#c8b8a0", wall2="#7a6a5a")
S([257, 258, 259], "office", [A("rio", 0.4, "explain", "determined", talk=[0, 1]), A("boss", 0.6, "sit", [[0, "surprised"], ["@2", "smile"]], facing=-1), A("crowd1", 0.75, "sit", "surprised", facing=-1)], [{"k": "table", "x": 0.65, "w": 1.4}], text=[T("YOU SPEAK UP IN MEETINGS", 0.5, 0.16, 0.05, size=46), T("THEY START LISTENING", 0.5, 0.26, "@2", size=46)])
S([260, 261], "kitchen", [A("sam", 0.55, "present", "smile", facing=-1, hold={"k": "bagel"}), A("rio", 0.42, "relaxed", "joy")], [], text=[T("SAM BUYS YOU A DONUT", 0.5, 0.16, 0.05, size=48)])
S([262, 263, 264, 265], "park", [A("rosa", 0.4, "crouch", "joy", s=1.5), A("rio", 0.55, "crouch", "smile")], [{"k": "prop", "p": "bird", "x": 0.47, "size": 0.25}, {"k": "prop", "p": "bird", "x": 0.62, "size": 0.25}, {"k": "prop", "p": "bird", "x": 0.3, "size": 0.25}], text=[T("PIGEONS EVERY SATURDAY", 0.5, 0.14, 0.05, size=46), T("THE CLOAK: IN A DRAWER", 0.5, 0.24, "@1", size=44), T("NOT INVISIBLE ANYMORE", 0.5, 0.34, "@3", size=48)])

# ---- science ----
S([266], "space", [], [], text=[T("COULD INVISIBILITY BE REAL?", 0.5, 0.45, 0.05, size=70)])
S([267, 268, 269, 270, 271], "lab", [A("doctor", 0.35, "explain", "smile", talk=[0, 1])], [], card=card("2006", "Duke University + John Pendry", at=0.05, x=0.65, w=640), props=[P("magnet", 0.65, 0.5, 50, "@1")], text=[T("A CLOAK FOR MICROWAVES", 0.65, 0.38, "@1", size=44), T("METAMATERIALS", 0.65, 0.62, "@2", size=46), T("IT WORKED... A LITTLE", 0.65, 0.72, "@3", size=44)])
S([272, 273, 274, 275], "space", [], [], text=[T("VISIBLE LIGHT: MUCH HARDER", 0.5, 0.3, 0.05, size=52), T("TINY WAVES NEED TINIER MATERIALS", 0.5, 0.42, "@1", size=44), T("A TRULY INVISIBLE PERSON IS BLIND", 0.5, 0.54, "@2", size=44)], props=[P("eye", 0.5, 0.74, 50, "@2")])

# ---- teaser ----
S([276, 277, 278, 279], "room", [A("rosa", 0.4, "present", "smile", hold={"k": "towel"}, talk=["@3", 1], s=1.5), A("rio", 0.58, "relaxed", "surprised", facing=-1)], [door(0.15, open=1)], props=[P("bag", 0.45, 0.4, 45, "@2")], text=[T("AN OLD CLOTH BAG", 0.5, 0.16, "@2", size=48), T("\"IT CAN GRAB ANYTHING ON EARTH\"", 0.5, 0.26, "@3", size=44)], **APT)
S([280, 281], "face", [], [], who="rio", expr=[[0, "smile"]])
S([282], "end", [], [], tpl="end")

B[:] = [b for b in B if b is not None]
v3_pass(38)
save(38, 283)
