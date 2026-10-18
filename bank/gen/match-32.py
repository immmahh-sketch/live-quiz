# Bank session 18 Oct 2026: 3 Match questions -> bank/match-32.json (strings on an instrument, desserts' home countries, sauces
# with the Sunday roast). Each topic probed against every match question in the live bank first (dips like pesto and hummus
# were already there). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Music", ["instruments", "strings"], "medium", "Match each instrument to how many strings it usually has",
  ("Violin", "4"), ("Banjo", "5"), ("Guitar", "6"), ("Concert harp", "47"))
m("Food and drink", ["desserts", "countries"], "easy", "Match each dessert to the country it comes from",
  ("Tiramisu", "Italy"), ("Apple strudel", "Austria"), ("Churros", "Spain"), ("Crème brûlée", "France"))
m("Food and drink", ["sauces", "Sunday roast"], "easy", "Match each sauce to the roast it traditionally goes with",
  ("Mint sauce", "Lamb"), ("Apple sauce", "Pork"), ("Horseradish sauce", "Beef"), ("Bread sauce", "Turkey"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-32.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
