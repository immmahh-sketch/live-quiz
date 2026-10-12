# Bank session 12 Oct 2026: 2 more Put in order questions -> bank/order-36.json (monks' daily services, the end of the Cold War).
# Each theme was checked against every order question title and
# item list in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("History", ["monks", "monasteries", "religion"], "hard", "Put these monks' services in order through the day, earliest first",
  ["Matins", "Lauds", "Terce", "Sext", "Vespers", "Compline"], "earliest first")
o("History", ["Cold War", "1980s"], "medium", "Put these events from the end of the Cold War in order, earliest first",
  ["Solidarity is founded in Poland", "Gorbachev takes power", "Chernobyl", "The INF missile treaty", "The Berlin Wall falls", "The Soviet Union breaks up"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-36.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
