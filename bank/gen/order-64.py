# Bank session 19 Oct 2026: 3 Put in order questions -> bank/order-64.json (wildlife reintroductions, seabirds by wingspan,
# BBC One sleuth shows). Probed against every order question in the live bank first (nothing on reintroductions or seabirds; a
# Luther / Line of Duty / Broadchurch / Happy Valley order exists, so these are the older BBC One shows).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# white-tailed eagle on Rum 1975, red kite 1989, beaver at Knapdale 2009, bison in Kent 2022
o("Nature", ["rewilding", "British wildlife"], "hard", "Put these animals in the order they were brought back to the wild in Britain, earliest first",
  ["White-tailed eagle", "Red kite", "Beaver", "Bison"], "earliest first")
# about 180, 140, 107 and 55 cm
o("Nature", ["seabirds", "birds", "British wildlife"], "medium", "Rank these seabirds by wingspan, widest first",
  ["Gannet", "Herring gull", "Fulmar", "Puffin"], "widest first")
# 1979, 1981, 1986, 1996, 2003
o("Television", ["detectives", "BBC", "TV drama"], "hard", "Put these BBC One sleuth shows by start year, oldest first",
  ["Shoestring", "Bergerac", "Lovejoy", "Dalziel and Pascoe", "New Tricks"], "oldest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-64.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
