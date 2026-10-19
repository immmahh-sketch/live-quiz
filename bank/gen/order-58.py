# Bank session 19 Oct 2026: 3 Put in order questions -> bank/order-58.json (Man About the House and its spin-offs, panel shows
# by first series, the magpie rhyme). Probed against every order question in the live bank first (none of these were there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1973, 1976, 1977
o("Comedy", ["Man About the House", "spin-offs", "ITV"], "medium", "Put these Thames sitcoms in order of first series, earliest first",
  ["Man About the House", "George and Mildred", "Robin's Nest"], "earliest first")
# 1990, 1996, 2003, 2005, 2007
o("Comedy", ["panel shows"], "medium", "Put these panel shows in order of first series, earliest first",
  ["Have I Got News for You", "Never Mind the Buzzcocks", "QI", "Mock the Week", "Would I Lie to You?"], "earliest first")
o("Everyday life", ["magpies", "rhymes", "folklore"], "medium", "Put the lines of the magpie rhyme in order, starting with one magpie",
  ["For sorrow", "For joy", "For a girl", "For a boy", "For silver", "For gold", "For a secret never to be told"], "one magpie first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-58.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
