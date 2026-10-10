# Bank session 10 Oct 2026: 2 more general races -> bank/race-128.json (gym exercises, gardening words). 20 rows each, target 10; wrong options are
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


race("which exercise is this?", "Sport", "medium", ["fitness", "gym", "exercise"], [
 ("Squat, kick back to a press-up, jump your feet in and leap up", "Burpee", ["Thruster", "Bear crawl", "Inchworm"]),
 ("Bend your knees and lower your bottom as if sitting on a chair, then stand", "Squat", ["Good morning", "Hollow hold", "Inchworm"]),
 ("Step one leg forward and drop the back knee towards the floor", "Lunge", ["Skater jump", "High knees", "Good morning"]),
 ("Hold your body straight and rigid, resting on your forearms and toes", "Plank", ["Hollow hold", "Superman", "Bear crawl"]),
 ("Lie face down and push your body up and down with your arms", "Press-up", ["Superman", "Inchworm", "Lat pulldown"]),
 ("Lie on your back and raise your whole upper body up to your knees", "Sit-up", ["Flutter kicks", "Hollow hold", "Superman"]),
 ("Jump while spreading your arms and legs wide, then bring them back together", "Star jump", ["High knees", "Skater jump", "Tuck jump"]),
 ("Hang from a bar and haul your chin up over it", "Pull-up", ["Lat pulldown", "Farmer's walk", "Inchworm"]),
 ("Lift a loaded barbell from the floor until you're standing up straight", "Deadlift", ["Snatch", "Clean and jerk", "Good morning"]),
 ("Lie on a bench and push a barbell up from your chest", "Bench press", ["Lat pulldown", "Leg press", "Thruster"]),
 ("Lie on your back and curl just your shoulders off the floor", "Crunch", ["Flutter kicks", "Superman", "Hollow hold"]),
 ("From a press-up position, drive your knees towards your chest one after the other, fast", "Mountain climber", ["High knees", "Bear crawl", "Inchworm"]),
 ("Bend your elbow to lift a dumbbell up towards your shoulder", "Bicep curl", ["Lat pulldown", "Shoulder press", "Farmer's walk"]),
 ("Lower and raise yourself on your arms, hands on the edge of a bench behind you", "Tricep dip", ["Shoulder press", "Lat pulldown", "Superman"]),
 ("Leap from the floor up onto a raised platform", "Box jump", ["Tuck jump", "Skater jump", "Step-up"]),
 ("Lean your back against a wall with your knees bent at right angles, and hold", "Wall sit", ["Hollow hold", "Superman", "Good morning"]),
 ("Sit leaning back with your feet up and turn from side to side, often holding a weight", "Russian twist", ["Flutter kicks", "Hollow hold", "Woodchop"]),
 ("Swing a handled iron ball from between your legs up to chest height", "Kettlebell swing", ["Turkish get-up", "Farmer's walk", "Thruster"]),
 ("Lie on your back with knees bent and push your hips up towards the ceiling", "Glute bridge", ["Superman", "Hollow hold", "Flutter kicks"]),
 ("Rise up onto your tiptoes, then lower back down", "Calf raise", ["Good morning", "Step-up", "High knees"])])

race("what's this gardening word?", "Nature and the environment", "medium", ["gardening", "plants", "words"], [
 ("Rotted-down kitchen and garden waste, dug back in to feed the soil", "Compost", ["Tilth", "Loam", "Bedding"]),
 ("A layer of bark or straw spread on the soil to keep weeds down and moisture in", "Mulch", ["Tilth", "Loam", "Riddle"]),
 ("Snipping off faded flowers so the plant blooms again", "Deadheading", ["Bolting", "Layering", "Scarifying"]),
 ("Cutting back branches to shape a plant or keep it healthy", "Pruning", ["Layering", "Scarifying", "Aerating"]),
 ("A plant that comes back year after year", "Perennial", ["Biennial", "Bedding", "Standard"]),
 ("A plant that grows, flowers, seeds and dies all within one year", "Annual", ["Biennial", "Standard", "Cordon"]),
 ("Hedges and shrubs clipped into shapes like birds or balls", "Topiary", ["Parterre", "Potager", "Arbour"]),
 ("A fruit tree trained flat against a wall with its branches in tiers", "Espalier", ["Standard", "Obelisk", "Pergola"]),
 ("A glass or plastic cover put over young plants to protect them", "Cloche", ["Water butt", "Trug", "Obelisk"]),
 ("A wooden lattice fixed to a wall or fence for climbers to grow up", "Trellis", ["Obelisk", "Arbour", "Gazebo"]),
 ("A pointed stick for poking holes to plant seeds or seedlings", "Dibber", ["Widger", "Riddle", "Trug"]),
 ("A long-handled blade pushed through the topsoil to slice off weeds", "Hoe", ["Rake", "Fork", "Widger"]),
 ("Strong one-handed clippers for snipping stems and twigs", "Secateurs", ["Trug", "Widger", "Riddle"]),
 ("A mound of stones planted with alpine plants", "Rockery", ["Parterre", "Potager", "Sunken garden"]),
 ("A rented plot of council land for growing your own vegetables", "Allotment", ["Potager", "Parterre", "Orangery"]),
 ("A low box with a glass lid where young plants toughen up", "Cold frame", ["Orangery", "Water butt", "Gazebo"]),
 ("Slowly getting indoor-raised plants used to life outdoors", "Hardening off", ["Bolting", "Damping off", "Layering"]),
 ("Moving tiny seedlings from a tray into pots of their own", "Pricking out", ["Layering", "Double digging", "Scarifying"]),
 ("A wall sunk in a ditch that keeps livestock out without spoiling the view", "Ha-ha", ["Folly", "Parterre", "Arbour"]),
 ("Joining a piece of one plant onto the roots of another", "Grafting", ["Layering", "Bolting", "Pollarding"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-128.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
