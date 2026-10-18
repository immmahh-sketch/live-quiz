# Bank session 18 Oct 2026: 4 Put in order questions -> bank/order-49.json (Price Is Right hosts, 1980s and 2000s game shows,
# primates by size). Probed against every order question in the live bank first (Bullseye and Blockbusters hosts and the
# classic quiz-show order were already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Television", ["The Price Is Right", "game shows", "hosts"], "hard", "Put these UK 'The Price Is Right' hosts in order, earliest first",
  ["Leslie Crowther", "Bob Warman", "Bruce Forsyth", "Joe Pasquale", "Alan Carr"], "earliest first")
# 1980, 1981, 1983, 1984
o("Television", ["game shows", "1980s"], "hard", "Put these 1980s game shows in order of first broadcast, earliest first",
  ["Play Your Cards Right", "Bullseye", "Blockbusters", "The Price Is Right"], "earliest first")
# 2000, 2005, 2009, 2012
o("Television", ["quiz shows", "2000s"], "medium", "Put these 21st-century teatime and evening quizzes in the order they began, earliest first",
  ["The Weakest Link", "Deal or No Deal", "Pointless", "Tipping Point"], "earliest first")
o("Nature", ["primates", "monkeys", "apes"], "easy", "Put these primates in order of size, smallest first",
  ["Marmoset", "Capuchin monkey", "Chimpanzee", "Gorilla"], "smallest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-49.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
