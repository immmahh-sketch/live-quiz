# Bank session 19 Oct 2026: 2 Match questions -> bank/match-74.json (Cracker cast, Alan Partridge's world). Each topic probed against
# every match question in the live bank first (Coltrane and Coogan appear only for other roles; nothing on Cracker or Partridge's
# supporting cast). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["Cracker", "actors", "ITV"], "medium", "Match each Cracker actor to their character",
  ("Robbie Coltrane", "Fitz"), ("Geraldine Somerville", "Jane Penhaligon"), ("Lorcan Cranitch", "Jimmy Beck"), ("Christopher Eccleston", "Bilborough"))
m("Television", ["Alan Partridge", "sitcoms", "BBC"], "medium", "Match each Alan Partridge character to who they are",
  ("Alan", "Host of Knowing Me, Knowing You"), ("Lynn", "Alan's long-suffering PA"), ("Michael", "The assistant who lives in a caravan"), ("Dan Moody", "The rival who takes his radio slot"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-74.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
