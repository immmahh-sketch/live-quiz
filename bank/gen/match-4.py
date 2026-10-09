# Bank session 9 Oct 2026 (third pass): 1–2 more Match questions for 13 broad topics that had 5 live (Christmas first).
# Writes bank/topics/<slug>__m4.json; import each with FILE=<slug>__m4 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})

m("christmas", "medium", "Match each Christmas tradition to the country it began in",
  ("The Christmas tree", "Germany"), ("Christmas crackers", "England"), ("The poinsettia", "Mexico"), ("Twelve grapes at midnight", "Spain"))
m("christmas", "medium", "Match each Christmas song to the year it came out",
  ("White Christmas", "1942"), ("Jingle Bell Rock", "1957"), ("Last Christmas", "1984"), ("All I Want for Christmas Is You", "1994"))
m("christmas-tv", "easy", "Match each Christmas cartoon to the author of the book",
  ("The Snowman", "Raymond Briggs"), ("The Gruffalo", "Julia Donaldson"), ("The Tiger Who Came to Tea", "Judith Kerr"), ("We're Going on a Bear Hunt", "Michael Rosen"))
m("christmas-movies", "easy", "Match each Christmas film to its star",
  ("Elf", "Will Ferrell"), ("The Santa Clause", "Tim Allen"), ("Jingle All the Way", "Arnold Schwarzenegger"), ("Bad Santa", "Billy Bob Thornton"))
m("christmas-movies", "medium", "Match each Christmas film to where it's set",
  ("Home Alone 2: Lost in New York", "New York"), ("Love Actually", "London"), ("Die Hard", "Los Angeles"), ("The Holiday", "Surrey"))
m("christmas-music", "easy", "Match each Christmas hit to the band that recorded it",
  ("Merry Xmas Everybody", "Slade"), ("I Wish It Could Be Christmas Everyday", "Wizzard"), ("Fairytale of New York", "The Pogues"), ("Last Christmas", "Wham!"))
m("christmas-music", "medium", "Match each Christmas number one to its year",
  ("Merry Xmas Everybody", "1973"), ("Mistletoe and Wine", "1988"), ("Stay Another Day", "1994"), ("Mad World", "2003"))

m("bonfire-night", "easy", "Match each autumn star sign to its symbol",
  ("Virgo", "The maiden"), ("Libra", "The scales"), ("Scorpio", "The scorpion"), ("Sagittarius", "The archer"))
m("bonfire-night", "easy", "Match each firework to what it does",
  ("Catherine wheel", "Spins round on a pin"), ("Rocket", "Shoots up into the sky"), ("Roman candle", "Fires balls of colour one after another"), ("Sparkler", "Fizzes in your hand"))

m("boxing-combat", "easy", "Match each boxer to his nickname",
  ("Muhammad Ali", "The Greatest"), ("Mike Tyson", "Iron Mike"), ("Tyson Fury", "The Gypsy King"), ("Joe Frazier", "Smokin' Joe"))
m("boxing-combat", "medium", "Match each combat sport to where it's fought",
  ("Boxing", "A ring"), ("Sumo", "A dohyō"), ("UFC", "The Octagon"), ("Fencing", "A piste"))

m("british-history", "hard", "Match each queen to her husband",
  ("Queen Victoria", "Prince Albert"), ("Elizabeth II", "Prince Philip"), ("Mary I", "Philip II of Spain"), ("Queen Anne", "Prince George of Denmark"))
m("british-history", "medium", "Match each event to its century",
  ("Magna Carta is sealed", "13th century"), ("The Battle of Agincourt", "15th century"), ("The Great Fire of London", "17th century"), ("The Battle of Waterloo", "19th century"))

m("capital-cities", "easy", "Match each South American country to its capital",
  ("Argentina", "Buenos Aires"), ("Chile", "Santiago"), ("Peru", "Lima"), ("Colombia", "Bogotá"))
m("capital-cities", "medium", "Match each capital to its nickname",
  ("Paris", "The City of Light"), ("Rome", "The Eternal City"), ("Edinburgh", "Auld Reekie"), ("Vienna", "The City of Music"))

m("cars-motoring", "medium", "Match each road sign shape to what it usually means",
  ("Circle", "An order"), ("Triangle", "A warning"), ("Rectangle", "Information"), ("Octagon", "Stop"))
m("cars-motoring", "easy", "Match each car to its maker",
  ("Golf", "Volkswagen"), ("Fiesta", "Ford"), ("Corsa", "Vauxhall"), ("Qashqai", "Nissan"))

m("kids-tv", "easy", "Match each Teletubby to its colour",
  ("Tinky Winky", "Purple"), ("Dipsy", "Green"), ("Laa-Laa", "Yellow"), ("Po", "Red"))
m("kids-tv", "medium", "Match each Thunderbird to its job",
  ("Thunderbird 1", "Fast rescue rocket, first on the scene"), ("Thunderbird 2", "Heavy carrier for the rescue gear"), ("Thunderbird 3", "Space rocket"), ("Thunderbird 4", "Submarine"))

m("childrens-books", "easy", "Match each Roald Dahl character to their book",
  ("Augustus Gloop", "Charlie and the Chocolate Factory"), ("Miss Trunchbull", "Matilda"), ("The Grand High Witch", "The Witches"), ("Boggis, Bunce and Bean", "Fantastic Mr Fox"))
m("childrens-books", "medium", "Match each Beatrix Potter character to its animal",
  ("Mrs Tiggy-Winkle", "Hedgehog"), ("Jeremy Fisher", "Frog"), ("Mr Tod", "Fox"), ("Samuel Whiskers", "Rat"))

m("classical-music", "easy", "Match each composer to a famous work",
  ("Holst", "The Planets"), ("Vivaldi", "The Four Seasons"), ("Handel", "Messiah"), ("Tchaikovsky", "The Nutcracker"))
m("classical-music", "easy", "Match each instrument to its section of the orchestra",
  ("Oboe", "Woodwind"), ("Trombone", "Brass"), ("Viola", "Strings"), ("Timpani", "Percussion"))

m("computers-internet", "easy", "Match each tech company to the person who founded it",
  ("Microsoft", "Bill Gates"), ("Amazon", "Jeff Bezos"), ("Facebook", "Mark Zuckerberg"), ("SpaceX", "Elon Musk"))
m("computers-internet", "easy", "Match each file ending to what the file holds",
  (".jpg", "A picture"), (".mp3", "Music"), (".pdf", "A document"), (".zip", "A compressed folder"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__m4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'matches in', len(OUT), 'topics:', ' '.join(OUT))
