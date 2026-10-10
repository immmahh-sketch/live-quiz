# Bank session 10 Oct 2026: more Nearest Wins questions -> bank/nearest-11.json: when everyday life changed (money, roads, the web).
# (text, answer, unit, spread, difficulty, category, wow). Each was checked against the live bank's wording first.
import json, os
Q = [
 ("The Penny Black, the world's first sticky postage stamp, was issued in which year?", 1840, "", 20, "medium", "History", False),
 ("The round pound coin first went into people's pockets in which year?", 1983, "", 8, "medium", "History", False),
 ("Britain's seven-sided 50p coin first appeared in which year?", 1969, "", 8, "hard", "History", False),
 ("The 20p coin first appeared in which year?", 1982, "", 8, "hard", "History", False),
 ("The £2 coin first went into general circulation in which year?", 1998, "", 6, "hard", "History", False),
 ("The Bank of England's first plastic note, the Churchill £5, came out in which year?", 2016, "", 5, "medium", "History", False),
 ("Barclaycard, Britain's first credit card, was launched in which year?", 1966, "", 10, "hard", "History", False),
 ("Chip and PIN became compulsory for card payments in UK shops in which year?", 2006, "", 5, "hard", "History", False),
 ("The first contactless bank cards were launched in the UK in which year?", 2007, "", 5, "hard", "History", False),
 ("London's Oyster card was launched in which year?", 2003, "", 5, "medium", "London", False),
 ("The smoking ban in pubs and workplaces in England began in which year?", 2007, "", 5, "medium", "History", False),
 ("Shops in England began charging for plastic carrier bags in which year?", 2015, "", 4, "medium", "History", False),
 ("Apple's first iPhone went on sale in which year?", 2007, "", 4, "easy", "Science and tech", False),
 ("Google was founded in which year?", 1998, "", 5, "medium", "Science and tech", False),
 ("Facebook was launched by Mark Zuckerberg in which year?", 2004, "", 4, "easy", "Science and tech", False),
 ("Wikipedia was launched in which year?", 2001, "", 5, "medium", "Science and tech", False),
 ("Twitter, now called X, was launched in which year?", 2006, "", 4, "medium", "Science and tech", False),
 ("Britain's first speed camera went up in which year?", 1992, "", 8, "hard", "History", False),
 ("The first Highway Code was published in which year?", 1931, "", 15, "hard", "History", False),
 ("The MOT test for older cars was brought in during which year?", 1960, "", 10, "hard", "History", False),
 ("Driving tests became compulsory for new drivers in Britain in which year?", 1935, "", 15, "medium", "History", False),
 ("The 70 mph speed limit was first brought in on Britain's roads in which year?", 1965, "", 10, "hard", "History", False),
 ("Cars in Britain first had to carry number plates in which year?", 1904, "", 15, "hard", "History", True),
 ("Euro notes and coins first went into people's purses in which year?", 2002, "", 4, "easy", "History", False),
 ("Roughly how many years separate the Penny Black from the first email?", 131, "years", 40, "hard", "History", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
