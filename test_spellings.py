# these are words from the supported languages
# that are sourced from historical materials,
# so they are used to verify that the conversion functions
# are working properly.
TEST_SPELLINGS = {
    # English
    "en": [
        "ſatisfation",
        "misfortune",
        "transfuſe",
        "transfix",
        "transfer",
        "ſucceſsful",
        "offset",
        "off-ſet",
        "huſband",  # no long S before mid 18th century.
        "Shaftſbury",  # no long S before mid 18th century.
        "ſkin",  # no long S before mid 18th century.
        "aſk",  # no long S before mid 18th century.
        "riſk",  # no long S before mid 18th century.
        "maſked",  # no long S before mid 18th century.
        "Croſs-ſtitch",
        "Croſs-ſtaff",
        "Croſsſtitch",
        "croſsſtaff",
        "ſong",
        "uſe",
        "preſs",
        "ſubſtitute",
        "croſs-piece",
        "croſs-examination",
        "Preſs-work",
        "bird's-neſt",
    ],
    # French
    "fr": [
        "ils",
        "s'il",
        "s'eſt",
        "ſatisfaction",
        "toutesfois",
        "presbyter",
        "déshabiller",
        "déshonnête",
        "ſans",
        "eſt",
        "ſubſtituer",
        "tres-bien",
    ],
    # German
    "de": [
        "Aaſe",
        "Abendeſſen",
        "abgeſchmackt",
        "abſcheulich",
        "abſchlägig",
        "abſchläglich",
        "Abſchluſs",
        "Abſinth",
        "abſolut",
        "abſolvieren",
        "abſorbieren",
        "Abſorption",
        "abſpenſtig",
        "abſtrakt",
        "abſträngen",
        "Abweſenheit",
        "Achſe",
        "Achſel",
        "Adhäſion",
        "Adreſſe",
        "Akkuſativ",
        "Akquiſition",
        "Akuſtik",
        "Akzeſſiſt",
        "Akziſe",
        "Alabaſter",
        "Alchimiſt",
        "algebraiſch",
        "allerſeite",
        "alltagstauglich",
        "Ameiſe",
        "Amethyſt",
        "Amneſtie",
        "amortiſieren",
        "Amtsgerichtsrat",
        "amüſant",
        "Amüſement",
        "amüſieren",
        "Anachronismus",
        "Analogie",
        "Analyſe",
        "analytiſch",
        "angeſichts",
        "angeſtachelt",
        "Angſt",
        "anheiſchig",
        "Anlaſs",
        "anſäſſig",
        "anſchaulich",
        "anſchirren",
        "anſchließend",
        "Anſiedlung",
        "Anſpruch",
        "anſtatt",
        "anſtändig",
        "anſträngen",
        "anſtrengen",
        "Anſtrengung",
        "antipathiſch",
        "Antitheſe",
        "Anwartſchaft",
        "Anweſenheit",
        "apathiſch",
        "Apfelſine",
        "apodiktiſch",
        "Apoſtel",
        "apoſtoliſch",
        "Apoſtroph",
        "Appoſition",
        "Aprikoſe",
        "Arabeske",
        "Arbeitsamt",
        "Ariſtokratie",
        "Arreſt",
        "Arſchkriecher",
        "arteſiſch",
        "Artiſchocke",
        "aſſimiliert",
        "Aſſiſtenzarzt",
        "Aſſocie",
        "Aſſonanz",
        "Aſt",
        "Aſthma",
        "aſthmatiſch",
        "Aſtronom",
        "Aſtronomie",
        "Aſyl",
        "Atheiſt",
        "Atlaſſe",
        "Atmoſphäre",
        "aufſäſſig",
        "Ausbeutung",
        "Ausdehnung",
        "ausfindig",
        "ausgiebig",
        "Auslaſſungszeichen",
        "ausländiſch",
        "ausmerzen",
        "ausnahmsweiſe",
        "ausnuzten",
        "auspacken",
        "ausrenken",
        "ausreuten",
        "ausroden",
        "ausrotten",
        "Ausſaat",
        "ausſäßig",
        "Ausſicht",
        "ausſpannen",
        "ausſpielen",
        "Ausſprache",
        "austrickſen",
        "auswärtig",
        "auswendig",
        "Auſpizien",
        "authentiſch",
        "Äbtiſſin",
        "ängſtlich",
        "Äſer",
        "Äſthetik",
        "äſthetiſch",
        "äußerſt",
        "äußerſte",
        "Bachſtelze",
        "Ballaſt",
        "Balſam",
        "Balſamine",
        "barfuß",
        "Barfüßer",
        "barſch",
        "Barſchaft",
        "barſt",
        "Baſar",
        "Baſen",
        "Baſilisk",
        "Baſis",
        "Baſſin",
        "Baſt",
        "Baſtard",
        "Baſtei",
        "Batiſt",
        "Bauſch",
        "Bauſtil",
        "Bänkelſänger",
        "Bäſſe",
        "Beefſteak",
        "befeſtigen",
        "befiehlſt",
        "begeiſtert",
        "beiſeite",
        "bemooſt",
        "berſten",
        "beſcheren",
        "beſchimpfen",
        "beſchränken",
        "beſchweren",
        "beſchwichtigen",
        "beſeelen",
        "beſeelt",
        "beſeligen",
        "beſeligt",
        "Beſing",
        "beſſer",
        "Beſtand",
        "beſtätigen",
        "beſte",
        "Beſteck",
        "beſten",
        "beſuchen",
        "Betriebsunfall",
        "beweiſen",
        "Bewuſſtſein",
        "beziehungsweiſe",
        "bibliſch",
        "Bimsſtein",
        "Binnenſee",
        "Binſe",
        "birſt",
        "bisher",
        "Bistum",
        "bisweilen",
        "Biſchof",
        "biſchöflich",
        "Biſs",
        "biſschen",
        "Biſſen",
        "Biſſes",
        "biſſig",
        "Bläſſe",
        "Bleſſe",
        "blutrünſtig",
        "Bombaſt",
        "bombaſtiſch",
        "boshaft",
        "Bosheit",
        "Boskett",
        "boſſeln",
        "boſſieren",
        "Botſchaft",
        "böslich",
        "Böſewicht",
        "Brackwaſſer",
        "brandſchaßen",
        "Bratroſt",
        "Bremſe",
        "bremſen",
        "Brenneſſel",
        "Breſche",
        "breſthaft",
        "Briefumſchlag",
        "Broſamen",
        "Broſche",
        "broſchieren",
        "Broſchüre",
        "Brunſt",
        "brünſtig",
        "brüsk",
        "brüskieren",
        "Buchsbaum",
        "bugſieren",
        "Bugſpriet",
        "burlesk",
        "Buſch",
        "Büchſe",
        "Bügeleiſen",
        "Bürgermeiſter",
        "Büſte",
        "Celliſt",
        "chaotiſch",
        "Charakteriſtik",
        "Chauſſee",
        "Chemiſette",
        "chevaleresk",
        "choleriſch",
        "Choriſt",
        "Chreſtomathie",
        "Chriſt",
        "Chriſtbeſcherung",
        "Chriſtentum",
        "chromatiſch",
        "Couſin",
        "Couſine",
        "Dachſe",
        "Damaſt",
        "Dambrettſpiel",
        "Dambrettſtein",
        "Darmſaite",
        "dasſelbe",
        "Deichſel",
        "Demonſtration",
        "Depeſche",
        "dergeſtalt",
        "desfalls",
        "desgleichen",
        "deshalb",
        "Desinfektion",
        "desſelben",
        "desungeachtet",
        "deswegen",
        "Deſpot",
        "deſſen",
        "Deſſert",
        "deutſch",
        "deutſche",
        "Deviſe",
        "Diakoniſſe",
        "Diakoniſſin",
        "Diebſtahl",
        "Dienstag",
        "Dienstages",
        "Dienstags",
        "Dienſt",
        "Dienſten",
        "diesjährig",
        "diesmal",
        "diesſeits",
        "dieſes",
        "Diözeſe",
        "Disharmonie",
        "disharmoniſch",
        "Diskant",
        "diskret",
        "Diskretion",
        "Diskuſſion",
        "diskutieren",
        "Dispens",
        "dispenſieren",
        "disponieren",
        "Dispoſition",
        "Disput",
        "disputieren",
        "Diſſident",
        "Diſſonanz",
        "Diſtanz",
        "Diſtichon",
        "diſtinguiert",
        "Diſtinktion",
        "Diſtrikt",
        "Diſziplin",
        "Diviſor",
        "dogmatiſch",
        "Donnerstag",
        "Donnerstages",
        "Donnerstags",
        "Dorfſchulze",
        "Dornröschen",
        "Doſe",
        "Doſen",
        "Doſis",
        "dramatiſch",
        "Drangſal",
        "drechſeln",
        "Drechſler",
        "dreiſt",
        "Dreiſtigkeit",
        "Dresden",
        "Dreſchflegel",
        "dreſſieren",
        "Dreſſur",
        "Drogiſt",
        "Droſchke",
        "druckſen",
        "Drüſe",
        "Duckmäuſer",
        "Duſchbad",
        "Duſche",
        "duſchen",
        "duſcheſt",
        "Dynaſtie",
        "eheſten",
        "eheſtens",
        "Ehrenſalve",
        "Eigenſchaftswörtern",
        "einäſchern",
        "einesteils",
        "eingeſpenſter",
        "Einſchiebſel",
        "Einſiedler",
        "Einſpänner",
        "einſpielen",
        "Einſtellung",
        "einſt",
        "Ekſtaſe",
        "Elaſtizität",
        "Ellipſe",
        "Elſäſſer",
        "Elyſium",
        "empfiehlſt",
        "Emphaſe",
        "emphatiſch",
        "empiriſch",
        "emſig",
        "Enthuſiasmus",
        "entſeßlich",
        "Epilepſie",
        "epileptiſch",
        "Epiſkopat",
        "Epiſode",
        "Epiſtel",
        "erboſen",
        "erboſt",
        "Erbsſtroh",
        "Erbſe",
        "Erbſenſtroh",
        "erforſchen",
        "erkieſen",
        "erkieſt",
        "erkieſte",
        "Erlaſſe",
        "erſchlaffſt",
        "erſchrak",
        "erſchrecken",
        "erſchrocken",
        "erſprießlich",
        "erſt",
        "erſtaunen",
        "erſte",
        "erſtemal",
        "erweilen",
        "erweiſen",
        "Eschatologie",
        "Eskadron",
        "Eskorte",
        "Eſche",
        "Eſpe",
        "Eſpenlaub",
        "eſſen",
        "Eſſenz",
        "Eſſig",
        "Eſtrich",
        "Euphemismus",
        "exotiſch",
        "exzentriſch",
        "fahrläſſig",
        "Faſan",
        "Faſanerie",
        "Faſchine",
        "Faſelei",
        "faſelig",
        "faſeln",
        "Faſs",
        "Faſſade",
        "faſſen",
        "faſſeſt",
        "Faſſon",
        "faſſungslos",
        "Faſſung",
        "faſten",
        "Faſtnacht",
        "Faſttag",
        "faſzinierend",
        "Fauſt",
        "fällſt",
        "Fäſſer",
        "Fäuſtel",
        "feiſt",
        "Feldſpat",
        "Feſte",
        "Feſtung",
        "Fiasko",
        "fichtſt",
        "Finſternis",
        "firniſſen",
        "firniſſeſt",
        "Firſt",
        "fiskaliſch",
        "Fiskus",
        "Fiſchgräte",
        "Fiſchreuſe",
        "Fiſchrogen",
        "Fitneſsſtudios",
        "Flaſh",
        "Flauſch",
        "Flechſe",
        "Flitterſtaat",
        "Floskel",
        "Floſſe",
        "Fluſsſchifffahrt",
        "Flüſſe",
        "flüſſig",
        "flüſtern",
        "Foſſil",
        "Foſſilien",
        "Förſter",
        "fragſt",
        "Franſe",
        "Freiheitskrieg",
        "Freiſchärler",
        "Fresken",
        "Fresko",
        "freſh",
        "freſſen",
        "Freundeskreis",
        "Frieſeln",
        "Frikaſſee",
        "friſchweg",
        "Friſeur",
        "friſieren",
        "friſſt",
        "Friſt",
        "Friſur",
        "Frondienſt",
        "Fronfeſte",
        "früheſtens",
        "Frühſtück",
        "Fußtapſe",
        "Fürſt",
        "Fürſtentum",
        "Füſilier",
        "Galoſche",
        "galvaniſch",
        "Gamaſche",
        "Gardiſt",
        "Garniſon",
        "garſtig",
        "Gaſe",
        "Gaſſe",
        "Gaſtmahl",
        "Gaſtſtätte",
        "Gaſtwirt",
        "Gänſe",
        "Gänſerich",
        "Gebiſs",
        "gebiſſen",
        "geborſten",
        "Gebreſten",
        "gediehſt",
        "Geeſt",
        "gefliſſentlich",
        "Geflüſter",
        "Gegelſtange",
        "gegoſſen",
        "gehäſſig",
        "Geiſel",
        "geiſtreich",
        "Gemsbock",
        "Gemſe",
        "Gemüſe",
        "Genoſſe",
        "genoſſen",
        "Genüſſe",
        "geringſten",
        "geriſſen",
        "geſamt",
        "Geſamtheit",
        "geſandt",
        "Geſandter",
        "Geſandtſchaft",
        "geſchah",
        "Geſchäft",
        "geſchehen",
        "geſcheit",
        "Geſcheuk",
        "Geſchichte",
        "geſchieht",
        "Geſchmeide",
        "Geſchmeiß",
        "geſchmelzt",
        "geſchmolzen",
        "Geſchwader",
        "Geſchichte",
        "geſchiet",
        "geſchwind",
        "Geſchwulſt",
        "Geſchwür",
        "geſeſſen",
        "Geſichtsausdruck",
        "Geſims",
        "Geſinde",
        "Geſindel",
        "geſotten",
        "Geſpan",
        "Geſpann",
        "Geſpenſt",
        "Geſpinſt",
        "geſpreizt",
        "geſprenkelt",
        "Geſtade",
        "Geſtalt",
        "Geſtändnis",
        "Geſtänge",
        "Geſte",
        "Geſten",
        "geſtern",
        "geſtikulieren",
        "Geſtöber",
        "Geſtöhne",
        "geſtrig",
        "Geſtrüpp",
        "Gewahrſam",
        "Gewährsmann",
        "gewerbsmäßig",
        "gibſt",
        "Gleichniſſe",
        "gleichſchenklig",
        "Gleisner",
        "gleisneriſch",
        "Gletſcher",
        "Globuſſe",
        "gotiſch",
        "Grabſcheit",
        "graſig",
        "graſſieren",
        "grauſen",
        "grauſig",
        "gräſslich",
        "grätſchen",
        "Greiſin",
        "Griesgram",
        "griesgrämig",
        "Grimaſſe",
        "grotesk",
        "gruſeln",
        "Gſtaad",
        "Guckkaſten",
        "Gunſt",
        "Gunſten",
        "Guſtav",
        "Güſſe",
        "Gymnaſium",
        "Gymnaſtik",
        "Haifiſch",
        "Halbſcheid",
        "halsſtarrig",
        "Hamſter",
        "Harniſch",
        "Haſardſpiel",
        "Haſe",
        "Haſpe",
        "haſpeln",
        "haſſen",
        "haſſeſt",
        "haſſt",
        "haſt",
        "haſtig",
        "Hausaufgaben",
        "Hausflur",
        "Hausgerät",
        "haushalten",
        "Hausrat",
        "Haustor",
        "Haustür",
        "Hauſe",
        "hauſieren",
        "hältſt",
        "hämiſch",
        "Häschen",
        "Häuslein",
        "häuslich",
        "Häuſer",
        "Hechſe",
        "Heerſtraße",
        "Hemiſphäre",
        "Herbſt",
        "Herrſchaft",
        "Heuſchober",
        "hinausſichtlich",
        "Hinſicht",
        "hinſichtlich",
        "hinſiechen",
        "Hirſe",
        "hiſſen",
        "hiſſeſt",
        "hiſſt",
        "Hiſtorie",
        "hiſtoriſch",
        "holdſelig",
        "Horniſſe",
        "Horoſkop",
        "Hoſpital",
        "Hoſpiz",
        "höchſte",
        "höchſtens",
        "höhlenforſchen",
        "Huſar",
        "hübſch",
        "Hülſe",
        "Hypotenuſe",
        "Hypotheſe",
        "Idealismus",
        "identiſch",
        "Illuſtration",
        "Iltiſſe",
        "imſtande",
        "inbrünſtig",
        "indeſſen",
        "Induſtrie",
        "induſtriell",
        "inkonſequent",
        "Inkonſequenz",
        "Inquiſition",
        "insbeſondere",
        "insgeheim",
        "insgeſamt",
        "Inſaſſe",
        "Inſekt",
        "inſofern",
        "inſonderheit",
        "inſoweit",
        "Inſpekteur",
        "Inſpektor",
        "inſpizieren",
        "inſtand",
        "Inſtanz",
        "Inſtinkt",
        "Inſtitut",
        "Inſtruktion",
        "Inſtrument",
        "intereſſant",
        "Intereſſe",
        "Iſlam",
        "iſolieren",
        "Iſraelit",
        "iſſeſt",
        "Iſthmus",
        "italieniſch",
        "jammerſchade",
        "jenſeits",
        "Juſtiz",
        "jüngſt",
        "Kaiſer",
        "Kaleſche",
        "Kamiſol",
        "kanoniſch",
        "Kantſchu",
        "Kardätſche",
        "Karmeſin",
        "Karoſſe",
        "Kartauſe",
        "Kartätſche",
        "Kartäuſer",
        "Karuſſell",
        "Kaskade",
        "Kaſematte",
        "Kaſerue",
        "Kaſimir",
        "Kaſino",
        "Kaſpar",
        "Kaſſe",
        "Kaſſerolle",
        "Kaſſette",
        "Kaſſierer",
        "Kaſtagnette",
        "Kaſtanie",
        "Kaſte",
        "kaſteien",
        "Kaſtell",
        "Kaſtellan",
        "Kaſus",
        "katarrhaliſch",
        "Kataſter",
        "Kataſtrophe",
        "Katechismus",
        "kategoriſch",
        "katholiſch",
        "Katholizismus",
        "kauderwelſch",
        "Kauffahrteiſchiff",
        "Kautſchuk",
        "Kavalleriſt",
        "Keuchhuſten",
        "keuſch",
        "kieſen",
        "Kiosk",
        "Kirmeſſe",
        "Kiſſen",
        "Kiſtchen",
        "Kiſte",
        "Klaſſe",
        "klaſſifizieren",
        "Klaſſiker",
        "klaſſiſch",
        "Klausner",
        "Klauſe",
        "Klauſel",
        "kleidſam",
        "kleinſte",
        "Kleriſei",
        "klimatiſch",
        "kliniſch",
        "Kliſtier",
        "Kloſter",
        "knichſen",
        "knirſchen",
        "knirſcheſt",
        "Knoſpe",
        "Knöſpchen",
        "knuſpern",
        "Knüttelverſe",
        "Kokosnuſs",
        "Kolliſion",
        "Koloniſt",
        "koloſſal",
        "komiſch",
        "Kommiſſar",
        "Kommiſſion",
        "Kompreſſe",
        "Konfeſſion",
        "konfiszieren",
        "Konfuſion",
        "koniſch",
        "Konſens",
        "konſequent",
        "Konſequenz",
        "Konſerve",
        "Konſiſtorium",
        "Konſole",
        "Konſonant",
        "Konſorte",
        "Konſtitution",
        "Konſtruktion",
        "Konſul",
        "Konſum",
        "Kontraſt",
        "Konverſation",
        "konzentriſch",
        "Konzeſſion",
        "Kopfkiſſen",
        "Korreſpondenz",
        "korreſpondieren",
        "Korſett",
        "kosmiſch",
        "Kosmopolit",
        "kosmopolitiſch",
        "Kosmos",
        "Koſſat",
        "Koſſäte",
        "Koſtüm",
        "Kramtsvogel",
        "kreiſchen",
        "kreiſcheſt",
        "kreiſchſt",
        "Kreiſel",
        "kreiſen",
        "Kreſſe",
        "Kriminaliſt",
        "Kriſe",
        "Kriſis",
        "Kriſtall",
        "kritiſch",
        "Krupphuſten",
        "Kruſte",
        "kubiſch",
        "Kuliſſe",
        "Kundſchaft",
        "Kunſt",
        "Kunſtſtück",
        "Kurfürſt",
        "Kurrentſchrift",
        "Kurſe",
        "Kurſus",
        "Kuſtos",
        "Kutſche",
        "Künſtler",
        "Künſtlerbund",
        "Küraſſier",
        "Kürbiſſe",
        "Kürſchner",
        "küſſen",
        "küſſeſt",
        "küſſt",
        "Küſte",
        "Küſter",
        "Labſal",
        "Lachſe",
        "Landsknecht",
        "laſſen",
        "laſſ'",
        "Laſt",
        "Laſten",
        "lädſt",
        "längſt",
        "längſten",
        "läppiſch",
        "läſſeſt",
        "läſſig",
        "läſſt",
        "läſtig",
        "lebenslang",
        "Leibesleben",
        "lesbiſch",
        "leſen",
        "leutſelig",
        "Lichtmeſſe",
        "lieſt",
        "Linſe",
        "liſpeln",
        "literariſch",
        "logiſch",
        "loſen",
        "Loſung",
        "Lotſe",
        "löslich",
        "löſchen",
        "löſcheſt",
        "löſcht",
        "löſen",
        "Luiſe",
        "Luſt",
        "Lünſe",
        "lüſtern",
        "lyriſch",
        "Magiſtrat",
        "Maiſche",
        "maiſchen",
        "maiſcheſt",
        "maiſchſt",
        "Malſtein",
        "Manſchette",
        "Manuſkript",
        "Markiſe",
        "Marquiſe",
        "Marſch",
        "Marſchall",
        "marſchieren",
        "Marſchroute",
        "martialiſch",
        "Maske",
        "Maskerade",
        "Maskulinum",
        "Maſchine",
        "Maſern",
        "Maſſage",
        "Maſſe",
        "maſſieren",
        "maſſiv",
        "Maſt",
        "Maſtbaum",
        "Matroſe",
        "Mauſe",
        "mauſern",
        "Mäuschen",
        "Mäuſe",
        "mechaniſch",
        "Meeresküſte",
        "meinerſeits",
        "meinesteils",
        "Meiſe",
        "meiſt",
        "meiſte",
        "meiſten",
        "meiſtens",
        "Menſchenraſſe",
        "Menſchen",
        "Mesner",
        "Meſſergebnis",
        "Meſſe",
        "Meſſegehörig",
        "meſſen",
        "Meſſung",
        "Meſtize",
        "Metamorphoſe",
        "metaphoriſch",
        "Metaphyſik",
        "Mettwurſt",
        "Mikroſkop",
        "militäriſch",
        "mindeſen",
        "mindeſte",
        "mindeſtens",
        "Miniſter",
        "Miſanthrop",
        "miſchen",
        "miſcheſt",
        "miſchſt",
        "Miſpel",
        "miſsbrauchen",
        "miſshandeln",
        "miſſen",
        "miſſeſt",
        "Miſſetat",
        "Miſſetäter",
        "Miſſion",
        "Miſſionar",
        "Miſſionär",
        "miſſt",
        "Miſzelle",
        "Mittfaſten",
        "mondſüchtig",
        "Mooſe",
        "Moraſt",
        "morſch",
        "Moſaik",
        "Moſchee",
        "Moſt",
        "Moſtrich",
        "möglicherweiſe",
        "Möpſe",
        "Muskat",
        "Muskel",
        "Muskete",
        "Musketier",
        "muskulös",
        "Muſe",
        "Muſelmanen",
        "Muſelmänner",
        "Muſeum",
        "Muſikant",
        "muſizieren",
        "Muſſelin",
        "muſſt",
        "muſſteſt",
        "Münſter",
        "müſſen",
        "myſteriös",
        "Myſtik",
        "Nachläſſigkeit",
        "nachſichtig",
        "nachweisbar",
        "nagelfeſt",
        "Narziſſe",
        "Nashorn",
        "naſchen",
        "naſcheſt",
        "naſchſt",
        "naſeweis",
        "naſe",
        "närriſch",
        "närriſchſte",
        "Näſſe",
        "Neceſſaire",
        "Nieswurz",
        "nieſen",
        "Niſche",
        "Notenſyſtem",
        "notwendigerweiſe",
        "Nuſs",
        "Nuſsſchokolade",
        "Nüſſe",
        "Nüſter",
        "Oaſe",
        "Obelisk",
        "Oberſten",
        "obligatoriſch",
        "obſkur",
        "Obſt",
        "ohmweiſe",
        "Omnibuſſe",
        "optiſch",
        "Orcheſter",
        "Ordnungsliebe",
        "Organiſt",
        "Oskar",
        "Oslo",
        "Osnabrück",
        "Oswald",
        "Oſzillograph",
        "Öſe",
        "Palaſt",
        "Paliſade",
        "Pallaſch",
        "Pantheismus",
        "Papſt",
        "Parentheſe",
        "Parſüm",
        "parteiiſch",
        "Pasquill",
        "Paſs",
        "Paſſage",
        "Paſſagier",
        "Paſſion",
        "Paſſiv",
        "paſſte",
        "Paſtell",
        "Paſtete",
        "Paſtor",
        "Paſtoren",
        "pathetiſch",
        "patriotiſch",
        "Pausbacken",
        "Pauspapier",
        "Pauſchquantum",
        "pauſen",
        "päpſtlich",
        "Päſſe",
        "pedantiſch",
        "Penſa",
        "Penſen",
        "Penſion",
        "Penſionär",
        "penſionieren",
        "Penſum",
        "Perſiflage",
        "Perſon",
        "perſönlich",
        "Perſpektive",
        "Peſtilenz",
        "Peterſilie",
        "Petſchaft",
        "Pfingſten",
        "Pfirſich",
        "Pflaſter",
        "Pflugſchar",
        "Pfoſten",
        "pfuſchen",
        "pfuſcheſt",
        "pfuſchſt",
        "Phantaſie",
        "Phantaſt",
        "Phariſäer",
        "Philiſter",
        "Philoſoph",
        "phlegmatiſch",
        "Phosphor",
        "Phyſik",
        "phyſiſch",
        "Piedeſtal",
        "Pilſener",
        "Pilſner",
        "pirſchen",
        "pirſcheſt",
        "pirſchſt",
        "Piſtole",
        "Plaſtik",
        "plaſtiſch",
        "Plätteiſen",
        "Plusquamperfekt",
        "Poeſie",
        "poetiſch",
        "politiſch",
        "Poliziſt",
        "Poſamentier",
        "poſitiv",
        "Poſſe",
        "Poſſen",
        "poſſierlich",
        "Poſtillion",
        "poſtnumerando",
        "Pottaſche",
        "Pottfiſch",
        "Pökelfleiſch",
        "praktiſch",
        "praſſen",
        "Praſſer",
        "praſſeſt",
        "praſſt",
        "Prägſtock",
        "Präpoſition",
        "Präſens",
        "präſentieren",
        "Präſenzliſte",
        "Präſident",
        "Präziſion",
        "preisgeben",
        "preislich",
        "Preiſelbeere",
        "preiſen",
        "Presbyter",
        "Preſſe",
        "preſſen",
        "preſſeſt",
        "preſſt",
        "Prieſter",
        "Prinzeſſin",
        "Prisma",
        "Prismen",
        "Priſe",
        "Pritſche",
        "problematiſch",
        "Profeſſor",
        "propädeutiſch",
        "Propſt",
        "Proſa",
        "proſaiſch",
        "Proſelyt",
        "proſkribieren",
        "Proſkription",
        "Proſodie",
        "proſodiſch",
        "Proſpekt",
        "Proteſt",
        "Proteſtant",
        "Prozeſſion",
        "Pröpſte",
        "Prunkſucht",
        "Prüfungsordnung",
        "Pſalm",
        "Pſalmen",
        "pſeudonym",
        "Pſyche",
        "Pſychologie",
        "Pulsſchlag",
        "Pulſe",
        "pulveriſieren",
        "Punſch",
        "Pyraſe",
        "Quackſalber",
        "Quaſte",
        "Quäſtor",
        "Quäſtur",
        "Quechſilber",
        "quetſchen",
        "quetſcheſt",
        "quetſchſt",
        "quietſchen",
        "quietſcheſt",
        "quietſchſt",
        "rachſüchtig",
        "Radieschen",
        "Randgloſſe",
        "raſen",
        "Raſenſtüber",
        "raſieren",
        "Raſſe",
        "raſten",
        "Raſttag",
        "Raſur",
        "ratenweiſe",
        "ratſam",
        "rauskriegen",
        "Rädelsführer",
        "räſonieren",
        "Rätſel",
        "rätſt",
        "räuſpern",
        "Realismus",
        "Redensart",
        "redſelig",
        "Regiſter",
        "Regiſtrator",
        "regueriſch",
        "Reichsſtadt",
        "Reisbrei",
        "Reislauf",
        "Reiſer",
        "Reiſig",
        "Reiſigen",
        "reiſt",
        "reiſte",
        "rekognoſzieren",
        "Rekonvaleſzent",
        "Remiſe",
        "Repreſſalien",
        "Requiſiten",
        "Reſcher",
        "Reſerve",
        "Reſidenz",
        "Reſkript",
        "Reſonanz",
        "Reſpekt",
        "Reſpiration",
        "Reſſort",
        "Reſſoruce",
        "Reſt",
        "Reſtaurant",
        "Reſultat",
        "Retuſche",
        "retuſchieren",
        "Reuſe",
        "Reviſion",
        "Reviſor",
        "Rezenſent",
        "Rhapſode",
        "Rhapſodie",
        "rhetoriſch",
        "Rheumatismus",
        "rhythmiſch",
        "Rienſpan",
        "Riesling",
        "Rieſe",
        "Rieſel",
        "Rieſin",
        "Rieſter",
        "ringsum",
        "Rinnſal",
        "riskieren",
        "Riſiko",
        "Riſpe",
        "Riſs",
        "Riſſe",
        "Roaſtbeef",
        "romantiſch",
        "Rosmarin",
        "Roſe",
        "Roſine",
        "Roſs",
        "Roſſe",
        "Roſt",
        "roſten",
        "Royaliſt",
        "Röschen",
        "Röslein",
        "röſten",
        "Runenſchrift",
        "Rückkunſt",
        "Rückſicht",
        "Rüſſel",
        "Rüſte",
        "Rüſter",
        "Sakriſtei",
        "Samstag",
        "Samstages",
        "Samstags",
        "Schellfiſch",
        "Scheuſal",
        "Schiedsrichter",
        "Schiffstau",
        "Schirrmeiſter",
        "Schisma",
        "Schleswig",
        "Schlotſeger",
        "Scluſs",
        "Schlüſſel",
        "Schneiſe",
        "Schöſſe",
        "Schwulſt",
        "Sechſtel",
        "Selbſtbewuſſtſein",
        "Semeſter",
        "Seſſel",
        "Seſſion",
        "Sippſchaft",
        "Sophiſt",
        "Speſen",
        "Sproſſe",
        "Staubbeſen",
        "Staupbeſen",
        "Steinſchleuder",
        "Stemmeiſen",
        "Stereoſkop",
        "Subſkription",
        "Subſtantiv",
        "Subſtanz",
        "Suspenſion",
        "Syſtem",
        "ſanguiniſch",
        "ſaſten",
        "ſataniſch",
        "ſatiriſch",
        "ſattſam",
        "ſaumſelig",
        "ſauſen",
        "ſcheelſüchtig",
        "ſchematiſch",
        "ſchilteſt",
        "ſchlüſſig",
        "ſchmauſen",
        "ſchmiegſam",
        "ſchnippiſch",
        "ſchwülſtig",
        "ſechspfündig",
        "ſechsſtern",
        "ſechſte",
        "ſehnſüchtig",
        "ſelbſtändig",
        "ſelbſtverſtändlich",
        "ſeltſam",
        "ſiehſt",
        "ſittſam",
        "ſkanadlös",
        "ſkeptiſch",
        "ſpäteſtens",
        "ſpezifiſch",
        "ſtätiſch",
        "ſtiehlſt",
        "ſtiliſtiſch",
        "ſtillſchweigend",
        "ſtoßweiſe",
        "ſtörriſch",
        "ſubſkribieren",
        "ſuspendieren",
        "ſüdländiſchen",
        "ſymptomatiſch",
        "ſyntaktiſch",
        "ſyſtematiſch",
        "Talisman",
        "taubſtumm",
        "tauſchen",
        "tauſcheſt",
        "tauſchſt",
        "tauſend",
        "Tauſende",
        "Tauſendſtel",
        "täuſchen",
        "täuſcheſt",
        "täuſchſt",
        "techniſch",
        "Teerſchwelerei",
        "Teleſkop",
        "Terraſſe",
        "theatraliſch",
        "theoretiſch",
        "Thereſe",
        "Theſe",
        "Thunfiſch",
        "tieriſch",
        "Toaſt",
        "toaſten",
        "Todesangſt",
        "Todſünde",
        "Tolpatſch",
        "Torfſtich",
        "Totſchlag",
        "totſchlagen",
        "totſtill",
        "Touriſt",
        "Trainſoldat",
        "Transparent",
        "Transporteuer",
        "transportieren",
        "tranſitiv",
        "tranſpirieren",
        "tranſzendent",
        "tranſzendieren",
        "Treidelſteig",
        "Trenſe",
        "Treſpe",
        "Treſſe",
        "triffſt",
        "trittſt",
        "tropiſch",
        "Truchſeß",
        "Trübſal",
        "trübſelig",
        "Tſchako",
        "Tuffſtein",
        "Tuſche",
        "tuſchen",
        "tuſcheſt",
        "tuſchſt",
        "tückiſch",
        "typiſch",
        "tyranniſch",
        "ungeſchlacht",
        "ungeſtaltet",
        "ungeſtüm",
        "Ungunſt",
        "Univerſität",
        "Univerſum",
        "unparteiiſch",
        "unratſam",
        "unſäglich",
        "unſelig",
        "unſre",
        "unſtet",
        "unterdeſſen",
        "Unterſuchungsergebnis",
        "Unterſtützung",
        "unverſehens",
        "unverſehrt",
        "unwiderſtehlich",
        "unwirſch",
        "unwiſſentlich",
        "Utenſilien",
        "überdrüſſig",
        "Überfluſs",
        "überflüſſig",
        "überſchüſſig",
        "überſchwenglich",
        "Vaſall",
        "Vaſe",
        "väterlicherſeits",
        "verdroſſen",
        "verharſchen",
        "verharſcheſt",
        "verharſchſt",
        "verkaufsfördernd",
        "verklauſulieren",
        "verroſtet",
        "Verſand",
        "verſanden",
        "verſandet",
        "Verſchleiß",
        "Verſchmeltzung",
        "verſchmiſſt",
        "verſchoben",
        "verſchoſſenes",
        "verſchränken",
        "verſchwenden",
        "verſchwöreriſchen",
        "verſehren",
        "verſenden",
        "verſengt",
        "verſenkt",
        "verſetzen",
        "verſeuchen",
        "verſeuchſt",
        "Verſicherungsgeſellſchaft",
        "Verſicherungsſchein",
        "verſiegen",
        "Verſöhnung",
        "verſöhnen",
        "verſprechen",
        "Verſtändnis",
        "verwahrloſen",
        "verwahrloſt",
        "verwaiſen",
        "verwaiſt",
        "Verwandtſchaft",
        "verweiſen",
        "verweslich",
        "verweſen",
        "Veſper",
        "Veſtibül",
        "vierſchrötig",
        "Viſier",
        "Viſite",
        "vonſtatten",
        "vorſäßlich",
        "Vorſchuſs",
        "vorſtehenden",
        "vorſtehendes",
        "Wachstum",
        "wachſen",
        "Wachtmeiſter",
        "wahnſchaffen",
        "Wahnſinn",
        "Wahrſpruch",
        "Waiſe",
        "Waiſenhaus",
        "Walfiſch",
        "Walnuſs",
        "Wanſt",
        "waſchen",
        "Waſſer",
        "watſcheln",
        "wächſern",
        "wächſeſt",
        "wächſt",
        "wähleriſch",
        "wäſcheſt",
        "wäſchſt",
        "wäſſerig",
        "wechſeln",
        "Wechſler",
        "Wegweiſer",
        "Weisheit",
        "weislich",
        "weismachen",
        "weisſagen",
        "Weisſager",
        "Weiſe",
        "weiſe",
        "weiſen",
        "Welſchland",
        "Weltherrſchaft",
        "wenigſten",
        "Werkſtatt",
        "Werkſtätte",
        "weshalb",
        "weſentlich",
        "weſentlichen",
        "Weſir",
        "Weſpe",
        "weſſen",
        "Weſt",
        "Weſtfalen",
        "Whiſt",
        "Wichſe",
        "Widerſacher",
        "Widerſchein",
        "widerſpenſtig",
        "Wirrſal",
        "Wirſing",
        "wirſt",
        "Wirtshaus",
        "Wirtsſtube",
        "Wirtſchaftsmächte",
        "Wirtſchaft",
        "Wismut",
        "Wiſpel",
        "wiſſen",
        "wiſſentlich",
        "wohlweislich",
        "Wolluſt",
        "wollüſtig",
        "Wunſch",
        "wünſchen",
        "wüſt",
        "Wüſte",
        "Wüſtenei",
        "Wüßtling",
        "Zahlſchein",
        "zauſen",
        "Zeichenſtunde",
        "Zeiſig",
        "Zeitgeſchichte",
        "zeitweiſe",
        "Zenſur",
        "zerſtücken",
        "Zervelatwurſt",
        "Zetergeſchrei",
        "Zeugniſſe",
        "Zinſen",
        "ziſelieren",
        "Ziſterne",
        "Zuchthäusler",
        "zuläſſig",
        "zurechtſtellen",
        "zurechweiſen",
        "zuſammenrotten",
        "Zuſammenſetzungen",
        "zuſätzlich",
        "zuſchulden",
        "zuſehends",
        "zuſtand",
        "zuſtande",
        "zuſtatten",
        "Zuverſicht",
        "zweifelsohne",
        "zweiſpännig",
        "zweitauſend",
        "Zwerchſack",
        "Zwetſche",
        "Zwieſpalt",
        "Zwiſt",
        "zwiſtig",
        "zwitſchern",
        "Zypreſſe",
    ],
    
    # Spanish
    # [ ] force short S before accented O
    "es": [
        "illuſtriſsimos",
        "confeſſores",
        "sí",
        "sì",
        "sé",
        "sè",
        "Apoſtasìa",
        "Apoſtasía",
        "abrasò",
        "paſsò",
        "ſi",
        "ſe",
        "paſſo",
        "transformandoſe",
        "transfigura",
        "ſatisfaccion",
        "presbytero",
        "deshoneſtos",
        "deshoneſtidad",
        "illuſtriſsimo",
        "paſsion",
        "confeſsion",
        "poſsible",
        "exceſſo",
        "comiſſario",
        "neceſſaria",
        "paſſa",
        "tranſ-formados",
        "copioſiſ-ſimo",
    ],
    # Italian
    "it": [
        "s’informaſſero",
        "fuſs’egli",
        "paſsò",
        "ricusò",
        "sù",
        "sì",
        "così",
        "paſſo",
        "ſi",
        "ſoddisfare",
        "ſoddisfazione",
        "trasfigurazione",
        "sfogo",
        "sfarzo",
        "sbaglio",
        "sbagliato",
        "reſtaſ-ſero",
        # sometimes ſſi was forced to ſsi historically (but not here).
        "compreſſioni",
        "proſſima",
    ],
}