# Bank session 10 Oct 2026: 19 more Put in order questions -> bank/order-4.json. Checked against every order question in
# the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Science", ["space", "rockets"], "easy", "Put these stages of a rocket launch in order", ["Countdown", "Ignition", "Lift-off", "Stage separation", "Reaching orbit"], "first to last")
o("Politics", ["Parliament", "laws"], "hard", "Put these stages of a bill becoming law in order", ["First reading", "Second reading", "Committee stage", "Report stage", "Third reading", "Passed by the Lords", "Royal Assent"], "first to last")
o("Science", ["minerals", "hardness"], "hard", "Put these minerals in order of hardness, softest first", ["Talc", "Gypsum", "Fluorite", "Quartz", "Topaz", "Corundum", "Diamond"], "softest first")
o("Everyday life", ["generations"], "easy", "Put these generations in order, oldest first", ["Silent Generation", "Baby Boomers", "Generation X", "Millennials", "Generation Z", "Generation Alpha"], "oldest first")
o("Sport", ["darts"], "hard", "Put these dartboard numbers in order, going clockwise from 20 at the top", ["20", "1", "18", "4", "13", "6", "10"], "clockwise from 20")
o("Words and language", ["keyboards", "letters"], "medium", "Put these letters in the order they sit on a keyboard's top row, left to right", ["Q", "W", "E", "T", "Y", "P"], "left to right")
o("North East England", ["football", "clubs"], "hard", "Put these North East football clubs in order of founding, earliest first", ["Middlesbrough", "Sunderland", "Darlington", "Newcastle United", "Hartlepool United", "Gateshead FC (today's club)"], "earliest first")
o("North East England", ["Tyne bridges", "Newcastle"], "hard", "Put these Tyne bridges in order, going upriver from the sea", ["Gateshead Millennium Bridge", "Tyne Bridge", "Swing Bridge", "High Level Bridge", "Queen Elizabeth II Metro Bridge", "King Edward VII Bridge", "Redheugh Bridge"], "upriver from the sea")
o("Sport", ["sporting calendar"], "medium", "Put these British sporting events in the order they usually happen in the year", ["Six Nations", "Grand National", "London Marathon", "FA Cup final", "Wimbledon", "The Open"], "earliest in the year first")
o("Everyday life", ["days", "festivals"], "easy", "Put these special days in the order they fall in the year", ["Burns Night", "Valentine's Day", "St Patrick's Day", "St George's Day", "Halloween", "Bonfire Night", "St Andrew's Day"], "January to December")
o("Science", ["weights", "units"], "medium", "Put these units of weight in order, lightest first", ["Gram", "Ounce", "Pound", "Kilogram", "Stone", "Hundredweight", "Tonne"], "lightest first")
o("Food and drink", ["kitchen", "measures"], "easy", "Put these amounts in order, smallest first", ["A teaspoon", "A tablespoon", "A can of pop", "A pint", "A litre", "A gallon"], "smallest first")
o("Music", ["dynamics", "music theory"], "medium", "Put these musical dynamics in order, quietest first", ["Pianissimo", "Piano", "Mezzo-piano", "Mezzo-forte", "Forte", "Fortissimo"], "quietest first")
o("World geography", ["compass"], "easy", "Put these compass points in order, going clockwise from north", ["North", "North-east", "East", "South-east", "South", "South-west", "West"], "clockwise from north")
o("Music", ["Oasis", "number ones"], "hard", "Put these Oasis number ones in release order, earliest first", ["Some Might Say", "Don't Look Back in Anger", "D'You Know What I Mean?", "All Around the World", "Go Let It Out", "The Hindu Times", "Lyla"], "earliest first")
o("Landmarks", ["heights"], "easy", "Put these in order of height, shortest first", ["An adult man", "A double-decker bus", "A giraffe", "The Angel of the North", "The Statue of Liberty, with its base", "The Eiffel Tower"], "shortest first")
o("Science", ["science"], "easy", "Put these steps of a science experiment in order", ["Ask a question", "Make a prediction", "Do the experiment", "Record the results", "Draw a conclusion"], "first to last")
o("Games and toys", ["chess"], "easy", "Put these stages of a chess game in order", ["Opening", "Middlegame", "Endgame", "Checkmate"], "first to last")
o("Music", ["Sound of Music", "scales"], "easy", "Put these notes of the scale in order, as in 'Do-Re-Mi'", ["Do", "Re", "Mi", "Fa", "So", "La", "Ti"], "going up the scale")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
