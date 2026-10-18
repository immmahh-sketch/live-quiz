# Bank session 18 Oct 2026: 4 Categorise questions -> bank/sort-50.json. Two groups, three or four items each. Each pair of
# categories was probed against every Categorise question in the live bank first (Brownies v Cub Scouts words, Pooh v Wind in
# the Willows and Pooh v Beatrix Potter exist, but not these pairs).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("History", ["ranks", "Royal Navy", "British Army"], "medium", "A Royal Navy rank or a British Army rank?", "Royal Navy", "British Army",
  ["Commodore", "Rear Admiral", "Petty Officer", "Able Seaman"], ["Brigadier", "Corporal", "Lance Corporal", "Private"])
s("Everyday life", ["Girlguiding", "Scouts", "youth groups"], "easy", "A Girlguiding section or a Scouts section?", "Girlguiding", "Scouts",
  ["Rainbows", "Brownies", "Guides", "Rangers"], ["Squirrels", "Beavers", "Cubs", "Explorers"])
s("Nature", ["marsupials", "Australia", "animals"], "medium", "An Australian animal: a marsupial or not?", "Marsupial", "Not a marsupial",
  ["Kangaroo", "Koala", "Wombat", "Tasmanian devil"], ["Platypus", "Dingo", "Echidna", "Flying fox"])
s("Books", ["Paddington", "Winnie-the-Pooh", "bears"], "easy", "A Paddington character or a Winnie-the-Pooh character?", "Paddington", "Winnie-the-Pooh",
  ["Mr Brown", "Mrs Bird", "Mr Gruber", "Mr Curry"], ["Piglet", "Eeyore", "Christopher Robin", "Kanga"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-50.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
