# Bank session 10 Oct 2026: 2 more general races -> bank/race-113.json (North East birthplaces, sporting terms). 20 rows each, target 10; wrong options are
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

race("which North East town or city were they born in?", "North East England", "hard", ["North East", "famous people", "birthplaces"], [
 ("Michael Carrick", "Wallsend", ["Blyth", "Whitley Bay", "Tynemouth"]),
 ("Cheryl", "Newcastle", ["Morpeth", "Blyth", "Whitley Bay"]),
 ("Paul Gascoigne", "Gateshead", ["Blyth", "Stanley", "Chester-le-Street"]),
 ("Rowan Atkinson", "Consett", ["Stanley", "Bishop Auckland", "Spennymoor"]),
 ("Jordan Henderson", "Sunderland", ["Seaham", "Houghton-le-Spring", "Peterlee"]),
 ("Sir Bobby Robson", "Sacriston", ["Chester-le-Street", "Stanley", "Spennymoor"]),
 ("Jack Charlton", "Ashington", ["Bedlington", "Morpeth", "Blyth"]),
 ("Catherine Cookson", "South Shields", ["Whitley Bay", "Seaham", "Tynemouth"]),
 ("Brendan Foster", "Hebburn", ["Blyth", "Tynemouth", "Seaham"]),
 ("Ross Noble", "Cramlington", ["Morpeth", "Bedlington", "Ponteland"]),
 ("Bryan Ferry", "Washington", ["Houghton-le-Spring", "Seaham", "Peterlee"]),
 ("Paul Collingwood", "Shotley Bridge", ["Stanley", "Bishop Auckland", "Prudhoe"]),
 ("Steph Houghton", "Durham", ["Bishop Auckland", "Spennymoor", "Peterlee"]),
 ("Lucy Bronze", "Berwick-upon-Tweed", ["Alnwick", "Seahouses", "Morpeth"]),
 ("Peter Beardsley", "Longbenton", ["Whitley Bay", "Blyth", "Ponteland"]),
 ("Brian Clough", "Middlesbrough", ["Stockton", "Redcar", "Darlington"]),
 ("Neil Tennant of the Pet Shop Boys", "North Shields", ["Whitley Bay", "Blyth", "Tynemouth"]),
 ("Jeff Stelling", "Hartlepool", ["Stockton", "Redcar", "Darlington"]),
 ("George Stephenson", "Wylam", ["Prudhoe", "Hexham", "Ponteland"]),
 ("Grace Darling", "Bamburgh", ["Seahouses", "Alnwick", "Amble"])])

race("which sport is this term from?", "Sport", "easy", ["sport", "words"], [
 ("A birdie", "Golf", ["Croquet", "Bowls", "Archery"]),
 ("Scoring a try", "Rugby union", ["Gaelic football", "Aussie rules", "Lacrosse"]),
 ("A maximum 147 break", "Snooker", ["Pool", "Bowls", "Table tennis"]),
 ("Hitting the bullseye", "Darts", ["Bowls", "Croquet", "Table tennis"]),
 ("Bowling a strike", "Ten-pin bowling", ["Bowls", "Croquet", "Curling"]),
 ("A touchdown", "American football", ["Aussie rules", "Gaelic football", "Lacrosse"]),
 ("A home run", "Baseball", ["Rounders", "Lacrosse", "Squash"]),
 ("A slam dunk", "Basketball", ["Volleyball", "Handball", "Water polo"]),
 ("Checkmate", "Chess", ["Draughts", "Backgammon", "Go"]),
 ("A knockout", "Boxing", ["Wrestling", "Judo", "Sumo"]),
 ("Scoring a century", "Cricket", ["Rounders", "Bowls", "Croquet"]),
 ("A penalty corner", "Hockey", ["Lacrosse", "Handball", "Water polo"]),
 ("Touché!", "Fencing", ["Judo", "Karate", "Archery"]),
 ("A centre pass", "Netball", ["Handball", "Volleyball", "Lacrosse"]),
 ("A face-off", "Ice hockey", ["Curling", "Handball", "Water polo"]),
 ("A chukka", "Polo", ["Croquet", "Showjumping", "Lacrosse"]),
 ("Catching a crab", "Rowing", ["Sailing", "Canoeing", "Surfing"]),
 ("A furlong", "Horse racing", ["Greyhound racing", "Showjumping", "Athletics"]),
 ("A tumble turn", "Swimming", ["Gymnastics", "Diving", "Water polo"]),
 ("Love-fifteen", "Tennis", ["Badminton", "Squash", "Table tennis"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-113.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
