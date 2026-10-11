# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-74.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("In England's squad at the 1998 World Cup", "Football", "medium", ["England", "France 98", "World Cup"],
 ["David Seaman", "Gary Neville", "Tony Adams", "Sol Campbell", "Martin Keown", "Graeme Le Saux", "Gareth Southgate", "David Beckham", "Paul Ince", "Paul Scholes", "David Batty", "Darren Anderton", "Michael Owen", "Alan Shearer", "Teddy Sheringham"],
 ["Paul Gascoigne", "Phil Neville", "Ian Wright", "Andy Cole", "Dion Dublin"])
board("In England's squad at Euro 2004", "Football", "medium", ["England", "Euro 2004"],
 ["David James", "Gary Neville", "Sol Campbell", "John Terry", "Ashley Cole", "Jamie Carragher", "Ledley King", "David Beckham", "Steven Gerrard", "Frank Lampard", "Paul Scholes", "Owen Hargreaves", "Michael Owen", "Wayne Rooney", "Darius Vassell"],
 ["Rio Ferdinand", "Alan Shearer", "Jermain Defoe", "Jonathan Woodgate", "Teddy Sheringham"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-74.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
