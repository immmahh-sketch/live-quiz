# Bank session 19 Oct 2026: 2 Match questions -> bank/match-52.json (sitcoms to the building they're set in, actresses to a
# famous sitcom role). Each topic probed against every match question in the live bank first (neither was there).
# Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["sitcoms", "places"], "medium", "Match each sitcom to the building it's set in",
  ("Ghosts", "Button House"), ("To the Manor Born", "Grantleigh Manor"), ("Hi-de-Hi!", "Maplins holiday camp"), ("'Allo 'Allo!", "Café René"))
m("Comedy", ["sitcoms", "actresses"], "medium", "Match each actress to her sitcom role",
  ("Penelope Keith", "Audrey fforbes-Hamilton"), ("Wendy Craig", "Ria Parkinson"), ("Zoë Wanamaker", "Susan Harper"), ("Pauline Quirke", "Sharon Theodopolopodous"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-52.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
