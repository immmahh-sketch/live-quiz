# Bank session 19 Oct 2026: 2 Match questions -> bank/match-65.json (Call the Midwife actresses to their characters, Yorkshire and
# North East coast villages to what they're known for). Each topic probed against every match question in the live bank first
# (nothing on Call the Midwife; only a seaside-towns-to-counties match). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["Call the Midwife", "actors", "BBC"], "medium", "Match each Call the Midwife actress to the character she played",
  ("Jenny Agutter", "Sister Julienne"), ("Pam Ferris", "Sister Evangelina"), ("Judy Parfitt", "Sister Monica Joan"), ("Miranda Hart", "Chummy"))
m("UK geography", ["coast", "North East", "Yorkshire"], "hard", "Match each coastal village or town to what it's known for",
  ("Craster", "Smoked kippers"), ("Robin Hood's Bay", "Smugglers"), ("Saltburn-by-the-Sea", "A Victorian cliff lift"), ("Cullercoats", "A colony of painters"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-65.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
