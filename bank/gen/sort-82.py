# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-82.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Crossroads or All Creatures sorts; dog breeds appear only as dog v cat and terrier
# v spaniel). Fruit on trees or bushes and sheep v cattle were drafted and dropped: both already in.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["Crossroads", "All Creatures Great and Small"], "medium", "A character from Crossroads or from All Creatures Great and Small?", "Crossroads", "All Creatures",
  ["Meg Richardson", "Benny", "Amy Turtle", "Miss Diane"], ["Siegfried Farnon", "Tristan Farnon", "Mrs Hall", "Mrs Pumphrey"])
# the Bedlington comes from Northumberland
s("Nature", ["dogs", "breeds", "Scotland", "England"], "hard", "A dog breed from Scotland or from England?", "Scotland", "England",
  ["Cairn terrier", "Skye terrier", "West Highland terrier", "Gordon setter"], ["Bedlington terrier", "Airedale terrier", "Staffordshire bull terrier", "Yorkshire terrier"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-82.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
