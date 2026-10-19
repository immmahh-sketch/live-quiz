# Bank session 19 Oct 2026: more Picture Reveal faces -> bank/reveal-people-21.json
# (Wikipedia title, accepted answers, difficulty). Checked against every answer in the live bank. Guessable names only: stars of
# the sitcoms written up as races today and last night. Stock with PEOPLE=bank/reveal-people-21.json node tools/reveal-stock.mjs, then
# contact-sheet them (wrong person, tiny face, small image -> RETIRED below).
import json, os
P = [
 ("Tom Ellis (actor)", ["Tom Ellis", "Ellis"], "medium"), ("Patricia Hodge", ["Patricia Hodge", "Hodge"], "hard"),
 ("Robert Lindsay", ["Robert Lindsay", "Lindsay"], "medium"), ("Gregor Fisher", ["Gregor Fisher", "Fisher", "Rab C. Nesbitt"], "medium"),
 ("Elaine C. Smith", ["Elaine C. Smith", "Elaine C Smith", "Elaine Smith"], "hard"), ("Ford Kiernan", ["Ford Kiernan", "Kiernan"], "medium"),
 ("Greg Hemphill", ["Greg Hemphill", "Hemphill"], "medium"), ("Maxine Peake", ["Maxine Peake", "Peake"], "medium"),
 ("Celia Imrie", ["Celia Imrie", "Imrie"], "medium"), ("Anne Reid", ["Anne Reid", "Reid"], "hard"),
 ("Charlotte Ritchie", ["Charlotte Ritchie", "Ritchie"], "medium"), ("Mathew Baynton", ["Mathew Baynton", "Matthew Baynton", "Baynton"], "hard"),
 ("Simon Farnaby", ["Simon Farnaby", "Farnaby"], "hard"), ("Steve Pemberton", ["Steve Pemberton", "Pemberton"], "medium"),
 ("Armando Iannucci", ["Armando Iannucci", "Iannucci"], "hard"), ("Brendan O'Carroll", ["Brendan O'Carroll", "O'Carroll", "Mrs Brown"], "medium"),
 ("Frankie Boyle", ["Frankie Boyle", "Boyle"], "medium"), ("Limmy", ["Limmy", "Brian Limond"], "medium"),
]
# After stocking: no usable Wikipedia picture for Patricia Hodge, Gregor Fisher, Ford Kiernan, Greg Hemphill or Charlotte
# Ritchie. Retired from the contact sheet: Robert Lindsay (the picture was an old oil painting of a different man).
NO_PICTURE = {"Patricia Hodge", "Gregor Fisher", "Ford Kiernan", "Greg Hemphill", "Charlotte Ritchie"}
RETIRED = {"Robert Lindsay"}
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
