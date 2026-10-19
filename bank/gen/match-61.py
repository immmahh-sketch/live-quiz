# Bank session 19 Oct 2026: 2 Match questions -> bank/match-61.json (TV police shows to their stations, wild flowers to their old
# country names). Each topic probed against every match question in the live bank first (nothing on police stations or flower
# names). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["police", "TV drama"], "hard", "Match each TV police show to the station or town its officers work from",
  ("The Bill", "Sun Hill"), ("Taggart", "Maryhill"), ("Heartbeat", "Ashfordly"), ("Z-Cars", "Newtown"))
m("Nature", ["wild flowers", "British wildlife", "names"], "hard", "Match each British wild flower to its old country name",
  ("Cuckooflower", "Lady's smock"), ("Lords-and-ladies", "Cuckoo pint"), ("Bluebell", "Wild hyacinth"), ("Ox-eye daisy", "Moon daisy"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-61.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
