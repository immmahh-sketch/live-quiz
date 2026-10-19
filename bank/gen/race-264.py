# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-264.json (Birds of a Feather; Goodnight Sweetheart).
# Checked against every race in stock with lqsql/audit/race-overlap.py before importing.
# raceOk: 20 rows, 20 different right answers, no right answer among another row's options, no wrong option on 3+ rows.
import json, os
from collections import Counter
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    over = [w for w, n in Counter(w for _, _, wrong in rows for w in wrong).items() if n > 2]
    assert not over, (title, 'wrong option on 3+ rows', over)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("Birds of a Feather - name it", "Television", "medium", ["Birds of a Feather", "sitcoms", "BBC"], [
 ("The two sisters", "Sharon and Tracey", ["Shirley and Tracey", "Sharon and Tina", "Sandra and Tracey"]),
 ("The actress who played Sharon", "Pauline Quirke", ["Pauline Collins", "Pauline McLynn", "Pauline Yates"]),
 ("The actress who played Tracey", "Linda Robson", ["Linda Bellingham", "Linda Lusardi", "Linda Henry"]),
 ("Where the sisters' husbands are", "In prison", ["In the army", "Abroad", "On an oil rig"]),
 ("What the husbands did", "Armed robbery", ["Fraud", "Smuggling", "Car theft"]),
 ("Sharon's husband", "Chris", ["Craig", "Colin", "Carl"]),
 ("Tracey's husband", "Darryl", ["Darren", "Dean", "Daniel"]),
 ("Tracey's son", "Garth", ["Gareth", "Gavin", "Gary"]),
 ("Their man-eating neighbour", "Dorien", ["Doreen", "Dolores", "Daphne"]),
 ("The actress who played her", "Lesley Joseph", ["Lesley Garrett", "Lesley Sharp", "Lesley Ash"]),
 ("What the neighbour is famous for", "Chasing younger men", ["Baking cakes", "Gardening", "Collecting antiques"]),
 ("The dance show she joined in 2017", "Strictly Come Dancing", ["Dancing on Ice", "Let's Dance", "Stepping Out"]),
 ("The Essex town they live in", "Chigwell", ["Romford", "Basildon", "Loughton"]),
 ("The writers", "Laurence Marks and Maurice Gran", ["Galton and Simpson", "Croft and Perry", "Clement and La Frenais"]),
 ("Those writers' time-travel sitcom", "Goodnight Sweetheart", ["Birds of Paradise", "Dear John", "Only Fools and Horses"]),
 ("The channel it began on", "BBC One", ["BBC Two", "Channel 4", "Sky One"]),
 ("The year it began", "1989", ["1985", "1993", "1997"]),
 ("The channel that revived it", "ITV", ["Channel 5", "UKTV", "Dave"]),
 ("The year of the revival", "2014", ["2010", "2017", "2020"]),
 ("The county", "Essex", ["Kent", "Surrey", "Hertfordshire"])])

race("Goodnight Sweetheart - name it", "Television", "medium", ["Goodnight Sweetheart", "sitcoms", "BBC"], [
 ("The time-travelling hero", "Gary Sparrow", ["Gary Swallow", "Garry Finch", "Gary Starling"]),
 ("The actor who played him", "Nicholas Lyndhurst", ["Nicholas Parsons", "Nicholas Hoult", "Nicholas Ball"]),
 ("That actor's role in Only Fools and Horses", "Rodney", ["Del Boy", "Trigger", "Boycie"]),
 ("His earlier sitcom with Wendy Craig", "Butterflies", ["After Henry", "Ever Decreasing Circles", "Brush Strokes"]),
 ("The era he travels back to", "The Second World War", ["The 1960s", "Victorian times", "The 1920s"]),
 ("Where the time portal is", "Ducketts Passage", ["Diagon Alley", "Carnaby Street", "Albert Square"]),
 ("His job in the present day", "TV repairman", ["Plumber", "Taxi driver", "Milkman"]),
 ("His wife in the present day", "Yvonne", ["Yvette", "Yolanda", "Yasmin"]),
 ("His love in the 1940s", "Phoebe", ["Phyllis", "Penny", "Pauline"]),
 ("The first actress to play her", "Dervla Kirwan", ["Dawn French", "Denise Welch", "Daisy Haggard"]),
 ("Her pub in the 1940s", "The Royal Oak", ["The Crown", "The Red Lion", "The Swan"]),
 ("What Gary passes off as his own", "Future hit songs", ["Inventions", "Paintings", "Recipes"]),
 ("What he tells 1940s Londoners he is", "A secret agent", ["A film star", "A doctor", "A vicar"]),
 ("His best friend", "Ron", ["Reg", "Roy", "Rob"]),
 ("That friend's trade", "Printer", ["Plumber", "Butcher", "Postman"]),
 ("The writers", "Laurence Marks and Maurice Gran", ["Galton and Simpson", "Croft and Perry", "Clement and La Frenais"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1993", ["1989", "1997", "2001"]),
 ("Series made", "6", ["3", "4", "8"]),
 ("The year of the one-off return", "2016", ["2010", "2013", "2019"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-264.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
