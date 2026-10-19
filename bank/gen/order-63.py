# Bank session 19 Oct 2026: 3 Put in order questions -> bank/order-63.json (owls by weight, wild deer by weight, ITV crime dramas).
# Probed against every order question in the live bank first (a British mammals by size order and a detective series order
# exist, so the wording here is kept distinct and the dramas are ITV ones from 1987 on).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# about 170 g, 300 g, 500 g, 3 kg
o("Nature", ["owls", "birds", "British wildlife"], "medium", "Rank these owls seen in Britain from lightest to heaviest",
  ["Little owl", "Barn owl", "Tawny owl", "Eagle owl"], "lightest first")
# about 15 kg, 25 kg, 60 kg, 150 kg
o("Nature", ["deer", "British wildlife"], "medium", "Rank these deer found wild in Britain from lightest to heaviest",
  ["Muntjac", "Roe deer", "Fallow deer", "Red deer"], "lightest first")
# 1987, 1992, 1997, 2002, 2011
o("Television", ["detectives", "ITV", "TV drama"], "hard", "Put these ITV crime dramas by the year they started, oldest first",
  ["Inspector Morse", "A Touch of Frost", "Midsomer Murders", "Foyle's War", "Vera"], "oldest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-63.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
