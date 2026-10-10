# Bank session 10 Oct 2026: more Nearest Wins questions -> bank/nearest-8.json, mostly Britain and sport.
# (text, answer, unit, spread, difficulty, category, wow). Each was checked against the live bank's wording first.
import json, os
Q = [
 ("How many steps are there from the floor of St Paul's Cathedral up to the Golden Gallery at the top of the dome?", 528, "steps", 250, "hard", "Places", False),
 ("How tall is Nelson's Column, including Nelson, to the nearest metre?", 52, "metres", 25, "hard", "Places", False),
 ("Roughly how many people can the Royal Albert Hall seat, to the nearest 100?", 5300, "seats", 2500, "hard", "Places", False),
 ("Roughly how many rooms are there in the Palace of Westminster, to the nearest 100?", 1100, "rooms", 600, "hard", "Places", True),
 ("Roughly how many islands does Scotland have, to the nearest 100?", 800, "islands", 400, "hard", "Scotland", True),
 ("How deep is Loch Ness at its deepest, to the nearest 10 metres?", 230, "metres", 120, "hard", "Scotland", False),
 ("The first Severn Bridge, between England and Wales, opened in which year?", 1966, "", 15, "medium", "Britain", False),
 ("The first stretch of the M1 motorway opened in which year?", 1959, "", 15, "medium", "Britain", False),
 ("How many medals did Team GB win in total at the Paris 2024 Olympics?", 65, "medals", 25, "medium", "Sport", False),
 ("How many gold medals did Team GB win at the London 2012 Olympics?", 29, "golds", 12, "medium", "Sport", False),
 ("How many countries took part in the first modern Olympics, in Athens in 1896?", 14, "countries", 10, "hard", "Sport", True),
 ("How many players are there in a hurling team?", 15, "players", 6, "medium", "Sport", False),
 ("Roughly how many centimetres is it round a full-size football?", 70, "cm", 30, "hard", "Football", False),
 ("Roughly how much does a men's cricket ball weigh, to the nearest 10 grams?", 160, "grams", 80, "hard", "Cricket", False),
 ("How many stitches are there on an official Major League baseball?", 108, "stitches", 60, "hard", "Sport", True),
 ("Roughly how long is the Bayeux Tapestry, to the nearest metre?", 70, "metres", 35, "hard", "History", True),
 ("Robert the Bruce beat the English at Bannockburn in which year?", 1314, "", 50, "hard", "Scotland", False),
 ("The Battle of Culloden, the last pitched battle on British soil, was fought in which year?", 1746, "", 40, "medium", "Scotland", False),
 ("According to the 2021 census, how many million people live in Wales, to one decimal place?", 3.1, "million", 1.5, "medium", "Wales", False),
 ("According to the 2021 census, how many million people live in Northern Ireland, to one decimal place?", 1.9, "million", 1, "medium", "Britain", False),
 ("According to the 2021 census, how many million people live in England, to the nearest million?", 57, "million", 15, "medium", "Britain", False),
 ("How many stations does the Elizabeth line serve?", 41, "stations", 20, "hard", "London", False),
 ("How tall is Blackpool Tower, to the nearest metre?", 158, "metres", 70, "medium", "Places", False),
 ("How tall is Portsmouth's Spinnaker Tower, to the nearest 10 metres?", 170, "metres", 80, "hard", "Places", False),
 ("How many steps are there up the Monument to the Great Fire of London?", 311, "steps", 150, "hard", "London", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
