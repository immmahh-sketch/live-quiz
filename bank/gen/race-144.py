# Bank session 10 Oct 2026: 3 more general races -> bank/race-144.json (camping words, ballet words, office words). 20 rows each, target 10; wrong options are
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

race("what's this camping word?", "Everyday life", "easy", ["camping", "outdoors", "words"], [
 ("Cords pegged out to hold a tent taut", "Guy rope", ["Carabiner", "Gaiters", "Pannier"]),
 ("Hammered into the ground to pin the tent down", "Tent peg", ["Carabiner", "Crampon", "Ice axe"]),
 ("The waterproof layer under the tent floor", "Groundsheet", ["Gaiters", "Awning", "Canopy"]),
 ("A zipped-up padded bed you crawl inside", "Sleeping bag", ["Rucksack", "Bum bag", "Pannier"]),
 ("A metal pot hung over the fire to boil water", "Billy can", ["Lantern", "Compass", "Whistle"]),
 ("Small dry twigs to get the fire going", "Kindling", ["Charcoal", "Compass", "Gaiters"]),
 ("A tiny waterproof shelter just big enough for one sleeper", "Bivvy", ["Gazebo", "Awning", "Canopy"]),
 ("Camping in luxury, with real beds and fairy lights", "Glamping", ["Wild camping", "Backpacking", "Caravanning"]),
 ("A swinging bed slung between two trees", "Hammock", ["Gazebo", "Awning", "Pannier"]),
 ("A light strapped to your forehead", "Head torch", ["Lantern", "Compass", "Whistle"]),
 ("The outer waterproof skin of a tent", "Flysheet", ["Awning", "Canopy", "Gaiters"]),
 ("Striped fabric on poles, staked into the sand on a breezy beach", "Windbreak", ["Gazebo", "Awning", "Canopy"]),
 ("Keeps the drinks and sandwiches cold", "Cool box", ["Pannier", "Rucksack", "Bum bag"]),
 ("A folding frame bed that keeps you off the ground", "Camp bed", ["Gazebo", "Pannier", "Canopy"]),
 ("Springs into shape the moment it's out of the bag", "Pop-up tent", ["Gazebo", "Awning", "Canopy"]),
 ("Where you toast marshmallows after dark", "Campfire", ["Lantern", "Compass", "Gazebo"]),
 ("A rubber hammer for knocking in the pegs", "Mallet", ["Crampon", "Ice axe", "Carabiner"]),
 ("A thin foam layer between you and the cold ground", "Roll mat", ["Gaiters", "Pannier", "Canopy"]),
 ("A round canvas tent with a single centre pole, a glamping favourite", "Bell tent", ["Gazebo", "Awning", "Marquee"]),
 ("What you do when you put a tent up", "Pitch", ["Strike", "Rig", "Moor"])])

race("what's this ballet word?", "Theatre", "hard", ["ballet", "dance", "words"], [
 ("Bending the knees with the feet turned out", "Plié", ["Glissade", "Cabriole", "Brisé"]),
 ("Spinning round on one leg", "Pirouette", ["Glissade", "Échappé", "Sissonne"]),
 ("Standing on one leg with the other stretched out straight behind", "Arabesque", ["Développé", "Cabriole", "Coupé"]),
 ("A dance for two, usually the star couple", "Pas de deux", ["Pas de bourrée", "Balancé", "Brisé"]),
 ("The stiff, sticking-out skirt a ballerina wears", "Tutu", ["Leg warmers", "Unitard", "Bodice"]),
 ("Satin shoes with stiffened toes for dancing on the very tips", "Pointe shoes", ["Ghillies", "Jazz shoes", "Character shoes"]),
 ("The handrail dancers hold on to while they warm up", "Barre", ["Ballon", "Brisé", "Coupé"]),
 ("The leading female dancer of a company", "Prima ballerina", ["Soloist", "Coryphée", "Danseur"]),
 ("The ensemble dancers who perform as a group", "Corps de ballet", ["Danseur noble", "Soloist", "Principal"]),
 ("A big leap with the legs flung out front and back, like the splits in mid-air", "Grand jeté", ["Cabriole", "Sissonne", "Échappé"]),
 ("A jump where the feet beat together quickly in the air", "Entrechat", ["Échappé", "Glissade", "Balancé"]),
 ("A turn where the working leg whips out, done 32 times in 'Swan Lake'", "Fouetté", ["Glissade", "Échappé", "Balancé"]),
 ("Rising up onto the balls of the feet or the tips of the toes", "Relevé", ["Glissade", "Ballon", "Coupé"]),
 ("The person who creates the dance steps", "Choreographer", ["Répétiteur", "Accompanist", "Dresser"]),
 ("Graceful carriage and movement of the arms", "Port de bras", ["Rond de jambe", "Battement", "Frappé"]),
 ("A gliding step where one foot 'chases' the other", "Chassé", ["Battement", "Frappé", "Brisé"]),
 ("Stretching the foot along the floor until only the toe touches", "Tendu", ["Frappé", "Rond de jambe", "Coupé"]),
 ("The 'step of the cat': a sideways jump with both knees drawn up", "Pas de chat", ["Pas de bourrée", "Balancé", "Brisé"]),
 ("A stretchy one-piece worn for practice, named after a French acrobat", "Leotard", ["Leg warmers", "Bodice", "Tabard"]),
 ("Fixing your eyes on one point so you don't get dizzy while turning", "Spotting", ["Ballon", "Balancé", "Coupé"])])

race("what's this office word?", "Everyday life", "easy", ["office", "work", "words"], [
 ("Joins sheets of paper with a little metal clip it punches through", "Stapler", ["Laminator", "Guillotine", "Franking machine"]),
 ("Makes two holes so paper fits in a ring binder", "Hole punch", ["Laminator", "Guillotine", "Shredder"]),
 ("Makes copies of a page, and often jams", "Photocopier", ["Laminator", "Shredder", "Franking machine"]),
 ("Metal drawers full of hanging folders", "Filing cabinet", ["Pigeonhole", "Desk tidy", "Flip chart"]),
 ("Where new work lands on your desk", "In-tray", ["Out-tray", "Pigeonhole", "Desk tidy"]),
 ("A small sticky square for a quick reminder", "Post-it note", ["Treasury tag", "Bulldog clip", "Rolodex"]),
 ("A bent loop of wire that holds a few sheets together", "Paper clip", ["Treasury tag", "Rolodex", "Letter opener"]),
 ("Sitting wherever's free instead of having your own place", "Hot desk", ["Pigeonhole", "Desk tidy", "Secondment"]),
 ("Spins round and rolls about on wheels", "Swivel chair", ["Flip chart", "Whiteboard", "Desk tidy"]),
 ("Where office gossip happens over a paper cup", "Water cooler", ["Franking machine", "Shredder", "Laminator"]),
 ("Your yearly review with the boss", "Appraisal", ["Secondment", "Duvet day", "Clock in"]),
 ("The whole team goes off-site for workshops and team-building", "Away day", ["Duvet day", "Casual Friday", "Secondment"]),
 ("The written record of what was said in a meeting", "Minutes", ["Reply all", "Blind copy", "Payslip"]),
 ("The list of what a meeting will cover", "Agenda", ["Reply all", "Blind copy", "Payslip"]),
 ("A short internal note sent round the office", "Memo", ["Payslip", "P45", "Sick note"]),
 ("Rows and columns of numbers on screen, like Excel", "Spreadsheet", ["Rolodex", "Flip chart", "Dictaphone"]),
 ("The cord round your neck that holds your pass", "Lanyard", ["Treasury tag", "Bulldog clip", "Rolodex"]),
 ("Choosing your own start and finish times around core hours", "Flexitime", ["Clock in", "Casual Friday", "Duvet day"]),
 ("Your paid holiday days for the year", "Annual leave", ["Secondment", "Casual Friday", "Clock in"]),
 ("The weeks you must keep working after handing in your resignation", "Notice period", ["Secondment", "Probation", "Casual Friday"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-144.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
