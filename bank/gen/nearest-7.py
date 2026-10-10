# Bank session 10 Oct 2026: more Nearest Wins questions -> bank/nearest-7.json, with a North East block.
# (text, answer, unit, spread, difficulty, category, wow). Each was checked against the live bank's wording first.
import json, os
Q = [
 ("How many Premier League goals did Wayne Rooney score?", 208, "goals", 80, "medium", "Football", False),
 ("Peter Shilton holds the record for England caps. How many did he win?", 125, "caps", 40, "medium", "Football", False),
 ("How many goals did Jackie Milburn score for Newcastle United in all competitions?", 200, "goals", 80, "hard", "The North East of England", False),
 ("How many goals did Alan Shearer score for Newcastle United in all competitions?", 206, "goals", 80, "medium", "The North East of England", False),
 ("Newcastle United was formed when Newcastle East End took over at St James' Park. In which year?", 1892, "", 30, "hard", "The North East of England", False),
 ("Sunderland AFC was founded by a schoolteacher in which year?", 1879, "", 30, "hard", "The North East of England", False),
 ("Middlesbrough Football Club was founded in which year?", 1876, "", 30, "hard", "The North East of England", False),
 ("Roughly how many fans does St James' Park hold, to the nearest 1,000?", 52000, "fans", 20000, "medium", "The North East of England", False),
 ("Roughly how many fans does the Stadium of Light hold, to the nearest 1,000?", 49000, "fans", 20000, "medium", "The North East of England", False),
 ("The Sage Gateshead, now The Glasshouse, opened on the Quayside in which year?", 2004, "", 10, "medium", "The North East of England", False),
 ("The Tyne and Wear Metro first opened to passengers in which year?", 1980, "", 15, "medium", "The North East of England", False),
 ("Durham University, England's third oldest, was founded in which year?", 1832, "", 50, "hard", "The North East of England", True),
 ("The BALTIC Centre for Contemporary Art opened in Gateshead in which year?", 2002, "", 10, "medium", "The North East of England", False),
 ("The first Great North Run was held in which year?", 1981, "", 15, "medium", "The North East of England", False),
 ("Up to 2025, how many different clubs had won the Premier League?", 7, "clubs", 4, "medium", "Football", False),
 ("How many Grand Slam singles titles did Serena Williams win?", 23, "titles", 10, "easy", "Sport", False),
 ("How many Olympic gold medals did Mo Farah win?", 4, "golds", 3, "easy", "Sport", False),
 ("The Ashes began with a mock obituary after England lost to Australia at The Oval in which year?", 1882, "", 30, "hard", "Cricket", True),
 ("How many feet are there in a fathom?", 6, "feet", 4, "medium", "Science and nature", False),
 ("How many pounds are there in a stone?", 14, "pounds", 8, "easy", "Science and nature", False),
 ("How many yards are there in a mile?", 1760, "yards", 800, "medium", "Science and nature", False),
 ("How many litres are there in a UK gallon, to two decimal places?", 4.55, "litres", 3, "medium", "Science and nature", False),
 ("How many times did Steve Davis win the World Snooker Championship?", 6, "titles", 4, "medium", "Sport", False),
 ("How many world snooker titles had Ronnie O'Sullivan won, up to 2025?", 7, "titles", 4, "medium", "Sport", False),
 ("How many times did Red Rum win the Grand National?", 3, "wins", 3, "easy", "Sport", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
