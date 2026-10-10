# Bank session 10 Oct 2026: 20 more Put in order questions -> bank/order-3.json. Checked against every order question in
# the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Music", ["notes", "music theory"], "medium", "Put these musical notes in order of length, longest first", ["Semibreve", "Minim", "Crotchet", "Quaver", "Semiquaver"], "longest first")
o("Science", ["temperature"], "medium", "Put these temperatures in order, coldest first", ["Absolute zero", "Dry ice", "Water freezing", "Inside a fridge", "Human body", "Water boiling"], "coldest first")
o("Britain", ["railways", "North East"], "medium", "Put these East Coast Main Line stations in order, heading north from London King's Cross", ["Peterborough", "Doncaster", "York", "Darlington", "Durham", "Newcastle", "Berwick-upon-Tweed"], "heading north")
o("Nature", ["dogs", "size"], "easy", "Put these dog breeds in order of size, smallest first", ["Chihuahua", "Jack Russell", "Beagle", "Border Collie", "Labrador", "Great Dane"], "smallest first")
o("Everyday life", ["weddings"], "easy", "Put these moments of a traditional British wedding day in order", ["Bride arrives", "Vows exchanged", "Register signed", "Confetti thrown", "Wedding breakfast", "Speeches", "First dance"], "first to last")
o("Sport", ["football", "cup ties"], "easy", "Put these stages of a knockout cup tie in order", ["Kick-off", "Half-time", "Second half", "Extra time", "Penalty shoot-out"], "first to last")
o("Sport", ["Formula One"], "easy", "Put these parts of a Formula One race weekend in order", ["Practice", "Qualifying", "Formation lap", "Race start", "Chequered flag", "Podium"], "first to last")
o("Words and language", ["slang", "money"], "medium", "Put these slang amounts of money in order, smallest first", ["Fiver", "Tenner", "Score", "Pony", "Ton", "Monkey", "Grand"], "smallest first")
o("Sport", ["distances", "measurements"], "hard", "Put these sporting distances in order, shortest first", ["Darts throwing line to the board", "Length of a snooker table", "Penalty spot to the goal line", "Length of a cricket pitch", "Length of a tennis court", "An Olympic sprint (100m)"], "shortest first")
o("Science", ["weather", "clouds"], "hard", "Put these in order of how high they form, lowest first", ["Fog", "Stratus", "Altostratus", "Cirrus"], "lowest first")
o("Sport", ["team sizes"], "easy", "Put these sports in order of players per side on court or pitch, fewest first", ["Tennis singles", "Beach volleyball", "Basketball", "Netball", "Football", "Rugby union"], "fewest first")
o("Law", ["courts", "justice"], "easy", "Put these steps of a criminal case in order", ["Arrest", "Charge", "Plea", "Trial", "Verdict", "Sentence"], "first to last")
o("Royals", ["coronation"], "hard", "Put these parts of a British coronation service in order", ["Recognition", "Oath", "Anointing", "Crowning", "Enthronement", "Homage"], "first to last")
o("Music", ["Eurovision"], "easy", "Put these parts of a Eurovision final night in order", ["Opening act", "The songs", "Interval act", "Jury votes", "Public vote", "Winner sings again"], "first to last")
o("Sport", ["Olympics", "ceremonies"], "medium", "Put these moments of an Olympic opening ceremony in their traditional order", ["Greece's team enters", "Host nation's team enters", "Games declared open", "Olympic flag raised", "Athletes' oath taken", "Cauldron lit"], "first to last")
o("Games and toys", ["bingo"], "medium", "Put these bingo calls in number order, lowest first", ["Kelly's eye", "Legs eleven", "Key of the door", "Two little ducks", "Dirty Gertie", "Two fat ladies"], "lowest first")
o("Britain", ["police", "ranks"], "medium", "Put these police ranks in order, most junior first", ["Constable", "Sergeant", "Inspector", "Chief Inspector", "Superintendent", "Chief Superintendent", "Chief Constable"], "most junior first")
o("Everyday life", ["Scouts"], "medium", "Put these Scouts sections in age order, youngest first", ["Squirrels", "Beavers", "Cubs", "Scouts", "Explorers"], "youngest first")
o("Everyday life", ["university"], "easy", "Put these UK degree classes in order, lowest first", ["Third", "Lower second (2:2)", "Upper second (2:1)", "First"], "lowest first")
o("Religion", ["Church of England", "ranks"], "medium", "Put these Church of England ranks in order, most junior first", ["Deacon", "Priest", "Archdeacon", "Bishop", "Archbishop"], "most junior first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
