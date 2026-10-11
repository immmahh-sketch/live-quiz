# Bank session 11 Oct 2026 (eleventh pass): more Picture Reveal faces -> bank/reveal-people-12.json
# (Wikipedia title, accepted answers, difficulty). Each name was checked against every answer already in the live bank
# and every name retired or not stocked in earlier passes. Stock with PEOPLE=bank/reveal-people-12.json node tools/reveal-stock.mjs, then contact-sheet them.
import json, os
P = [
 # football
 ("Gareth Bale", ["Gareth Bale", "Bale"], "easy"), ("Ange Postecoglou", ["Ange Postecoglou", "Postecoglou"], "medium"), ("Arne Slot", ["Arne Slot", "Slot"], "medium"),
 ("Enzo Maresca", ["Enzo Maresca", "Maresca"], "hard"), ("Unai Emery", ["Unai Emery", "Emery"], "medium"), ("Thomas Frank (footballer)", ["Thomas Frank"], "hard"),
 ("Robert Lewandowski", ["Robert Lewandowski", "Lewandowski"], "medium"), ("Rodri (footballer, born 1996)", ["Rodri", "Rodrigo Hernández"], "medium"), ("Martin Ødegaard", ["Martin Odegaard", "Martin Ødegaard", "Odegaard", "Ødegaard"], "medium"),
 ("Ella Toone", ["Ella Toone", "Toone"], "medium"), ("Georgia Stanway", ["Georgia Stanway", "Stanway"], "hard"), ("Lauren James (footballer)", ["Lauren James"], "medium"),
 ("Beth England", ["Beth England"], "hard"),
 # other sport
 ("Fernando Alonso", ["Fernando Alonso", "Alonso"], "medium"), ("Scottie Scheffler", ["Scottie Scheffler", "Scheffler"], "hard"), ("Chris Eubank Jr.", ["Chris Eubank Jr", "Chris Eubank Junior", "Eubank Jr"], "medium"),
 # TV
 ("Stephen Merchant", ["Stephen Merchant", "Merchant"], "medium"), ("Nick Knowles", ["Nick Knowles", "Knowles"], "medium"), ("Dan Snow", ["Dan Snow"], "medium"),
 ("Lucy Worsley", ["Lucy Worsley", "Worsley"], "medium"), ("Tony Robinson", ["Tony Robinson", "Sir Tony Robinson", "Baldrick"], "easy"), ("Michael Portillo", ["Michael Portillo", "Portillo"], "medium"),
 ("Derrick Evans", ["Mr Motivator", "Derrick Evans"], "medium"), ("Peter Andre", ["Peter Andre"], "easy"), ("Kelly Osbourne", ["Kelly Osbourne"], "medium"),
]
# After stocking: names skipped as already in the bank or with no usable photo, and those retired from the contact sheet.
ALREADY = {"Chris Eubank Jr."}  # no usable Wikipedia picture
RETIRED = {"Enzo Maresca", "Lauren James (footballer)", "Derrick Evans", "Thomas Frank (footballer)"}  # crowd/action shots, a sign instead of Mr Motivator, and an old photo of a different Thomas Frank
P = [p for p in P if p[0] not in ALREADY | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-12.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
