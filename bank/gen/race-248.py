# Bank session 18 Oct 2026: 2 quiz-show races -> bank/race-248.json (Only Connect; Tipping Point).
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

race("Only Connect - name it", "Television", "hard", ["Only Connect", "quiz shows", "BBC"], [
 ("The host", "Victoria Coren Mitchell", ["Victoria Wood", "Victoria Derbyshire", "Victoria Pendleton"]),
 ("The channel it started on", "BBC Four", ["BBC Three", "ITV4", "Channel 4"]),
 ("The year it began", "2008", ["2004", "2011", "2014"]),
 ("Its reputation", "The hardest quiz on TV", ["The friendliest quiz", "The fastest quiz", "The noisiest quiz"]),
 ("Rounds in each match", "4", ["6", "7", "8"]),
 ("Players in each team", "3", ["2", "6", "7"]),
 ("What the clue sets are picked with", "Egyptian hieroglyphs", ["Greek letters", "Roman numerals", "Chess pieces"]),
 ("One of those symbols", "Two Reeds", ["Two Sticks", "Three Feathers", "Twin Rushes"]),
 ("The symbol that's an eye", "Eye of Horus", ["Eye of Osiris", "Eye of Anubis", "Eye of Isis"]),
 ("Seconds to answer in round one", "40", ["30", "60", "90"]),
 ("Most points for guessing round one on the first clue", "5", ["1", "9", "15"]),
 ("What round two asks you to finish", "Sequences", ["Pairs", "Opposites", "Anagrams"]),
 ("The 16-clue round", "The Connecting Wall", ["The Brick Wall", "The Puzzle Wall", "The Word Wall"]),
 ("Clues on the wall", "16", ["12", "20", "25"]),
 ("Most points from a wall", "10", ["8", "12", "20"]),
 ("The buzzer round at the end", "Missing Vowels", ["Hidden Letters", "Lost Consonants", "Vowel Play"]),
 ("The host's husband", "David Mitchell", ["Robert Webb", "Jack Dee", "Lee Mack"]),
 ("The game she won big at", "Poker", ["Bridge", "Chess", "Scrabble"]),
 ("Her journalist father", "Alan Coren", ["Alan Bennett", "Alan Partridge", "Alan Davies"]),
 ("Her restaurant-critic brother", "Giles Coren", ["Giles Brandreth", "Giles Fraser", "Giles Terera"])])

race("Tipping Point - name it", "Television", "medium", ["Tipping Point", "game shows", "ITV"], [
 ("The host", "Ben Shephard", ["Ben Fogle", "Ben Miller", "Ben Elton"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "Channel 5"]),
 ("The year it began", "2012", ["2008", "2015", "2018"]),
 ("When it's on, on weekdays", "Afternoon", ["Breakfast", "Late night", "Lunchtime"]),
 ("What the giant machine is based on", "An arcade coin pusher", ["A pinball table", "A fruit machine", "A claw grabber"]),
 ("What drops into it", "Counters", ["Coins", "Tokens", "Marbles"]),
 ("What pushes them forward", "A moving shelf", ["A spinning wheel", "A magnet", "A jet of air"]),
 ("Drop zones at the top", "4", ["2", "3", "6"]),
 ("What a right answer earns you", "A counter to drop", ["A coin", "A token", "Ten points"]),
 ("The counter worth twice as much", "Double counter", ["Golden counter", "Bonus counter", "Lucky counter"]),
 ("The counter that wins a surprise", "Mystery prize counter", ["Golden counter", "Surprise counter", "Wild counter"]),
 ("Players who reach the final", "1", ["2", "3", "5"]),
 ("The top prize", "£10,000", ["£5,000", "£20,000", "£50,000"]),
 ("The choice at the end", "Take the money or go for the jackpot", ["Swap or stick", "Double or quits", "Higher or lower"]),
 ("The celebrity version", "Tipping Point: Lucky Stars", ["Tipping Point All Stars", "Celebrity Tipping Point", "Tipping Point Champions"]),
 ("The breakfast show the host made his name on", "GMTV", ["BBC Breakfast", "TV-am", "The Big Breakfast"]),
 ("The breakfast show he co-hosts now", "Good Morning Britain", ["This Morning", "Lorraine", "Daybreak"]),
 ("The game show he revived in 2009", "The Krypton Factor", ["Bullseye", "Blockbusters", "Countdown"]),
 ("The obstacle show he co-hosted", "Ninja Warrior UK", ["Gladiators", "Total Wipeout", "The Cube"]),
 ("His football-pundit co-host on it", "Chris Kamara", ["Jeff Stelling", "Paul Merson", "Matt Le Tissier"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-248.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
