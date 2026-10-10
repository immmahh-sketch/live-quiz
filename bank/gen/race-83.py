# Bank session 10 Oct 2026: 2 more general races -> bank/race-83.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Silver'?", "General knowledge", "medium", ["silver", "wordplay"], [
 ("Treasure Island's one-legged ship's cook", "Long John Silver", ["Billy Bones", "Blind Pew", "Ben Gunn"]), ("Marvel's cosmic herald of Galactus, riding a board", "Silver Surfer", ["Nova", "Captain Marvel", "Adam Warlock"]),
 ("Marvel's super-fast son of Magneto, and an old name for mercury", "Quicksilver", ["The Flash", "Northstar", "Hermes"]), ("The Queen's 1977 celebrations", "Silver Jubilee", ["Golden Jubilee", "Diamond Jubilee", "Platinum Jubilee"]),
 ("Bradley Cooper and Jennifer Lawrence's 2012 film", "Silver Linings Playbook", ["American Hustle", "Joy", "Passengers"]), ("New Zealand's national netball team", "Silver Ferns", ["All Blacks", "Black Ferns", "Black Caps"]),
 ("The nickname of Mercedes's Formula One cars", "Silver Arrows", ["Prancing Horse", "Red Bulls", "Papaya"]), ("Hawkwind's 1972 hit, sung by Lemmy", "Silver Machine", ["Motorhead", "Hurry on Sundown", "Urban Guerrilla"]),
 ("David Essex's 1980 motorbike hit", "Silver Dream Machine", ["Hold Me Close", "Gonna Make You a Star", "Rock On"]), ("The Christmas song about 'city sidewalks, busy sidewalks'", "Silver Bells", ["Jingle Bells", "Sleigh Ride", "White Christmas"]),
 ("The prize for coming second at the Olympics", "Silver medal", ["Bronze medal", "Runner-up", "Gold medal"]), ("An adult male gorilla", "Silverback", ["Greyback", "Blackback", "Kingback"]),
 ("The British tree with white papery bark", "Silver birch", ["Aspen", "Rowan", "White willow"]), ("Rolls-Royce's legendary car of 1907", "Silver Ghost", ["Phantom", "Silver Shadow", "Spirit of Ecstasy"]),
 ("The posh British pram maker founded in 1877", "Silver Cross", ["Maclaren", "Mamas & Papas", "Bugaboo"]), ("The US medal for gallantry in combat, below the Distinguished Service Cross", "Silver Star", ["Bronze Star", "Purple Heart", "Navy Cross"]),
 ("Formal waiting where food is served at the table from platters", "Silver service", ["Butler service", "Table d'hôte", "À la carte"]), ("An attractive older man with grey hair", "Silver fox", ["Grey wolf", "Old dog", "Dark horse"]),
 ("The East London district of the great 1917 munitions explosion", "Silvertown", ["Woolwich", "Canning Town", "Beckton"]), ("The Lone Ranger's horse", "Silver", ["Scout", "Trigger", "Champion"])])

race("which famous 'Night'?", "General knowledge", "medium", ["night", "wordplay"], [
 ("Shakespeare's comedy with Viola and Malvolio", "Twelfth Night", ["As You Like It", "Much Ado About Nothing", "The Tempest"]), ("The Beatles' first film, from 1964", "A Hard Day's Night", ["Help!", "Yellow Submarine", "Magical Mystery Tour"]),
 ("Hitler's 1934 purge of his own stormtroopers", "Night of the Long Knives", ["Kristallnacht", "Beer Hall Putsch", "Reichstag fire"]), ("John Travolta's 1977 disco film", "Saturday Night Fever", ["Grease", "Staying Alive", "Urban Cowboy"]),
 ("Van Gogh's painting of a swirling sky over a village", "The Starry Night", ["Sunflowers", "The Potato Eaters", "Irises"]), ("Rembrandt's 1642 painting of a militia company", "The Night Watch", ["The Anatomy Lesson", "The Jewish Bride", "Self-Portrait with Two Circles"]),
 ("Scotland's celebration on 25 January", "Burns Night", ["Hogmanay", "St Andrew's Day", "Up Helly Aa"]), ("F. Scott Fitzgerald's 1934 novel about Dick and Nicole Diver", "Tender Is the Night", ["The Great Gatsby", "This Side of Paradise", "The Beautiful and Damned"]),
 ("The John le Carré thriller that became a 2016 BBC series with Tom Hiddleston", "The Night Manager", ["The Little Drummer Girl", "The Tailor of Panama", "The Constant Gardener"]), ("W. H. Auden's 1936 poem about the postal train", "Night Mail", ["Funeral Blues", "September 1, 1939", "Musée des Beaux Arts"]),
 ("Shakespeare's comedy with Puck and Bottom", "A Midsummer Night's Dream", ["The Tempest", "The Winter's Tale", "As You Like It"]), ("Ben Stiller's comedy where the exhibits come alive", "Night at the Museum", ["Meet the Parents", "Zoolander", "Tropic Thunder"]),
 ("The Bee Gees' 1978 UK number one", "Night Fever", ["Stayin' Alive", "How Deep Is Your Love", "Tragedy"]), ("The 1985 horror about a vampire moving in next door", "Fright Night", ["The Lost Boys", "Near Dark", "Vamp"]),
 ("Frank Sinatra's 1966 number one", "Strangers in the Night", ["My Way", "Somethin' Stupid", "New York, New York"]), ("Kool & the Gang's 1979 hit", "Ladies' Night", ["Celebration", "Get Down on It", "Cherish"]),
 ("Madness's 1979 instrumental-ish single", "Night Boat to Cairo", ["Our House", "Baggy Trousers", "House of Fun"]), ("Murray Head's 1984 hit from the musical Chess", "One Night in Bangkok", ["I Know Him So Well", "Anthem", "Nobody's Side"]),
 ("Someone who likes to stay up late", "Night owl", ["Early bird", "Lark", "Dormouse"]), ("Working while everyone else sleeps", "Night shift", ["Overtime", "Day shift", "Flexitime"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-83.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
