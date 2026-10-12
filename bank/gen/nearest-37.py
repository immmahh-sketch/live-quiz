# Bank session 12 Oct 2026: more Nearest Wins questions -> bank/nearest-37.json: food and drink numbers (a thin theme in the bank).
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("In what year did the first ever Pizza Hut open, in Wichita, Kansas?", 1958, "", 5, "medium", "Food and drink", False),
 ("Golden Wonder brought out the Pot Noodle in which year?", 1979, "", 5, "hard", "Food and drink", False),
 ("In what year did Starbucks open its first coffee shops in the UK?", 1998, "", 4, "medium", "Food and drink", False),
 ("Britain's first Wimpy burger bar opened in London in which year?", 1954, "", 6, "hard", "Food and drink", False),
 ("Fry's launched the Crunchie bar in which year?", 1929, "", 7, "hard", "Food and drink", False),
 ("Rowntree's launched the chunky Yorkie bar in which year?", 1976, "", 5, "medium", "Food and drink", False),
 ("Monster Munch crisps first went on sale in which year?", 1977, "", 5, "hard", "Food and drink", False),
 ("PG Tips tea first went on sale, as Pre-Gest-Tee, in which year?", 1930, "", 7, "hard", "Food and drink", False),
 ("Marmite was first made in Burton upon Trent in which year?", 1902, "", 8, "hard", "Food and drink", False),
 ("Mackintosh's of Halifax launched Quality Street in which year?", 1936, "", 7, "hard", "Food and drink", False),
 ("Irn-Bru was first made in Scotland, as Iron Brew, in which year?", 1901, "", 8, "hard", "Food and drink", False),
 ("A Tyneside chemist invented Lucozade, first sold in chemists for the sick. In what year?", 1927, "", 7, "hard", "Food and drink", True),
 ("Toblerone was first made in Bern, Switzerland, in which year?", 1908, "", 8, "hard", "Food and drink", False),
 ("Costa Coffee was founded in London in which year?", 1971, "", 5, "medium", "Food and drink", False),
 ("How many fingers does a classic KitKat have?", 4, "fingers", 1, "easy", "Food and drink", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-37.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
