# Bank session 18 Oct 2026: more Picture Reveal faces -> bank/reveal-people-17.json
# (Wikipedia title, accepted answers, difficulty). Checked against every answer in the live bank. Guessable names only: stars of
# the sitcoms written up as races today. Stock with PEOPLE=bank/reveal-people-17.json node tools/reveal-stock.mjs, then
# contact-sheet them (wrong person, tiny face, small image -> RETIRED below).
import json, os
P = [
 ("Neil Morrissey", ["Neil Morrissey", "Morrissey"], "medium"), ("Caroline Quentin", ["Caroline Quentin", "Quentin"], "medium"),
 ("Leslie Ash", ["Leslie Ash", "Ash"], "medium"), ("Sue Johnston", ["Sue Johnston", "Johnston"], "medium"),
 ("Ralf Little", ["Ralf Little", "Little"], "medium"), ("Jane Horrocks", ["Jane Horrocks", "Horrocks"], "medium"),
 ("Julia Sawalha", ["Julia Sawalha", "Sawalha"], "hard"), ("Rik Mayall", ["Rik Mayall", "Mayall"], "medium"),
 ("Alexei Sayle", ["Alexei Sayle", "Sayle"], "medium"), ("Craig Charles", ["Craig Charles"], "easy"),
 ("Robert Llewellyn", ["Robert Llewellyn", "Llewellyn"], "hard"), ("Leonard Rossiter", ["Leonard Rossiter", "Rossiter"], "medium"),
 ("Frances de la Tour", ["Frances de la Tour", "de la Tour"], "hard"), ("Richard Armitage (actor)", ["Richard Armitage", "Armitage"], "medium"),
 ("Caroline Aherne", ["Caroline Aherne", "Aherne", "Mrs Merton"], "medium"), ("Arthur Lowe", ["Arthur Lowe", "Lowe"], "medium"),
 ("Clive Dunn", ["Clive Dunn", "Dunn"], "hard"), ("Ian Lavender", ["Ian Lavender", "Lavender"], "hard"),
 ("Danny John-Jules", ["Danny John-Jules", "John-Jules"], "hard"), ("Chris Barrie", ["Chris Barrie", "Barrie"], "hard"),
]
# After stocking: no usable Wikipedia picture for Leslie Ash, Sue Johnston, Jane Horrocks, Rik Mayall or Caroline Aherne;
# Neil Morrissey was already in. Retired from the contact sheet: Arthur Lowe (the picture was his signature) and Clive Dunn
# (a 1951 film still, decades before Dad's Army, unrecognisable).
NO_PICTURE = {"Leslie Ash", "Sue Johnston", "Jane Horrocks", "Rik Mayall", "Caroline Aherne", "Neil Morrissey"}
RETIRED = {"Arthur Lowe", "Clive Dunn"}
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-17.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
