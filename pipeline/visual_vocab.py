"""visual_vocab.py - maps the words of a sentence to things the animation can show.

props_in(sentence)  -> ordered list of (prop_key, word_index)
action_in(sentence) -> action key for Rio (fly, run, swim, climb, eat, sleep, ...)
LOC2                -> extra locations, checked before the original LOC list
power_of(title, knob) -> power effect key used on Rio in every shot of that video
"""
import re

PROP_WORDS = {
    "kidney": "kidney kidneys urine urea pee peeing bladder filter filters",
    "toilet": "toilet toilets bathroom restroom",
    "tooth": "tooth teeth smile dentist wisdom molar",
    "cavity": "cavity cavities decay",
    "nose": "nose noses nostril nostrils smell smells sniff mucus snot sneeze",
    "mouth": "mouth mouths saliva spit tongue swallow swallows burp burps breath",
    "blood": "blood bleed bleeds bleeding clot clots nosebleed veins vein",
    "sweat": "sweat sweats sweating sweaty",
    "knee": "knee knees kneecap kneecaps joint joints knuckle knuckles crack cracks",
    "ribs": "rib ribs ribcage chest",
    "thumb": "thumb thumbs finger fingers pinky",
    "hair": "hair hairs gray eyebrow eyebrows eyelash eyelashes",
    "carrot": "carrot carrots orange",
    "pepper": "spicy pepper peppers hot sauce capsaicin chili",
    "gum": "gum chewing",
    "vitamin": "vitamin vitamins scurvy",
    "octopus": "octopus octopuses",
    "tail": "tail tails tailbone",
    "dizzy": "dizzy dizziness spin",
    "headache": "headache headaches migraine",
    "itch": "itch itchy itching scratch mosquito",
    "bruise": "bruise bruises purple",
    "foot": "foot toes tingling",
    "smile": "smile smiles smiling happy happier",
    "mute": "silence silent quiet",
    "leaf": "solar sunlight photosynthesis plant plants leaf leaves",
    "tissue": "tissue tissues cold",
    "gravity": "gravity g-force heavy weight",
    "window": "window windows",
    "radio": "radio",
    "shirt": "shirt jacket clothes",
    "game": "game games video game controller",
    "table": "table",
    "earth": "rotation rotates orbit spinning",
    "phone": "phone phones smartphone texts texted texting text message messages call calls called calling ringtone app apps notification notifications selfie",
    "laptop": "laptop computer computers keyboard email emails internet online website code hacker hackers wifi password passwords",
    "tv": "tv television broadcast news channel channels livestream stream streaming viewers show shows episode",
    "camera": "camera cameras photo photos picture pictures photographer filming film footage video videos",
    "mic": "microphone mic podcast interview speech",
    "car": "car cars drive drives driving driver taxi truck traffic uber",
    "bus": "bus buses",
    "ambulance": "ambulance ambulances paramedic paramedics",
    "police": "police cop cops officer officers detective arrest arrested",
    "plane": "plane planes airplane airport flight flights jet pilot",
    "helicopter": "helicopter helicopters chopper",
    "rocket": "rocket rockets launch nasa spacecraft",
    "boat": "boat boats ship ships sailor kayak canoe ferry",
    "bike": "bike bikes bicycle cycling",
    "money": "money cash dollars dollar paid pay paycheck salary rich fortune bucks bills million millions billion sponsor sponsors deal offer",
    "coin": "coin coins cents penny",
    "diamond": "diamond diamonds jewel jewels gem necklace",
    "trophy": "trophy trophies champion championship win wins winner prize award",
    "medal": "medal medals gold olympic olympics",
    "contract": "contract contracts sign signed signature paperwork papers document documents form",
    "letter": "letter letters envelope mail note notes postcard",
    "book": "book books read reading reads novel library homework study studying",
    "newspaper": "newspaper headline headlines article",
    "pencil": "pencil pen write writes writing wrote draw drawing sketch",
    "clock": "clock clocks minute minutes hour hours time timer late",
    "watch": "watch countdown stopwatch wristwatch",
    "alarm": "alarm alarms wake",
    "hourglass": "forever hourglass",
    "calendar": "calendar day days week weeks month months year years birthday",
    "key": "key keys",
    "lock": "lock locked locks safe vault secret secrets",
    "gift": "gift gifts present presents surprise",
    "balloon": "balloon balloons party",
    "pizza": "pizza",
    "burger": "burger burgers fries sandwich food meal lunch dinner",
    "apple": "apple apples fruit healthy",
    "coffee": "coffee tea cup mug latte",
    "cake": "cake cakes candles dessert",
    "water": "water drink drinks drank thirsty sweat tears",
    "bottle": "bottle bottles",
    "pill": "pill pills medicine medication",
    "syringe": "needle shot vaccine injection",
    "bandage": "bandage wound wounds scratch scrape bleeding",
    "thermometer": "fever temperature degrees hot cold freezing heat",
    "dog": "dog dogs puppy puppies",
    "cat": "cat cats kitten",
    "bird": "bird birds pigeon pigeons crow parrot eagle seagull",
    "fish": "fish fishes goldfish",
    "shark": "shark sharks",
    "horse": "horse horses",
    "spider": "spider spiders",
    "snake": "snake snakes",
    "bee": "bee bees insect insects",
    "monkey": "monkey monkeys chimp chimpanzee ape",
    "elephant": "elephant elephants",
    "gecko": "gecko geckos lizard lizards",
    "eel": "eel eels",
    "heart": "heart hearts love loves loved heartbeat pulse kind kindness",
    "brokenheart": "heartbroken breakup",
    "star": "star stars famous fame celebrity viral",
    "fire": "fire fires flame flames burning burn smoke",
    "lightning": "lightning electricity electric volts voltage shock spark sparks power",
    "battery": "battery energy tired exhausted charge",
    "bulb": "idea ideas lightbulb bulb light lights",
    "magnifier": "search clue clues investigate notice details evidence",
    "glasses": "glasses",
    "eye": "eye eyes see sees saw seeing vision look looks stare stares blink",
    "ear": "ear ears hear hears heard hearing listen listens sound sounds noise loud whisper",
    "brain": "brain brains mind think thinks memory memories smart genius neurons",
    "lungs": "lungs breath breathe breathing oxygen air",
    "stomach": "stomach belly digest digests digestion gut hungry hunger ate eat eats eating",
    "bone": "bone bones skeleton broken",
    "muscle": "muscle muscles strong strength lift lifts",
    "dna": "dna gene genes genetic",
    "cell": "cell cells",
    "germ": "germ germs bacteria virus sick flu",
    "hand": "hand hands wave waves grab grabs fingers",
    "footprint": "footsteps footprints walk walks walked",
    "house": "house home homes apartment neighbor neighbors neighborhood",
    "building": "building buildings skyscraper tower towers city",
    "hospital": "hospital clinic",
    "school": "school class teacher teachers classmates",
    "globe": "world earth country countries planet global",
    "pin": "map location place address",
    "flag": "flag flags finish",
    "mountain": "mountain mountains cliff cliffs peak summit",
    "tree": "tree trees forest park",
    "flower": "flower flowers garden",
    "sun": "sun sunny sunlight morning",
    "moon": "moon night midnight sleep sleeps asleep",
    "cloud": "cloud clouds sky",
    "rain": "rain raining storm wet",
    "storm": "thunder hurricane tornado",
    "snowflake": "snow ice frozen winter",
    "wave": "ocean sea waves wave lake river pool swim swims swimming",
    "volcano": "volcano lava",
    "planet": "mars jupiter saturn planets",
    "astronaut": "astronaut astronauts spacesuit",
    "satellite": "satellite satellites signal",
    "wifi": "wifi wireless connected",
    "chart": "percent statistics data numbers chart grade grades score scores",
    "target": "target aim shot shots goal goals accuracy miss misses",
    "ball": "basketball ball hoop",
    "soccer": "soccer football",
    "dumbbell": "gym workout exercise weights",
    "guitar": "guitar band",
    "note": "music song songs sing sings singing singer melody pitch tune",
    "speaker": "speaker speakers concert",
    "paint": "paint painting painter art artist",
    "shield": "armor shield protect protects bulletproof",
    "magnet": "magnet magnetic",
    "robot": "robot robots ai machine",
    "ladder": "ladder climb climbs climbing",
    "rope": "rope ropes",
    "candle": "candle candles",
    "umbrella": "umbrella",
    "bed": "bed beds nap",
    "glass": "juice soda",
    "bag": "bag bags wallet",
    "crown": "king queen royal",
    "mask": "mask masks disguise face faces",
    "check": "yes right correct true",
    "cross": "wrong false fail fails",
    "warning": "danger dangerous warning careful risk risky",
    "bell": "bell doorbell",
    "siren": "emergency siren sirens 911",
    "skull": "poison poisonous deadly toxic",
    "sparkles": "magic sparkle shiny",
    "dice": "luck lucky chance odds",
    "card": "credit card bank",
    "hammer": "hammer build builds fix fixes",
    "wrench": "tools tool repair",
    "paw": "animal animals pet pets",
    "web": "web",
    "mirror": "mirror reflection",
    "ghost": "invisible ghost",
    "crowd": "crowd crowds fans audience everyone people",
    "family": "family parents mom dad",
    "baby": "baby babies newborn",
    "stethoscope": "doctor doctors nurse",
    "xray": "x-ray x-rays xray radiation",
    "bomb": "explosion explode explodes",
}
WORD2PROP = {}
for k, ws in PROP_WORDS.items():
    for w in ws.split():
        WORD2PROP.setdefault(w, k)

# generic words that should not trigger a prop on their own (too common)
WEAK = set("time look looks see sees saw right power world people everyone day days light kind face faces read wave waves fix think mind minute minutes hour hours year years week weeks month months yes true video videos hand hands breath air love loves loved place family call calls called show shows wrong crack cracks orange cold heavy weight leg legs".split())


def props_in(sentence, limit=3):
    toks = re.findall(r"[a-z0-9'-]+", sentence.lower())
    out, seen = [], set()
    strong = []
    for i, w in enumerate(toks):
        w2 = w.strip("'")
        k = WORD2PROP.get(w2) or (WORD2PROP.get(w2[:-1]) if w2.endswith("s") else None)
        if not k or k in seen: continue
        seen.add(k)
        (out if w2 in WEAK else strong).append((k, i, w2))
    res = strong + out
    return res[:limit]


ACTIONS = [
    ("fly", r"\b(fly|flies|flying|flew|soar|soars|soaring|float|floats|floating|hover|hovers|glide|glides|lift off|take off|takes off)\b"),
    ("swim", r"\b(swim|swims|swimming|swam|dive|dives|diving|underwater|splash)\b"),
    ("climb", r"\b(climb|climbs|climbing|climbed|crawl|crawls|scale|scales|up the wall|wall)\b"),
    ("jump", r"\b(jump|jumps|jumping|jumped|leap|leaps|leaping|bounce|bounces|hop)\b"),
    ("fall", r"\b(fall|falls|falling|fell|trips over|slip|slips|collapse|collapses|tumble|tumbles)\b"),
    ("run", r"\b(run|runs|running|ran|sprint|sprints|rush|rushes|race|races|chase|chases|dash|dashes|hurry)\b"),
    ("walk", r"\b(walk|walks|walking|walked|step|steps|stroll|wander|heads? (home|out|to|back)|enter|enters|leave|leaves)\b"),
    ("drive", r"\b(drive|drives|driving|drove|car|taxi)\b"),
    ("eat", r"\b(eat|eats|eating|ate|bite|bites|chew|chews|swallow|swallows|taste|tastes|lunch|dinner|breakfast|food|digest)\b"),
    ("drink", r"\b(drink|drinks|drinking|sip|sips|coffee)\b"),
    ("sleep", r"\b(sleep|sleeps|sleeping|asleep|nap|naps|bed|dream|dreams|yawn)\b"),
    ("laugh", r"\b(laugh|laughs|laughing|laughter|giggle|giggles|joke|jokes|funny)\b"),
    ("cry", r"\b(cry|cries|crying|cried|tears|sob|sobs)\b"),
    ("hug", r"\b(hug|hugs|hugging|hugged|embrace|holds? (her|him|them))\b"),
    ("phone", r"\b(phone|text|texts|scroll|scrolls|call|calls|app|message|screen)\b"),
    ("type", r"\b(type|types|typing|laptop|computer|keyboard|code|hack)\b"),
    ("read", r"\b(read|reads|reading|book|books|study|studies|homework)\b"),
    ("write", r"\b(write|writes|writing|sign|signs|draw|draws)\b"),
    ("sing", r"\b(sing|sings|singing|song|hum|hums|whistle)\b"),
    ("shout", r"\b(shout|shouts|yell|yells|scream|screams|call out)\b"),
    ("lift", r"\b(lift|lifts|lifting|carry|carries|carrying|push|pushes|pull|pulls|hold|holds)\b"),
    ("throw", r"\b(throw|throws|threw|toss|tosses|shoot|shoots|shot|kick|kicks|pass|passes)\b"),
    ("dance", r"\b(dance|dances|dancing|celebrate|celebrates|party)\b"),
    ("look", r"\b(look|looks|stare|stares|see|sees|watch|watches|spot|spots|notice|notices|scan|scans|peek)\b"),
    ("listen", r"\b(listen|listens|hear|hears|heard)\b"),
    ("talk", r"\b(say|says|said|tell|tells|ask|asks|explain|explains|whisper|whispers|talk|talks|speak|speaks)\b"),
    ("think", r"\b(think|thinks|wonder|wonders|remember|remembers|realize|realizes|imagine|decide|decides|plan)\b"),
    ("sit", r"\b(sit|sits|sitting|sat|desk|couch|chair)\b"),
    ("wave", r"\b(wave|waves|hello|hi|goodbye|bye)\b"),
    ("cheer", r"\b(cheer|cheers|win|wins|won|yes!|amazing|incredible|awesome|perfect)\b"),
]


def action_in(sentence):
    low = sentence.lower()
    for k, rx in ACTIONS:
        if re.search(rx, low): return k
    return None


LOC2 = [
    ("space", r"\b(space|orbit|astronaut|astronauts|spacewalk|moon|mars|planet|planets|galaxy|rocket|vacuum|space station|zero gravity)\b"),
    ("sky", r"\b(sky|clouds?|flying|flight|airborne|above the city|thousand feet in the air|in the air)\b"),
    ("ocean", r"\b(ocean|sea|seas|waves|underwater|reef|whale|sharks?|ship|boat)\b"),
    ("beach", r"\b(beach|sand|shore|surf|surfing|palm)\b"),
    ("poolside", r"\b(swimming pool|pool|lifeguard)\b"),
    ("lake", r"\b(lake|river|pond|dock|fishing)\b"),
    ("canyon", r"\b(canyon|red rock|desert cliff|grand canyon|cliff|cliffs|ledge)\b"),
    ("mountain", r"\b(mountain|mountains|peak|summit|trail|hike|hiking|climber|climbers|rescue team|avalanche)\b"),
    ("snowy", r"\b(snow|snowy|blizzard|ice|frozen|ski|skiing|winter)\b"),
    ("desert", r"\b(desert|sand dunes|cactus)\b"),
    ("forest", r"\b(forest|woods|jungle|trees|camp|campsite|zoo|farm|barn)\b"),
    ("kitchen", r"\b(kitchen|cook|cooks|cooking|stove|fridge|recipe|chef|restaurant kitchen)\b"),
    ("office", r"\b(office|boss|meeting|company|startup|coworkers?|desk|job|interview|bank|ceo)\b"),
    ("studio", r"\b(stage|show|tv|television|studio|cameras?|live|audience|concert|talent|host|reality|podcast|interview|broadcast|comedy club|comedian)\b"),
    ("bedroom", r"\b(bedroom|bed|pillow|nightmare|midnight|sleep|asleep|night)\b"),
    ("rooftop", r"\b(rooftop|roof|ledge|balcony)\b"),
    ("museum", r"\b(museum|diamond|gallery|vault|heist|exhibit|jewel)\b"),
    ("gym", r"\b(gym|workout|weights|training|trainer|court|basketball|practice)\b"),
    ("store", r"\b(store|shop|mall|supermarket|grocery|market|cashier)\b"),
    ("library", r"\b(library|librarian|bookstore)\b"),
    ("highway", r"\b(highway|interstate|road trip|freeway|truck)\b"),
    ("city", r"\b(city|downtown|new york|chicago|los angeles|traffic|crowd|crowds|street|streets)\b"),
]

POWERS = [
    ("fly", r"\bfly\b|flight"), ("invisible", r"invisib"), ("xray", r"see through|x-ray"), ("language", r"language"),
    ("lie", r"lying|lie\b|lies\b"), ("shrink", r"shrink|inch tall|tiny"), ("giant", r"20 feet|feet tall|giant|grew"),
    ("glow", r"glow"), ("reflex", r"reflex"), ("gecko", r"climb walls|gecko"), ("face", r"change your face|face at will"),
    ("electric", r"electric|eel"), ("space", r"outer space|survive in space"), ("animal", r"animal"), ("teleport", r"teleport"),
    ("future", r"future"), ("voice", r"voice"), ("stretch", r"stretch|rubber"), ("armor", r"armor|tough"), ("double", r"two of you"),
    ("internet", r"internet"), ("arms", r"four arms"), ("believe", r"believed"), ("aim", r"missed a shot|never miss"),
    ("digest", r"digest"), ("water", r"walk on water"), ("pitch", r"perfect pitch"), ("laugh", r"laugh"), ("jumpbig", r"jump as high|jump"),
    ("swap", r"swap bodies"),
]


def power_of(title, knob=""):
    s = (title + " " + (knob or "")).lower()
    for k, rx in POWERS:
        if re.search(rx, s): return k
    return None


# words in a sentence that say the power is being used right now
POWER_ON = r"\b(power|ability|gift|suddenly|again|now|watch this|use it|using it|fly|flies|flying|invisible|vanish|disappear|glow|glowing|spark|sparks|zap|stretch|teleport|blink|jump|shrink|grow|grows|see through|translate|copy|voice|arms|laugh|digest|walk on|water|catch|catches|aim|shot)\b"
