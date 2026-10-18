# Bank session 18 Oct 2026: 6 Put in order questions -> bank/order-48.json (Bullseye, Generation Game and Blockbusters hosts,
# the Paddington films, sleepy animals, Richard Osman's milestones). Probed against every order question in the live bank first
# (Countdown and Mastermind hosts, Gerry Anderson shows and Blackadder series were already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Television", ["Bullseye", "game shows", "hosts"], "easy", "Put these 'Bullseye' hosts in order, earliest first",
  ["Jim Bowen", "Dave Spikey", "Freddie Flintoff"], "earliest first")
o("Television", ["The Generation Game", "game shows", "hosts"], "medium", "Put these 'Generation Game' hosts in order of their first series, earliest first",
  ["Bruce Forsyth", "Larry Grayson", "Jim Davidson", "Mel and Sue"], "earliest first")
o("Television", ["Blockbusters", "game shows", "hosts"], "hard", "Put these 'Blockbusters' hosts in order, earliest first",
  ["Bob Holness", "Michael Aspel", "Simon Mayo", "Dara Ó Briain"], "earliest first")
o("Film", ["Paddington", "films"], "easy", "Put the Paddington films in order of release, earliest first",
  ["Paddington", "Paddington 2", "Paddington in Peru"], "earliest first")
# koala about 20 hours, cat about 15, people about 8, giraffe about 2
o("Nature", ["sleep", "animals"], "medium", "Put these in order of how many hours they sleep a day, longest first",
  ["Koala", "Cat", "Human", "Giraffe"], "longest first")
o("Television", ["Richard Osman", "Pointless", "books"], "medium", "Put these Richard Osman milestones in order, earliest first",
  ["Pointless begins", "Richard Osman's House of Games begins", "The Thursday Murder Club is published", "The Thursday Murder Club film comes out"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-48.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
