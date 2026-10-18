# Bank session 18 Oct 2026: 4 Match questions -> bank/match-28.json (David Croft sitcom settings, Gerry Anderson heroes,
# Platonic solids' faces, Big Four railways' locomotives). Each topic probed against every match question in the live bank first
# (Mallard is already in a speed-records match, so the railway one uses other engines).
# Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("British sitcoms", ["David Croft", "sitcoms"], "easy", "Match each David Croft sitcom to where it's set",
  ("Dad's Army", "Walmington-on-Sea"), ("Hi-de-Hi!", "Maplins holiday camp"), ("'Allo 'Allo!", "A café in Nouvion"), ("Are You Being Served?", "Grace Brothers department store"))
m("Television", ["Gerry Anderson", "puppets", "1960s TV"], "hard", "Match each Gerry Anderson show to its hero",
  ("Stingray", "Troy Tempest"), ("Fireball XL5", "Steve Zodiac"), ("Joe 90", "Joe McClaine"), ("Terrahawks", "Dr Tiger Ninestein"))
m("Maths and numbers", ["shapes", "geometry", "Platonic solids"], "medium", "Match each solid shape to its number of faces",
  ("Tetrahedron", "4"), ("Cube", "6"), ("Octahedron", "8"), ("Dodecahedron", "12"))
m("History", ["railways", "steam", "locomotives"], "hard", "Match each of the 'Big Four' railway companies to one of its famous engines",
  ("LNER", "Flying Scotsman"), ("GWR", "City of Truro"), ("LMS", "Royal Scot"), ("Southern", "Merchant Navy class"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-28.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
