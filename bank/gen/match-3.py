# Bank session 9 Oct 2026 (second pass): 2 more Match questions for 14 topics that had 5 live.
# Writes bank/topics/<slug>__m3.json; import each with FILE=<slug>__m3 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})

m("action-films", "medium", "Match each screen hero to the agency he works for",
  ("James Bond", "MI6"), ("Ethan Hunt", "IMF"), ("Nick Fury", "S.H.I.E.L.D."), ("Jason Bourne", "CIA"))
m("action-films", "easy", "Match each villain to the action film he's from",
  ("Hans Gruber", "Die Hard"), ("Bane", "The Dark Knight Rises"), ("Raoul Silva", "Skyfall"), ("Agent Smith", "The Matrix"))

m("us-tv", "medium", "Match each US sitcom to its regular hangout",
  ("Friends", "Central Perk"), ("How I Met Your Mother", "MacLaren's"), ("Seinfeld", "Monk's Café"), ("Happy Days", "Arnold's"))
m("us-tv", "medium", "Match each US drama to where it's set",
  ("Breaking Bad", "Albuquerque"), ("Grey's Anatomy", "Seattle"), ("The Sopranos", "New Jersey"), ("Dexter", "Miami"))

m("anagrams-wordplay", "medium", "Match each country to the word its letters make",
  ("Spain", "Pains"), ("Peru", "Pure"), ("Mali", "Mail"), ("Nepal", "Panel"))
m("anagrams-wordplay", "medium", "Match each clue to its palindrome",
  ("Small Inuit boat", "Kayak"), ("Female sheep", "Ewe"), ("Mother", "Mum"), ("Look quickly", "Peep"))

m("ancient-history", "medium", "Match each Wonder of the Ancient World to its city",
  ("The Colossus", "Rhodes"), ("The Lighthouse", "Alexandria"), ("The Hanging Gardens", "Babylon"), ("The Mausoleum", "Halicarnassus"))
m("ancient-history", "medium", "Match each Roman name to the British city",
  ("Eboracum", "York"), ("Londinium", "London"), ("Deva", "Chester"), ("Aquae Sulis", "Bath"))

m("animals", "medium", "Match each animal to its home",
  ("Badger", "Sett"), ("Rabbit", "Warren"), ("Eagle", "Eyrie"), ("Beaver", "Lodge"))
m("animals", "medium", "Match each group name to its animals",
  ("A tower", "Giraffes"), ("A dazzle", "Zebras"), ("A crash", "Rhinos"), ("A pod", "Dolphins"))

m("pixar-animation", "easy", "Match each Pixar film to its main character",
  ("Ratatouille", "Remy"), ("Up", "Carl"), ("Coco", "Miguel"), ("Brave", "Merida"))
m("pixar-animation", "easy", "Match each Disney film to its villain",
  ("Snow White and the Seven Dwarfs", "The Evil Queen"), ("The Little Mermaid", "Ursula"), ("Aladdin", "Jafar"), ("Tangled", "Mother Gothel"))

m("art", "hard", "Match each painting to the gallery where it hangs",
  ("Mona Lisa", "The Louvre, Paris"), ("The Starry Night", "MoMA, New York"), ("The Night Watch", "Rijksmuseum, Amsterdam"), ("The Birth of Venus", "Uffizi, Florence"))
m("art", "medium", "Match each British artist to a famous work",
  ("L. S. Lowry", "Going to the Match"), ("Damien Hirst", "A shark in formaldehyde"), ("Tracey Emin", "My Bed"), ("Banksy", "Girl with Balloon"))

m("australia", "easy", "Match each bit of Aussie slang to its meaning",
  ("Arvo", "Afternoon"), ("Brekkie", "Breakfast"), ("Thongs", "Flip-flops"), ("Ute", "Pick-up truck"))
m("australia", "medium", "Match each Australian town or city to its state or territory",
  ("Alice Springs", "Northern Territory"), ("Geelong", "Victoria"), ("Newcastle", "New South Wales"), ("Fremantle", "Western Australia"))

m("beer-wine-spirits", "medium", "Match each spirit to what it's made from",
  ("Rum", "Sugar cane"), ("Tequila", "Agave"), ("Brandy", "Grapes"), ("Malt whisky", "Malted barley"))
m("beer-wine-spirits", "medium", "Match each cocktail to its base spirit",
  ("Mojito", "Rum"), ("Margarita", "Tequila"), ("Negroni", "Gin"), ("Cosmopolitan", "Vodka"))

m("books", "easy", "Match each children's book to its author",
  ("The Very Hungry Caterpillar", "Eric Carle"), ("Where the Wild Things Are", "Maurice Sendak"), ("Matilda", "Roald Dahl"), ("The Tiger Who Came to Tea", "Judith Kerr"))
m("books", "medium", "Match each novel to the city it's set in",
  ("Ulysses", "Dublin"), ("Trainspotting", "Edinburgh"), ("The Great Gatsby", "New York"), ("Les Misérables", "Paris"))

m("brands-logos", "medium", "Match each brand to the animal in its logo",
  ("Ferrari", "Prancing horse"), ("Peugeot", "Lion"), ("Lamborghini", "Bull"), ("Twitter", "Bird"))
m("brands-logos", "easy", "Match each company to the country it began in",
  ("IKEA", "Sweden"), ("LEGO", "Denmark"), ("Nokia", "Finland"), ("Samsung", "South Korea"))

m("british-films", "easy", "Match each British film to its leading man",
  ("Billy Elliot", "Jamie Bell"), ("Trainspotting", "Ewan McGregor"), ("The Full Monty", "Robert Carlyle"), ("Notting Hill", "Hugh Grant"))
m("british-films", "easy", "Match each actor to their Harry Potter role",
  ("Alan Rickman", "Severus Snape"), ("Maggie Smith", "Minerva McGonagall"), ("Robbie Coltrane", "Rubeus Hagrid"), ("Michael Gambon", "Albus Dumbledore"))

m("british-food", "medium", "Match each dish to where it comes from",
  ("Stottie cake", "Tyneside"), ("Scouse", "Liverpool"), ("Cullen skink", "Scotland"), ("Laverbread", "Wales"))
m("british-food", "medium", "Match each pudding to its key ingredient",
  ("Spotted dick", "Suet and currants"), ("Eton mess", "Meringue"), ("Bakewell tart", "Almonds and jam"), ("Sticky toffee pudding", "Dates"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__m3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'matches in', len(OUT), 'topics:', ' '.join(OUT))
