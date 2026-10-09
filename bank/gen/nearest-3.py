# Bank session 9 Oct 2026 (second pass): 37 more Nearest Wins questions -> bank/nearest-3.json
# (text, answer, unit, spread, difficulty, category, wow). Checked against the live bank's wording first; avoids
# well-worn pub facts and local giveaways (both were reasons a reviewer rejected earlier questions).
import json, os
Q = [
 ("The Tyne Bridge was opened by King George V. In which year?", 1928, "", 20, "medium", "The North East of England", False),
 ("In what year was football first played at St James' Park?", 1880, "", 30, "hard", "Football", False),
 ("In what year did Sunderland move into the Stadium of Light?", 1997, "", 12, "medium", "Football", False),
 ("In what year was Sunderland granted city status?", 1992, "", 25, "hard", "The North East of England", True),
 ("Building work on Hadrian's Wall began during Emperor Hadrian's visit to Britain. In what year AD?", 122, "AD", 60, "medium", "History", False),
 ("In what year did building work begin on Durham Cathedral?", 1093, "", 100, "hard", "History", False),
 ("In what year did the BBC make its first radio broadcasts?", 1922, "", 20, "medium", "Film and TV", False),
 ("Coronation Street began on ITV in which year?", 1960, "", 15, "medium", "Film and TV", False),
 ("EastEnders began on BBC One in which year?", 1985, "", 10, "easy", "Film and TV", False),
 ("Greggs began as a bakery round in Gosforth. In what year?", 1939, "", 25, "hard", "Food and drink", False),
 ("In what year was Newcastle Brown Ale first brewed?", 1927, "", 25, "hard", "Food and drink", False),
 ("Roughly how many muscles are there in the human body, to the nearest 100?", 600, "muscles", 300, "hard", "Science and nature", True),
 ("Roughly how many kilometres does light travel in one second, to the nearest 100,000?", 300000, "km", 150000, "medium", "Science and nature", False),
 ("How old was John Lennon when he died?", 40, "years old", 15, "medium", "Music", False),
 ("In what year was the first ever text message sent?", 1992, "", 10, "medium", "Science and technology", True),
 ("When Twitter launched, how many characters long could a tweet be?", 140, "characters", 80, "easy", "Science and technology", False),
 ("In what year was the Mona Lisa stolen from the Louvre?", 1911, "", 40, "hard", "Art", True),
 ("Roughly how many rooms are there in Buckingham Palace, to the nearest 100?", 775, "rooms", 350, "hard", "Places", True),
 ("A Scrabble board is a square grid. How many squares does it have?", 225, "squares", 100, "medium", "Games and toys", False),
 ("How many official Eon James Bond films were released up to and including No Time to Die?", 25, "films", 10, "medium", "Film and TV", False),
 ("In what year did Oasis release their first album, Definitely Maybe?", 1994, "", 10, "medium", "Music", False),
 ("In what year did the Spice Girls release Wannabe?", 1996, "", 10, "easy", "Music", False),
 ("In what year did Sunderland beat Leeds United to win the FA Cup?", 1973, "", 25, "medium", "Football", False),
 ("How many times did Roger Federer win the men's singles at Wimbledon?", 8, "times", 5, "medium", "Sport", False),
 ("How many players are there in a rugby league team on the pitch?", 13, "players", 6, "medium", "Sport", False),
 ("How many countries were members of the European Union in 2026?", 27, "countries", 10, "medium", "Geography", False),
 ("The Simpsons began as a full series on American TV in which year?", 1989, "", 10, "medium", "Film and TV", False),
 ("In what year did Concorde carry its first fare-paying passengers?", 1976, "", 15, "medium", "History", False),
 ("The Gateshead Millennium Bridge first let people walk across it in which year?", 2001, "", 10, "medium", "The North East of England", False),
 ("How many steps are there up the inside of Grey's Monument in Newcastle?", 164, "steps", 70, "hard", "The North East of England", True),
 ("How old was Elizabeth II on the day of her coronation in 1953?", 27, "years old", 15, "medium", "History", False),
 ("In what year was the first Grand National run at Aintree?", 1839, "", 40, "hard", "Sport", False),
 ("A Formula One Grand Prix must be at least how many kilometres long?", 305, "km", 120, "hard", "Sport", True),
 ("The Forth Bridge, the red railway bridge near Edinburgh, carried its first trains in which year?", 1890, "", 40, "hard", "History", False),
 ("In what year did the great bell Big Ben first ring out from the Houses of Parliament?", 1859, "", 50, "hard", "History", False),
 ("Donald Trump took office again in January 2025. Which number president of the United States did that make him?", 47, "", 15, "medium", "The United States", False),
 ("How many Doctor Who episodes were made in its original run, from 1963 to 1989, to the nearest 100?", 700, "episodes", 300, "hard", "Film and TV", True),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
