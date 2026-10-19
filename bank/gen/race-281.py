# Bank session 19 Oct 2026: 2 races -> bank/race-281.json (The Bill; The Sweeney).
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

race("The Bill - name it", "Television", "medium", ["The Bill", "police", "ITV"], [
 ("The police station", "Sun Hill", ["Fenchurch East", "Kingsmarkham", "Denton"]),
 ("The made-up borough it covers", "Canley", ["Walford", "Weatherfield", "Holby"]),
 ("The city", "London", ["Manchester", "Birmingham", "Liverpool"]),
 ("What the title means", "Slang for the police", ["A pub bill", "A law going through Parliament", "A copper's first name"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The ITV company that made it", "Thames Television", ["Granada", "Central", "Yorkshire Television"]),
 ("The one-off drama it grew out of", "Woodentop", ["Copper", "Beat", "The Nick"]),
 ("The year that drama was shown", "1983", ["1979", "1987", "1990"]),
 ("The writer who created it", "Geoff McQueen", ["Lynda La Plante", "Jimmy McGovern", "Tony Jordan"]),
 ("The year it ended", "2010", ["2004", "2007", "2013"]),
 ("The theme tune", "Overkill", ["Kickback", "Night Beat", "The Chase"]),
 ("The long-serving woman officer", "June Ackland", ["Jane Tennison", "Jackie Reid", "Kate Fleming"]),
 ("The actress who played her", "Trudie Goodwin", ["Tracy-Ann Oberman", "Tessa Peake-Jones", "Trudie Styler"]),
 ("The moaning PC always filing complaints", "Reg Hollis", ["Reg Holdsworth", "Reg Cox", "Reg Varney"]),
 ("The actor who played him", "Jeff Stewart", ["Jeff Rawle", "Jeff Stelling", "Jeff Goldblum"]),
 ("The hard-man detective inspector", "Frank Burnside", ["Frank Butcher", "Frank Gallagher", "Frank Spencer"]),
 ("The actor who played him", "Christopher Ellison", ["Christopher Eccleston", "Christopher Biggins", "Christopher Timothy"]),
 ("That detective's own spin-off", "Burnside", ["Sun Hill CID", "Canley Nights", "Cryer's Law"]),
 ("Scruffy DC Tosh's surname", "Lines", ["Lynch", "Lomas", "Lane"]),
 ("The actor who played Sergeant Bob Cryer", "Eric Richard", ["Eric Sykes", "Eric Idle", "Eric Porter"])])

race("The Sweeney - name it", "Television", "medium", ["The Sweeney", "police", "ITV"], [
 ("The actor who played Jack Regan", "John Thaw", ["John Nettles", "Michael Elphick", "Lewis Collins"]),
 ("The actor who played George Carter", "Dennis Waterman", ["Martin Shaw", "Gareth Hunt", "Patrick Mower"]),
 ("Regan's rank", "Detective Inspector", ["Detective Sergeant", "Chief Inspector", "Superintendent"]),
 ("The squad they worked for", "Flying Squad", ["Special Branch", "Vice Squad", "Serious Crime Squad"]),
 ("Where the name comes from", "Rhyming slang: Sweeney Todd, Flying Squad", ["A real detective's surname", "A London street", "A police radio code"]),
 ("Regan's famous line", "Get your trousers on, you're nicked!", ["Evenin' all", "There's been a murder", "Book 'em, Danno"]),
 ("Their boss", "Frank Haskins", ["Frank Butcher", "Frank Gallagher", "Frank Spencer"]),
 ("The city", "London", ["Manchester", "Birmingham", "Glasgow"]),
 ("The channel", "ITV", ["BBC One", "BBC Two", "Channel 4"]),
 ("The film company that made it", "Euston Films", ["Granada", "LWT", "Central"]),
 ("The one-off drama that launched it", "Regan", ["Carter", "Squad Car", "The Squad"]),
 ("The year the series began", "1975", ["1970", "1979", "1983"]),
 ("The year it ended", "1978", ["1973", "1982", "1986"]),
 ("The comedy double act who guest-starred", "Morecambe and Wise", ["The Two Ronnies", "Cannon and Ball", "Little and Large"]),
 ("Feature films made from it in the 1970s", "2", ["1", "3", "4"]),
 ("The theme tune composer", "Harry South", ["Ron Grainer", "Tony Hatch", "Laurie Johnson"]),
 ("The year of the big-screen remake", "2012", ["2005", "2016", "2019"]),
 ("The remake's Regan", "Ray Winstone", ["Ross Kemp", "Danny Dyer", "Jason Statham"]),
 ("The musician who played Carter in the remake", "Plan B", ["Stormzy", "Example", "Professor Green"]),
 ("The lead actor's later Oxford detective", "Inspector Morse", ["Lewis", "Frost", "Barnaby"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-281.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
