# Bank session 10 Oct 2026: 2 more general races -> bank/race-68.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Cross'?", "General knowledge", "medium", ["crosses", "wordplay"], [
 ("The London station with Platform 9¾", "King's", ["Queen's", "Prince's", "Golden"]), ("The station at the end of the Strand, from where distances to London are measured", "Charing", ["Holborn", "Temple", "Ludgate"]),
 ("The humanitarian movement founded by Henri Dunant", "Red", ["White", "Green", "Golden"]), ("Britain's highest award for gallantry in the face of the enemy", "Victoria", ["Albert", "Elizabeth", "Edward"]),
 ("Awarded to the whole island of Malta in 1942", "George", ["Albert", "Elizabeth", "Edward"]), ("The constellation on the Australian and New Zealand flags", "Southern", ["Northern", "Eastern", "Pacific"]),
 ("The German military medal of both World Wars", "Iron", ["Steel", "Black", "Bronze"]), ("A stone cross with a ring around its centre", "Celtic", ["Saxon", "Gaelic", "Norse"]),
 ("The eight-pointed badge of St John Ambulance", "Maltese", ["Templar", "Jerusalem", "Teutonic"]), ("'Ride a cock-horse to ...'", "Banbury", ["Coventry", "Bampton", "Burford"]),
 ("To betray someone", "Double", ["Triple", "Twice", "Back"]), ("The buns eaten on Good Friday", "Hot", ["Bath", "Chelsea", "Iced"]),
 ("The Buckinghamshire commuter town on the Chiltern line", "Gerrards", ["Chalfont", "Denham", "Amersham"]), ("The Essex town named after one of Edward I's memorials", "Waltham", ["Epping", "Romford", "Loughton"]),
 ("Scotland's white saltire on blue", "St Andrew's", ["St David's", "St Patrick's", "St George's"]), ("The RAF's gallantry award for officers flying against the enemy", "Distinguished Flying", ["Distinguished Service", "Conspicuous Gallantry", "Royal Victorian"]),
 ("The Army's gallantry award, one step below the Victoria Cross's level", "Military", ["Army", "Soldier's", "Infantry"]), ("The 1346 battle outside Durham where the Scottish king was captured", "Neville's", ["Percy's", "Bishop's", "Durham"]),
 ("Edward I's memorials marking where his queen's coffin rested", "Eleanor", ["Isabella", "Matilda", "Margaret"]), ("The animal charity founded in 1897", "Blue", ["Green", "Purple", "White"])])

race("which famous 'House'?", "General knowledge", "medium", ["houses", "wordplay"], [
 ("The US President's home", "White", ["Blair", "Grey", "Federal"]), ("Dickens's novel about the case of Jarndyce and Jarndyce", "Bleak", ["Cold", "Dark", "Hard"]),
 ("The 1978 John Belushi college comedy", "Animal", ["Party", "Frat", "Beast"]), ("A child's playhouse, named after Peter Pan's friend", "Wendy", ["Tinker", "Darling", "Pixie"]),
 ("The Lord Mayor of London's official home", "Mansion", ["Guild", "Mayor's", "Manor"]), ("The Strand palace with a winter ice rink in its courtyard", "Somerset", ["Dorset", "Devonshire", "Arundel"]),
 ("'Number One, London', the Duke of Wellington's home", "Apsley", ["Spencer", "Lancaster", "Burlington"]), ("The King's London home, next to St James's Palace", "Clarence", ["Lancaster", "Spencer", "York"]),
 ("The Strand building that housed the BBC World Service until 2012", "Bush", ["Television", "Ariel", "Media"]), ("The BBC's headquarters in Portland Place", "Broadcasting", ["Television", "Ariel", "Media"]),
 ("Home of the Commonwealth Secretariat on Pall Mall", "Marlborough", ["Lancaster", "Spencer", "York"]), ("Three of a kind and a pair in poker", "Full", ["Straight", "Flush", "Royal"]),
 ("Ibsen's play about Nora, 'A ... House'", "Doll's", ["Glass", "Wild", "Paper"]), ("South Korea's old presidential palace, named after its roof tiles", "Blue", ["Red", "Jade", "Golden"]),
 ("The Hertfordshire house where Elizabeth I heard she was queen", "Hatfield", ["Hever", "Knole", "Audley"]), ("The Wiltshire stately home with Britain's first safari park", "Longleat", ["Woburn", "Wilton", "Stourhead"]),
 ("Northumberland's home that was the first lit by hydroelectricity", "Cragside", ["Wallington", "Belsay", "Seaton"]), ("Derbyshire's 'Palace of the Peak'", "Chatsworth", ["Haddon", "Hardwick", "Kedleston"]),
 ("The reality show where housemates are filmed day and night", "Big Brother", ["Paradise", "Survivor", "Shipwrecked"]), ("Sydney's sail-roofed landmark", "Opera", ["Concert", "Music", "Harbour"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-68.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
