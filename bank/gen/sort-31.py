# Bank session 11 Oct 2026: more Categorise questions -> bank/sort-28.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})


s("Film", ["Dickens", "Scrooge", "Fagin", "actors"], "hard", "Has played Scrooge or has played Fagin?", "Scrooge", "Fagin", ["Alastair Sim", "Michael Caine", "Patrick Stewart", "Jim Carrey"], ["Alec Guinness", "Ron Moody", "Ben Kingsley", "Timothy Spall"])
s("Film", ["Elizabeth I", "Elizabeth II", "actresses"], "medium", "Has played Elizabeth I or Elizabeth II on screen?", "Elizabeth I", "Elizabeth II", ["Cate Blanchett", "Judi Dench", "Glenda Jackson", "Bette Davis"], ["Claire Foy", "Olivia Colman", "Imelda Staunton"])
s("TV", ["Gavin & Stacey", "Essex", "Wales"], "easy", "A Gavin & Stacey character from Essex or from Wales?", "Essex", "Wales", ["Gavin", "Pam", "Mick", "Smithy"], ["Stacey", "Nessa", "Bryn", "Gwen"])
s("TV", ["Derry Girls", "Father Ted", "Irish comedy"], "medium", "A Derry Girls character or a Father Ted character?", "Derry Girls", "Father Ted", ["Erin", "Orla", "Clare", "Sister Michael"], ["Dougal", "Father Jack", "Mrs Doyle", "Bishop Brennan"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-28.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
