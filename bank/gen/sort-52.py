# Bank session 18 Oct 2026: 4 Categorise questions -> bank/sort-52.json. Two groups, three or four items each. Each pair of
# categories was probed against every Categorise question in the live bank first (mammal-or-fish and quiz-or-game-show
# exist, but not these pairs).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

# orcas and pilot whales are both members of the dolphin family
s("Nature", ["dolphins", "whales", "sea life"], "hard", "Dolphin family or whale?", "Dolphin family", "Whale",
  ["Orca", "Pilot whale", "Bottlenose", "Risso's dolphin"], ["Humpback", "Blue whale", "Sperm whale", "Minke"])
s("Television", ["catchphrases", "Bruce Forsyth", "Larry Grayson"], "medium", "A Bruce Forsyth catchphrase or a Larry Grayson one?", "Bruce Forsyth", "Larry Grayson",
  ["Nice to see you, to see you nice!", "Didn't he do well!", "Give us a twirl!"], ["Shut that door!", "Seems like a nice boy!", "Look at the muck in here!"])
s("Nature", ["Africa", "Asia", "animals"], "easy", "Found wild in Africa or in Asia?", "Africa", "Asia",
  ["Giraffe", "Hippo", "Zebra", "Gorilla"], ["Giant panda", "Orangutan", "Komodo dragon", "Red panda"])
s("Television", ["game shows", "Channel 4", "ITV"], "medium", "A Channel 4 game show or an ITV one?", "Channel 4", "ITV",
  ["Countdown", "Deal or No Deal", "The Crystal Maze", "Fifteen to One"], ["Bullseye", "Blockbusters", "The Price Is Right", "Who Wants to Be a Millionaire?"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-52.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
