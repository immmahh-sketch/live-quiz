# Bank session 10 Oct 2026: 2 more general races -> bank/race-85.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Summer'?", "General knowledge", "medium", ["summer", "wordplay"], [
 ("San Francisco's hippie season of 1967", "Summer of Love", ["Woodstock", "Hippie Trail", "Swinging Sixties"]), ("Cliff Richard's 1963 film with a London bus", "Summer Holiday", ["The Young Ones", "Expresso Bongo", "Wonderful Life"]),
 ("The Grease duet: 'Tell me more, tell me more'", "Summer Nights", ["You're the One That I Want", "Grease Lightnin'", "Hopelessly Devoted to You"]), ("Bryan Adams: 'I got my first real six-string'", "Summer of '69", ["Run to You", "Heaven", "(Everything I Do) I Do It for You"]),
 ("A spell of warm weather in autumn", "Indian summer", ["Heatwave", "Dog days", "Cold snap"]), ("A. S. Neill's famously free school in Suffolk", "Summerhill", ["Gordonstoun", "Bedales", "Dartington"]),
 ("The BBC's long-running Yorkshire sitcom, 'Last of the ...'", "Summer Wine", ["Summer Ale", "Red Wine", "Mild Ale"]), ("What the clocks go forward to in March", "British Summer Time", ["Greenwich Mean Time", "Central European Time", "Universal Time"]),
 ("Around 21 June, the longest day", "Summer solstice", ["Spring equinox", "Winter solstice", "Autumn equinox"]), ("A bread-lined bowl of red berries", "Summer pudding", ["Eton mess", "Bread and butter pudding", "Charlotte russe"]),
 ("The seaside town in Home and Away", "Summer Bay", ["Erinsborough", "Ramsay Street", "Wentworth"]), ("The disco queen behind 'I Feel Love'", "Donna Summer", ["Gloria Gaynor", "Diana Ross", "Chaka Khan"]),
 ("Bananarama's 1983 hit, later a Taylor Swift song too", "Cruel Summer", ["Venus", "Robert De Niro's Waiting", "Love in the First Degree"]), ("Don Henley's 1984 hit", "The Boys of Summer", ["Dirty Laundry", "All She Wants to Do Is Dance", "The End of the Innocence"]),
 ("Mungo Jerry's 1970 number one", "In the Summertime", ["Lady Rose", "Baby Jump", "Alright Alright Alright"]), ("The Lovin' Spoonful's 1966 hit", "Summer in the City", ["Daydream", "Do You Believe in Magic", "Nashville Cats"]),
 ("The Style Council's 1983 hit", "Long Hot Summer", ["Walls Come Tumbling Down", "My Ever Changing Moods", "Shout to the Top"]), ("The 1997 slasher film with Jennifer Love Hewitt", "I Know What You Did Last Summer", ["Scream", "Urban Legend", "Final Destination"]),
 ("The 2009 film with Joseph Gordon-Levitt and Zooey Deschanel", "(500) Days of Summer", ["Yes Man", "Garden State", "Elf"]), ("DJ Jazzy Jeff & the Fresh Prince's 1991 hit", "Summertime", ["Boom! Shake the Room", "Parents Just Don't Understand", "Gettin' Jiggy wit It"])])

race("which famous 'Winter'?", "General knowledge", "medium", ["winter", "wordplay"], [
 ("The strikes of 1978–79 under James Callaghan", "Winter of Discontent", ["Three-Day Week", "Miners' Strike", "Black Wednesday"]), ("The Shakespeare play with 'Exit, pursued by a bear'", "The Winter's Tale", ["The Tempest", "Cymbeline", "Pericles"]),
 ("The seat of House Stark", "Winterfell", ["Castle Black", "King's Landing", "Riverrun"]), ("The Stark family words", "Winter Is Coming", ["Fire and Blood", "Hear Me Roar", "Ours Is the Fury"]),
 ("Captain America's 2014 sequel", "The Winter Soldier", ["Civil War", "The First Avenger", "Brave New World"]), ("The 2010 film that made Jennifer Lawrence's name", "Winter's Bone", ["The Burning Plain", "Like Crazy", "Joy"]),
 ("The freezing gloom that a big atomic war could bring", "Nuclear winter", ["Ice age", "Fallout", "Dark ages"]), ("Birmingham's much-mocked 1997 name for the festive season", "Winterval", ["Winterfest", "Festivus", "Yuletide"]),
 ("The Lancashire moor with a giant TV mast, scene of a 2018 wildfire", "Winter Hill", ["Pendle Hill", "Rivington Pike", "Darwen Moor"]), ("England's first full-time football manager, from 1946 to 1962", "Walter Winterbottom", ["Alf Ramsey", "Joe Mercer", "Don Revie"]),
 ("Hyde Park's Christmas funfair, and a festive song", "Winter Wonderland", ["Christmas Fayre", "Santa's Grotto", "Frost Fair"]), ("The actress in The Poseidon Adventure, twice an Oscar winner", "Shelley Winters", ["Shirley MacLaine", "Ruth Gordon", "Jessica Tandy"]),
 ("The 1968 film with Katharine Hepburn as Eleanor of Aquitaine", "The Lion in Winter", ["Becket", "A Man for All Seasons", "Anne of the Thousand Days"]), ("The Games held every four years with skiing and skating", "Winter Olympics", ["Commonwealth Games", "Nordic Games", "Snow Games"]),
 ("Around 21 December, the shortest day", "Winter solstice", ["Summer solstice", "Autumn equinox", "Spring equinox"]), ("Feeling low in the dark months", "Winter blues", ["Cabin fever", "Brain fog", "Hangover"]),
 ("The minty plant oil used in muscle rubs", "Wintergreen", ["Peppermint", "Eucalyptus", "Camphor"]), ("The BBC's live wildlife show in the cold months", "Winterwatch", ["Springwatch", "Countryfile", "Seasonwatch"]),
 ("The author of Oranges Are Not the Only Fruit", "Jeanette Winterson", ["Hilary Mantel", "Margaret Drabble", "Fay Weldon"]), ("Vogue's long-time editor", "Anna Wintour", ["Grace Coddington", "Miranda Priestly", "Diana Vreeland"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-85.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
