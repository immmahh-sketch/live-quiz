# Bank session 10 Oct 2026: 2 more general races -> bank/race-90.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Rose'?", "General knowledge", "medium", ["roses", "wordplay"], [
 ("The 15th-century civil wars between Lancaster and York", "Wars of the Roses", ["Hundred Years' War", "Barons' Wars", "The Anarchy"]), ("Charles Foster Kane's dying word", "Rosebud", ["Xanadu", "Mother", "Susan"]),
 ("Billie Piper's character in Doctor Who", "Rose Tyler", ["Martha Jones", "Donna Noble", "Clara Oswald"]), ("The red-and-white emblem of Henry VII's dynasty", "Tudor rose", ["English rose", "Rose of Sharon", "Thistle"]),
 ("The Bankside playhouse built before the Globe", "The Rose", ["The Swan", "The Curtain", "The Hope"]), ("Umberto Eco's medieval monastery murder mystery", "The Name of the Rose", ["Foucault's Pendulum", "The Da Vinci Code", "Baudolino"]),
 ("Seal's hit from Batman Forever", "Kiss from a Rose", ["Crazy", "Killer", "Prayer for the Dying"]), ("Poison's 1988 power ballad", "Every Rose Has Its Thorn", ["Nothing but a Good Time", "Talk Dirty to Me", "Home Sweet Home"]),
 ("The disco band behind 'Car Wash'", "Rose Royce", ["Kool & the Gang", "The Trammps", "Chic"]), ("Axl Rose's band", "Guns N' Roses", ["Mötley Crüe", "Bon Jovi", "Def Leppard"]),
 ("The Manchester band behind 'I Wanna Be Adored'", "The Stone Roses", ["Happy Mondays", "Inspiral Carpets", "The Charlatans"]), ("Sting's 1999 hit with Cheb Mami", "Desert Rose", ["Fields of Gold", "Englishman in New York", "Shape of My Heart"]),
 ("The nursery rhyme with 'a pocket full of posies'", "Ring a Ring o' Roses", ["Oranges and Lemons", "Here We Go Round the Mulberry Bush", "The Grand Old Duke of York"]), ("What you see the past through when it seems better than it was", "Rose-tinted glasses", ["Hindsight", "Nostalgia", "Blinkers"]),
 ("The red fruit of the wild rose, made into a syrup", "Rose hip", ["Sloe", "Haw", "Elderberry"]), ("The Pasadena stadium of the 1994 World Cup final", "Rose Bowl", ["Orange Bowl", "Cotton Bowl", "Sugar Bowl"]),
 ("The Australian actress in Bridesmaids and Neighbors", "Rose Byrne", ["Rebel Wilson", "Margot Robbie", "Cate Blanchett"]), ("The Blackpink star behind 'APT.' with Bruno Mars", "Rosé", ["Lisa", "Jennie", "Jisoo"]),
 ("The New Zealand comedian who created and starred in Starstruck", "Rose Matafeo", ["Rhys Darby", "Jemaine Clement", "Taika Waititi"]), ("The first deaf winner of Strictly Come Dancing, in 2021", "Rose Ayling-Ellis", ["Bill Bailey", "Hamza Yassin", "Ellie Leach"])])

race("which famous 'Thunder'?", "General knowledge", "medium", ["thunder", "wordplay"], [
 ("Gerry Anderson's puppet rescue show", "Thunderbirds", ["Stingray", "Captain Scarlet", "Joe 90"]), ("Sean Connery's 1965 Bond film", "Thunderball", ["Goldfinger", "You Only Live Twice", "From Russia with Love"]),
 ("AC/DC's 1990 stadium anthem", "Thunderstruck", ["Highway to Hell", "Back in Black", "T.N.T."]), ("Tom Cruise's 1990 NASCAR film", "Days of Thunder", ["Top Gun", "Cocktail", "Far and Away"]),
 ("The 1980s cartoon with Lion-O", "ThunderCats", ["He-Man", "Visionaries", "SilverHawks"]), ("Ben Stiller's 2008 war-film spoof", "Tropic Thunder", ["Zoolander", "Dodgeball", "Hot Shots! Part Deux"]),
 ("1985's 'Mad Max Beyond ...'", "Thunderdome", ["Fury Road", "The Road Warrior", "Wasteland"]), ("Imagine Dragons' 2017 hit", "Thunder", ["Believer", "Radioactive", "Demons"]),
 ("The band behind 1969's number one 'Something in the Air'", "Thunderclap Newman", ["The Move", "Amen Corner", "Marmalade"]), ("To grab the credit someone else deserves", "Steal their thunder", ["Steal a march", "Rain on their parade", "Take the biscuit"]),
 ("Ford's classic two-seater of 1955", "Thunderbird", ["Mustang", "Corvette", "Firebird"]), ("Clint Eastwood and Jeff Bridges' 1974 heist film", "Thunderbolt and Lightfoot", ["Kelly's Heroes", "Escape from Alcatraz", "The Gauntlet"]),
 ("In Bohemian Rhapsody, what's 'very, very frightening me'?", "Thunderbolt and lightning", ["Scaramouche", "Galileo", "Bismillah"]), ("The Canadian port city on Lake Superior", "Thunder Bay", ["Sault Ste. Marie", "Duluth", "Kingston"]),
 ("Full-blooded, passionate rugby, all 'blood and ...'", "Blood and thunder", ["Blood and guts", "Blood and sand", "Fire and brimstone"]), ("Meck and Leo Sayer's 2006 number one", "Thunder in My Heart", ["You Make Me Feel Like Dancing", "When I Need You", "Moonlighting"]),
 ("The P-47 fighter plane of the Second World War", "Thunderbolt", ["Mustang", "Spitfire", "Lightning"]), ("Bob Dylan's travelling 1975 tour", "Rolling Thunder Revue", ["Never Ending Tour", "The Last Waltz", "Blood on the Tracks"]),
 ("Oklahoma City's NBA team", "Oklahoma City Thunder", ["Denver Nuggets", "San Antonio Spurs", "Houston Rockets"]), ("Disney's runaway mine train ride", "Big Thunder Mountain", ["Space Mountain", "Splash Mountain", "Matterhorn Bobsleds"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-90.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
