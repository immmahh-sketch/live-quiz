# Bank session 18 Oct 2026: 2 races -> bank/race-228.json ('Allo 'Allo!; Grange Hill).
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

race("'Allo 'Allo! - name it", "British sitcoms", "medium", ["'Allo 'Allo", "sitcoms", "1980s TV", "BBC"], [
 ("The town where René runs his café", "Nouvion", ["Calais", "Rouen", "Amiens"]),
 ("René's surname", "Artois", ["Dupont", "Lafarge", "Moreau"]),
 ("René's tone-deaf wife, who sings in the café", "Edith", ["Odette", "Simone", "Colette"]),
 ("The waitress forever kissing René in the kitchen", "Yvette", ["Babette", "Juliette", "Colette"]),
 ("The Resistance leader who says 'Listen very carefully'", "Michelle", ["Marie", "Monique", "Madeleine"]),
 ("The tiny waitress who joined later", "Mimi", ["Fifi", "Gigi", "Lulu"]),
 ("The forger and master of disguise who loves Edith's mother", "Leclerc", ["Lefèvre", "Lambert", "Laurent"]),
 ("The undertaker in love with Edith", "Monsieur Alfonse", ["Monsieur Henri", "Monsieur Albert", "Monsieur Gaston"]),
 ("The sinister Gestapo man in the long black coat", "Herr Flick", ["Herr Schmidt", "Herr Müller", "Herr Braun"]),
 ("His devoted helper, Private …", "Helga", ["Greta", "Ingrid", "Hilde"]),
 ("The lieutenant always offering to show René his 'little tank'", "Gruber", ["Gerber", "Gruner", "Kruger"]),
 ("The German colonel in charge of the town", "Colonel von Strohm", ["Colonel Klink", "Colonel Schultz", "Colonel Hoffmann"]),
 ("The vain Italian officer", "Captain Bertorelli", ["Captain Rossi", "Captain Bellini", "Captain Mancini"]),
 ("The undercover English policeman with hopeless French", "Officer Crabtree", ["Officer Dibble", "Constable Savage", "PC Plod"]),
 ("His mangled greeting", "Good moaning", ["Bonjour, mate", "Hello, hello, hello", "Evening all"]),
 ("The stolen painting everyone is after", "The Fallen Madonna with the Big Boobies", ["The Weeping Duchess", "The Naked Shepherdess", "The Blushing Nun"]),
 ("What the painting gets hidden inside", "A sausage", ["A wheel of cheese", "A baguette", "A wine barrel"]),
 ("The actor who played René", "Gorden Kaye", ["Richard Briers", "Brian Murphy", "Arthur Lowe"]),
 ("David Croft's co-writer on the show", "Jeremy Lloyd", ["Jimmy Perry", "Ray Galton", "Barry Took"]),
 ("The year it began", "1982", ["1977", "1986", "1990"])])

race("Grange Hill - name it", "Television", "medium", ["Grange Hill", "children's TV", "school", "nostalgia"], [
 ("The writer who created it", "Phil Redmond", ["Tony Holland", "Julia Smith", "Jimmy McGovern"]),
 ("The year it began", "1978", ["1974", "1982", "1985"]),
 ("Peter Jenkins's nickname, the original cheeky hero", "Tucker", ["Tusker", "Tiger", "Taffy"]),
 ("The actor who played him, later Mark Fowler in 'EastEnders'", "Todd Carty", ["Nick Berry", "Adam Woodyatt", "Tom Watt"]),
 ("Tucker's own spin-off series", "Tucker's Luck", ["Tucker's Way", "Tucker's Mob", "Tucker Grows Up"]),
 ("Tucker's best mate, Benny …", "Green", ["Gray", "Brown", "White"]),
 ("The pupil whose heroin addiction shocked viewers", "Zammo", ["Pogo", "Hollo", "Stewpot"]),
 ("The cast's 1986 anti-drugs single", "Just Say No", ["Say No to Drugs", "Stay Clean", "Don't Do It"]),
 ("The school bully", "Gripper Stebson", ["Smasher Smith", "Dodger Doyle", "Grinder Gibson"]),
 ("The overweight boy often picked on", "Roland Browning", ["Ronald Brown", "Rowland Bates", "Roland Rat"]),
 ("The fearsome headmistress", "Mrs McClusky", ["Mrs McGonagall", "Miss Trunchbull", "Mrs Doyle"]),
 ("The strict teacher with the toupee", "Mr Bronson", ["Mr Chips", "Mr Garvey", "Mr Gilbert"]),
 ("The pupil who died in that teacher's car", "Danny Kendall", ["Danny Baker", "Danny Dyer", "Danny Kane"]),
 ("The pupil who was always running a money-making scheme", "Gonch", ["Fozzy", "Hollo", "Trevor"]),
 ("The theme tune", "Chicken Man", ["Popcorn", "Barnacle Bill", "Hot Butter"]),
 ("What the opening cartoon flicked off a fork", "A sausage", ["A pea", "A sprout", "A meatball"]),
 ("The made-up corner of London it was set in", "Northam", ["Walford", "Southam", "Eastbury"]),
 ("The city production moved to in 2003", "Liverpool", ["Manchester", "Birmingham", "Leeds"]),
 ("The year it ended", "2008", ["1998", "2003", "2012"]),
 ("The channel it began on", "BBC One", ["ITV", "Channel 4", "BBC Two"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-228.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
