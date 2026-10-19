# Bank session 19 Oct 2026: 2 races -> bank/race-287.json (Downton Abbey; Peaky Blinders).
# Neither show had a race in the live bank. Checked against every live race with lqsql/audit/race-overlap-live.py before importing.
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

race("Downton Abbey - name it", "Television", "medium", ["Downton Abbey", "TV drama", "ITV"], [
 ("The writer who created it", "Julian Fellowes", ["Andrew Davies", "Russell T Davies", "Steven Moffat"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "Sky One"]),
 ("The year it began", "2010", ["2005", "2013", "2016"]),
 ("The year the TV series ended", "2015", ["2012", "2018", "2020"]),
 ("The news that opens the first episode", "The sinking of the Titanic", ["The death of Queen Victoria", "The General Strike", "The coronation of George V"]),
 ("The county it's set in", "Yorkshire", ["Cornwall", "Norfolk", "Derbyshire"]),
 ("The real house used for filming", "Highclere Castle", ["Castle Howard", "Blenheim Palace", "Chatsworth"]),
 ("The county that house is in", "Hampshire", ["Wiltshire", "Oxfordshire", "Kent"]),
 ("The family upstairs", "The Crawleys", ["The Bellamys", "The Flytes", "The Poldarks"]),
 ("Lord Grantham's rank", "Earl", ["Duke", "Viscount", "Baron"]),
 ("The actor who plays him", "Hugh Bonneville", ["Hugh Grant", "Hugh Laurie", "Hugh Dennis"]),
 ("The actress who played the Dowager Countess", "Maggie Smith", ["Judi Dench", "Helen Mirren", "Eileen Atkins"]),
 ("The eldest daughter", "Lady Mary", ["Lady Jane", "Lady Sarah", "Lady Anne"]),
 ("Her husband, killed in a car crash", "Matthew Crawley", ["Matthew Corbett", "Matthew Perry", "Matthew Kelly"]),
 ("The actor who played him", "Dan Stevens", ["Dan Snow", "Dan Walker", "Dan Aykroyd"]),
 ("The chauffeur who married the youngest daughter", "Tom Branson", ["Tom Barnaby", "Tom Daley", "Tom Jones"]),
 ("The butler", "Carson", ["Hudson", "Jeeves", "Lurch"]),
 ("The housekeeper", "Mrs Hughes", ["Mrs Hall", "Mrs Danvers", "Mrs Bridges"]),
 ("The cook", "Mrs Patmore", ["Mrs Overall", "Mrs Doyle", "Mrs Beeton"]),
 ("The year of the first film", "2019", ["2016", "2021", "2023"])])

race("Peaky Blinders - name it", "Television", "medium", ["Peaky Blinders", "TV drama", "BBC"], [
 ("The city it's set in", "Birmingham", ["Manchester", "Liverpool", "Glasgow"]),
 ("The district", "Small Heath", ["Aston", "Handsworth", "Edgbaston"]),
 ("The family's surname", "Shelby", ["Kray", "Richardson", "Mitchell"]),
 ("The actor who plays Tommy", "Cillian Murphy", ["Colin Farrell", "Michael Fassbender", "Jamie Dornan"]),
 ("Tommy's older brother", "Arthur", ["Albert", "Alfred", "Archie"]),
 ("Tommy's aunt", "Polly", ["Peggy", "Pauline", "Patsy"]),
 ("The actress who played her", "Helen McCrory", ["Helen Mirren", "Helen Baxendale", "Helen Flanagan"]),
 ("Tom Hardy's character", "Alfie Solomons", ["Alfie Moon", "Alfie Elkins", "Alfie Allen"]),
 ("The kind of cap they wear", "Flat cap", ["Bowler hat", "Top hat", "Beret"]),
 ("What the name refers to", "Razor blades sewn into their caps", ["Their sharp suits", "Their pointed noses", "A pub sign"]),
 ("The war Tommy fought in", "First World War", ["Boer War", "Second World War", "Crimean War"]),
 ("The year the first series is set", "1919", ["1905", "1929", "1939"]),
 ("The fascist leader in the later series", "Oswald Mosley", ["Enoch Powell", "Neville Chamberlain", "Lord Haw-Haw"]),
 ("What Tommy goes on to become", "An MP", ["A judge", "A mayor", "A bishop"]),
 ("The theme song", "Red Right Hand", ["Into My Arms", "Hurt", "Paint It Black"]),
 ("Who recorded it", "Nick Cave and the Bad Seeds", ["Tom Waits", "Johnny Cash", "Leonard Cohen"]),
 ("The writer who created it", "Steven Knight", ["Steven Moffat", "Jed Mercurio", "Jimmy McGovern"]),
 ("The channel it started on", "BBC Two", ["Channel 4", "ITV", "Sky One"]),
 ("The year it began", "2013", ["2009", "2016", "2019"]),
 ("The year the final series aired", "2022", ["2018", "2020", "2024"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-287.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
