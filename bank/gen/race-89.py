# Bank session 10 Oct 2026: 2 more general races -> bank/race-89.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Dark'?", "General knowledge", "medium", ["dark", "wordplay"], [
 ("Christopher Nolan's 2008 Batman film", "The Dark Knight", ["Batman Begins", "The Dark Knight Rises", "Batman Returns"]), ("Pink Floyd's 1973 album with the prism cover", "The Dark Side of the Moon", ["Wish You Were Here", "Animals", "Meddle"]),
 ("The centuries after the fall of Rome", "The Dark Ages", ["The Iron Age", "The Renaissance", "The Bronze Age"]), ("Gary Oldman's Oscar-winning Churchill film", "Darkest Hour", ["Dunkirk", "The King's Speech", "Their Finest"]),
 ("Philip Pullman's trilogy about Lyra", "His Dark Materials", ["The Book of Dust", "A Series of Unfortunate Events", "The Chronicles of Narnia"]), ("The invisible stuff that makes up most of the universe's mass", "Dark matter", ["Antimatter", "Black hole", "Dark energy"]),
 ("The hidden corner of the internet where crooks trade", "Dark web", ["Intranet", "Cloud", "Mainframe"]), ("The Lowestoft band behind 'I Believe in a Thing Called Love'", "The Darkness", ["The Struts", "Muse", "Feeder"]),
 ("Ozzy Osbourne's nickname", "Prince of Darkness", ["The Boss", "The Thin White Duke", "The Lizard King"]), ("The gritstone moorland in the north of the Peak District", "Dark Peak", ["White Peak", "Kinder Scout", "Hope Valley"]),
 ("What the Death Eaters call Voldemort", "The Dark Lord", ["The Half-Blood Prince", "The Chosen One", "The Boy Who Lived"]), ("The Hogwarts job Snape always wanted", "Defence Against the Dark Arts", ["Potions", "Transfiguration", "Herbology"]),
 ("The 2019 X-Men film about Jean Grey", "Dark Phoenix", ["Days of Future Past", "Apocalypse", "Logan"]), ("Darth Vader's side of the Force", "The Dark Side", ["The Light Side", "The Rebellion", "The Jedi Order"]),
 ("Chocolate with lots of cocoa and little or no milk", "Dark chocolate", ["Milk chocolate", "White chocolate", "Couverture"]), ("Kielder's special status for stargazers", "Dark Sky Park", ["Starlight Reserve", "Observatory Park", "Night Park"]),
 ("Johnny Depp's 2012 Tim Burton vampire film", "Dark Shadows", ["Sleepy Hollow", "Sweeney Todd", "Corpse Bride"]), ("Bruce Springsteen's 1978 album", "Darkness on the Edge of Town", ["Born to Run", "The River", "Nebraska"]),
 ("Bruce Springsteen's 1984 hit with Courteney Cox in the video", "Dancing in the Dark", ["Born in the U.S.A.", "Glory Days", "I'm on Fire"]), ("Where photographs used to be developed", "Darkroom", ["Studio", "Lab", "Gallery"])])

race("which famous 'Light'?", "General knowledge", "medium", ["light", "wordplay"], [
 ("Sunderland's ground", "Stadium of Light", ["Roker Park", "St James' Park", "Riverside Stadium"]), ("Tennyson's doomed cavalry charge", "The Charge of the Light Brigade", ["The Charge of the Heavy Brigade", "Pickett's Charge", "The Thin Red Line"]),
 ("Toy Story's space ranger", "Buzz Lightyear", ["Emperor Zurg", "Jessie", "Rex"]), ("Ian Broudie's band, who co-wrote 'Three Lions'", "The Lightning Seeds", ["The Farm", "Space", "Shed Seven"]),
 ("Holman Hunt's painting of Jesus with a lantern", "The Light of the World", ["The Scapegoat", "The Awakening Conscience", "The Hireling Shepherd"]), ("The BBC radio station that became Radio 2 in 1967", "The Light Programme", ["The Home Service", "The Third Programme", "Radio Luxembourg"]),
 ("About 300,000 km per second", "The speed of light", ["The speed of sound", "Escape velocity", "Warp speed"]), ("The first book of Pullman's His Dark Materials", "Northern Lights", ["The Subtle Knife", "The Amber Spyglass", "La Belle Sauvage"]),
 ("Manfred Mann's Earth Band's Springsteen cover, and a 2019 film", "Blinded by the Light", ["Davy's on the Road Again", "Mighty Quinn", "Do Wah Diddy Diddy"]), ("The 2015 Best Picture about the Boston Globe", "Spotlight", ["The Post", "Birdman", "The Big Short"]),
 ("Chaplin's 1952 film about a fading music-hall clown", "Limelight", ["The Great Dictator", "Modern Times", "The Kid"]), ("The 2017 Best Picture, after the envelope mix-up", "Moonlight", ["La La Land", "Hidden Figures", "Manchester by the Sea"]),
 ("Andrew Lloyd Webber's musical on roller skates", "Starlight Express", ["Cats", "Evita", "Aspects of Love"]), ("Stephenie Meyer's vampire saga", "Twilight", ["True Blood", "The Vampire Diaries", "Interview with the Vampire"]),
 ("A Jedi's weapon", "Lightsaber", ["Blaster", "Bowcaster", "Electrostaff"]), ("Amsterdam's famous after-dark quarter", "Red Light District", ["Jordaan", "De Pijp", "Dam Square"]),
 ("What stops you at a junction", "Traffic light", ["Give way sign", "Lollipop lady", "Zebra crossing"]), ("The 1980s TV detective show with Bruce Willis and Cybill Shepherd", "Moonlighting", ["Remington Steele", "Hart to Hart", "Magnum, P.I."]),
 ("The Newcastle duo behind 'Lifted' and 'High'", "Lighthouse Family", ["Prefab Sprout", "The Beautiful South", "Del Amitri"]), ("The boxing weight just below welterweight", "Lightweight", ["Featherweight", "Bantamweight", "Middleweight"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-89.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
