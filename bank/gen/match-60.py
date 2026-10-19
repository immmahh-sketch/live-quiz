# Bank session 19 Oct 2026: 2 Match questions -> bank/match-60.json (actors to the TV detectives they played, British beetles to
# their tricks). Each topic probed against every match question in the live bank first (the detectives here aren't in the first-name
# match's set apart from Frost and Barnaby, which are asked the other way round; nothing on beetles). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["detectives", "actors", "ITV", "BBC"], "medium", "Match each actor to the TV detective he played",
  ("David Jason", "Jack Frost"), ("John Nettles", "Jim Bergerac"), ("Mark McManus", "Jim Taggart"), ("Neil Dudgeon", "John Barnaby"))
m("Nature", ["beetles", "insects", "British wildlife"], "hard", "Match each British beetle to its trick",
  ("Glow-worm", "Lights up to attract a mate"), ("Devil's coach horse", "Raises its tail like a scorpion"),
  ("Stag beetle", "Males wrestle with giant jaws"), ("Ladybird", "Oozes foul-tasting yellow fluid from its legs"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-60.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
