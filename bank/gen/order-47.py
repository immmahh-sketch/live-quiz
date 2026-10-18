# Bank session 18 Oct 2026: 5 Put in order questions -> bank/order-47.json (Girlguiding sections, degree results, Army officer
# ranks, senior Royal Navy ranks, qualifications). Probed against every order question in the live bank first (Scouts sections,
# the peerage, Army ranks Private to Captain, Navy ranks Able Seaman to Admiral, champagne bottles and moon phases were there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Everyday life", ["Girlguiding", "Brownies", "youth groups"], "easy", "Put these Girlguiding sections in age order, youngest first",
  ["Rainbows", "Brownies", "Guides", "Rangers"], "youngest first")
o("Everyday life", ["university", "degrees"], "easy", "Put these university degree results in order, best first",
  ["First", "2:1", "2:2", "Third"], "best first")
o("History", ["British Army", "ranks", "officers"], "medium", "Put these British Army officer ranks in order, most junior first",
  ["Second Lieutenant", "Lieutenant", "Captain", "Major", "Lieutenant Colonel", "Colonel", "Brigadier"], "most junior first")
o("History", ["Royal Navy", "ranks", "admirals"], "hard", "Put these senior Royal Navy ranks in order, most junior first",
  ["Captain", "Commodore", "Rear Admiral", "Vice Admiral", "Admiral", "Admiral of the Fleet"], "most junior first")
o("Everyday life", ["exams", "qualifications", "school"], "easy", "Put these qualifications in the order you'd usually gain them, earliest first",
  ["GCSE", "A level", "Bachelor's degree", "Master's degree", "Doctorate"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-47.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
