# Bank session 11 Oct 2026: 3 more general races -> bank/race-184.json (car mechanic, tenpin bowling and Valentine's words). 20 rows each, target 10; wrong options are
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

race("what's this car mechanic's word?", "Science", "medium", ["cars", "garages", "words"], [
 ("The pedal you press to change gear in a manual", "Clutch", ["Throttle", "Choke", "Handbrake"]),
 ("The hinged cover over the engine", "Bonnet", ["Sunroof", "Tailgate", "Sill"]),
 ("The luggage space at the back", "Boot", ["Glovebox", "Footwell", "Sunroof"]),
 ("The yearly roadworthiness test once a car is three years old", "MOT", ["DVLA", "AA", "RAC"]),
 ("Spark to light the fuel in each cylinder", "Spark plugs", ["Fuses", "Valves", "Bulbs"]),
 ("Moves up and down inside a cylinder", "Piston", ["Camshaft", "Flywheel", "Driveshaft"]),
 ("Keeps the engine cool, behind the front grille", "Radiator", ["Condenser", "Carburettor", "Sump"]),
 ("Charges the battery while the engine runs", "Alternator", ["Starter motor", "Distributor", "Regulator"]),
 ("Added to the coolant so it doesn't freeze", "Antifreeze", ["De-icer", "Screenwash", "Brake fluid"]),
 ("The grooved pattern on a tyre that grips the road", "Tread", ["Sidewall", "Rim", "Hubcap"]),
 ("The legal minimum tread depth on a car tyre", "1.6 mm", ["1 mm", "2.5 mm", "3 mm"]),
 ("The pipe carrying fumes out of the back", "Exhaust", ["Fuel line", "Axle", "Driveshaft"]),
 ("The stick you pull out to check the oil", "Dipstick", ["Gearstick", "Joystick", "Yardstick"]),
 ("Lifts one corner of the car to change a wheel", "Jack", ["Winch", "Crane", "Hoist"]),
 ("Springs and shock absorbers soaking up the bumps", "Suspension", ["Ignition", "Steering", "Transmission"]),
 ("Starting a flat battery with leads from another car", "Jump start", ["Kick start", "Head start", "False start"]),
 ("The belt that drives the valves, costly if it snaps", "Timing belt", ["Fan belt", "Seat belt", "Conveyor belt"]),
 ("Adjusting the wheels' angles to stop uneven tyre wear", "Tracking", ["Tuning", "Bleeding", "Topping up"]),
 ("A thorough clean of the car inside and out", "Valet", ["Service", "Respray", "Tune-up"]),
 ("The mirror on the side of the car", "Wing mirror", ["Rear-view mirror", "Vanity mirror", "Mirror ball"])])

race("what's this tenpin bowling word?", "Sport", "medium", ["tenpin bowling", "bowling", "words"], [
 ("All ten pins down with your first ball", "Strike", ["Hit", "Slam", "Smash"]),
 ("All ten pins down using both balls", "Spare", ["Extra", "Bonus", "Second"]),
 ("Three strikes in a row", "Turkey", ["Chicken", "Goose", "Hat-trick"]),
 ("Two strikes in a row", "Double", ["Brace", "Pair", "Twin"]),
 ("A ball that drops into the channel at the side", "Gutter ball", ["Dead ball", "Wide", "No-ball"]),
 ("A perfect game's score", "300", ["100", "200", "500"]),
 ("Each of the ten turns in a game", "Frame", ["Round", "End", "Over"]),
 ("A turn with no strike or spare", "Open frame", ["Empty frame", "Dead frame", "Blank"]),
 ("The line you mustn't step over when you bowl", "Foul line", ["Oche", "Crease", "Baseline"]),
 ("The run-up area before that line", "Approach", ["Slipway", "Runway", "Apron"]),
 ("Pins left standing far apart after the first ball", "Split", ["Spread", "Fork", "Gap"]),
 ("The pin at the very front", "Headpin", ["Kingpin", "Toppin", "Leadpin"]),
 ("The gap between the front pin and the next, where strikes come from", "Pocket", ["Slot", "Notch", "Groove"]),
 ("A ball that curves into the pins", "Hook", ["Slice", "Swerve", "Bender"]),
 ("The machine that resets the pins", "Pinsetter", ["Pinball", "Pin cushion", "Pin-up"]),
 ("Barriers raised in the gutters for children", "Bumpers", ["Buffers", "Cushions", "Kerbs"]),
 ("The polished wooden strip you bowl along", "Lane", ["Rink", "Pitch", "Green"]),
 ("The shape the pins are set out in", "Triangle", ["Diamond", "Square", "Circle"]),
 ("Pins in the back row", "4", ["3", "5", "6"]),
 ("What the balls' weights are marked in", "Pounds", ["Kilograms", "Stones", "Ounces"])])

race("what's this Valentine's word?", "Lifestyle", "easy", ["Valentine's Day", "love", "words"], [
 ("Someone who sends a card without signing it", "Secret admirer", ["Pen pal", "Wingman", "Matchmaker"]),
 ("The winged boy with a bow and arrow", "Cupid", ["Puck", "Pan", "Mercury"]),
 ("The date of Valentine's Day", "14 February", ["14 March", "1 February", "29 February"]),
 ("The Greek god of love", "Eros", ["Ares", "Hermes", "Apollo"]),
 ("The classic Valentine's flower", "Red rose", ["White lily", "Yellow tulip", "Daffodil"]),
 ("The letter that stands for a kiss on a card", "X", ["O", "H", "Y"]),
 ("Fizzy sweets printed with messages like 'Be Mine'", "Love Hearts", ["Parma Violets", "Refreshers", "Polos"]),
 ("A romantic meal for two by the light of a flame", "Candlelit dinner", ["TV dinner", "Packed lunch", "Afternoon tea"]),
 ("Asking someone to marry you", "Proposal", ["Petition", "Motion", "Overture"]),
 ("The ring that seals a yes", "Engagement ring", ["Eternity ring", "Signet ring", "Nose ring"]),
 ("Getting down on one ...", "Knee", ["Elbow", "Foot", "Hand"]),
 ("The shape of a box of Valentine's chocolates", "Heart", ["Star", "Diamond", "Moon"]),
 ("What SWALK on an envelope stands for", "Sealed with a loving kiss", ["Sent with a little kindness", "Signed with a lucky key", "Sealed with all love, Kate"]),
 ("'Roses are red, violets are ...'", "Blue", ["Green", "Pink", "Purple"]),
 ("What 'je t'aime' means", "I love you", ["I miss you", "Thank you", "Good night"]),
 ("The city of love, with padlocks on its bridges", "Paris", ["Rome", "Vienna", "Prague"]),
 ("Shakespeare's star-crossed lovers", "Romeo and Juliet", ["Antony and Cleopatra", "Beatrice and Benedick", "Oberon and Titania"]),
 ("Meeting lots of singles for a few minutes each", "Speed dating", ["Speed reading", "Hen do", "Ceilidh"]),
 ("Going out with someone you've never met", "Blind date", ["Double date", "Dinner date", "Play date"]),
 ("A bunch of flowers", "Bouquet", ["Corsage", "Garland", "Wreath"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-184.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
