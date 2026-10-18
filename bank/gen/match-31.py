# Bank session 18 Oct 2026: 3 Match questions -> bank/match-31.json (cartoon dogs' owners, zeros in big numbers, famous cats'
# owners). Each topic probed against every match question in the live bank first (fictional dogs Gromit/Snowy/Toto/Fang,
# number words like dozen and googol, and Tube line colours were already there). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Children's TV", ["cartoons", "dogs", "comics"], "easy", "Match each cartoon dog to its owner",
  ("Gnasher", "Dennis the Menace"), ("Snoopy", "Charlie Brown"), ("Scooby-Doo", "Shaggy"), ("Muttley", "Dick Dastardly"))
m("Maths and numbers", ["big numbers", "zeros"], "medium", "Match each number to how many zeros it has",
  ("Million", "6"), ("Billion", "9"), ("Trillion", "12"), ("Googol", "100"))
m("Children's TV", ["cats", "cartoons", "books"], "medium", "Match each famous cat to its owner",
  ("Garfield", "Jon Arbuckle"), ("Jess", "Postman Pat"), ("Salem", "Sabrina"), ("Mrs Norris", "Argus Filch"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-31.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
