# Bank session 19 Oct 2026: more Picture Reveal faces -> bank/reveal-people-25.json
# (Wikipedia title, accepted answers, difficulty). Checked against every answer in the live bank. Guessable names only: faces from
# the soap and drama races written today (Call the Midwife, Doc Martin, Brookside, Home and Away, Neighbours, The Professionals).
# Stock with PEOPLE=bank/reveal-people-25.json node tools/reveal-stock.mjs, then contact-sheet them (wrong person, tiny face, small image -> RETIRED below).
import json, os
P = [
 ("Jenny Agutter", ["Jenny Agutter", "Agutter"], "medium"), ("Pam Ferris", ["Pam Ferris", "Ferris"], "medium"),
 ("Vanessa Redgrave", ["Vanessa Redgrave", "Redgrave"], "medium"), ("Stephanie Cole", ["Stephanie Cole", "Cole"], "hard"),
 ("Isla Fisher", ["Isla Fisher", "Fisher"], "medium"), ("Melissa George", ["Melissa George"], "hard"),
 ("Guy Pearce", ["Guy Pearce", "Pearce"], "medium"), ("Anna Friel", ["Anna Friel", "Friel"], "medium"),
 ("Sue Johnston", ["Sue Johnston", "Johnston"], "medium"), ("Lewis Collins", ["Lewis Collins", "Collins"], "hard"),
 ("Gordon Jackson (actor)", ["Gordon Jackson", "Jackson"], "hard"), ("Ray Meagher", ["Ray Meagher", "Meagher"], "hard"),
 ("Kate Ritchie", ["Kate Ritchie", "Ritchie"], "hard"), ("Jessica Raine", ["Jessica Raine", "Raine"], "hard"),
 ("Caroline Catz", ["Caroline Catz", "Catz"], "hard"),
]
# After stocking: no usable Wikipedia picture for Sue Johnston, Lewis Collins or Gordon Jackson. Retired from the contact sheet:
# Jenny Agutter (a tiny 190-pixel image) and Caroline Catz (full-length shot, face too small).
NO_PICTURE = {"Sue Johnston", "Lewis Collins", "Gordon Jackson (actor)"}
RETIRED = {"Jenny Agutter", "Caroline Catz"}
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-25.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
