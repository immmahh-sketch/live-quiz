# Bank session 11 Oct 2026: 3 more general races -> bank/race-177.json (bus, strongman and nightclub words). 20 rows each, target 10; wrong options are
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

race("what's this bus word?", "Travel", "easy", ["buses", "transport", "words"], [
 ("A bus with two floors", "Double-decker", ["Minibus", "Charabanc", "Trolleybus"]),
 ("A long bus with a hinge in the middle", "Bendy bus", ["Minibus", "Charabanc", "Trolleybus"]),
 ("The classic red London bus with an open platform at the back", "Routemaster", ["Roadmaster", "Ringmaster", "Roadrunner"]),
 ("Where you wait for the bus", "Bus stop", ["Full stop", "Pit stop", "Backstop"]),
 ("The roof over the stop", "Bus shelter", ["Bomb shelter", "Tax shelter", "Animal shelter"]),
 ("The card that gives free travel to pensioners", "Bus pass", ["Boarding pass", "Backstage pass", "Ski pass"]),
 ("The old job of collecting fares on board", "Conductor", ["Inspector", "Steward", "Porter"]),
 ("What you press to stop the bus", "Bell", ["Horn", "Whistle", "Siren"]),
 ("The list of departure times", "Timetable", ["Times table", "Tide table", "Coffee table"]),
 ("The last stop at the end of the line", "Terminus", ["Junction", "Interchange", "Crossing"]),
 ("A long-distance bus, like National Express", "Coach", ["Tram", "Shuttle", "Rickshaw"]),
 ("A lane only for buses", "Bus lane", ["Memory lane", "Fast lane", "Lovers' lane"]),
 ("London's travel card, named after a shellfish", "Oyster", ["Mussel", "Clam", "Cockle"]),
 ("A stop where the bus only pulls in if you signal", "Request stop", ["Emergency stop", "Last orders", "Rain check"]),
 ("When the buses are packed", "Rush hour", ["Happy hour", "Zero hour", "Witching hour"]),
 ("The Cliff Richard film about a London bus trip across Europe", "Summer Holiday", ["The Italian Job", "Carry On Abroad", "Mamma Mia!"]),
 ("The 1970s sitcom with Reg Varney and 'I 'ate you, Butler!'", "On the Buses", ["Dad's Army", "Porridge", "Rising Damp"]),
 ("The price of a journey", "Fare", ["Toll", "Rent", "Levy"]),
 ("'Please have the ___ ready'", "Exact change", ["Small change", "Climate change", "Sea change"]),
 ("The 1994 film about a bus that mustn't drop below 50 mph", "Speed", ["Crash", "Drive", "Duel"])])

race("what's this strongman word?", "Sport", "medium", ["strongman", "weightlifting", "words"], [
 ("Lifting a bar from the floor to the hips", "Deadlift", ["Curl", "Shrug", "Row"]),
 ("Pushing the bar up while lying on your back", "Bench press", ["Curl", "Shrug", "Row"]),
 ("The Olympic lift: to the shoulders, then overhead", "Clean and jerk", ["Push-up", "Pull-up", "Sit-up"]),
 ("The Olympic lift: floor to overhead in one movement", "Snatch", ["Push-up", "Pull-up", "Sit-up"]),
 ("Huge round stones lifted onto platforms", "Atlas stones", ["Rosetta stones", "Stepping stones", "Curling stones"]),
 ("Carrying heavy weights in each hand along a course", "Farmer's walk", ["Moonwalk", "Catwalk", "Sponsored walk"]),
 ("Dragging a lorry by a rope", "Truck pull", ["Cracker pull", "Tug of love", "Pub crawl"]),
 ("Pressing a giant log overhead", "Log lift", ["Log flume", "Log fire", "Logbook"]),
 ("The TV contest won by Geoff Capes and Eddie Hall", "World's Strongest Man", ["Gladiators", "Superstars", "Ninja Warrior"]),
 ("The Stoke strongman who deadlifted 500 kg in 2016", "Eddie Hall", ["Brian Shaw", "Mark Felix", "Bill Kazmaier"]),
 ("The Icelandic strongman who played The Mountain", "Hafþór Björnsson", ["Magnús Ver Magnússon", "Jón Páll Sigmarsson", "Brian Shaw"]),
 ("The wide belt supporting the lower back", "Weight belt", ["Seat belt", "Black belt", "Green belt"]),
 ("The round weights loaded onto the bar", "Plates", ["Saucers", "Hubcaps", "Coasters"]),
 ("A partner standing by in case you get stuck", "Spotter", ["Trainspotter", "Talent scout", "Lookout"]),
 ("Your heaviest lift ever, in two letters", "PB", ["PE", "PG", "PC"]),
 ("What lifters eat lots of to build muscle", "Protein", ["Sugar", "Fibre", "Salt"]),
 ("The sport of squat, bench press and deadlift", "Powerlifting", ["Paragliding", "Powerboating", "Pole vault"]),
 ("A painful bulge from lifting too much", "Hernia", ["Hiccup", "Cramp", "Rash"]),
 ("The wide-stance deadlift named after Japanese wrestlers", "Sumo", ["Samurai", "Ninja", "Karate"]),
 ("The shot putter who twice won World's Strongest Man and bred budgies", "Geoff Capes", ["Bill Kazmaier", "Jamie Reeves", "Mark Felix"])])

race("what's this nightclub word?", "Entertainment", "easy", ["nightclubs", "nights out", "words"], [
 ("The doorman who decides who gets in", "Bouncer", ["Usher", "Butler", "Steward"]),
 ("Where everyone dances", "Dance floor", ["Shop floor", "Ground floor", "Forest floor"]),
 ("The mirrored ball hanging from the ceiling", "Glitter ball", ["Snowball", "Cannonball", "Meatball"]),
 ("The flashing white light", "Strobe", ["Lava lamp", "Night light", "Torch"]),
 ("Puffs out fog onto the dance floor", "Smoke machine", ["Fruit machine", "Slot machine", "Time machine"]),
 ("The names allowed in free", "Guest list", ["Bucket list", "Shopping list", "Waiting list"]),
 ("Where you hand in your coat", "Cloakroom", ["Boardroom", "Box room", "Green room"]),
 ("The final call at the bar", "Last orders", ["Last rites", "Last Post", "Last Supper"]),
 ("When the lights come up and everyone's sent home", "Chucking-out time", ["Half-time", "Teatime", "Bedtime"]),
 ("The roped-off section for special guests", "VIP area", ["Fire exit", "Smoking area", "Car park"]),
 ("The line outside the door", "Queue", ["Cue", "Crowd", "Herd"]),
 ("Rules like 'no trainers'", "Dress code", ["Morse code", "Highway Code", "Barcode"]),
 ("An ink mark on your wrist to get back in", "Hand stamp", ["Postage stamp", "Stamp duty", "Rubber stamp"]),
 ("A mixed drink with a little umbrella", "Cocktail", ["Ponytail", "Dovetail", "Coat-tail"]),
 ("The famous Manchester club of the rave era", "Haçienda", ["Ministry of Sound", "Cream", "Gatecrasher"]),
 ("The Balearic party island", "Ibiza", ["Majorca", "Crete", "Malta"]),
 ("A new version of a song for the dance floor", "Remix", ["Rehash", "Repeat", "Rerun"]),
 ("What a DJ wears round their neck", "Headphones", ["Earmuffs", "Earplugs", "Hearing aids"]),
 ("The party after the club shuts", "Afters", ["Starters", "Mains", "Desserts"]),
 ("Where you queue for a cab home", "Taxi rank", ["Rank and file", "Bus stop", "Car wash"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-177.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
