# Bank session 10 Oct 2026: 3 more general races -> bank/race-142.json (driving words, restaurant words, hospital words). 20 rows each, target 10; wrong options are
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

race("what's this driving word?", "Cars and motoring", "easy", ["driving", "roads", "words"], [
 ("The routine drilled into learners before every turn", "Mirror, signal, manoeuvre", ["Tailgating", "Undertaking", "Rubbernecking"]),
 ("Turning round in a narrow road using forward and reverse", "Three-point turn", ["Chicane", "Filter lane", "Slip road"]),
 ("Reversing into a gap between two parked cars", "Parallel parking", ["Filter lane", "Slip road", "Undertaking"]),
 ("The examiner slaps the dashboard and you brake hard", "Emergency stop", ["Tailgating", "Rubbernecking", "Undertaking"]),
 ("Moving off on a slope without rolling back", "Hill start", ["Chicane", "Slip road", "Filter lane"]),
 ("The area your mirrors can't show, so you look over your shoulder", "Blind spot", ["Central reservation", "Verge", "Kerb"]),
 ("Red letters on white showing a learner is at the wheel", "L-plates", ["Gantry", "Bollard", "Tax disc"]),
 ("The computer test of multiple-choice questions and clips", "Theory test", ["Tailgating", "MOT", "Undertaking"]),
 ("Clicking when you spot a developing danger in a video clip", "Hazard perception", ["Rubbernecking", "Tailgating", "Undertaking"]),
 ("Yellow criss-cross lines you mustn't stop on", "Box junction", ["Rumble strip", "Chicane", "Clearway"]),
 ("Black and white stripes with flashing orange Belisha beacons", "Zebra crossing", ["Puffin crossing", "Pegasus crossing", "Rumble strip"]),
 ("Lights with a flashing amber phase, when you may go if the crossing is clear", "Pelican crossing", ["Puffin crossing", "Pegasus crossing", "Chicane"]),
 ("A crossing shared by people on foot and people on bikes", "Toucan crossing", ["Puffin crossing", "Pegasus crossing", "Rumble strip"]),
 ("A white painted circle you drive round, not over", "Mini roundabout", ["Bollard", "Chicane", "Gantry"]),
 ("The strip at the edge of the motorway, for breakdowns only", "Hard shoulder", ["Central reservation", "Slip road", "Crawler lane"]),
 ("Traffic moved over to share the other side of the motorway during roadworks", "Contraflow", ["Clearway", "Crawler lane", "Filter lane"]),
 ("Main London roads where red lines mean no stopping at all", "Red route", ["Bus lane", "Crawler lane", "Filter lane"]),
 ("A raised hump in the road that makes you slow down", "Speed bump", ["Chicane", "Rumble strip", "Gantry"]),
 ("Little reflectors set into the middle of the road", "Cat's eyes", ["Bollard", "Gantry", "Rumble strip"]),
 ("A road with a central reservation dividing the two directions", "Dual carriageway", ["Slip road", "Single-track road", "Lay-by"])])

race("what's this restaurant word?", "Food and drink", "medium", ["restaurants", "dining", "words"], [
 ("Choosing each dish separately from the menu, each with its own price", "À la carte", ["Smörgåsbord", "Entrée", "Petit four"]),
 ("A set menu of a few courses at a fixed price", "Table d'hôte", ["Smörgåsbord", "Entrée", "Garnish"]),
 ("A free bite-sized treat from the chef before your starter", "Amuse-bouche", ["Petit four", "Digestif", "Garnish"]),
 ("The wine expert who helps you choose a bottle", "Sommelier", ["Commis chef", "Kitchen porter", "Chef de partie"]),
 ("The head waiter who greets you and shows you to your table", "Maître d'", ["Commis chef", "Kitchen porter", "Chef de partie"]),
 ("A fee for drinking wine you brought in yourself", "Corkage", ["Covers", "Garnish", "Gratuity"]),
 ("An extra percentage added to the bill for the staff", "Service charge", ["Covers", "Garnish", "Petit four"]),
 ("Lots of tiny courses showing off the chef's skills", "Tasting menu", ["Smörgåsbord", "Buffet", "Entrée"]),
 ("The dish of the day", "Plat du jour", ["Petit four", "Digestif", "Entrée"]),
 ("Your leftovers boxed up to take home", "Doggy bag", ["Bento", "Hamper", "Lunchbox"]),
 ("A small, casual French-style restaurant", "Bistro", ["Canteen", "Diner", "Chippy"]),
 ("Roast meat sliced for you at a counter, with all the trimmings", "Carvery", ["Canteen", "Diner", "Smörgåsbord"]),
 ("Waiters serve food onto your plate from a platter with a spoon and fork", "Silver service", ["Buffet", "Smörgåsbord", "Self-service"]),
 ("Small Spanish dishes shared round the table", "Tapas", ["Smörgåsbord", "Meze", "Dim sum"]),
 ("The famous top award for a restaurant, given out by a tyre company", "Michelin star", ["Blue plaque", "Kitemark", "Queen's Award"]),
 ("Booking a table ahead", "Reservation", ["Covers", "Walk-in", "Gratuity"]),
 ("Getting every ingredient chopped and ready before service starts", "Mise en place", ["The pass", "Expo", "Garnish"]),
 ("Everyone who looks after the diners rather than cooking", "Front of house", ["Back of house", "Kitchen porter", "Commis chef"]),
 ("A cheaper deal for eating before a certain time", "Early bird", ["Covers", "Gratuity", "Last orders"]),
 ("The head chef's second in command", "Sous chef", ["Commis chef", "Chef de partie", "Kitchen porter"])])

race("what's this hospital word?", "Science", "easy", ["hospitals", "NHS", "medicine"], [
 ("The department you rush to in an emergency", "A&E", ["Hospice", "Day case", "Pharmacy"]),
 ("Sorting patients by how urgent their case is", "Triage", ["Suture", "Nebuliser", "Locum"]),
 ("Someone seen at the hospital who goes home the same day", "Outpatient", ["Inpatient", "Locum", "Orderly"]),
 ("A room of beds where patients stay", "Ward", ["Hospice", "Pharmacy", "Day case"]),
 ("The unit for the most seriously ill, with one-to-one nursing", "Intensive care", ["Hospice", "Day case", "Pharmacy"]),
 ("Where operations take place", "Theatre", ["Pharmacy", "Hospice", "Day case"]),
 ("Puts you to sleep, or numbs you, for an operation", "Anaesthetic", ["Nebuliser", "Tourniquet", "Suture"]),
 ("The doctor's listening tube for hearing your heart", "Stethoscope", ["Sphygmomanometer", "Thermometer", "Scalpel"]),
 ("A bag of fluid fed slowly into a vein", "Drip", ["Catheter", "Tourniquet", "Nebuliser"]),
 ("A hard shell round a broken bone", "Plaster cast", ["Tourniquet", "Bandage", "Suture"]),
 ("A pair of sticks to help you walk with a broken leg", "Crutches", ["Trolley", "Tourniquet", "Bandage"]),
 ("The picture that shows a broken bone", "X-ray", ["Thermometer", "Nebuliser", "Sphygmomanometer"]),
 ("Lying in a noisy tube while magnets take detailed pictures inside you", "MRI scan", ["Nebuliser", "Sphygmomanometer", "Thermometer"]),
 ("The doctor's note telling the pharmacist what medicine to give you", "Prescription", ["Referral", "Locum", "Suture"]),
 ("Being allowed to go home from hospital", "Discharge", ["Referral", "Locum", "Day case"]),
 ("Used by a patient who can't get out of bed to go to the loo", "Bedpan", ["Nebuliser", "Tourniquet", "Trolley"]),
 ("Crews the ambulance and treats you on the way in", "Paramedic", ["Porter", "Orderly", "Phlebotomist"]),
 ("The senior doctor in charge of your care", "Consultant", ["Porter", "Orderly", "Phlebotomist"]),
 ("The senior nurse who runs the wards", "Matron", ["Porter", "Orderly", "Midwife"]),
 ("Gives an electric shock to restart the heart", "Defibrillator", ["Nebuliser", "Ventilator", "Sphygmomanometer"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-142.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
