# Bank session 10 Oct 2026: more Nearest Wins questions -> bank/nearest-9.json, famous structures around the world.
# (text, answer, unit, spread, difficulty, category, wow). Each was checked against the live bank's wording first.
import json, os
Q = [
 ("San Francisco's Golden Gate Bridge opened in which year?", 1937, "", 20, "medium", "Places", False),
 ("How tall are the Golden Gate Bridge's towers, to the nearest metre?", 227, "metres", 100, "hard", "Places", False),
 ("The Sydney Harbour Bridge opened in which year?", 1932, "", 20, "medium", "Places", False),
 ("The Statue of Liberty was unveiled in New York in which year?", 1886, "", 30, "medium", "Places", False),
 ("How many steps do you climb to reach the crown of the Statue of Liberty?", 354, "steps", 150, "hard", "Places", False),
 ("Carving on Mount Rushmore was finished in which year?", 1941, "", 25, "medium", "Places", False),
 ("Roughly how tall is each president's face on Mount Rushmore, in feet?", 60, "feet", 30, "medium", "Places", False),
 ("How many lifts are there in Dubai's Burj Khalifa?", 57, "lifts", 30, "hard", "Places", True),
 ("Roughly how many panes of glass cover London's Shard, to the nearest 1,000?", 11000, "panes", 6000, "hard", "London", False),
 ("How many passenger capsules are there on the London Eye?", 32, "capsules", 15, "medium", "London", False),
 ("How tall is the London Eye, to the nearest metre?", 135, "metres", 60, "medium", "London", False),
 ("The Sydney Opera House opened in which year?", 1973, "", 15, "medium", "Places", False),
 ("How tall is the statue of Christ the Redeemer in Rio, not counting its base, to the nearest metre?", 30, "metres", 15, "medium", "Places", False),
 ("After its repairs, roughly how many degrees does the Leaning Tower of Pisa lean?", 4, "degrees", 3, "hard", "Places", True),
 ("How tall is the Leaning Tower of Pisa, to the nearest metre?", 56, "metres", 25, "hard", "Places", False),
 ("The Berlin Wall went up in which year?", 1961, "", 15, "medium", "History", False),
 ("Roughly how many kilometres long was the Berlin Wall, all the way round West Berlin?", 155, "km", 70, "hard", "History", True),
 ("The Hoover Dam was finished in which year?", 1936, "", 20, "hard", "Places", False),
 ("How tall is the Hoover Dam, to the nearest metre?", 221, "metres", 100, "hard", "Places", False),
 ("The Suez Canal opened in which year?", 1869, "", 30, "medium", "History", False),
 ("Roughly how many kilometres long is the Suez Canal?", 193, "km", 90, "hard", "Places", False),
 ("The Panama Canal opened in which year?", 1914, "", 20, "medium", "History", False),
 ("The Trans-Siberian Railway's main line was finally finished in which year?", 1916, "", 30, "hard", "History", False),
 ("Roughly how many kilometres long is the Trans-Siberian Railway from Moscow to Vladivostok?", 9289, "km", 4000, "hard", "Places", True),
 ("Edmund Hillary and Tenzing Norgay first stood on top of Everest in which year?", 1953, "", 15, "easy", "History", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-9.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
