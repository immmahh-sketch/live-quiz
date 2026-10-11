# Bank session 11 Oct 2026: more Categorise questions -> bank/sort-27.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})


s("Books", ["Robert Burns", "William Wordsworth", "poetry"], "medium", "A poem by Robert Burns or by William Wordsworth?", "Burns", "Wordsworth", ["Tam o' Shanter", "To a Mouse", "Auld Lang Syne", "A Red, Red Rose"], ["Daffodils", "The Prelude", "Tintern Abbey", "Composed upon Westminster Bridge"])
s("Science", ["gemstones", "colours"], "medium", "A green gemstone or a red one?", "Green", "Red", ["Emerald", "Jade", "Peridot", "Malachite"], ["Ruby", "Garnet", "Carnelian"])
s("TV", ["sitcoms", "workplaces"], "medium", "A sitcom set in a shop or in an office?", "Shop", "Office", ["Open All Hours", "Are You Being Served?", "Black Books", "Still Open All Hours"], ["The Office", "The IT Crowd", "W1A", "Drop the Dead Donkey"])
s("Football", ["Liverpool", "Everton", "managers"], "medium", "Managed Liverpool or managed Everton?", "Liverpool", "Everton", ["Bill Shankly", "Bob Paisley", "Rafael Benítez", "Jürgen Klopp"], ["Howard Kendall", "David Moyes", "Roberto Martínez", "Sean Dyche"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-27.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
