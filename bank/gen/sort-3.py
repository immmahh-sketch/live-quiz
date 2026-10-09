# Bank session 9 Oct 2026 (second pass): 2 more Categorise (sort) questions for 13 topics that had 5 live.
# Writes bank/topics/<slug>__s3.json; import with FILE=<slug>__s3 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def s(slug, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.setdefault(slug, []).append({"type": "sort", "text": text, "categories": [a, b],
        "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B], "difficulty": diff})

s("action-films", "medium", "A Bruce Willis film or a Mel Gibson film?", "Bruce Willis", "Mel Gibson",
  ["Die Hard", "Armageddon", "The Sixth Sense", "Pulp Fiction"], ["Braveheart", "Mad Max", "Lethal Weapon", "Ransom"])
s("action-films", "medium", "A submarine film or a spaceship film?", "Submarine", "Spaceship",
  ["Das Boot", "The Hunt for Red October", "Crimson Tide", "U-571"], ["Alien", "Gravity", "Apollo 13", "Interstellar"])

s("us-tv", "easy", "Set in a hospital, or in a police station?", "Hospital", "Police station",
  ["Grey's Anatomy", "ER", "Scrubs", "House"], ["Brooklyn Nine-Nine", "NYPD Blue", "Hill Street Blues", "The Shield"])
s("us-tv", "easy", "Animated US comedy or live-action US comedy?", "Animated", "Live action",
  ["Family Guy", "South Park", "Futurama", "King of the Hill"], ["Seinfeld", "Frasier", "Cheers", "Friends"])

s("ancient-history", "medium", "Built by the Romans or by the ancient Greeks?", "Romans", "Greeks",
  ["Colosseum", "Pantheon", "Hadrian's Wall", "Pont du Gard"], ["Parthenon", "Theatre of Epidaurus", "Temple of Apollo at Delphi", "Erechtheion"])
s("ancient-history", "easy", "Egyptian pharaoh or Roman emperor?", "Pharaoh", "Roman emperor",
  ["Tutankhamun", "Ramesses II", "Cleopatra", "Akhenaten"], ["Nero", "Hadrian", "Trajan", "Caligula"])

s("pixar-animation", "medium", "A Disney Animation film or a Pixar film?", "Disney Animation", "Pixar",
  ["Frozen", "Moana", "Tangled", "Encanto"], ["Up", "Coco", "Ratatouille", "Inside Out"])
s("pixar-animation", "easy", "Shrek character or Toy Story character?", "Shrek", "Toy Story",
  ["Donkey", "Lord Farquaad", "Fiona", "Puss in Boots"], ["Woody", "Rex", "Hamm", "Jessie"])

s("art", "medium", "Painted by Monet or by Van Gogh?", "Monet", "Van Gogh",
  ["Water Lilies", "Impression, Sunrise", "Rouen Cathedral", "Poppy Field"], ["Sunflowers", "The Starry Night", "Café Terrace at Night", "The Potato Eaters"])
s("art", "easy", "A famous painting or a famous sculpture?", "Painting", "Sculpture",
  ["Mona Lisa", "The Scream", "Guernica", "The Hay Wain"], ["Michelangelo's David", "The Thinker", "Venus de Milo", "Angel of the North"])

s("australia", "easy", "A sight in Australia or in New Zealand?", "Australia", "New Zealand",
  ["Uluru", "Great Barrier Reef", "Bondi Beach", "Sydney Opera House"], ["Milford Sound", "Hobbiton", "Rotorua", "Aoraki / Mount Cook"])
s("australia", "medium", "Played cricket for Australia, or rugby for New Zealand?", "Australian cricketer", "All Black",
  ["Shane Warne", "Don Bradman", "Ricky Ponting", "Steve Smith"], ["Jonah Lomu", "Richie McCaw", "Dan Carter", "Beauden Barrett"])

s("beer-wine-spirits", "medium", "A whisky or a gin?", "Whisky", "Gin",
  ["Glenfiddich", "Johnnie Walker", "Jameson", "Famous Grouse"], ["Gordon's", "Tanqueray", "Hendrick's", "Bombay Sapphire"])
s("beer-wine-spirits", "medium", "A red wine grape or a white wine grape?", "Red", "White",
  ["Merlot", "Pinot Noir", "Shiraz", "Cabernet Sauvignon"], ["Chardonnay", "Sauvignon Blanc", "Riesling", "Pinot Grigio"])

s("books", "medium", "Written by a Brontë sister or by Jane Austen?", "A Brontë", "Jane Austen",
  ["Jane Eyre", "Wuthering Heights", "Villette", "The Tenant of Wildfell Hall"], ["Emma", "Persuasion", "Sense and Sensibility", "Mansfield Park"])
s("books", "medium", "Written by J. R. R. Tolkien or by C. S. Lewis?", "Tolkien", "C. S. Lewis",
  ["The Hobbit", "The Silmarillion", "The Two Towers", "The Fellowship of the Ring"], ["The Lion, the Witch and the Wardrobe", "Prince Caspian", "The Screwtape Letters", "The Magician's Nephew"])

s("brands-logos", "medium", "A car brand or a watch brand?", "Cars", "Watches",
  ["Bentley", "Lotus", "Bugatti", "Maserati"], ["Rolex", "Omega", "TAG Heuer", "Breitling"])
s("brands-logos", "easy", "Founded in the UK or in the USA?", "UK", "USA",
  ["Tesco", "Greggs", "Burberry", "Cadbury"], ["Nike", "Starbucks", "Walmart", "Gap"])

s("british-films", "medium", "A Richard Curtis film or a Guy Ritchie film?", "Richard Curtis", "Guy Ritchie",
  ["Four Weddings and a Funeral", "Notting Hill", "Love Actually", "About Time"], ["Lock, Stock and Two Smoking Barrels", "Snatch", "RocknRolla", "The Gentlemen"])
s("british-films", "medium", "Starring Hugh Grant or starring Colin Firth?", "Hugh Grant", "Colin Firth",
  ["About a Boy", "Music and Lyrics", "Paddington 2", "Wonka"], ["The King's Speech", "Mamma Mia!", "Kingsman: The Secret Service", "A Single Man"])

s("british-food", "medium", "A pie or a pudding?", "Pie", "Pudding",
  ["Cottage pie", "Steak and kidney pie", "Pork pie", "Shepherd's pie"], ["Yorkshire pudding", "Black pudding", "Bread and butter pudding", "Christmas pudding"])
s("british-food", "hard", "A British sausage or a British cheese?", "Sausage", "Cheese",
  ["Cumberland", "Lincolnshire", "Glamorgan", "Oxford"], ["Cheddar", "Stilton", "Lancashire", "Red Leicester"])

s("british-history", "easy", "Tudor or Victorian?", "Tudor", "Victorian",
  ["Henry VIII", "Elizabeth I", "Thomas Cromwell", "The Spanish Armada"], ["Charles Dickens", "Florence Nightingale", "Isambard Kingdom Brunel", "The Great Exhibition"])
s("british-history", "medium", "A battle fought in England or in Scotland?", "England", "Scotland",
  ["Hastings", "Bosworth", "Naseby", "Marston Moor"], ["Bannockburn", "Culloden", "Prestonpans", "Stirling Bridge"])

s("british-sitcoms", "medium", "First shown on the BBC or on ITV?", "BBC", "ITV",
  ["Only Fools and Horses", "Fawlty Towers", "The Office", "Gavin & Stacey"], ["Rising Damp", "Benidorm", "Man About the House", "Bless This House"])
s("british-sitcoms", "medium", "Set in the north of England or the south?", "North", "South",
  ["The Royle Family", "Last of the Summer Wine", "Early Doors", "Phoenix Nights"], ["Only Fools and Horses", "Fawlty Towers", "Men Behaving Badly", "The Good Life"])

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__s3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'sorts in', len(OUT), 'topics:', ' '.join(OUT))
