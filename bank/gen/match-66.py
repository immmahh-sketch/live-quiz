# Bank session 19 Oct 2026: 2 Match questions -> bank/match-66.json (All Creatures characters to the original cast, Doctor Who actors to
# other dramas they're known for). Each topic probed against every match question in the live bank first (Doctor Who matches cover
# companions, trademarks, showrunners and Masters, not other roles; no All Creatures cast match). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["All Creatures Great and Small", "actors", "BBC"], "hard", "Match each All Creatures Great and Small character to the actor who played them in the original series",
  ("James Herriot", "Christopher Timothy"), ("Siegfried Farnon", "Robert Hardy"), ("Tristan Farnon", "Peter Davison"), ("Helen Herriot", "Carol Drinkwater"))
m("Television", ["Doctor Who", "actors", "TV drama"], "medium", "Match each Doctor Who actor to another drama he's known for",
  ("Peter Davison", "All Creatures Great and Small"), ("David Tennant", "Broadchurch"), ("Christopher Eccleston", "Our Friends in the North"), ("Matt Smith", "The Crown"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-66.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
