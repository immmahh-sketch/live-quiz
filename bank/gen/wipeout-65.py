# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-65.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("Played for Newcastle under Kevin Keegan, 1992 to 1997", "Football", "hard", ["Newcastle United", "Kevin Keegan", "The Entertainers"],
 ["Andy Cole", "Peter Beardsley", "Les Ferdinand", "David Ginola", "Faustino Asprilla", "Rob Lee", "Philippe Albert", "Steve Watson", "Warren Barton", "John Beresford", "Darren Peacock", "Steve Howey", "Pavel Srníček", "Keith Gillespie", "Alan Shearer"],
 ["Gary Speed", "Nolberto Solano", "Kieron Dyer", "Shay Given", "Duncan Ferguson"])
board("Played for Sunderland under Peter Reid, 1995 to 2002", "Football", "hard", ["Sunderland", "Peter Reid"],
 ["Niall Quinn", "Kevin Phillips", "Thomas Sørensen", "Michael Gray", "Kevin Ball", "Gavin McCann", "Allan Johnston", "Nicky Summerbee", "Stefan Schwarz", "Julio Arca", "Don Hutchison", "Chris Makin", "Jody Craddock", "Lee Clark", "Alex Rae"],
 ["Jermain Defoe", "Jordan Henderson", "Darren Bent", "Kenwyne Jones", "Gary Rowell"])
board("In England's squad at the 1990 World Cup", "Football", "medium", ["England", "Italia 90", "World Cup"],
 ["Gary Lineker", "Paul Gascoigne", "David Platt", "Stuart Pearce", "Chris Waddle", "Peter Shilton", "Bryan Robson", "Terry Butcher", "Des Walker", "Mark Wright", "John Barnes", "Peter Beardsley", "Paul Parker", "Trevor Steven", "Steve Bull"],
 ["Tony Adams", "Alan Shearer", "Ian Wright", "Paul Merson", "Teddy Sheringham"])
board("In England's Euro 2022-winning Lionesses squad", "Football", "medium", ["Lionesses", "England", "Euro 2022"],
 ["Mary Earps", "Lucy Bronze", "Rachel Daly", "Keira Walsh", "Leah Williamson", "Millie Bright", "Georgia Stanway", "Fran Kirby", "Beth Mead", "Ellen White", "Lauren Hemp", "Chloe Kelly", "Alessia Russo", "Ella Toone", "Jill Scott"],
 ["Steph Houghton", "Lauren James", "Karen Carney", "Toni Duggan", "Jordan Nobbs"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-65.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
