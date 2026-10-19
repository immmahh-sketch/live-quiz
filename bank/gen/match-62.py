# Bank session 19 Oct 2026: 2 Match questions -> bank/match-62.json (soap clans to their soaps, Neighbours stars to their characters).
# Each topic probed against every match question in the live bank first (a sitcom-family match and a stars-to-first-soap match exist;
# no soap clan or Neighbours character match). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["soaps", "families"], "easy", "Match each soap clan to the soap it belongs to",
  ("The Dingles", "Emmerdale"), ("The Mitchells", "EastEnders"), ("The Barlows", "Coronation Street"), ("The Robinsons", "Neighbours"))
m("Television", ["Neighbours", "soaps", "actors"], "medium", "Match each Neighbours star to the character they played",
  ("Kylie Minogue", "Charlene Robinson"), ("Jason Donovan", "Scott Robinson"), ("Guy Pearce", "Mike Young"), ("Margot Robbie", "Donna Freedman"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-62.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
