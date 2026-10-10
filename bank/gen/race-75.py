# Bank session 10 Oct 2026: 2 more general races -> bank/race-75.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Market'?", "General knowledge", "medium", ["markets", "wordplay"], [
 ("The Newcastle street famous for its Saturday-night revellers", "Bigg", ["Groat", "Cloth", "Grainger"]), ("North London's market beside the Lock", "Camden", ["Greenwich", "Brixton", "Portobello"]),
 ("The City of London's Victorian covered market, used as Diagon Alley", "Leadenhall", ["Borough", "Greenwich", "Brixton"]), ("The East London market beside Hawksmoor's Christ Church", "Spitalfields", ["Borough", "Brixton", "Greenwich"]),
 ("The East London street of the Sunday flower market", "Columbia Road", ["Petticoat Lane", "Brick Lane", "Broadway"]), ("London's historic meat market", "Smithfield", ["Billingsgate", "Covent Garden", "Nine Elms"]),
 ("The old British name for the EEC", "Common", ["Single", "European", "Free"]), ("Illegal buying and selling", "Black", ["Grey", "Dark", "Shadow"]),
 ("Where shares are bought and sold", "Stock", ["Share", "Money", "Bond"]), ("A market where prices keep falling", "Bear", ["Wolf", "Stag", "Lame"]),
 ("A market where prices keep rising", "Bull", ["Stag", "Ox", "Ram"]), ("A second-hand market named after an insect", "Flea", ["Rag", "Jumble", "Junk"]),
 ("Posh, aimed at wealthy shoppers", "Up", ["High", "Top", "Over"]), ("Cheap and cheerful, aimed at bargain hunters", "Down", ["Low", "Cheap", "Under"]),
 ("Where local growers sell straight to shoppers", "Farmers'", ["Growers'", "Country", "Village"]), ("Tokyo's old fish market, famous for its tuna auctions", "Tsukiji", ["Toyosu", "Ginza", "Akihabara"]),
 ("Aimed at as many ordinary buyers as possible", "Mass", ["Big", "Wide", "General"]), ("The German festive tradition of mulled wine and wooden stalls", "Christmas", ["Winter", "Advent", "Yule"]),
 ("Asia's after-dark street food markets", "Night", ["Evening", "Moon", "Dark"]), ("Thailand's markets where traders sell from boats", "Floating", ["Boat", "River", "Water"])])

race("which famous 'Point'?", "General knowledge", "medium", ["points", "wordplay"], [
 ("Mainland Britain's most southerly point, in Cornwall", "Lizard", ["Rame", "Mullion", "Kynance"]), ("The Devon headland and lighthouse facing out towards Lundy", "Hartland", ["Baggy", "Morte", "Bull"]),
 ("The Norfolk spit famous for its seal colony", "Blakeney", ["Scolt", "Holkham", "Cley"]), ("100°C for water at sea level", "Boiling", ["Steaming", "Flash", "Smoke"]),
 ("The temperature at which water turns to ice", "Freezing", ["Frost", "Ice", "Chill"]), ("The temperature at which a solid turns to liquid", "Melting", ["Thawing", "Softening", "Liquid"]),
 ("The temperature at which moisture in the air forms droplets", "Dew", ["Mist", "Fog", "Rain"]), ("In tennis, one point from winning the whole thing", "Match", ["Game", "Final", "Win"]),
 ("In tennis, one point from winning the set", "Set", ["Game", "Tie", "Love"]), ("In tennis, a chance to win your opponent's service game", "Break", ["Return", "Deuce", "Ace"]),
 ("The US Army's military academy in New York State", "West", ["Fort", "Annapolis", "Sandhurst"]), ("Malcolm Gladwell's book about how little things make a big difference", "Tipping", ["Breaking", "Critical", "Crunch"]),
 ("The moment when everything changes", "Turning", ["Breaking", "Crunch", "Pivot"]), ("Microsoft's slideshow program", "Power", ["Slide", "Key", "Show"]),
 ("The dot in 3.14", "Decimal", ["Full", "Period", "Dot"]), ("A list item marked with a dot", "Bullet", ["Dot", "Star", "Tick"]),
 ("Credit for trying to please the boss", "Brownie", ["Bonus", "Gold", "Merit"]), ("A spot on the body that martial artists strike", "Pressure", ["Nerve", "Trigger", "Weak"]),
 ("A topic everyone is discussing", "Talking", ["Speaking", "Chat", "Gossip"]), ("Where something begins", "Starting", ["Opening", "Launch", "Kick-off"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-75.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
