# Bank session 19 Oct 2026: 2 Match questions -> bank/match-72.json (Life on Mars cast, Fleabag cast). Each topic probed against
# every match question in the live bank first (Fleabag appears only in a drama-to-star match; nothing on Life on Mars). Import with:
# node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["Life on Mars", "actors", "BBC"], "medium", "Match each Life on Mars actor to their character",
  ("John Simm", "Sam Tyler"), ("Philip Glenister", "Gene Hunt"), ("Liz White", "Annie Cartwright"), ("Dean Andrews", "Ray Carling"))
m("Television", ["Fleabag", "actors", "BBC"], "medium", "Match each Fleabag actor to their character",
  ("Sian Clifford", "Claire"), ("Olivia Colman", "The Godmother"), ("Andrew Scott", "The Priest"), ("Bill Paterson", "Dad"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-72.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
