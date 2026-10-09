# Bank session 9 Oct 2026 (fourth pass): new Wipeout boards -> bank/wipeout-6.json. 15 right and 5 wrong each. Decoys
# need knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Things you'd see in a traditional nativity scene", "Christmas", "easy", ["Christmas", "nativity"],
 ["Mary", "Joseph", "Baby Jesus", "Manger", "Shepherds", "Sheep", "Wise men", "Angel", "Star", "Donkey", "Ox", "Gold", "Frankincense", "Myrrh", "Stable"],
 ["Robin", "Holly", "Reindeer", "Christmas tree", "Snowman"])
board("Words that make a new word when you put 'snow' in front", "Words and language", "medium", ["wordplay", "winter"],
 ["Ball", "Man", "Flake", "Drop", "Board", "Storm", "Fall", "Plough", "Shoe", "Drift", "Mobile", "Line", "Bound", "Cap", "Bird"],
 ["Sock", "Hat", "Coat", "Tree", "Cake"])
board("Men who have captained the England football team", "Football", "medium", ["England", "football"],
 ["Billy Wright", "Bobby Moore", "Emlyn Hughes", "Kevin Keegan", "Bryan Robson", "Terry Butcher", "Gary Lineker", "Tony Adams", "Alan Shearer", "David Beckham", "John Terry", "Rio Ferdinand", "Steven Gerrard", "Wayne Rooney", "Harry Kane"],
 ["Paul Gascoigne", "Paul Scholes", "Ian Wright", "Peter Crouch", "Jamie Carragher"])
board("Clubs that have won the FA Cup", "Football", "medium", ["FA Cup", "football"],
 ["Arsenal", "Manchester United", "Chelsea", "Tottenham Hotspur", "Liverpool", "Aston Villa", "Newcastle United", "Blackburn Rovers", "Everton", "Manchester City", "West Bromwich Albion", "Bolton Wanderers", "Wolverhampton Wanderers", "Sheffield United", "Sunderland"],
 ["Middlesbrough", "Fulham", "Norwich City", "Stoke City", "Watford"])
board("Famous people from the North East of England", "The North East of England", "medium", ["North East", "people"],
 ["Sting", "Cheryl", "Ant McPartlin", "Declan Donnelly", "Alan Shearer", "Jimmy Nail", "Rowan Atkinson", "Bryan Ferry", "Paul Gascoigne", "Jordan Henderson", "Sarah Millican", "Ross Noble", "Robson Green", "Steve Cram", "Brendan Foster"],
 ["Peter Kay", "Wayne Rooney", "Vernon Kay", "Sean Bean", "Jodie Comer"])
board("Chemical elements named after a place", "Science", "hard", ["chemistry", "elements"],
 ["Americium", "Berkelium", "Californium", "Europium", "Francium", "Germanium", "Polonium", "Scandium", "Strontium", "Ytterbium", "Hafnium", "Ruthenium", "Darmstadtium", "Nihonium", "Tennessine"],
 ["Einsteinium", "Curium", "Nobelium", "Mendelevium", "Fermium"])
board("Countries whose flag is red, white and blue", "Geography", "medium", ["flags"],
 ["United Kingdom", "USA", "France", "Netherlands", "Russia", "Norway", "Iceland", "Australia", "New Zealand", "Czech Republic", "Slovakia", "Luxembourg", "Thailand", "Chile", "Cuba"],
 ["Italy", "Ireland", "Germany", "Belgium", "Sweden"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
