# Bank session 18 Oct 2026: 4 Match questions -> bank/match-33.json (Mr Men colours, peers' wives' titles, Thunderbirds pilots,
# famous bears' homes). Each topic probed against every match question in the live bank first (Thunderbirds craft to their
# jobs and Girlguiding age ranges were already there, so the pilots and bears are new angles). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Children's TV", ["Mr Men", "colours", "books"], "easy", "Match each Mr Man to his colour",
  ("Mr Happy", "Yellow"), ("Mr Tickle", "Orange"), ("Mr Bump", "Blue"), ("Mr Strong", "Red"))
m("History", ["peerage", "titles", "aristocracy"], "medium", "Match each peer to his wife's title",
  ("Duke", "Duchess"), ("Marquess", "Marchioness"), ("Earl", "Countess"), ("Viscount", "Viscountess"))
m("Children's TV", ["Thunderbirds", "Gerry Anderson", "Tracy brothers"], "medium", "Match each Thunderbird to the Tracy brother who flies it",
  ("Thunderbird 1", "Scott"), ("Thunderbird 2", "Virgil"), ("Thunderbird 3", "Alan"), ("Thunderbird 5", "John"))
m("Books", ["bears", "Paddington", "Rupert"], "easy", "Match each famous bear to where it lives",
  ("Paddington", "Darkest Peru, then London"), ("Rupert", "Nutwood"), ("Winnie-the-Pooh", "Hundred Acre Wood"), ("Yogi", "Jellystone Park"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-33.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
