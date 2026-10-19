# Bank session 19 Oct 2026: 2 Match questions -> bank/match-68.json (Sherlock cast, Sally Wainwright dramas to a star). Each topic
# probed against every match question in the live bank first (Sherlock and Happy Valley appear in a drama-to-star match, so Happy
# Valley is left out of the Wainwright one; nothing on the Sherlock cast). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["Sherlock", "actors", "BBC"], "easy", "Match each Sherlock actor to the character he played",
  ("Benedict Cumberbatch", "Sherlock Holmes"), ("Martin Freeman", "Dr John Watson"), ("Andrew Scott", "Moriarty"), ("Mark Gatiss", "Mycroft Holmes"))
m("Television", ["Sally Wainwright", "TV drama", "actors"], "hard", "Match each Sally Wainwright drama to one of its stars",
  ("Gentleman Jack", "Suranne Jones"), ("Scott & Bailey", "Lesley Sharp"), ("Last Tango in Halifax", "Anne Reid"), ("At Home with the Braithwaites", "Amanda Redman"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-68.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
