# Bank session 11 Oct 2026 (tenth pass): more Picture Reveal faces -> bank/reveal-people-11.json
# (Wikipedia title, accepted answers, difficulty). Each name was checked against every answer already in the live bank
# and every name retired or not stocked in earlier passes. Stock with PEOPLE=bank/reveal-people-11.json node tools/reveal-stock.mjs, then contact-sheet them.
import json, os
P = [
 # TV and comedy
 ("Gaby Roslin", ["Gaby Roslin"], "medium"), ("Reggie Yates", ["Reggie Yates"], "medium"), ("Stacey Dooley", ["Stacey Dooley", "Dooley"], "medium"),
 ("Nish Kumar", ["Nish Kumar"], "medium"), ("Sean Lock", ["Sean Lock"], "medium"), ("Tim Vine", ["Tim Vine"], "medium"),
 ("John Bishop (comedian)", ["John Bishop"], "medium"), ("Alan Davies", ["Alan Davies"], "medium"), ("Rose Matafeo", ["Rose Matafeo", "Matafeo"], "hard"),
 ("Jamali Maddix", ["Jamali Maddix"], "hard"), ("Guz Khan", ["Guz Khan"], "hard"), ("Big Zuu", ["Big Zuu"], "hard"),
 ("Joe Swash", ["Joe Swash"], "medium"), ("Gloria Hunniford", ["Gloria Hunniford"], "medium"), ("Darragh Ennis", ["Darragh Ennis", "The Menace"], "medium"),
 # music
 ("Jamie Cullum", ["Jamie Cullum"], "medium"), ("Gareth Gates", ["Gareth Gates"], "medium"), ("Matt Cardle", ["Matt Cardle"], "medium"),
 ("Ella Henderson", ["Ella Henderson"], "hard"), ("Kian Egan", ["Kian Egan"], "hard"),
 # sport
 ("Lawrence Dallaglio", ["Lawrence Dallaglio", "Dallaglio"], "medium"), ("Jason Robinson (rugby)", ["Jason Robinson"], "medium"), ("Courtney Lawes", ["Courtney Lawes", "Lawes"], "hard"),
 ("Graeme Swann", ["Graeme Swann", "Swann"], "medium"), ("Andrew Strauss", ["Andrew Strauss", "Strauss"], "medium"), ("Michael Vaughan", ["Michael Vaughan", "Vaughan"], "medium"),
 ("Nasser Hussain", ["Nasser Hussain", "Hussain"], "medium"), ("Michael Atherton", ["Michael Atherton", "Mike Atherton", "Atherton"], "medium"), ("Zak Crawley", ["Zak Crawley", "Crawley"], "hard"),
 ("Ollie Pope", ["Ollie Pope"], "hard"), ("Mason Mount", ["Mason Mount", "Mount"], "medium"),
 ("Dan Burn", ["Dan Burn", "Burn"], "easy"), ("Callum Wilson (footballer, born 1992)", ["Callum Wilson"], "easy"), ("Allan Saint-Maximin", ["Allan Saint-Maximin", "Saint-Maximin", "ASM"], "easy"),
 ("Miguel Almirón", ["Miguel Almiron", "Miguel Almirón", "Almiron", "Almirón"], "easy"), ("Fabian Schär", ["Fabian Schar", "Fabian Schär", "Schar", "Schär"], "easy"), ("Sven Botman", ["Sven Botman", "Botman"], "easy"),
]
# After stocking: names skipped as already in the bank or with no usable photo, and those retired from the contact sheet.
ALREADY = {"Gaby Roslin", "Jamali Maddix", "Joe Swash", "Darragh Ennis"}  # no usable Wikipedia picture
RETIRED = {"Courtney Lawes", "Dan Burn", "Ella Henderson", "Jamie Cullum", "Nish Kumar", "Ollie Pope", "Sean Lock", "Zak Crawley"}  # action, stage or sunglasses shots
P = [p for p in P if p[0] not in ALREADY | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
