# Bank session 18 Oct 2026: 2 races -> bank/race-233.json (Mr Bean; Peep Show).
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

race("Mr Bean - name it", "Television", "easy", ["Mr Bean", "Rowan Atkinson", "comedy", "ITV"], [
 ("The actor who plays him", "Rowan Atkinson", ["Hugh Laurie", "Richard Wilson", "Griff Rhys Jones"]),
 ("His beloved toy", "Teddy", ["Bunny", "Mr Snuggles", "Barnaby"]),
 ("The make of his car", "Mini", ["Beetle", "Morris Minor", "Fiat 500"]),
 ("Its colour, apart from the black bonnet", "Green", ["Red", "Blue", "Yellow"]),
 ("How he locks the car door", "With a padlock", ["With a crook lock", "With a steering lock", "With a bike lock"]),
 ("The three-wheeled car he keeps tipping over", "Reliant Robin", ["Reliant Regal", "Bond Bug", "Isetta"]),
 ("His long-suffering girlfriend", "Irma Gobb", ["Ivy Gobb", "Edna Gobb", "Irma Grubb"]),
 ("The Latin sung over the opening titles", "Ecce homo qui est faba", ["Veni, vidi, vici", "Carpe diem", "In vino veritas"]),
 ("What that Latin means", "Behold the man who is a bean", ["Here comes the bean", "The bean has landed", "All hail the bean"]),
 ("What he gets his head stuck in at Christmas", "A turkey", ["A pudding", "A stocking", "A cracker"]),
 ("The year it was first shown", "1990", ["1987", "1993", "1995"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The writer who created him with Atkinson", "Richard Curtis", ["Ben Elton", "John Lloyd", "Rob Grant"]),
 ("The year the cartoon series began", "2002", ["1998", "2006", "2010"]),
 ("The title of the first film, in 1997", "Bean", ["Mr Bean Goes West", "The Bean Movie", "Bean There"]),
 ("The city whose art gallery he wreaks havoc in, in that film", "Los Angeles", ["New York", "Chicago", "San Francisco"]),
 ("The painting he ruins in it", "Whistler's Mother", ["The Mona Lisa", "The Laughing Cavalier", "American Gothic"]),
 ("The 2007 film", "Mr Bean's Holiday", ["Mr Bean Abroad", "Bean in Paris", "Mr Bean's Big Trip"]),
 ("Where that film ends up", "Cannes", ["Paris", "Nice", "Monaco"]),
 ("The tune he played at the 2012 Olympics opening ceremony", "Chariots of Fire", ["Jerusalem", "Land of Hope and Glory", "Rule, Britannia!"])])

race("Peep Show - name it", "British sitcoms", "medium", ["Peep Show", "sitcoms", "Channel 4", "Mitchell and Webb"], [
 ("The town where Mark and Jez share a flat", "Croydon", ["Bromley", "Sutton", "Slough"]),
 ("Mark's surname", "Corrigan", ["Corbett", "Cartwright", "Callaghan"]),
 ("What Jeremy is called", "Jez", ["Jem", "Jeds", "J-Man"]),
 ("The actor who plays Mark", "David Mitchell", ["Simon Bird", "Stephen Merchant", "Matt Lucas"]),
 ("The actor who plays Jez", "Robert Webb", ["James Corden", "Mathew Horne", "Jack Whitehall"]),
 ("Jez's wild, drug-loving bandmate", "Super Hans", ["Mega Hans", "Big Hans", "Super Gaz"]),
 ("Mark's on-off love from work", "Sophie", ["Sarah", "Stella", "Susie"]),
 ("The actor who plays her", "Olivia Colman", ["Sophie Okonedo", "Tamsin Greig", "Rachael Stirling"]),
 ("Mark's swaggering boss", "Alan Johnson", ["Alan Partridge", "Alan Jenkins", "Johnny Allen"]),
 ("The company Mark works for", "JLB", ["JBL", "LJB", "JCB"]),
 ("Mark's later girlfriend from IT", "Dobby", ["Debbie", "Daisy", "Dotty"]),
 ("The American Jez marries so she can stay", "Nancy", ["Nicole", "Natalie", "Nina"]),
 ("What Jez dreams of being", "Musician", ["Actor", "Chef", "Footballer"]),
 ("The period of history Mark is obsessed with", "The Second World War", ["The Romans", "The Tudors", "The Cold War"]),
 ("The channel", "Channel 4", ["BBC Three", "E4", "BBC Two"]),
 ("The writing partnership behind it", "Armstrong and Bain", ["Mitchell and Webb", "Linehan and Mathews", "Baddiel and Newman"]),
 ("Jesse Armstrong's later American hit", "Succession", ["Billions", "Mad Men", "Veep"]),
 ("The year it began", "2003", ["2000", "2006", "2009"]),
 ("The year it ended", "2015", ["2011", "2013", "2018"]),
 ("How many series were made", "9", ["5", "7", "11"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-233.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
