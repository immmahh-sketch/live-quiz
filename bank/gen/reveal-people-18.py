# Bank session 18 Oct 2026: more Picture Reveal faces -> bank/reveal-people-18.json
# (Wikipedia title, accepted answers, difficulty). Checked against every answer in the live bank. Guessable names only: hosts of
# the game shows written up as races today. Stock with PEOPLE=bank/reveal-people-18.json node tools/reveal-stock.mjs, then
# contact-sheet them (wrong person, tiny face, small image -> RETIRED below).
import json, os
P = [
 ("Bob Holness", ["Bob Holness", "Holness"], "medium"), ("Jim Bowen", ["Jim Bowen", "Bowen"], "medium"),
 ("Bamber Gascoigne", ["Bamber Gascoigne", "Gascoigne"], "hard"), ("Magnus Magnusson", ["Magnus Magnusson", "Magnusson"], "medium"),
 ("Larry Grayson", ["Larry Grayson", "Grayson"], "hard"), ("Dale Winton", ["Dale Winton", "Winton"], "medium"),
 ("Des Lynam", ["Des Lynam", "Lynam"], "medium"), ("Andrew Flintoff", ["Freddie Flintoff", "Andrew Flintoff", "Flintoff", "Freddie"], "easy"),
 ("Michael Aspel", ["Michael Aspel", "Aspel"], "medium"), ("Richard Whiteley", ["Richard Whiteley", "Whiteley"], "medium"),
 ("Des O'Connor", ["Des O'Connor", "O'Connor"], "medium"), ("Mel Giedroyc", ["Mel Giedroyc", "Giedroyc", "Mel"], "medium"),
 ("Bob Monkhouse", ["Bob Monkhouse", "Monkhouse"], "medium"), ("Roy Walker", ["Roy Walker", "Walker"], "medium"),
 ("Matthew Kelly", ["Matthew Kelly"], "medium"), ("Nicholas Parsons", ["Nicholas Parsons", "Parsons"], "medium"),
 ("Angus Deayton", ["Angus Deayton", "Deayton"], "medium"), ("Henry Kelly", ["Henry Kelly"], "hard"),
]
# After stocking: no usable Wikipedia picture for Bob Holness, Magnus Magnusson, Larry Grayson, Dale Winton, Michael Aspel,
# Richard Whiteley, Bob Monkhouse or Matthew Kelly; Mel Giedroyc was already in. Retired from the contact sheet: Roy Walker
# (the picture was a different Roy) and Des O'Connor (a blurred 1974 stage shot).
NO_PICTURE = {"Bob Holness", "Magnus Magnusson", "Larry Grayson", "Dale Winton", "Michael Aspel", "Richard Whiteley", "Bob Monkhouse", "Matthew Kelly", "Mel Giedroyc"}
RETIRED = {"Roy Walker", "Des O'Connor"}
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
