# Bank session 12 Oct 2026: 2 more general races -> bank/race-204.json (shape words, behind-the-scenes words). Rows overlapping the
# existing maths, TV and cinema word races were swapped out.
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

race("what's this shape word?", "Science", "easy", ["maths", "shapes", "geometry", "words"], [
 ("A flat shape with three straight sides", "Triangle", ["Square", "Kite", "Oblong"]),
 ("Six sides, like a cell in a honeycomb", "Hexagon", ["Heptagon", "Decagon", "Nonagon"]),
 ("Eight sides, like a stop sign", "Octagon", ["Heptagon", "Decagon", "Dodecagon"]),
 ("Five sides, like the US military headquarters", "Pentagon", ["Heptagon", "Nonagon", "Dodecagon"]),
 ("Two halves that mirror each other exactly", "Symmetry", ["Rotation", "Translation", "Enlargement"]),
 ("Shapes fitting together with no gaps, like floor tiles", "Tessellation", ["Rotation", "Translation", "Enlargement"]),
 ("Four right angles, with two long sides and two short", "Rectangle", ["Kite", "Parallelogram", "Square"]),
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
 ("The flat sides of a 3D shape, like the six on a cube", "Faces", ["Edges", "Vertices", "Angles"]),
 ("An angle between 90 and 180 degrees", "Obtuse", ["Acute", "Reflex", "Oblique"])])

race("what's this behind-the-scenes word?", "TV", "medium", ["TV", "film", "words"], [
 ("The screen that shows the presenter their script", "Autocue", ["Viewfinder", "Cue light", "Monitor"]),
 ("The crew member holding the long microphone pole over the actors", "Boom operator", ["Grip", "Best boy", "Focus puller"]),
 ("The wheeled trolley the camera glides along on, on tracks", "Dolly", ["Crane", "Steadicam", "Tripod"]),
 ("The channel's short logo clip between programmes", "Ident", ["Jingle", "Watermark", "Ticker"]),
 ("A mistake that ends up on a funny outtakes show", "Blooper", ["Montage", "Cutaway", "Freeze-frame"]),
 ("The plain background swapped for something else in the edit", "Green screen", ["Backdrop", "Blackout", "Spotlight"]),
 ("Making sure nothing changes between shots, like how full a glass is", "Continuity", ["Catering", "Casting", "Costume"]),
 ("The performer who takes the dangerous falls for the star", "Stunt double", ["Stand-in", "Understudy", "Choreographer"]),
 ("'That's a ___!': said when the filming is finished", "Wrap", ["Take", "Cut", "Print"]),
 ("Making the words up on the spot instead of using the script", "Ad-lib", ["Recap", "Monologue", "Cue card"]),
 ("Giving away a plot twist before someone's seen it", "Spoiler", ["Teaser", "Recap", "Cliffhanger"]),
 ("A narrator's voice heard but not seen", "Voice-over", ["Playback", "Echo", "Soundtrack"]),
 ("The director's shout to start the scene", "Action", ["Cut", "Places", "Quiet please"]),
 ("Miming along to a recorded song", "Lip-sync", ["Karaoke", "Busking", "Encore"]),
 ("The striped board snapped shut at the start of every take", "Clapperboard", ["Viewfinder", "Light meter", "Megaphone"]),
 ("The chief electrician on a film or TV set", "Gaffer", ["Grip", "Best boy", "Camera operator"]),
 ("The junior who fetches and carries on set", "Runner", ["Grip", "Best boy", "Producer"]),
 ("A background actor with no lines", "Extra", ["Understudy", "Stand-in", "Leading lady"]),
 ("Drawings of every shot in order, like a comic strip", "Storyboard", ["Viewfinder", "Script", "Shot list"]),
 ("The raw, unedited footage from a day's filming", "Rushes", ["Cutaways", "Montage", "Trailers"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-204.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
