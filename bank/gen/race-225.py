# Bank session 18 Oct 2026: 2 general races -> bank/race-225.json (Shipping Forecast areas, clouds and sky sights).
# Cycling and Tube races were drafted first, but both overlapped existing races, so they were replaced. Clue-style rows are fine since 13 Oct (the race title asks the question).
# Checked against every race in stock with lqsql/audit/race-overlap.py before importing.
# raceOk: 20 rows, 20 different right answers, no right answer among another row's options, no wrong option on 3+ rows.
import json, os
from collections import Counter
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    over = [w for w, n in Counter(w for _, _, wrong in rows for w in wrong).items() if n > 2]
    assert not over, (title, 'wrong option on 3+ rows', over)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("which Shipping Forecast area is this?", "UK geography", "hard", ["Shipping Forecast", "sea", "radio", "geography"], [
 ("Named after the North Sea bank that was once land joining Britain to Europe", "Dogger", ["North Utsire", "Sole", "Moray"]),
 ("Renamed in 2002 after the founder of the Met Office", "FitzRoy", ["Finisterre", "Beaufort", "Nelson"]),
 ("Off north-west Germany and south-west Denmark", "German Bight", ["Fisher", "South Utsire", "Skagerrak"]),
 ("Named after a lighthouse rock off south-west Ireland", "Fastnet", ["Sole", "Cork", "Mizen"]),
 ("The remotest area, named after a tiny islet far west of the Hebrides", "Rockall", ["Bailey", "St Kilda", "Faeroes"]),
 ("The far north of the North Sea, between Shetland and Norway", "Viking", ["North Utsire", "Faeroes", "Bergen"]),
 ("Named after a stretch of sea about forty fathoms deep, off north-east Scotland", "Forties", ["Fathoms", "Fisher", "Moray"]),
 ("Off the Moray Firth and Inverness", "Cromarty", ["Forth", "Orkney", "Pentland"]),
 ("Named after the most northerly point of Ireland", "Malin", ["Clyde", "Irish Sea", "Donegal"]),
 ("Named after the Bristol Channel island famous for puffins", "Lundy", ["Severn", "Bristol", "Portland"]),
 ("Our own North East coast, from Berwick down to Whitby", "Tyne", ["Forth", "Wear", "Tees"]),
 ("Off Yorkshire and Lincolnshire, named after an estuary", "Humber", ["Wash", "Tees", "Trent"]),
 ("Off Essex and Kent, named after a river", "Thames", ["Medway", "Wash", "Severn"]),
 ("The narrowest part of the English Channel", "Dover", ["Calais", "Portland", "Solent"]),
 ("Named after the island off Hampshire", "Wight", ["Solent", "Plymouth", "Purbeck"]),
 ("Off south-west Spain, named after Nelson's last battle", "Trafalgar", ["Nelson", "Cadiz", "Finisterre"]),
 ("Off western Ireland, named after a river", "Shannon", ["Galway", "Liffey", "Cork"]),
 ("The famously stormy bay off western France", "Biscay", ["Brest", "Gascony", "Plymouth"]),
 ("Off the Western Isles of Scotland", "Hebrides", ["St Kilda", "Minch", "Bailey"]),
 ("Named after the island between Orkney and Shetland famous for its knitwear", "Fair Isle", ["Orkney", "Shetland", "Foula"])])

race("name the cloud or sky sight", "Nature and the environment", "medium", ["weather", "clouds", "sky", "nature"], [
 ("The towering thunder cloud", "Cumulonimbus", ["Altostratus", "Stratocumulus", "Cirrocumulus"]),
 ("Thin, wispy high cloud, the 'mares' tails'", "Cirrus", ["Cirrostratus", "Altocumulus", "Smog"]),
 ("Fluffy, fair-weather cotton-wool cloud", "Cumulus", ["Stratocumulus", "Altostratus", "Pileus"]),
 ("A low grey blanket of cloud, like fog that has lifted", "Stratus", ["Cirrocumulus", "Altocumulus", "Shelf cloud"]),
 ("A thick, dark, featureless layer that brings steady rain", "Nimbostratus", ["Cirrostratus", "Wall cloud", "Funnel cloud"]),
 ("Pouch-like bulges hanging under a storm cloud", "Mammatus", ["Pileus", "Shelf cloud", "Wall cloud"]),
 ("A smooth, lens- or UFO-shaped cloud over mountains", "Lenticular cloud", ["Funnel cloud", "Ball lightning", "Will-o'-the-wisp"]),
 ("Glowing clouds seen on summer nights, the highest of all", "Noctilucent clouds", ["Zodiacal light", "St Elmo's fire", "Ball lightning"]),
 ("Rows of small ripples that look like fish scales", "Mackerel sky", ["Herring sky", "Salmon sky", "Sardine sky"]),
 ("A bright spot either side of the Sun, also called a parhelion", "Sun dog", ["Moonbow", "Glory", "Sun cat"]),
 ("A ring of light round the Sun or Moon, made by ice crystals", "Halo", ["Glory", "Iridescence", "Zodiacal light"]),
 ("A white rainbow made in fog", "Fogbow", ["Iridescence", "Sea fret", "Smog"]),
 ("Streaks of rain that dry up before they reach the ground", "Virga", ["Drizzle", "Sleet", "Graupel"]),
 ("The cold sea fog of Scotland's east coast", "Haar", ["Mist", "Murk", "Smirr"]),
 ("The line of cloud left behind a jet", "Contrail", ["Jet stream", "Slipstream", "Airstream"]),
 ("The Northern Lights' Latin name", "Aurora borealis", ["Aurora australis", "Ignis fatuus", "Stella maris"]),
 ("Your giant shadow on the mist below a mountain top", "Brocken spectre", ["Will-o'-the-wisp", "Fata Morgana", "Green man"]),
 ("A flicker of colour at the top of the setting Sun", "Green flash", ["Blue moon", "Red sky", "Fata Morgana"]),
 ("Sunbeams fanning out through gaps in the clouds", "Crepuscular rays", ["Solar flares", "Cosmic rays", "Northern rays"]),
 ("The flat, spreading top of a thunderstorm cloud", "Anvil", ["Hammerhead", "Plateau", "Crown"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-225.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
