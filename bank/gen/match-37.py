# Bank session 18 Oct 2026: 2 Match questions -> bank/match-37.json (animals to their meat, comedians to the sitcoms they
# starred in). Each topic probed against every match question in the live bank first (male and female animal names were
# already there). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Food and drink", ["meat", "farm animals"], "easy", "Match each animal to the name of its meat",
  ("Pig", "Pork"), ("Cow", "Beef"), ("Deer", "Venison"), ("Sheep", "Mutton"))
m("Comedy", ["comedians", "sitcoms"], "medium", "Match each comedian to the sitcom they starred in",
  ("Richard Ayoade", "The IT Crowd"), ("David Mitchell", "Peep Show"), ("Romesh Ranganathan", "The Reluctant Landlord"), ("Steve Coogan", "I'm Alan Partridge"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-37.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
