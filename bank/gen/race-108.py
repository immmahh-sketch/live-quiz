# Bank session 10 Oct 2026: 2 more general races -> bank/race-108.json (memoirs, drummers). 20 rows each, target 10; wrong options are
# the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("whose memoir is this?", "Books", "medium", ["memoirs", "autobiographies", "famous people"], [
 ("Open", "Andre Agassi", ["Pete Sampras", "Boris Becker", "John McEnroe"]),
 ("Born a Crime", "Trevor Noah", ["Dave Chappelle", "Chris Rock", "Kevin Hart"]),
 ("Bossypants", "Tina Fey", ["Mindy Kaling", "Sarah Silverman", "Ellen DeGeneres"]),
 ("Yes Please", "Amy Poehler", ["Mindy Kaling", "Sarah Silverman", "Lena Dunham"]),
 ("Is It Just Me?", "Miranda Hart", ["Sarah Millican", "Jo Brand", "Victoria Wood"]),
 ("Dear Fatty", "Dawn French", ["Jennifer Saunders", "Jo Brand", "Victoria Wood"]),
 ("My Side", "David Beckham", ["Gary Neville", "Wayne Rooney", "Steven Gerrard"]),
 ("Managing My Life", "Alex Ferguson", ["Arsène Wenger", "Kenny Dalglish", "Bobby Robson"]),
 ("Life", "Keith Richards", ["Mick Jagger", "Ronnie Wood", "Ozzy Osbourne"]),
 ("Chronicles: Volume One", "Bob Dylan", ["Leonard Cohen", "Neil Young", "Paul Simon"]),
 ("Just Kids", "Patti Smith", ["Joni Mitchell", "Chrissie Hynde", "Kim Gordon"]),
 ("Me", "Elton John", ["Rod Stewart", "George Michael", "Freddie Mercury"]),
 ("Face It", "Debbie Harry", ["Chrissie Hynde", "Siouxsie Sioux", "Kim Gordon"]),
 ("Born to Run", "Bruce Springsteen", ["Jon Bon Jovi", "Billy Joel", "Tom Petty"]),
 ("This Is Going to Hurt", "Adam Kay", ["Ben Goldacre", "Michael Mosley", "Henry Marsh"]),
 ("My Booky Wook", "Russell Brand", ["Noel Fielding", "Jimmy Carr", "Frankie Boyle"]),
 ("Moab Is My Washpot", "Stephen Fry", ["Hugh Laurie", "Rowan Atkinson", "Alan Davies"]),
 ("Scar Tissue", "Anthony Kiedis", ["Flea", "Eddie Vedder", "Chris Cornell"]),
 ("The Storyteller", "Dave Grohl", ["Taylor Hawkins", "Eddie Vedder", "Josh Homme"]),
 ("Total Recall, named after one of his own films", "Arnold Schwarzenegger", ["Sylvester Stallone", "Bruce Willis", "Jean-Claude Van Damme"])])

race("which band did this drummer play in?", "Music", "hard", ["drummers", "bands"], [
 ("Charlie Watts", "The Rolling Stones", ["The Kinks", "The Animals", "The Yardbirds"]),
 ("Keith Moon", "The Who", ["The Kinks", "Small Faces", "The Move"]),
 ("John Bonham", "Led Zeppelin", ["Cream", "Free", "Bad Company"]),
 ("Roger Taylor, alongside Freddie Mercury", "Queen", ["Thin Lizzy", "Status Quo", "ELO"]),
 ("Phil Collins, before his solo fame", "Genesis", ["Yes", "Emerson, Lake & Palmer", "Roxy Music"]),
 ("Dave Grohl, before he fronted his own band", "Nirvana", ["Pearl Jam", "Soundgarden", "Alice in Chains"]),
 ("Larry Mullen Jr.", "U2", ["Simple Minds", "INXS", "R.E.M."]),
 ("Lars Ulrich", "Metallica", ["Megadeth", "Slayer", "Anthrax"]),
 ("Nick Mason", "Pink Floyd", ["Yes", "Roxy Music", "10cc"]),
 ("Ian Paice", "Deep Purple", ["Rainbow", "Whitesnake", "Uriah Heep"]),
 ("Bill Ward", "Black Sabbath", ["Judas Priest", "Iron Maiden", "Motörhead"]),
 ("Taylor Hawkins", "Foo Fighters", ["Weezer", "Queens of the Stone Age", "Pearl Jam"]),
 ("Chad Smith", "Red Hot Chili Peppers", ["Faith No More", "Jane's Addiction", "Rage Against the Machine"]),
 ("Tré Cool", "Green Day", ["The Offspring", "Blink-182", "Sum 41"]),
 ("Dave Rowntree", "Blur", ["Pulp", "Oasis", "Suede"]),
 ("Reni", "The Stone Roses", ["Happy Mondays", "Inspiral Carpets", "The Charlatans"]),
 ("Matt Helders", "Arctic Monkeys", ["Kaiser Chiefs", "Kasabian", "Franz Ferdinand"]),
 ("Topper Headon", "The Clash", ["The Jam", "The Damned", "Buzzcocks"]),
 ("Rick Allen, who plays with one arm", "Def Leppard", ["Iron Maiden", "Whitesnake", "Saxon"]),
 ("Mike Joyce", "The Smiths", ["The Cure", "Joy Division", "Echo & the Bunnymen"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-108.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
