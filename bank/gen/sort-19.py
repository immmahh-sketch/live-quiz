# Bank session 11 Oct 2026: 8 more Categorise questions -> bank/sort-16.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Books", ["Tolkien", "The Lord of the Rings"], "medium", "A Tolkien elf or a Tolkien dwarf?", "Elf", "Dwarf", ["Legolas", "Galadriel", "Elrond", "Arwen"], ["Gimli", "Thorin", "Balin", "Dwalin"])
s("TV", ["The Simpsons", "Futurama", "cartoons"], "medium", "A Simpsons character or a Futurama character?", "The Simpsons", "Futurama", ["Ned Flanders", "Moe", "Mr Burns", "Krusty"], ["Bender", "Leela", "Fry", "Zoidberg"])
s("Numbers", ["units", "imperial measures"], "hard", "An old unit of length or an old unit of weight?", "Length", "Weight", ["Furlong", "Fathom", "League", "Chain"], ["Ounce", "Stone", "Dram", "Grain"])
s("World geography", ["islands", "Greece", "Spain"], "easy", "A Greek island or a Spanish island?", "Greek", "Spanish", ["Crete", "Corfu", "Rhodes", "Kos"], ["Majorca", "Ibiza", "Tenerife", "Lanzarote"])
s("Famous people", ["Liverpool", "Manchester", "birthplaces"], "medium", "Born in Liverpool or in Manchester?", "Liverpool", "Manchester", ["Paul McCartney", "Cilla Black", "John Bishop", "Jamie Carragher"], ["Noel Gallagher", "Morrissey", "Jason Manford", "Karl Pilkington"])
s("Animals", ["dogs", "terriers", "spaniels"], "medium", "A terrier or a spaniel?", "Terrier", "Spaniel", ["Yorkshire", "Jack Russell", "Border", "Airedale"], ["Cocker", "Springer", "Clumber", "Sussex"])
s("Food and drink", ["pastry", "bread", "baking"], "easy", "A type of pastry or a type of bread?", "Pastry", "Bread", ["Filo", "Choux", "Puff", "Shortcrust"], ["Sourdough", "Bloomer", "Cob", "Bap"])
s("Music", ["Liverpool", "Manchester", "bands"], "hard", "A football ground or a famous music venue?", "Football ground", "Music venue", ["Anfield", "Goodison Park", "Old Trafford", "Maine Road"], ["The Cavern", "The Haçienda", "Free Trade Hall", "Eric's"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
