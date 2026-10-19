# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-74.json (Olivia Colman's roles, David Tennant's roles).
# Probed against every order question in the live bank first (nothing on either actor's career).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 2003, 2013, 2018, 2019
o("Television", ["Olivia Colman", "actors"], "medium", "Put these Olivia Colman roles in the order she first played them, earliest first",
  ["Sophie in Peep Show", "Ellie Miller in Broadchurch", "Queen Anne in The Favourite", "The Queen in The Crown"], "earliest first")
# 2005, 2013, 2015, 2019
o("Television", ["David Tennant", "actors"], "medium", "Put these David Tennant roles in the order he first played them, earliest first",
  ["The Doctor in Doctor Who", "Alec Hardy in Broadchurch", "Kilgrave in Jessica Jones", "Crowley in Good Omens"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-74.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
