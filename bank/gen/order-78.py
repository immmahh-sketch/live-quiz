# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-78.json (Jodie Comer's projects, Matthew Macfadyen's projects).
# Probed against every order question in the live bank first (neither actor's career appears).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 2016, 2018, 2021, 2023
o("Film", ["Jodie Comer", "actors"], "medium", "Put these Jodie Comer projects in order of first release, earliest first",
  ["Thirteen", "Killing Eve", "Free Guy", "The Bikeriders"], "earliest first")
# 2002, 2005, 2012, 2018
o("Television", ["Matthew Macfadyen", "actors"], "medium", "Put these Matthew Macfadyen projects in order of first release, earliest first",
  ["Spooks", "Pride & Prejudice (as Mr Darcy)", "Ripper Street", "Succession"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-78.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
