# Bank session 10 Oct 2026: 2 more general races -> bank/race-87.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Sun'?", "General knowledge", "medium", ["sun", "wordplay"], [
 ("Louis XIV's nickname", "The Sun King", ["The Lion King", "The Merry Monarch", "The Iron King"]), ("The Memphis label that launched Elvis", "Sun Records", ["Stax", "Motown", "Chess"]),
 ("South Africa's casino resort, boycotted by musicians in the 1980s", "Sun City", ["Durban", "Port Elizabeth", "Bloemfontein"]), ("The Animals' 1964 number one about New Orleans", "The House of the Rising Sun", ["Don't Let Me Be Misunderstood", "We Gotta Get Out of This Place", "It's My Life"]),
 ("George Harrison's song that opens side two of Abbey Road", "Here Comes the Sun", ["Something", "Octopus's Garden", "Come Together"]), ("Billy Wilder's 1950 film about Norma Desmond", "Sunset Boulevard", ["All About Eve", "Double Indemnity", "Some Like It Hot"]),
 ("The Proclaimers' song, and the 2013 film of their music", "Sunshine on Leith", ["I'm Gonna Be (500 Miles)", "Letter from America", "King of the Road"]), ("Katrina and the Waves' 1985 hit", "Walking on Sunshine", ["Love Shine a Light", "Going Down to Liverpool", "Que Te Quiero"]),
 ("Robert Redford's film festival in Utah", "Sundance", ["Telluride", "Tribeca", "Slamdance"]), ("The ancient Chinese author of The Art of War", "Sun Tzu", ["Confucius", "Lao Tzu", "Mencius"]),
 ("J. G. Ballard's novel of a boy in a Shanghai camp, filmed by Spielberg", "Empire of the Sun", ["Crash", "High-Rise", "The Drowned World"]), ("Hemingway's 1926 novel set around the Pamplona bull run", "The Sun Also Rises", ["A Farewell to Arms", "For Whom the Bell Tolls", "The Old Man and the Sea"]),
 ("The police station in The Bill", "Sun Hill", ["Holby", "Sandford", "Denton"]), ("Lorraine Hansberry's 1959 play about a Chicago family", "A Raisin in the Sun", ["Death of a Salesman", "A Streetcar Named Desire", "Fences"]),
 ("The Arctic summer when it never gets dark", "Midnight sun", ["Northern lights", "Polar night", "Solstice"]), ("Britain's best-selling daily tabloid", "The Sun", ["The Mirror", "Daily Star", "Daily Mail"]),
 ("The baby's face in the Teletubbies' sky", "Sun Baby", ["Moon Baby", "Sky Baby", "Noo-Noo"]), ("What you slap on to avoid burning", "Sun cream", ["Aftersun", "Moisturiser", "Calamine"]),
 ("The song Morecambe and Wise skipped off to", "Bring Me Sunshine", ["Side by Side", "Sing a Rainbow", "Walking on Air"]), ("The Wearside city of the Stadium of Light", "Sunderland", ["Gateshead", "Middlesbrough", "Hartlepool"])])

race("which famous 'Rain'?", "General knowledge", "medium", ["rain", "wordplay"], [
 ("Gene Kelly's 1952 musical", "Singin' in the Rain", ["An American in Paris", "On the Town", "Anchors Aweigh"]), ("Dustin Hoffman's 1988 film as an autistic savant", "Rain Man", ["Tootsie", "Kramer vs. Kramer", "Awakenings"]),
 ("Guns N' Roses' epic 1991 ballad", "November Rain", ["Sweet Child o' Mine", "Paradise City", "Don't Cry"]), ("Prince's 1984 film and album", "Purple Rain", ["Under the Cherry Moon", "Sign o' the Times", "1999"]),
 ("The Weather Girls' 1982 hit", "It's Raining Men", ["I Will Survive", "Don't Leave Me This Way", "Hot Stuff"]), ("Eurythmics' 1984 hit", "Here Comes the Rain Again", ["Sweet Dreams", "Love Is a Stranger", "There Must Be an Angel"]),
 ("Creedence Clearwater Revival's 1970 song", "Who'll Stop the Rain", ["Proud Mary", "Bad Moon Rising", "Fortunate Son"]), ("Lady Gaga and Ariana Grande's 2020 duet", "Rain on Me", ["Shallow", "Stupid Love", "7 Rings"]),
 ("The Greenpeace ship sunk by French agents in 1985", "Rainbow Warrior", ["Arctic Sunrise", "Sea Shepherd", "Esperanza"]), ("The 1829 contest won by Stephenson's Rocket", "Rainhill Trials", ["Stockton Trials", "Locomotion Cup", "Stephenson Prize"]),
 ("A tropical forest with heavy rainfall all year", "Rainforest", ["Cloud forest", "Mangrove", "Savanna"]), ("Turning down an offer for now, but maybe later", "Rain check", ["IOU", "Wait list", "Back burner"]),
 ("Feeling perfectly fine again", "Right as rain", ["Fair to middling", "Under the weather", "Off colour"]), ("Pollution that falls from the clouds", "Acid rain", ["Smog", "Fallout", "Ozone"]),
 ("Mario Kart's colourful final track", "Rainbow Road", ["Bowser's Castle", "Moo Moo Meadows", "Koopa Beach"]), ("The ITV children's show with Zippy, George and Bungle", "Rainbow", ["Play School", "Button Moon", "Pipkins"]),
 ("Judy Garland's song in The Wizard of Oz", "Over the Rainbow", ["Follow the Yellow Brick Road", "If I Only Had a Brain", "Ding-Dong! The Witch Is Dead"]), ("Burt Bacharach's song from Butch Cassidy and the Sundance Kid", "Raindrops Keep Fallin' on My Head", ["Do You Know the Way to San Jose", "Close to You", "Walk On By"]),
 ("A lawyer or salesperson who brings in the big money", "Rainmaker", ["Breadwinner", "Cash cow", "Big hitter"]), ("Bob Dylan's 'everybody must get stoned' song", "Rainy Day Women #12 & 35", ["Like a Rolling Stone", "Just Like a Woman", "Positively 4th Street"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-87.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
