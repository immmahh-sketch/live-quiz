# Bank session 10 Oct 2026: 4 more general races -> bank/race-41.json. 20 rows each, target 10; wrong options are
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

race("what's on this club's badge?", "Football", "medium", ["football", "club badges"], [
 ("Arsenal", "Cannon", ["Anchor", "Crown", "Sword"]), ("Tottenham Hotspur", "Cockerel", ["Peacock", "Magpie", "Pheasant"]),
 ("Liverpool", "Liver bird", ["Seahorse", "Hawk", "Falcon"]), ("Leicester City", "Fox", ["Badger", "Wolf", "Rabbit"]),
 ("Norwich City", "Canary", ["Kestrel", "Magpie", "Peacock"]), ("Crystal Palace", "Eagle", ["Hawk", "Falcon", "Kestrel"]),
 ("Brentford", "Bee", ["Hornet", "Wasp", "Butterfly"]), ("Ipswich Town", "Horse", ["Unicorn", "Stag", "Bull"]),
 ("Derby County", "Ram", ["Bull", "Stag", "Goat"]), ("Sheffield Wednesday", "Owl", ["Hawk", "Magpie", "Kestrel"]),
 ("Huddersfield Town", "Terrier", ["Badger", "Wolf", "Bulldog"]), ("Bristol City", "Robin", ["Magpie", "Wren", "Kestrel"]),
 ("West Bromwich Albion", "Thrush", ["Magpie", "Wren", "Blackbird"]), ("Hull City", "Tiger", ["Leopard", "Panther", "Wolf"]),
 ("Coventry City", "Elephant", ["Rhino", "Bull", "Bear"]), ("Brighton & Hove Albion", "Seagull", ["Albatross", "Gannet", "Puffin"]),
 ("Swansea City", "Swan", ["Dragon", "Goose", "Heron"]), ("Cardiff City", "Bluebird", ["Dragon", "Kingfisher", "Magpie"]),
 ("Chelsea", "Lion", ["Unicorn", "Dragon", "Bear"]), ("Everton", "Tower", ["Castle", "Lighthouse", "Bridge"])])

race("which country is this national park in?", "World geography", "medium", ["national parks", "countries"], [
 ("Kruger", "South Africa", ["Botswana", "Zimbabwe", "Mozambique"]), ("The Serengeti", "Tanzania", ["Rwanda", "Ethiopia", "Zambia"]),
 ("Banff", "Canada", ["Greenland", "Mexico", "Norway"]), ("Yellowstone", "the USA", ["Mexico", "Greenland", "Norway"]),
 ("Kakadu", "Australia", ["Papua New Guinea", "Fiji", "Malaysia"]), ("Fiordland", "New Zealand", ["Norway", "Chile", "Fiji"]),
 ("The Galápagos", "Ecuador", ["Peru", "Colombia", "Chile"]), ("Etosha", "Namibia", ["Botswana", "Angola", "Zambia"]),
 ("The Masai Mara", "Kenya", ["Ethiopia", "Rwanda", "Zambia"]), ("Chitwan", "Nepal", ["Bhutan", "Bangladesh", "Sri Lanka"]),
 ("Komodo", "Indonesia", ["the Philippines", "Malaysia", "Papua New Guinea"]), ("Jim Corbett", "India", ["Bhutan", "Pakistan", "Sri Lanka"]),
 ("Bwindi Impenetrable", "Uganda", ["Rwanda", "Burundi", "Ethiopia"]), ("Virunga", "DR Congo", ["Rwanda", "Burundi", "Gabon"]),
 ("The Cairngorms", "Scotland", ["Wales", "England", "Norway"]), ("Killarney", "Ireland", ["Wales", "England", "the Faroe Islands"]),
 ("Abisko", "Sweden", ["Norway", "Finland", "Denmark"]), ("Gran Paradiso", "Italy", ["Switzerland", "Austria", "France"]),
 ("Vatnajökull", "Iceland", ["Greenland", "Norway", "the Faroe Islands"]), ("Triglav", "Slovenia", ["Croatia", "Austria", "Switzerland"])])

race("which Scottish place has this Gaelic name?", "Scotland", "hard", ["Gaelic", "place names", "Scotland"], [
 ("Dùn Èideann", "Edinburgh", ["Dunfermline", "Dumfries", "Dunoon"]), ("Glaschu", "Glasgow", ["Paisley", "Falkirk", "Greenock"]),
 ("Obar Dheathain", "Aberdeen", ["Elgin", "Arbroath", "Montrose"]), ("Inbhir Nis", "Inverness", ["Inveraray", "Invergordon", "Nairn"]),
 ("Dùn Dè", "Dundee", ["Dumfries", "Dunoon", "Dunfermline"]), ("Peairt", "Perth", ["Paisley", "Peebles", "Peterhead"]),
 ("Sruighlea", "Stirling", ["Falkirk", "St Andrews", "Kirkcaldy"]), ("An t-Òban", "Oban", ["Ayr", "Mallaig", "Tobermory"]),
 ("An Gearasdan", "Fort William", ["Fort Augustus", "Fort George", "Mallaig"]), ("Port Rìgh", "Portree", ["Port Ellen", "Portpatrick", "Tobermory"]),
 ("Steòrnabhagh", "Stornoway", ["Tarbert", "Castlebay", "Lochmaddy"]), ("An t-Eilean Sgitheanach", "Skye", ["Arran", "Tiree", "Barra"]),
 ("Muile", "Mull", ["Arran", "Tiree", "Coll"]), ("Ìle", "Islay", ["Jura", "Arran", "Barra"]),
 ("Alba", "Scotland", ["Ireland", "Wales", "the Isle of Man"]), ("Leòdhas", "Lewis", ["Barra", "Tiree", "Uist"]),
 ("Na Hearadh", "Harris", ["Uist", "Barra", "Coll"]), ("Ullapul", "Ullapool", ["Mallaig", "Kyle of Lochalsh", "Thurso"]),
 ("Baile Chloichridh", "Pitlochry", ["Aberfeldy", "Crieff", "Braemar"]), ("An Aghaidh Mhòr", "Aviemore", ["Braemar", "Ballater", "Kingussie"])])

race("whose national day falls on this date?", "World geography", "hard", ["national days", "countries"], [
 ("4 July", "the USA", ["Australia", "Argentina", "Chile"]), ("14 July", "France", ["Luxembourg", "Austria", "Poland"]),
 ("25 March", "Greece", ["Bulgaria", "Croatia", "Romania"]), ("1 October", "China", ["Taiwan", "Vietnam", "Mongolia"]),
 ("6 February", "New Zealand", ["Australia", "Fiji", "Samoa"]), ("5 June", "Denmark", ["Iceland", "Poland", "Austria"]),
 ("3 October", "Germany", ["Austria", "Hungary", "Czechia"]), ("17 May", "Norway", ["Iceland", "Poland", "Estonia"]),
 ("6 June", "Sweden", ["Iceland", "Poland", "Estonia"]), ("6 December", "Finland", ["Estonia", "Iceland", "Russia"]),
 ("15 August", "India", ["Pakistan", "Bangladesh", "Sri Lanka"]), ("1 July", "Canada", ["Australia", "Iceland", "Ireland"]),
 ("16 September", "Mexico", ["Argentina", "Chile", "Colombia"]), ("7 September", "Brazil", ["Argentina", "Peru", "Colombia"]),
 ("27 April (King's Day)", "the Netherlands", ["Luxembourg", "Austria", "Poland"]), ("2 June", "Italy", ["Austria", "Croatia", "Malta"]),
 ("12 October", "Spain", ["Argentina", "Chile", "Malta"]), ("10 June", "Portugal", ["Croatia", "Luxembourg", "Malta"]),
 ("21 July", "Belgium", ["Luxembourg", "Austria", "Poland"]), ("1 August", "Switzerland", ["Austria", "Liechtenstein", "Luxembourg"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-41.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
