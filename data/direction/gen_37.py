# Storyboard long_37 "What If You Had A Doctor's Bag That Could Cure Any Disease?"
# Rio works the front desk of a city hospital. The bag glows green when it heals (held at the patient's chest).
from sb import *
def door(x, **kw): d = {"k": "housedoor", "x": x}; d.update(kw); return d
APT = dict(wall="#c8b0a0", wall2="#7a6070", room={"frames": 260, "window": 1250})
WAIT = dict(wall="#c8d4d8", wall2="#7a8a90", room={"window": 1300})
DESK = {"k": "desk", "x": 0.5}
FRIDGE = {"k": "fridge", "x": 0.84}
def bag(**kw): d = {"k": "docbag"}; d.update(kw); return d
def heal(x, glow, pose="reach", expr="determined", **kw): return A("rio", x, pose, expr, hold=bag(glow=glow), **kw)

# ---- cold open: the waiting room ----
S([0, 1], "room", [A("boy", 0.45, "sit", "sad", s=1.6), A("mom2", 0.6, "sit", "worried", facing=-1), A("crowd1", 0.25, "sit", "neutral")], [], text=[T("COUGH! COUGH!", 0.45, 0.32, 0.1, size=56)], **WAIT)
S([2, 3, 4], "room", [A("boy", 0.45, "sit", [[0, "sad"], ["@2.5", "surprised"]]), A("mom2", 0.6, "sit", "worried", facing=-1), heal([[0, 0.2], ["@0.8", 0.39]], ["@1.6", "@2.8"], pose=[[0, "relaxed"], ["@0.9", "reach"]])], [], text=[T("A SOFT GREEN LIGHT", 0.5, 0.16, "@2", size=50), T("THE COUGH STOPS", 0.5, 0.26, "@2.6", size=50)], **WAIT)
S([5, 6], "room", [A("mom2", 0.6, [[0, "sit"], ["@0.5", "relaxed"]], "shocked", facing=-1, talk=["@1", 1]), A("rio", 0.39, "relaxed", "nervous", hold=bag()), A("boy", 0.47, "sit", "happy")], [], text=[T("\"WHAT DID YOU JUST DO?\"", 0.5, 0.16, "@1", size=52)], **WAIT)
S([7, 8, 9], "room", [A("rio", 0.39, [[0, "relaxed"], ["@2", "shrug"]], [[0, "nervous"], ["@2", "smirk"]], hold=bag(to="@1.9"), talk=["@2", 1]), A("mom2", 0.6, "relaxed", "confused", facing=-1)], [], text=[T("\"I HAVE NO IDEA.\"", 0.4, 0.16, "@2", size=54)], **WAIT)

# ---- who you are ----
S([10, 11], "hospital", [A("rio", 0.45, "sitTable", "neutral")], [DESK], card=card("RIO", "front desk, a busy city hospital", at=0.05, x=0.68, w=640))
S([12, 13, 14], "hospital", [A("rio", 0.45, [[0, "sitTable"], ["@2", "explain"]], [[0, "neutral"], ["@1", "sleepy"]], talk=["@2", 1]), A("crowd1", 0.66, "relaxed", "neutral", facing=-1), A("crowd2", 0.78, "relaxed", "sad", facing=-1)], [DESK], props=[P("paper", 0.58, 0.45, 30, 0.1)], text=[T("FORMS. EXCITING?", 0.5, 0.16, 0.05, size=50), T("\"PLEASE WAIT...\" ALL DAY", 0.5, 0.26, "@2", size=46)])
S([15, 16, 17, 18, 19], "hospital", [A("rio", [[0, 0.2], ["@0.8", 0.42]], [[0, "relaxed"], ["@1", "think"], ["@3", "reach"]], [[0, "neutral"], ["@1", "confused"], ["@4", "surprised"]])], [DESK], props=[P("bag", 0.5, 0.58, 40, 0.05), P("letter", 0.6, 0.4, 40, "@4")],
  card=card("LAST MONDAY", "an old doctor's bag on your desk", at=0.05, x=0.68, w=640), text=[T("NO NAME TAG", 0.3, 0.3, "@2", size=46), T("A BRASS CLASP", 0.3, 0.4, "@3", size=46)])
S([20, 21, 22], "hospital", [A("rio", 0.42, "holdFront", "awe", hold={"k": "note"})], [DESK], text=[T("\"HOLD ME NEAR THE SICK.\"", 0.5, 0.16, 0.05, size=52), T("ANY SICKNESS. ANY PERSON.", 0.5, 0.26, "@1", size=48)])
S([23, 24], "hospital", [A("doctor", 0.6, "explain", "neutral", facing=-1)], [], props=[P("pill", 0.3, 0.4, 40, 0.05), P("calendar", 0.42, 0.4, 40, 0.2)], card=card("10 SECONDS", None, at="@1", x=0.3))
S([25, 26, 27], "hospital", [A("rio", 0.42, "relaxed", "thinking", hold=bag())], [], card=card("ONE RULE", "one cure... then it sleeps one hour", at=0.05, x=0.68, w=640), props=[P("clock", 0.68, 0.55, 50, "@1")], text=[T("NO EXCEPTIONS", 0.68, 0.42, "@2", size=46)])
S([28, 29], "space", [], [], card=card("24 PEOPLE A DAY", "on a planet of 8 billion", at=0.05, w=720), props=[P("earth", 0.5, 0.6, 90, 0.2)])
S([30], "room", [], [], tpl="title", params={"title": "What If A Bag Could Cure Any Disease?"})

# ---- day one: a cold ----
S([31, 32, 33], "room", [A("rio", 0.42, [[0, "relaxed"], ["@2", "sad"]], [[0, "neutral"], ["@2", "sleepy"]], hold=bag())], [], card=card("DAY ONE", "you test it on yourself", at=0.05, x=0.7), props=[P("tissue", 0.55, 0.42, 40, "@2")], **APT)
S([34, 35], "room", [], [], tpl="science", params={"sci": "200+ COLD VIRUSES", "icon": "germ"})
S([36, 37, 38, 39], "room", [A("rio", 0.42, [[0, "relaxed"], ["@0.5", "brush"]], [[0, "sleepy"], ["@3", "joy"]], hold=bag(glow=["@1", "@2.9"]))], [], text=[T("GREEN LIGHT", 0.6, 0.16, "@1", size=50), T("10 SECONDS", 0.6, 0.26, "@2", size=50), T("NOSE: CLEAR", 0.6, 0.36, "@3", size=50)], **APT)
S([40, 41], "hospital", [A("rio", 0.42, [[0, "relaxed"], ["@1", "handsOnHead"]], [[0, "joy"], ["@1", "awe"]], hold=bag(to="@0.9"))], [DESK], props=[P("coffee", 0.6, 0.35, 50, 0.1)], text=[T("COFFEE... 3 FLOORS DOWN", 0.6, 0.18, 0.2, size=46), T("IS THIS REAL?", 0.5, 0.3, "@1")])

# ---- day two: the flu ----
S([42, 43, 44], "hospital", [A("mom2", 0.6, "lie", "sad", rot=-1.5708, dy=41), A("rio", 0.38, "relaxed", "worried", hold=bag())], [{"k": "bed", "x": 0.6}], card=card("DAY TWO", "a terrible flu", at=0.05, x=0.25), props=[P("thermometer", 0.62, 0.36, 40, "@1")], text=[T("FEVER. CHILLS. ACHING BONES.", 0.62, 0.22, "@1", size=40)])
S([45, 46], "hospital", [A("mom2", 0.6, [[0, "lie"], ["@1", "sitTable"]], [[0, "sad"], ["@1", "surprised"]], rot=[[0, -1.5708], ["@1", -1.5708], ["@1.3", 0]], yk=[[0, 0.038], ["@1", 0.038], ["@1.3", -0.02]], chair=False), heal(0.5, [0, "@0.95"])], [{"k": "bed", "x": 0.6}], text=[T("GREEN LIGHT", 0.4, 0.2, 0.05)])
S([47, 48, 49, 50], "hospital", [A("mom2", 0.6, "sitTable", "joy", yk=-0.02, chair=False, talk=[0, "@1.9"]), A("rio", 0.42, "relaxed", "smile", hold=bag()), A("nurse", 0.82, [[0, "relaxed"], ["@3", "shocked"]], [[0, "neutral"], ["@3", "shocked"]], facing=-1, hold={"k": "note", "drop": "@3.2"})], [{"k": "bed", "x": 0.6}],
  text=[T("\"A SANDWICH. HAM AND CHEESE.\"", 0.5, 0.14, 0.1, size=46), T("\"EXTRA PICKLES.\"", 0.5, 0.24, "@1", size=46)])

# ---- day four: a superbug ----
S([51, 52, 53, 54], "hospital", [A("oldman", 0.6, "lie", "sleepy", rot=-1.5708, dy=41), A("doctor", 0.78, "sad", "sad", facing=-1)], [{"k": "bed", "x": 0.6}], card=card("DAY FOUR", "things get serious", at=0.05, x=0.25), props=[P("pill", 0.35, 0.42, 40, "@3"), P("cross", 0.35, 0.42, 40, "@3.5")], text=[T("EVERY ANTIBIOTIC... NOTHING WORKS", 0.5, 0.32, "@3", size=44)])
S([55, 56], "hospital", [], [], card=card("~1.27 MILLION", "deaths directly caused by drug-resistant infections, 2019", at="@1", w=920), props=[P("germ", 0.5, 0.62, 80, 0.05)], text=[T("GERMS THAT SURVIVE OUR MEDICINES", 0.5, 0.42, 0.05, size=46)])
S([57, 58, 59], "hospital", [A("oldman", 0.6, "lie", [[0, "sleepy"], ["@2", "neutral"]], rot=-1.5708, dy=41), heal(0.5, ["@0.6", "@2.9"])], [{"k": "bed", "x": 0.6}], text=[T("GREEN LIGHT", 0.4, 0.2, "@1"), T("THE FEVER BREAKS", 0.5, 0.3, "@2", size=50)])
S([60, 61, 62, 63], "hospital", [A("oldman", 0.6, "sitTable", "happy", yk=-0.02, chair=False, talk=["@1", "@2.9"]), A("rio", 0.5, [[0, "shake"], ["@3", "relaxed"]], [[0, "smile"], ["@3", "smirk"]], hold=bag())], [{"k": "bed", "x": 0.6}],
  text=[T("\"THANK YOU, SON.\"", 0.5, 0.14, "@1", size=50), T("\"WHO ARE YOU?\"", 0.5, 0.24, "@2", size=50), T("FRONT DESK", 0.38, 0.4, "@3", size=50)])

# ---- word spreads ----
S([64, 65, 66], "room", [A("crowd1", 0.2, "sit", "worried"), A("crowd2", 0.35, "sit", "sad"), A("oldwoman", 0.5, "sit", "worried"), A("mom2", 0.65, "relaxed", "worried"), A("dad", 0.8, "relaxed", "sad"), A("lily", 0.72, "sad", "sad")], [], card=card("DAY FIVE", "word spreads, fast", at=0.05, y=0.14), **WAIT)
S([67, 68, 69, 70], "city", [A("crowd1", 0.2, "relaxed", "worried"), A("crowd2", 0.3, "relaxed", "sad"), A("oldwoman", 0.4, "relaxed", "worried"), A("dad", 0.62, "relaxed", "sad"), A("mom2", 0.72, "relaxed", "worried")], [{"k": "car", "x": 0.85, "color": "#5a6a8a"}], text=[T("THE HALLWAY. THE PARKING LOT.", 0.5, 0.14, 0.05, size=46), T("FROM 3 STATES AWAY", 0.5, 0.24, "@2", size=46), T("SLEEPING IN THEIR CARS", 0.5, 0.34, "@3", size=46)])
S([71, 72, 73, 74], "city", [A("mom2", 0.35, "photo", "cry", hold={"k": "note"}), A("dad", 0.5, "photo", "sad", hold={"k": "note"}), A("crowd2", 0.65, "wave", "worried"), A("rio", 0.85, "relaxed", "worried", facing=-1, hold=bag())], [], text=[T("PHOTOS OF SICK CHILDREN", 0.45, 0.14, 0.05, size=46), T("ONE PER HOUR", 0.5, 0.24, "@2", size=50), T("HOW DO YOU CHOOSE?", 0.5, 0.34, "@3")])

# ---- Dr. Maya Patel ----
S([75, 76, 77, 78], "hospital", [A("maya", [[0, 0.85], ["@0.8", 0.6]], "relaxed", "smile", facing=-1), A("rio", 0.4, "sad", "sleepy", hold=bag())], [], card=card("DR. MAYA PATEL", "runs the emergency room, 20 years", at="@1", x=0.5, w=760), text=[T("TIRED EYES. KIND VOICE.", 0.5, 0.36, "@3", size=46)])
S([79, 80, 81], "hospital", [A("maya", 0.6, "explain", "smile", facing=-1, talk=[0, "@0.95"]), A("rio", 0.4, [[0, "relaxed"], ["@2", "sit"]], "sleepy")], [], text=[T("\"YOU LOOK LIKE YOU HAVEN'T SLEPT\"", 0.5, 0.14, 0.05, size=46), T("\"RIO, SIT.\"", 0.5, 0.24, "@2")])
S([82, 83, 84, 85, 86], "hospital", [A("maya", 0.6, "explain", "neutral", facing=-1, talk=[0, 1]), A("rio", 0.4, "sit", "thinking")], [], card=card("TRIAGE", "from a French word: to sort", at="@1", x=0.5, w=660), text=[T("NOT IN ORDER OF ARRIVAL", 0.5, 0.36, "@2", size=46), T("THE SICKEST FIRST", 0.5, 0.46, "@3", size=50)])
S([87, 88, 89], "hospital", [A("maya", 0.6, "tap", "smile", facing=-1), A("rio", 0.42, "sit", "thinking")], [], cam={"z": [1.5, 1.6], "x": [190, 190], "y": [-80, -80]}, props=[P("note", 0.62, 0.45, 40, 0.05)], text=[T("THREE WORDS, IN RED", 0.5, 0.14, "@1", size=46), T("ONE AT A TIME", 0.5, 0.24, "@2", color="#ff6a5a")])
S([90, 91, 92, 93], "hospital", [A("maya", 0.6, "explain", "sad", facing=-1, talk=[0, 1]), A("rio", 0.42, "sit", "neutral")], [], text=[T("\"YOU CAN'T SAVE EVERYBODY AT ONCE\"", 0.5, 0.14, 0.05, size=46), T("\"NOBODY CAN.\"", 0.5, 0.24, "@1"), T("ONE. THEN THE NEXT.", 0.5, 0.34, "@2", size=50)])
S([94, 95, 96], "hospital", [A("rio", 0.45, [[0, "sit"], ["@1", "relaxed"]], [[0, "neutral"], ["@1", "determined"]], talk=["@2", 1]), A("maya", 0.62, "relaxed", "smile", facing=-1)], [], text=[T("\"ONE AT A TIME.\"", 0.45, 0.16, "@2", color="#ff6a5a")])

# ---- the system ----
S([97, 98, 99, 100, 101], "hospital", [A("doctor", 0.25, "point", "neutral"), A("maya", 0.38, "explain", "neutral"), A("rio", 0.6, "relaxed", "determined", facing=-1, hold=bag())], [], card=card("WEEK TWO", "you and Maya make a system", at=0.05, x=0.72, w=600), text=[T("THE DOCTORS CHOOSE.", 0.5, 0.36, "@2", size=46), T("YOU HEAL.", 0.5, 0.46, "@3", size=50), T("EVERY HOUR, ON THE HOUR", 0.5, 0.56, "@4", size=44)])
S([102, 103], "hospital", [A("lily", 0.6, "lie", "sleepy", rot=-1.5708, dy=41), heal(0.5, ["@0.8", 1])], [{"k": "bed", "x": 0.6}], text=[T("A FAILING HEART", 0.5, 0.16, 0.05, size=50), T("GREEN LIGHT", 0.5, 0.26, "@1", size=46)])
S([104, 105], "hospital", [A("crowd2", 0.6, "lie", "sleepy", rot=-1.5708, dy=41), heal(0.5, ["@0.8", 1])], [{"k": "bed", "x": 0.6}], text=[T("A TEACHER WITH CANCER", 0.5, 0.16, 0.05, size=50), T("GREEN LIGHT", 0.5, 0.26, "@1", size=46)])
S([106, 107, 108], "hospital", [heal(0.45, ["@0.8", "@1.9"]), A("mom2", 0.68, [[0, "relaxed"], ["@2", "kneel"]], [[0, "worried"], ["@2", "cry"]], facing=-1), A("dad", 0.8, [[0, "relaxed"], ["@2", "kneel"]], [[0, "worried"], ["@2", "cry"]], facing=-1)], [{"k": "bed", "x": 0.55}], props=[P("baby", 0.56, 0.52, 40, 0.05)], text=[T("A BABY WHO CAN'T BREATHE ALONE", 0.5, 0.14, 0.05, size=46), T("GREEN LIGHT", 0.5, 0.24, "@1", size=46)])
S([109, 110], "street", [A("rio", [[0, 0.1], [1, 0.45]], "relaxed", [[0, "cry"], ["@1", "smile"]], hold=bag())], [], fx=["night"], text=[T("SHAKING... IN A GOOD WAY", 0.5, 0.18, "@1", size=50)])

# ---- the cost ----
S([111, 112, 113, 114], "bedroom", [A("rio", 0.47, [[0, "lie"], ["@2", "lie"]], [[0, "sleepy"], ["@2", "shocked"]], rot=-1.5708, dy=52, who="rioPj")], [{"k": "alarm", "x": 0.3}], fx=["night"], text=[T("BUT THERE'S A COST", 0.5, 0.16, 0.05, size=50), T("BEEP! EVERY HOUR. ALL NIGHT.", 0.5, 0.26, "@2", size=46)])
S([115], "bedroom", [A("rio", 0.4, "sit", "sleepy", who="rioPj")], [], fx=["night"], text=[T("EVERY HOUR ASLEEP = ONE PERSON NOT HELPED", 0.5, 0.18, 0.1, size=40)])
S([116, 117], "room", [], [], card=card("17-19 HOURS AWAKE", "reactions as slow as after drinking alcohol", at=0.05, w=860), props=[P("brain", 0.5, 0.62, 80, 0.2)], text=[T("YOU: 30 HOURS", 0.5, 0.45, "@1", color="#ff6a5a")], **APT)
S([118, 119, 120], "room", [A("rio", [[0, 0.5], ["@0.6", 0.72]], [[0, "relaxed"], ["@0.7", "reach"], ["@1", "talk"], ["@2", "facepalm"]], "sleepy", talk=["@1", "@1.9"])], [FRIDGE], text=[T("KEYS IN THE FRIDGE", 0.5, 0.16, 0.2, size=50), T("\"THANKS... MOM\"", 0.4, 0.26, "@1", size=46), T("IS THIS HELPING ANYONE?", 0.5, 0.36, "@2", size=46)], **APT)

# ---- the world finds out ----
S([121, 122, 123, 124], "city", [A("crowd1", 0.2, "photo", "neutral", hold={"k": "camera", "flash": 70}), A("crowd2", 0.35, "point", "shocked"), A("oldman", 0.6, "wave", "joy"), A("rio", 0.85, "relaxed", "nervous", facing=-1, hold=bag())], [], card=card("WEEK THREE", "the world finds out", at=0.05, x=0.5, y=0.14), props=[P("helicopter", 0.3, 0.3, 50, "@1"), P("camera", 0.7, 0.3, 40, "@1")], text=[T("\"RIO! RIO!\"", 0.5, 0.36, "@3", size=56)])
S([125, 126, 127, 128], "city", [], [], props=[P("tv", 0.5, 0.45, 120, 0.05)], text=[T("HERO?", 0.25, 0.25, 0.05), T("FAKE?", 0.75, 0.25, "@1", color="#ff6a5a"), T("WHO'S RIGHT?", 0.5, 0.72, "@2", size=56), T("\"GIVE IT TO THE GOVERNMENT\"", 0.5, 0.84, "@3", size=44)])

# ---- Gordon Steele ----
S([129, 130, 131], "street", [A("gordon", [[0, 0.62], ["@1.3", 0.62], ["@1.9", 0.5]], "relaxed", "neutral", facing=-1, alpha=[[0, 0], ["@1", 0], ["@1.2", 1]]), A("rio", 0.3, "relaxed", "surprised", hold=bag())], [{"k": "car", "x": 0.7, "color": "#c8ccd4"}], fx=["night"], card=card("GORDON STEELE", "one of the richest men in the world", at="@1.5", x=0.5, w=760))
S([132, 133, 134, 135, 136, 137], "street", [A("gordon", 0.5, [[0, "talk"], ["@1", "kneel"], ["@2", "explain"], ["@3", "point"]], [[0, "neutral"], ["@1", "sad"], ["@3", "neutral"]], facing=-1, talk=[0, 1]), A("rio", 0.32, "relaxed", "thinking", hold=bag())], [{"k": "car", "x": 0.75, "color": "#c8ccd4"}], fx=["night"],
  text=[T("\"MY KNEES ARE RUINED\"", 0.5, 0.14, "@1", size=48), T("\"20 YEARS OF PAIN\"", 0.5, 0.24, "@2", size=46), T("\"HEAL ME TONIGHT. 9 O'CLOCK.\"", 0.5, 0.34, "@3", size=46)])
S([138, 139, 140, 141, 142], "street", [A("gordon", 0.5, "explain", "smirk", facing=-1, talk=[0, "@2.9"]), A("rio", 0.32, [[0, "relaxed"], ["@3", "think"]], [[0, "surprised"], ["@3", "thinking"]], hold=bag())], [{"k": "car", "x": 0.75, "color": "#c8ccd4"}], fx=["night"],
  card=card("$1,000,000,000", "to build 10 new hospitals", at=0.05, x=0.5, w=760), props=[P("hospital", 0.25, 0.62, 50, "@2"), P("hospital", 0.35, 0.62, 50, "@2.2"), P("hospital", 0.45, 0.62, 50, "@2.4")], text=[T("THOUSANDS OF LIVES? MORE?", 0.5, 0.42, "@4", size=46)])
S([143, 144, 145, 146], "street", [A("gordon", [[0, 0.5], ["@2.5", 0.5], ["@3", 0.7]], [[0, "point"], ["@2", "crossArms"]], "neutral", facing=[[0, -1], ["@2.6", 1]], talk=["@1", "@2.9"], alpha=[["@3", 1], ["@3.3", 0]]), A("rio", 0.32, "relaxed", "nervous", hold=bag())], [{"k": "car", "x": [[0, 0.75], ["@3.3", 0.75], [1, 1.3]], "color": "#c8ccd4"}], fx=["night"],
  text=[T("\"NINE O'CLOCK EXACTLY.\"", 0.5, 0.14, "@1", size=48), T("\"I DON'T WAIT FOR ANYONE.\"", 0.5, 0.24, "@3", size=46)])

# ---- Noah ----
S([147, 148, 149, 150, 151], "room", [A("noah", 0.4, [[0, "wave"], ["@2", "relaxed"]], "joy"), A("rio", 0.55, "relaxed", "smile", facing=-1)], [door(0.2, open=1)], card=card("NOAH", "8, lives next door", at="@1", x=0.72, w=560), text=[T("RED SNEAKERS", 0.72, 0.38, "@3", size=44), T("TWO FRONT TEETH MISSING", 0.72, 0.46, "@4", size=40)], **APT)
S([152, 153, 154, 155, 156], "room", [A("noah", 0.42, [[0, "relaxed"], ["@1", "present"]], "joy", hold={"k": "note", "from": "@1"}), A("rio", 0.55, [[0, "relaxed"], ["@3", "holdFront"]], [[0, "smile"], ["@4", "joy"]], facing=-1)], [door(0.2, open=1)], props=[P("crown", 0.5, 0.3, 50, "@2"), P("bag", 0.56, 0.3, 40, "@3")], text=[T("A DRAWING EVERY AFTERNOON", 0.5, 0.14, "@1", size=46), T("\"SUPER RIO\"", 0.5, 0.42, "@4", color="#5ad28a")], **APT)
S([157, 158, 159, 160, 161], "room", [A("noah", 0.42, "cheer", "joy", talk=[0, "@0.9"]), A("rio", 0.55, "relaxed", [[0, "smile"], ["@4", "happy"]], facing=-1)], [], text=[T("\"ONE AT A TIME!\"", 0.42, 0.16, 0.05, color="#ff6a5a"), T("HE HEARD IT ON TV", 0.5, 0.26, "@1", size=46), T("YOU LOVE HIM FOR IT", 0.5, 0.36, "@4", size=46)], **APT)
S([162, 163], "room", [A("rio", [[0, 0.5], ["@0.5", 0.72]], [[0, "relaxed"], ["@0.6", "reach"]], "smile")], [FRIDGE, {"k": "paper", "x": 0.84, "up": 1.3, "s": "SUPER RIO"}], cam={"z": [1.3, 1.5], "x": [420, 480], "y": [-60, -60]}, text=[T("NEXT TO YOUR KEYS", 0.5, 0.16, "@1", size=46)], **APT)

# ---- Friday night ----
S([164, 165, 166, 167], "room", [A("rio", 0.42, [[0, "relaxed"], ["@2", "crossArms"]], "determined", who="rioSuit", hold=bag())], [FRIDGE], card=card("FRIDAY, 8:15 PM", "the car comes at 8:40", at=0.05, x=0.7, w=600), props=[P("clock", 0.7, 0.55, 50, "@3")], **APT)
S([168, 169, 170, 171], "room", [A("rio", 0.42, "think", "smirk", who="rioSuit", hold=bag())], [FRIDGE], thought={"props": ["money", "hospital"], "x": 0.7, "y": 0.28, "at": 0.05}, text=[T("9 O'CLOCK. $1 BILLION. 10 HOSPITALS.", 0.5, 0.56, "@1", size=40), T("EASY CHOICE. RIGHT?", 0.5, 0.66, "@3", size=46)], **APT)
S([172, 173, 174], "room", [A("rio", [[0, 0.42], ["@0.6", 0.32]], "relaxed", [[0, "surprised"], ["@1", "shocked"]], who="rioSuit", facing=-1, hold=bag()), A("mom2", 0.18, "carry", "cry", talk=["@2", 1]), A("noah", 0.18, "lie", "sleepy", rot=1.5708, yk=-0.12, s=1.6)], [door(0.12, open=[[0, 0], ["@0.3", 1]])], text=[T("BANG! BANG!", 0.2, 0.16, 0.05), T("\"RIO. PLEASE.\"", 0.3, 0.26, "@2")], **APT)
S([175, 176, 177, 178], "room", [A("mom2", 0.3, "carry", "cry", talk=[0, 1]), A("noah", 0.33, "lie", "sleepy", rot=1.5708, yk=-0.12), A("rio", 0.48, "kneel", "scared", who="rioSuit", facing=-1, hold=bag())], [], props=[P("bandage", 0.3, 0.42, 40, 0.05), P("thermometer", 0.42, 0.42, 40, "@1")],
  text=[T("\"A SMALL CUT, TWO DAYS AGO\"", 0.5, 0.14, 0.05, size=44), T("\"NOW HE'S BURNING HOT\"", 0.5, 0.24, "@1", size=44), T("\"HE DOESN'T KNOW WHO I AM\"", 0.5, 0.34, "@3", size=44)], **APT)
S([179, 180, 181, 182, 183], "room", [A("mom2", 0.3, "carry", "cry"), A("noah", 0.33, "lie", "sleepy", rot=1.5708, yk=-0.12), A("rio", 0.42, "kneel", "worried", who="rioSuit", facing=-1, hold=bag())], [], cam={"z": [1.5, 1.6], "x": [-250, -250], "y": [-20, -20]},
  text=[T("PALE, CLAMMY SKIN", 0.62, 0.16, "@1", size=44), T("LIPS A LITTLE BLUE", 0.62, 0.26, "@2", size=44), T("HEART RACING", 0.62, 0.36, "@3", size=44)])
S([184, 185], "room", [A("rio", 0.42, "kneel", "scared", who="rioSuit", facing=-1, hold=bag())], [], card=card("SEPSIS?", None, at="@1", x=0.68), **APT)
S([186, 187, 188, 189, 190, 191], "hospital", [A("maya", 0.25, "explain", "worried", talk=[0, 1])], [], card=card("SEPSIS", "the body's response to infection attacks its own organs", at=0.05, w=900), props=[P("bandage", 0.5, 0.62, 40, "@2"), P("germ", 0.62, 0.62, 40, "@3"), P("lungs", 0.74, 0.62, 40, "@4")],
  text=[T("IT CAN START SMALL", 0.6, 0.42, "@1", size=46), T("~11 MILLION DEATHS A YEAR, WORLDWIDE", 0.6, 0.78, "@5", size=40)])
S([192, 193, 194, 195, 196, 197, 198], "hospital", [A("maya", 0.25, "point", "worried", talk=[0, 1])], [], card=card("WARNING SIGNS", None, at=0.05, x=0.62, y=0.14),
  text=[T("FEVER, OR FEELING VERY COLD", 0.62, 0.32, "@1", size=40), T("FAST BREATHING", 0.62, 0.4, "@2", size=40), T("RACING HEART. CONFUSION.", 0.62, 0.48, "@3", size=40), T("CLAMMY SKIN", 0.62, 0.56, "@4", size=40), T("EXTREME PAIN", 0.62, 0.64, "@5", size=40), T("IT GETS WORSE FAST", 0.62, 0.74, "@6", size=46, color="#ff6a5a")])

# ---- the choice ----
S([199, 200, 201, 202], "room", [A("rio", 0.42, "kneel", "worried", who="rioSuit", facing=-1, hold=bag(glow=[0, "@0.9"])), A("mom2", 0.3, "carry", "cry"), A("noah", 0.33, "lie", "sleepy", rot=1.5708, yk=-0.12)], [], card=card("8:20 PM", None, at="@1", x=0.72), text=[T("HEAL NOAH = BAG ASLEEP TILL 9:20", 0.6, 0.36, "@2", size=40), T("STEELE DOESN'T WAIT", 0.6, 0.46, "@3", size=46)], **APT)
S([203, 204, 205, 206], "room", [A("rio", 0.45, [[0, "kneel"], ["@0.5", "phoneEar"]], "nervous", who="rioSuit", facing=-1, hold={"k": "phone", "from": "@0.5"})], [], inset={"who": "pilot", "label": "THE DRIVER", "talk": True, "at": "@1", "x": 0.78}, text=[T("\"I'M OUTSIDE, MR. RIO.\"", 0.45, 0.16, "@2", size=48)], **APT)
S([207, 208, 209, 210], "room", [A("rio", 0.45, "relaxed", "worried", who="rioSuit", facing=[[0, -1], ["@1", 1], ["@2", -1]], hold=bag())], [], props=[P("child", 0.2, 0.4, 50, 0.05) if False else P("heart", 0.2, 0.4, 50, 0.05), P("car", 0.8, 0.4, 50, "@1")], text=[T("$1 BILLION FOR 10 HOSPITALS...", 0.5, 0.14, "@2", size=44), T("...OR ONE LITTLE BOY, NOW", 0.5, 0.24, "@2.5", size=44), T("WHAT WOULD YOU DO?", 0.5, 0.58, "@3")], **APT)
S([211, 212, 213, 214, 215], "room", [A("rio", 0.45, [[0, "relaxed"], ["@1", "handsOnHead"]], [[0, "scared"], ["@2", "sleepy"], ["@4", "determined"]], who="rioSuit", facing=-1, hold=bag())], [], inset={"who": "maya", "label": "MAYA (MEMORY)", "talk": True, "at": "@3", "x": 0.78}, text=[T("2 DAYS WITHOUT SLEEP", 0.5, 0.16, "@2", size=46), T("\"ONE AT A TIME.\"", 0.5, 0.26, "@4", color="#ff6a5a")], **APT)
S([216, 217, 218], "room", [A("rio", [[0, 0.45], ["@0.5", 0.42]], [[0, "relaxed"], ["@0.6", "kneel"], ["@1.5", "carry"]], "determined", who="rioSuit", facing=-1, hold=bag(glow=["@2", 1])), A("mom2", 0.3, "carry", "cry"), A("noah", 0.33, "lie", "sleepy", rot=1.5708, yk=-0.12)], [], text=[T("GREEN LIGHT", 0.5, 0.16, "@2")], **APT)
S([219, 220, 221, 222, 223, 224, 225, 226], "room", [A("rio", 0.42, "carry", "determined", who="rioSuit", facing=-1, hold=bag(glow=[0, "@5.8"])), A("mom2", 0.3, "carry", [[0, "cry"], ["@6", "shocked"]]), A("noah", 0.33, "lie", [[0, "sleepy"], ["@3", "neutral"], ["@7", "happy"]], rot=1.5708, yk=-0.12, talk=["@7", 1])], [],
  cam={"z": [1.4, 1.6], "x": [-250, -250], "y": [-20, -20]}, text=[T("1 SECOND", 0.62, 0.14, 0.02, size=46), T("2 SECONDS", 0.62, 0.22, "@1", size=46), T("5 SECONDS", 0.62, 0.3, "@3", size=46), T("10 SECONDS", 0.62, 0.38, "@5", size=46), T("\"SUPER RIO?\"", 0.4, 0.46, "@7", color="#5ad28a")], **APT)
S([227, 228, 229], "room", [A("mom2", 0.3, "hug", "cry"), A("noah", 0.36, "hug", "happy", facing=-1), A("rio", 0.6, [[0, "relaxed"], ["@1", "phoneEar"]], "smile", who="rioSuit", facing=-1, hold={"k": "phone", "from": "@1"})], [], props=[P("ambulance", 0.8, 0.3, 50, "@1")], text=[T("YOU CALL AN AMBULANCE ANYWAY", 0.5, 0.16, "@1", size=44), T("A DOCTOR SHOULD STILL CHECK HIM", 0.5, 0.26, "@2", size=42)], **APT)

# ---- no deal ----
S([230, 231, 232, 233, 234], "street", [A("rio", [[0, 0.1], ["@1", 0.45]], [[0, "relaxed"], ["@2", "talk"]], "smile", who="rioSuit", talk=["@2", 1], hold=bag()), A("pilot", 0.6, "relaxed", "neutral", facing=-1)], [{"k": "car", "x": 0.75, "color": "#c8ccd4"}], fx=["night"], text=[T("\"THE BAG IS ASLEEP\"", 0.5, 0.14, "@3", size=48), T("\"I CAN HEAL HIM AT 9:20\"", 0.5, 0.24, "@4", size=46)])
S([235, 236, 237, 238, 239], "street", [A("rio", 0.45, "relaxed", [[0, "neutral"], ["@2", "sad"]], who="rioSuit", hold=bag()), A("pilot", [[0, 0.6], ["@3", 0.6], ["@3.3", 0.75]], [[0, "phoneEar"], ["@1", "shrug"]], "neutral", facing=-1, hold={"k": "phone", "to": "@0.95"}, talk=["@2", "@2.9"], alpha=[["@3.2", 1], ["@3.4", 0]])], [{"k": "car", "x": [[0, 0.75], ["@3.4", 0.75], [1, 1.4]], "color": "#c8ccd4"}], fx=["night"],
  text=[T("\"MR. STEELE SAYS NO DEAL.\"", 0.5, 0.16, "@2", size=48), T("$1 BILLION... DRIVES AWAY", 0.5, 0.26, "@4", size=48)])
S([240, 241, 242, 243, 244], "street", [A("rio", 0.45, "sit", [[0, "sad"], ["@2", "joy"]], who="rioSuit", chair=False, yk=0.03, hold=bag())], [], fx=["night"], text=[T("ON THE CURB. IN YOUR BEST SHIRT.", 0.5, 0.16, 0.05, size=44), T("HA... HA HA", 0.5, 0.26, "@2", size=54), T("YOU'D DO IT AGAIN", 0.5, 0.36, "@4", size=50)])

# ---- Maya calls ----
S([245, 246, 247, 248], "room", [A("rio", 0.42, "phoneEar", [[0, "sleepy"], ["@2", "nervous"]], hold={"k": "phone"}, talk=["@1.8", "@2.9"])], [], inset={"who": "maya", "label": "MAYA", "talk": True, "at": 0, "x": 0.75}, text=[T("\"A BILLION... FOR A KID WITH SEPSIS?\"", 0.42, 0.16, "@1", size=42), T("\"WAS THAT STUPID?\"", 0.42, 0.26, "@2", size=46)], **APT)
S([249, 250], "room", [A("rio", 0.42, "phoneEar", [[0, "nervous"], ["@1", "cry"]], hold={"k": "phone"})], [], inset={"who": "maya", "label": "MAYA", "talk": True, "at": 0, "x": 0.75, "expr": [[0, "smile"]]}, text=[T("\"THAT'S THE MOST DOCTOR THING", 0.42, 0.16, "@1", size=44), T("I'VE EVER HEARD.\"", 0.42, 0.26, "@1.3", size=44)], **APT)

# ---- the story spreads ----
S([251, 252, 253, 254, 255], "city", [A("mom2", 0.3, "phone", "worried", hold={"k": "phone"}), A("dad", 0.62, "phone", "neutral", hold={"k": "phone"}, facing=-1)], [], props=[P("tv", 0.5, 0.3, 90, 0.05)], text=[T("NOAH'S STORY SPREADS... NOT THE BAG", 0.5, 0.14, "@1", size=42), T("FEVER. FAST BREATHING.", 0.5, 0.54, "@2", size=44), T("CONFUSION. CLAMMY SKIN.", 0.5, 0.62, "@3", size=44)])
S([256, 257, 258, 259], "hospital", [A("mom2", 0.35, "talk", "worried", talk=[0, "@1.9"]), A("doctor", 0.55, "explain", "smile", facing=-1), A("nurse", 0.75, "point", "smile", facing=-1)], [], text=[T("\"COULD IT BE SEPSIS?\"", 0.5, 0.14, 0.05, size=50), T("NURSES SHARE IT. SCHOOLS SHARE IT.", 0.5, 0.24, "@2", size=44)])
S([260, 261], "hospital", [A("maya", 0.45, "explain", "smile", talk=[0, 1]), A("rio", 0.62, "relaxed", "happy", facing=-1)], [], card=card("A MONTH LATER", "more early cases caught than ever", at=0.05, x=0.5, w=700), text=[T("MANY NEVER NEEDED THE BAG", 0.5, 0.4, "@1", size=46)])
S([262, 263, 264, 265], "city", [], [], props=[P("money", 0.3, 0.5, 50, 0.1), P("coin", 0.5, 0.5, 50, "@1"), P("heart", 0.7, 0.5, 50, "@2")], text=[T("$5. $10.", 0.5, 0.3, "@1", size=60), T("FROM THOUSANDS OF STRANGERS", 0.5, 0.7, "@3", size=48)])
S([266, 267, 268], "hospital", [A("noah", 0.4, "cheer", "joy"), A("rio", 0.6, "relaxed", "happy", facing=-1), A("mom2", 0.25, "relaxed", "smile")], [door(0.5), {"k": "sign", "x": 0.5, "y": 0.4, "s": "NOAH WING"}], card=card("ONE NEW CHILDREN'S WING", "not ten hospitals", at=0.05, w=760))

# ---- what changes ----
S([269, 270, 271, 272, 273, 274], "bedroom", [A("rio", 0.47, [[0, "lie"]], "sleepy", rot=-1.5708, dy=52, who="rioPj", zzz=True)], [], fx=["night"], text=[T("NO MORE HOURLY ALARMS", 0.5, 0.14, "@1", size=46), T("HEAL BY DAY. SLEEP AT NIGHT.", 0.5, 0.24, "@3", size=46), T("THE DOCTORS HANDLE THE REST", 0.5, 0.34, "@5", size=44)])
S([275, 276, 277], "hospital", [A("maya", 0.4, "relaxed", "smile"), A("rio", 0.55, "relaxed", "determined", facing=-1, hold=bag())], [], text=[T("YOU CAN'T SAVE EVERYONE", 0.5, 0.16, "@1", size=50), T("BUT YOU CAN SAVE THE NEXT ONE", 0.5, 0.26, "@2", size=48)])
S([278, 279, 280, 281], "room", [A("noah", [[0, 0.15], ["@1", 0.4]], "wave", "joy"), A("rio", 0.55, "relaxed", "smile", facing=-1)], [door(0.12, open=1)], text=[T("KNOCK KNOCK", 0.15, 0.16, "@1", size=50), T("ONE NEW FRONT TOOTH", 0.5, 0.26, "@3", size=46)], **APT)
S([282, 283, 284, 285, 286, 287, 288, 289], "room", [A("noah", 0.4, "present", "joy", hold={"k": "note"}), A("rio", 0.55, [[0, "relaxed"], ["@4", "joy"]], "smile", facing=-1)], [], props=[P("bed", 0.78, 0.4, 50, "@3")], text=[T("NO CAPE. NO BAG.", 0.5, 0.12, "@1", size=46), T("JUST YOU... ASLEEP ON THE COUCH", 0.5, 0.2, "@3", size=42), T("\"SUPER RIO. TAKING A NAP.\"", 0.5, 0.28, "@5", size=44, color="#5ad28a"), T("ONE AT A TIME", 0.5, 0.36, "@7", size=44, color="#ff6a5a")], **APT)
S([290, 291], "room", [A("rio", 0.72, "reach", "happy")], [FRIDGE, {"k": "paper", "x": 0.84, "up": 1.1, "s": "SUPER RIO, NAP"}], cam={"z": [1.4, 1.5], "x": [440, 460], "y": [-60, -60]}, text=[T("RIGHT IN THE MIDDLE", 0.5, 0.16, "@1", size=48)], **APT)

# ---- teaser ----
S([292, 293, 294], "bedroom", [A("rio", 0.4, "relaxed", [[0, "neutral"], ["@1", "shocked"]], alpha=[[0, 1], ["@1", 1], ["@1.3", 0.35], ["@1.6", 1], ["@2", 0.25]])], [{"k": "glass", "x": 0.6}], fx=["night"], text=[T("YOUR REFLECTION FLICKERS", 0.5, 0.16, 0.2, size=48), T("...INVISIBLE?", 0.5, 0.26, "@2")])
S([295, 296], "face", [], [], who="rio", expr=[[0, "smile"]])
S([297], "end", [], [], tpl="end")

v3_pass(37)
save(37, 298)
