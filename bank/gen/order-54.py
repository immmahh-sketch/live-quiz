# Bank session 19 Oct 2026: 4 Put in order questions -> bank/order-54.json (Rik Mayall's career, Victoria Wood's shows,
# Scottish sitcoms, British garden birds by size). Probed against every order question in the live bank first (none of
# these were there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1982, 1986, 1987, 1991
o("Comedy", ["Rik Mayall", "career"], "hard", "Put these Rik Mayall shows in order of first appearance, earliest first",
  ["The Young Ones", "Blackadder II (as Flashheart)", "The New Statesman", "Bottom"], "earliest first")
# 1985, 1998, 2006
o("Comedy", ["Victoria Wood", "career"], "medium", "Put these Victoria Wood shows in order, earliest first",
  ["Victoria Wood: As Seen on TV", "Dinnerladies", "Housewife, 49"], "earliest first")
# 1988, 1999, 2002, 2016
o("Comedy", ["Scotland", "sitcoms"], "medium", "Put these Scottish comedies in order of first series, earliest first",
  ["Rab C. Nesbitt", "Chewin' the Fat", "Still Game", "Two Doors Down"], "earliest first")
o("Nature", ["birds", "British wildlife", "size"], "easy", "Put these British birds in order of size, smallest first",
  ["Wren", "Robin", "Blackbird", "Wood pigeon", "Mute swan"], "smallest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-54.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
