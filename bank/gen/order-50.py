# Bank session 18 Oct 2026: 4 Put in order questions -> bank/order-50.json (Blankety Blank and Crystal Maze hosts, big cats
# by weight, birds by wingspan). Probed against every order question in the live bank first (snooker values and the
# rainbow were already there; no big-cat or wingspan orders).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Television", ["Blankety Blank", "game shows", "hosts"], "medium", "Put these 'Blankety Blank' hosts in order, earliest first",
  ["Terry Wogan", "Les Dawson", "Lily Savage", "David Walliams", "Bradley Walsh"], "earliest first")
o("Television", ["The Crystal Maze", "game shows", "hosts"], "medium", "Put these 'Crystal Maze' hosts in order, earliest first",
  ["Richard O'Brien", "Ed Tudor-Pole", "Stephen Merchant", "Richard Ayoade"], "earliest first")
# typical big males: tiger up to 300 kg, lion 190, jaguar 100, leopard 65, cheetah 50
o("Nature", ["big cats", "animals"], "medium", "Put these big cats in order of weight, heaviest first",
  ["Tiger", "Lion", "Jaguar", "Leopard", "Cheetah"], "heaviest first")
o("Nature", ["birds", "wingspan"], "easy", "Put these birds in order of wingspan, widest first",
  ["Wandering albatross", "Mute swan", "Barn owl", "Robin"], "widest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-50.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
