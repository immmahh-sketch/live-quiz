# Bank session 18 Oct 2026: 2 quiz-show races -> bank/race-244.json (University Challenge; Who Wants to Be a Millionaire?).
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

race("University Challenge - name it", "Television", "medium", ["University Challenge", "quiz shows", "BBC"], [
 ("The first host", "Bamber Gascoigne", ["Magnus Magnusson", "Robert Robinson", "David Dimbleby"]),
 ("The famous line before each starter", "Your starter for ten", ["Come on down", "Let's play", "Here's your clue"]),
 ("The host from 1994 to 2023", "Jeremy Paxman", ["Jeremy Vine", "Jeremy Clarkson", "Jeremy Kyle"]),
 ("The host since 2023", "Amol Rajan", ["Nick Robinson", "Evan Davis", "Huw Edwards"]),
 ("The year it began", "1962", ["1958", "1966", "1971"]),
 ("The year the original ITV run ended", "1987", ["1980", "1992", "1997"]),
 ("The year the BBC brought it back", "1994", ["1990", "1999", "2002"]),
 ("The ITV company that first made it", "Granada", ["Yorkshire", "Tyne Tees", "Central"]),
 ("The channel it's on today", "BBC Two", ["BBC One", "ITV", "Channel 4"]),
 ("The American show it was based on", "College Bowl", ["Jeopardy!", "Quiz Kids", "The $64,000 Question"]),
 ("Who takes part", "University students", ["Sixth-formers", "Pensioners", "Teachers"]),
 ("Teams in each match", "2", ["1", "6", "8"]),
 ("Players in each team", "4", ["3", "6", "8"]),
 ("Points for a starter", "10", ["15", "20", "25"]),
 ("Points for each bonus", "5", ["3", "7", "15"]),
 ("The round where you identify images", "Picture round", ["Video round", "Map round", "Spelling round"]),
 ("The voice who announces who buzzed", "Roger Tilling", ["Peter Dickson", "Redd Pepper", "John Sachs"]),
 ("The Young Ones episode that spoofed it", "Bambi", ["Boring", "Cash", "Nasty"]),
 ("The university whose 1975 team answered 'Che Guevara' to everything", "Manchester", ["Oxford", "Liverpool", "Durham"]),
 ("The Oxford college of 2009's 'human Google', Gail Trimble", "Corpus Christi", ["Balliol", "Magdalen", "Christ Church"])])

race("Who Wants to Be a Millionaire? - name it", "Television", "medium", ["Who Wants to Be a Millionaire?", "quiz shows", "ITV"], [
 ("The original host", "Chris Tarrant", ["Chris Evans", "Chris Moyles", "Chris Packham"]),
 ("The host since 2018", "Jeremy Clarkson", ["Jeremy Vine", "Jeremy Kyle", "Jeremy Paxman"]),
 ("The year it began", "1998", ["1995", "2001", "2004"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "Sky One"]),
 ("Questions to win the million", "15", ["10", "12", "20"]),
 ("The lifeline where you ring someone", "Phone a Friend", ["Call a Mate", "Dial a Pal", "Ring a Friend"]),
 ("The lifeline that takes away two wrong answers", "50:50", ["Half and Half", "Two Down", "Split"]),
 ("The lifeline where the studio votes", "Ask the Audience", ["Ask the Crowd", "Poll the Room", "Ask the Studio"]),
 ("The lifeline added in the Clarkson years", "Ask the Host", ["Double Dip", "Second Chance", "Phone a Stranger"]),
 ("The host's famous question", "Is that your final answer?", ["Do you want to play on?", "Are you feeling lucky?", "Shall we take the money?"]),
 ("The round that picks who gets in the chair", "Fastest Finger First", ["Quickest on the Buzzer", "Speed Round", "First to Five"]),
 ("The first safe amount in the original show", "£1,000", ["£500", "£2,000", "£5,000"]),
 ("The second safe amount in the original show", "£32,000", ["£16,000", "£50,000", "£64,000"]),
 ("The first UK million winner", "Judith Keppel", ["Judith Chalmers", "Judith Kerr", "Judith Hann"]),
 ("The year she won", "2000", ["1999", "2002", "2005"]),
 ("The army major in the coughing scandal", "Charles Ingram", ["Charles Dance", "Charles Kennedy", "Charles Hazlewood"]),
 ("The college lecturer who coughed", "Tecwen Whittock", ["Trevor Whitlock", "Terence Wheaton", "Tegwyn Williams"]),
 ("The 2020 ITV drama about the scandal", "Quiz", ["Cough", "Final Answer", "The Major"]),
 ("The company that made it", "Celador", ["Endemol", "Talkback", "Hat Trick"]),
 ("The Oscar-winning film built around the Indian version", "Slumdog Millionaire", ["Life of Pi", "Lion", "The Million Pound Note"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-244.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
