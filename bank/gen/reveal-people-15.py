# Bank session 12 Oct 2026 (second pass): more Picture Reveal faces -> bank/reveal-people-15.json
# (Wikipedia title, accepted answers, difficulty). Checked against every answer in the live bank and every name retired or not
# stocked in earlier passes. Stock with PEOPLE=bank/reveal-people-15.json node tools/reveal-stock.mjs, then contact-sheet them.
import json, os
P = [
 # Newcastle United, 2025-26
 ("Tino Livramento", ["Tino Livramento", "Livramento"], "medium"), ("Lewis Hall (footballer)", ["Lewis Hall"], "medium"),
 ("Nick Woltemade", ["Nick Woltemade", "Woltemade"], "medium"), ("Yoane Wissa", ["Yoane Wissa", "Wissa"], "medium"),
 ("Malick Thiaw", ["Malick Thiaw", "Thiaw"], "hard"), ("Harvey Barnes", ["Harvey Barnes", "Barnes"], "medium"), ("Jacob Ramsey", ["Jacob Ramsey"], "hard"),
 # Sunderland, 2025-26
 ("Granit Xhaka", ["Granit Xhaka", "Xhaka"], "easy"), ("Enzo Le Fée", ["Enzo Le Fée", "Le Fée", "Le Fee"], "hard"), ("Chris Rigg", ["Chris Rigg", "Rigg"], "medium"),
 ("Wilson Isidor", ["Wilson Isidor", "Isidor"], "hard"), ("Dan Ballard", ["Dan Ballard", "Ballard"], "hard"), ("Trai Hume", ["Trai Hume", "Hume"], "hard"),
 # TV
 ("Matt Baker (presenter)", ["Matt Baker"], "medium"), ("Roman Kemp", ["Roman Kemp"], "medium"), ("Anita Rani", ["Anita Rani"], "medium"),
 ("Adrian Chiles", ["Adrian Chiles", "Chiles"], "medium"), ("Mark Chapman (presenter)", ["Mark Chapman", "Chappers"], "hard"), ("Kelly Cates", ["Kelly Cates"], "hard"),
 ("Laura Woods", ["Laura Woods"], "hard"), ("Mackenzie Crook", ["Mackenzie Crook", "Crook"], "medium"), ("Nicola Walker", ["Nicola Walker"], "medium"),
 ("Lesley Sharp", ["Lesley Sharp"], "hard"),
]
# After stocking: no usable Wikipedia picture for Tino Livramento or Kelly Cates. Retired from the contact sheet: the wrong
# person entirely (Dan Ballard: a forest-fire survey; Mark Chapman: an Oklahoma politician; Laura Woods: Laura Kurgan), action
# shots with a tiny face (Yoane Wissa, Jacob Ramsey, Granit Xhaka, Wilson Isidor), and Nicola Walker (portrait only 352 px wide).
NO_PICTURE = {"Tino Livramento", "Kelly Cates"}
RETIRED = {"Dan Ballard", "Mark Chapman (presenter)", "Laura Woods", "Yoane Wissa", "Jacob Ramsey", "Granit Xhaka", "Wilson Isidor", "Nicola Walker"}
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-15.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
