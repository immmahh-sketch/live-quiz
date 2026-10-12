# Bank session 12 Oct 2026: 4 more Categorise questions -> bank/sort-35.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

# Alston and Brampton sit right by the border; Haltwhistle is Northumberland
s("UK geography", ["North East", "Cumbria"], "medium", "A town in the North East or in Cumbria?", "North East", "Cumbria", ["Alnwick", "Morpeth", "Haltwhistle", "Consett"], ["Alston", "Brampton", "Penrith", "Whitehaven"])
s("Music", ["Spice Girls", "Teletubbies"], "easy", "A Spice Girl or a Teletubby?", "Spice Girl", "Teletubby", ["Posh", "Scary", "Sporty", "Baby"], ["Dipsy", "Po", "Laa-Laa", "Tinky Winky"])
s("TV", ["Auf Wiedersehen, Pet", "Only Fools and Horses"], "medium", "A character in 'Auf Wiedersehen, Pet' or in 'Only Fools and Horses'?", "Auf Wiedersehen, Pet", "Only Fools and Horses", ["Oz", "Neville", "Barry", "Bomber"], ["Del Boy", "Rodney", "Trigger", "Boycie"])
s("UK geography", ["rivers", "North East", "Yorkshire"], "hard", "A river in the North East or in Yorkshire?", "North East", "Yorkshire", ["Coquet", "Aln", "Wansbeck", "Wear"], ["Aire", "Swale", "Wharfe", "Calder"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-35.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
