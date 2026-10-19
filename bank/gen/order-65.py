# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-65.json (David Jason's characters, Midsomer Murders sergeants).
# Probed against every order question in the live bank first (nothing on David Jason or Midsomer; national parks already in).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# Open All Hours pilot 1973, Only Fools 1981, The Darling Buds of May 1991, A Touch of Frost 1992
o("Television", ["David Jason", "sitcoms", "TV drama"], "medium", "Put these David Jason characters in the order he first played them",
  ["Granville", "Del Boy", "Pop Larkin", "Jack Frost"], "earliest first")
# Troy 1997, Scott 2004, Jones 2005, Nelson 2013, Winter 2016
o("Television", ["Midsomer Murders", "detectives", "ITV"], "hard", "Put these Midsomer Murders sergeants in the order they joined, earliest first",
  ["Gavin Troy", "Dan Scott", "Ben Jones", "Charlie Nelson", "Jamie Winter"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-65.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
