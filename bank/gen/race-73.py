# Bank session 10 Oct 2026: 2 more general races -> bank/race-73.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Star'?", "General knowledge", "medium", ["stars", "wordplay"], [
 ("The Empire's planet-destroying space station", "Death", ["Doom", "Dark", "Battle"]), ("Polaris, the sailor's guide", "North", ["South", "Guide", "Compass"]),
 ("Texas's nickname: the ... Star State", "Lone", ["Big", "Golden", "Single"]), ("Venus, shining in the east before sunrise", "Morning", ["Evening", "Dawn", "Day"]),
 ("The tyre firm whose guide hands out stars to restaurants", "Michelin", ["Pirelli", "Dunlop", "Goodyear"]), ("The tabloid sister paper of the Daily Express", "Daily", ["Sunday", "Evening", "Weekly"]),
 ("The Soviet emblem on top of the Kremlin towers", "Red", ["Yellow", "Communist", "Soviet"]), ("The Japanese throwing weapon, or shuriken", "Ninja", ["Samurai", "Shogun", "Karate"]),
 ("Smash Mouth's 1999 hit from Shrek", "All", ["Rock", "Pop", "Mega"]), ("A luxury hotel's top rating", "Five", ["Four", "Six", "Seven"]),
 ("The ultra-dense remains of a collapsed giant star", "Neutron", ["Proton", "Electron", "Quark"]), ("'..., twinkle, little star'", "Twinkle", ["Sparkle", "Glitter", "Shimmer"]),
 ("Madonna's 1984 hit, '... Star'", "Lucky", ["Rising", "Shining", "Falling"]), ("David Bowie's final album, released two days before he died", "Blackstar", ["Darkstar", "Lazarus", "Heroes"]),
 ("Sirius, the brightest star in the night sky", "Dog", ["Wolf", "Hound", "Bear"]), ("The sticker a teacher gives for good work", "Gold", ["Silver", "Bronze", "Green"]),
 ("Andrew Lloyd Webber's 'Jesus Christ ...'", "Superstar", ["Megastar", "Rockstar", "Starlight"]), ("The everyday name for a meteor", "Shooting", ["Flying", "Racing", "Burning"]),
 ("Keats's sonnet: '... star, would I were steadfast as thou art'", "Bright", ["Brave", "Lonely", "Silent"]), ("The 'Galactica' warship in the sci-fi series", "Battlestar", ["Starship", "Warstar", "Starbase"])])

race("which famous 'Bell'?", "General knowledge", "medium", ["bells", "wordplay"], [
 ("Philadelphia's cracked symbol of independence", "Liberty", ["Freedom", "Independence", "Union"]), ("Peter Pan's fairy", "Tinker", ["Silver", "Fairy", "Tingle"]),
 ("The Mexican-style fast-food chain", "Taco", ["Burrito", "Nacho", "Pepper"]), ("The Christmas song '... Bell Rock'", "Jingle", ["Ring", "Ding", "Silver"]),
 ("The long weight lifted in Olympic weightlifting", "Bar", ["Kettle", "Hand", "Iron"]), ("A short bar with a weight at each end, held in one hand", "Dumb", ["Kettle", "Wrist", "Ankle"]),
 ("Mike Oldfield's 1973 album, used in The Exorcist", "Tubular", ["Crystal", "Hollow", "Silver"]), ("True Cockneys are born within the sound of these", "Bow", ["St Clement's", "St Paul's", "Shoreditch"]),
 ("The AC/DC song that opens Back in Black", "Hell's", ["Heaven's", "Devil's", "Thunder"]), ("The wild flower that carpets English woods in spring", "Blue", ["Hare", "Snow", "Fox"]),
 ("The instrument in the 'More cowbell!' sketch", "Cow", ["Sheep", "Goat", "Hand"]), ("What a visitor rings at your front door", "Door", ["Gate", "Hand", "Front"]),
 ("The underwater chamber used by early divers", "Diving", ["Deep", "Sea", "Water"]), ("'... bells are ringing' for the bride and groom", "Wedding", ["Church", "Christmas", "Silver"]),
 ("Big Ben's official name: the ... Bell", "Great", ["Big", "Grand", "Royal"]), ("The bells on Santa's reindeer harness", "Sleigh", ["Reindeer", "Santa", "Snow"]),
 ("Rung to call everyone to eat, famously on a western ranch", "Dinner", ["Supper", "Lunch", "Tea"]), ("The actress who voices Anna in Frozen", "Kristen", ["Idina", "Mandy", "Kirsten"]),
 ("The singer of Erasure", "Andy", ["Vince", "Marc", "Jimmy"]), ("The actor who played Billy Elliot", "Jamie", ["Gary", "Tom", "Daniel"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-73.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
