# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-62.json (Taskmaster champions, Bob Mortimer shows).
# Probed against every order question in the live bank first (nothing on Taskmaster or Mortimer; Sunderland and the
# reality-show winners were already well covered, so left alone).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# series 1, 4, 5, 9, 14
o("Television", ["Taskmaster", "panel shows", "comedians"], "hard", "Put these Taskmaster series champions in the order they won, earliest first",
  ["Josh Widdicombe", "Noel Fielding", "Bob Mortimer", "Ed Gamble", "Dara Ó Briain"], "earliest first")
# 1990, 1993, 2000, 2007, 2018
o("Television", ["Bob Mortimer", "comedy"], "medium", "Put these Bob Mortimer shows in order of first broadcast, earliest first",
  ["Vic Reeves Big Night Out", "Shooting Stars", "Randall & Hopkirk (Deceased)", "Would I Lie to You?", "Gone Fishing"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-62.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
