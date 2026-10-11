# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-71.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("In England's squad at Euro 96", "Football", "medium", ["England", "Euro 96"],
 ["David Seaman", "Gary Neville", "Stuart Pearce", "Tony Adams", "Gareth Southgate", "Sol Campbell", "Paul Ince", "Paul Gascoigne", "David Platt", "Steve McManaman", "Darren Anderton", "Jamie Redknapp", "Alan Shearer", "Teddy Sheringham", "Robbie Fowler"],
 ["Ian Wright", "Matt Le Tissier", "Peter Beardsley", "Chris Waddle", "David Beckham"])
board("In England's squad at the 2002 World Cup", "Football", "medium", ["England", "2002 World Cup"],
 ["David Seaman", "Sol Campbell", "Rio Ferdinand", "Danny Mills", "Ashley Cole", "Gareth Southgate", "David Beckham", "Paul Scholes", "Nicky Butt", "Owen Hargreaves", "Kieron Dyer", "Joe Cole", "Michael Owen", "Emile Heskey", "Teddy Sheringham"],
 ["Steven Gerrard", "Gary Neville", "Frank Lampard", "Alan Shearer", "Jamie Carragher"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-71.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
