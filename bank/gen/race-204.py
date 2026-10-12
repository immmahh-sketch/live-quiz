# Bank session 12 Oct 2026: 3 more general races -> bank/race-204.json (flying words, shape and maths words, TV and film set words).
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

race("what's this flying word?", "Travel", "medium", ["flying", "aviation", "words"], [
 ("The person who flies the plane", "Pilot", ["Marshal", "Dispatcher", "Loadmaster"]),
 ("Where the pilots sit, right at the front", "Cockpit", ["Hold", "Nacelle", "Wheel well"]),
 ("The long main body of the plane, where the passengers sit", "Fuselage", ["Keel", "Chassis", "Hull"]),
 ("The big shed where planes are kept and repaired", "Hangar", ["Depot", "Terminal", "Silo"]),
 ("The little kitchen where the cabin crew make the drinks", "Galley", ["Pantry", "Buttery", "Scullery"]),
 ("Leaving the runway and climbing into the air", "Take-off", ["Touchdown", "Go-around", "Climb-out"]),
 ("Rolling slowly along the ground to the runway", "Taxiing", ["Gliding", "Hovering", "Stalling"]),
 ("Tilting the wings to make a turn", "Banking", ["Pitching", "Coasting", "Drifting"]),
 ("A sudden bumpy patch of air", "Turbulence", ["Headwind", "Backdraft", "Downforce"]),
 ("The 'black box' that records the flight", "Flight recorder", ["Transponder", "Gyroscope", "Beacon"]),
 ("The dial that shows how high you are", "Altimeter", ["Barometer", "Odometer", "Speedometer"]),
 ("The hinged flap on the tail that steers the nose left and right", "Rudder", ["Aileron", "Elevator", "Spoiler"]),
 ("A stop on the way where you wait to change planes", "Layover", ["Detour", "Shortcut", "Diversion"]),
 ("An aircraft with no pilot on board, flown remotely", "Drone", ["Glider", "Blimp", "Kite"]),
 ("A giant rigid airship like the Hindenburg", "Zeppelin", ["Blimp", "Balloon", "Autogyro"]),
 ("The covered walkway from the gate to the plane door", "Jet bridge", ["Gangplank", "Slipway", "Causeway"]),
 ("The radio distress call, said three times", "Mayday", ["Pan-pan", "Roger", "Wilco"]),
 ("The senior cabin crew member in charge of the cabin", "Purser", ["Bosun", "Quartermaster", "Bursar"]),
 ("The tall airport building where controllers guide the planes", "Control tower", ["Terminal", "Concourse", "Lighthouse"]),
 ("The patch of tarmac where planes park to load up", "Apron", ["Runway", "Forecourt", "Verge"])])

race("what's this shape or maths word?", "Science", "easy", ["maths", "shapes", "geometry", "words"], [
 ("A flat shape with three straight sides", "Triangle", ["Square", "Kite", "Oblong"]),
 ("Six sides, like a cell in a honeycomb", "Hexagon", ["Heptagon", "Decagon", "Nonagon"]),
 ("Eight sides, like a stop sign", "Octagon", ["Heptagon", "Decagon", "Dodecagon"]),
 ("Five sides, like the US military headquarters", "Pentagon", ["Heptagon", "Nonagon", "Dodecagon"]),
 ("From the centre of a circle out to its edge", "Radius", ["Chord", "Arc", "Tangent"]),
 ("Straight across a circle, through the middle", "Diameter", ["Arc", "Sector", "Tangent"]),
 ("The distance all the way round a circle", "Circumference", ["Area", "Arc", "Segment"]),
 ("An angle of exactly 90 degrees", "Right angle", ["Acute angle", "Reflex angle", "Straight angle"]),
 ("Lines that run side by side and never meet", "Parallel", ["Diagonal", "Tangent", "Axis"]),
 ("Four equal sides, like the diamond on a playing card", "Rhombus", ["Kite", "Oblong", "Parallelogram"]),
 ("Four sides with just one pair of parallel sides", "Trapezium", ["Parallelogram", "Kite", "Oblong"]),
 ("A perfectly round 3D ball", "Sphere", ["Ellipse", "Oval", "Torus"]),
 ("Six square faces, like a dice", "Cube", ["Prism", "Tetrahedron", "Octahedron"]),
 ("A square base with four sides meeting at a point", "Pyramid", ["Prism", "Tetrahedron", "Octahedron"]),
 ("The shape of a tin of beans", "Cylinder", ["Prism", "Cuboid", "Torus"]),
 ("The shape of an ice-cream cornet", "Cone", ["Prism", "Crescent", "Tetrahedron"]),
 ("A triangle with exactly two equal sides", "Isosceles", ["Scalene", "Acute", "Reflex"]),
 ("A triangle with all three sides equal", "Equilateral", ["Scalene", "Quadrilateral", "Oblique"]),
 ("The longest side of a right-angled triangle", "Hypotenuse", ["Tangent", "Diagonal", "Vertex"]),
 ("An angle between 90 and 180 degrees", "Obtuse", ["Acute", "Reflex", "Oblique"])])

race("what's this TV and film set word?", "TV", "medium", ["TV", "film", "words"], [
 ("The screen that shows the presenter their script", "Autocue", ["Viewfinder", "Cue light", "Monitor"]),
 ("Words along the bottom of the screen for people who can't hear", "Subtitles", ["Ticker", "Watermark", "Teaser"]),
 ("A short advert for a programme that's coming soon", "Trailer", ["Jingle", "Bumper", "Sting"]),
 ("The channel's short logo clip between programmes", "Ident", ["Jingle", "Watermark", "Ticker"]),
 ("A mistake that ends up on a funny outtakes show", "Blooper", ["Montage", "Cutaway", "Freeze-frame"]),
 ("A brief appearance by a famous face", "Cameo", ["Lead role", "Understudy", "Stunt double"]),
 ("The first test episode of a new series", "Pilot", ["Season", "Box set", "Reboot"]),
 ("The very last episode of a series", "Finale", ["Reboot", "Prequel", "Remake"]),
 ("A new show built around a character from another show", "Spin-off", ["Reboot", "Prequel", "Remake"]),
 ("Making the words up on the spot instead of using the script", "Ad-lib", ["Recap", "Monologue", "Cue card"]),
 ("Giving away a plot twist before someone's seen it", "Spoiler", ["Teaser", "Recap", "Cliffhanger"]),
 ("A narrator's voice heard but not seen", "Voice-over", ["Playback", "Echo", "Soundtrack"]),
 ("Replacing the actors' voices in another language", "Dubbing", ["Playback", "Remake", "Remix"]),
 ("Miming along to a recorded song", "Lip-sync", ["Karaoke", "Busking", "Encore"]),
 ("The striped board snapped shut at the start of every take", "Clapperboard", ["Viewfinder", "Dolly", "Boom"]),
 ("The chief electrician on a film or TV set", "Gaffer", ["Grip", "Best boy", "Dolly operator"]),
 ("The junior who fetches and carries on set", "Runner", ["Grip", "Best boy", "Producer"]),
 ("A background actor with no lines", "Extra", ["Understudy", "Stand-in", "Stunt double"]),
 ("Drawings of every shot in order, like a comic strip", "Storyboard", ["Viewfinder", "Script", "Shot list"]),
 ("The raw, unedited footage from a day's filming", "Rushes", ["Cutaways", "Montage", "Trailers"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-204.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
