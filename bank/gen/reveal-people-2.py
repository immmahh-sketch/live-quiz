# Bank session 9 Oct 2026: more Picture Reveal faces -> bank/reveal-people-2.json
# (Wikipedia title, accepted answers, difficulty). Famous and guessable for a UK pub crowd; nobody already in reveal-people.json.
import json, os
P = [
 ("Lily Allen", ["Lily Allen", "Allen"], "medium"), ("Jessie J", ["Jessie J"], "medium"), ("Ronan Keating", ["Ronan Keating", "Keating"], "medium"),
 ("Gwen Stefani", ["Gwen Stefani", "Stefani"], "medium"), ("Jon Bon Jovi", ["Jon Bon Jovi", "Bon Jovi"], "medium"), ("Dave Grohl", ["Dave Grohl", "Grohl"], "hard"),
 ("Meat Loaf", ["Meat Loaf", "Meatloaf"], "medium"), ("Michael Bublé", ["Michael Bublé", "Michael Buble", "Buble"], "medium"), ("Andrea Bocelli", ["Andrea Bocelli", "Bocelli"], "medium"),
 ("Luciano Pavarotti", ["Luciano Pavarotti", "Pavarotti"], "easy"), ("Barry Manilow", ["Barry Manilow", "Manilow"], "hard"), ("Neil Diamond", ["Neil Diamond"], "hard"),
 ("Shawn Mendes", ["Shawn Mendes", "Mendes"], "hard"), ("Alice Cooper", ["Alice Cooper"], "medium"), ("Usher (musician)", ["Usher"], "medium"),
 ("Patrick Stewart", ["Patrick Stewart", "Stewart"], "medium"), ("Steve Carell", ["Steve Carell", "Carell"], "medium"), ("Jack Black", ["Jack Black"], "medium"),
 ("Will Ferrell", ["Will Ferrell", "Ferrell"], "medium"), ("Adam Sandler", ["Adam Sandler", "Sandler"], "medium"), ("Ben Stiller", ["Ben Stiller", "Stiller"], "medium"),
 ("Eddie Murphy", ["Eddie Murphy", "Murphy"], "easy"), ("Danny DeVito", ["Danny DeVito", "Danny De Vito", "DeVito"], "easy"), ("Jack Nicholson", ["Jack Nicholson", "Nicholson"], "medium"),
 ("Al Pacino", ["Al Pacino", "Pacino"], "medium"), ("Dustin Hoffman", ["Dustin Hoffman", "Hoffman"], "hard"), ("Mark Wahlberg", ["Mark Wahlberg", "Wahlberg"], "medium"),
 ("Matthew McConaughey", ["Matthew McConaughey", "McConaughey"], "medium"), ("Robert Pattinson", ["Robert Pattinson", "Pattinson"], "medium"), ("Daniel Day-Lewis", ["Daniel Day-Lewis", "Day-Lewis"], "hard"),
 ("Ralph Fiennes", ["Ralph Fiennes", "Fiennes"], "hard"), ("David Jason", ["David Jason", "Jason"], "easy"), ("Warwick Davis", ["Warwick Davis"], "medium"),
 ("John Travolta", ["John Travolta", "Travolta"], "easy"), ("Olivia Newton-John", ["Olivia Newton-John", "Olivia Newton John"], "medium"), 
 ("Bill Murray", ["Bill Murray"], "hard"), ("Ant McPartlin", ["Ant McPartlin", "Ant"], "easy"), ("Declan Donnelly", ["Declan Donnelly", "Dec"], "easy"),
 ("Michael Palin", ["Michael Palin", "Palin"], "medium"), ("John Cleese", ["John Cleese", "Cleese"], "medium"), ("Ronnie Corbett", ["Ronnie Corbett", "Corbett"], "medium"),
 ("Ronnie Barker", ["Ronnie Barker", "Barker"], "medium"), ("Eric Morecambe", ["Eric Morecambe", "Morecambe"], "medium"), ("Paul O'Grady", ["Paul O'Grady", "O'Grady"], "medium"),
 ("Bob Mortimer", ["Bob Mortimer", "Mortimer"], "medium"), ("Harry Hill", ["Harry Hill"], "easy"), 
 ("Matt Lucas", ["Matt Lucas", "Lucas"], "medium"), ("David Walliams", ["David Walliams", "Walliams"], "easy"), ("Nigella Lawson", ["Nigella Lawson", "Nigella"], "easy"),
 ("Delia Smith", ["Delia Smith", "Delia"], "medium"), ("Gino D'Acampo", ["Gino D'Acampo", "Gino"], "medium"), ("Gary Neville", ["Gary Neville", "Neville"], "medium"),
 ("Gabby Logan", ["Gabby Logan", "Logan"], "hard"), ("Frank Lampard", ["Frank Lampard", "Lampard"], "medium"), ("Michael Owen", ["Michael Owen", "Owen"], "medium"),
 ("Ryan Giggs", ["Ryan Giggs", "Giggs"], "medium"), ("Eric Cantona", ["Eric Cantona", "Cantona"], "medium"), ("Ian Botham", ["Ian Botham", "Botham", "Beefy"], "medium"),
 ("Phil Taylor (darts player)", ["Phil Taylor", "The Power"], "medium"), ("Lennox Lewis", ["Lennox Lewis"], "medium"), ("Chris Eubank", ["Chris Eubank", "Eubank"], "medium"),
 ("Bradley Wiggins", ["Bradley Wiggins", "Wiggins", "Wiggo"], "medium"), ("Daley Thompson", ["Daley Thompson"], "hard"),
 ("Michael Schumacher", ["Michael Schumacher", "Schumacher"], "medium"), ("Ayrton Senna", ["Ayrton Senna", "Senna"], "hard"), ("John McEnroe", ["John McEnroe", "McEnroe"], "medium"),
 ("Nick Faldo", ["Nick Faldo", "Faldo"], "hard"), ("Tim Henman", ["Tim Henman", "Henman"], "medium"), ("Conor McGregor", ["Conor McGregor", "McGregor"], "medium"),
 ("Floyd Mayweather Jr.", ["Floyd Mayweather", "Mayweather"], "hard"), ("Queen Camilla", ["Queen Camilla", "Camilla"], "easy"), ("Anne, Princess Royal", ["Princess Anne", "The Princess Royal", "Anne"], "medium"),
 ("Greta Thunberg", ["Greta Thunberg", "Thunberg"], "medium"), ("Malala Yousafzai", ["Malala Yousafzai", "Malala"], "hard"), ("Mark Zuckerberg", ["Mark Zuckerberg", "Zuckerberg"], "medium"),
 ("Jeff Bezos", ["Jeff Bezos", "Bezos"], "medium"), ("David Cameron", ["David Cameron", "Cameron"], "easy"), ("Gordon Brown", ["Gordon Brown"], "medium"),
 ("Nicola Sturgeon", ["Nicola Sturgeon", "Sturgeon"], "medium"), ("John F. Kennedy", ["John F. Kennedy", "JFK", "John Kennedy", "Kennedy"], "easy"), ("Abraham Lincoln", ["Abraham Lincoln", "Lincoln"], "easy"),
 ("Charles Darwin", ["Charles Darwin", "Darwin"], "medium"), ("Florence Nightingale", ["Florence Nightingale", "Nightingale"], "hard"), ("Agatha Christie", ["Agatha Christie", "Christie"], "hard"),
 ("Roald Dahl", ["Roald Dahl", "Dahl"], "hard"), ("J. K. Rowling", ["J. K. Rowling", "JK Rowling", "Rowling"], "medium"), ("Andy Warhol", ["Andy Warhol", "Warhol"], "hard"),
 ("Charles Dickens", ["Charles Dickens", "Dickens"], "hard"),
 ("Sharon Osbourne", ["Sharon Osbourne", "Sharon"], "medium"), ("Joan Collins", ["Joan Collins", "Collins"], "medium"), ("Jamie Redknapp", ["Jamie Redknapp", "Redknapp"], "medium"), ("Paul Daniels", ["Paul Daniels", "Daniels"], "hard"),
]
here = os.path.dirname(os.path.abspath(__file__))
old = {p['title'].lower() for p in json.load(open(os.path.join(here, '..', 'reveal-people.json'), encoding='utf-8'))}
out = [{"title": t, "answers": a, "difficulty": d} for t, a, d in P if t.lower() not in old]
json.dump(out, open(os.path.join(here, '..', 'reveal-people-2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'people;', len(P) - len(out), 'already listed;', {d: sum(1 for x in out if x['difficulty'] == d) for d in ('easy', 'medium', 'hard')})
