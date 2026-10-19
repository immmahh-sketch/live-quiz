# Bank session 19 Oct 2026: 2 Match questions -> bank/match-70.json (dramas to the authors of their books, TV crime dramas to their
# writers). Each topic probed against every match question in the live bank first (Luther and Bodyguard already appear with their
# stars, so this asks for writers; no drama-to-book-author or drama-to-writer match). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["period dramas", "books", "authors"], "medium", "Match each TV drama to the author of the books it's based on",
  ("Poldark", "Winston Graham"), ("Call the Midwife", "Jennifer Worth"), ("Bridgerton", "Julia Quinn"), ("Outlander", "Diana Gabaldon"))
m("Television", ["TV drama", "writers", "BBC"], "hard", "Match each BBC drama to the writer who created it",
  ("Bodyguard", "Jed Mercurio"), ("Luther", "Neil Cross"), ("Happy Valley", "Sally Wainwright"), ("Peaky Blinders", "Steven Knight"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-70.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
