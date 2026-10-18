# Bank session 19 Oct 2026: 2 Match questions -> bank/match-39.json (sitcom homes, 1970s sitcom characters' trades). Each topic
# probed against every match question in the live bank first (workplaces to shows and Basil/Del Boy/Brent/Ted's jobs were
# already there, so these use different pairs). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["sitcoms", "homes"], "medium", "Match each sitcom to where its main characters live",
  ("Only Fools and Horses", "Nelson Mandela House"), ("Steptoe and Son", "Oil Drum Lane"), ("Father Ted", "The Parochial House"), ("Keeping Up Appearances", "Blossom Avenue"))
m("Comedy", ["sitcoms", "jobs", "1970s"], "medium", "Match each classic sitcom character to how they earn a living",
  ("Albert Steptoe", "Rag-and-bone man"), ("Mr Humphries", "Department store assistant"), ("Captain Mainwaring", "Bank manager"), ("Tom Good", "Self-sufficient smallholder"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-39.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
