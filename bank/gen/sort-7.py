# Bank session 10 Oct 2026: 14 more Categorise questions -> bank/sort-4.json. Two groups, four items each (three for the
# colours). Each pair of categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Music", ["Beatles", "solo"], "medium", "John Lennon solo or Paul McCartney (with or without Wings)?", "Lennon", "McCartney", ["Imagine", "Instant Karma!", "Jealous Guy", "Woman"], ["Band on the Run", "Mull of Kintyre", "Jet", "Silly Love Songs"])
s("Sport", ["Paralympics", "Olympics"], "medium", "Paralympic-only sport or Olympic sport?", "Paralympic only", "Olympic", ["Goalball", "Boccia", "Wheelchair rugby", "Sitting volleyball"], ["Fencing", "Handball", "Water polo", "Modern pentathlon"])
s("Science", ["dinosaurs", "wow"], "hard", "Lived in the Jurassic or the Cretaceous?", "Jurassic", "Cretaceous", ["Stegosaurus", "Brachiosaurus", "Diplodocus", "Allosaurus"], ["Tyrannosaurus rex", "Triceratops", "Velociraptor", "Spinosaurus"])
s("Nature", ["British wildlife"], "easy", "Mostly out at night, or mostly out by day?", "Night", "Day", ["Tawny owl", "Badger", "Hedgehog", "Bat"], ["Red squirrel", "Robin", "Butterfly", "Swan"])
s("Music", ["Britpop", "Pulp", "Suede"], "medium", "Pulp song or Suede song?", "Pulp", "Suede", ["Common People", "Disco 2000", "Babies", "Sorted for E's & Wizz"], ["Animal Nitrate", "Trash", "The Drowners", "Beautiful Ones"])
s("Space", ["moons", "wow"], "hard", "Bigger than our Moon, or smaller?", "Bigger", "Smaller", ["Ganymede", "Titan", "Callisto", "Io"], ["Europa", "Triton", "Enceladus", "Phobos"])
s("Words and language", ["spelling"], "easy", "British spelling or American spelling?", "British", "American", ["Aluminium", "Cheque", "Tyre", "Programme"], ["Center", "Defense", "Gray", "Pajamas"])
s("UK geography", ["national parks", "Lake District", "Yorkshire Dales"], "medium", "In the Lake District or the Yorkshire Dales?", "Lake District", "Yorkshire Dales", ["Ullswater", "Keswick", "Grasmere", "Helvellyn"], ["Malham Cove", "Aysgarth Falls", "Hawes", "Pen-y-ghent"])
s("Music", ["Queen", "Freddie Mercury"], "medium", "A Queen song or a Freddie Mercury solo song?", "Queen", "Freddie solo", ["Bohemian Rhapsody", "Radio Ga Ga", "Somebody to Love", "Killer Queen"], ["Living on My Own", "The Great Pretender", "Barcelona", "Love Kills"])
s("Shakespeare", ["plays"], "medium", "Shakespeare comedy or history play?", "Comedy", "History", ["Twelfth Night", "As You Like It", "Much Ado About Nothing", "The Merry Wives of Windsor"], ["Henry V", "Richard III", "King John", "Henry VIII"])
s("Food and drink", ["cheese", "wine"], "easy", "A cheese or a wine?", "Cheese", "Wine", ["Brie", "Stilton", "Gouda", "Manchego"], ["Rioja", "Merlot", "Chablis", "Prosecco"])
s("World geography", ["lakes", "seas", "wow"], "hard", "Despite its name, really a lake? Or a true sea?", "A lake", "A sea", ["Caspian Sea", "Dead Sea", "Sea of Galilee", "Aral Sea"], ["Sargasso Sea", "Red Sea", "Black Sea", "Coral Sea"])
s("James Bond", ["Bond themes"], "medium", "Bond theme sung by a man (or men) or by a woman?", "A man", "A woman", ["Thunderball", "A View to a Kill", "Writing's on the Wall", "You Know My Name"], ["Goldfinger", "Skyfall", "No Time to Die", "Nobody Does It Better"])
s("UK geography", ["London", "M25"], "medium", "Inside the M25 or outside it?", "Inside", "Outside", ["Croydon", "Romford", "Kingston upon Thames", "Enfield"], ["Slough", "Guildford", "St Albans", "Sevenoaks"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
