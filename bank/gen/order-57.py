# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-57.json (Brendan O'Carroll's Mrs Brown, 21st-century family
# sitcoms). Probed against every order question in the live bank first (leg-count orders
# exist; these were not there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1992 radio, 1994 novel, 1999 film, 2011 BBC
o("Comedy", ["Mrs Brown's Boys", "Brendan O'Carroll"], "hard", "Put these Mrs Brown milestones in order, earliest first",
  ["The radio series", "The first novel, The Mammy", "The film Agnes Browne", "Mrs Brown's Boys on BBC One"], "earliest first")
# 2000, 2007, 2009, 2011, 2015
o("Comedy", ["sitcoms", "2000s"], "medium", "Put these 21st-century family comedies in order of first episode, earliest first",
  ["My Family", "Outnumbered", "Miranda", "Mrs Brown's Boys", "Car Share"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-57.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
