# Bank session 10 Oct 2026: 14 more Categorise questions -> bank/sort-8.json. Two groups, four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("TV", ["Geordie Shore", "TOWIE", "reality TV"], "easy", "A 'Geordie Shore' star or a 'TOWIE' star?", "Geordie Shore", "TOWIE", ["Charlotte Crosby", "Gaz Beadle", "Holly Hagan", "Vicky Pattison"], ["Mark Wright", "Joey Essex", "Gemma Collins", "Lauren Goodger"])
s("James Bond", ["Bond girls", "Bond villains"], "easy", "A Bond girl or a Bond villain?", "Bond girl", "Bond villain", ["Honey Ryder", "Pussy Galore", "Vesper Lynd", "Holly Goodhead"], ["Le Chiffre", "Goldfinger", "Blofeld", "Scaramanga"])
s("Food and drink", ["cheese"], "hard", "A cheese made from cow's milk or from sheep's milk?", "Cow's milk", "Sheep's milk", ["Cheddar", "Brie", "Gouda", "Stilton"], ["Roquefort", "Manchego", "Pecorino Romano", "Feta"])
s("World geography", ["Commonwealth", "monarchy"], "medium", "A Commonwealth country with King Charles as head of state, or a Commonwealth republic?", "King Charles", "Republic", ["Canada", "Australia", "New Zealand", "Jamaica"], ["India", "South Africa", "Kenya", "Barbados"])
s("Art", ["Teenage Mutant Ninja Turtles", "Renaissance"], "easy", "A Teenage Mutant Ninja Turtle, or only a Renaissance artist?", "Ninja Turtle", "Just an artist", ["Leonardo", "Michelangelo", "Donatello", "Raphael"], ["Titian", "Botticelli", "Caravaggio", "Bellini"])
s("Science", ["dinosaurs"], "easy", "A plant-eating dinosaur or a meat-eating one?", "Plant-eater", "Meat-eater", ["Stegosaurus", "Triceratops", "Diplodocus", "Brachiosaurus"], ["Tyrannosaurus rex", "Velociraptor", "Spinosaurus", "Allosaurus"])
s("TV", ["soaps", "Coronation Street", "Emmerdale"], "medium", "A 'Coronation Street' character or an 'Emmerdale' character?", "Coronation Street", "Emmerdale", ["Rita Sullivan", "Ken Barlow", "Hilda Ogden", "Steve McDonald"], ["Zak Dingle", "Seth Armstrong", "Kim Tate", "Annie Sugden"])
s("Books", ["Charles Dickens", "Thomas Hardy", "characters"], "hard", "A Charles Dickens character or a Thomas Hardy character?", "Dickens", "Hardy", ["Pip", "Fagin", "Mr Micawber", "Miss Havisham"], ["Bathsheba Everdene", "Gabriel Oak", "Michael Henchard", "Tess Durbeyfield"])
s("Food and drink", ["pasta", "rice"], "medium", "A pasta shape or a variety of rice?", "Pasta", "Rice", ["Penne", "Fusilli", "Farfalle", "Orzo"], ["Arborio", "Basmati", "Jasmine", "Carnaroli"])
s("TV", ["Bake Off", "MasterChef", "cookery"], "hard", "A 'Bake Off' winner or a 'MasterChef' winner?", "Bake Off", "MasterChef", ["Edd Kimber", "John Whaite", "Nadiya Hussain", "Candice Brown"], ["Thomasina Miers", "Mat Follas", "Tim Anderson", "Ping Coombes"])
s("UK geography", ["islands", "Scotland", "Wales"], "medium", "A Scottish island or a Welsh island?", "Scottish", "Welsh", ["Arran", "Skye", "Islay", "Mull"], ["Anglesey", "Caldey", "Bardsey", "Skomer"])
s("Travel", ["London Underground", "Paris Métro"], "easy", "A London Tube station or a Paris Métro station?", "London", "Paris", ["Angel", "Mornington Crescent", "Elephant & Castle", "Cockfosters"], ["Bastille", "Châtelet", "Pigalle", "Trocadéro"])
s("Food and drink", ["beer", "Belgium", "Germany"], "medium", "A Belgian beer or a German beer?", "Belgian", "German", ["Stella Artois", "Leffe", "Hoegaarden", "Duvel"], ["Beck's", "Warsteiner", "Erdinger", "Paulaner"])
s("Sport", ["England", "football", "cricket"], "easy", "Played for England at football or at cricket?", "Football", "Cricket", ["Gary Lineker", "Bobby Moore", "Wayne Rooney", "Harry Kane"], ["Ian Botham", "Joe Root", "Andrew Flintoff", "Stuart Broad"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
