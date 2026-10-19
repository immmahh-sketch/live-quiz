# Bank session 19 Oct 2026: 2 Match questions -> bank/match-51.json (the magpie rhyme, comedians to the panel shows they're
# regulars on). Each topic probed against every match question in the live bank first (neither was there).
# Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Nature", ["magpies", "rhymes", "folklore"], "easy", "In the magpie rhyme, match each number of magpies to its line",
  ("One", "For sorrow"), ("Two", "For joy"), ("Three", "For a girl"), ("Four", "For a boy"))
m("Comedy", ["panel shows", "comedians"], "medium", "Match each comedian to the panel show they're a regular on",
  ("Lee Mack", "Would I Lie to You?"), ("Hugh Dennis", "Mock the Week"), ("Ian Hislop", "Have I Got News for You"), ("Alan Davies", "QI"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-51.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
