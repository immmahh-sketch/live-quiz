# Bank session 19 Oct 2026: more Picture Reveal faces -> bank/reveal-people-20.json
# (Wikipedia title, accepted answers, difficulty). Checked against every answer in the live bank. Guessable names only: stars of
# the sitcoms written up as races today. Stock with PEOPLE=bank/reveal-people-20.json node tools/reveal-stock.mjs, then
# contact-sheet them (wrong person, tiny face, small image -> RETIRED below).
import json, os
P = [
 ("Dylan Moran", ["Dylan Moran", "Moran"], "medium"), ("Bill Bailey", ["Bill Bailey", "Bailey"], "easy"),
 ("Tamsin Greig", ["Tamsin Greig", "Greig"], "hard"), ("Toby Jones", ["Toby Jones"], "medium"),
 ("Diana Rigg", ["Diana Rigg", "Rigg"], "medium"), ("Michael Crawford", ["Michael Crawford", "Crawford", "Frank Spencer"], "medium"),
 ("Mollie Sugden", ["Mollie Sugden", "Sugden", "Mrs Slocombe"], "medium"), ("John Inman", ["John Inman", "Inman", "Mr Humphries"], "medium"),
 ("Wilfrid Brambell", ["Wilfrid Brambell", "Brambell", "Albert Steptoe"], "hard"), ("Harry H. Corbett", ["Harry H. Corbett", "Harry H Corbett", "Harry Corbett"], "hard"),
 ("Nigel Hawthorne", ["Nigel Hawthorne", "Hawthorne", "Sir Humphrey"], "hard"), ("Paul Eddington", ["Paul Eddington", "Eddington", "Jim Hacker"], "hard"),
 ("Simon Bird", ["Simon Bird", "Bird"], "medium"), ("James Buckley (actor)", ["James Buckley", "Buckley"], "medium"),
 ("Chris O'Dowd", ["Chris O'Dowd", "O'Dowd"], "medium"), ("Katherine Parkinson", ["Katherine Parkinson", "Parkinson"], "hard"),
 ("Matt Berry", ["Matt Berry", "Berry"], "medium"), ("Rebecca Front", ["Rebecca Front", "Front"], "hard"),
]
# After stocking: no usable Wikipedia picture for Mollie Sugden, John Inman, Wilfrid Brambell, Harry H. Corbett or Paul
# Eddington. Retired from the contact sheet: Dylan Moran (a tiny figure on a stage), Nigel Hawthorne (a dark, shadowy still)
# and Katherine Parkinson (face hidden behind a BAFTA mask).
NO_PICTURE = {"Mollie Sugden", "John Inman", "Wilfrid Brambell", "Harry H. Corbett", "Paul Eddington"}
RETIRED = {"Dylan Moran", "Nigel Hawthorne", "Katherine Parkinson"}
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-20.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
