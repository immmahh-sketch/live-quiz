# Bank session 10 Oct 2026: 2 more general races -> bank/race-111.json (Bond henchmen, where brands began). 20 rows each, target 10; wrong options are
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

race("which Bond film is this henchman from?", "James Bond", "hard", ["James Bond", "villains", "films"], [
 ("Oddjob, with his steel-rimmed bowler hat", "Goldfinger", ["Quantum of Solace", "You Only Live Twice", "Casino Royale"]),
 ("Rosa Klebb, with a poisoned blade in her shoe", "From Russia with Love", ["Quantum of Solace", "You Only Live Twice", "For Your Eyes Only"]),
 ("Nick Nack, Scaramanga's tiny butler", "The Man with the Golden Gun", ["You Only Live Twice", "For Your Eyes Only", "Quantum of Solace"]),
 ("May Day, played by Grace Jones", "A View to a Kill", ["For Your Eyes Only", "Casino Royale", "You Only Live Twice"]),
 ("Xenia Onatopp, who crushes men with her thighs", "GoldenEye", ["The World Is Not Enough", "Casino Royale", "Quantum of Solace"]),
 ("Tee Hee, with a metal claw for a hand", "Live and Let Die", ["You Only Live Twice", "For Your Eyes Only", "Casino Royale"]),
 ("Mr Hinx, who gouges eyes with his thumbnails", "Spectre", ["Quantum of Solace", "Casino Royale", "The World Is Not Enough"]),
 ("Mr Wint and Mr Kidd", "Diamonds Are Forever", ["You Only Live Twice", "For Your Eyes Only", "Casino Royale"]),
 ("Fiona Volpe, SPECTRE's red-haired assassin", "Thunderball", ["You Only Live Twice", "For Your Eyes Only", "Quantum of Solace"]),
 ("Irma Bunt, Blofeld's stern sidekick in the Alps", "On Her Majesty's Secret Service", ["You Only Live Twice", "For Your Eyes Only", "Casino Royale"]),
 ("Necros, who strangles with his headphone wire", "The Living Daylights", ["For Your Eyes Only", "Casino Royale", "The World Is Not Enough"]),
 ("Gobinda, who crushes dice in his fist", "Octopussy", ["For Your Eyes Only", "You Only Live Twice", "The World Is Not Enough"]),
 ("Stamper, Elliot Carver's blond heavy", "Tomorrow Never Dies", ["The World Is Not Enough", "Quantum of Solace", "Casino Royale"]),
 ("Zao, with diamonds stuck in his face", "Die Another Day", ["The World Is Not Enough", "Quantum of Solace", "Casino Royale"]),
 ("Patrice, the sniper who falls from a Shanghai tower", "Skyfall", ["Quantum of Solace", "Casino Royale", "The World Is Not Enough"]),
 ("Primo, with a bionic eye", "No Time to Die", ["Quantum of Solace", "Casino Royale", "The World Is Not Enough"]),
 ("Dario, played by a young Benicio del Toro", "Licence to Kill", ["For Your Eyes Only", "The World Is Not Enough", "Quantum of Solace"]),
 ("Chang, Drax's kendo-fighting manservant", "Moonraker", ["For Your Eyes Only", "You Only Live Twice", "The World Is Not Enough"]),
 ("Professor Dent, sent with a tarantula", "Dr. No", ["You Only Live Twice", "For Your Eyes Only", "Casino Royale"]),
 ("Jaws, on his very first outing", "The Spy Who Loved Me", ["For Your Eyes Only", "You Only Live Twice", "The World Is Not Enough"])])

race("which town or city did this famous brand start in?", "Brands", "hard", ["brands", "Britain", "business"], [
 ("Greggs", "Newcastle", ["Sunderland", "Durham", "Middlesbrough"]),
 ("Boots the Chemist", "Nottingham", ["Derby", "Lincoln", "Chesterfield"]),
 ("Marks & Spencer, as a market stall", "Leeds", ["Manchester", "Liverpool", "Huddersfield"]),
 ("Morrisons", "Bradford", ["Halifax", "Huddersfield", "Wakefield"]),
 ("Cadbury", "Birmingham", ["Coventry", "Wolverhampton", "Bristol"]),
 ("Rowntree's", "York", ["Harrogate", "Halifax", "Hull"]),
 ("Lea & Perrins Worcestershire sauce", "Worcester", ["Hereford", "Gloucester", "Cheltenham"]),
 ("Colman's mustard", "Norwich", ["Ipswich", "Cambridge", "King's Lynn"]),
 ("Hovis bread", "Macclesfield", ["Stockport", "Crewe", "Stoke"]),
 ("Barbour", "South Shields", ["Hexham", "Morpeth", "Gateshead"]),
 ("Wilko", "Leicester", ["Derby", "Northampton", "Coventry"]),
 ("JD Sports", "Bury", ["Rochdale", "Oldham", "Wigan"]),
 ("Iceland", "Oswestry", ["Shrewsbury", "Wrexham", "Chester"]),
 ("Lush cosmetics", "Poole", ["Bournemouth", "Brighton", "Bath"]),
 ("Thorntons chocolates", "Sheffield", ["Rotherham", "Barnsley", "Chesterfield"]),
 ("Warburtons", "Bolton", ["Wigan", "Preston", "Blackburn"]),
 ("Burberry", "Basingstoke", ["Reading", "Guildford", "Winchester"]),
 ("Clarks shoes", "Street", ["Glastonbury", "Wells", "Taunton"]),
 ("Primark, as Penneys", "Dublin", ["Belfast", "Cork", "Galway"]),
 ("Ted Baker", "Glasgow", ["Edinburgh", "Aberdeen", "Dundee"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-111.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
