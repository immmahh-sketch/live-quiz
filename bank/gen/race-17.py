# Bank session 10 Oct 2026: 4 more general races -> bank/race-17.json. 20 rows each, target 10; wrong options are
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

race("name the pub or bar", "Film, TV and books", "medium", ["pubs", "fiction"], [
 ("EastEnders' local", "The Queen Vic", ["The Queen's Arms", "The Albert", "The Beale Arms"]), ("Coronation Street's local", "The Rovers Return", ["The Rovers Rest", "The Weatherfield Arms", "The Bargain Arms"]),
 ("Emmerdale's local", "The Woolpack", ["The Wool Shed", "The Dingle Arms", "The Sheep's Head"]), ("Hollyoaks' local", "The Dog in the Pond", ["The Duck in the Pond", "The Cat and Fiddle", "The Fox and Hounds"]),
 ("Del Boy's local in Only Fools", "The Nag's Head", ["The Horse and Groom", "The Trotters' Arms", "The Three Horseshoes"]), ("The pub in The Archers", "The Bull", ["The Cat and Fiddle", "The Feathers", "The Red Lion"]),
 ("Homer's local", "Moe's Tavern", ["Duff's Bar", "Barney's Bar", "Krusty's Tavern"]), ("Where Shaun waits for it all to blow over", "The Winchester", ["The Crown", "The Red Lion", "The King's Arms"]),
 ("The bar in How I Met Your Mother", "MacLaren's", ["Central Perk", "Paddy's Pub", "The Max"]), ("The wizarding pub on Charing Cross Road", "The Leaky Cauldron", ["The Hog's Head", "The Burrow", "Honeydukes"]),
 ("The inn at Bree where Frodo meets Strider", "The Prancing Pony", ["The Ivy Bush", "The Golden Perch", "The Floating Log"]), ("The Hobbits' favourite inn near Hobbiton", "The Green Dragon", ["The Ivy Bush", "The Golden Perch", "The Floating Log"]),
 ("The Hogsmeade pub famous for its Butterbeer", "The Three Broomsticks", ["The Hog's Head", "Honeydukes", "The Burrow"]), ("Brian Potter's club in Phoenix Nights", "The Phoenix Club", ["The Neptune Club", "The Peacock Club", "The Talk of the Town"]),
 ("The moors pub in An American Werewolf in London", "The Slaughtered Lamb", ["The Black Sheep", "The Hanged Man", "The Butcher's Arms"]), ("Jim Hawkins's family inn in Treasure Island", "The Admiral Benbow", ["The Spyglass", "The Jolly Sailor", "The Anchor"]),
 ("The pub in Heartbeat", "The Aidensfield Arms", ["The Ashfordly Arms", "The Goathland Arms", "The Moorland Inn"]), ("The pub in Neighbours", "The Waterhole", ["The Billabong", "The Kangaroo Arms", "Harold's Café"]),
 ("Frank Gallagher's local in Shameless", "The Jockey", ["The Saddle", "The Trotter", "The Racehorse"]), ("The Boston bar where everybody knows your name", "Cheers", ["Norm's", "Sam's Place", "Melville's"])])

race("which country is this cathedral or church in?", "Famous landmarks", "medium", ["cathedrals", "churches", "countries"], [
 ("The Sagrada Família", "Spain", ["Andorra", "Mexico", "Argentina"]), ("Notre-Dame", "France", ["Belgium", "Luxembourg", "Switzerland"]),
 ("St Peter's Basilica", "Vatican City", ["San Marino", "Malta", "Monaco"]), ("Hagia Sophia", "Turkey", ["Greece", "Cyprus", "Bulgaria"]),
 ("St Basil's Cathedral", "Russia", ["Ukraine", "Belarus", "Georgia"]), ("Cologne Cathedral", "Germany", ["Switzerland", "the Netherlands", "Belgium"]),
 ("The Stephansdom", "Austria", ["Switzerland", "Hungary", "Slovakia"]), ("St Vitus Cathedral", "Czechia", ["Slovakia", "Hungary", "Slovenia"]),
 ("The Duomo with Brunelleschi's dome", "Italy", ["Malta", "San Marino", "Croatia"]), ("Canterbury Cathedral", "England", ["Ireland", "Northern Ireland", "the Isle of Man"]),
 ("St Giles' Cathedral", "Scotland", ["Ireland", "Northern Ireland", "the Isle of Man"]), ("St Davids Cathedral", "Wales", ["Ireland", "Northern Ireland", "the Isle of Man"]),
 ("Nidaros Cathedral", "Norway", ["Estonia", "Finland", "the Netherlands"]), ("Oscar Niemeyer's crown-shaped cathedral", "Brazil", ["Argentina", "Mexico", "Chile"]),
 ("Wawel Cathedral", "Poland", ["Slovakia", "Lithuania", "Hungary"]), ("Roskilde Cathedral", "Denmark", ["Finland", "the Netherlands", "Estonia"]),
 ("Uppsala Cathedral", "Sweden", ["Finland", "Estonia", "Latvia"]), ("Hallgrímskirkja", "Iceland", ["Finland", "the Faroe Islands", "Greenland"]),
 ("The rock-cut churches of Lalibela", "Ethiopia", ["Eritrea", "Sudan", "Kenya"]), ("The Jerónimos Monastery", "Portugal", ["Andorra", "Malta", "Argentina"])])

race("what does this Harry Potter spell do?", "Harry Potter", "medium", ["spells", "Harry Potter"], [
 ("Lumos", "Lights up your wand", ["Makes a shield", "Reveals hidden ink", "Points north"]), ("Nox", "Puts out your wand light", ["Ends other spells", "Locks a door", "Makes a shield"]),
 ("Accio", "Summons an object", ["Repels Muggles", "Locks a door", "Reveals hidden ink"]), ("Expelliarmus", "Disarms your opponent", ["Makes a shield", "Ends other spells", "Causes great pain"]),
 ("Wingardium Leviosa", "Makes things float", ["Points north", "Repels Muggles", "Makes a shield"]), ("Alohomora", "Unlocks doors", ["Locks a door", "Reveals hidden ink", "Repels Muggles"]),
 ("Obliviate", "Wipes memories", ["Controls someone's mind", "Reveals hidden ink", "Causes great pain"]), ("Riddikulus", "Defeats a boggart", ["Summons a Patronus", "Ends other spells", "Makes a shield"]),
 ("Stupefy", "Stuns someone", ["Kills instantly", "Causes great pain", "Tickles the target"]), ("Reparo", "Repairs broken things", ["Heals small wounds", "Ends other spells", "Locks a door"]),
 ("Aguamenti", "Makes water", ["Makes a shield", "Points north", "Repels Muggles"]), ("Incendio", "Makes fire", ["Slashes like a sword", "Causes great pain", "Points north"]),
 ("Silencio", "Makes someone silent", ["Locks a door", "Ends other spells", "Controls someone's mind"]), ("Engorgio", "Makes things bigger", ["Heals small wounds", "Reveals hidden ink", "Tickles the target"]),
 ("Reducio", "Makes things smaller", ["Heals small wounds", "Locks a door", "Ends other spells"]), ("Scourgify", "Cleans things", ["Repels Muggles", "Reveals hidden ink", "Ends other spells"]),
 ("Sonorus", "Makes your voice loud", ["Controls someone's mind", "Tickles the target", "Summons a Patronus"]), ("Morsmordre", "Conjures the Dark Mark", ["Kills instantly", "Summons a Patronus", "Controls someone's mind"]),
 ("Tarantallegra", "Makes legs dance", ["Tickles the target", "Controls someone's mind", "Causes great pain"]), ("Petrificus Totalus", "Freezes the whole body", ["Kills instantly", "Slashes like a sword", "Controls someone's mind"])])

race("which Prime Minister had this nickname?", "Politics", "hard", ["Prime Ministers", "nicknames"], [
 ("The Iron Lady", "Margaret Thatcher", ["Clement Attlee", "Harold Wilson", "Anthony Eden"]), ("Supermac", "Harold Macmillan", ["Harold Wilson", "Anthony Eden", "Alec Douglas-Home"]),
 ("The Grey Man", "John Major", ["Alec Douglas-Home", "Anthony Eden", "Clement Attlee"]), ("Teflon Tony", "Tony Blair", ["Harold Wilson", "Keir Starmer", "Ramsay MacDonald"]),
 ("Outlasted by a lettuce", "Liz Truss", ["Keir Starmer", "Anthony Eden", "Alec Douglas-Home"]), ("Dishy Rishi", "Rishi Sunak", ["Keir Starmer", "Harold Wilson", "Robert Peel"]),
 ("The British Bulldog", "Winston Churchill", ["Neville Chamberlain", "Stanley Baldwin", "Clement Attlee"]), ("Pam", "Lord Palmerston", ["Lord Melbourne", "Robert Peel", "Lord John Russell"]),
 ("Dizzy", "Benjamin Disraeli", ["Lord Salisbury", "Robert Peel", "Lord Melbourne"]), ("The Grand Old Man", "William Gladstone", ["Lord Salisbury", "Robert Peel", "Lord Melbourne"]),
 ("Sunny Jim", "James Callaghan", ["Harold Wilson", "Clement Attlee", "Alec Douglas-Home"]), ("The Maybot", "Theresa May", ["Keir Starmer", "Anthony Eden", "Harold Wilson"]),
 ("BoJo", "Boris Johnson", ["Keir Starmer", "Robert Peel", "Harold Wilson"]), ("The Welsh Wizard", "David Lloyd George", ["Stanley Baldwin", "Ramsay MacDonald", "Bonar Law"]),
 ("Old Squiffy", "H. H. Asquith", ["Arthur Balfour", "Henry Campbell-Bannerman", "Bonar Law"]), ("The Clunking Fist", "Gordon Brown", ["Keir Starmer", "Clement Attlee", "Harold Wilson"]),
 ("Ted", "Edward Heath", ["Harold Wilson", "Anthony Eden", "Alec Douglas-Home"]), ("The Iron Duke", "The Duke of Wellington", ["Robert Peel", "Lord Liverpool", "Lord Grey"]),
 ("The Pilot that Weathered the Storm", "William Pitt the Younger", ["Pitt the Elder", "Lord North", "Spencer Perceval"]), ("Call Me Dave", "David Cameron", ["Keir Starmer", "Harold Wilson", "Robert Peel"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-17.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
