# Storyboard for long_31 "What If You Owned Doraemon's Anywhere Door In Real Life?"
# Written by reading the script line by line. Times "@n.f" = sentence n of the shot + fraction f.
import json, os
B = []
def S(lines, set_, actors=(), items=(), **kw):
    d = {"lines": list(lines) if not isinstance(lines, int) else [lines], "set": set_.split(":")[0], "actors": list(actors), "items": list(items)}
    if ":" in set_: d["smood"] = set_.split(":")[1]
    d.update(kw); B.append(d)
def A(id_, x, pose="relaxed", expr="neutral", **kw):
    d = {"id": id_, "who": id_, "x": x, "pose": pose if isinstance(pose, list) else [[0, pose]], "expr": expr if isinstance(expr, list) else [[0, expr]]}
    d.update(kw); return d
def card(big, small=None, at=0.12, **kw): d = {"big": big, "small": small, "at": at}; d.update(kw); return d
def prop(p, x, size=0.5, up=0.0, **kw): d = {"k": "prop", "p": p, "x": x, "size": size, "up": up}; d.update(kw); return d
def door(x, **kw): d = {"k": "door", "x": x}; d.update(kw); return d
HALL = dict(wall="#d8b898", wall2="#8a6a5a", room={"frames": 300})
NIGHT_ROOM = dict()
KNOB = 0.564   # Rio's x when his hand is on the knob of a door at x = 0.64

# ---- 0-12: cold open (approved demo storyboard) ----
demo = json.load(open(os.path.join(os.path.dirname(__file__), "long_41.json")))
for b in demo[:13]: B.append(b)

S([13], "night", [A("rio", [[0, 0.42], [0.6, 0.5]], [[0, "think"], [0.6, "reach"]], "confused", who="rioPj")], [door(0.6, front=True)], cam={"z": [1.2, 1.3], "x": [80, 120]})
S([14], "night", [A("rio", 0.44, "shrug", "smirk", who="rioPj")], [door(0.6)], cam={"z": [1.0, 1.0]})
S([15, 16, 17, 18], "room", [A("rio", [[0, KNOB], ["@2.8", KNOB], ["@3.6", 0.64]], [[0, "knob"], ["@1", "think"], ["@2", "knob"]], [[0, "smile"], ["@1", "thinking"], ["@3", "joy"]], alpha=[["@3.5", 1], ["@3.9", 0]])],
  [door(0.64, open=[["@2.1", 0], ["@2.6", 1]], inside="sunset", sparkle=True)], thought={"props": ["globe"], "x": 0.3, "y": 0.25, "at": "@1"}, cam={"z": [1.1, 1.25], "x": [0, 120]}, **HALL)
S([19, 20], "highway", [], [prop("car", 0.2, 1.2, dx=[[0, 0], [1, 0.05]]), prop("bus", 0.45, 1.6, dx=[[0, 0], [1, 0.03]]), prop("car", 0.7, 1.2)], card=card("27 MIN", "average commute in the US... one way"), fx=["speed"])
S([21], "highway", [], [prop("car", 0.3, 1.2), prop("car", 0.6, 1.2)], card=card("4.5 HOURS", "every week, just getting to work"))
S([22], "room", [A("rio", [[0, 0.64], [0.6, 0.5]], "holdCup", "smirk", hold={"k": "cup"}, alpha=[[0, 0], [0.15, 1]])], [door(0.64, open=[[0, 1], [0.7, 1], [0.95, 0]], inside="office")], card=card("0 SECONDS", None, at=0.3), **HALL)
S([23], "room", [A("rio", 0.45, "pointUp", "determined")], [door(0.64)], card=card("ONE RULE", None, at=0.3), **HALL)
S([24], "room", [A("rio", 0.42, "think", "thinking")], [door(0.64, open=[[0, 0], [0.2, 1]], inside="sunset"), prop("hourglass", 0.82, 0.6, up=1.6, disc=True)], card=card("60 SECONDS", "the door stays open", x=0.3), **HALL)
S([25], "room", [A("rio", 0.42, [[0, "relaxed"], ["@0.95", "handsOnHead"]], [[0, "neutral"], ["@0.95", "shocked"]])], [door(0.64, open=[[0, 1], ["@0.9", 1], ["@1.0", 0]], inside="sunset"), prop("clock", 0.82, 0.5, up=1.6, disc=True, a=[["@0.9", 0], ["@1.1", 1]])],
  card=card("1 HOUR", "to recharge", at="@1.1", x=0.3), sfx=[{"at": 1.2, "name": "whoosh", "gain": -12}], **HALL)
S([26, 27], "room", [A("rio", 0.4, [[0, "cheer"], ["@1", "sit"]], [[0, "joy"], ["@1", "sleepy"]])], [door(0.64), prop("clock", 0.78, 0.5, up=1.7, disc=True, a=[["@1", 0], ["@1.2", 1]])],
  card=card("1 MIN", "of magic", x=0.3, at=0.05), **HALL)
S([28], "room", [], [], tpl="title", params={"title": "What If You Owned The Anywhere Door?"})
S([29, 30], "office", [A("rio", 0.42, "type", "neutral"), A("max", 0.66, "sit", "neutral", facing=-1)], [{"k": "desk", "x": 0.45}], card=card("DAY ONE", "lunch break", at=0.05))
S([31, 32], "office", [A("rio", 0.42, [[0, "think"], ["@1", "cheer"]], [[0, "thinking"], ["@1", "joy"]])], [{"k": "desk", "x": 0.7}], thought={"props": ["fire"], "s": "RAMEN", "x": 0.3, "y": 0.23}, card=card("TOKYO", "real ramen", at="@1", x=0.7))
S([33], "street", [A("rio", [[0, 0.4], ["@0.6", 0.4], ["@1", 0.5]], "holdCup", [[0, "smile"], ["@0.6", "shocked"]])], [door(0.4, open=[[0, 0], [0.25, 1]], inside="office"), {"k": "shop", "x": 0.72, "s": "RAMEN", "closed": True}], fx=["night"], cam={"z": [1.0, 1.1]})
S([34], "street", [A("rio", 0.5, "shrug", "sad")], [door(0.4, open=1, inside="office"), {"k": "shop", "x": 0.72, "s": "RAMEN", "closed": True}], fx=["night"])
S([35], "street", [], [], fx=["night"], card=card("12 PM CHICAGO = 3 AM TOKYO", "15 hours apart", w=980, size=64))
S([36], "street", [A("rio", 0.48, "sad", "sad")], [{"k": "shop", "x": 0.62, "s": "RAMEN", "closed": True}], fx=["night"], cam={"z": [1.25, 1.35], "x": [60, 80]})
S([37], "street", [A("rio", 0.4, "stand", "surprised")], [prop("cat", 0.62, 0.5)], fx=["night"], cam={"z": [1.3, 1.4], "x": [40, 60], "y": [60, 60]})
S([38], "street", [A("rio", 0.45, "crouch", "thinking")], [prop("cat", 0.6, 0.5)], fx=["night"], cam={"z": [1.5, 1.55], "x": [40, 40], "y": [120, 120]})
S([39], "street", [A("rio", [[0, 0.55], [0.8, 0.4]], "sad", "sad", alpha=[[0.75, 1], [0.9, 0]])], [door(0.4, open=1, inside="office"), prop("cat", 0.7, 0.35)], fx=["night"])
S([40, 41, 42], "room", [A("rio", 0.42, [[0, "explain"], ["@2", "pointUp"]], "smile")], [door(0.64)], card=card("LESSON ONE", "the door moves you...", at=0.05), props=[{"k": "sun", "x": 0.8, "y": 0.25, "r": 70, "at": "@2", "disc": True}], **HALL)
S([43, 44], "kitchen", [A("rio", 0.45, "sad", "sleepy", hold={"k": "cup"})], [], card=card("DAY THREE", "problem.", at=0.05), props=[{"k": "dizzy", "x": 0.47, "y": 0.42, "r": 50, "at": "@1"}])
S([45, 46], "kitchen", [], [], tpl="science", params={"sci": "BODY CLOCK", "icon": "brain"})
S([47], "kitchen", [A("rio", 0.4, "think", "thinking")], [], card=card("1 HOUR / DAY", "how fast your body clock can shift", w=760))
S([48], "room", [A("rio", [[0, KNOB], [0.25, 0.64], [0.35, 0.64], [0.6, KNOB], [0.7, KNOB], [0.95, 0.64]], "holdCup", "nervous", alpha=[[0.2, 1], [0.27, 0], [0.38, 0], [0.45, 1], [0.88, 1], [0.95, 0]])],
  [door(0.64, open=1, inside="tokyo")], card=card("12 TIME ZONES", "before dinner", x=0.3), **HALL)
S([49], "kitchen", [A("rio", 0.45, "chest", "confused")], [], props=[{"k": "stomach", "x": 0.6, "y": 0.4, "r": 60, "at": 0.1, "disc": True}, {"k": "sun", "x": 0.75, "y": 0.25, "r": 50, "at": 0.4, "disc": True}], card=card("BREAKFAST?", None, x=0.3, at=0.5))
S([50], "kitchen", [A("rio", 0.45, "sad", "sleepy")], [], props=[{"k": "eye", "x": 0.6, "y": 0.4, "r": 60, "at": 0.1, "disc": True}, {"k": "moon", "x": 0.75, "y": 0.25, "r": 50, "at": 0.4, "disc": True}], card=card("MIDNIGHT", None, x=0.3, at=0.5))
S([51, 52, 53], "home", [A("rio", 0.4, [[0, "sad"], ["@1", "shrug"], ["@2", "facepalm"]], [[0, "sleepy"], ["@1", "smirk"], ["@2", "sad"]])], [], card=card("JET LAG", "...without the jet", at=0.05), text=[{"s": "GENIUS?", "x": 0.75, "y": 0.42, "at": "@1"}, {"s": "TORTURE?", "x": 0.75, "y": 0.55, "at": "@2", "color": "#ff6a5a"}])
S([54, 55, 56, 57], "room", [A("rio", KNOB, [[0, "relaxed"], ["@1", "knob"], ["@3", "holdCup"]], "smile")], [door(0.64, open=[["@1.3", 0], ["@2", 1]], inside="mountain")], card=card("DENVER", "the Mile High City... about 1,600 m up", at="@1", w=820), **HALL)
S([58, 59, 60], "room", [A("rio", 0.5, [[0, "knob"], ["@0.6", "handsOnHead"]], [[0, "smile"], ["@0.6", "shocked"]])],
  [door(0.64, open=1, inside="mountain"), prop("letter", 0.3, 0.3, up=1.0, dx=[["@1", 0], ["@2", 0.4]], upk=[["@1", 1.0], ["@2", 1.8]], rot=[["@1", 0], ["@2", 4]]), prop("letter", 0.25, 0.25, up=0.8, dx=[["@1", 0], ["@2", 0.45]], upk=[["@1", 0.8], ["@2", 1.4]], rot=[["@1", 0], ["@2", -3]]),
   prop("flower", 0.2, 0.5, rot=[["@2", 0], ["@2.4", 1.4]])], fx=["speed"], sfx=[{"at": 0.4, "name": "whoosh", "gain": -10}], **HALL)
S([61, 62], "mountain", [], [], card=card("1/6 LESS AIR PRESSURE", "in Denver than in Miami", w=840, at="@1"), text=[{"s": "THINNER AIR", "x": 0.5, "y": 0.45, "at": 0.05, "size": 80}])
S([63, 64], "room", [A("rio", 0.42, [[0, "explain"], ["@1", "facepalm"]], [[0, "thinking"], ["@1", "smirk"]])], [door(0.64, open=1, inside="mountain")],
  text=[{"s": "HIGH  >>>  LOW", "x": 0.55, "y": 0.2, "at": 0.05, "size": 64}, {"s": "ACHOO!", "x": 0.75, "y": 0.35, "at": "@1"}], fx=["speed"], **HALL)
S([65], "room", [A("rio", 0.45, "handsOnHead", "nervous")], [door(0.64, open=1, inside="mountain")], props=[{"k": "ear", "x": 0.55, "y": 0.3, "r": 50, "at": 0.1, "disc": True}], text=[{"s": "POP!", "x": 0.35, "y": 0.3, "at": 0.3}], cam={"z": [1.3, 1.4], "x": [-40, -40], "y": [-80, -80]}, **HALL)
S([66, 67], "room", [A("rio", 0.5, [[0, "relaxed"], ["@1", "nervous"]], [[0, "surprised"], ["@1", "nervous"]], facing=-1), A("oldman", [[0, 0.12], [0.3, 0.22]], "talk", "confused", talk=["@1", 1])], [door(0.72, open=1, inside="mountain")], text=[{"s": "KNOCK KNOCK", "x": 0.2, "y": 0.25, "at": 0.05, "size": 54}], **HALL)
S([68, 69], "room", [A("rio", 0.5, [[0, "relaxed"], ["@1", "shrug"]], "smile", facing=-1), A("oldman", 0.22, "crossArms", "confused")], [door(0.72, open=[[0, 1], ["@1.5", 1], ["@1.9", 0]], inside="mountain")], text=[{"s": "VENTILATION", "x": 0.5, "y": 0.2, "at": "@1"}], **HALL)
S([70], "room", [A("rio", 0.45, "ready", "determined")], [door(0.64)], cam={"z": [1.2, 1.35]}, **HALL)
S([71, 72, 73], "mountain", [], [], card=card("MOUNT EVEREST", "8,849 m... the top of the world", at=0.05, w=820), fx=["snow"])
S([74], "room", [A("rio", KNOB, "think", "thinking")], [door(0.64)], thought={"props": ["mountain", "flag"], "x": 0.3, "y": 0.25, "at": 0.1}, **HALL)
S([75], "room", [A("rio", [[0, KNOB], [0.4, 0.5]], [[0, "knob"], [0.3, "ready"]], [[0, "smile"], [0.3, "shocked"]])], [door(0.64, open=[[0, 0], [0.25, 1]], inside="snow"), prop("letter", 0.3, 0.3, up=1.2, dx=[[0.3, 0], [0.8, 0.5]], rot=[[0.3, 0], [0.8, 5]])], fx=["speed", "snow"], sfx=[{"at": 0.6, "name": "whoosh", "gain": -8}], **HALL)
S([76], "mountain", [], [], card=card("1/3 AIR PRESSURE", "of sea level, at the summit", w=780), fx=["snow"])
S([77], "mountain", [A("rio", 0.45, "crossArms", "scared")], [], card=card("-30 C", "or colder", x=0.72), fx=["snow"], props=[{"k": "snowflake", "x": 0.3, "y": 0.3, "r": 50, "at": 0.2, "disc": True}])
S([78, 79], "room", [A("rio", 0.5, [[0, "relaxed"], ["@1", "sad"]], [[0, "shocked"], ["@1", "confused"]])], [door(0.64, open=1, inside="snow")], props=[{"k": "dizzy", "x": 0.52, "y": 0.42, "r": 50, "at": "@1"}], fx=["snow"], cam={"z": [1.3, 1.4], "x": [0, 0], "y": [-60, -60]}, **HALL)
S([80], "mountain", [], [], card=card("1-2 MINUTES", "of clear thinking for an unprepared person", w=880), props=[{"k": "brain", "x": 0.5, "y": 0.55, "r": 90, "at": 0.3, "disc": True}], fx=["snow"])
S([81], "room", [A("rio", 0.52, [[0, "ready"], [0.3, "kick2"]], "determined")], [door(0.64, open=[[0, 1], [0.45, 1], [0.6, 0]], inside="snow")], sfx=[{"at": 0.6, "name": "whoosh", "gain": -12}], **HALL)
S([82], "room", [A("rio", 0.45, "lie", "happy", rot=-1.5708, dy=136)], [door(0.64)], cam={"z": [1.2, 1.25], "y": [80, 80]}, **HALL)
S([83, 84], "beach", [A("rio", 0.4, "think", "smile")], [], card=card("BALI", "a quiet beach", at="@1", x=0.7), thought={"props": ["sun", "wave"], "x": 0.3, "y": 0.22, "at": 0.05})
S([85, 86], "room", [A("rio", KNOB, "think", "thinking")], [door(0.64)], card=card("A FEW METERS TOO FAR OUT", None, w=900, size=56, at="@1"), **HALL)
S([87], "ocean", [], [], card=card("+1 ATMOSPHERE", "every 10 m of seawater", w=760), props=[{"k": "wave", "x": 0.5, "y": 0.55, "r": 90, "at": 0.3, "disc": True}])
S([88], "room", [A("rio", KNOB, [[0, "knob"], [0.5, "handsOnHead"]], [[0, "smile"], [0.5, "shocked"]])], [door(0.64, open=[[0.3, 0], [0.42, 0.12]], inside="water"), {"k": "jet", "x": 0.61, "a": [[0.4, 0], [0.45, 1]], "up": 1.5}], sfx=[{"at": 1.0, "name": "whoosh", "gain": -10}], **HALL)
S([89], "room", [A("rio", 0.56, "push", "determined")], [door(0.64, open=[[0, 0.12], ["@0.5", 0]], inside="water"), {"k": "jet", "x": 0.61, "a": [[0, 1], ["@0.5", 0]], "up": 1.5}, {"k": "puddle", "x": 0.56}],
  text=[{"s": "CLICK", "x": 0.75, "y": 0.25, "at": "@1"}, {"s": "drip... drip", "x": 0.4, "y": 0.62, "at": "@3", "size": 46}], **HALL)
S([90, 91], "room", [A("rio", 0.56, "knob", "smirk", hold={"k": "note"})], [door(0.64), {"k": "puddle", "x": 0.56}, {"k": "paper", "x": 0.64, "up": 1.5, "s": "PICTURE THE SAND"}], cam={"z": [1.3, 1.4], "x": [100, 120], "y": [-60, -60]}, **HALL)
S([92, 93, 94], "town", [A("rio", 0.42, [[0, "relaxed"], ["@2", "holdCup"]], "joy", hold={"k": "tomato", "from": "@1.5"})], [{"k": "stall", "x": 0.68}, door(0.15, open=1, inside="apartment")], card=card("ITALY", "Saturday groceries", at="@1", x=0.3), text=[{"s": "TASTES LIKE SUMMER", "x": 0.6, "y": 0.18, "at": "@2", "size": 56}])
S([95, 96, 97], "town", [A("rio", 0.42, "holdCup", [[0, "smile"], ["@1", "surprised"]], hold={"k": "tomato"})], [{"k": "stall", "x": 0.68}],
  card=card("THE CATCH?", None, at=0.05), props=[{"k": "magnifier", "x": 0.55, "y": 0.45, "r": 70, "at": "@2", "disc": True}, {"k": "bee", "x": 0.6, "y": 0.47, "r": 30, "at": "@2.4"}], text=[{"s": "NO FRESH FRUIT ACROSS BORDERS", "x": 0.5, "y": 0.42, "at": "@1", "size": 46}])
S([98, 99, 100], "town", [A("rio", 0.42, [[0, "think"], ["@1", "sad"]], "nervous", hold={"k": "tomato"})], [{"k": "stall", "x": 0.68}], props=[{"k": "card", "x": 0.6, "y": 0.4, "r": 60, "at": 0.05, "disc": True}, {"k": "police", "x": 0.75, "y": 0.4, "r": 50, "at": "@1", "disc": True}], card=card("STILL ILLEGAL", "even with a magic door", at="@1", x=0.3))
S([101, 102], "office", [A("rio", 0.4, "holdCup", "nervous", hold={"k": "tomato"}), A("max", 0.62, [[0, "cheer"], ["@1", "point"]], "happy", facing=-1, talk=["@1", 1])], [{"k": "desk", "x": 0.82}], text=[{"s": "HA HA HA", "x": 0.65, "y": 0.25, "at": 0.05, "size": 54}])
S([103], "town", [A("rio", 0.52, [[0, "reach"], [0.6, "sad"]], "sad", hold={"k": "tomato", "to": 0.55})], [{"k": "stall", "x": 0.68}])
S([104, 105], "room", [A("rio", [[0, 0.15], ["@1", 0.35]], "relaxed", [[0, "smile"], ["@1", "shocked"]]), A("oldman", 0.5, [[0, "stand"], ["@1", "chest"]], [[0, "neutral"], ["@1", "scared"]], facing=-1)], [{"k": "stairs", "x": 0.55}], wall="#c8b8a8", wall2="#7a6a5a")
S([106], "room", [A("oldman", 0.5, "chest", "scared", facing=-1), A("oldwoman", 0.4, "phoneEar", "worried", facing=-1, hold={"k": "phone"}, talk=[0, 1])], [{"k": "stairs", "x": 0.55}], card=card("911", None, x=0.3), wall="#c8b8a8", wall2="#7a6a5a")
S([107], "city", [], [prop("ambulance", 0.4, 1.6, dx=[[0, -0.2], [1, 0.1]])], card=card("~7 MINUTES", "average ambulance arrival in big US cities", w=860))
S([108, 109], "room", [A("rio", [[0, 0.4], ["@1", KNOB]], [[0, "determined"], ["@1", "knob"]], "determined")], [door(0.64, open=[["@1.3", 0], ["@1.7", 1]], inside="hospital", sparkle=True)], wall="#c8b8a8", wall2="#7a6a5a")
S([110], "hospital", [A("nurse", [[0, 0.85], [0.8, 0.55]], "relaxed", "worried", facing=-1), A("doctor", [[0, 0.95], [0.8, 0.68]], "relaxed", "worried", facing=-1), A("rio", 0.3, "point", "determined")], [door(0.18, open=1, inside="apartment")])
S([111, 112], "hospital", [A("oldman", 0.42, "lie", "sleepy", rot=-1.5708, dy=41), A("doctor", 0.64, "explain", "smile", facing=-1, talk=["@1", 1]), A("rio", 0.78, "relaxed", "joy", facing=-1)], [{"k": "bed", "x": 0.42}], card=card("60 SECONDS LATER", None, at=0.05, y=0.15))
S([113, 114, 115], "bedroom", [A("rio", 0.47, "lie", [[0, "neutral"], ["@2", "happy"]], rot=-1.5708, dy=52, who="rioPj")], [], text=[{"s": "NOT JET LAG...", "x": 0.5, "y": 0.2, "at": "@1"}, {"s": "JOY", "x": 0.5, "y": 0.32, "at": "@2", "size": 90}])
S([116, 117], "city", [A("rio", [[0, 0.5], [0.4, 0.5]], "relaxed", "smile", alpha=[[0, 0], [0.3, 1]]), A("crowd1", 0.25, "phone", "shocked", hold={"k": "phone"}), A("crowd2", 0.78, "point", "shocked", facing=-1)], [door(0.5, a=[[0, 1], [0.35, 0]], open=1, inside="apartment")])
S([118, 119], "home", [A("rio", 0.45, "phone", [[0, "surprised"], ["@1", "nervous"]], hold={"k": "phone"})], [], card=card("12,000,000 VIEWS", "by Monday", at=0.05, w=760), props=[{"k": "bell", "x": 0.7, "y": 0.42, "r": 40, "at": "@1", "disc": True}])
S([120, 121, 122], "home", [A("rio", 0.4, "phoneEar", "surprised", hold={"k": "phone"})], [], inset={"who": "victor", "label": "VICTOR HALE", "talk": False, "at": "@1"}, card=card("SHIPPING CEO", "biggest on Earth", at="@2", x=0.3, y=0.18))
S([123], "home", [A("rio", 0.4, "phoneEar", "thinking", hold={"k": "phone"})], [], inset={"who": "victor", "label": "VICTOR HALE", "talk": True, "at": 0})
S([124, 125], "ocean", [], [{"k": "ship", "x": 0.5, "y": 0.62, "len": 30, "sc": 0.3}], card=card("80%", "of world trade travels by sea", at=0.05), text=[{"s": "WEEKS ON THE OCEAN", "x": 0.5, "y": 0.42, "at": "@1", "size": 56}])
S([126], "room", [A("rio", 0.45, "carry", "smirk")], [door(0.64, open=1, inside="market"), prop("box", 0.56, 0.4, up=0.9, a=0)], props=[{"k": "gift", "x": 0.55, "y": 0.6, "r": 40, "at": 0.1}], card=card("1 MINUTE", None, x=0.3, at=0.4), inset={"who": "victor", "label": "VICTOR HALE", "talk": True, "at": 0, "x": 0.85}, **HALL)
S([127], "home", [A("rio", 0.4, "phoneEar", "shocked", hold={"k": "phone"})], [], card=card("$1,000,000,000", None, at=0.4, x=0.45, w=760), inset={"who": "victor", "label": "VICTOR HALE", "talk": True, "at": 0, "x": 0.85})
S([128, 129, 130, 131, 132], "home", [A("rio", 0.4, "phoneEar", "nervous", hold={"k": "phone"})], [], inset={"who": "victor", "label": "VICTOR HALE", "talk": True, "at": 0, "x": 0.82},
  card=card("THE DOOR BECOMES OURS", "our warehouses only", at="@1", x=0.4, w=820, size=60), text=[{"s": "SINGAPORE - FRIDAY, NOON", "x": 0.45, "y": 0.45, "at": "@3", "size": 50}], props=[{"k": "contract", "x": 0.62, "y": 0.6, "r": 50, "at": "@3", "disc": True}])
S([133, 134, 135], "home", [A("rio", 0.5, [[0, "phone"], ["@2", "handsOnHead"]], [[0, "awe"], ["@2", "confused"]], hold={"k": "phone", "to": "@2"})], [], card=card("ONE BILLION", "is that even a real number?", at="@1"), cam={"z": [1.3, 1.45], "y": [-60, -60]})
S([136, 137], "beach", [A("rio", [[0, 0.64], [0.6, 0.45]], "relaxed", "joy", alpha=[[0, 0], [0.15, 1]])], [door(0.64, open=[[0, 1], [0.7, 1], [0.95, 0]], inside="apartment")], mood="dusk", text=[{"s": "CHASING SUNSETS", "x": 0.5, "y": 0.2, "at": "@1"}])
S([138], "space", [], [], props=[{"k": "earth", "x": 0.5, "y": 0.5, "r": 200, "at": 0, "disc": False}], card=card("1,670 KM/H", "Earth's spin at the equator", y=0.15, w=720))
S([139, 140], "space", [], [], props=[{"k": "globe", "x": 0.35, "y": 0.5, "r": 160, "at": 0}, {"k": "clock", "x": 0.72, "y": 0.5, "r": 110, "at": "@1"}], card=card("1 HOUR = 1 TIME ZONE WEST", None, w=900, size=58, y=0.15))
S([141], "desert", [A("rio", [[0, 0.62], [0.5, 0.45]], "relaxed", "awe", alpha=[[0, 0], [0.15, 1]])], [door(0.62, open=[[0, 1], [0.8, 1], [1, 0]], inside="sunset")], mood="dusk")
S([142], "lake", [A("rio", 0.4, "cheer", "joy")], [door(0.62, open=1, inside="sunset")], mood="dusk")
S([143], "mountain", [A("rio", 0.4, "relaxed", "awe")], [door(0.62, open=1, inside="sunset")], mood="dusk", card=card("7 SUNSETS", "in one evening", at=0.2))
S([144, 145, 146], "beach", [A("rio", 0.42, [[0, "phone"], ["@2", "cheer"]], [[0, "smile"], ["@2", "smirk"]], hold={"k": "phone", "to": "@2"})], [], mood="dusk",
  text=[{"s": "MAX: You're showing off.", "x": 0.68, "y": 0.25, "at": "@1", "size": 46, "color": "#f2ecdf"}, {"s": "RIO: Yes.", "x": 0.68, "y": 0.36, "at": "@2", "size": 46}])
S([147, 148], "room", [A("rio", 0.45, "think", "thinking")], [door(0.64)], thought={"props": ["car", "map"], "x": 0.3, "y": 0.25, "at": "@1"}, **HALL)
S([149, 150, 151], "room", [A("rio", 0.45, "sad", "sad")], [door(0.64)], thought={"props": ["plane", "car", "note"], "x": 0.32, "y": 0.25, "at": 0.05, "cross": True}, text=[{"s": "NO AIRPORTS", "x": 0.75, "y": 0.2, "at": 0.05, "size": 44}, {"s": "NO WINDOW SEATS", "x": 0.75, "y": 0.3, "at": "@1", "size": 44}, {"s": "NO ROAD TRIPS", "x": 0.75, "y": 0.4, "at": "@2", "size": 44}], **HALL)
S([152, 153], "room", [A("rio", [[0, KNOB], ["@0.6", 0.64]], "relaxed", "neutral", alpha=[["@0.5", 1], ["@0.7", 0]])], [door(0.64, open=1, inside="sunset")], fx=["dark"], text=[{"s": "ONE STEP AWAY", "x": 0.5, "y": 0.2, "at": 0.05}], **HALL)
S([154], "room", [], [], tpl="science", params={"sci": "NEW TRIPS = MEMORIES", "icon": "brain"})
S([155, 156], "room", [A("rio", [[0, 0.2], [0.3, KNOB], [0.32, 0.2], [0.62, KNOB], [0.64, 0.2], [0.95, KNOB]], "holdCup", "sad", hold={"k": "cup"})], [door(0.64)], fx=["dark"], text=[{"s": "SAME HALLWAY. SAME DOOR.", "x": 0.5, "y": 0.2, "at": 0.05, "size": 56}], **HALL)
S([157], "room", [A("rio", 0.5, "sad", "sad", s=0.9)], [door(0.64)], cam={"z": [1.0, 0.75]}, **HALL)
S([158, 159, 160], "town", [A("linda", 0.36, "relaxed", "smile", s=1.6)], [{"k": "house", "x": 0.5}], cam={"z": [0.55, 0.6], "y": [-200, -200]}, card=card("MISSOURI", "a small river town... home", at="@1", y=0.15))
S([161, 162], "room", [A("rio", 0.45, "sad", "sad")], [door(0.64)], card=card("2 YEARS", "since you last visited", at=0.05), **HALL)
S([163, 164, 165, 166], "town", [], [{"k": "house", "x": 0.62}], cam={"z": [1.6, 1.8], "x": [-560, -560], "y": [-200, -200]}, text=[{"s": "MADE BY RIO, AGE 9", "x": 0.5, "y": 0.2, "at": "@1", "size": 46}, {"s": "6 OLD SPOONS", "x": 0.5, "y": 0.3, "at": "@2", "size": 46}])
S([167, 168], "home", [A("rio", 0.4, "phoneEar", "smile", hold={"k": "phone"})], [], inset={"who": "linda", "label": "MOM", "talk": True, "at": 0, "expr": [[0, "smile"]]})
S([169, 170, 171], "home", [A("rio", 0.4, "phoneEar", "smile", hold={"k": "phone"}, talk=["@1", 1])], [], inset={"who": "linda", "label": "MOM", "at": 0, "expr": [[0, "smile"]]}, text=[{"s": "\"DISTANCE IS JUST A DOOR\"", "x": 0.42, "y": 0.18, "at": "@2", "size": 52}])
S([172, 173, 174], "home", [A("rio", 0.4, "phoneEar", [[0, "smile"], ["@1", "sad"]], hold={"k": "phone"})], [], inset={"who": "linda", "label": "MOM", "talk": True, "at": 0, "expr": [[0, "happy"], ["@1", "sad"]]}, cam={"z": [1.2, 1.35], "y": [-60, -60]})
S([175, 176], "town", [], [{"k": "house", "x": 0.62}], cam={"z": [1.8, 1.9], "x": [-560, -560], "y": [-200, -200]}, text=[{"s": "clink... clink", "x": 0.45, "y": 0.3, "at": 0.2, "size": 50}])
S([177, 178, 179, 180], "room", [A("rio", 0.45, [[0, "relaxed"], ["@3", "crossArms"]], "smirk", who="rioSuit")], [door(0.64), prop("clock", 0.8, 0.5, up=1.7, disc=True)], card=card("FRIDAY 11:00 AM", "Singapore at 11:59", at=0.05, w=760), **HALL)
S([181, 182, 183], "room", [A("rio", 0.45, "phoneEar", [[0, "smile"], ["@1", "worried"]], hold={"k": "phone"}, who="rioSuit")], [door(0.64)], inset={"who": "linda", "label": "MOM", "talk": True, "rain": True, "at": 0, "expr": [[0, "scared"]], "bg": ["#2a3a4a", "#0a1018"]}, **HALL)
S([184, 185, 186], "town:night", [A("linda", 0.86, "wave", "scared", up=5.2, s=1.6)], [{"k": "house", "x": 0.5, "night": True, "chime": False}, {"k": "water", "level": [[0, 1.2], [1, 1.6]]}], fx=["rain", "night"], cam={"z": [0.6, 0.63], "x": [560, 560], "y": [-640, -640]})
S([187, 188, 189, 190], "town:night", [A("linda", 0.79, "wave", "scared", up=5.2), A("oldwoman", 0.84, "sad", "scared", up=5.2), A("oldman", 0.88, "crossArms", "worried", up=5.2), A("crowd1", 0.75, "handsOnHead", "scared", up=5.2), A("kid", 0.72, "sad", "scared", up=5.2), A("boy", 0.82, "sad", "scared", up=5.2)],
  [{"k": "house", "x": 0.5, "night": True, "chime": False}, {"k": "water", "level": [[0, 1.6], [1, 2.1]]}], fx=["rain", "night"], cam={"z": [0.6, 0.63], "x": [560, 560], "y": [-640, -640]}, card=card("12 PEOPLE", "on one roof", at="@1", y=0.15))
S([191, 192], "room", [A("rio", 0.45, "phoneEar", "worried", hold={"k": "phone"}, who="rioSuit")], [door(0.64)], card=card("911", "every boat is already out", at=0.05, x=0.3), props=[{"k": "boat", "x": 0.75, "y": 0.35, "r": 50, "at": "@1", "disc": True}], **HALL)
S([193, 194, 195, 196], "room", [A("rio", KNOB, "think", "worried", who="rioSuit")], [door(0.64)], thought={"props": ["house", "wave"], "x": 0.3, "y": 0.25, "at": 0.05, "cross": True}, card=card("THE PORCH IS UNDERWATER", None, at="@1", w=900, size=56, y=0.12), **HALL)
S([197, 198, 199], "room", [A("rio", KNOB, "think", "determined", who="rioSuit")], [door(0.64)], thought={"props": ["house", "star"], "x": 0.3, "y": 0.25, "at": 0.05}, text=[{"s": "THE ROOF", "x": 0.5, "y": 0.15, "at": "@1"}], **HALL)
ROOF = dict()
S([200, 201, 202], "roof", [A("rio", 0.3, [[0, "knob"], ["@2", "point"]], "determined", who="rioSuit"), A("linda", 0.72, "wave", "scared", facing=-1), A("oldwoman", 0.8, "sad", "scared", facing=-1), A("crowd2", 0.88, "handsOnHead", "scared", facing=-1)],
  [door(0.38, open=[[0, 0], [0.12, 1]], inside="apartment")], fx=["rain"], text=[{"s": "GO, GO, GO!", "x": 0.3, "y": 0.18, "at": "@2"}], **ROOF)
S([203, 204, 205, 206], "roof", [A("rio", 0.28, "think", "worried", who="rioSuit"), A("crowd1", 0.72, "relaxed", "scared", facing=-1), A("oldman", 0.8, "sad", "scared", facing=-1)], [door(0.38, open=1, inside="apartment")], fx=["rain"], card=card("60 SECONDS", "12 people... 5 seconds each", at="@1", x=0.62, w=640), **ROOF)
S([207, 208], "roof", [A("oldwoman", [[0, 0.7], [1, 0.62]], "holdFront", "scared", facing=-1), A("linda", 0.8, "point", "worried", facing=-1)], [door(0.38, open=1, inside="apartment")], fx=["rain"], text=[{"s": "SLIPPERY", "x": 0.6, "y": 0.2, "at": "@1"}], **ROOF)
S([209, 210], "town:night", [], [prop("car", 0.6, 1.2, up=0.3, rot=[[0, 0], [1, 0.2]]), {"k": "water", "level": [[0, 0.15], ["@1", 0.15], ["@1.6", 0.6]]}], card=card("15 CM", "of moving water can knock you down", at=0.05, w=760), text=[{"s": "60 CM FLOATS A CAR", "x": 0.5, "y": 0.4, "at": "@1", "size": 60}], fx=["rain"])
S([211], "town:night", [], [{"k": "house", "x": 0.5, "night": True, "chime": False}, {"k": "water", "level": [[0, 2.4], [1, 2.6]]}], fx=["rain", "night"], cam={"z": [0.6, 0.63], "x": [560, 560], "y": [-640, -640]}, card=card("WATER AT THE GUTTERS", None, w=820, size=56))
S([212], "roof", [A("oldman", [[0, 0.72], [0.4, 0.38]], "relaxed", "scared", facing=-1, alpha=[[0.35, 1], [0.42, 0]]), A("kid", [[0.3, 0.72], [0.7, 0.38]], "relaxed", "scared", facing=-1, alpha=[[0.65, 1], [0.72, 0]]), A("crowd1", [[0.55, 0.8], [0.95, 0.38]], "relaxed", "scared", facing=-1, alpha=[[0.9, 1], [0.97, 0]]), A("rio", 0.28, "point", "determined", who="rioSuit")],
  [door(0.38, open=1, inside="apartment")], fx=["rain"], text=[{"s": "5...  6...  7...", "x": 0.6, "y": 0.18, "at": 0.1}], **ROOF)
S([213, 214, 215], "roof", [A("linda", 0.6, [[0, "point"], ["@1", "wave"]], "determined", facing=-1, talk=[0, "@1.6"]), A("oldwoman", [[0, 0.5], ["@0.8", 0.38]], "relaxed", "scared", facing=-1, alpha=[["@0.7", 1], ["@0.9", 0]])],
  [door(0.38, open=[[0, 1], ["@1.7", 1], ["@2.0", 0]], inside="apartment")], fx=["rain"], text=[{"s": "SLAM", "x": 0.38, "y": 0.2, "at": "@1.8"}], sfx=[{"at": 2.4, "name": "whoosh", "gain": -8}], **ROOF)
S([216, 217], "town:night", [A("linda", 0.79, "wave", "scared", up=5.2), A("oldwoman", 0.84, "sad", "scared", up=5.2), A("oldman", 0.88, "crossArms", "worried", up=5.2), A("boy", 0.75, "sad", "scared", up=5.2), A("crowd2", 0.91, "sad", "scared", up=5.2)],
  [{"k": "house", "x": 0.5, "night": True, "chime": False}, {"k": "water", "level": [[0, 2.5], [1, 2.7]]}], fx=["rain", "night"], cam={"z": [0.6, 0.63], "x": [560, 560], "y": [-640, -640]}, card=card("5 STILL ON THE ROOF", "including Mom", at=0.05, y=0.14))
S([218, 219], "home", [A("rio", 0.4, "sad", "scared", who="rioSuit")], [prop("clock", 0.68, 0.6, up=1.6, disc=True)], card=card("11:00", "the door needs 1 hour", at="@1", x=0.3))
S([220, 221, 222], "home", [A("rio", 0.4, "think", "worried", who="rioSuit")], [prop("clock", 0.68, 0.6, up=1.6, disc=True)], card=card("12:00 NOON", "same minute as Singapore", at="@1", x=0.32, w=700))
S([223, 224, 225], "room", [A("rio", 0.5, "think", "worried", who="rioSuit")], [door(0.5)], thought={"props": ["money", "house"], "x": 0.25, "y": 0.32, "at": "@2"}, text=[{"s": "ONE OPENING. ONE DOOR.", "x": 0.5, "y": 0.12, "at": 0.05, "size": 56}], **HALL)
S([226, 227], "home", [A("rio", [[0, 0.15], ["@1.3", 0.42]], "carry", "worried", who="rioSuit", hold={"k": "towel"}, walkArms=True), A("oldman", 0.5, "sad", "sad"), A("kid", 0.6, "sad", "sad"), A("crowd1", 0.7, "crossArms", "sad"), A("crowd2", 0.8, "sad", "sad")], [], card=card("THE LONGEST HOUR", None, at=0.05, y=0.14, w=700))
S([228, 229, 230, 231], "home", [A("rio", 0.42, "relaxed", "sad", who="rioSuit"), A("oldwoman", 0.55, [[0, "reach"], ["@1", "talk"]], "smile", facing=-1, talk=["@1", "@1.9"])], [], cam={"z": [1.4, 1.5], "x": [0, 0], "y": [-60, -60]})
S([232, 233], "room", [A("rio", KNOB, "phoneEar", "determined", who="rioSuit", hold={"k": "phone"})], [door(0.64)], inset={"who": "victor", "label": "VICTOR HALE", "talk": True, "at": 0, "x": 0.25}, props=[{"k": "pencil", "x": 0.25, "y": 0.55, "r": 40, "at": "@1", "disc": True}], **HALL)
S([234, 235, 236, 237], "room", [A("rio", KNOB, "knob", "determined", who="rioSuit")], [door(0.64, open=[["@3.6", 0], ["@3.95", 1]], inside="roof")], card=card("11:59", None, at=0.05, x=0.3), thought={"props": ["house"], "x": 0.3, "y": 0.45, "at": "@3"}, cam={"z": [1.2, 1.45], "x": [60, 140], "y": [-40, -40]}, **HALL)
S([238, 239], "roof", [A("rio", 0.3, "point", "determined", who="rioSuit"), A("linda", 0.72, "wave", "scared", facing=-1), A("oldwoman", 0.6, "sad", "scared", facing=-1), A("oldman", 0.82, "sad", "scared", facing=-1)], [door(0.38, open=1, inside="apartment"), {"k": "water", "level": [[0, -0.05], [1, 0.03]]}], fx=["rain"], **ROOF)
S([240, 241, 242], "roof", [A("oldwoman", [[0, 0.6], ["@0.8", 0.38]], "relaxed", "scared", facing=-1, alpha=[["@0.7", 1], ["@0.9", 0]]), A("oldman", [[0, 0.75], ["@1.8", 0.38]], "relaxed", "scared", facing=-1, alpha=[["@1.7", 1], ["@1.9", 0]]),
  A("kid", [["@1", 0.82], ["@2.8", 0.38]], "relaxed", "scared", facing=-1, alpha=[["@2.7", 1], ["@2.9", 0]]), A("boy", [["@1.5", 0.88], ["@2.9", 0.4]], "relaxed", "scared", facing=-1), A("linda", 0.9, "wave", "worried", facing=-1)], [door(0.38, open=1, inside="apartment")], fx=["rain"], **ROOF)
S([243, 244, 245, 246], "roof", [A("linda", [[0, 0.7], ["@3", 0.45]], "holdCup", "sad", facing=-1, hold={"k": "chime"})], [door(0.38, open=1, inside="apartment")], fx=["rain"], cam={"z": [1.2, 1.4], "x": [0, -60], "y": [-40, -40]}, text=[{"s": "clink", "x": 0.55, "y": 0.25, "at": "@3", "size": 50}], **ROOF)
S([247], "home", [A("rio", 0.36, "hug", "cry", who="rioSuit"), A("linda", 0.46, "hug", "cry", facing=-1, hold={"k": "chime"})], [door(0.72, open=[[0, 1], [0.6, 1], [0.8, 0]], inside="roof")], text=[{"s": "SLAM", "x": 0.72, "y": 0.2, "at": 0.7}])
S([248, 249, 250], "home", [A("rio", 0.42, [[0, "phone"], ["@2", "hug"]], "smile", who="rioSuit", hold={"k": "phone", "to": "@2"}), A("linda", 0.52, "hug", "smile", facing=-1)], [], card=card("CONTRACT CANCELLED", None, at="@1", w=760, size=60))
S([251, 252, 253, 254], "home", [A("oldman", 0.3, "lie", "sleepy", rot=-1.5708, dy=136, zzz=True), A("kid", 0.5, "lie", "sleepy", rot=-1.5708, dy=136), A("crowd1", 0.66, "lie", "sleepy", rot=-1.5708, dy=136)], [], fx=["night"], card=card("12 GUESTS", "on the couch, on the floor", at=0.05, y=0.14), text=[{"s": "SNORE...", "x": 0.35, "y": 0.4, "at": "@3"}])
S([255], "home", [A("rio", 0.36, "sitTable", "confused", who="rioSuit"), A("oldwoman", 0.6, "sitTable", "happy", facing=-1)], [{"k": "table", "x": 0.48, "w": 1.0}, {"k": "cards", "x": 0.48}], card=card("3 - 0", "Mrs. Parker wins again", x=0.5, y=0.15))
S([256, 257], "city", [A("crowd1", 0.3, "phone", "joy", hold={"k": "phone"}), A("crowd2", 0.7, "phone", "joy", facing=-1, hold={"k": "phone"})], [], props=[{"k": "tv", "x": 0.5, "y": 0.35, "r": 120, "at": 0, "disc": True}, {"k": "gift", "x": 0.3, "y": 0.2, "r": 40, "at": "@1"}, {"k": "boat", "x": 0.5, "y": 0.14, "r": 40, "at": "@1.3"}, {"k": "cake", "x": 0.7, "y": 0.2, "r": 40, "at": "@1.6"}])
S([258, 259], "town", [A("rio", 0.3, "kneel", "determined", hold={"k": "hammer"}, who="rioSuit"), A("linda", 0.42, "holdFront", "smile", facing=-1)], [{"k": "house", "x": 0.62, "chime": False}], cam={"z": [1.0, 1.05], "x": [-300, -300], "y": [-100, -100]}, card=card("BOARD BY BOARD", None, at="@1", y=0.14))
S([260, 261, 262], "highway", [A("rio", 0.44, "sit", "smile", dy=0, clip=0.62), A("linda", 0.52, "sit", "happy", dy=0, clip=0.62)], [{"k": "car", "x": 0.5, "drive": True, "color": "#3a8ad0"}, {"k": "car", "x": 0.5, "drive": True, "color": "#3a8ad0", "part": "front", "front": True}], card=card("MIAMI > MISSOURI", None, at="@2", y=0.15, w=720), fx=["speed"])
S([263, 264], "highway", [A("rio", 0.44, "sit", "smile", dy=0, clip=0.62), A("linda", 0.52, "sit", "happy", dy=0, clip=0.62)], [{"k": "car", "x": 0.5, "drive": True, "color": "#3a8ad0"}, {"k": "car", "x": 0.5, "drive": True, "color": "#3a8ad0", "part": "front", "front": True}], card=card("1,800 KM", "two days", at=0.05, y=0.15))
S([265, 266, 267], "highway", [A("rio", 0.44, "sit", "smile", dy=0, clip=0.62, hold={"k": "cup"}), A("linda", 0.52, "sit", [[0, "happy"], ["@2", "sleepy"]], dy=0, clip=0.62, rot=[[0, 0], ["@2", 0], ["@2.5", -0.25]])], [{"k": "car", "x": 0.5, "drive": True, "color": "#3a8ad0"}, {"k": "car", "x": 0.5, "drive": True, "color": "#3a8ad0", "part": "front", "front": True}], mood="dusk", props=[{"k": "note", "x": 0.7, "y": 0.3, "r": 40, "at": "@1", "disc": True}], cam={"z": [1.3, 1.4], "y": [-40, -40]})
S([268, 269], "highway", [A("rio", 0.44, "sit", "happy", dy=0, clip=0.62), A("linda", 0.52, "sit", "sleepy", dy=0, clip=0.62, rot=-0.25)], [{"k": "car", "x": 0.5, "drive": True, "color": "#3a8ad0"}, {"k": "car", "x": 0.5, "drive": True, "color": "#3a8ad0", "part": "front", "front": True}], mood="dusk", text=[{"s": "THE BEST TRIP OF YOUR LIFE", "x": 0.5, "y": 0.18, "at": 0.1, "size": 56}])
S([270], "town", [], [{"k": "house", "x": 0.62}], cam={"z": [1.8, 1.9], "x": [-560, -560], "y": [-200, -200]}, text=[{"s": "clink... clink", "x": 0.45, "y": 0.3, "at": 0.2, "size": 50}])
S([271, 272, 273, 274], "town:dusk", [A("rio", 0.3, "talk", "smile", who="rioSuit", talk=[0, "@0.9"]), A("linda", 0.4, [[0, "relaxed"], ["@2", "talk"]], "smile", facing=-1, talk=["@2", 1])], [{"k": "house", "x": 0.62}], cam={"z": [1.1, 1.2], "x": [-300, -320], "y": [-100, -100]}, text=[{"s": "\"DISTANCE IS A CHOICE.\"", "x": 0.5, "y": 0.15, "at": "@3", "size": 56}])
S([275], "space", [], [], text=[{"s": "IS IT REAL?", "x": 0.5, "y": 0.45, "at": 0.05, "size": 110}])
S([276, 277, 278], "space", [], [], card=card("1935", "Einstein & Rosen: a bridge through space", at=0.05, w=820), props=[{"k": "planet", "x": 0.25, "y": 0.6, "r": 80, "at": "@1"}, {"k": "planet", "x": 0.75, "y": 0.6, "r": 80, "at": "@1"}], text=[{"s": "WORMHOLE", "x": 0.5, "y": 0.62, "at": "@2", "size": 80}])
S([279, 280, 281], "space", [], [], card=card("1988", "Thorne & Morris: how to keep one open?", at=0.05, w=840), text=[{"s": "NEGATIVE ENERGY", "x": 0.5, "y": 0.55, "at": "@2", "size": 70}])
S([282, 283, 284], "space", [], [], text=[{"s": "NEVER FOUND... YET", "x": 0.5, "y": 0.4, "at": 0.05, "size": 80}], props=[{"k": "question", "x": 0.5, "y": 0.62, "r": 80, "at": "@1"}])
S([285], "highway", [A("rio", 0.44, "sit", "smile", dy=0, clip=0.62), A("linda", 0.52, "sit", "sleepy", dy=0, clip=0.62, rot=-0.25)], [{"k": "car", "x": 0.5, "drive": True, "color": "#3a8ad0"}, {"k": "car", "x": 0.5, "drive": True, "color": "#3a8ad0", "part": "front", "front": True}], mood="dusk")
S([286, 287, 288, 289, 290], "street", [A("rio", [[0, 0.2], ["@2", 0.4]], [[0, "relaxed"], ["@3", "surprised"]], [[0, "neutral"], ["@3", "surprised"]])], [{"k": "booth", "x": 0.62, "ring": ["@3", 1]}, {"k": "booth", "x": 0.62, "part": "front"}], fx=["night"], text=[{"s": "RING... RING", "x": 0.62, "y": 0.2, "at": "@3", "size": 54}, {"s": "\"WHAT KIND OF WORLD DO YOU WANT?\"", "x": 0.5, "y": 0.12, "at": "@4", "size": 46, "color": "#f2ecdf"}])
S([291, 292], "face", [], [], who="rio", expr=[[0, "smile"]])
S([293], "end", [], [], tpl="end")


# ---- v3 pass (same as video 32): talkers change gesture each sentence, no aimless pacing,
# long shots cut into 1-2 sentence shots with varied framing ----
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "pipeline"))
from sb import split_board, plan_chunks
from build import split_sentences
for b in B: b.setdefault("actors", []); b.setdefault("items", []); b.setdefault("set", "home")
VAR = {"relaxed": ["think", "crossArms", "shrug"], "think": ["relaxed", "crossArms"], "crossArms": ["think", "relaxed"], "sad": ["facepalm", "chest"], "nervous": ["handsOnHead", "think"],
       "talk": ["explain", "point"], "explain": ["talk", "point"], "worried": ["think", "handsOnHead"], "point": ["explain", "relaxed"], "shrug": ["relaxed", "think"]}
for b in B:
    if b.get("tpl") or b["set"] in ("face", "space"): continue
    n = len(b["lines"])
    for a in b["actors"]:
        poses = a["pose"]; p0 = poses[0][1]
        if len(poses) == 1 and p0 in VAR and n > 1 and (a.get("talk") or len(b["actors"]) == 1) and not a.get("rot") and not a.get("up") and not a.get("hold"):
            v = VAR[p0]; a["pose"] = [[0, p0]] + [[f"@{i}", v[(i - 1) % len(v)] if i % 2 else p0] for i in range(1, n)]
item = next(x for x in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts.json")))["long"] if x["stt"] == 31)
LENS = [len(x.split()) for x in split_sentences(item["script"])]
def xs(a):
    v = a["x"]; return [k[1] for k in v] if isinstance(v, list) else [v]
def frame(c, j):
    if j == 0 or c.get("tpl") or c["set"] in ("face", "space", "map") or "cam" in c or not c["actors"]: return
    acts = c["actors"]
    if any(a.get("up") or a.get("rot") or a.get("alpha") or a.get("clip") is not None for a in acts): return
    f = ([a for a in acts if a.get("talk")] or [a for a in acts if a["id"] == "rio"] or acts)[0]; X = xs(f)
    if max(X) - min(X) > 0.15: return
    xm = sum(X) / len(X)
    if j % 2 == 1: c["cam"] = {"z": [1.34, 1.42], "x": [max(-520, min(520, (xm - 0.5) * 1920))] * 2, "y": [-40, -40]}
    else: c["cam"] = {"z": [1.12, 1.16], "x": [max(-300, min(300, (xm - 0.5) * 960))] * 2, "y": [-10, -10]}
NB = []
for b in B:
    n = len(b["lines"])
    if n < 2 or b.get("tpl") or b["set"] == "face": NB.append(b); continue
    ch = plan_chunks(n, [LENS[i] for i in b["lines"]])
    if len(ch) == 1: NB.append(b); continue
    for j, c in enumerate(split_board(b, ch)): frame(c, j); NB.append(c)
B[:] = NB
out = os.path.join(os.path.dirname(__file__), "long_31.json")
json.dump(B, open(out, "w"), indent=0, ensure_ascii=False)
covered = sorted(i for b in B for i in b["lines"]); print(len(B), "shots, lines", covered[0], "-", covered[-1], "count", len(covered), "dupes" if len(set(covered)) != len(covered) else "")
