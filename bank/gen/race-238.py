# Bank session 18 Oct 2026: 2 races -> bank/race-238.json (Absolutely Fabulous; The Royle Family).
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

race("Absolutely Fabulous - name it", "British sitcoms", "medium", ["Absolutely Fabulous", "sitcoms", "1990s TV", "Jennifer Saunders"], [
 ("The frantic PR boss", "Edina Monsoon", ["Edwina Monsoon", "Edina Monroe", "Edith Monsoon"]),
 ("Her best friend, a fashion magazine editor", "Patsy Stone", ["Patsy Stein", "Pansy Stone", "Patsy Stern"]),
 ("Edina's sensible, long-suffering daughter", "Saffron", ["Sorrel", "Sage", "Rosemary"]),
 ("Edina's hopeless assistant", "Bubble", ["Bunny", "Babe", "Pickle"]),
 ("Edina's son, who left home", "Serge", ["Sergio", "Stefan", "Sebastian"]),
 ("Saffron's father, Edina's ex-husband", "Justin", ["Marshall", "Julian", "Jasper"]),
 ("Edina's job", "PR", ["Fashion designer", "Magazine editor", "Interior designer"]),
 ("The part of London she lives in", "Holland Park", ["Notting Hill", "Chelsea", "Hampstead"]),
 ("Their favourite champagne, 'Bolly'", "Bollinger", ["Moët", "Krug", "Veuve Clicquot"]),
 ("Patsy's way of saying hello", "Sweetie, darling", ["Hiya, babe", "Ciao, bella", "Toodle-pip"]),
 ("The writer, who also plays Edina", "Jennifer Saunders", ["Dawn French", "Ruby Wax", "Victoria Wood"]),
 ("The actor who plays Patsy", "Joanna Lumley", ["Honor Blackman", "Diana Rigg", "Joan Collins"]),
 ("The actor who plays Saffron", "Julia Sawalha", ["Jessica Hynes", "Emma Bunton", "Sally Phillips"]),
 ("The actor who plays the assistant", "Jane Horrocks", ["Kathy Burke", "Sarah Lancashire", "Caroline Aherne"]),
 ("The actor who plays Edina's mother", "June Whitfield", ["Thora Hird", "Liz Smith", "Patricia Routledge"]),
 ("The double act whose sketch it grew out of", "French and Saunders", ["The Comic Strip", "Smack the Pony", "Girls on Top"]),
 ("Who sings 'This Wheel's on Fire' over the titles, with Adrian Edmondson", "Julie Driscoll", ["Dusty Springfield", "Lulu", "Sandie Shaw"]),
 ("The year it began", "1992", ["1988", "1996", "2000"]),
 ("The year of its last TV episode, a London Olympics special", "2012", ["2005", "2009", "2014"]),
 ("The year of the film", "2016", ["2010", "2013", "2019"])])

race("The Royle Family - name it", "British sitcoms", "medium", ["The Royle Family", "sitcoms", "Manchester", "BBC"], [
 ("The family's surname", "Royle", ["Royal", "Boyle", "Rolle"]),
 ("The dad's favourite reply", "My arse!", ["Lovely jubbly!", "Shut it!", "Bobbins!"]),
 ("The actor who played the dad, Jim", "Ricky Tomlinson", ["Bernard Hill", "Johnny Vegas", "Peter Kay"]),
 ("The actor who played the mum, Barbara", "Sue Johnston", ["Julie Walters", "Pauline Quirke", "Brenda Blethyn"]),
 ("Their daughter", "Denise", ["Diane", "Dawn", "Debbie"]),
 ("Her husband", "Dave", ["Darren", "Dennis", "Derek"]),
 ("His job", "Mobile DJ", ["Taxi driver", "Plumber", "Postman"]),
 ("The actor who played him", "Craig Cash", ["Steve Pemberton", "Craig Charles", "John Thomson"]),
 ("Their son", "Antony", ["Andrew", "Adam", "Alan"]),
 ("The actor who played the son", "Ralf Little", ["Ralph Ineson", "Joe Absolom", "Matthew Wolfenden"]),
 ("Nana's first name", "Norma", ["Nora", "Nancy", "Nellie"]),
 ("The actor who played Nana", "Liz Smith", ["Thora Hird", "June Whitfield", "Kathy Staff"]),
 ("The daughter's new baby", "Baby David", ["Baby Darren", "Baby Dean", "Baby Jack"]),
 ("Where nearly every scene takes place", "The living room", ["The kitchen", "The pub", "The car"]),
 ("The city it's set in", "Manchester", ["Liverpool", "Bolton", "Stockport"]),
 ("The writers", "Caroline Aherne and Craig Cash", ["Steve Coogan and Henry Normal", "Peter Kay and Paddy McGuinness", "Johnny Vegas and Steve Edge"]),
 ("Caroline Aherne's earlier chat-show character", "Mrs Merton", ["Mrs Brown", "Mrs Doyle", "Mrs Overall"]),
 ("The year it began", "1998", ["1994", "2001", "2004"]),
 ("How many series were made before the specials", "3", ["2", "5", "7"]),
 ("The 2006 special in which Nana dies", "The Queen of Sheba", ["Nana's Birthday", "The Last Supper", "Christmas at Jim's"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-238.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
