import itertools
import re
from unidecode import unidecode

def english_conversion(text):
    ROUND_S_BEFORE_BK = False # True in 17th and early 18th century
    
    if ROUND_S_BEFORE_BK:
        # selects every S that has a letter after it,
        # so long as that letter is not B nor K.
        pattern = r"s(?=[a-ac-jm-zA-AC-JM-Z])"
    else:
        # selects every S that has any letter after it.
        pattern = r"s(?=[a-zA-Z])"
    indices = [m.start() for m in re.finditer(pattern, text)]

    # excludes any S that comes before or after the letter F.
    pattern = r"s(?=f|F)|(?<=f|F)s"
    excluded_indices = [m.start() for m in re.finditer(pattern, text)]
    indices = [i for i in indices if i not in excluded_indices]
    for i in indices:
        text = text[:i] + "ſ" + text[i + 1: ]

    # replaces any occurrence of "ſſſ" with "ſsſ".
    pattern = r"ſſſ"
    indices = [m.start() for m in re.finditer(pattern, text)]
    for i in indices:
        text = text[:i] + "ſsſ" + text[i + 3: ]

    return text

_REPLACEMENTS = {
    "bonapartismus": "bonapartismus",
    "chartismus": "chartismus",
    "tripartismus": "tripartismus",
    "herbergssuche": "herbergsſuche",
    "tausalz": "tauſalz",
    "trausaal": "trauſaal",
    "bernsdorf": "bernsdorf",
    "bertoldsbrunnen": "bertoldsbrunnen",
    "kentumsprache": "kentumſprache",
    "thalassämie": "thalaſſämie",
    "thalassämien": "thalaſſämien",
    "essäpfel": "eſsäpfel",
    "dreiflüssestadt": "dreiflüſseſtadt",
    "dreiflüssestädte": "dreiflüſseſtädte",
    "odessa": "odeſſa",
    "vanessa": "vaneſſa",
    "alessandro": "aleſſandro",
    "intrauterinpessar": "intrauterinpeſſar",
    "vasall": "vaſall",
    "basal": "baſal",
    "lassalle": "laſſalle",
    "nasal": "naſal",
    "knosso": "knoſſo",
    "kassapreise": "kaſſapreise",
    "hausterrasse": "hausterraſſe",
    "austral": "auſtral",
    "inkasso": "inkaſſo",
    "isobut": "iſobut",
    "isoba": "iſoba",
    "lassob": "laſſob",
    "espresso": "espreſſo",
    "lebensodem": "lebensodem",
    "arbeitsoverall": "arbeitsoverall",
    "crossover": "croſsover",
    "passow": "paſſow",
    "lomonossow": "lomonoſſow",
    "dissert": "diſſert",
    "baſſetrüden": "baſſetrüden",
    "setymologie": "setymologie",
    "eschatologie": "eschatologie",
    "sadressat": "sadreſſat",
    "adressat": "adreſſat",
    "auster": "auſter",
    "baseballs": "baſeballſ", # UNCERTAIN
    "baseball": "baſeball", # UNCERTAIN
    "gottessöhne": "gottesſöhne",
    "renaissance": "renaiſſance",
    "bessarab": "beſsarab",
    "essay": "eſſay",
    "somelett": "somelett",
    "ssattel": "sſattel",
    "sattel": "ſattel",
    "ssattler": "sſattler",
    "sattler": "ſattler",
    "ssediment": "sſediment",
    "sediment": "ſediment",
    "sethik": "sethik",
    "sethisch": "sethiſch",
    "sessig": "seſſig",
    "syoga": "syoga",
    "lissabon": "liſſabon",
    "melissa": "meliſſa",
    "nissan": "niſſan",
    "orissa": "oriſſa",
    "clarissa": "clariſſa",
    "chamisso": "chamiſſo",
    "pissoir": "piſſoir",
    "glossar": "gloſſar",
    "ossarium": "oſſarium",
    "passat": "paſſat",
    "briefaustausch": "briefaustauſch",
    "nikolaustag": "nikolaustag",
    "schauspiel": "ſchauſpiel",
    "grausam": "grauſam",
    "klausu": "klauſu",
    "hausung": "hauſung",
    "kolossal": "koloſſal",
    "plateaus": "plateauſ",
    "mausole": "mauſole",
    "bussard": "buſſard",
    "russisch": "ruſſiſch",
    "mussolini": "muſſolini",
    "perkussorisch": "perkuſſoriſch",
    "schance": "schance",

    "genauso": "genauſo",
    "dasselb": "dasſelb",
    "sideal": "sideal",
    "sidee": "sidee",
    "sadress": "sadreſſ",
    "adressi": "adreſſi",
    "adress": "adreſs",
    "beeinflusser": "beeinfluſſer",
    "flussen": "fluſſen",
    "fluss": "fluſs",
    "interessant": "intereſſant",
    "sinteresse": "sintereſſe",
    "interesse": "intereſſe",
    "jahressi": "jahresſi",
    "kommissar": "kommiſſar",
    "kommissär": "kommiſſär",
    "skongresses": "skongreſses",
    "kongresses": "kongreſses",
    "skongresse": "skongreſſe",
    "kongresse": "kongreſſe",
    "skongress": "skongreſs",
    "kongress": "kongreſs",
    "messes": "meſſeſ",
    "messen": "meſſen",
    "messa": "meſsa",
    "messer": "meſſer",
    "messu": "meſsu",
    "messins": "meſsinſ",
    "missach": "miſsach",
    "prozesses": "prozeſses",
    "prozesse": "prozeſſe",
    "prozess": "prozeſs",
    "sache": "ſache",
    "ssöl": "ſsöl",

    "schossest": "ſchoſſeſt",
    "schosses": "ſchoſses",
    "schossen": "ſchoſſen",
    "schlossest": "ſchloſſeſt",
    "schlosses": "ſchloſses",
    "schlossen": "ſchloſſen",
    "schlosser": "ſchloſſer",
    "schloss": "ſchloſs",
    "schlusses": "ſchluſses",
    "schluss": "ſchluſs",

    "sselbs": "sſelbſ",
    "selbs": "ſelbſ",

    # aus
    "sausarbeit": "sausarbeit",
    "ausarbeit": "ausarbeit",
    "bausa": "bauſa",
    "kausa": "kauſa",
    "schausa": "ſchauſa",
    "ausa": "ausa",

    "hausä": "hausä",
    "ausä": "auſä",

    "sausen": "ſauſen",
    "ausen": "auſen",
    "sauses": "ſauſeſ",
    "auses": "auseſ",

    "ausib": "auſib",
    "ausic": "auſic",
    "ausid": "ausid",
    "hausim": "hausim",
    "ausim": "auſim",
    "hausin": "hausin",
    "ausin": "auſin",
    "ausip": "auſip",
    "ausisch": "auſiſch",
    "ausit": "auſit",

    "bauso": "bauſo",
    "auso": "auso",

    "ausu": "ausu",

    "ausüb": "ausüb",
    "ausü": "auſü",

    "auss": "ausſ",
    "bausp": "bauſp",
    "sausp": "sausp",
    "ausp": "ausp",

    "saustrag": "saustrag",
    "austrag": "austrag",
    "saustrieb": "saustrieb",
    "austrieb": "austrieb",
    "saustritt": "saustritt",
    "austritt": "austritt",
    "saustausch": "saustauſch",
    "austausch": "austauſch",
    "saustreibung": "saustreibung",
    "austreibung": "austreibung",
    "baust": "bauſt",
    "caust": "cauſt",
    "daust": "daust",
    "ffaust": "ffaust",
    "faust": "fauſt",
    "gaust": "gaust",
    "laust": "lauſt",
    "naust": "naust",
    "pfaust": "pfaust",
    "paust": "pauſt",
    "raust": "rauſt",
    "saust": "ſauſt",
    "taust": "tauſt",
    "zaust": "zauſt",

    # sch combos
    "ssch": "sſch",

    # double s with consonants.
    "bss": "bsſ",
    "css": "cſſ",
    "dss": "dsſ",
    "fss": "fsſ",
    "gss": "gsſ",
    "hss": "hsſ",
    "jss": "jſſ",
    "kss": "ksſ",
    "lss": "lsſ",
    "mss": "msſ",
    "nss": "nsſ",
    "pss": "psſ",
    "rss": "rsſ",
    "sss": "ſsſ",
    "tss": "tsſ",
    "wss": "wsſ",

    # occurrences, mostly with double letters of some kind.
    "ssassi": "ſsaſſi",
    "ssabot": "sſabot",
    "ssall": "ſsall",
    "ssamm": "sſamm",
    "ssapp": "ſsapp",
    "ssatt": "ſsatt",
    "ssab": "ſsab",
    "ssac": "sſac",
    "ssap": "ſsap",
    "ssar": "ſſar",
    "ssay": "ſſay",
    "sadd": "ſadd",
    "saff": "ſaff",
    "sagg": "sagg",
    "sakk": "sakk",
    "sall": "sall",
    "samm": "ſamm",
    "sannahm": "sannahm",
    "sannä": "sannä",
    "sapp": "sapp",
    "sarr": "sarr",
    "sassi": "saſſi",
    "satt": "satt",
    "sabot": "ſabot",
    "sab": "sab",
    "saj": "ſaj",
    "saq": "saq",   
    "saw": "ſaw",

    "ssäb": "sſäb",
    "ssäc": "sſäc",
    "ssäf": "sſäf",
    "ssäg": "sſäg",
    "ssäl": "sſäl",
    "ssät": "sſät",
    "sänn": "ſänn",
    "säss": "ſäſſ",
    "sätt": "ſätt",
    "ssä": "sſä",

    "sseff": "ſseff",
    "ssell": "ſſell",
    "sserr": "ſſerr",
    "ssett": "ſſett",
    "sseb": "ſſeb",
    "ssed": "ſſed",
    "ssenn": "ſſenn",
    "ssef": "ſſef",
    "ssels": "ſſelſ",
    "ssens": "ſſenſ",
    "ssev": "ſſev",
    "seff": "seff",
    "sell": "ſell",
    "sels": "ſelſ",
    "semm": "ſemm",
    "senn": "ſenn",
    "serr": "ſerr",
    "sess": "ſeſſ",
    "sett": "ſett",
    "sef": "ſef",
    "sev": "ſev",

    "ssipp": "sſipp",
    "ssitt": "sſitt",
    "ssib": "ſſib",
    "ssic": "sſic",
    "ssid": "sſid",
    "ssif": "ſſif",
    "ssik": "ſſik",
    "ssio": "ſſio",
    "ssir": "sſir",
    "ssit": "sſit",
    "ssiz": "ſſiz",
    "siff": "ſiff",
    "sirr": "sirr",
    "sitt": "ſitt",
    "sivv": "ſſiv",
    "sib": "ſib",
    "sic": "ſic",
    "sid": "ſid",
    "sif": "ſif",
    "sik": "ſik",
    "siv": "ſiv",
    "siw": "ſiw",

    "ssonn": "sſonn",
    "ssorr": "ſſorr",
    "ssob": "ſsob",
    "ssoc": "sſoc",
    "ssog": "sſog",
    "ssoh": "sſoh",
    "ssok": "ſsok",
    "ssol": "sſol",
    "ssom": "sſom",
    "sson": "sſon",
    "ssop": "ſsop",
    "ssow": "sſow",
    "ssoz": "sſoz",
    "sonn": "ſonn",
    "sope": "sope",
    "sopp": "ſopp",
    "sorr": "ſorr",
    "sob": "sob",
    "soc": "ſoc",
    "sod": "ſod",
    "soj": "ſoj",
    "sol": "ſol",
    "som": "ſom",
    "son": "ſon",
    "sov": "ſov",
    "sow": "ſow",
    "soz": "ſoz",

    "ssöh": "sſöh",
    "ssök": "ſsök",
    "ssöl": "ſsöl",
    "ssöm": "sſöm",
    "ssön": "sſön",
    "söc": "ſöc",
    "söd": "söd",
    "söf": "söf",
    "sög": "ſög",
    "söh": "ſöh",
    "sök": "sök",
    "söm": "ſöm",
    "sön": "ſön",
    "sör": "ſör",
    "sös": "söſ",

    "ssuff": "sſuff",
    "ssumm": "sſumm",
    "ssub": "sſub",
    "ssuc": "sſuc",
    "ssuh": "ſsuh",
    "ssul": "sſul",
    "ssung": "ſſung",
    "ssup": "sſup",
    "suff": "ſuff",
    "sugg": "ſugg",
    "sukk": "ſukk",
    "summ": "ſumm",
    "sunn": "ſunn",
    "sub": "ſub",
    "suc": "ſuc",
    "sud": "ſud",
    "suh": "suh",
    "sul": "ſul",
    "sup": "ſup",
    "sut": "sut",

    #"ssüb": "ſsüb",
    #"ssüc": "sſüc",
    #"ssüd": "sſüd",
    #"ssül": "sſül",
    #"ssün": "sſün",
    #"ssüp": "sſüp",
    "ssü": "sſü",
    "süb": "süb",
    "süc": "ſüc",
    "süd": "ſüd",
    "süf": "ſüf",
    "süh": "ſüh",
    "sül": "ſül",
    "süm": "ſüm",
    "sün": "ſün",
    "süp": "ſüp",

    "ssy": "sſy",
    "sy": "ſy",

    # terms starting with s and ending with t + consonant.
    "ssatg": "ſſatg",
    "ssatk": "ſſatk",
    "ssatm": "ſsatm",
    "ssatr": "ſsatr",
    "ssatz": "sſatz",
    "satg": "ſatg",
    "sath": "sath",
    "satk": "ſatk",
    "satl": "satl",
    "satm": "satm",
    "satr": "satr",
    "satz": "ſatz",
    
    "ssätz": "sſätz",
    "sätz": "ſätz",
    
    "sseth": "ſſeth",
    "ssetr": "ſſetr",
    "ssety": "ſſety",
    "ssetz": "sſetz",
    "setb": "ſetb",
    "setd": "ſetd",
    "setf": "ſetf",
    "setg": "ſetg",
    "seth": "ſeth",
    "setk": "ſetk",
    "setl": "ſetl",
    "setm": "ſetm",
    "setp": "ſetp",
    "setr": "ſetr",
    "sets": "ſetſ",
    "setw": "ſetw",
    "sety": "ſety",
    "setz": "ſetz",
    
    "ssitz": "sſitz",
    "sitb": "ſitb",
    "sitc": "ſitc",
    "sitd": "ſitd",
    "sitf": "ſitf",
    "sitg": "ſitg",
    "sith": "ſith",
    "sitk": "ſitk",
    "sitl": "ſitl",
    "sitm": "ſitm",
    "sitn": "ſitn",
    "sitp": "ſitp",
    "sitr": "ſitr",
    "sits": "ſitſ",
    "sitv": "ſitv",
    "sitw": "ſitw",
    "sity": "ſity",
    "sitz": "ſitz",

    "soth": "ſoth",
    "sotr": "ſotr",

    # s with eszett
    "saß": "ſaß",
    "soß": "ſoß",
    "söß": "ſöß",
    "süß": "ſüß",

    # double s with vowels
    "sassoz": "saſſoz",
    "assa": "aſſa",
    "assä": "asſä",
    "assest": "aſſeſt",
    "asses": "aſseſ",
    "asse": "aſſe",
    "assi": "aſſi",
    "assoz": "aſſoz",
    "assö": "aſsö",
    "assu": "aſſu",
    "assü": "aſsü",
    "assyr": "aſſyr",
    "assy": "asſy",
    "assas": "aſſaſ",

    "ässes": "äſſeſ",
    "ässe": "äſſe",
    "ässi": "äſſi",
    "ässu": "äſſu",

    "essatt": "eſsatt",
    "essas": "eſsaſ",
    "essan": "eſsan",
    "essar": "eſsar",
    "essä": "esſä",
    "essest": "eſſeſt",
    "esses": "eſseſ",
    "esse": "eſſe",
    "essi": "eſſi",
    "esso": "eſſo",
    "essö": "esſö",
    "essy": "esſy",

    "rissa": "riſsa",
    "issa": "isſa",
    "issä": "isſä",
    "issest": "iſſeſt",
    "isses": "iſseſ",
    "isse": "iſſe",
    "issi": "iſſi",
    "isso": "isſo",
    "issö": "iſsö",

    "ossac": "oſsac",
    "ossam": "oſſam",
    "ossar": "oſsar",
    "ossest": "oſſeſ",
    "osses": "oſseſ",
    "osse": "oſſe",
    "ossi": "oſſi",
    "ossoc": "osſoc",
    "osso": "osſo",
    "ossö": "oſsö",
    "ossu": "oſſu",
    "ossü": "osſü",

    "össe": "öſſe",
    "össi": "öſſi",

    "aussa": "ausſa",
    "ussa": "uſsa",
    "ussest": "uſſeſt",
    "usses": "uſseſ",
    "usse": "usſe",
    "ussi": "uſsi",
    "gusso": "guſso",
    "usso": "usſo",
    "ussö": "usſö",
    "ussung": "uſſung",
    "ussu": "usſu",

    "üsse": "üſſe",
    "üssi": "üſſi",

    "ysse": "yſſe",

    # suffixes.
    "bars": "barſ",
    "becks": "beckſ",
    "bergs": "bergſ",
    "bührens": "bührenſ",
    "chors": "chorſ",
    "fachs": "fachſ",
    "fähigs": "fähigſ",
    "einfalts": "einfalts",
    "sorgfältig": "ſorgfältig",
    "sorgfalts": "ſorgfalts",
    "sorgfalt": "ſorgfalt",
    "falts": "faltſ",
    "farbens": "farbenſ",
    "fertigs": "fertigſ",
    "förmigs": "förmigſ",
    "freis": "freiſ",
    "gens": "genſ",
    "gleichs": "gleichs",
    "grafs": "grafſ",
    "graphies": "graphieſ",
    "schaft": "ſchaft",
    "hafts": "hafts",
    "halbers": "halberſ",
    "hausens": "hauſens",
    "heims": "heimſ",
    "heits": "heits",
    "igste": "igſte",
    "keits": "keitſ",
    "kens": "kenſ",
    "kraties": "kratieſ",
    "kundes": "kundeſ",
    "leis": "leiſ",
    "leins": "leinſ",
    "lekts": "lektſ",
    "lers": "lerſ",
    "lichs": "lichſ",
    "lings": "lings",
    "loges": "logeſ",
    "logies": "logieſ",
    "lyses": "lyſeſ",
    "mals": "malſ",
    "metries": "metrieſ",
    "nisse": "niſſe",
    "pathies": "pathieſ",
    "reichst": "reichſt",
    "reichs": "reichs",
    "richs": "richſ",
    "sals": "ſalſ",
    "sams": "ſamſ",
    "sans": "sanſ",
    "sches": "ſcheſ",
    "seits": "ſeits",
    "sels": "ſelſ",
    "sens": "ſenſ",
    "skopies": "skopieſ", # UNCERTAIN: endos(ſ)kopie?
    "stes": "ſteſ",
    "steins": "ſteinſ",
    "tions": "tions",
    "trops": "tropſ",
    "tums": "tums",
    "volls": "vollſ",
    "wärts": "wärts",
    "weise": "weiſe",
    "werks": "werkſ",
    "werts": "wertſ",
    "wesen": "weſen",
    "witzs": "witzſ",
    "syls": "ſylſ",
    "syl": "ſyl",
    "yls": "ylſ",
}

_END_REPLACEMENTS = {
    "sses": "ſses",
    "sch": "ſch",
    "ssen": "ſſen",

    "ssterem": "ſſterem",
    "ssteren": "ſſteren",
    "ssterer": "ſſterer",
    "ssteres": "ſſteres",
    "sstere": "ſſtere",
    "sster": "ſſter",

    "sstemem": "ſſtemem",
    "sstemen": "ſſtemen",
    "sstemer": "ſſtemer",
    "sstemes": "ſſtemes",
    "ssteme": "ſſteme",
    "sstem": "ſſtem",

    "sstenem": "ſſtenem",
    "sstenen": "ſſtenen",
    "sstener": "ſſtener",
    "sstenes": "ſſtenes",
    "sstene": "ſſtene",
    "ssten": "ſſten",

    "sstes": "ſſtes",
    "sste": "ſſte",
    "sst": "ſſt",

    "sen": "ſen",

    "sterem": "ſterem",
    "steren": "ſteren",
    "sterers": "ſterers",
    "sterer": "ſterer",
    "steres": "ſteres",
    "stere": "ſtere",
    "sters": "ſters",
    "ster": "ſter",

    "stemem": "ſtemem",
    "stemen": "ſtemen",
    "stemer": "ſtemer",
    "stemes": "ſtemes",
    "steme": "ſteme",
    "stems": "ſtems",
    "stem": "ſtem",

    "stenem": "ſtenem",
    "stenen": "ſtenen",
    "stener": "ſtener",
    "stenes": "ſtenes",
    "stene": "ſtene",
    "stens": "ſtens",
    "sten": "ſten",

    "stes": "ſtes",
    "ste": "ſte",
    "st": "ſt", 

    # -abel
    "ssabel": "ſſabel",
    "sabel": "ſabel",

    # -al
    "saler": "ſaler",
    "salem": "ſalem",
    "salen": "ſalen",
    "sales": "ſales",
    "sale": "ſale",
    "sals": "ſals",
    "sal": "ſal",

    # -am
    "samerem": "ſamerem",
    "sameren": "ſameren",
    "samerer": "ſamerer",
    "sameres": "ſameres",
    "samere": "ſamere",
    "samers": "ſamers",
    "samer": "ſamer",
    "samem": "ſamem",
    "samen": "ſamen",
    "sames": "ſames",

    # -gesamt
    "gesamtem": "geſamtem",
    "gesamten": "geſamten",
    "gesamter": "geſamter",
    "gesamtes": "geſamtes",
    "gesamte": "geſamte",
    "gesamt": "geſamt",
    
    # -amt
    "samterem": "ſamterem",
    "samteren": "ſamteren",
    "samterer": "ſamterer",
    "samteres": "ſamteres",
    "samtere": "ſamtere",
    "samter": "ſamter",
    "samtem": "ſamtem",
    "samten": "ſamten",
    "samtes": "samtes",
    "samte": "ſamte",
    "samts": "samts",
    "samt": "samt",
    "sams": "ſams",
    "sam": "ſam",

    # -ant
    "ssanterem": "ſſanterem",
    "ssanteren": "ſſanteren",
    "ssanterer": "ſſanterer",
    "ssanteres": "ſſanteres",
    "ssantere": "ſſantere",
    "ssanter": "ſſanter",
    "ssans": "ſſans",
    "ssantem": "ſſantem",
    "ssanten": "ſſanten",
    "ssantes": "ſſantes",
    "ssante": "ſſante",
    "ssants": "ſſants",
    "ssant": "ſſant",

    "santerem": "ſanterem",
    "santeren": "ſanteren",
    "santerer": "ſanterer",
    "santeres": "ſanteres",
    "santere": "ſantere",
    "santers": "ſanters",
    "santer": "ſanter",
    "santem": "ſantem",
    "santen": "ſanten",
    "santes": "ſantes",
    "sante": "ſante",
    "sants": "ſants",
    "sant": "ſant",

    # -an
    "ssans": "ſſans",
    "ssan": "ſſan",
    "sane": "ſane",
    "sans": "ſans",
    "san": "ſan",

    # -anz
    "sanz": "ſanz",

    # -är
    "ssärs": "ſſärs",
    "ssär": "ſſär",
    "särs": "ſärs",
    "sär": "ſär",

    # -arm
    "ssarms": "ſsarms",
    "ssarm": "ſsarm",
    "sarms": "sarms",
    "sarm": "sarm",

    # -at
    "ssats": "ſſats",
    "ssat": "ſſat",
    "sats": "ſats",
    "sat": "ſat",

    # -artig
    "ssartigerem": "ſsartigerem",
    "ssartigeren": "ſsartigeren",
    "ssartigerer": "ſsartigerer",
    "ssartigeres": "ſsartigeres",
    "ssartiger": "ſsartiger",
    "ssartiges": "ſsartiges",
    "ssartige": "ſsartige",
    "ssartig": "ſsartig",
    
    "sartigerem": "sartigerem",
    "sartigeren": "sartigeren",
    "sartigerer": "sartigerer",
    "sartigeres": "sartigeres",
    "sartiger": "sartiger",
    "sartiges": "sartiges",
    "sartige": "sartige",
    "sartig": "sartig",

    # -äugig
    "säugigem": "säugigem",
    "säugigen": "säugigen",
    "säugiger": "säugiger",
    "säugiges": "säugiges",
    "säugige": "säugige",
    "säugig": "säugig",

    # -e
    "sserem": "ſſerem",
    "sseren": "ſſeren",
    "sserers": "ſſerers",
    "sserer": "ſſerer",
    "sseres": "ſſeres",
    "ssere": "ſſere",
    "ssers": "ſſers",
    "sser": "ſſer",
    "ssems": "ſſems",
    "ssens": "ſſens",
    "ssem": "ſſem",
    "ssen": "ſſen",
    "sse": "ſſe",

    "serem": "ſerem",
    "seren": "ſeren",
    "serers": "ſerers",
    "serer": "ſerer",
    "seres": "ſeres",
    "sere": "ſere",
    "sers": "ſers",
    "ser": "ſer",
    "sems": "ſems",
    "sens": "ſens",
    "sem": "ſem",
    "sen": "ſen",
    "se": "ſe" ,

    # -ei
    "sei": "sei",

    # -el
    "sselers": "ſſelers",
    "sseler": "ſſeler",
    "ssele": "ſſele",
    "sseln": "ſſeln",
    "ssels": "ſſels",
    "sselt": "ſſelt",
    "ssel": "ſſel",

    "seler": "ſeler",
    "sele": "ſele",
    "seln": "ſeln",
    "sels": "ſels",
    "selt": "ſelt",
    "sel": "ſel",

    # -elchen
    "sselchens": "ſſelchens",
    "sselchen": "ſſelchen",
    "selchens": "ſelchens",
    "selchen": "ſelchen",

    # -ell
    "ssells": "ſſells",
    "ssell": "ſſell",
    "sells": "ſells",
    "sell": "ſell",

    # -eln
    
}

_dict_processed = False

UNKNOWN_S = "╳"

def _process_dict():
    global _REPLACEMENTS, _END_REPLACEMENTS, _dict_processed
    if _dict_processed:
        return
    _REPLACEMENTS = {
        key.replace("s", UNKNOWN_S): value
        for key, value in _REPLACEMENTS.items()
    }
    _END_REPLACEMENTS = {
        key.replace("s", UNKNOWN_S): value
        for key, value in _END_REPLACEMENTS.items()
    }

def german_conversion(text):
    _process_dict()
    SHORT_S_ALWAYS_BEFORE_Z = False # False after 1901.
    
    clean_text = text.lower().replace("s", UNKNOWN_S)
    
    # applies simple start patterns.
    if clean_text[0] == UNKNOWN_S:
        clean_text = "ſ" + clean_text[1:]

    # any unknown S that comes before many consonants will be a short S.
    if SHORT_S_ALWAYS_BEFORE_Z:
        pattern = f"{UNKNOWN_S}(?=[aäceioöp{UNKNOWN_S}tuüyAÄCEIOÖPTUÜY])"
    else:
        pattern = f"{UNKNOWN_S}(?=[aäceioöp{UNKNOWN_S}tuüyzAÄCEIOÖPTUÜYZ])"

    uncertain_indices = [m.start() for m in re.finditer(pattern, clean_text)]
    short_s_indices = [
        i for i, char in enumerate(clean_text)
        if char == UNKNOWN_S and i not in uncertain_indices
    ]
    for i in short_s_indices:
        clean_text = clean_text[:i] + "s" + clean_text[i + 1: ]


    for key, replacement in _REPLACEMENTS.items():
        if UNKNOWN_S not in clean_text:
            break
        clean_text = smart_replace(clean_text, key, replacement)

    # applies end spelling patterns.
    if clean_text[-1] in [UNKNOWN_S, "ſ"]:
        clean_text = clean_text[:-1] + "s"

    #if clean_text.endswith(f"{UNKNOWN_S}ch"):
    #    clean_text = clean_text[:-3] + "ſch"
    if clean_text[:-1].endswith(f"{UNKNOWN_S}ch"):
        clean_text = clean_text[:-4] + "ſch" + clean_text[-1]
    elif clean_text[:-1].endswith(f"{UNKNOWN_S}{UNKNOWN_S}"):
        clean_text = clean_text[:-3] + "ſſ" + clean_text[-1]

    for key, replacement in _END_REPLACEMENTS.items():
        clean_text = smart_replace(
            clean_text, key, replacement, restrict_to_end=True
        )

    return clean_text

def smart_replace(text, search_term, replacement, restrict_to_end=False):
    s_indices = [
        i for i, char
        in enumerate(replacement)
        if char in "sſ"
    ]
    if len(s_indices) == 0 or len(search_term) > len(text):
        return text

    old_snippet = ""
    if restrict_to_end and len(search_term) < len(text):
        old_snippet = text[:-len(search_term)]
        text = text[-len(search_term):]

    n_unknowns = len(s_indices)
    if n_unknowns <= 1:
        text = text.replace(search_term, replacement)
        return old_snippet + text

    combinations = itertools.product([True, False], repeat=n_unknowns)
    combinations = [c for c in combinations if any(c)]
    keys = []
    for combo in combinations:
        #print(combo)
        new_string = list(replacement)
        for i, make_unknown in zip(s_indices, combo):
            if make_unknown:
                new_string[i] = UNKNOWN_S
        keys.append("".join(new_string))
    
    for key in keys:
        text = text.replace(key, replacement)

    return old_snippet + text

