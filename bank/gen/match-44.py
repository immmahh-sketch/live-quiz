# Bank session 19 Oct 2026: 2 Match questions -> bank/match-44.json (the Ghosts of Button House to their eras, sitcoms to who
# sang their theme). Each topic probed against every match question in the live bank first (none of these pairs were there).
# Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["Ghosts", "history"], "medium", "Match each Ghosts character to the time they died in",
  ("Robin", "The Stone Age"), ("The Captain", "The Second World War"), ("Fanny", "The Edwardian era"), ("Julian", "The 1990s"))
m("Comedy", ["sitcoms", "theme tunes"], "hard", "Match each sitcom to who sang its theme",
  ("Only Fools and Horses", "John Sullivan"), ("The Royle Family", "Oasis"), ("Detectorists", "Johnny Flynn"), ("Auf Wiedersehen, Pet", "Joe Fagin"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-44.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
