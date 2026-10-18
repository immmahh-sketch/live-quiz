# Bank session 18 Oct 2026: 3 Match questions -> bank/match-36.json (comedians' alter egos, car models to makes, broadcasters
# to their famous parents). Each topic probed against every match question in the live bank first (car makers to countries
# and animal records were already there). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["comedians", "characters"], "easy", "Match each comedian to their famous alter ego",
  ("Paul O'Grady", "Lily Savage"), ("Barry Humphries", "Dame Edna Everage"), ("Steve Coogan", "Alan Partridge"), ("Sacha Baron Cohen", "Ali G"))
m("Everyday life", ["cars", "models"], "easy", "Match each car model to its maker",
  ("Mondeo", "Ford"), ("Corsa", "Vauxhall"), ("Golf", "Volkswagen"), ("Clio", "Renault"))
m("Television", ["broadcasters", "families"], "medium", "Match each broadcaster to their famous parent",
  ("Sally Magnusson", "Magnus Magnusson"), ("Victoria Coren Mitchell", "Alan Coren"), ("Dan Snow", "Peter Snow"), ("Jack Whitehall", "Michael Whitehall"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-36.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
