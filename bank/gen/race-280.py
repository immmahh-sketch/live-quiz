# Bank session 19 Oct 2026: 2 races -> bank/race-280.json (Midsomer Murders; A Touch of Frost).
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

race("Midsomer Murders - name it", "Television", "medium", ["Midsomer Murders", "detectives", "ITV"], [
 ("The first detective in charge", "Tom Barnaby", ["Jack Frost", "Jim Taggart", "Charlie Resnick"]),
 ("The actor who played him", "John Nettles", ["John Thaw", "John Hannah", "John Simm"]),
 ("The year he left", "2011", ["2006", "2014", "2017"]),
 ("His cousin who took over", "John Barnaby", ["Peter Barnaby", "Mark Barnaby", "Ben Barnaby"]),
 ("The actor who played the cousin", "Neil Dudgeon", ["Neil Morrissey", "Neil Pearson", "Neil Stuke"]),
 ("The cousin's wife", "Sarah", ["Emma", "Claire", "Helen"]),
 ("The cousin's dog", "Sykes", ["Gnasher", "Wellard", "Patch"]),
 ("Tom Barnaby's wife", "Joyce", ["Jean", "Joan", "Janet"]),
 ("Their daughter", "Cully", ["Molly", "Polly", "Holly"]),
 ("Tom's first sergeant", "Gavin Troy", ["Robbie Lewis", "Mike Jardine", "George Toolan"]),
 ("The actor who played him", "Daniel Casey", ["Daniel Craig", "Daniel Mays", "Daniel Radcliffe"]),
 ("The county town where the police are based", "Causton", ["Kingsmarkham", "Denton", "Aidensfield"]),
 ("The author of the books it's based on", "Caroline Graham", ["Ruth Rendell", "P. D. James", "Ann Cleeves"]),
 ("The first story", "The Killings at Badger's Drift", ["The Body in the Library", "A Taste for Death", "The Mysterious Affair at Styles"]),
 ("The eerie instrument in the theme", "Theremin", ["Harpsichord", "Bagpipes", "Banjo"]),
 ("The theme's composer", "Jim Parker", ["Ron Grainer", "George Fenton", "Barrington Pheloung"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The year it began", "1997", ["1992", "2000", "2003"]),
 ("The real county where much of it is filmed", "Buckinghamshire", ["Cornwall", "Yorkshire", "Cumbria"]),
 ("What the sleepy villages are famous for having a lot of", "Murders", ["Car chases", "Cliffhangers", "Musical numbers"])])

race("A Touch of Frost - name it", "Television", "medium", ["A Touch of Frost", "detectives", "ITV"], [
 ("The actor who played Frost", "David Jason", ["David Suchet", "David Troughton", "David Haig"]),
 ("Frost's first name", "Jack", ["Jim", "Tom", "Frank"]),
 ("His rank", "Detective Inspector", ["Detective Sergeant", "Chief Inspector", "Superintendent"]),
 ("The town he polices", "Denton", ["Causton", "Aidensfield", "Kingsmarkham"]),
 ("The author of the novels", "R. D. Wingfield", ["Colin Dexter", "Caroline Graham", "Reginald Hill"]),
 ("The medal Frost won for bravery", "George Cross", ["Victoria Cross", "George Medal", "MBE"]),
 ("What Frost hates doing", "Paperwork", ["Driving", "Public speaking", "Flying"]),
 ("His pompous boss, the Superintendent", "Mullett", ["Strange", "Hastings", "Crozier"]),
 ("The actor who played the boss", "Bruce Alexander", ["Bruce Forsyth", "Bruce Jones", "Bruce Willis"]),
 ("Frost's loyal sergeant", "George Toolan", ["Gavin Troy", "Mike Jardine", "Robbie Lewis"]),
 ("The actor who played him", "John Lyons", ["John Challis", "John Sessions", "John Bird"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The ITV company that made it", "Yorkshire Television", ["Granada", "Central", "Anglia"]),
 ("The county where it was mostly filmed", "Yorkshire", ["Kent", "Hampshire", "Devon"]),
 ("The year it began", "1992", ["1987", "1996", "2001"]),
 ("The year it ended", "2010", ["2004", "2007", "2013"]),
 ("The star's ITV hit from the year before", "The Darling Buds of May", ["Heartbeat", "Boon", "Lovejoy"]),
 ("The star's most famous sitcom", "Only Fools and Horses", ["Open All Hours", "Porridge", "Last of the Summer Wine"]),
 ("The cartoon mouse he voiced", "Danger Mouse", ["SuperTed", "Bananaman", "Dogtanian"]),
 ("The year he was knighted", "2005", ["1999", "2008", "2015"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-280.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
