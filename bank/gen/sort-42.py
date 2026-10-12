# Bank session 12 Oct 2026: 2 more Categorise questions -> bank/sort-42.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("TV", ["Dragons' Den", "The Apprentice", "business"], "medium", "A Dragon from 'Dragons' Den' or an adviser on 'The Apprentice'?", "Dragon", "Apprentice adviser",
  ["Peter Jones", "Deborah Meaden", "Theo Paphitis", "Touker Suleyman"], ["Karren Brady", "Nick Hewer", "Margaret Mountford", "Claude Littner"])
s("History", ["monasteries", "Benedictines", "Cistercians"], "hard", "A Benedictine house or a Cistercian abbey?", "Benedictine", "Cistercian",
  ["Durham Cathedral Priory", "Whitby Abbey", "Westminster Abbey", "Lindisfarne Priory"], ["Fountains Abbey", "Rievaulx Abbey", "Tintern Abbey", "Furness Abbey"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-42.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
