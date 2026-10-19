# Bank session 19 Oct 2026: 2 Match questions -> bank/match-55.json (North East actors to the detectives they played, North
# East landmarks to their towns). Each topic probed against every match question in the live bank first (detectives to actors,
# cities and cars exist with other names; North East landmarks to towns weren't there). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["North East", "detectives", "actors"], "medium", "Match each North East actor to the TV detective they played",
  ("Kevin Whately", "Lewis"), ("Brenda Blethyn", "Vera Stanhope"), ("Robson Green", "Geordie Keating"), ("Jimmy Nail", "Spender"))
m("UK geography", ["North East", "landmarks"], "easy", "Match each North East landmark to the town it's in",
  ("Angel of the North", "Gateshead"), ("Penshaw Monument", "Sunderland"), ("Transporter Bridge", "Middlesbrough"), ("St James' Park", "Newcastle"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-55.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
