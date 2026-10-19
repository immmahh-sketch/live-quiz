# Bank session 19 Oct 2026: 2 Match questions -> bank/match-64.json (Home and Away stars to their characters, English islands to
# their counties). Each topic probed against every match question in the live bank first (Hemsworth is already in two matches, so
# left out; the island-to-UK-nation match uses Lundy, so not here). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["Home and Away", "soaps", "actors"], "medium", "Match each Home and Away star to the character they played",
  ("Isla Fisher", "Shannon Reed"), ("Melissa George", "Angel Parrish"), ("Ray Meagher", "Alf Stewart"), ("Kate Ritchie", "Sally Fletcher"))
m("Geography", ["islands", "England", "counties"], "medium", "Match each English island to its county",
  ("Lindisfarne", "Northumberland"), ("Hayling Island", "Hampshire"), ("St Michael's Mount", "Cornwall"), ("Brownsea Island", "Dorset"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-64.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
