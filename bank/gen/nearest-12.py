# Bank session 10 Oct 2026: more Nearest Wins questions -> bank/nearest-12.json: animals and nature in numbers.
# (text, answer, unit, spread, difficulty, category, wow). Each was checked against the live bank's wording first.
import json, os
Q = [
 ("A 2016 study aged Greenland sharks from the lenses of their eyes. The oldest was estimated at roughly how many years old?", 392, "years", 120, "hard", "Nature", True),
 ("One ostrich egg holds about as much as how many hen's eggs?", 24, "eggs", 10, "medium", "Nature", False),
 ("An earthworm has no single heart but several pairs of heart-like pumps. How many pairs?", 5, "", 3, "hard", "Nature", True),
 ("A modern laying hen can lay roughly how many eggs in a year?", 300, "eggs", 80, "medium", "Nature", False),
 ("The fastest sprint ever timed by a Thoroughbred racehorse was in 2008. How fast was it, to the nearest mile per hour?", 44, "mph", 10, "medium", "Nature", False),
 ("Bats make up about one in five of all mammal species. Roughly how many species of bat are there, to the nearest 100?", 1400, "species", 500, "hard", "Nature", True),
 ("A hummingbird's heart can beat up to roughly how many times a minute?", 1200, "beats", 400, "hard", "Nature", True),
 ("Arctic terns fly from the Arctic to the Antarctic and back every year. Roughly how many kilometres is that round trip?", 70000, "km", 25000, "hard", "Nature", True),
 ("An elephant's trunk has no bones but a huge number of muscle bundles. Roughly how many?", 40000, "muscles", 20000, "hard", "Nature", True),
 ("A garden snail's tongue is covered in tiny teeth. Roughly how many does it have?", 14000, "teeth", 7000, "hard", "Nature", True),
 ("An ant can carry up to roughly how many times its own body weight?", 50, "times", 25, "medium", "Nature", False),
 ("A blue whale's tongue weighs about as much as an elephant. Roughly how much is that, in kilograms, to the nearest 100?", 2700, "kg", 1500, "hard", "Nature", True),
 ("Roughly how many species of spider have been named by scientists, to the nearest thousand?", 52000, "species", 20000, "hard", "Nature", False),
 ("To make one 1lb jar of honey, a hive's bees fly roughly how many miles between them?", 55000, "miles", 25000, "hard", "Nature", True),
 ("A very thirsty camel can drink roughly how many litres of water in about ten minutes?", 100, "litres", 50, "medium", "Nature", True),
 ("Monarch butterflies migrate from Canada to Mexico every autumn. Up to roughly how many miles is the journey?", 3000, "miles", 1000, "medium", "Nature", False),
 ("An adult elephant can eat roughly how many kilograms of food in a day?", 150, "kg", 75, "medium", "Nature", False),
 ("A typical British dairy cow gives roughly how many litres of milk a year, to the nearest thousand?", 8000, "litres", 3000, "hard", "Nature", False),
 ("Roughly how many million sheep are there in the UK?", 31, "million", 12, "medium", "Britain", False),
 ("Roughly how many dog breeds does the Kennel Club recognise, to the nearest 10?", 220, "breeds", 60, "hard", "Nature", False),
 ("The fastest-growing kinds of bamboo can grow up to roughly how many centimetres in a single day?", 90, "cm", 40, "medium", "Nature", True),
 ("Young common swifts can stay in the air without landing for up to roughly how many months?", 10, "months", 4, "medium", "Nature", True),
 ("The wandering albatross has the widest wingspan of any living bird. How wide can it be, in metres, to one decimal place?", 3.5, "m", 1, "medium", "Nature", False),
 ("Roughly how many hours a day does a typical pet cat spend asleep?", 15, "hours", 4, "easy", "Nature", False),
 ("Up to roughly how tall can an adult male giraffe stand, to the nearest metre?", 6, "m", 2, "medium", "Nature", False),
 ("An owl can't move its eyes, so it turns its head. Through roughly how many degrees can it turn it?", 270, "degrees", 90, "easy", "Nature", False),
 ("Roughly how many spines does an adult hedgehog have, to the nearest thousand?", 6000, "spines", 2500, "medium", "Nature", True),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-12.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
