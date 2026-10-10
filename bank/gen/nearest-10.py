# Bank session 10 Oct 2026: more Nearest Wins questions -> bank/nearest-10.json: brands, games and music firsts.
# (text, answer, unit, spread, difficulty, category, wow). Each was checked against the live bank's wording first.
import json, os
Q = [
 ("The Mars bar was first made in Slough in which year?", 1932, "", 15, "medium", "Food and drink", False),
 ("Birds Eye fish fingers first went on sale in Britain in which year?", 1955, "", 15, "hard", "Food and drink", False),
 ("Michael Marks opened the Leeds market stall that grew into Marks & Spencer in which year?", 1884, "", 25, "hard", "Food and drink", False),
 ("Fenwick opened its first shop in Newcastle in which year?", 1882, "", 25, "hard", "North East", False),
 ("Nando's opened its first UK restaurant, in Ealing, in which year?", 1992, "", 10, "hard", "Food and drink", False),
 ("Rowntree's launched the chocolate bar we now call KitKat in which year?", 1935, "", 15, "medium", "Food and drink", False),
 ("Twix first went on sale in Britain in which year?", 1967, "", 15, "hard", "Food and drink", False),
 ("Jack Cohen started the market stall that became Tesco in which year?", 1919, "", 20, "hard", "Food and drink", False),
 ("Walkers crisps were first made in Leicester in which year?", 1948, "", 15, "hard", "Food and drink", False),
 ("Pizza Express opened its first restaurant, in Soho, in which year?", 1965, "", 15, "hard", "Food and drink", False),
 ("Lego's interlocking plastic brick was patented in which year?", 1958, "", 15, "medium", "Toys and games", False),
 ("The board game Cluedo was first published in Britain in which year?", 1949, "", 15, "hard", "Toys and games", False),
 ("Trivial Pursuit was invented by two Canadian journalists in which year?", 1979, "", 10, "medium", "Toys and games", False),
 ("Nintendo's Game Boy first came out in Japan in which year?", 1989, "", 8, "medium", "Toys and games", False),
 ("Sony's first PlayStation came out in Japan in which year?", 1994, "", 8, "medium", "Toys and games", False),
 ("Alexey Pajitnov created Tetris in which year?", 1984, "", 10, "medium", "Toys and games", False),
 ("How old was Freddie Mercury when he died in 1991?", 45, "years old", 10, "medium", "Music", False),
 ("Whitney Houston's 'I Will Always Love You' spent how many weeks at number one in the UK?", 10, "weeks", 5, "hard", "Music", False),
 ("Up to 2025, how many UK number one singles had Madonna had?", 13, "number ones", 6, "hard", "Music", False),
 ("BBC Radio 1 first went on air in which year?", 1967, "", 10, "medium", "Music", False),
 ("MTV launched in America, with 'Video Killed the Radio Star' as its first video, in which year?", 1981, "", 8, "medium", "Music", False),
 ("Apple's first iPod went on sale in which year?", 2001, "", 5, "easy", "Science and tech", False),
 ("Spotify launched in which year?", 2008, "", 5, "medium", "Science and tech", False),
 ("Oasis played two nights at Knebworth in 1996. Roughly how many people saw them across both nights, to the nearest 10,000?", 250000, "people", 120000, "hard", "Music", True),
 ("Drake's 'One Dance' spent how many weeks at number one in the UK in 2016?", 15, "weeks", 6, "hard", "Music", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
