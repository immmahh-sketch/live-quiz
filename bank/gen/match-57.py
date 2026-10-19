# Bank session 19 Oct 2026: 2 Match questions -> bank/match-57.json (TV dramas to their fictional villages, owls to what they're
# known for). Each topic probed against every match question in the live bank first (nothing on villages or owls; the bird-of-prey
# match uses the barn owl, so its clue here is the face, not hunting). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["TV drama", "villages", "fictional places"], "hard", "Match each TV drama to the fictional village it's set in",
  ("Heartbeat", "Aidensfield"), ("Doc Martin", "Portwenn"), ("All Creatures Great and Small", "Darrowby"), ("Hamish Macbeth", "Lochdubh"))
m("Nature", ["owls", "birds", "British wildlife"], "medium", "Match each British owl to what it's known for",
  ("Barn owl", "A white, heart-shaped face"), ("Tawny owl", "The 'twit-twoo' call"), ("Little owl", "Brought to Britain by the Victorians"),
  ("Short-eared owl", "Hunting over moorland in daylight"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-57.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
