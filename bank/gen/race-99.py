# Bank session 10 Oct 2026: 2 more general races -> bank/race-99.json (jobs before fame, famous siblings). 20 rows each, target 10; wrong options are
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

race("what was their job before they were famous?", "Famous people", "medium", ["celebrities", "jobs", "wow"], [
 ("Sting", "Teacher", ["Postman", "Bus conductor", "Window cleaner"]),
 ("Rod Stewart", "Gravedigger", ["Butcher", "Bricklayer", "Bin man"]),
 ("Harrison Ford", "Carpenter", ["Plumber", "Taxi driver", "Lifeguard"]),
 ("Sean Connery", "Milkman", ["Postman", "Coal miner", "Bus conductor"]),
 ("Danny DeVito", "Hairdresser", ["Waiter", "Florist", "Tailor"]),
 ("Whoopi Goldberg", "Mortuary make-up artist", ["Nurse", "Dental nurse", "Florist"]),
 ("Christopher Walken", "Lion tamer", ["Lifeguard", "Chimney sweep", "Ice cream seller"]),
 ("Elvis Presley", "Lorry driver", ["Taxi driver", "Bin man", "Car salesman"]),
 ("Ozzy Osbourne", "Slaughterhouse worker", ["Coal miner", "Bricklayer", "Chimney sweep"]),
 ("Gordon Ramsay", "Footballer", ["Policeman", "Estate agent", "Lifeguard"]),
 ("Hugh Jackman", "Children's party clown", ["Lifeguard", "Ice cream seller", "Car salesman"]),
 ("Simon Cowell", "Post room clerk", ["Estate agent", "Car salesman", "Shop assistant"]),
 ("Madonna", "Doughnut shop worker", ["Shop assistant", "Florist", "Dental nurse"]),
 ("Brad Pitt", "Man in a chicken costume", ["Lifeguard", "Ice cream seller", "Paperboy"]),
 ("Mr T", "Bodyguard", ["Policeman", "Bin man", "Taxi driver"]),
 ("Michael Caine", "Meat market porter", ["Coal miner", "Butcher", "Bus conductor"]),
 ("Steve Buscemi", "Firefighter", ["Policeman", "Taxi driver", "Paperboy"]),
 ("Tom Hanks", "Hotel bellboy", ["Waiter", "Paperboy", "Shop assistant"]),
 ("Johnny Depp", "Selling pens over the phone", ["Car salesman", "Estate agent", "Window cleaner"]),
 ("Alan Rickman", "Graphic designer", ["Accountant", "Estate agent", "Tailor"])])

race("who's the famous brother or sister?", "Famous people", "medium", ["celebrities", "families"], [
 ("Noel Gallagher", "Liam Gallagher", ["Paul Weller", "Richard Ashcroft", "Ian Brown"]),
 ("Venus Williams", "Serena Williams", ["Maria Sharapova", "Kim Clijsters", "Justine Henin"]),
 ("Dannii Minogue", "Kylie Minogue", ["Natalie Imbruglia", "Holly Valance", "Delta Goodrem"]),
 ("Prince William", "Prince Harry", ["Prince Edward", "Prince Andrew", "Peter Phillips"]),
 ("Jack Charlton", "Bobby Charlton", ["Bobby Moore", "Geoff Hurst", "Nobby Stiles"]),
 ("Phil Neville", "Gary Neville", ["Jamie Carragher", "Paul Scholes", "Nicky Butt"]),
 ("Andy Murray", "Jamie Murray", ["Tim Henman", "Greg Rusedski", "Kyle Edmund"]),
 ("Joseph Fiennes", "Ralph Fiennes", ["Kenneth Branagh", "Rufus Sewell", "Clive Owen"]),
 ("Julia Roberts", "Eric Roberts", ["Mickey Rourke", "Dennis Quaid", "Kurt Russell"]),
 ("Beyoncé", "Solange Knowles", ["Kelly Rowland", "Michelle Williams", "Ciara"]),
 ("Warren Beatty", "Shirley MacLaine", ["Faye Dunaway", "Natalie Wood", "Julie Christie"]),
 ("Maggie Gyllenhaal", "Jake Gyllenhaal", ["Tobey Maguire", "Heath Ledger", "Ryan Gosling"]),
 ("Ben Affleck", "Casey Affleck", ["Matt Damon", "Joaquin Phoenix", "Mark Ruffalo"]),
 ("Janet Jackson", "Michael Jackson", ["Prince", "Lionel Richie", "Stevie Wonder"]),
 ("Joan Collins", "Jackie Collins", ["Barbara Cartland", "Shirley Conran", "Jilly Cooper"]),
 ("Liam Hemsworth", "Chris Hemsworth", ["Chris Pratt", "Chris Pine", "Chris Evans"]),
 ("Alistair Brownlee", "Jonny Brownlee", ["Mo Farah", "Chris Hoy", "Bradley Wiggins"]),
 ("Elle Fanning", "Dakota Fanning", ["Chloë Grace Moretz", "Saoirse Ronan", "Abigail Breslin"]),
 ("Ed Miliband", "David Miliband", ["David Cameron", "Nick Clegg", "Ed Balls"]),
 ("Catherine, Princess of Wales", "Pippa Middleton", ["Zara Tindall", "Princess Beatrice", "Autumn Phillips"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-99.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
