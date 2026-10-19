# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-79.json (Steve Coogan's projects, Robbie Coltrane's roles).
# Probed against every order question in the live bank first (neither career appears).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1991, 1994, 2002, 2010, 2013
o("Television", ["Steve Coogan", "comedians"], "hard", "Put these Steve Coogan projects in order of first release, earliest first",
  ["On the Hour", "Knowing Me, Knowing You", "24 Hour Party People", "The Trip", "Philomena"], "earliest first")
# 1987, 1993, 1995, 2001
o("Film", ["Robbie Coltrane", "actors"], "medium", "Put these Robbie Coltrane roles in the order he first played them, earliest first",
  ["Tutti Frutti", "Cracker", "GoldenEye", "Harry Potter and the Philosopher's Stone"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-79.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
