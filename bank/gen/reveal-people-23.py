# Bank session 19 Oct 2026: more Picture Reveal faces -> bank/reveal-people-23.json
# (Wikipedia title, accepted answers, difficulty). Checked against every answer in the live bank. Guessable names only: faces from
# the races, sorts and matches written today (Heartbeat, Morse, panel shows, Strictly, Taskmaster, The Tube). Stock with
# PEOPLE=bank/reveal-people-23.json node tools/reveal-stock.mjs, then contact-sheet them (wrong person, tiny face, small image -> RETIRED below).
import json, os
P = [
 ("John Thaw", ["John Thaw", "Thaw"], "medium"), ("Bill Maynard", ["Bill Maynard", "Maynard"], "hard"),
 ("Derek Fowlds", ["Derek Fowlds", "Fowlds"], "hard"), ("Nick Berry", ["Nick Berry", "Berry"], "medium"),
 ("Tricia Penrose", ["Tricia Penrose", "Penrose"], "hard"), ("Shaun Evans", ["Shaun Evans", "Evans"], "hard"),
 ("Adam Hills", ["Adam Hills", "Hills"], "medium"), ("Phill Jupitus", ["Phill Jupitus", "Phil Jupitus", "Jupitus"], "medium"),
 ("Matt Dawson", ["Matt Dawson", "Dawson"], "hard"), ("David Gower", ["David Gower", "Gower"], "hard"),
 ("Paula Yates", ["Paula Yates", "Yates"], "medium"), ("Leslie Ash", ["Leslie Ash", "Ash"], "medium"),
 ("Tony Blackburn", ["Tony Blackburn", "Blackburn"], "medium"), ("Kerry Godliman", ["Kerry Godliman", "Godliman"], "hard"),
 ("Liza Tarbuck", ["Liza Tarbuck", "Tarbuck"], "hard"), ("Kelvin Fletcher", ["Kelvin Fletcher", "Fletcher"], "medium"),
 ("Jill Halfpenny", ["Jill Halfpenny", "Halfpenny"], "medium"), ("Richard Whiteley", ["Richard Whiteley", "Whiteley"], "medium"),
 ("Ulrika Jonsson", ["Ulrika Jonsson", "Ulrika"], "easy"), ("Mark Lamarr", ["Mark Lamarr", "Lamarr"], "hard"),
]
# After stocking: no usable Wikipedia picture for John Thaw, Bill Maynard, Tricia Penrose, Paula Yates, Leslie Ash, Liza
# Tarbuck, Jill Halfpenny, Richard Whiteley, Ulrika Jonsson or Mark Lamarr. Retired from the contact sheet: David Gower (an
# old black-and-white shot that may not be him), Tony Blackburn (small, side-on at an event) and Kelvin Fletcher (blurry stage shot).
NO_PICTURE = {"John Thaw", "Bill Maynard", "Tricia Penrose", "Paula Yates", "Leslie Ash", "Liza Tarbuck", "Jill Halfpenny", "Richard Whiteley", "Ulrika Jonsson", "Mark Lamarr"}
RETIRED = {"David Gower", "Tony Blackburn", "Kelvin Fletcher"}
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-23.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
