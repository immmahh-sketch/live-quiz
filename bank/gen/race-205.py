# Bank session 12 Oct 2026: 1 more general race -> bank/race-205.json (shipbuilding words). Checked against the navy, sailing,
# pirate, lifeboat and boat races so no row repeats theirs.
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

race("what's this shipbuilding word?", "The North East of England", "medium", ["shipbuilding", "Tyne", "Wear", "North East", "words"], [
 ("The skilled tradesman who builds ships", "Shipwright", ["Wheelwright", "Cartwright", "Millwright"]),
 ("Hammered red-hot metal pins to hold the steel plates together", "Riveter", ["Blacksmith", "Farrier", "Glazier"]),
 ("Joins metal together with a hot arc or flame", "Welder", ["Tinsmith", "Brazier", "Cooper"]),
 ("Shaped and fitted the big steel plates of the hull", "Plater", ["Fitter", "Turner", "Moulder"]),
 ("Made the seams between the plates watertight", "Caulker", ["Thatcher", "Tiler", "Roofer"]),
 ("A basin pumped empty so a ship can be worked on out of the water", "Dry dock", ["Wet dock", "Marina", "Quayside"]),
 ("The giant T-shaped crane over a fitting-out berth", "Hammerhead crane", ["Tower crane", "Crawler crane", "Derrick"]),
 ("The siren that sounded the start and end of every shift", "Hooter", ["Klaxon", "Bugle", "Gong"]),
 ("Finishing the ship's insides after she has been launched", "Fitting-out", ["Kitting-up", "Rigging-down", "Topping-off"]),
 ("Test voyages before the ship is handed over to her owners", "Sea trials", ["Maiden voyage", "Dress rehearsal", "Test drive"]),
 ("Smashing a bottle on the bow as she's named", "Christening", ["Baptism", "Toasting", "Crowning"]),
 ("A watertight wall dividing up the inside of the ship", "Bulkhead", ["Hatch", "Deckhead", "Gunwale"]),
 ("The detailed plan drawing of the ship", "Blueprint", ["Sketch", "Mock-up", "Doodle"]),
 ("The famous Wallsend shipyard whose cranes stood over the Tyne until 2009", "Swan Hunter", ["Harland and Wolff", "Cammell Laird", "Vickers"]),
 ("The famous shipbuilder and engine maker on the Wear in Sunderland", "Doxford", ["Readhead", "Smith's Dock", "Vosper Thornycroft"]),
 ("The record-breaking Cunard liner launched on the Tyne in 1906", "Mauretania", ["Lusitania", "Aquitania", "Olympic"]),
 ("The mark on the hull showing how low a loaded ship may safely sit", "Plimsoll line", ["Sea line", "Tide mark", "Hemline"]),
 ("A young worker learning the trade over several years", "Apprentice", ["Journeyman", "Foreman", "Gaffer"]),
 ("A tall frame running on rails, carrying loads across the berth", "Gantry", ["Scaffold", "Trestle", "Pulley"]),
 ("The number a shipyard gives every ship it builds", "Yard number", ["Berth number", "Pennant number", "Call sign"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-205.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
