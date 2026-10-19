# Bank session 19 Oct 2026: 1 Match question -> bank/match-42.json (sitcom spin-offs and sequels). An animal-homes question
# (sett, holt, drey, warren) was imported too but retired straight after: two animal-homes questions were already in.
# Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["sitcoms", "spin-offs"], "medium", "Match each spin-off or sequel to the show it came from",
  ("Grace & Favour", "Are You Being Served?"), ("Max and Paddy's Road to Nowhere", "Phoenix Nights"), ("In the Loop", "The Thick of It"), ("Still Open All Hours", "Open All Hours"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-42.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
