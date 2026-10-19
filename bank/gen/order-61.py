# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-61.json (North East TV shows by first episode, 1990s music TV).
# Probed against every order question in the live bank first (a TOTP / Whistle Test / Tube / Popstars / X Factor order exists,
# so the music one uses the 1990s shows).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1964, 1976, 1983, 1989, 1996, 2011
o("Television", ["North East", "TV drama", "sitcoms"], "medium", "Put these North East TV shows in order of first episode, earliest first",
  ["The Likely Lads", "When the Boat Comes In", "Auf Wiedersehen, Pet", "Byker Grove", "Our Friends in the North", "Vera"], "earliest first")
# 1990, 1992, 1994, 1996
o("Television", ["music TV", "1990s"], "hard", "Put these music shows in order of first broadcast, earliest first",
  ["The Word", "Later... with Jools Holland", "Top of the Pops 2", "TFI Friday"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-61.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
