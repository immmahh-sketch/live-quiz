# Bank session 19 Oct 2026: 2 races -> bank/race-276.json (Fifteen to One; Have I Got News for You).
# Neither show had a race in the live bank; two rows dropped for overlapping the One Foot in the Grave race. Checked against every live race with lqsql/audit/race-overlap-live.py before importing.
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

race("Fifteen to One - name it", "Television", "medium", ["Fifteen to One", "game shows", "Channel 4"], [
 ("The original host", "William G. Stewart", ["William Roache", "Bill Turnbull", "Bob Holness"]),
 ("The G in his name", "Gladstone", ["George", "Gordon", "Graham"]),
 ("The channel", "Channel 4", ["BBC Two", "ITV", "Channel 5"]),
 ("The year it began", "1988", ["1982", "1993", "1996"]),
 ("The year the original run ended", "2003", ["1996", "1999", "2008"]),
 ("What the title means", "15 players down to 1 winner", ["15 questions to win £1", "15 seconds for 1 answer", "15 rounds in 1 hour"]),
 ("Contestants at the start", "15", ["10", "12", "20"]),
 ("Lives each contestant starts with", "3", ["4", "5", "6"]),
 ("What a wrong answer costs you", "A life", ["Ten points", "Your turn", "A round"]),
 ("Questions each player gets in round one", "Two", ["One", "Four", "Five"]),
 ("What you do after a right answer in round two", "Nominate another contestant", ["Pass to your left", "Spin a wheel", "Pick a category"]),
 ("The choice put to the leader in the final", "Question or nominate", ["Stick or twist", "Higher or lower", "Gamble or bank"]),
 ("The most questions asked in the final", "40", ["20", "30", "50"]),
 ("How the contestants stood", "In a semicircle", ["In two rows", "Around a table", "Behind a long desk"]),
 ("When it was shown", "Weekday afternoons", ["Saturday nights", "Sunday mornings", "Late at night"]),
 ("Who played in the series Grand Final", "The 15 top scorers of the series", ["The 15 youngest players", "15 viewers picked by post", "15 past champions"]),
 ("The comedian who hosted the 2013 celebrity special", "Adam Hills", ["Alan Davies", "Jimmy Carr", "Rob Brydon"]),
 ("His Channel 4 show", "The Last Leg", ["The Mash Report", "8 Out of 10 Cats", "Have I Got News for You"]),
 ("Who hosted the daytime revival from 2014", "Sandi Toksvig", ["Sue Perkins", "Clare Balding", "Victoria Coren Mitchell"]),
 ("The panel show she took over in 2016", "QI", ["Would I Lie to You?", "Mock the Week", "Just a Minute"])])

race("Have I Got News for You - name it", "Television", "medium", ["Have I Got News for You", "panel shows", "BBC"], [
 ("The original host", "Angus Deayton", ["Clive Anderson", "Nick Hancock", "Jack Dee"]),
 ("Hislop said that if a libel verdict against him was justice, he was...", "A banana", ["A Dutchman", "A monkey's uncle", "The Pope"]),
 ("The year he was sacked as host", "2002", ["1998", "2005", "2008"]),
 ("The captain who edits a satirical magazine", "Ian Hislop", ["Richard Ingrams", "Andrew Marr", "Nick Robinson"]),
 ("The magazine", "Private Eye", ["The Spectator", "Punch", "The Oldie"]),
 ("The year he became its editor", "1986", ["1979", "1983", "1992"]),
 ("The other team captain", "Paul Merton", ["Frank Skinner", "Phill Jupitus", "Sean Lock"]),
 ("The Radio 4 word game he is a regular on", "Just a Minute", ["I'm Sorry I Haven't a Clue", "The Unbelievable Truth", "The Now Show"]),
 ("The Radio 4 show it grew out of", "The News Quiz", ["Week Ending", "Round the Horne", "Dead Ringers"]),
 ("The year it began", "1990", ["1988", "1994", "1996"]),
 ("The channel it started on", "BBC Two", ["Channel 4", "ITV", "Channel 5"]),
 ("The channel it moved to", "BBC One", ["Channel 4", "ITV", "Sky One"]),
 ("The night it is usually on", "Friday", ["Monday", "Wednesday", "Sunday"]),
 ("Players on each team", "2", ["1", "3", "4"]),
 ("The company that makes it", "Hat Trick Productions", ["Talkback", "Tiger Aspect", "Endemol"]),
 ("What sat in Roy Hattersley's seat when he pulled out", "A tub of lard", ["A cardboard cut-out", "An empty chair", "A teddy bear"]),
 ("The future Prime Minister who guest-hosted", "Boris Johnson", ["Theresa May", "David Cameron", "Gordon Brown"]),
 ("The guest host with the most appearances", "Alexander Armstrong", ["Jeremy Clarkson", "Martin Clunes", "Jo Brand"]),
 ("The round where you fill gaps in headlines", "Missing Words", ["Blank Headlines", "Fill the Gap", "Finish the Story"]),
 ("The round where one of four doesn't belong", "Odd One Out", ["Spot the Link", "Four of a Kind", "Picture This"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-276.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
