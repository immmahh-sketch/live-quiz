# Bank session 12 Oct 2026: 2 more Put in order questions -> bank/order-37.json (Kipling works, classic animal stories).
# Each theme was checked against every order question title and
# item list in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Books", ["Kipling", "classic books"], "hard", "Put these Rudyard Kipling works in order of publication, earliest first",
  ["The Jungle Book", "Captains Courageous", "Kim", "Just So Stories", "Puck of Pook's Hill", "If—"], "earliest first")
o("Books", ["animal stories", "classic books"], "medium", "Put these classic animal stories in order of publication, earliest first",
  ["Black Beauty", "The Call of the Wild", "The Wind in the Willows", "Bambi", "Charlotte's Web", "Watership Down"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-37.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
