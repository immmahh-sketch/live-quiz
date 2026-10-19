# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-72.json (British period dramas, Cillian Murphy films).
# Probed against every order question in the live bank first (Bridgerton and Austen only as siblings, novels and books; nothing on
# period TV or Murphy).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1971, 1981, 1995, 2010, 2013, 2020
o("Television", ["period dramas", "TV drama"], "medium", "Put these period dramas in order of first broadcast, earliest first",
  ["Upstairs, Downstairs", "Brideshead Revisited", "Pride and Prejudice (with Colin Firth)", "Downton Abbey", "Peaky Blinders", "Bridgerton"], "earliest first")
# 2002, 2005, 2010, 2017, 2023
o("Film", ["Cillian Murphy", "films"], "medium", "Put these Cillian Murphy films in order of release, earliest first",
  ["28 Days Later", "Batman Begins", "Inception", "Dunkirk", "Oppenheimer"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-72.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
