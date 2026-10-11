# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-73.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("In England's squad at Euro 2012", "Football", "medium", ["England", "Euro 2012"],
 ["Joe Hart", "Glen Johnson", "John Terry", "Joleon Lescott", "Ashley Cole", "Steven Gerrard", "Scott Parker", "James Milner", "Ashley Young", "Alex Oxlade-Chamberlain", "Theo Walcott", "Wayne Rooney", "Danny Welbeck", "Andy Carroll", "Jermain Defoe"],
 ["Rio Ferdinand", "Frank Lampard", "Micah Richards", "Peter Crouch", "Daniel Sturridge"])
board("In England's squad at Euro 2016", "Football", "medium", ["England", "Euro 2016"],
 ["Joe Hart", "Kyle Walker", "Danny Rose", "Gary Cahill", "Chris Smalling", "John Stones", "Jordan Henderson", "James Milner", "Jack Wilshere", "Eric Dier", "Dele Alli", "Adam Lallana", "Raheem Sterling", "Wayne Rooney", "Marcus Rashford"],
 ["Theo Walcott", "Andros Townsend", "Danny Drinkwater", "Phil Jagielka", "Danny Welbeck"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-73.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
