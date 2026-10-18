# Bank session 19 Oct 2026: 5 Put in order questions -> bank/order-51.json (Wheel of Fortune and Robot Wars hosts, Yes Minister's
# story, farm-animal pregnancies, eggs by size). Probed against every order question in the live bank first (a mouse-to-elephant
# pregnancy order exists, so this one uses farm animals only).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Television", ["Wheel of Fortune", "game shows", "hosts"], "medium", "Put these UK 'Wheel of Fortune' hosts in order, earliest first",
  ["Nicky Campbell", "Bradley Walsh", "John Leslie", "Graham Norton"], "earliest first")
o("Television", ["Robot Wars", "hosts"], "medium", "Put these 'Robot Wars' hosts in order, earliest first",
  ["Jeremy Clarkson", "Craig Charles", "Dara Ó Briain"], "earliest first")
# 1980, 1986, 2010, 2013
o("Television", ["Yes Minister", "sitcoms"], "hard", "Put these 'Yes Minister' milestones in order, earliest first",
  ["Yes Minister begins on BBC Two", "Yes, Prime Minister begins", "The stage play opens", "The revival on Gold"], "earliest first")
# horse about 11 months, cow 9, sheep 5, pig 4, rabbit 1
o("Nature", ["farm animals", "pregnancy"], "medium", "Put these farm animals in order of pregnancy length, longest first",
  ["Horse", "Cow", "Sheep", "Pig", "Rabbit"], "longest first")
o("Food and drink", ["eggs", "birds"], "easy", "Put these eggs in order of size, biggest first",
  ["Ostrich", "Goose", "Duck", "Hen", "Quail"], "biggest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-51.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
