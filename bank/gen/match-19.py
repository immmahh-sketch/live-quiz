# Bank session 11 Oct 2026 (eighteenth pass): one more Match question each for 19 topics on 7 or 8 live, checked against
# the live questions in each topic. Writes bank/topics/<slug>__m19.json; import each with FILE=<slug>__m19 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})

m("connections", "easy", "Match each famous name to their partner in a well-known pair",
  ("Torvill and ...", "Dean"), ("Ant and ...", "Dec"), ("Bill and ...", "Ben"), ("Pinky and ...", "Perky"))
m("no-such-thing-as-a-fish", "hard", "Match each animal to a surprising close relative",
  ("Hippopotamus", "Whale"), ("Elephant", "Manatee"), ("Chicken", "Tyrannosaurus rex"), ("Horseshoe crab", "Spider"))
m("ripleys-believe-it-or-not", "medium", "Match each oddly named British place to its county",
  ("Westward Ho!", "Devon"), ("Wetwang", "Yorkshire"), ("Great Snoring", "Norfolk"), ("Pity Me", "County Durham"))
m("handmaids-tale", "medium", "Match each Gilead place to what it is",
  ("The Red Center", "Where Handmaids are trained"), ("The Wall", "Where bodies are hung"), ("Jezebel's", "A secret brothel"), ("The Colonies", "Toxic labour camps"))
m("valentines", "medium", "Match each Shakespeare lover to their partner",
  ("Benedick", "Beatrice"), ("Oberon", "Titania"), ("Ferdinand", "Miranda"), ("Petruchio", "Katherina"))
m("number-ones", "medium", "Match each act to its first UK number one",
  ("Oasis", "Some Might Say"), ("Blur", "Country House"), ("Take That", "Pray"), ("Spice Girls", "Wannabe"))
m("words-language", "easy", "Match each Latin phrase to its meaning",
  ("Carpe diem", "Seize the day"), ("Ad infinitum", "For ever"), ("Bona fide", "Genuine"), ("Status quo", "The way things are"))
m("action-films", "medium", "Match each action star to the martial art he's known for",
  ("Bruce Lee", "Jeet Kune Do"), ("Chuck Norris", "Karate"), ("Jean-Claude Van Damme", "Kickboxing"), ("Steven Seagal", "Aikido"))
m("us-tv", "medium", "Match each US sitcom to its lead character's job",
  ("Frasier", "Radio psychiatrist"), ("Cheers", "Bar owner"), ("The Office", "Paper company manager"), ("Scrubs", "Hospital doctor"))
m("pixar-animation", "easy", "Match each Toy Story toy to what it is",
  ("Rex", "Dinosaur"), ("Hamm", "Piggy bank"), ("Slinky", "Dog"), ("Bullseye", "Horse"))
m("art", "medium", "Match each artist to the city most linked with their work",
  ("L. S. Lowry", "Salford"), ("Rembrandt", "Amsterdam"), ("Antoni Gaudí", "Barcelona"), ("Andy Warhol", "New York"))
m("australia", "medium", "Match each Australian creature to what it is",
  ("Quokka", "Small marsupial"), ("Dingo", "Wild dog"), ("Kookaburra", "Kingfisher"), ("Taipan", "Venomous snake"))
m("beer-wine-spirits", "medium", "Match each beer style to its character",
  ("Stout", "Dark and roasty"), ("Pilsner", "Pale, crisp lager"), ("IPA", "Hoppy pale ale"), ("Mild", "Low-strength dark ale"))
m("bonfire-night", "easy", "Match each autumn find to the tree or bush it comes from",
  ("Conker", "Horse chestnut"), ("Acorn", "Oak"), ("Sloe", "Blackthorn"), ("Rosehip", "Wild rose"))
m("boxing-combat", "medium", "Match each UFC star to their country",
  ("Conor McGregor", "Ireland"), ("Khabib Nurmagomedov", "Russia"), ("Israel Adesanya", "New Zealand"), ("Jon Jones", "USA"))
m("boy-bands-girl-groups", "easy", "Match each boy band to one of its hits",
  ("Busted", "Year 3000"), ("McFly", "All About You"), ("JLS", "Beat Again"), ("Blue", "All Rise"))
m("brands-logos", "hard", "Match each company to what it first made or sold",
  ("Nokia", "Paper"), ("Nintendo", "Playing cards"), ("Lamborghini", "Tractors"), ("Samsung", "Groceries"))
m("cars-motoring", "medium", "Match each Bond car to its film",
  ("Aston Martin DB5", "Goldfinger"), ("Lotus Esprit submarine", "The Spy Who Loved Me"), ("BMW Z3", "GoldenEye"), ("Invisible Aston Martin Vanquish", "Die Another Day"))
m("kids-tv", "medium", "Match each Saturday morning show to a presenter",
  ("Going Live!", "Phillip Schofield"), ("SM:TV Live", "Ant and Dec"), ("Live & Kicking", "Zoe Ball"), ("Saturday Superstore", "Mike Read"))
m("capital-cities", "hard", "Match each European capital to its country",
  ("Ljubljana", "Slovenia"), ("Bratislava", "Slovakia"), ("Tallinn", "Estonia"), ("Chișinău", "Moldova"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, qs in OUT.items():
    json.dump(qs, open(os.path.join(here, '..', 'topics', slug + '__m19.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(len(q) for q in OUT.values()), 'match questions written for', len(OUT), 'topics')
