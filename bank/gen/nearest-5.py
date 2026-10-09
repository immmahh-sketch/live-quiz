# Bank session 9 Oct 2026 (fourth pass): more Nearest Wins questions -> bank/nearest-5.json, a few for Christmas.
# (text, answer, unit, spread, difficulty, category, wow). Each was checked against the live bank's wording first.
import json, os
Q = [
 ("Charles Dickens published A Christmas Carol in which year?", 1843, "", 40, "medium", "Christmas", False),
 ("Norway has sent a Christmas tree to stand in Trafalgar Square every year since which year?", 1947, "", 20, "hard", "Christmas", True),
 ("The Norwegian spruce in Trafalgar Square is usually about how many metres high?", 20, "metres", 10, "hard", "Christmas", False),
 ("The film White Christmas, starring Bing Crosby, came out in which year?", 1954, "", 15, "medium", "Christmas", False),
 ("Tom Smith, a London sweet-maker, invented the Christmas cracker in roughly which year?", 1847, "", 40, "hard", "Christmas", True),
 ("Coca-Cola's 'Holidays Are Coming' lorry advert was first shown in which year?", 1995, "", 10, "medium", "Christmas", False),
 ("Mariah Carey released All I Want for Christmas Is You in which year?", 1994, "", 10, "easy", "Christmas", False),
 ("Love Actually, Richard Curtis's Christmas film, came out in which year?", 2003, "", 10, "easy", "Christmas", False),
 ("Adding up every gift in every verse of 'The Twelve Days of Christmas', how many gifts are given altogether?", 364, "gifts", 200, "hard", "Christmas", True),
 ("How many different countries have won the men's football World Cup, up to 2022?", 8, "countries", 4, "medium", "Football", False),
 ("The original Wembley Stadium, with its twin towers, opened in which year?", 1923, "", 20, "hard", "Football", False),
 ("How tall is the Statue of Liberty from her heel to the top of the torch, to the nearest metre?", 46, "metres", 20, "hard", "Places", False),
 ("Roughly how many billion people were living on Earth in 2026, to one decimal place?", 8.2, "billion", 3, "medium", "Geography", False),
 ("Braemar in Aberdeenshire holds the UK record for cold. How far below freezing did it fall, in °C?", 27, "°C below zero", 15, "hard", "Geography", False),
 ("Women first ran an Olympic marathon at which Games year?", 1984, "", 20, "hard", "Sport", True),
 ("How many National Olympic Committees sent athletes to the Paris 2024 Olympics?", 206, "teams", 80, "hard", "Sport", False),
 ("How many sonnets did Shakespeare write?", 154, "sonnets", 60, "medium", "Books and literature", False),
 ("The Hawaiian language gets by with how few letters?", 13, "letters", 8, "hard", "Words and language", True),
 ("How many letters are there in the Welsh alphabet?", 29, "letters", 10, "hard", "Wales", True),
 ("Newcastle's Central Station was opened by Queen Victoria in which year?", 1850, "", 40, "hard", "The North East of England", False),
 ("Grey's Monument was put up in the centre of Newcastle in which year?", 1838, "", 40, "hard", "The North East of England", False),
 ("Penguin Books started selling its paperbacks in which year?", 1935, "", 20, "hard", "Books and literature", False),
 ("Strictly Come Dancing first appeared on BBC One in which year?", 2004, "", 10, "medium", "Film and TV", False),
 ("The Great British Bake Off's first series was shown in which year?", 2010, "", 8, "medium", "Film and TV", False),
 ("Who Wants to Be a Millionaire? first aired on ITV in which year?", 1998, "", 10, "medium", "Film and TV", False),
 ("Top Gear was relaunched with Jeremy Clarkson, Richard Hammond and James May in which year?", 2002, "", 10, "medium", "Film and TV", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
