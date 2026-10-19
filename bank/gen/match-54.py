# Bank session 19 Oct 2026: 2 Match questions -> bank/match-54.json (British birds of prey to their trademark, sitcom characters
# to their obsessions). Each topic probed against every match question in the live bank first (neither was there).
# Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Nature", ["birds of prey", "British wildlife"], "medium", "Match each bird of prey to what it's known for",
  ("Osprey", "Diving feet-first for fish"), ("Peregrine falcon", "The fastest dive of any animal"), ("Kestrel", "Hovering over roadside verges"), ("Barn owl", "Silent flight at dusk"))
m("Comedy", ["sitcoms", "hobbies"], "medium", "Match each sitcom character to their obsession",
  ("Martin Bryce", "Running local committees"), ("Tim Bisley", "Comics and video games"), ("Ben Parkinson", "Collecting butterflies"), ("Mike Watt", "The army"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-54.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
