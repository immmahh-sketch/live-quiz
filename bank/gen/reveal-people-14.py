# Bank session 12 Oct 2026: more Picture Reveal faces -> bank/reveal-people-14.json
# (Wikipedia title, accepted answers, difficulty). About 200 candidates were checked against every answer already in the live
# bank and every name retired or not stocked in earlier passes; these are what was left. Mostly North East faces.
# Stock with PEOPLE=bank/reveal-people-14.json node tools/reveal-stock.mjs, then contact-sheet them.
import json, os
P = [
 # North East
 ("Steve Bruce", ["Steve Bruce", "Bruce"], "medium"), ("Jackie Milburn", ["Jackie Milburn", "Wor Jackie", "Milburn"], "hard"),
 ("Charlie Hardwick", ["Charlie Hardwick", "Hardwick"], "hard"), ("Dave Stewart (musician)", ["Dave Stewart"], "hard"),
 ("Vicky Pattison", ["Vicky Pattison", "Pattison"], "medium"), ("Charlotte Crosby", ["Charlotte Crosby", "Crosby"], "medium"),
 ("Gaz Beadle", ["Gaz Beadle", "Gary Beadle", "Beadle"], "hard"), ("Jacob Murphy (footballer)", ["Jacob Murphy"], "medium"),
 # sport
 ("Micah Richards", ["Micah Richards", "Richards"], "medium"), ("Jobe Bellingham", ["Jobe Bellingham"], "hard"),
 # TV and comedy
 ("Phillip Schofield", ["Phillip Schofield", "Schofield", "Phil Schofield"], "easy"), ("Rosie Jones (comedian)", ["Rosie Jones"], "medium"),
 ("Joe Wilkinson", ["Joe Wilkinson"], "hard"), ("Fern Brady", ["Fern Brady"], "hard"),
 # world
 ("Pope Leo XIV", ["Pope Leo XIV", "Pope Leo", "Leo XIV", "Robert Prevost"], "medium"),
]
# After stocking: no usable Wikipedia picture for Fern Brady or Charlie Hardwick, and these were retired from the contact
# sheet: Dave Stewart (the lead photo is a farmhouse), Steve Bruce and Jacob Murphy (face tiny in a crowd or action shot),
# Jackie Milburn (portrait only 175 px wide).
NO_PICTURE = {"Fern Brady", "Charlie Hardwick"}
RETIRED = {"Dave Stewart (musician)", "Steve Bruce", "Jacob Murphy (footballer)", "Jackie Milburn"}
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
