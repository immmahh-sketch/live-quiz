# Bank session 19 Oct 2026: 3 Categorise questions -> bank/sort-56.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (herb v spice exists; none of these pairs were there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["The Inbetweeners", "Yes Minister", "sitcoms"], "easy", "An Inbetweeners character or a Yes Minister character?", "The Inbetweeners", "Yes Minister",
  ["Will McKenzie", "Jay Cartwright", "Mr Gilbert", "Carli D'Amato"], ["Jim Hacker", "Sir Humphrey Appleby", "Bernard Woolley", "Annie Hacker"])
# peanuts ripen underground; cashews grow on trees
s("Food and drink", ["vegetables", "growing"], "medium", "Does it grow underground or above ground?", "Underground", "Above ground",
  ["Potato", "Carrot", "Peanut", "Beetroot"], ["Sweetcorn", "Peas", "Broccoli", "Cashew"])
s("Everyday life", ["newspapers"], "easy", "A red-top tabloid or a 'quality' paper?", "Red-top", "Quality paper",
  ["The Sun", "Daily Mirror", "Daily Star", "Daily Record"], ["The Times", "The Daily Telegraph", "The Guardian", "Financial Times"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-56.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
