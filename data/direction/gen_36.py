# Storyboard long_36 "What If You Owned A Time Machine And Went Back 20 Years?"
# Written line by line from the script. Kitchen = the family kitchen (2006 and 2026), garage = grandpa's garage.
from sb import *
def door(x, **kw): d = {"k": "housedoor", "x": x}; d.update(kw); return d
GAR = dict(wall="#5a5a64", wall2="#2a2a32", room={})
APT = dict(wall="#c8b0a0", wall2="#7a6070", room={"frames": 260, "window": 1250})
TBL = {"k": "table", "x": 0.5, "w": 1.2}
FRIDGE = {"k": "paper", "x": 2.0}   # the kitchen set already has a fridge (x ~0.94); this is a no-op placeholder
def tom(x=0.38, pose="sitTable", expr="neutral", **kw): return A("tom", x, pose, expr, **kw)
def rio_seat(pose="sitTable", expr="neutral", **kw): return A("rio", 0.62, pose, expr, facing=-1, **kw)
MACH = {"k": "tmachine", "x": 0.5}

# ---- cold open: the kitchen in 2006 ----
S([0], "kitchen", [A("rio", 0.3, "relaxed", [[0, "sleepy"], [0.5, "awe"]])], [TBL], fx=["flash"], cam={"z": [1.3, 1.15], "x": [-200, -150], "y": [-40, -40]})
S([1, 2], "kitchen", [A("rio", 0.3, [[0, "relaxed"], ["@1", "point"]], "awe", facing=[[0, 1], ["@0.5", -1], ["@1", 1]])], [TBL], text=[T("YOUR CHILDHOOD KITCHEN", 0.5, 0.14, 0.1, size=50), T("LITTLE YELLOW DUCKS", 0.5, 0.24, "@1", size=46)])
S([3], "kitchen", [A("rio", [[0, 0.3], [0.5, 0.2]], "relaxed", "smile", facing=-1)], [TBL], props=[P("radio", 0.12, 0.42, 50, 0.1), P("note", 0.17, 0.32, 30, 0.3), P("note", 0.09, 0.28, 26, 0.5)])
S([4], "kitchen", [A("rio", [[0, 0.3], [0.5, 0.72]], "relaxed", [[0, "neutral"], [0.6, "surprised"]])], [TBL, FRIDGE, {"k": "paper", "x": 0.94, "up": 1.25, "s": "AUG 2006"}], cam={"z": [1.0, 1.35], "x": [0, 520], "y": [0, -40]})
S([5, 6, 7], "kitchen", [tom(hold={"k": "newspaper"}), A("rio", 0.72, "relaxed", [[0, "surprised"], ["@1", "shocked"], ["@2", "cry"]], facing=-1)], [TBL], text=[T("YOUR DAD", 0.4, 0.16, "@1"), T("20 YEARS YOUNGER... ALIVE", 0.5, 0.26, "@2", size=50)])
S([8, 9], "kitchen", [tom(expr=[[0, "neutral"], [0.2, "confused"]], hold={"k": "newspaper"}, talk=["@1", 1]), A("rio", 0.72, "relaxed", "shocked", facing=-1)], [TBL], text=[T("\"CAN I HELP YOU, BUDDY?\"", 0.4, 0.16, "@1", size=52)])
S([10], "face", [], [], who="rio", expr=[[0, "shocked"]], bg="kitchen")

# ---- who you are ----
S([11, 12], "room", [A("rio", 0.42, "relaxed", "neutral")], [], card=card("RIO, 34", None, at=0.1, x=0.68), **APT)
S([13, 14, 15], "room", [A("rio", 0.42, [[0, "relaxed"], ["@1", "sad"]], "sad")], [], card=card("TOM", "your dad... died in 2007", at=0.05, x=0.68, w=560), props=[P("brokenheart", 0.68, 0.5, 60, "@1")], text=[T("HE WAS 52. YOU WERE 15.", 0.5, 0.36, "@2", size=50)], **APT)
S([16, 17], "room", [A("rio", [[0, 0.05], [0.6, 0.3]], [[0, "relaxed"], [0.65, "point"]], [[0, "neutral"], [0.65, "awe"]])], [MACH], fx=["dark"], text=[T("GRANDPA'S OLD GARAGE", 0.5, 0.14, 0.05, size=50), T("A METAL CHAIR... A BRASS DIAL", 0.5, 0.24, "@1", size=46)], **GAR)
S([18, 19], "room", [A("rio", 0.32, "relaxed", "thinking")], [MACH], cam={"z": [1.6, 1.8], "x": [100, 118], "y": [60, 70]}, text=[T("ONE SETTING:", 0.5, 0.14, 0.1, size=50), T("20 YEARS AGO. TODAY.", 0.5, 0.24, "@1", size=54)], **GAR)
S([20, 21], "room", [A("rio", [[0, 0.32], [0.3, 0.5]], [[0, "relaxed"], [0.35, "sit"], ["@1.2", "push"]], [[0, "determined"], ["@1.3", "scared"]], chair=False)], [dict(MACH, lever=[[0, 0], ["@1.3", 0], ["@1.6", 1]])], text=[T("CLICK", 0.7, 0.3, "@1.6")], **GAR)
S([22], "home", [A("oldwoman", 0.45, "sit", "smile", hold={"k": "note"})], [], props=[P("camera", 0.65, 0.4, 50, 0.2)], text=[T("MOST PEOPLE VISIT THE PAST IN PHOTOS", 0.5, 0.16, 0.1, size=46)])
S([23], "kitchen", [A("rio", 0.4, "relaxed", "awe")], [TBL], text=[T("YOU'RE STANDING IN IT", 0.5, 0.16, 0.1, size=56)])
S([24, 25], "room", [A("rio", 0.3, "think", "thinking")], [MACH], card=card("ONE RULE", "exactly one hour", at=0.05, x=0.7), props=[P("hourglass", 0.7, 0.55, 50, "@1")], **GAR)
S([26, 27], "room", [A("rio", 0.3, "think", "worried")], [MACH], card=card("ONE CHANGE", "one message... to one person", at=0.05, x=0.7, w=620), text=[T("...THEN IT PULLS YOU HOME", 0.62, 0.42, "@1", size=44)], **GAR)
S([28, 29], "kitchen", [A("rio", 0.4, "relaxed", "thinking")], [TBL], text=[T("ONE MESSAGE.", 0.5, 0.14, 0.05), T("ONE CHANGE.", 0.5, 0.24, "@1")])
S([30], "room", [], [], tpl="title", params={"title": "What If You Went Back 20 Years?"})

# ---- minute one: 2006 ----
S([31, 32, 33], "kitchen", [A("rio", [[0, 0.62], ["@1.6", 0.42]], [[0, "relaxed"], ["@2", "point"]], [[0, "neutral"], ["@1", "confused"]], facing=-1)], [{"k": "tvset", "x": 0.22, "show": "news", "who": "crowd2", "bg": "#3a5a8a"}], card=card("MINUTE 1", None, at=0.05, x=0.75), text=[T("A TV LIKE A BOX", 0.3, 0.3, "@2", size=46)])
S([34, 35], "kitchen", [tom(hold={"k": "phone"}), A("rio", 0.72, "relaxed", "smile", facing=-1)], [TBL], text=[T("PHONES FLIP OPEN", 0.5, 0.14, 0.05, size=50), T("NOBODY IS SCROLLING", 0.5, 0.24, "@1", size=46)])
S([36], "space", [], [], card=card("JANUARY 2007", "when the first iPhone is announced", at=0.05, w=780), props=[P("phone", 0.5, 0.6, 70, 0.3)])
S([37, 38, 39, 40], "kitchen", [A("rio", 0.42, [[0, "relaxed"], ["@0.4", "phone"]], [[0, "neutral"], ["@1", "confused"], ["@3", "smirk"]], hold={"k": "phone", "from": "@0.4"})], [TBL], text=[T("NO SIGNAL. NO APPS.", 0.5, 0.14, "@1", size=50), T("A VERY EXPENSIVE MIRROR", 0.5, 0.24, "@3", size=46)])
S([41, 42, 43, 44], "kitchen", [tom(hold={"k": "newspaper"}), A("rio", [[0, 0.72], ["@1", 0.5]], "relaxed", [[0, "neutral"], ["@2", "surprised"]], facing=-1)], [TBL], card=card("MINUTE 3", None, at=0.05, x=0.75), props=[P("newspaper", 0.3, 0.42, 60, "@1.5"), P("planet", 0.42, 0.42, 40, "@2")], text=[T("PLUTO", 0.36, 0.28, "@2", size=60)])
S([45, 46], "space", [], [], card=card("AUGUST 2006", "Pluto is no longer a full planet", at=0.05, w=760), props=[P("planet", 0.5, 0.6, 80, 0.2)], text=[T("NOW: A DWARF PLANET", 0.5, 0.42, "@1", size=56)])
S([47, 48, 49, 50], "kitchen", [tom(expr=[[0, "sad"], ["@2", "smirk"]], hold={"k": "newspaper"}, talk=["@1", "@2.9"]), rio_seat(expr=[[0, "neutral"], ["@2.5", "joy"]])], [TBL], text=[T("\"POOR LITTLE GUY\"", 0.38, 0.16, "@1", size=54), T("\"50 YEARS A PLANET, AND NOW THIS\"", 0.5, 0.26, "@2", size=44)])
S([51, 52], "kitchen", [A("tom", [[0, 0.38], ["@0.6", 0.68]], [[0, "relaxed"], ["@0.8", "pour"]], "smile", hold={"k": "pour", "from": "@0.8"}), A("rio", 0.3, "relaxed", "nervous")], [{"k": "counter", "x": 0.95}], card=card("MINUTE 5", None, at=0.05, x=0.25), text=[T("COFFEE?", 0.7, 0.3, "@1")])
S([53, 54, 55], "kitchen", [A("tom", 0.52, [[0, "relaxed"], ["@1", "shake"]], "smile", facing=-1, talk=[0, 1]), A("rio", 0.42, "relaxed", [[0, "nervous"], ["@2", "shocked"]])], [], text=[T("\"I'M TOM. AND YOU ARE?\"", 0.5, 0.16, "@1", size=54)])
S([56, 57, 58, 59, 60], "kitchen", [A("rio", 0.42, [[0, "relaxed"], ["@1", "think"], ["@4", "handsOnHead"]], [[0, "shocked"], ["@1", "thinking"], ["@4", "scared"]])], [], thought={"props": ["police"], "x": 0.7, "y": 0.28, "at": "@3"}, text=[T("\"I'M YOUR SON... FROM THE FUTURE?\"", 0.5, 0.14, "@2", size=46), T("OR WORSE... HE'D BELIEVE YOU", 0.5, 0.48, "@4", size=46)])
S([61, 62], "kitchen", [A("rio", 0.42, [[0, "relaxed"], ["@1", "talk"]], "nervous", talk=["@1", 1]), A("tom", 0.56, "relaxed", "smile", facing=-1)], [], text=[T("\"A FRIEND OF THE FAMILY\"", 0.5, 0.16, "@1", size=54)])
S([63, 64, 65], "kitchen", [A("tom", [[0, 0.56], ["@1.5", 0.42]], [[0, "shrug"], ["@1", "explain"], ["@2", "sitTable"]], "smile", talk=["@1", 1], facing=[[0, -1], ["@1.6", 1]]), A("rio", [[0, 0.42], ["@2", 0.62]], [[0, "relaxed"], ["@2.5", "sitTable"]], "nervous", facing=-1)], [TBL], text=[T("\"SIT DOWN.\"", 0.5, 0.16, "@2")])
S([66, 67], "kitchen", [tom(x=0.42, hold={"k": "newspaper"}), rio_seat(expr="awe")], [TBL], card=card("MINUTE 7", None, at=0.05, x=0.25))
S([68, 69, 70], "kitchen", [tom(x=0.42, hold={"k": "newspaper"}, expr="smile"), rio_seat(expr="cry")], [TBL], cam={"z": [1.6, 1.75], "x": [-160, -160], "y": [-110, -110]}, text=[T("THE LITTLE SCAR ON HIS CHIN", 0.5, 0.14, "@1", size=46), T("HE HUMS WHEN HE READS", 0.5, 0.24, "@2", size=46)], props=[P("note", 0.32, 0.35, 30, "@2.2"), P("note", 0.28, 0.3, 24, "@2.5")])
S([71, 72, 73], "kitchen", [], [], tpl="science", params={"sci": "MEMORY REBUILDS", "icon": "brain"})
S([74], "face", [], [], who="rio", expr=[[0, "awe"]], bg="kitchen")

# ---- young Rio ----
S([75, 76, 77], "kitchen", [tom(x=0.42, hold={"k": "newspaper"}), rio_seat(expr=[[0, "neutral"], ["@1", "surprised"]])], [TBL, {"k": "stairs", "x": 0.02}], card=card("MINUTE 9", None, at=0.05, x=0.75), text=[T("STOMP... STOMP", 0.2, 0.3, "@1", size=50), T("SLAM!", 0.3, 0.2, "@2")])
S([78, 79, 80], "kitchen", [A("rioKid", [[0, 0.25], [0.4, 0.04], ["@0.9", 0.24]], "relaxed", "neutral", yk=[[0, -0.27], [0.4, 0], ["@0.9", 0]], hold={"k": "phone"}, walkArms=True), tom(x=0.42, hold={"k": "newspaper"}), rio_seat(expr=[[0, "surprised"], ["@2", "shocked"]])], [TBL, {"k": "stairs", "x": 0.02}],
  text=[T("HEADPHONES. MESSY HAIR.", 0.5, 0.14, "@1", size=46), T("IT'S YOU", 0.62, 0.26, "@2")])
S([81, 82], "kitchen", [A("rioKid", 0.28, "talk", "happy", talk=[0, 1], hold={"k": "phone"}), tom(x=0.42, expr="smile", facing=-1), rio_seat(expr="surprised")], [TBL], text=[T("\"DAD! CAN I GO TO JOSH'S?\"", 0.4, 0.16, 0.2, size=52)])
S([83, 84], "kitchen", [A("rioKid", 0.28, "relaxed", "neutral", hold={"k": "phone"}), tom(x=0.42, pose="sitTable", expr="smile", facing=-1, talk=["@1", 1]), rio_seat(expr="smile")], [TBL], text=[T("\"HOMEWORK FIRST, CHAMP.\"", 0.4, 0.16, "@1", size=52)])
S([85, 86], "kitchen", [A("rioKid", [[0, 0.28], ["@1", 0.28], ["@1.8", -0.08]], [[0, "facepalm"], ["@0.8", "relaxed"]], "angry", hold={"k": "phone"}), tom(x=0.42, expr="smile"), rio_seat(expr="surprised")], [TBL], text=[T("\"UGH. FINE.\"", 0.3, 0.2, 0.3, size=54)])
S([87, 88], "kitchen", [tom(x=0.42, hold={"k": "newspaper"}), rio_seat(expr=[[0, "shocked"], ["@1", "confused"]])], [TBL], text=[T("WAS I REALLY THAT RUDE?", 0.5, 0.16, "@1", size=52)])
S([89, 90], "kitchen", [tom(x=0.42, expr="joy", talk=["@1", 1]), rio_seat(expr="smile")], [TBL], text=[T("HA HA", 0.38, 0.2, 0.1), T("\"HE'S FOURTEEN.\"", 0.42, 0.3, "@1", size=52)])
S([91, 92], "kitchen", [], [], tpl="science", params={"sci": "BRAIN DONE ~25", "icon": "brain"})
S([93, 94], "kitchen", [tom(x=0.42, expr="joy"), rio_seat(expr="joy")], [TBL], text=[T("HALF A BRAIN", 0.5, 0.16, 0.1), T("HA HA HA", 0.5, 0.26, "@1", size=54)])

# ---- the temptation ----
S([95, 96, 97], "kitchen", [A("rio", 0.42, "think", [[0, "thinking"], ["@1", "smirk"]])], [], card=card("MINUTE 12", None, at=0.05, x=0.75), thought={"props": ["money", "chart"], "x": 0.25, "y": 0.28, "at": "@1"})
S([98], "space", [], [], card=card("~$1.65 BILLION", "Google buys YouTube in two months", at=0.05, w=780), props=[P("money", 0.5, 0.6, 70, 0.3)])
S([99, 100], "space", [], [], text=[T("TWITTER JUST LAUNCHED", 0.5, 0.35, 0.05, size=56), T("FACEBOOK OPENS TO EVERYONE", 0.5, 0.5, "@1", size=52)], props=[P("phone", 0.5, 0.7, 50, 0.2)])
S([101, 102], "space", [], [], card=card("50x+", "Apple stock over the next 20 years", at="@1", w=700), props=[P("chart", 0.5, 0.6, 80, 0.2)])
S([103, 104, 105, 106, 107], "kitchen", [A("rio", [[0, 0.42], ["@1", 0.28]], [[0, "relaxed"], ["@1.2", "point"], ["@4", "think"]], [[0, "thinking"], ["@4", "smirk"]], facing=-1)], [{"k": "stairs", "x": 0.02}], text=[T("BUY APPLE STOCK.", 0.62, 0.14, "@1", size=50), T("SAVE EVERY DOLLAR.", 0.62, 0.24, "@2", size=46), T("DON'T SELL.", 0.62, 0.34, "@3", size=46)], thought={"props": ["house", "money"], "x": 0.6, "y": 0.5, "at": "@4"})
S([108, 109, 110], "kitchen", [A("rio", 0.4, "think", "smirk")], [], thought={"props": ["car", "money", "house"], "x": 0.62, "y": 0.3, "at": 0.05}, text=[T("NO MORE STUDENT LOANS", 0.5, 0.14, "@1", size=46), T("NO MORE TINY APARTMENT", 0.5, 0.56, "@2", size=46)])
S([111, 112], "kitchen", [A("rio", 0.42, [[0, "shrug"], ["@1", "point"]], "smirk")], [], text=[T("WHO WOULDN'T?", 0.5, 0.16, 0.1), T("WOULDN'T YOU?", 0.5, 0.26, "@1")])

# ---- why you came ----
S([113, 114], "kitchen", [A("rio", 0.42, [[0, "relaxed"], ["@1", "sad"]], [[0, "smirk"], ["@1", "sad"]])], [], card=card("MINUTE 15", None, at=0.05, x=0.75))
S([115, 116, 117, 118, 119], "room", [A("tom", 0.5, [[0, "relaxed"], ["@1", "chest"], ["@3", "holdFront"], ["@4", "shrug"]], [[0, "neutral"], ["@1", "worried"], ["@4", "smile"]], talk=["@4", 1], facing=-1), A("rioKid", [[0, 0.1], ["@0.8", 0.3]], "relaxed", "worried")], [{"k": "car", "x": 0.85, "color": "#5a6a8a"}], fx=["night"], card=card("2007", "a night in the garage", at=0.05, x=0.75), text=[T("\"JUST HEARTBURN, CHAMP\"", 0.5, 0.16, "@4", size=50)], **GAR)
S([120], "kitchen", [], [TBL, {"k": "dish", "x": 0.45, "food": "cocoa", "at": -1}], fx=["dark"], text=[T("TWO DAYS LATER", 0.5, 0.2, 0.1, size=56)])
S([121, 122, 123, 124, 125], "hospital", [A("doctor", 0.6, "explain", "sad", facing=-1, talk=[0, "@2.9"]), A("rioKid", 0.35, "sad", "cry")], [], card=card("WARNING SIGNS", "for months", at=0.05, x=0.3), text=[T("CHEST PRESSURE", 0.72, 0.16, "@1", size=44), T("SHORT BREATH... COLD SWEATS", 0.68, 0.26, "@2", size=40), T("HE NEVER TOLD ANYONE", 0.5, 0.42, "@3", size=50)])
S([126, 127], "hospital", [], [], card=card("~800,000", "heart attacks a year in the US", at=0.05, w=700), props=[P("heart", 0.5, 0.58, 80, 0.2)], text=[T("MANY HAVE WARNING SIGNS FIRST", 0.5, 0.42, "@1", size=46)])
S([128, 129, 130, 131], "hospital", [A("nurse", 0.22, "explain", "neutral", talk=[0, 1])], [], props=[P("heart", 0.42, 0.3, 40, 0.05), P("hand", 0.56, 0.3, 40, "@1"), P("lungs", 0.7, 0.3, 40, "@2"), P("sweat", 0.84, 0.3, 40, "@3")],
  text=[T("CHEST PAIN OR PRESSURE", 0.62, 0.48, 0.05, size=40), T("ARM, JAW OR BACK", 0.62, 0.56, "@1", size=40), T("SHORT OF BREATH", 0.62, 0.64, "@2", size=40), T("COLD SWEAT, NAUSEA", 0.62, 0.72, "@3", size=40)])
S([132, 133], "kitchen", [A("tom", 0.45, [[0, "chest"], ["@0.6", "shrug"]], [[0, "worried"], ["@0.6", "smile"]])], [TBL], text=[T("MANY PEOPLE IGNORE THEM", 0.5, 0.16, 0.05, size=50), T("JUST LIKE YOUR DAD", 0.5, 0.26, "@1", size=50)])

# ---- the crossword ----
S([134, 135, 136, 137], "kitchen", [tom(x=0.42, hold={"k": "pen"}, expr="thinking"), rio_seat(expr="smile")], [TBL], card=card("MINUTE 18", None, at=0.05, x=0.75), props=[P("pencil", 0.47, 0.5, 30, "@1")], text=[T("A CROSSWORD... IN PEN", 0.4, 0.16, "@2", size=50)])
S([138, 139, 140, 141], "kitchen", [tom(x=0.42, hold={"k": "pen"}, expr=[[0, "confused"], ["@1", "smirk"]], talk=["@1", "@2.9"]), rio_seat(expr=[[0, "smile"], ["@3", "cry"]])], [TBL], text=[T("\"SOME THINGS CAN'T WAIT, BUDDY.\"", 0.5, 0.14, "@1", size=48), T("\"MIGHT AS WELL GUESS.\"", 0.5, 0.24, "@2", size=48)])
S([142, 143, 144], "kitchen", [tom(x=0.42, hold={"k": "pen"}), rio_seat(expr="sad")], [TBL], cam={"z": [1.4, 1.5], "x": [230, 230], "y": [-60, -60]}, text=[T("HIS LINE", 0.5, 0.14, "@1"), T("THE ONE THING HE NEVER DID FOR HIMSELF", 0.5, 0.24, "@2", size=40)])
S([145, 146, 147, 148, 149, 150], "kitchen", [A("rio", [[0, 0.5], ["@0.8", 0.74]], [[0, "relaxed"], ["@1", "reach"], ["@4", "sad"]], [[0, "neutral"], ["@2", "smile"], ["@5", "sad"]])], [{"k": "paper", "x": 0.94, "up": 1.2, "s": "YELLOWSTONE"}, {"k": "paper", "x": 0.94, "up": 0.85, "s": "NEXT SUMMER!"}],
  cam={"z": [1.3, 1.55], "x": [420, 520], "y": [-60, -60]}, props=[P("map", 0.8, 0.22, 40, "@0.5")], text=[T("OLD FAITHFUL", 0.45, 0.16, "@1", size=50), T("THE TRIP NEVER HAPPENED", 0.45, 0.26, "@5", size=46)])

# ---- the house, the old room ----
S([151, 152, 153], "kitchen", [A("rio", [[0, 0.75], ["@2", 0.3]], [[0, "relaxed"], ["@2.1", "reach"]], "smile")], [], card=card("MINUTE 25", None, at=0.05, x=0.25), text=[T("THE DUCKS", 0.3, 0.42, "@2.2", size=50)])
S([154, 155, 156, 157, 158], "bedroom", [A("rioKid", 0.55, "type", [[0, "neutral"], ["@2", "smile"]]), A("rio", 0.2, "relaxed", [[0, "neutral"], ["@3", "smile"]])], [{"k": "desk", "x": 0.6}], props=[P("robot", 0.62, 0.42, 40, "@2")], text=[T("PRETENDING TO DO HOMEWORK", 0.5, 0.14, "@1", size=46), T("A CARTOON ROBOT", 0.62, 0.24, "@2", size=46), T("FOR THE NEXT 20 YEARS", 0.4, 0.34, "@4", size=44)])
S([159, 160, 161], "kitchen", [A("rio", 0.42, "relaxed", "worried")], [], card=card("MINUTE 30", "half your time is gone", at=0.05, x=0.68, w=620), props=[P("clock", 0.3, 0.3, 50, "@1")])
S([162, 163, 164, 165, 166, 167, 168], "kitchen", [A("rio", 0.5, [[0, "think"], ["@1", "point"], ["@2", "point"], ["@3", "think"]], "thinking", facing=[[0, 1], ["@1", -1], ["@2", 1]])], [], props=[P("money", 0.2, 0.36, 60, "@1"), P("heart", 0.8, 0.36, 60, "@2")],
  text=[T("GET RICH", 0.2, 0.2, "@1"), T("SAVE DAD", 0.8, 0.2, "@2"), T("ONE MESSAGE. ONE PERSON. NOT TWO.", 0.5, 0.56, "@3", size=44)])

# ---- the stairs ----
STAIRS = {"k": "stairs", "x": 0.3}
S([169, 170, 171, 172, 173, 174], "kitchen", [A("rio", [[0, 0.22], ["@0.6", 0.3], ["@3", 0.44]], [[0, "relaxed"], ["@3.2", "think"]], [[0, "determined"], ["@3", "smirk"], ["@5", "thinking"]], yk=[[0, 0], ["@0.6", 0], ["@3", -0.17]])], [STAIRS],
  card=card("MINUTE 35", None, at=0.05, x=0.2), text=[T("TOWARD YOUR YOUNGER SELF", 0.72, 0.36, "@1", size=44), T("YOU'D BE RICH", 0.72, 0.46, "@3", size=50)], thought={"props": ["money", "stethoscope"], "x": 0.78, "y": 0.62, "at": "@5"})
S([175, 176, 177], "kitchen", [A("rio", 0.44, "think", [[0, "surprised"], ["@1", "worried"]], yk=-0.17)], [STAIRS], text=[T("BUT WAIT.", 0.5, 0.14, 0.05), T("NOBODY WILL KNOW HE'S SICK", 0.62, 0.26, "@1", size=46)])
S([178, 179, 180, 181, 182], "kitchen", [A("rio", 0.44, [[0, "relaxed"], ["@2", "chest"]], [[0, "worried"], ["@3", "sad"]], yk=-0.17, facing=-1)], [STAIRS], card=card("MINUTE 40", None, at=0.05, x=0.75), props=[P("note", 0.2, 0.55, 30, "@3"), P("note", 0.15, 0.5, 24, "@3.4")], text=[T("WHISTLING... OFF KEY", 0.25, 0.4, "@3", size=44)])
S([183, 184, 185], "kitchen", [A("rio", [[0, 0.44], ["@1.2", 0.44], ["@2.8", 0.22]], "relaxed", "determined", yk=[[0, -0.17], ["@1.2", -0.17], ["@2.8", 0]], facing=-1)], [STAIRS], card=card("MINUTE 45", "15 minutes left", at=0.05, x=0.75))

# ---- the message ----
S([186, 187, 188], "kitchen", [tom(x=0.42, hold={"k": "pen"}, expr="worried", facing=1, talk=["@1", 1]), A("rio", [[0, 0.85], ["@0.8", 0.7]], "relaxed", "sad", facing=-1)], [TBL], text=[T("\"EVERYTHING OKAY, BUDDY?\"", 0.42, 0.14, "@1", size=48), T("\"YOU LOOK PALE.\"", 0.42, 0.24, "@2", size=48)])
S([189, 190, 191, 192], "kitchen", [tom(x=0.42, hold={"k": "pen"}, expr="confused"), A("rio", [[0, 0.7], ["@0.6", 0.62]], [[0, "relaxed"], ["@0.7", "sitTable"]], [[0, "sad"], ["@1", "determined"]], facing=-1, talk=["@2", 1])], [TBL], text=[T("\"TOM... I NEED TO TELL YOU SOMETHING.\"", 0.5, 0.14, "@2", size=44), T("\"AND I NEED YOU TO REALLY LISTEN.\"", 0.5, 0.24, "@3", size=44)])
S([193], "kitchen", [tom(x=0.42, hold={"k": "pen", "to": 0.4}, expr="worried"), rio_seat(expr="determined")], [TBL], cam={"z": [1.5, 1.6], "x": [-160, -160], "y": [-80, -80]}, props=[P("pencil", 0.46, 0.55, 30, 0.45)])
S([194, 195, 196, 197, 198, 199], "kitchen", [tom(x=0.42, expr=[[0, "confused"], ["@2", "worried"], ["@4", "scared"]]), rio_seat(expr="determined", talk=[0, 1])], [TBL],
  text=[T("\"PRESSURE IN YOUR CHEST\"", 0.5, 0.14, 0.05, size=46), T("\"WHEN YOU CLIMB STAIRS\"", 0.5, 0.24, "@2", size=44), T("\"YOUR LEFT ARM FEELS HEAVY\"", 0.5, 0.34, "@4", size=44), T("\"YOU'VE BEEN CALLING IT HEARTBURN\"", 0.5, 0.44, "@5", size=42)])
S([200, 201], "kitchen", [tom(x=0.42, expr=[[0, "scared"]], talk=["@1", 1]), rio_seat(expr="sad")], [TBL], cam={"z": [1.5, 1.6], "x": [-160, -160], "y": [-80, -80]}, text=[T("\"HOW DO YOU KNOW THAT?\"", 0.5, 0.16, "@1", size=50)])
S([202, 203, 204, 205, 206], "kitchen", [tom(x=0.42, expr="scared"), rio_seat(expr=[[0, "sad"], ["@2", "determined"]], talk=[0, 1])], [TBL], text=[T("\"GO TO A DOCTOR.\"", 0.5, 0.14, "@2", size=52), T("\"NOT NEXT SUMMER... THIS WEEK.\"", 0.5, 0.24, "@4", size=48)])
S([207, 208, 209, 210], "kitchen", [tom(x=0.42, expr=[[0, "scared"], ["@2", "surprised"]], talk=["@3", 1]), rio_seat(expr="sad")], [TBL], cam={"z": [1.3, 1.55], "x": [-160, -200], "y": [-60, -80]}, text=[T("\"WHO ARE YOU?\"", 0.42, 0.16, "@3")])
S([211, 212, 213], "kitchen", [tom(x=0.42, expr="surprised"), rio_seat(expr=[[0, "sad"], ["@0.5", "smile"]], talk=["@1", 1])], [TBL], text=[T("\"SOME THINGS CAN'T WAIT, TOM.\"", 0.5, 0.14, "@1", size=48), T("\"MIGHT AS WELL GUESS.\"", 0.5, 0.24, "@2", size=48)])
S([214], "face", [], [], who="tom", expr=[[0, "shocked"]], bg="kitchen")
S([215, 216], "kitchen", [tom(x=0.42, expr="shocked"), rio_seat(expr="sad", alpha=[[0, 1], ["@1.5", 0]])], [TBL], fx=["speed"], cam={"z": [1.0, 1.3]})
S([217, 218], "kitchen", [A("tom", [[0, 0.42], ["@0.5", 0.42], ["@1.5", 0.2]], [[0, "relaxed"], ["@1.6", "phoneEar"]], "determined", facing=[[0, 1], ["@0.6", -1]], hold={"k": "phone", "from": "@1.6"})], [TBL, {"k": "wallphone", "x": 0.15}], fx=["speed"])
S([219], "room", [], [], fx=["dark"], text=[T("...", 0.5, 0.45, 0.2, size=90)], wall="#0a0a10", wall2="#050508")

# ---- 2026 ----
S([220, 221, 222, 223, 224], "room", [A("rio", [[0, 0.4], ["@2", 0.4]], [[0, "lie"], ["@2", "kneel"], ["@3", "sad"]], [[0, "sleepy"], ["@1", "confused"], ["@3", "sad"]], rot=[[0, -1.5708], ["@2", -1.5708], ["@2.3", 0]], yk=[[0, 0.126], ["@2", 0.126], ["@2.3", 0]])], [dict(MACH, x=0.6, cracked=True, glow=0)],
  card=card("2026", "grandpa's garage", at=0.05, x=0.25), text=[T("THE DIAL IS CRACKED", 0.62, 0.3, "@3", size=46), T("IT WILL NEVER WORK AGAIN", 0.62, 0.4, "@4", size=46)], **GAR)
S([225, 226, 227, 228, 229], "room", [A("rio", 0.42, "phone", [[0, "neutral"], ["@3", "sad"]], hold={"k": "phone"})], [], text=[T("SAME TINY APARTMENT", 0.62, 0.14, "@1", size=46), T("SAME STUDENT LOANS", 0.62, 0.24, "@2", size=46), T("NOT RICH. NOT EVEN A LITTLE.", 0.5, 0.34, "@3", size=46)], **APT)
S([230, 231, 232, 233, 234], "room", [A("rio", 0.42, [[0, "think"], ["@3", "handsOnHead"]], [[0, "worried"], ["@3", "scared"]])], [], text=[T("DID IT WORK?", 0.65, 0.16, 0.05), T("DID HE GO?", 0.65, 0.26, "@1"), T("DID HE BELIEVE YOU?", 0.65, 0.36, "@2", size=52)], **APT)
S([235, 236, 237, 238], "highway", [A("rio", 0.48, "sit", "sad", dy=0, clip=0.62)], [{"k": "car", "x": 0.5, "drive": True, "color": "#7a7a86"}, {"k": "car", "x": 0.5, "drive": True, "color": "#7a7a86", "part": "front", "front": True}], fx=["speed"], text=[T("TO MOM'S HOUSE", 0.5, 0.16, 0.05), T("TOO SAD. TOO QUIET.", 0.5, 0.26, "@2", size=50)])
S([239, 240, 241], "kitchen", [A("rio", [[0, 0.05], ["@0.8", 0.25]], [[0, "relaxed"], ["@1.5", "chest"]], [[0, "sad"], ["@1", "surprised"], ["@2", "shocked"]])], [door(0.08, open=[[0, 0.2], [0.3, 1]]), TBL], props=[P("coffee", 0.5, 0.42, 40, "@1"), P("note", 0.62, 0.32, 30, "@2"), P("note", 0.68, 0.26, 24, "@2.4")], text=[T("HUMMING... OFF KEY", 0.6, 0.18, "@2", size=50)])
S([242, 243, 244, 245], "kitchen", [A("tomOld", 0.48, "sitTable", [[0, "thinking"], ["@3", "smile"]], hold={"k": "pen"}, facing=-1), A("rio", 0.25, "relaxed", "shocked")], [{"k": "table", "x": 0.4, "w": 1.2}], card=card("72 YEARS OLD", "gray hair, a little scar on his chin", at=0.05, x=0.7, w=640), text=[T("A CROSSWORD... IN PEN", 0.62, 0.36, "@2", size=46)])
S([246, 247], "kitchen", [A("tomOld", 0.48, "sitTable", "joy", facing=-1, talk=[0, 1]), A("rio", 0.25, "relaxed", "cry")], [{"k": "table", "x": 0.4, "w": 1.2}], text=[T("\"HEY, CHAMP! YOU'RE EARLY.\"", 0.5, 0.16, 0.1, size=52)])
S([248, 249, 250, 251], "kitchen", [A("tomOld", 0.48, [[0, "sitTable"], ["@2", "shrug"]], [[0, "smile"], ["@2", "joy"]], facing=-1, talk=["@2", 1]), A("rio", 0.25, "relaxed", "cry")], [{"k": "table", "x": 0.4, "w": 1.2}], text=[T("\"YOU LOOK LIKE YOU'VE SEEN A GHOST.\"", 0.5, 0.16, "@3", size=46)])
S([252], "kitchen", [A("rio", [[0, 0.25], [0.3, 0.44]], [[0, "relaxed"], [0.35, "hug"]], "cry"), A("tomOld", 0.5, [[0, "relaxed"], [0.35, "hug"]], [[0, "smile"], [0.35, "surprised"]], facing=-1)], [{"k": "table", "x": 0.7, "w": 1.0}], text=[T("HIS GLASSES FALL OFF", 0.5, 0.16, 0.5, size=46)])
S([253, 254, 255, 256, 257, 258, 259], "kitchen", [A("oldwoman", 0.38, "sitTable", "sad", talk=[0, "@5.5"]), rio_seat(expr=[[0, "neutral"], ["@3", "surprised"], ["@5", "cry"]])], [TBL],
  card=card("3 BLOCKED ARTERIES", "surgery that same month", at="@4", x=0.7, w=640), text=[T("A STRANGER IN THE KITCHEN", 0.27, 0.14, "@1", size=40), T("HE SAW A DOCTOR THAT WEEK", 0.27, 0.24, "@3", size=40)])
S([260, 261, 262, 263, 264], "kitchen", [A("rio", 0.72, "reach", [[0, "smile"], ["@3", "cry"]])], [{"k": "paper", "x": 0.94, "up": 1.2, "s": "YELLOWSTONE"}, {"k": "paper", "x": 0.94, "up": 0.85, "s": "THIS SUMMER. RIO"}], cam={"z": [1.4, 1.6], "x": [500, 540], "y": [-60, -60]},
  text=[T("\"NEXT SUMMER!\" CROSSED OUT", 0.45, 0.16, "@2", size=44), T("THIS SUMMER. WITH RIO.", 0.45, 0.26, "@3", size=48)])

# ---- Yellowstone ----
GEY = {"k": "geyser", "x": 0.72}
S([265, 266, 267], "canyon", [A("rio", 0.3, "relaxed", "smile"), A("tomOld", 0.38, "relaxed", "joy"), A("crowd1", 0.15, "relaxed", "neutral"), A("crowd2", 0.48, "relaxed", "neutral")], [GEY], card=card("JUNE", "Yellowstone, Old Faithful", at=0.05, x=0.68, w=600))
S([268, 269, 270], "canyon", [A("rio", 0.3, "relaxed", "joy", talk=["@2", 1]), A("tomOld", 0.38, "explain", "smile", facing=-1, talk=[0, "@0.9"])], [GEY], cam={"z": [1.4, 1.45], "x": [-300, -300], "y": [-60, -60]}, text=[T("\"SOME THINGS CAN'T WAIT\"", 0.5, 0.14, 0.1, size=50), T("\"MIGHT AS WELL GUESS\"", 0.5, 0.24, "@2", size=50)])
S([271, 272, 273], "canyon", [A("rio", 0.3, [[0, "relaxed"], [0.2, "cheer"]], "awe"), A("tomOld", 0.38, [[0, "relaxed"], [0.25, "cheer"]], "joy"), A("crowd1", 0.15, [[0, "relaxed"], [0.3, "cheer"]], "awe"), A("crowd2", 0.48, [[0, "relaxed"], [0.3, "point"]], "awe")], [dict(GEY, erupt=0.1)], card=card("~50 METERS", "of steam and water", at="@1", x=0.3, w=560), text=[T("AND YOUR DAD IS THERE TO SEE IT", 0.5, 0.42, "@2", size=46)])

# ---- science ----
S([274, 275], "space", [], [], text=[T("IS TIME TRAVEL REAL?", 0.5, 0.42, 0.05, size=80), T("IN A STRANGE WAY... YES", 0.5, 0.56, "@1", size=50)])
S([276], "space", [], [], card=card("EINSTEIN", "time moves differently with speed and gravity", at=0.05, w=860), props=[P("clock", 0.5, 0.6, 70, 0.3)])
S([277, 278, 279], "space", [], [], props=[P("satellite", 0.35, 0.55, 80, 0.05), P("astronaut", 0.65, 0.55, 70, "@1")], card=card("6 MONTHS ON THE ISS", "you come home a few thousandths of a second younger", at="@1", w=900))
S([280, 281, 282, 283], "space", [], [], text=[T("THAT'S TRAVEL INTO THE FUTURE", 0.5, 0.3, 0.05, size=56), T("THE PAST?", 0.5, 0.44, "@1", size=70), T("NO ONE HAS EVER DONE IT", 0.5, 0.58, "@2", size=50)], props=[P("question", 0.5, 0.78, 50, "@3")])
S([284], "kitchen", [A("tomOld", 0.45, "relaxed", "smile"), A("rio", 0.55, "relaxed", "smile", facing=-1)], [], text=[T("WOULD YOU GO BACK IF YOU COULD?", 0.5, 0.16, 0.1, size=50)])

# ---- teaser ----
S([285, 286], "kitchen", [A("tomOld", 0.42, "chest", "worried")], [TBL], text=[T("AND ONE MORE THING...", 0.5, 0.14, 0.05, size=50), T("THE SURGERY SCAR STILL BOTHERS HIM", 0.5, 0.24, "@1", size=44)])
S([287, 288, 289], "room", [A("rio", [[0, 0.2], ["@0.8", 0.45]], [[0, "relaxed"], ["@1", "crouch"]], [[0, "neutral"], ["@1", "surprised"]])], [door(0.8)], props=[P("bag", 0.55, 0.68, 40, 0.1), P("letter", 0.55, 0.42, 45, "@1")], text=[T("\"IT CAN CURE ANYTHING.\"", 0.5, 0.16, "@2", size=52)], **APT)
S([290, 291], "face", [], [], who="rio", expr=[[0, "smile"]])
S([292], "end", [], [], tpl="end")

v3_pass(36)
save(36, 293)
