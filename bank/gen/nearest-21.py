# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-21.json: games, sports rules and numbers.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("How many wooden blocks come in a standard Jenga set?", 54, "blocks", 12, "medium", "Games and toys", False),
 ("Of the hundred Scrabble tiles, how many show an E?", 12, "tiles", 4, "hard", "Games and toys", True),
 ("How many balls start on the table in eight-ball pool, cue ball included?", 16, "balls", 3, "medium", "Sport", False),
 ("How many seconds are on the NBA shot clock?", 24, "seconds", 6, "hard", "Sport", False),
 ("Baseball fielding side: how many players?", 9, "players", 2, "medium", "Sport", False),
 ("How many syllables are there in a traditional haiku?", 17, "syllables", 4, "medium", "Words and language", False),
 ("How many lines does a limerick have?", 5, "lines", 2, "easy", "Words and language", False),
 ("Alpha to omega: how many letters?", 24, "letters", 4, "medium", "Words and language", False),
 ("How many digits make up a UK mobile phone number, starting with 07?", 11, "digits", 2, "easy", "Everyday life", False),
 ("How many digits are printed across the front of most bank cards?", 16, "digits", 3, "medium", "Everyday life", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
