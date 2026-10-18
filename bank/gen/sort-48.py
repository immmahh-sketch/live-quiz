# Bank session 18 Oct 2026: 3 Categorise questions -> bank/sort-48.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (the shows only appear there as items in decade sorts).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("British sitcoms", ["The Young Ones", "Dad's Army", "sitcoms"], "easy", "A character from The Young Ones or from Dad's Army?", "The Young Ones", "Dad's Army",
  ["Rik", "Vyvyan", "Neil", "Mike"], ["Mainwaring", "Pike", "Frazer", "Godfrey"])
s("British sitcoms", ["Absolutely Fabulous", "The Royle Family", "sitcoms"], "easy", "A character from Absolutely Fabulous or from The Royle Family?", "Absolutely Fabulous", "The Royle Family",
  ["Edina", "Patsy", "Saffron", "Bubble"], ["Jim", "Barbara", "Denise", "Antony"])
s("The human body", ["organs", "health"], "medium", "An organ you can live without, or one you can't?", "Can live without", "Can't live without",
  ["Appendix", "Spleen", "Gallbladder", "Tonsils"], ["Heart", "Brain", "Liver", "Skin"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-48.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
