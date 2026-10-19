# Bank session 19 Oct 2026: 2 Match questions -> bank/match-58.json (TV detectives to where they work, antiques shows to a presenter).
# Each topic probed against every match question in the live bank first (a detectives-to-city match uses Morse, Taggart, Rebus and
# Vera, so none of those here; nothing on antiques shows). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["detectives", "TV drama", "places"], "medium", "Match each TV detective to the place they police",
  ("Jim Bergerac", "Jersey"), ("Jimmy Pérez", "Shetland"), ("Tom Barnaby", "Causton"), ("Hamish Macbeth", "Lochdubh"))
m("Television", ["antiques", "presenters", "daytime TV"], "easy", "Match each antiques show to one of its best-known presenters",
  ("Antiques Roadshow", "Fiona Bruce"), ("Bargain Hunt", "Tim Wonnacott"), ("Flog It!", "Paul Martin"), ("Dickinson's Real Deal", "David Dickinson"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-58.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
