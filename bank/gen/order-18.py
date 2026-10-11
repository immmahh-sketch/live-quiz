# Bank session 11 Oct 2026: 12 more Put in order questions -> bank/order-15.json (party leaders, chancellors, reality winners, consoles and more).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
A("Franz Ferdinand", ["indie", "Glasgow"], "hard", ["Franz Ferdinand", "You Could Have It So Much Better", "Tonight", "Right Thoughts, Right Words, Right Action", "Always Ascending", "The Human Fear"])
A("Bloc Party", ["indie"], "hard", ["Silent Alarm", "A Weekend in the City", "Intimacy", "Four", "Hymns", "Alpha Games"])
o("Politics", ["Chancellors", "Treasury"], "hard", "Put these Chancellors of the Exchequer in order, earliest first", ["Nigel Lawson", "John Major", "Norman Lamont", "Kenneth Clarke", "Gordon Brown", "Alistair Darling", "George Osborne"], "earliest first")
o("Politics", ["Labour", "party leaders"], "medium", "Put these Labour leaders in order, earliest first", ["Harold Wilson", "Michael Foot", "Neil Kinnock", "John Smith", "Tony Blair", "Ed Miliband", "Jeremy Corbyn"], "earliest first")
o("Politics", ["Conservatives", "party leaders"], "medium", "Put these Conservative leaders in order, earliest first", ["Edward Heath", "Margaret Thatcher", "John Major", "William Hague", "Iain Duncan Smith", "Michael Howard", "David Cameron"], "earliest first")
o("Politics", ["Liberal Democrats", "party leaders"], "hard", "Put these Liberal Democrat leaders in order, earliest first", ["Paddy Ashdown", "Charles Kennedy", "Menzies Campbell", "Nick Clegg", "Tim Farron", "Vince Cable", "Ed Davey"], "earliest first")
o("Religion and myth", ["Church of England", "Archbishops of Canterbury"], "hard", "Put these Archbishops of Canterbury in order, earliest first", ["Donald Coggan", "Robert Runcie", "George Carey", "Rowan Williams", "Justin Welby"], "earliest first")
o("Sport", ["tennis", "Wimbledon"], "medium", "Put these men in order of their first Wimbledon singles title, earliest first", ["Björn Borg", "John McEnroe", "Boris Becker", "Pete Sampras", "Roger Federer", "Andy Murray", "Carlos Alcaraz"], "earliest first")
o("Football", ["Ballon d'Or"], "hard", "Put these players in order of their first Ballon d'Or, earliest first", ["George Best", "Johan Cruyff", "Michael Owen", "Cristiano Ronaldo", "Lionel Messi", "Luka Modrić", "Rodri"], "earliest first")
o("Games", ["PlayStation", "Xbox", "consoles"], "medium", "Put these games consoles in order of UK release, earliest first", ["PlayStation", "PlayStation 2", "Xbox", "Xbox 360", "PlayStation 3", "Xbox One", "Xbox Series X"], "earliest first")
o("TV", ["Big Brother", "reality TV"], "hard", "Put these Big Brother winners in order, earliest first", ["Craig Phillips", "Brian Dowling", "Kate Lawler", "Cameron Stout", "Nadia Almada", "Anthony Hutton", "Pete Bennett"], "earliest first")
o("TV", ["The Apprentice", "reality TV"], "hard", "Put these Apprentice winners in order, earliest first", ["Tim Campbell", "Michelle Dewberry", "Simon Ambrose", "Lee McQueen", "Yasmina Siadatan", "Stella English", "Tom Pellereau"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-15.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
