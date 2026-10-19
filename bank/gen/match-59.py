# Bank session 19 Oct 2026: 2 Match questions -> bank/match-59.json (TV right-hand men to their bosses, reintroduced animals to
# where they were released). Each topic probed against every match question in the live bank first (the detective-sidekick match
# uses Morse, Holmes, Poirot and Dalziel, so none of those here; nothing on reintroductions). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["TV drama", "detectives", "sidekicks"], "medium", "Match each TV right-hand man to the boss he worked for",
  ("Mike Jardine", "Taggart"), ("Terry McCann", "Arthur Daley"), ("Tinker", "Lovejoy"), ("Joe Ashworth", "Vera Stanhope"))
m("Nature", ["rewilding", "British wildlife"], "hard", "Match each animal brought back to Britain to where it was first released",
  ("White-tailed eagle", "Isle of Rum"), ("Beaver", "Knapdale, Argyll"), ("Bison", "West Blean Woods, Kent"), ("Red kite", "The Chilterns"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-59.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
