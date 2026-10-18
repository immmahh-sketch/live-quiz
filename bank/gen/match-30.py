# Bank session 18 Oct 2026: 3 Match questions -> bank/match-30.json (organs' jobs, Shakespeare villains, steam engines'
# designers). Each topic probed against every match question in the live bank first (vitamins, cheeses and organs by body
# system were already there; Shylock is in a character-to-play match, so he is left out).
# Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("The human body", ["organs", "biology"], "medium", "Match each organ to one of its jobs",
  ("Liver", "Makes bile"), ("Kidneys", "Filter blood to make urine"), ("Pancreas", "Makes insulin"), ("Spleen", "Clears out old red blood cells"))
m("Shakespeare", ["villains", "plays"], "medium", "Match each Shakespeare villain to the play they're in",
  ("Iago", "Othello"), ("Lady Macbeth", "Macbeth"), ("Edmund", "King Lear"), ("Tybalt", "Romeo and Juliet"))
m("History", ["steam", "railways", "engineers"], "hard", "Match each famous steam engine to the engineer behind it",
  ("Rocket", "Robert Stephenson"), ("Mallard", "Nigel Gresley"), ("City of Truro", "George Jackson Churchward"), ("Evening Star", "Robert Riddles"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-30.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
