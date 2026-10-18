# Bank session 18 Oct 2026: 2 races -> bank/race-227.json (Auf Wiedersehen, Pet; Wacky Races and Hanna-Barbera).
# Topics found free by probing candidate answers against every race in stock; checked again with lqsql/audit/race-overlap.py.
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

race("Auf Wiedersehen, Pet - name it", "Television", "medium", ["Auf Wiedersehen Pet", "Geordie", "North East", "1980s TV"], [
 ("The German city where the gang first worked", "Düsseldorf", ["Hamburg", "Cologne", "Frankfurt"]),
 ("Played Oz, the loudmouth Geordie bricklayer", "Jimmy Nail", ["Robson Green", "Alun Armstrong", "Brian Glover"]),
 ("Played Dennis, the gang's foreman", "Tim Healy", ["Bill Treacher", "Robson Green", "Mark Benton"]),
 ("Played Neville, the homesick Geordie with the patient wife", "Kevin Whately", ["Alun Armstrong", "Brian Glover", "Mark Benton"]),
 ("Played Barry, the boring electrician from Wolverhampton", "Timothy Spall", ["Jasper Carrott", "Ricky Tomlinson", "Bill Treacher"]),
 ("Played Bomber, the gentle giant from Bristol", "Pat Roach", ["Big Daddy", "Giant Haystacks", "Dave Prowse"]),
 ("Played Wayne, the cockney carpenter", "Gary Holton", ["Phil Daniels", "Dennis Waterman", "Nicky Henson"]),
 ("Played Moxey, the Scouse plasterer", "Christopher Fairbank", ["Ricky Tomlinson", "Ken Jones", "Bernard Hill"]),
 ("The writing partnership, also behind 'Porridge'", "Clement and La Frenais", ["Galton and Simpson", "Croft and Perry", "Esmonde and Larbey"]),
 ("Who sang the theme, 'That's Livin' Alright'", "Joe Fagin", ["Jim Diamond", "Joe Brown", "Alvin Stardust"]),
 ("The ITV company it was made for", "Central", ["Granada", "Tyne Tees", "Thames"]),
 ("Neville's wife back home", "Brenda", ["Barbara", "Beverley", "Bridget"]),
 ("The year the first series went out", "1983", ["1980", "1986", "1989"]),
 ("The Spanish resort where series 2 ended up", "Marbella", ["Benidorm", "Torremolinos", "Magaluf"]),
 ("Where the 2002 revival sent them, with a bridge to rebuild", "Arizona", ["Texas", "Nevada", "New Mexico"]),
 ("The Teesside bridge they were hired to move", "Transporter Bridge", ["Tyne Bridge", "Swing Bridge", "Humber Bridge"]),
 ("Where the 2004 series took them", "Cuba", ["Mexico", "Jamaica", "Brazil"]),
 ("Jimmy Nail's later Newcastle detective show", "Spender", ["Byker Grove", "Wire in the Blood", "55 Degrees North"]),
 ("Jimmy Nail's 1992 UK number one", "Ain't No Doubt", ["Crocodile Shoes", "Love Don't Live Here Anymore", "Big River"]),
 ("Kevin Whately's later sergeant in 'Inspector Morse'", "Lewis", ["Strange", "Hathaway", "Morse"])])

race("Wacky Races and Hanna-Barbera - name it", "Television", "medium", ["cartoons", "Hanna-Barbera", "Wacky Races", "children's TV"], [
 ("The moustache-twirling villain of 'Wacky Races'", "Dick Dastardly", ["Snidely Whiplash", "Professor Pat Pending", "Sylvester Sneekly"]),
 ("His snickering dog", "Muttley", ["Droopy", "Astro", "Scooby-Dum"]),
 ("The glamorous driver of the Compact Pussycat", "Penelope Pitstop", ["Daphne Blake", "Jane Jetson", "Josie McCoy"]),
 ("The number on the villain's car", "00", ["13", "99", "007"]),
 ("The villain's car", "The Mean Machine", ["The Turbo Terrific", "The Bulletproof Bomb", "The Arkansas Chuggabug"]),
 ("The cry from Dastardly and Muttley's flying spin-off", "Stop the Pigeon", ["Catch That Pigeon", "Get the Bird", "Pigeon Patrol"]),
 ("The gangsters in the Bulletproof Bomb", "The Ant Hill Mob", ["The Bash Street Kids", "The Hole in the Wall Gang", "The Beagle Boys"]),
 ("The cavemen in the Boulder Mobile", "The Slag Brothers", ["The Flintstones", "The Rubbles", "The Gruesome Twosome"]),
 ("Fred Flintstone's famous cry", "Yabba Dabba Doo", ["Scooby Dooby Doo", "Hey Hey Hey", "Exit, stage left"]),
 ("The Scooby-Doo gang's van", "The Mystery Machine", ["The Spooky Bus", "The Clue Wagon", "The Ghost Van"]),
 ("Velma's catchphrase", "Jinkies", ["Zoinks", "Ruh-roh", "Jeepers"]),
 ("Scooby-Doo's little nephew", "Scrappy-Doo", ["Yabba-Doo", "Scooter", "Scooby-Dum"]),
 ("Yogi Bear's home park", "Jellystone", ["Yellowstone", "Greenstone", "Jollystone"]),
 ("Yogi's little sidekick", "Boo-Boo", ["Ranger Smith", "Cindy", "Bamm-Bamm"]),
 ("The New York alley cat who leads the gang", "Top Cat", ["Benny the Ball", "Officer Dibble", "Choo-Choo"]),
 ("The space-age family with a robot maid", "The Jetsons", ["The Flintstones", "The Robinsons", "The Spacelys"]),
 ("Fred Flintstone's best friend and neighbour", "Barney Rubble", ["Barney Gumble", "Mr Slate", "Dino"]),
 ("The pink mountain lion who says 'Heavens to Murgatroyd!'", "Snagglepuss", ["Pink Panther", "Peter Potamus", "Wally Gator"]),
 ("The kung fu dog who works as a police janitor", "Hong Kong Phooey", ["Secret Squirrel", "Atom Ant", "Dynomutt"]),
 ("The film studio where Hanna and Barbera met and made 'Tom and Jerry'", "MGM", ["Warner Bros", "Disney", "Paramount"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-227.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
