# Bank session 18 Oct 2026: 2 game-show races -> bank/race-241.json (Countdown; Bullseye).
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

race("Countdown - name it", "Television", "medium", ["Countdown", "game shows", "Channel 4"], [
 ("The first presenter", "Richard Whiteley", ["Richard Madeley", "Richard Stilgoe", "Richard Baker"]),
 ("How many years he presented it", "23", ["10", "15", "28"]),
 ("The numbers whizz who started alongside him", "Carol Vorderman", ["Carol Smillie", "Carol Kirkwood", "Carol Decker"]),
 ("Who took over the numbers in 2009", "Rachel Riley", ["Rachel Stevens", "Rachel Johnson", "Rachel Hunter"]),
 ("The word expert in Dictionary Corner", "Susie Dent", ["Suzi Quatro", "Sue Perkins", "Susie Blake"]),
 ("The host after Whiteley died", "Des Lynam", ["Bruce Forsyth", "Paul Daniels", "Chris Tarrant"]),
 ("The football presenter who hosted from 2009", "Jeff Stelling", ["Jeff Brazier", "Gary Lineker", "Des Kelly"]),
 ("The Apprentice adviser who hosted from 2012", "Nick Hewer", ["Nick Hancock", "Nick Knowles", "Nick Owen"]),
 ("The Weakest Link host who took over in 2021", "Anne Robinson", ["Anne Diamond", "Anne Hegerty", "Ann Widdecombe"]),
 ("The host since 2022", "Colin Murray", ["Colin Jackson", "Colin Montgomerie", "Colin Firth"]),
 ("The channel", "Channel 4", ["BBC Two", "ITV", "Channel 5"]),
 ("When it was first shown", "Channel 4's opening day", ["Christmas Day", "New Year's Day", "Election night"]),
 ("The year", "1982", ["1979", "1985", "1988"]),
 ("Its first name as a Yorkshire regional show", "Calendar Countdown", ["Words and Numbers", "Calendar Quiz", "Letterbox"]),
 ("The ITV company behind that first version", "Yorkshire Television", ["Granada", "Tyne Tees", "Central"]),
 ("The French show it was based on", "Des chiffres et des lettres", ["Le Juste Prix", "Fort Boyard", "Questions pour un champion"]),
 ("Seconds on the famous clock", "30", ["20", "45", "60"]),
 ("The round where you pick consonants and vowels", "Letters round", ["Spelling round", "Vowel round", "Word round"]),
 ("Digits in the numbers round target", "3", ["2", "4", "5"]),
 ("Letters in the Conundrum", "9", ["7", "8", "11"])])

race("Bullseye - name it", "Television", "medium", ["Bullseye", "game shows", "darts", "ITV"], [
 ("The original host", "Jim Bowen", ["Jim Davidson", "Bob Monkhouse", "Bruce Forsyth"]),
 ("His famous praise", "Super, smashing, great!", ["Nice to see you, to see you nice!", "Come on down!", "Shut that door!"]),
 ("What he said as he showed losers the prize", "Look at what you could have won!", ["Better luck next time!", "Ooh, so close!", "That's the way the cookie crumbles!"]),
 ("His job before TV", "Teacher", ["Policeman", "Bus driver", "Butcher"]),
 ("The cartoon mascot", "Bully", ["Billy", "Butch", "Barney"]),
 ("The consolation gift you took home", "Bendy Bully", ["A Bully mug", "A bronze Bully", "A Bully badge"]),
 ("The darts commentator who kept the score", "Tony Green", ["Sid Waddell", "John Lowe", "Eric Bristow"]),
 ("How many pairs of contestants took part", "3", ["2", "4", "5"]),
 ("Who made up each pair", "A darts thrower and a question answerer", ["Two darts players", "A husband and wife", "Two quiz champions"]),
 ("The colour you wanted to hit to win money", "Red", ["Black", "Green", "White"]),
 ("What hitting the bull scored", "50", ["25", "60", "100"]),
 ("The final round", "Bully's Prize Board", ["Bully's Big Board", "The Jackpot Board", "The Final Throw"]),
 ("The star prize that famously went to landlocked winners", "A speedboat", ["A caravan", "A motorbike", "A sports car"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The ITV company that made it", "Central", ["Granada", "LWT", "Anglia"]),
 ("The year it began", "1981", ["1977", "1985", "1989"]),
 ("How many years the original ran", "14", ["8", "20", "25"]),
 ("The comedian who hosted the 2006 revival", "Dave Spikey", ["Dave Gorman", "Dave Lamb", "Dave Vitty"]),
 ("The channel that showed that revival", "Challenge", ["Dave", "Gold", "Sky One"]),
 ("The cricketer who hosted the 2024 revival", "Freddie Flintoff", ["Freddie Starr", "Bradley Walsh", "Paddy McGuinness"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-241.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
