# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-73.json (Benedict Cumberbatch's roles, Martin Freeman's roles).
# Probed against every order question in the live bank first (a screen-Holmeses order exists; nothing on either actor's career).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 2010, 2013, 2014, 2016
o("Film", ["Benedict Cumberbatch", "actors"], "medium", "Put these Benedict Cumberbatch roles in the order he first played them, earliest first",
  ["Sherlock Holmes in Sherlock", "Smaug in The Hobbit", "Alan Turing in The Imitation Game", "Doctor Strange"], "earliest first")
# 2001, 2005, 2010, 2012
o("Film", ["Martin Freeman", "actors"], "medium", "Put these Martin Freeman roles in the order he first played them, earliest first",
  ["Tim in The Office", "Arthur Dent in The Hitchhiker's Guide to the Galaxy", "Dr Watson in Sherlock", "Bilbo Baggins in The Hobbit"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-73.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
