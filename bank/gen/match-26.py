# Bank session 12 Oct 2026: 3 more Match questions -> bank/match-26.json (Girlguiding and Scouts age ranges, abbeys by county).
# Each title checked against every match question in the live bank. Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Everyday life", ["Girlguiding", "Brownies", "Guides"], "medium", "Match each Girlguiding section to its age range",
  ("Rainbows", "4 to 7"), ("Brownies", "7 to 10"), ("Guides", "10 to 14"), ("Rangers", "14 to 18"))
m("Everyday life", ["Scouts", "Cubs", "Beavers"], "medium", "Match each Scouts section to its age range",
  ("Beavers", "6 to 8"), ("Cubs", "8 to 10½"), ("Scouts", "10½ to 14"), ("Explorers", "14 to 18"))
m("History", ["abbeys", "monasteries", "counties"], "hard", "Match each ruined abbey to its county",
  ("Fountains Abbey", "North Yorkshire"), ("Tintern Abbey", "Monmouthshire"), ("Furness Abbey", "Cumbria"), ("Kirkstall Abbey", "West Yorkshire"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-26.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
