# Bank session 10 Oct 2026: 2 more general races -> bank/race-82.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Box'?", "General knowledge", "medium", ["boxes", "wordplay"], [
 ("The container of evils in Greek myth", "Pandora's box", ["Psyche's casket", "Midas's chest", "Helen's jar"]), ("An aircraft's orange flight recorder", "Black box", ["Grey box", "Blue box", "Flight deck"]),
 ("The battered case the Chancellor holds up on Budget Day", "Red box", ["Gladstone bag", "Briefcase", "Attaché case"]), ("Where you put your vote", "Ballot box", ["Post box", "Polling booth", "Ballot paper"]),
 ("Microsoft's games console", "Xbox", ["PlayStation", "GameCube", "Dreamcast"]), ("The Channel 4 show of people watching telly", "Gogglebox", ["Telly Addicts", "TV Burp", "Big Brother"]),
 ("Football's 18-yard area", "Penalty box", ["Six-yard box", "Centre circle", "Technical area"]), ("The Who's 1975 song about an accordion", "Squeezebox", ["Pinball Wizard", "Substitute", "Happy Jack"]),
 ("John Masefield's magical Christmas story, a BBC serial in 1984", "The Box of Delights", ["The Midnight Folk", "The Children of Green Knowe", "Moondial"]), ("A small spare bedroom", "Box room", ["Utility room", "Snug", "Scullery"]),
 ("The yellow criss-cross road markings you mustn't stop in", "Box junction", ["Zebra crossing", "Pelican crossing", "Red route"]), ("Forrest Gump: 'Life is like a ...'", "Box of chocolates", ["Bowl of cherries", "Bag of sweets", "Game of chess"]),
 ("The little box that plays a tune while a ballerina spins", "Music box", ["Jukebox", "Gramophone", "Barrel organ"]), ("The car compartment in front of the passenger", "Glovebox", ["Boot", "Dashboard", "Centre console"]),
 ("A situation ready to burst into flames, or an old fire-lighting kit", "Tinderbox", ["Hornet's nest", "Hotbed", "Firebox"]), ("The red Victorian post box on the street corner", "Pillar box", ["Wall box", "Letter box", "Mail drop"]),
 ("Where a witness stands in court", "Witness box", ["Dock", "Jury box", "Bench"]), ("The 1960s American band behind 'The Letter'", "The Box Tops", ["The Turtles", "The Monkees", "The Lovin' Spoonful"]),
 ("Old slang for the TV, the '... box'", "Idiot box", ["Boob tube", "Square eyes", "Telly"]), ("The red kiosk designed by Giles Gilbert Scott", "Telephone box", ["Police box", "Sentry box", "Bus shelter"])])

race("which famous 'Club'?", "General knowledge", "medium", ["clubs", "wordplay"], [
 ("The 1999 film with Brad Pitt and Edward Norton", "Fight Club", ["Se7en", "American History X", "Snatch"]), ("John Hughes's 1985 film about a Saturday detention", "The Breakfast Club", ["Sixteen Candles", "Pretty in Pink", "Ferris Bueller's Day Off"]),
 ("Boy George's band", "Culture Club", ["Duran Duran", "Spandau Ballet", "Wham!"]), ("Wham!'s 1983 holiday hit", "Club Tropicana", ["Wake Me Up Before You Go-Go", "Last Christmas", "Young Guns"]),
 ("The Liverpool cellar where the Beatles played nearly 300 times", "The Cavern Club", ["The Casbah", "The Jacaranda", "Eric's"]), ("Brian Potter's club in Peter Kay's Phoenix Nights", "The Phoenix Club", ["The Wheeltappers and Shunters", "Talk of the Town", "The Rovers Return"]),
 ("Where Phileas Fogg made his round-the-world bet", "The Reform Club", ["The Athenaeum", "The Garrick", "White's"]), ("Mycroft Holmes's club for men who hate company", "The Diogenes Club", ["The Carlton Club", "The Athenaeum", "The Garrick"]),
 ("Bertie Wooster's club", "The Drones Club", ["The Junior Ganymede", "The Senior Conservative", "Blandings"]), ("Rock stars who died at the same young age, like Hendrix, Joplin and Cobain", "The 27 Club", ["The 25 Club", "The 30 Club", "The 33 Club"]),
 ("The Cuban musicians filmed by Wim Wenders", "Buena Vista Social Club", ["Havana Social Club", "Tropicana Club", "Gipsy Kings"]), ("Amy Tan's novel about Chinese-American mothers and daughters", "The Joy Luck Club", ["Crazy Rich Asians", "Wild Swans", "The Kite Runner"]),
 ("'If you like a lot of chocolate on your biscuit, join our ...'", "Club", ["Penguin", "Breakaway", "Blue Riband"]), ("The holiday firm for party-loving 18-to-30s", "Club 18-30", ["Club Med", "Contiki", "Butlin's"]),
 ("Ann M. Martin's books about teen babysitters", "The Baby-Sitters Club", ["Sweet Valley High", "The Saddle Club", "Goosebumps"]), ("The Soho members' club named after a Marx brothers joke", "The Groucho Club", ["The Ivy", "Soho House", "The Garrick"]),
 ("Sir Francis Dashwood's scandalous 18th-century secret society", "The Hellfire Club", ["The Kit-Kat Club", "The Beefsteak Club", "The Order of the Garter"]), ("The Oxford dining society of David Cameron and Boris Johnson", "The Bullingdon Club", ["The Piers Gaveston Society", "The Footlights", "The Oxford Union"]),
 ("Richard and Judy's TV reading group", "Book club", ["Reading circle", "Library", "Literary society"]), ("Disney's online game world for children, with igloos", "Club Penguin", ["Moshi Monsters", "Habbo Hotel", "Neopets"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-82.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
