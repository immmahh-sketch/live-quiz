# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-266.json (My Family; Outnumbered).
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

race("My Family - name it", "Television", "medium", ["My Family", "sitcoms", "BBC"], [
 ("The family", "The Harpers", ["The Hoopers", "The Harveys", "The Hollands"]),
 ("The part of London they live in", "Chiswick", ["Clapham", "Croydon", "Camden"]),
 ("Dad", "Ben", ["Bill", "Bob", "Barry"]),
 ("The actor who played him", "Robert Lindsay", ["Robert Powell", "Robert Carlyle", "Robert Webb"]),
 ("That actor's 1970s sitcom", "Citizen Smith", ["Butterflies", "Bread", "Rising Damp"]),
 ("Dad's job", "Dentist", ["Doctor", "Vet", "Optician"]),
 ("Mum", "Susan", ["Sarah", "Sally", "Sandra"]),
 ("The actress who played her", "Zoë Wanamaker", ["Zoë Ball", "Zoë Lucker", "Zoe Sugg"]),
 ("Mum's job", "Tour guide", ["Teacher", "Nurse", "Estate agent"]),
 ("Their three children", "Nick, Janey and Michael", ["Nick, Jenny and Mark", "Neil, Janey and Matt", "Nick, Jane and Martin"]),
 ("The actor who played Nick", "Kris Marshall", ["Kris Akabusi", "Chris Martin", "Kris Hallenga"]),
 ("The BBC detective series he later led", "Death in Paradise", ["Midsomer Murders", "Shetland", "Vera"]),
 ("The actress who played Janey", "Daniela Denby-Ashe", ["Daniela Nardini", "Daniela Hantuchová", "Danielle Lineker"]),
 ("The actor who played Michael", "Gabriel Thomson", ["Gabriel Byrne", "Gabriel Macht", "Gabriel Clarke"]),
 ("Its creator", "Fred Barron", ["Fred Elliott", "Fred Dinenage", "Fred Talbot"]),
 ("The country he came from", "USA", ["Canada", "Australia", "Ireland"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "2000", ["1996", "2004", "2008"]),
 ("The year it ended", "2011", ["2008", "2014", "2017"]),
 ("Series made", "11", ["7", "9", "13"])])

race("Outnumbered - name it", "Television", "medium", ["Outnumbered", "sitcoms", "BBC"], [
 ("The family", "The Brockmans", ["The Brockleys", "The Brookes", "The Broadmans"]),
 ("Dad", "Pete", ["Paul", "Phil", "Patrick"]),
 ("The actor who played him", "Hugh Dennis", ["Hugh Laurie", "Hugh Grant", "Hugh Bonneville"]),
 ("That actor's topical panel show", "Mock the Week", ["Have I Got News for You", "QI", "Would I Lie to You?"]),
 ("Dad's job", "History teacher", ["Maths teacher", "Dentist", "Accountant"]),
 ("Mum", "Sue", ["Sally", "Sarah", "Sam"]),
 ("The actress who played her", "Claire Skinner", ["Claire Sweeney", "Claire Foy", "Claire King"]),
 ("The three children", "Jake, Ben and Karen", ["Josh, Ben and Kirsty", "Jake, Billy and Kate", "Jack, Ben and Karen"]),
 ("The actor who played Jake", "Tyger Drew-Honey", ["Taylor Drew-Hughes", "Tyler Drew", "Ty Drew-Holmes"]),
 ("The actor who played Ben", "Daniel Roche", ["Daniel Radcliffe", "Daniel Craig", "Daniel Kaluuya"]),
 ("The actress who played Karen", "Ramona Marquez", ["Ramona Shelburne", "Rosie Marquez", "Romola Garai"]),
 ("What Karen is famous for", "Endless awkward questions", ["Never speaking", "Singing", "Sleepwalking"]),
 ("What the child actors often did", "Improvised their lines", ["Wrote the scripts", "Sang the theme", "Directed episodes"]),
 ("The writers", "Andy Hamilton and Guy Jenkin", ["Galton and Simpson", "Marks and Gran", "Croft and Perry"]),
 ("Their earlier newsroom sitcom", "Drop the Dead Donkey", ["The Day Today", "The Thick of It", "Hot Metal"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "2007", ["2003", "2010", "2014"]),
 ("Series made", "5", ["3", "4", "7"]),
 ("The year of its first comeback special", "2016", ["2012", "2019", "2022"]),
 ("The family's city", "London", ["Manchester", "Bristol", "Leeds"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-266.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
