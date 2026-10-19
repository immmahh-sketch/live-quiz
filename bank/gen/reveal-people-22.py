# Bank session 19 Oct 2026: more Picture Reveal faces -> bank/reveal-people-22.json
# (Wikipedia title, accepted answers, difficulty). Checked against every answer in the live bank. Guessable names only: stars of
# the sitcoms written up as races today and last night. Stock with PEOPLE=bank/reveal-people-22.json node tools/reveal-stock.mjs, then
# contact-sheet them (wrong person, tiny face, small image -> RETIRED below).
import json, os
P = [
 ("Peter Bowles", ["Peter Bowles", "Bowles"], "hard"), ("Wendy Craig", ["Wendy Craig"], "hard"),
 ("Geoffrey Palmer", ["Geoffrey Palmer", "Palmer"], "medium"), ("Zoë Wanamaker", ["Zoë Wanamaker", "Zoe Wanamaker", "Wanamaker"], "medium"),
 ("Kris Marshall", ["Kris Marshall", "Marshall"], "medium"), ("Hugh Dennis", ["Hugh Dennis", "Dennis"], "medium"),
 ("Claire Skinner", ["Claire Skinner", "Skinner"], "hard"), ("Paul Ritter (actor)", ["Paul Ritter", "Ritter"], "hard"),
 ("Mark Heap", ["Mark Heap", "Heap"], "hard"), ("Jean Boht", ["Jean Boht", "Boht"], "hard"),
 ("Pauline Quirke", ["Pauline Quirke", "Quirke"], "medium"), ("Linda Robson", ["Linda Robson", "Robson"], "medium"),
 ("Nicholas Lyndhurst", ["Nicholas Lyndhurst", "Lyndhurst"], "medium"), ("Dervla Kirwan", ["Dervla Kirwan", "Kirwan"], "hard"),
 ("Richard O'Sullivan", ["Richard O'Sullivan", "O'Sullivan"], "hard"), ("Paula Wilcox", ["Paula Wilcox", "Wilcox"], "hard"),
 ("Brian Murphy (actor)", ["Brian Murphy", "Murphy"], "hard"), ("Sian Gibson", ["Sian Gibson", "Gibson"], "medium"),
]
# After stocking: no usable Wikipedia picture for Wendy Craig, Claire Skinner, Paul Ritter, Pauline Quirke, Nicholas
# Lyndhurst, Richard O'Sullivan, Paula Wilcox or Brian Murphy. Retired from the contact sheet: Geoffrey Palmer (the picture
# was a 17th-century portrait of a different Geoffrey Palmer) and Hugh Dennis (bearded, at a lectern, hard to recognise).
NO_PICTURE = {"Wendy Craig", "Claire Skinner", "Paul Ritter (actor)", "Pauline Quirke", "Nicholas Lyndhurst", "Richard O'Sullivan", "Paula Wilcox", "Brian Murphy (actor)"}
RETIRED = {"Geoffrey Palmer", "Hugh Dennis"}
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-22.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
