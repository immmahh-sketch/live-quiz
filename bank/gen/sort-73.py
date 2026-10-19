# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-73.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Heartbeat sort; Morse only in detective-nationality and setting sorts; no
# winter-visitor bird sort).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["Heartbeat", "Inspector Morse", "ITV"], "medium", "A character from Heartbeat or from Inspector Morse?", "Heartbeat", "Inspector Morse",
  ["Claude Greengrass", "Oscar Blaketon", "Gina Ward", "Alf Ventress"], ["Robbie Lewis", "Chief Superintendent Strange", "Max DeBryn", "Laura Hobson"])
# redwing, fieldfare, waxwing and brambling come from Scandinavia for the winter (a handful of redwings breed in Scotland)
s("Nature", ["birds", "migration", "British wildlife"], "hard", "A bird that breeds in Britain, or one that mostly just visits for the winter?", "Breeds here", "Winter visitor",
  ["Robin", "Swallow", "Puffin", "Wren"], ["Redwing", "Fieldfare", "Waxwing", "Brambling"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-73.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
