# Bank session 12 Oct 2026: 3 more Categorise questions -> bank/sort-36.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("The North East of England", ["shipbuilding", "Tyne", "Wear"], "hard", "A shipyard on the Tyne or on the Wear?", "Tyne", "Wear",
  ["Swan Hunter", "Hawthorn Leslie", "Palmers", "Readhead"], ["Doxford", "Austin & Pickersgill", "Short Brothers", "J.L. Thompson"])
s("Music", ["Lindisfarne", "The Police", "North East"], "medium", "A Lindisfarne song or a song by The Police?", "Lindisfarne", "The Police",
  ["Fog on the Tyne", "Meet Me on the Corner", "Lady Eleanor", "Run for Home"], ["Roxanne", "Message in a Bottle", "Every Breath You Take", "Walking on the Moon"])
s("Books", ["Catherine Cookson", "Brontë sisters", "North East"], "medium", "A Catherine Cookson novel or a Brontë novel?", "Catherine Cookson", "A Brontë",
  ["The Fifteen Streets", "The Mallen Streak", "The Cinder Path", "Tilly Trotter"], ["Jane Eyre", "Wuthering Heights", "Villette", "Agnes Grey"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-36.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
