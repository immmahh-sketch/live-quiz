# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-72.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("In England's squad at the 2006 World Cup", "Football", "medium", ["England", "2006 World Cup"],
 ["Paul Robinson", "Gary Neville", "Jamie Carragher", "Rio Ferdinand", "John Terry", "Ashley Cole", "Sol Campbell", "Owen Hargreaves", "David Beckham", "Steven Gerrard", "Frank Lampard", "Joe Cole", "Aaron Lennon", "Wayne Rooney", "Theo Walcott"],
 ["Jermain Defoe", "Shaun Wright-Phillips", "Darren Bent", "Andy Johnson", "Scott Parker"])
board("In England's squad at the 2010 World Cup", "Football", "medium", ["England", "2010 World Cup"],
 ["David James", "Robert Green", "Joe Hart", "Glen Johnson", "Jamie Carragher", "John Terry", "Ledley King", "Ashley Cole", "Frank Lampard", "Steven Gerrard", "Gareth Barry", "James Milner", "Wayne Rooney", "Jermain Defoe", "Emile Heskey"],
 ["Theo Walcott", "David Beckham", "Darren Bent", "Adam Johnson", "Scott Parker"])
board("In England's squad at the 2014 World Cup", "Football", "medium", ["England", "2014 World Cup"],
 ["Joe Hart", "Glen Johnson", "Phil Jagielka", "Gary Cahill", "Leighton Baines", "Steven Gerrard", "Jordan Henderson", "Frank Lampard", "Jack Wilshere", "Ross Barkley", "Raheem Sterling", "Wayne Rooney", "Daniel Sturridge", "Danny Welbeck", "Rickie Lambert"],
 ["Ashley Cole", "Andy Carroll", "Jermain Defoe", "Michael Carrick", "Theo Walcott"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-72.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
