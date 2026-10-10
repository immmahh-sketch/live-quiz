# Bank session 10 Oct 2026: 2 more general races -> bank/race-121.json (kinds of boat, kinds of building). 20 rows each, target 10; wrong options are
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

race("what kind of boat is this?", "General knowledge", "medium", ["boats", "ships"], [
 ("A black Venetian boat rowed by a standing oarsman", "Gondola", ["Felucca", "Skiff", "Wherry"]),
 ("A Chinese sailing ship with ribbed, fan-like sails", "Junk", ["Felucca", "Schooner", "Ketch"]),
 ("An Arab sailing boat with a triangular sail", "Dhow", ["Felucca", "Schooner", "Sloop"]),
 ("A round Welsh boat of wicker and animal hide", "Coracle", ["Kayak", "Skiff", "Raft"]),
 ("A flat boat pushed with a pole along the Cam", "Punt", ["Skiff", "Wherry", "Raft"]),
 ("A long, thin canal boat, about seven feet wide", "Narrowboat", ["Barge", "Wherry", "Lighter"]),
 ("A sailing boat with two hulls side by side", "Catamaran", ["Outrigger", "Ketch", "Schooner"]),
 ("A boat with three hulls side by side", "Trimaran", ["Outrigger", "Ketch", "Sloop"]),
 ("Rides on a cushion of air over land and sea", "Hovercraft", ["Hydrofoil", "Jet ski", "Airboat"]),
 ("A big Spanish treasure ship of the 1500s", "Galleon", ["Frigate", "Man-of-war", "Carrack"]),
 ("An ancient Greek warship with three rows of oars", "Trireme", ["Bireme", "Galley", "Carrack"]),
 ("A Viking raiding ship with a dragon on the prow", "Longship", ["Knarr", "Galley", "Carrack"]),
 ("A fast sailing ship of the tea trade, like the Cutty Sark", "Clipper", ["Schooner", "Frigate", "Carrack"]),
 ("A small, powerful boat that pushes and pulls big ships into port", "Tugboat", ["Tender", "Launch", "Lighter"]),
 ("A warship that travels under the water", "Submarine", ["Hydrofoil", "Destroyer", "Frigate"]),
 ("A small open sailing boat, often a beginner's first", "Dinghy", ["Skiff", "Sloop", "Ketch"]),
 ("A pedal-powered boat for hire at the seaside", "Pedalo", ["Skiff", "Raft", "Jet ski"]),
 ("A flat-bottomed wooden boat seen in East Asian harbours", "Sampan", ["Felucca", "Skiff", "Wherry"]),
 ("A ship built to smash a path through frozen seas", "Icebreaker", ["Destroyer", "Dreadnought", "Frigate"]),
 ("A fishing boat that drags a big net behind it", "Trawler", ["Coble", "Lugger", "Smack"])])

race("what kind of building is this?", "General knowledge", "medium", ["buildings", "architecture"], [
 ("A dome built from blocks of snow", "Igloo", ["Hogan", "Chalet", "Rotunda"]),
 ("The round felt tent of Mongolian nomads", "Yurt", ["Hogan", "Chalet", "Pavilion"]),
 ("The cone-shaped tent of the Plains peoples", "Tepee", ["Hogan", "Pavilion", "Kiosk"]),
 ("A tiered tower with upturned eaves at an Asian temple", "Pagoda", ["Rotunda", "Belvedere", "Obelisk"]),
 ("A slender tower from which the call to prayer is made", "Minaret", ["Spire", "Belfry", "Steeple"]),
 ("A tower with a bright light to warn ships", "Lighthouse", ["Belvedere", "Obelisk", "Turret"]),
 ("A Kentish building with a cowled roof for drying hops", "Oast house", ["Granary", "Silo", "Byre"]),
 ("A fanciful building put up just for show on a country estate", "Folly", ["Belvedere", "Pavilion", "Rotunda"]),
 ("A house all on one floor", "Bungalow", ["Chalet", "Maisonette", "Cottage"]),
 ("A stepped temple tower of ancient Mesopotamia", "Ziggurat", ["Obelisk", "Mausoleum", "Rotunda"]),
 ("A domed Buddhist shrine holding sacred relics", "Stupa", ["Mausoleum", "Rotunda", "Shrine"]),
 ("The church that holds a bishop's throne", "Cathedral", ["Chapel", "Priory", "Basilica"]),
 ("A round coastal fort built to keep Napoleon out", "Martello tower", ["Keep", "Turret", "Belfry"]),
 ("A building for keeping pigeons", "Dovecote", ["Byre", "Granary", "Kiosk"]),
 ("An open-sided garden shelter with a roof", "Gazebo", ["Pavilion", "Kiosk", "Lean-to"]),
 ("A small Scottish farm and its cottage", "Croft", ["Byre", "Manse", "Grange"]),
 ("A row of old stables turned into houses", "Mews", ["Terrace", "Tenement", "Arcade"]),
 ("A basic mountain shelter, free for walkers in Scotland", "Bothy", ["Hut", "Lodge", "Cabin"]),
 ("An open-air public swimming pool", "Lido", ["Rotunda", "Pavilion", "Arcade"]),
 ("An oval open-air arena, like the Colosseum", "Amphitheatre", ["Rotunda", "Colonnade", "Forum"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-121.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
