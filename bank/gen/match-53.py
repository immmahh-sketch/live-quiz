# Bank session 19 Oct 2026: 2 Match questions -> bank/match-53.json (breakfast TV shows to a famous presenter,
# actors of 1970s-90s comedy to a role). Each topic probed against every match question in the live bank first (puppets to
# their partners exists; breakfast TV pairs weren't there). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["breakfast TV", "presenters"], "medium", "Match each breakfast show to a presenter it made famous",
  ("TV-am", "Roland Rat"), ("The Big Breakfast", "Chris Evans"), ("GMTV", "Eamonn Holmes"), ("Good Morning Britain", "Piers Morgan"))
m("Television", ["actors", "roles"], "medium", "Match each actor to a character they played",
  ("Judi Dench", "M"), ("Geoffrey Palmer", "Lionel Hardcastle"), ("Peter Bowles", "Richard DeVere"), ("Penelope Keith", "Margo Leadbetter"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-53.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
