# Bank session 19 Oct 2026: 4 Put in order questions -> bank/order-55.json (John Sullivan's sitcoms, Robert Lindsay's career,
# the four UK capitals by population, four sitcoms' start dates). Probed against every order question in the live bank first (UK
# cities by population and by latitude exist; these use different sets).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1977, 1981, 1983, 1986, 2005
o("Comedy", ["John Sullivan", "sitcoms"], "hard", "Put these John Sullivan sitcoms in order of first series, earliest first",
  ["Citizen Smith", "Only Fools and Horses", "Just Good Friends", "Dear John", "The Green Green Grass"], "earliest first")
# 1977, 1985, 2000
o("Television", ["Robert Lindsay", "career"], "medium", "Put these moments in Robert Lindsay's career in order, earliest first",
  ["Citizen Smith begins", "Me and My Girl opens in the West End", "My Family begins"], "earliest first")
# London about 8.9m, Edinburgh 0.5m, Cardiff 0.37m, Belfast 0.35m
o("UK geography", ["capitals", "population"], "hard", "Put the four UK capital cities in order of population, largest first",
  ["London", "Edinburgh", "Cardiff", "Belfast"], "largest first")
# 1988, 1998, 2007, 2009
o("Comedy", ["sitcoms"], "medium", "Put these sitcoms in the order they began, earliest first",
  ["Rab C. Nesbitt", "Dinnerladies", "Benidorm", "Miranda"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-55.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
