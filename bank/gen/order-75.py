# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-75.json (Idris Elba's roles, Richard Madden's roles).
# Probed against every order question in the live bank first (nothing on either actor's career; Jed Mercurio's dramas already in).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 2002, 2010, 2011, 2013
o("Film", ["Idris Elba", "actors"], "medium", "Put these Idris Elba roles in the order he first played them, earliest first",
  ["Stringer Bell in The Wire", "John Luther in Luther", "Heimdall in Thor", "Nelson Mandela in Long Walk to Freedom"], "earliest first")
# 2011, 2015, 2018, 2021
o("Film", ["Richard Madden", "actors"], "medium", "Put these Richard Madden roles in the order he first played them, earliest first",
  ["Robb Stark in Game of Thrones", "Prince Kit in Cinderella", "David Budd in Bodyguard", "Ikaris in Eternals"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-75.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
