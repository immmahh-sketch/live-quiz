# Bank session 19 Oct 2026: 16 more Answer Smash questions written by hand -> bank/smash-2.json. Picture answers are faces stocked
# as Picture Reveals today (so their Wikipedia photos are known to be good); the clue answer starts with the last letters of the name
# (at least two letters overlap, the server's rule). Checked against every picture and clue answer already in the live bank; clue
# answers used twice or more before (Neptune, Mandarin, Ganges, Sonata, Allotment) were swapped for fresh ones.
# Lemon and Gerbil were then skipped by the server as near-duplicates of old clues, so became Lebanon and Geranium.
import json, os, re
OUT = []
def sm(picture, clue_answer, text, diff="medium", cat="Wordplay"):
    la = re.sub(r'[^a-z0-9]', '', picture.lower()); lb = re.sub(r'[^a-z0-9]', '', clue_answer.lower())
    n = next((k for k in range(min(len(la), len(lb)) - 1, 0, -1) if la[-k:] == lb[:k]), 0)
    assert n >= 2, (picture, clue_answer)
    OUT.append({"type": "smash", "text": text, "pictureAnswer": picture, "clueAnswer": clue_answer, "category": cat, "tags": ["Answer Smash"], "difficulty": diff})

sm("Pam Ferris", "Isle of Wight", "Island across the Solent from Southampton")
sm("Isla Fisher", "Herring", "Silvery fish the Scots called the 'silver darlings'")
sm("Guy Pearce", "Cereal", "Breakfast food such as cornflakes", "easy")
sm("Anna Friel", "Elephant", "The largest land animal", "easy")
sm("Ray Meagher", "Hercules", "Strongman hero of the twelve labours")
sm("Kate Ritchie", "Chief", "The head of a tribe or a fire brigade", "easy")
sm("Jessica Raine", "Nectarine", "Smooth-skinned cousin of the peach")
sm("Vanessa Redgrave", "Gravel", "Small stones on a path or drive", "easy")
sm("Dennis Waterman", "Manuscript", "A handwritten or typed draft of a book")
sm("Phyllis Logan", "Gangway", "The walkway you cross to board a ship")
sm("David Dickinson", "Sontaran", "Potato-headed alien warriors in Doctor Who", "hard")
sm("Martin Shaw", "Hawaii", "The US state made up of Pacific islands", "easy")
sm("Douglas Henshall", "Alligator", "Broad-snouted reptile of the Florida swamps")
sm("Shaun Evans", "Answer", "A reply to a question", "easy")
sm("Stephanie Cole", "Lebanon", "Country whose flag shows a cedar tree")
sm("Melissa George", "Geranium", "Pot plant with bright red flowers, also called a pelargonium")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'smash-2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'smash questions written')
