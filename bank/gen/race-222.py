# Bank session 12 Oct 2026: 1 more general race -> bank/race-222.json (lighthouse words). Checked against the lifeboat, pirate,
# navy and shipbuilding races: lighthouse and Grace Darling left out as answers, as the lifeboat race has them.
# 20 rows each, target 10; wrong options are the same kind of thing, never another row's right answer, and never also right for that row.
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

race("what's this lighthouse word?", "History", "medium", ["lighthouses", "sea", "North East", "words"], [
 ("The person who once lived in and ran a lighthouse", "Keeper", ["Warden", "Bosun", "Coxswain"]),
 ("The glass room at the top that holds the light", "Lantern", ["Crow's nest", "Belfry", "Turret"]),
 ("The ridged glass lens that throws the beam for miles", "Fresnel lens", ["Magnifying glass", "Contact lens", "Fisheye lens"]),
 ("Sounded in thick fog to warn ships", "Foghorn", ["Klaxon", "Bugle", "Kazoo"]),
 ("The body that runs the lighthouses of England and Wales", "Trinity House", ["Northern Lighthouse Board", "Admiralty", "Lloyd's"]),
 ("The famous lighthouse off Plymouth, rebuilt four times", "Eddystone", ["Bishop Rock", "Longships", "Wolf Rock"]),
 ("The ancient lighthouse of Alexandria, a Wonder of the World", "Pharos", ["Colossus", "Mausoleum", "Ziggurat"]),
 ("The lighthouse off Arbroath, the oldest sea-washed one still standing", "Bell Rock", ["Skerryvore", "Muckle Flugga", "Ardnamurchan"]),
 ("The red-and-white lighthouse at Marsden, near South Shields", "Souter", ["Roker", "Whitby", "Hartlepool"]),
 ("The lighthouse on a tidal island at Whitley Bay", "St Mary's", ["Coquet", "Holy Island", "Tynemouth"]),
 ("The Farne Islands lighthouse where Grace Darling lived", "Longstone", ["Coquet", "Inner Farne", "Bamburgh"]),
 ("A ship carrying a light, moored where no lighthouse can be built", "Lightship", ["Tugboat", "Hulk", "Pilot boat"]),
 ("A painted tower or pattern that guides ships by day", "Daymark", ["Landmark", "Waymark", "Benchmark"]),
 ("What ended the keepers' jobs: the last left in 1998", "Automation", ["Privatisation", "Electrification", "Decommissioning"]),
 ("The balcony that runs round the top", "Gallery", ["Veranda", "Parapet", "Mezzanine"]),
 ("Each light's own pattern of flashes", "Characteristic", ["Signature", "Morse code", "Call sign"]),
 ("The old Eddystone lighthouse, rebuilt on Plymouth Hoe", "Smeaton's Tower", ["Nelson's Column", "Cleopatra's Needle", "Drake's Tower"]),
 ("The Scottish family who built most of Scotland's lighthouses", "Stevenson", ["Telford", "Brunel", "Stephenson"]),
 ("The shaft of light swept across the sea", "Beam", ["Glow", "Glare", "Spark"]),
 ("People said to lure ships onto the rocks with false lights", "Wreckers", ["Pirates", "Smugglers", "Privateers"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-222.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
