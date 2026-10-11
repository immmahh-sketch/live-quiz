# Bank session 11 Oct 2026 (eighth pass): more Picture Reveal faces -> bank/reveal-people-9.json
# (Wikipedia title, accepted answers, difficulty). Each name was checked against every answer already in the live bank.
# Stock with PEOPLE=bank/reveal-people-9.json node tools/reveal-stock.mjs, then contact-sheet them.
import json, os
P = [
 # sport
 ("Harry Brook", ["Harry Brook", "Brook"], "hard"), ("Jos Buttler", ["Jos Buttler", "Buttler"], "medium"), ("Jofra Archer", ["Jofra Archer", "Archer"], "medium"),
 ("Oscar Piastri", ["Oscar Piastri", "Piastri"], "hard"), ("Charles Leclerc", ["Charles Leclerc", "Leclerc"], "medium"), ("Carlos Sainz Jr.", ["Carlos Sainz", "Sainz"], "hard"),
 ("Toto Wolff", ["Toto Wolff", "Wolff"], "medium"), ("Christian Horner", ["Christian Horner", "Horner"], "medium"),
 ("Jack Draper", ["Jack Draper", "Draper"], "hard"), ("Cameron Norrie", ["Cameron Norrie", "Norrie"], "hard"), ("Katie Boulter", ["Katie Boulter", "Boulter"], "hard"),
 ("Jannik Sinner", ["Jannik Sinner", "Sinner"], "medium"), ("Carlos Alcaraz", ["Carlos Alcaraz", "Alcaraz"], "medium"), ("Coco Gauff", ["Coco Gauff", "Gauff"], "medium"),
 ("Aryna Sabalenka", ["Aryna Sabalenka", "Sabalenka"], "hard"), ("Iga Świątek", ["Iga Swiatek", "Iga Świątek", "Swiatek"], "hard"),
 ("Gerwyn Price", ["Gerwyn Price"], "hard"), ("Josh Kerr", ["Josh Kerr"], "hard"), ("Katarina Johnson-Thompson", ["Katarina Johnson-Thompson", "KJT"], "medium"),
 ("Tom Pidcock", ["Tom Pidcock", "Pidcock"], "hard"), ("Chris Froome", ["Chris Froome", "Froome"], "medium"), ("Jason Kenny", ["Jason Kenny"], "medium"),
 ("Duncan Scott (swimmer)", ["Duncan Scott"], "hard"), ("Bruno Fernandes", ["Bruno Fernandes", "Fernandes"], "medium"), ("Martin Ødegaard", ["Martin Odegaard", "Martin Ødegaard", "Odegaard"], "medium"),
 ("Mikel Arteta", ["Mikel Arteta", "Arteta"], "medium"), ("Jürgen Klopp", ["Jurgen Klopp", "Jürgen Klopp", "Klopp"], "easy"), ("Thomas Tuchel", ["Thomas Tuchel", "Tuchel"], "medium"),
 ("Alessia Russo", ["Alessia Russo", "Russo"], "medium"), ("Beth Mead", ["Beth Mead", "Mead"], "medium"),
 # screen and music
 ("Timothée Chalamet", ["Timothee Chalamet", "Timothée Chalamet", "Chalamet"], "medium"), ("Riz Ahmed", ["Riz Ahmed"], "medium"), ("Aimee Lou Wood", ["Aimee Lou Wood"], "hard"),
 ("Jacob Elordi", ["Jacob Elordi", "Elordi"], "hard"), ("Chappell Roan", ["Chappell Roan"], "hard"), ("Yungblud", ["Yungblud", "Dominic Harrison"], "hard"),
 # TV and politics
 ("Kemi Badenoch", ["Kemi Badenoch", "Badenoch"], "medium"), ("Rachel Reeves", ["Rachel Reeves", "Reeves"], "medium"), ("Ken Bruce", ["Ken Bruce"], "medium"),
 ("James May", ["James May"], "easy"), ("Richard Hammond", ["Richard Hammond", "Hammond"], "easy"), ("Phil Spencer (television presenter)", ["Phil Spencer"], "medium"),
 ("Monica Galetti", ["Monica Galetti", "Galetti"], "medium"), ("Katherine Ryan", ["Katherine Ryan"], "medium"), ("Tom Allen (comedian)", ["Tom Allen"], "medium"),
]
# After stocking: Klopp and Chalamet were already in the bank under their accented names, Elordi had no usable photo,
# and these were retired from the contact sheet (action shots, caps, goggles or faces too small to read).
ALREADY = {"Jürgen Klopp", "Timothée Chalamet"}
NO_PHOTO = {"Jacob Elordi"}
RETIRED = {"Chris Froome", "Duncan Scott (swimmer)", "Harry Brook", "Iga Świątek", "Jack Draper", "Katie Boulter", "Mikel Arteta",
           "Monica Galetti", "Tom Pidcock", "Cameron Norrie"}
P = [p for p in P if p[0] not in ALREADY | NO_PHOTO | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-9.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
