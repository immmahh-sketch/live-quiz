# Bank session 10 Oct 2026: 2 more general races -> bank/race-135.json (hotel words, flying words). 20 rows each, target 10; wrong options are
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


race("what's this hotel word?", "Travel", "easy", ["hotels", "holidays", "words"], [
 ("The desk that books your theatre tickets, taxis and restaurant tables", "Concierge", ["Sommelier", "Maître d'", "Doorman"]),
 ("Carries your luggage up to your room", "Porter", ["Doorman", "Sommelier", "Maître d'"]),
 ("The team that cleans the rooms and changes the beds", "Housekeeping", ["Front of house", "Night audit", "Reservations"]),
 ("An evening service when your bed is folded back and a chocolate left on the pillow", "Turndown", ["Room only", "Day let", "Walk-in"]),
 ("A little fridge of pricey drinks and snacks in your room", "Minibar", ["Buffet", "À la carte", "Corkage"]),
 ("A grand room with a separate living area, often the best in the hotel", "Suite", ["Studio", "Annexe", "Family room"]),
 ("A room with two single beds", "Twin room", ["Family room", "Studio", "Annexe"]),
 ("Food brought up to your room", "Room service", ["Buffet", "À la carte", "Table d'hôte"]),
 ("Asking to keep your room past the usual leaving time", "Late checkout", ["Early check-in", "Day let", "Walk-in"]),
 ("The entrance hall with the reception desk", "Lobby", ["Mezzanine", "Annexe", "Penthouse"]),
 ("The sign you hang on the handle to keep the cleaners out", "Do Not Disturb", ["Walk-in", "No-show", "Room only"]),
 ("Breakfast and an evening meal included, but not lunch", "Half board", ["Room only", "Self-catering", "Table d'hôte"]),
 ("Breakfast, lunch and dinner all included", "Full board", ["Room only", "Self-catering", "Table d'hôte"]),
 ("Every meal, snack and drink included in the price", "All-inclusive", ["Room only", "Self-catering", "Table d'hôte"]),
 ("A room for the night and a morning meal, often in a small guest house", "Bed and breakfast", ["Room only", "Self-catering", "Day let"]),
 ("A light morning spread of pastries, bread, jam and coffee", "Continental breakfast", ["Table d'hôte", "À la carte", "Corkage"]),
 ("Someone takes your car keys and parks it for you", "Valet parking", ["Doorman", "Day let", "Walk-in"]),
 ("The plastic card that unlocks your door", "Key card", ["Room only", "Walk-in", "Corkage"]),
 ("Being moved to a better room at no extra cost", "Upgrade", ["Overbooking", "No-show", "Corkage"]),
 ("The full, undiscounted price of a room", "Rack rate", ["Corkage", "Cover charge", "No-show"])])

race("what's this flying word?", "Travel", "medium", ["flying", "planes", "airports"], [
 ("Where the pilots sit at the very front of the plane", "Cockpit", ["Nacelle", "Empennage", "Winglet"]),
 ("The main tube-shaped body of the plane", "Fuselage", ["Nacelle", "Empennage", "Winglet"]),
 ("Hinged flaps near the wing tips that make the plane roll", "Aileron", ["Slat", "Winglet", "Pitot tube"]),
 ("The upright flap on the tail that swings the nose left and right", "Rudder", ["Slat", "Winglet", "Spoiler"]),
 ("The wheels and legs a plane lands on", "Undercarriage", ["Nacelle", "Pitot tube", "Slat"]),
 ("The tough recorder that investigators search for after a crash", "Black box", ["Transponder", "Pitot tube", "Yoke"]),
 ("The aircraft's little kitchen", "Galley", ["Nacelle", "Airside", "Manifest"]),
 ("The long strip where planes take off and land", "Runway", ["Taxiway", "Apron", "Control tower"]),
 ("The huge shed where planes are kept and repaired", "Hangar", ["Apron", "Taxiway", "Control tower"]),
 ("Bumpy air that shakes the plane about", "Turbulence", ["Headwind", "Tailwind", "Contrail"]),
 ("The system that flies the plane by itself for long stretches", "Autopilot", ["Transponder", "Yoke", "Squawk"]),
 ("The distress call a pilot makes in a real emergency", "Mayday", ["Pan-pan", "Squawk", "Roger"]),
 ("The ticket you show at the gate to get on the plane", "Boarding pass", ["Manifest", "Codeshare", "Air miles"]),
 ("The moving belt where you pick up your suitcase", "Carousel", ["Taxiway", "Apron", "Airside"]),
 ("The shops where you can buy goods without paying certain taxes", "Duty free", ["Landside", "Codeshare", "Standby"]),
 ("A break of a night or more on the way to somewhere further", "Stopover", ["Standby", "Codeshare", "Air miles"]),
 ("An overnight flight that lands early in the morning", "Red-eye", ["Standby", "Codeshare", "Air miles"]),
 ("The covered walkway from the terminal straight to the plane door", "Air bridge", ["Taxiway", "Apron", "Airside"]),
 ("Where your hand luggage goes, above your seat", "Overhead locker", ["Nacelle", "Manifest", "Airside"]),
 ("A fast wind high up that can speed flights from America to Europe", "Jet stream", ["Contrail", "Headwind", "Squawk"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-135.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
