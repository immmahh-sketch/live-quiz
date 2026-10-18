# Bank session 18 Oct 2026: 3 Match questions -> bank/match-29.json (famous ships' captains, dips' main ingredients,
# UK national parks' highest points). Each topic probed against every match question in the live bank first (US national
# parks by state and explorers by fame were already there). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("History", ["ships", "explorers", "Royal Navy"], "medium", "Match each famous ship to its captain",
  ("HMS Endeavour", "James Cook"), ("HMS Beagle", "Robert FitzRoy"), ("HMS Bounty", "William Bligh"), ("Golden Hind", "Francis Drake"))
m("Food and drink", ["dips", "food"], "easy", "Match each dip to its main ingredient",
  ("Pesto", "Basil"), ("Guacamole", "Avocado"), ("Hummus", "Chickpeas"), ("Tzatziki", "Cucumber and yoghurt"))
m("UK geography", ["national parks", "mountains", "North East"], "medium", "Match each national park to its highest point",
  ("Lake District", "Scafell Pike"), ("Eryri (Snowdonia)", "Yr Wyddfa (Snowdon)"), ("Northumberland", "The Cheviot"), ("Peak District", "Kinder Scout"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-29.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
