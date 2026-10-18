# Bank session 18 Oct 2026: 2 Categorise questions -> bank/sort-54.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (Gladiator v WWE wrestler, darts v snooker, cow v pig
# and sheep v cattle breeds exist, but not these pairs).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["Robot Wars", "Gladiators"], "medium", "A Robot Wars house robot or a Gladiator?", "Robot Wars house robot", "Gladiator",
  ["Sir Killalot", "Matilda", "Shunt", "Dead Metal"], ["Wolf", "Jet", "Shadow", "Hunter"])
s("Television", ["Tipping Point", "Deal or No Deal", "game shows"], "medium", "From Tipping Point or from Deal or No Deal?", "Tipping Point", "Deal or No Deal",
  ["Counters", "Drop zones", "Double counter", "Moving shelf"], ["The Banker", "Red boxes", "The swap", "The phone"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-54.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
