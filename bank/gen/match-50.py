# Bank session 19 Oct 2026: 2 Match questions -> bank/match-50.json (sitcoms to their made-up towns, sitcom dads to their
# jobs). Each topic probed against every match question in the live bank first (only a films-to-fictional-towns set was
# there). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["sitcoms", "places"], "medium", "Match each sitcom to its made-up town",
  ("Dad's Army", "Walmington-on-Sea"), ("Hi-de-Hi!", "Crimpton-on-Sea"), ("Still Game", "Craiglang"), ("Detectorists", "Danebury"))
m("Comedy", ["sitcoms", "jobs"], "medium", "Match each sitcom character to his job",
  ("Ben Harper", "Dentist"), ("Pete Brockman", "Teacher"), ("Gary Sparrow", "TV repairman"), ("Gordon Brittas", "Leisure centre manager"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-50.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
