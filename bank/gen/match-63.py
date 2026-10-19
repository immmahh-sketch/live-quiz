# Bank session 19 Oct 2026: 2 Match questions -> bank/match-63.json (TV drama characters to their cars, British birds to their old
# nicknames). Each topic probed against every match question in the live bank first (the detectives' wheels and sitcom transport
# matches use Morse, Vera, Magnum, Columbo, Del Boy and Mr Bean, none of them here; no bird nickname match). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["TV drama", "cars"], "medium", "Match each TV drama character to the car they're known for",
  ("Jim Bergerac", "Triumph Roadster"), ("Lovejoy", "Morris Minor"), ("Arthur Daley", "Jaguar"), ("Ray Doyle", "Ford Capri"))
m("Nature", ["birds", "names", "British wildlife"], "hard", "Match each British bird to its old country nickname",
  ("Puffin", "Sea parrot"), ("Lapwing", "Peewit"), ("Mistle thrush", "Stormcock"), ("Wren", "Jenny"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-63.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
