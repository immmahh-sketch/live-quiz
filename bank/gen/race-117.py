# Bank session 10 Oct 2026: 2 more general races -> bank/race-117.json (where famous ships are, festival foods). 20 rows each, target 10; wrong options are
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

race("where can you go aboard this famous ship?", "History", "hard", ["ships", "museums", "travel"], [
 ("HMS Victory, Nelson's flagship", "Portsmouth", ["Southampton", "Chatham", "Plymouth"]),
 ("The Cutty Sark tea clipper", "Greenwich", ["Chatham", "Southampton", "Liverpool"]),
 ("Brunel's SS Great Britain", "Bristol", ["Liverpool", "Southampton", "Cardiff"]),
 ("Scott's RRS Discovery", "Dundee", ["Aberdeen", "Inverness", "Edinburgh"]),
 ("The Royal Yacht Britannia", "Leith", ["Rosyth", "Greenock", "Aberdeen"]),
 ("The Glenlee tall ship", "Glasgow", ["Greenock", "Aberdeen", "Liverpool"]),
 ("The Vasa, raised from the seabed in 1961", "Stockholm", ["Copenhagen", "Gothenburg", "Helsinki"]),
 ("The Kon-Tiki raft", "Oslo", ["Bergen", "Copenhagen", "Reykjavik"]),
 ("USS Constitution, 'Old Ironsides'", "Boston", ["Baltimore", "Philadelphia", "San Diego"]),
 ("The RMS Queen Mary, now a hotel", "Long Beach", ["San Diego", "Miami", "Baltimore"]),
 ("SS Nomadic, the Titanic's little tender", "Belfast", ["Southampton", "Liverpool", "Cobh"]),
 ("The aircraft carrier USS Intrepid", "New York", ["San Diego", "Baltimore", "Norfolk"]),
 ("A full-size replica of Captain Cook's Endeavour", "Whitby", ["Scarborough", "Sunderland", "Liverpool"]),
 ("The Mayflower II", "Plymouth, Massachusetts", ["Cape Cod", "Baltimore", "Southampton"]),
 ("The Golden Hinde, Drake's ship rebuilt", "London", ["Chatham", "Plymouth", "Falmouth"]),
 ("The battleship USS Missouri", "Pearl Harbor", ["San Diego", "Norfolk", "Baltimore"]),
 ("The submarine HMS Alliance", "Gosport", ["Chatham", "Plymouth", "Barrow-in-Furness"]),
 ("The QE2, now a floating hotel", "Dubai", ["Singapore", "Hong Kong", "Abu Dhabi"]),
 ("The SS Rotterdam, now a hotel", "Rotterdam", ["Amsterdam", "Antwerp", "Hamburg"]),
 ("The Arctic Corsair trawler", "Hull", ["Grimsby", "Fleetwood", "Aberdeen"])])

race("which festival or occasion is this food eaten at?", "Food and drink", "medium", ["festivals", "food", "traditions"], [
 ("Hot cross buns", "Good Friday", ["Maundy Thursday", "Ash Wednesday", "Palm Sunday"]),
 ("Simnel cake", "Easter", ["Maundy Thursday", "Ash Wednesday", "Whit Sunday"]),
 ("Pancakes", "Shrove Tuesday", ["Ash Wednesday", "Palm Sunday", "Whit Sunday"]),
 ("Mince pies", "Christmas", ["Harvest Festival", "Candlemas", "Whit Sunday"]),
 ("Haggis, neeps and tatties", "Burns Night", ["St Andrew's Day", "Up Helly Aa", "Candlemas"]),
 ("Parkin", "Bonfire Night", ["Harvest Festival", "Candlemas", "Up Helly Aa"]),
 ("Latkes and doughnuts", "Hanukkah", ["Yom Kippur", "Sukkot", "Rosh Hashanah"]),
 ("Mooncakes", "The Mid-Autumn Festival", ["Lantern Festival", "Dragon Boat Festival", "Qingming"]),
 ("Colcannon, with a ring hidden inside", "Halloween", ["St Patrick's Day", "Candlemas", "St Brigid's Day"]),
 ("Galette des rois, the king cake", "Epiphany", ["Candlemas", "Ash Wednesday", "All Saints' Day"]),
 ("Pączki doughnuts in Poland", "Fat Thursday", ["Ash Wednesday", "Candlemas", "All Saints' Day"]),
 ("Hamantaschen pastries", "Purim", ["Yom Kippur", "Sukkot", "Rosh Hashanah"]),
 ("Matzo, unleavened bread", "Passover", ["Yom Kippur", "Sukkot", "Rosh Hashanah"]),
 ("Dates to break the fast at sunset", "Ramadan", ["Lent", "Yom Kippur", "Vaisakhi"]),
 ("Boxes of sweets called mithai", "Diwali", ["Holi", "Vaisakhi", "Navratri"]),
 ("Pumpkin pie and roast turkey, in America", "Thanksgiving", ["Independence Day", "Labor Day", "Memorial Day"]),
 ("Black bun, a rich fruit cake in pastry", "Hogmanay", ["St Andrew's Day", "Up Helly Aa", "Candlemas"]),
 ("Dumplings shaped like gold ingots", "Chinese New Year", ["Lantern Festival", "Dragon Boat Festival", "Qingming"]),
 ("Pan de muerto, the 'bread of the dead'", "The Day of the Dead", ["Cinco de Mayo", "Candlemas", "All Saints' Day"]),
 ("Saffron buns called lussekatter, in Sweden", "St Lucia's Day", ["Midsummer", "Walpurgis Night", "Candlemas"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-117.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
