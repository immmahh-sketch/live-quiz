# Bank session 19 Oct 2026: 4 Put in order questions -> bank/order-52.json (Graham Linehan's sitcoms, Michael Crawford's career,
# pets by lifespan, 1970s-2000s sitcoms). Probed against every order question in the live bank first (Croft's sitcoms,
# workplace sitcoms and a Greenland-shark lifespan order exist; these use different items).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Comedy", ["Graham Linehan", "sitcoms"], "easy", "Put these Graham Linehan sitcoms in order of first series, earliest first",
  ["Father Ted", "Black Books", "The IT Crowd"], "earliest first")
# 1969, 1973, 1981, 1986
o("Television", ["Michael Crawford", "career"], "hard", "Put these moments in Michael Crawford's career in order, earliest first",
  ["Hello, Dolly! (the film)", "Some Mothers Do 'Ave 'Em begins", "Barnum opens in London", "The Phantom of the Opera opens"], "earliest first")
# tortoise 80+, horse 30, cat 15, rabbit 9, hamster 2
o("Nature", ["pets", "lifespan"], "easy", "Put these pets in order of how long they usually live, longest first",
  ["Tortoise", "Horse", "Cat", "Rabbit", "Hamster"], "longest first")
# 1973, 1980, 2006, 2008
o("Comedy", ["sitcoms"], "medium", "Put these sitcoms in the order they first aired, earliest first",
  ["Some Mothers Do 'Ave 'Em", "Yes Minister", "The IT Crowd", "The Inbetweeners"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-52.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
