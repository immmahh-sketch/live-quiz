# Bank session 10 Oct 2026: 2 more general races -> bank/race-76.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Moon'?", "General knowledge", "medium", ["moons", "wordplay"], [
 ("Manchester City's anthem", "Blue", ["Silver", "Pale", "Bright"]), ("The full moon nearest the autumn equinox", "Harvest", ["Autumn", "Barley", "Frost"]),
 ("The full moon that follows the Harvest Moon", "Hunter's", ["Hawk", "Deer", "Archer"]), ("The 1973 film starring Ryan and Tatum O'Neal", "Paper", ["Cardboard", "Glass", "Silver"]),
 ("The Japanese anime heroine Usagi Tsukino", "Sailor", ["Captain", "Pirate", "Star"]), ("The Who's wild drummer", "Keith", ["Kenney", "John", "Roger"]),
 ("The second Twilight book and film", "New", ["Eclipse", "Midnight", "Dark"]), ("A moon that turns red during a total eclipse", "Blood", ["Red", "Fire", "Rust"]),
 ("A full moon at its closest to Earth, looking bigger than usual", "Super", ["Mega", "Giant", "Big"]), ("The thin curved moon on many Islamic flags", "Crescent", ["Sickle", "Horn", "Quarter"]),
 ("The moon's phase between half and full", "Gibbous", ["Convex", "Hump", "Bulging"]), ("June's full moon, named after a summer fruit", "Strawberry", ["Raspberry", "Cherry", "Apple"]),
 ("January's full moon, named after howling animals", "Wolf", ["Fox", "Bear", "Dog"]), ("The holiday after a wedding", "Honey", ["Sugar", "Sweet", "Love"]),
 ("The South Korean who led the United Nations from 2007 to 2016", "Ban Ki-moon", ["Kofi Annan", "Boutros Boutros-Ghali", "António Guterres"]), ("Nick Drake's last album, and April's full moon", "Pink", ["Purple", "Rose", "Peach"]),
 ("Werewolves change when the moon is like this", "Full", ["Whole", "Round", "Bright"]), ("A common pub name, and a Californian bay", "Half", ["Quarter", "Silver", "Rising"]),
 ("December's full moon, named for the season", "Cold", ["Ice", "Frost", "Winter"]), ("February's full moon, named after the weather", "Snow", ["Rain", "Storm", "Ice"])])

race("which famous 'Fire'?", "General knowledge", "medium", ["fire", "wordplay"], [
 ("London, 1666", "The Great Fire", ["The Great Plague", "The Great Storm", "The Great Frost"]), ("The Supermarine fighter of the Battle of Britain", "Spitfire", ["Hurricane", "Typhoon", "Mosquito"]),
 ("The second Hunger Games book", "Catching Fire", ["Mockingjay", "The Hunger Games", "The Ballad of Songbirds and Snakes"]), ("The 1985 Brat Pack film set in Washington DC", "St. Elmo's Fire", ["The Breakfast Club", "Pretty in Pink", "Sixteen Candles"]),
 ("The Canadian band behind The Suburbs", "Arcade Fire", ["Broken Social Scene", "Metric", "The Stills"]), ("Amazon's colour tablet", "Kindle Fire", ["Kindle Paperwhite", "Echo Show", "Nexus"]),
 ("Being shot at by your own side", "Friendly fire", ["Crossfire", "Backfire", "Covering fire"]), ("Jerry Lee Lewis's 1957 hit", "Great Balls of Fire", ["Whole Lotta Shakin' Goin' On", "Breathless", "Johnny B. Goode"]),
 ("Johnny Cash's 1963 hit", "Ring of Fire", ["Folsom Prison Blues", "I Walk the Line", "A Boy Named Sue"]), ("The Doors' 1967 hit", "Light My Fire", ["Break On Through", "Riders on the Storm", "People Are Strange"]),
 ("The Oscar-winning film about Eric Liddell and Harold Abrahams", "Chariots of Fire", ["Gandhi", "Ordinary People", "Out of Africa"]), ("The fourth Harry Potter book", "Goblet of Fire", ["Order of the Phoenix", "Prisoner of Azkaban", "Half-Blood Prince"]),
 ("The Prodigy's 1996 number one", "Firestarter", ["Breathe", "Out of Space", "Charly"]), ("Kings of Leon's 2008 hit", "Sex on Fire", ["Use Somebody", "Closer", "Molly's Chambers"]),
 ("Alicia Keys's 2012 hit", "Girl on Fire", ["Fallin'", "No One", "Empire State of Mind"]), ("Billy Joel's 1989 rattle through history", "We Didn't Start the Fire", ["Piano Man", "Uptown Girl", "My Life"]),
 ("Ed Sheeran's song for The Hobbit", "I See Fire", ["Photograph", "Perfect", "Lego House"]), ("James Taylor's 1970 song about loss", "Fire and Rain", ["Sweet Baby James", "You've Got a Friend", "Carolina in My Mind"]),
 ("The Crazy World of Arthur Brown's 1968 number one, one word", "Fire", ["Flames", "Burn", "Inferno"]), ("The 5th of November celebrations", "Bonfire Night", ["Halloween", "Mischief Night", "Hogmanay"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-76.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
