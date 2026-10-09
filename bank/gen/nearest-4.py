# Bank session 9 Oct 2026 (third pass): 33 more Nearest Wins questions -> bank/nearest-4.json
# (text, answer, unit, spread, difficulty, category, wow). Each was checked against the live bank's wording first.
import json, os
Q = [
 ("The Premier League kicked off its very first season in which year?", 1992, "", 10, "easy", "Football", False),
 ("The Wimbledon Championships were first played in which year?", 1877, "", 40, "hard", "Sport", False),
 ("The first Rugby Union World Cup, co-hosted by New Zealand and Australia, was played in which year?", 1987, "", 15, "medium", "Sport", False),
 ("The first men's Cricket World Cup, played in England, took place in which year?", 1975, "", 15, "hard", "Sport", False),
 ("The first Tour de France cycle race was held in which year?", 1903, "", 30, "hard", "Sport", False),
 ("The world's first underground railway opened in London in which year?", 1863, "", 40, "medium", "History", True),
 ("Sky TV began broadcasting to British homes by satellite in which year?", 1989, "", 10, "medium", "Film and TV", False),
 ("Channel 4 went on air for the first time in which year?", 1982, "", 10, "medium", "Film and TV", False),
 ("Blue Peter was first shown on BBC television in which year?", 1958, "", 15, "medium", "Film and TV", False),
 ("The arcade game Pac-Man was released in which year?", 1980, "", 10, "medium", "Games and toys", False),
 ("Ernő Rubik made the first prototype of his famous cube in which year?", 1974, "", 10, "hard", "Games and toys", False),
 ("Barbie the doll was launched in which year?", 1959, "", 15, "medium", "Games and toys", False),
 ("The original Mini car was launched by the British Motor Corporation in which year?", 1959, "", 15, "medium", "History", False),
 ("How many member countries are there in the Commonwealth of Nations?", 56, "countries", 25, "hard", "Geography", False),
 ("The NATO alliance had how many member states in 2026?", 32, "countries", 12, "medium", "Geography", False),
 ("How many judges sit on the US Supreme Court?", 9, "judges", 6, "medium", "The United States", False),
 ("How many MSPs are elected to the Scottish Parliament?", 129, "MSPs", 60, "hard", "Scotland", False),
 ("How old was Queen Victoria when she died in 1901?", 81, "years old", 25, "medium", "History", False),
 ("A piano's 88 keys include how many black ones?", 36, "keys", 20, "medium", "Music", True),
 ("How many players does each Aussie rules football team have on the field at once?", 18, "players", 8, "hard", "Sport", True),
 ("How many players does each ice hockey team have on the ice at once, counting the goalie?", 6, "players", 4, "medium", "Sport", False),
 ("How many minutes long is an NBA basketball game, not counting overtime?", 48, "minutes", 20, "medium", "Sport", False),
 ("A full-size snooker table is how many feet long?", 12, "feet", 6, "medium", "Sport", False),
 ("A netball goal post stands how many feet high?", 10, "feet", 5, "medium", "Sport", False),
 ("The first Nobel Prizes were handed out in which year?", 1901, "", 30, "medium", "History", False),
 ("Comic Relief's first Red Nose Day was in which year?", 1988, "", 10, "medium", "Film and TV", False),
 ("BBC Children in Need held its first telethon in which year?", 1980, "", 10, "medium", "Film and TV", False),
 ("The breathalyser was brought in to catch drink-drivers in Britain in which year?", 1967, "", 20, "hard", "History", False),
 ("Wearing a seat belt in the front of a car became the law in Britain in which year?", 1983, "", 15, "hard", "History", False),
 ("Comedian Ernie Wise made Britain's first mobile phone call in which year?", 1985, "", 10, "hard", "Science and technology", True),
 ("Ray Tomlinson sent the first email between two computers in which year?", 1971, "", 15, "hard", "Science and technology", True),
 ("How many minutes are there in a week?", 10080, "minutes", 4000, "medium", "Maths", False),
 ("How many stations are there on the London Underground, to the nearest 10?", 272, "stations", 100, "hard", "Places", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
