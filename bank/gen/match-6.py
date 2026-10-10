# Bank session 10 Oct 2026 (fifth pass): 2 more Match questions for 14 topics that had 5 live.
# Writes bank/topics/<slug>__m6.json; import each with FILE=<slug>__m6 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})


m("uk-geography", "medium", "Match each bridge to the water it crosses",
  ("Humber Bridge", "The Humber Estuary"), ("Clifton Suspension Bridge", "The River Avon"), ("Forth Bridge", "The Firth of Forth"), ("Menai Suspension Bridge", "The Menai Strait"))
m("uk-geography", "medium", "Match each lake or loch to its part of the UK",
  ("Lough Neagh", "Northern Ireland"), ("Loch Lomond", "Scotland"), ("Windermere", "England"), ("Llyn Tegid (Bala Lake)", "Wales"))

m("world-geography", "medium", "Match each waterfall to its country",
  ("Angel Falls", "Venezuela"), ("Victoria Falls", "Zambia and Zimbabwe"), ("Iguazu Falls", "Argentina and Brazil"), ("Gullfoss", "Iceland"))
m("world-geography", "hard", "Match each strait to what it separates",
  ("Strait of Gibraltar", "Spain and Morocco"), ("Bering Strait", "Russia and Alaska"), ("Bosphorus", "Europe and Asia, in Istanbul"), ("Cook Strait", "New Zealand's North and South Islands"))

m("scotland", "medium", "Match each island group to one of its islands",
  ("Inner Hebrides", "Skye"), ("Outer Hebrides", "Lewis"), ("Orkney", "Hoy"), ("Shetland", "Unst"))
m("scotland", "hard", "Match each whisky region to one of its distilleries",
  ("Islay", "Laphroaig"), ("Speyside", "Glenfiddich"), ("Highland", "Glenmorangie"), ("Lowland", "Auchentoshan"))

m("wales", "medium", "Match each Welsh place to what it's famous for",
  ("Hay-on-Wye", "Its book festival"), ("Portmeirion", "The Italian-style village from The Prisoner"), ("Llanfairpwllgwyngyll", "The longest place name in Britain"), ("Builth Wells", "The Royal Welsh Show"))
m("wales", "medium", "Match each Welsh band to one of its hits",
  ("Manic Street Preachers", "A Design for Life"), ("Stereophonics", "Dakota"), ("Catatonia", "Mulder and Scully"), ("Feeder", "Buck Rogers"))

m("ireland", "easy", "Match each Irish band to one of its hits",
  ("U2", "With or Without You"), ("The Cranberries", "Zombie"), ("Thin Lizzy", "The Boys Are Back in Town"), ("The Pogues", "Fairytale of New York"))
m("ireland", "medium", "Match each Irish landmark to its county",
  ("Cliffs of Moher", "Clare"), ("Giant's Causeway", "Antrim"), ("Newgrange", "Meath"), ("Rock of Cashel", "Tipperary"))

m("space", "easy", "Match each mission to the first it achieved",
  ("Vostok 1", "First person in space"), ("Apollo 11", "First people on the Moon"), ("Sputnik 1", "First artificial satellite"), ("Voyager 1", "First probe into interstellar space"))
m("space", "medium", "Match each planet to something it's known for",
  ("Jupiter", "The Great Red Spot"), ("Mars", "Olympus Mons, the tallest volcano"), ("Uranus", "Rolling round the Sun on its side"), ("Venus", "The hottest surface of any planet"))

m("human-body", "medium", "Match each body part to how many an adult has",
  ("Ribs", "24"), ("Teeth, in a full set", "32"), ("Vertebrae", "33"), ("Bones in each hand", "27"))
m("human-body", "medium", "Match each hormone to where it's made",
  ("Insulin", "Pancreas"), ("Adrenaline", "Adrenal glands"), ("Melatonin", "Pineal gland"), ("Thyroxine", "Thyroid gland"))

m("food-drink", "easy", "Match each cocktail to its main spirit",
  ("Mojito", "Rum"), ("Margarita", "Tequila"), ("Negroni", "Gin"), ("Moscow Mule", "Vodka"))
m("food-drink", "easy", "Match each dish to its country",
  ("Paella", "Spain"), ("Moussaka", "Greece"), ("Goulash", "Hungary"), ("Pierogi", "Poland"))

m("the-beatles", "medium", "Match each Beatles film to the year it came out",
  ("A Hard Day's Night", "1964"), ("Help!", "1965"), ("Yellow Submarine", "1968"), ("Let It Be", "1970"))
m("the-beatles", "medium", "Match each Beatle to a song he sang lead on",
  ("Ringo", "Yellow Submarine"), ("George", "Here Comes the Sun"), ("Paul", "Yesterday"), ("John", "Strawberry Fields Forever"))

m("eurovision", "medium", "Match each act to the song they sang for the UK",
  ("Sandie Shaw", "Puppet on a String"), ("Brotherhood of Man", "Save Your Kisses for Me"), ("Lulu", "Boom Bang-a-Bang"), ("Bucks Fizz", "Making Your Mind Up"))
m("eurovision", "medium", "Match each winning act to the country they won for",
  ("ABBA", "Sweden"), ("Lordi", "Finland"), ("Conchita Wurst", "Austria"), ("Ruslana", "Ukraine"))

m("star-wars", "easy", "Match each actor to their Star Wars role",
  ("Ewan McGregor", "Obi-Wan Kenobi"), ("Daisy Ridley", "Rey"), ("Adam Driver", "Kylo Ren"), ("Billy Dee Williams", "Lando Calrissian"))
m("star-wars", "medium", "Match each planet or moon to what happens there",
  ("Tatooine", "Luke grows up on a desert farm"), ("Hoth", "The Rebels' ice base is attacked"), ("Endor", "Ewoks help beat the Empire"), ("Alderaan", "It's blown up by the Death Star"))

m("cricket", "easy", "Match each format to how long it lasts",
  ("Test match", "Up to five days"), ("One-day international", "50 overs a side"), ("T20", "20 overs a side"), ("The Hundred", "100 balls a side"))
m("cricket", "medium", "Match each county to its home ground",
  ("Surrey", "The Oval"), ("Middlesex", "Lord's"), ("Durham", "Chester-le-Street"), ("Sussex", "Hove"))

m("rugby", "easy", "Match each nickname to its national rugby union team",
  ("All Blacks", "New Zealand"), ("Springboks", "South Africa"), ("Wallabies", "Australia"), ("Pumas", "Argentina"))
m("rugby", "medium", "Match each score in rugby union to its points",
  ("Try", "5"), ("Conversion", "2"), ("Penalty goal", "3"), ("Penalty try", "7"))

m("shakespeare", "easy", "Match each character to their play",
  ("Shylock", "The Merchant of Venice"), ("Prospero", "The Tempest"), ("Puck", "A Midsummer Night's Dream"), ("Malvolio", "Twelfth Night"))
m("shakespeare", "medium", "Match each famous line to its play",
  ("To be, or not to be", "Hamlet"), ("Now is the winter of our discontent", "Richard III"), ("Friends, Romans, countrymen", "Julius Caesar"), ("All the world's a stage", "As You Like It"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__m6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'matches in', len(OUT), 'topics:', ' '.join(OUT))
