# Bank session 12 Oct 2026: 3 more Match questions -> bank/match-24.json (old coins, breads by region, Anglo-Saxon kingdoms).
# Each title checked against every match question in the live bank. Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("History", ["coins", "money", "pre-decimal"], "hard", "Match each old British coin to what it was worth",
  ("Farthing", "A quarter of a penny"), ("Florin", "Two shillings"), ("Half crown", "Two shillings and sixpence"), ("Guinea", "Twenty-one shillings"))
m("Food and drink", ["bread", "British food"], "medium", "Match each bread to the part of Britain it comes from",
  ("Stottie", "The North East"), ("Barm cake", "Lancashire"), ("Farl", "Northern Ireland"), ("Bara brith", "Wales"))
m("History", ["Anglo-Saxons", "kingdoms"], "medium", "Match each Anglo-Saxon kingdom to the area it covered",
  ("Northumbria", "The north of England"), ("Mercia", "The Midlands"), ("Wessex", "The south-west"), ("East Anglia", "Norfolk and Suffolk"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-24.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
