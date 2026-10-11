# Bank session 11 Oct 2026: 12 more Categorise questions -> bank/sort-13.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Film", ["Disney", "DreamWorks", "animation"], "easy", "A Disney Animation film or a DreamWorks film?", "Disney", "DreamWorks", ["Frozen", "Moana", "Tangled", "Zootopia"], ["Shrek", "Madagascar", "Kung Fu Panda", "How to Train Your Dragon"])
s("Football", ["Spain", "Italy", "European football"], "easy", "A Spanish club or an Italian club?", "Spain", "Italy", ["Sevilla", "Valencia", "Real Betis", "Athletic Bilbao"], ["Lazio", "Fiorentina", "Napoli", "Atalanta"])
s("Food and drink", ["gin", "vodka", "brands"], "medium", "A gin brand or a vodka brand?", "Gin", "Vodka", ["Gordon's", "Tanqueray", "Bombay Sapphire", "Hendrick's"], ["Smirnoff", "Absolut", "Grey Goose", "Stolichnaya"])
s("Film", ["Star Wars", "The Lord of the Rings"], "easy", "A Star Wars character or a Lord of the Rings character?", "Star Wars", "Lord of the Rings", ["Chewbacca", "Obi-Wan Kenobi", "Leia", "Yoda"], ["Gimli", "Galadriel", "Saruman", "Samwise"])
s("World geography", ["rivers", "Africa", "South America"], "medium", "A river in Africa or in South America?", "Africa", "South America", ["Nile", "Congo", "Niger", "Zambezi"], ["Amazon", "Orinoco", "Paraná", "Magdalena"])
s("World geography", ["mountain ranges", "Europe", "the Americas"], "easy", "A mountain range in Europe or in the Americas?", "Europe", "The Americas", ["Alps", "Pyrenees", "Carpathians", "Dolomites"], ["Andes", "Rockies", "Appalachians", "Sierra Madre"])
s("Words and language", ["carriages", "hats", "wordplay"], "hard", "A horse-drawn carriage or a hat?", "Carriage", "Hat", ["Landau", "Hansom", "Phaeton", "Brougham"], ["Fedora", "Trilby", "Homburg", "Stetson"])
s("Words and language", ["dogs", "cheese", "wordplay"], "medium", "A dog breed or a cheese?", "Dog breed", "Cheese", ["Lhasa Apso", "Shih Tzu", "Basenji", "Keeshond"], ["Gouda", "Gruyère", "Emmental", "Manchego"])
s("Music", ["David Bowie", "Prince"], "medium", "A David Bowie song or a Prince song?", "David Bowie", "Prince", ["Heroes", "Life on Mars?", "Starman", "Let's Dance"], ["Purple Rain", "Kiss", "When Doves Cry", "1999"])
s("Entertainment", ["comedians", "magicians"], "easy", "A comedian or a magician?", "Comedian", "Magician", ["Peter Kay", "Michael McIntyre", "Sarah Millican", "Jimmy Carr"], ["Paul Daniels", "Dynamo", "David Blaine", "David Copperfield"])
s("TV", ["newsreaders", "weather presenters", "BBC"], "medium", "A newsreader or a weather presenter?", "Newsreader", "Weather", ["Fiona Bruce", "Moira Stuart", "Trevor McDonald", "Jon Snow"], ["Carol Kirkwood", "Michael Fish", "Siân Lloyd", "Tomasz Schafernaker"])
s("Travel", ["airports", "London", "Paris"], "medium", "A London airport or a Paris airport?", "London", "Paris", ["Heathrow", "Gatwick", "Stansted", "Luton"], ["Charles de Gaulle", "Orly", "Beauvais", "Le Bourget"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
