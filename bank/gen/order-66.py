# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-66.json (spring migrants by arrival, British police shows).
# Probed against every order question in the live bank first (a flowers-by-bloom order exists, but no bird arrivals; the detective
# series order uses The Sweeney, Bergerac, Morse, Prime Suspect and Midsomer, so only The Sweeney is shared).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# chiffchaff in March, swallow early April, cuckoo mid to late April, swift early May
o("Nature", ["migration", "birds", "spring"], "medium", "Put these summer visitors in the order they usually arrive in Britain in spring, earliest first",
  ["Chiffchaff", "Swallow", "Cuckoo", "Swift"], "earliest first")
# 1955, 1962, 1975, 1984, 1992
o("Television", ["police", "TV drama"], "medium", "Put these British police shows in order of first broadcast, earliest first",
  ["Dixon of Dock Green", "Z-Cars", "The Sweeney", "The Bill", "Heartbeat"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-66.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
