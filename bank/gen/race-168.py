# Bank session 11 Oct 2026: 3 more general races -> bank/race-168.json (basketball, baseball and plumbing words). 20 rows each, target 10; wrong options are
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

race("what's this basketball word?", "Sport", "medium", ["basketball", "NBA", "words"], [
 ("Leaping up and forcing the ball down through the hoop", "Slam dunk", ["Home run", "Touchdown", "Hat-trick"]),
 ("A gentle shot off the backboard on the run", "Lay-up", ["Drop goal", "Bunt", "Volley"]),
 ("An unopposed shot from the line after a foul", "Free throw", ["Penalty", "Free kick", "Conversion"]),
 ("A shot from beyond the arc", "Three-pointer", ["Drop goal", "Hat-trick", "Six"]),
 ("Bouncing the ball while you move", "Dribble", ["Juggle", "Volley", "Dink"]),
 ("Grabbing the ball after a missed shot", "Rebound", ["Rally", "Deflection", "Scrum"]),
 ("Losing the ball to the other team", "Turnover", ["Overturn", "Turnstile", "Throw-in"]),
 ("The rectangle behind the hoop", "Backboard", ["Scoreboard", "Dartboard", "Skirting board"]),
 ("Taking too many steps without bouncing the ball", "Travelling", ["Offside", "Double hit", "Handball"]),
 ("Gives a team 24 seconds to shoot", "Shot clock", ["Stopwatch", "Egg timer", "Chess clock"]),
 ("America's top basketball league, by its initials", "NBA", ["NFL", "NHL", "MLB"]),
 ("The show team famous for trick shots and 'Sweet Georgia Brown'", "Harlem Globetrotters", ["Chicago Bulls", "LA Lakers", "Boston Celtics"]),
 ("The Chicago Bulls legend with six titles", "Michael Jordan", ["Kobe Bryant", "Magic Johnson", "Shaquille O'Neal"]),
 ("The star who became the NBA's all-time top scorer in 2023", "LeBron James", ["Kobe Bryant", "Magic Johnson", "Stephen Curry"]),
 ("The USA's superstar team at the 1992 Olympics", "Dream Team", ["A-Team", "Famous Five", "Invincibles"]),
 ("The playmaker who runs the attack", "Point guard", ["Centre", "Power forward", "Small forward"]),
 ("A shot that misses everything", "Air ball", ["Airmail", "Air guitar", "Hot air"]),
 ("Players on court for each team", "Five", ["Six", "Seven", "Eleven"]),
 ("Catching a pass in mid-air and dunking it", "Alley-oop", ["Hopscotch", "Hula hoop", "Whoopsie-daisy"]),
 ("Another word for the basket", "Hoop", ["Halo", "Wreath", "Bangle"])])

race("what's this baseball word?", "Sport", "medium", ["baseball", "American sport", "words"], [
 ("Hitting the ball right out of the park", "Home run", ["Touchdown", "Slam dunk", "Hat-trick"]),
 ("Throws the ball to the batter", "Pitcher", ["Bowler", "Server", "Kicker"]),
 ("Crouches behind home plate in a mask", "Catcher", ["Wicketkeeper", "Goalkeeper", "Sweeper"]),
 ("A swing and a miss", "Strike", ["Spare", "Wide", "No-ball"]),
 ("There are nine of these in a game", "Innings", ["Overs", "Quarters", "Halves"]),
 ("The infield, named after its shape", "Diamond", ["Pitch", "Oval", "Square"]),
 ("There are four of these, including home plate", "Bases", ["Wickets", "Posts", "Holes"]),
 ("The big padded glove", "Mitt", ["Gauntlet", "Muff", "Oven glove"]),
 ("Tapping the ball softly instead of swinging", "Bunt", ["Nudge", "Chip", "Dink"]),
 ("A home run with all the bases loaded", "Grand slam", ["Grand National", "Grand Prix", "Grand Tour"]),
 ("Baseball's championship, despite being all-American", "World Series", ["Super Bowl", "Stanley Cup", "NBA Finals"]),
 ("The legendary Yankees slugger, 'the Bambino'", "Babe Ruth", ["Joe DiMaggio", "Lou Gehrig", "Ty Cobb"]),
 ("The most successful team, from the Bronx", "New York Yankees", ["Boston Red Sox", "Los Angeles Dodgers", "Chicago Cubs"]),
 ("When fans stand and sing 'Take Me Out to the Ball Game'", "Seventh-inning stretch", ["Half-time show", "Tea interval", "Mexican wave"]),
 ("The sunken shelter where the team sits", "Dugout", ["Pavilion", "Paddock", "Pit lane"]),
 ("Where the relief pitchers warm up", "Bullpen", ["Pigpen", "Playpen", "Bullring"]),
 ("The British school game it's related to", "Rounders", ["Hockey", "Netball", "Quoits"]),
 ("Three strikes and you're out", "Strikeout", ["Knockout", "Stumped", "Run out"]),
 ("The quickest pitch", "Fastball", ["Googly", "Yorker", "Bouncer"]),
 ("A pitch that swerves on its way", "Curveball", ["Googly", "Inswinger", "Topspin"])])

race("what's this plumbing word?", "Everyday life", "medium", ["plumbing", "DIY", "words"], [
 ("The little rubber ring that stops a tap dripping", "Washer", ["Bolt", "Nut", "Rivet"]),
 ("The valve that turns off water to the whole house", "Stopcock", ["Weathercock", "Peacock", "Shuttlecock"]),
 ("The float valve that refills the toilet cistern", "Ballcock", ["Weathercock", "Peacock", "Shuttlecock"]),
 ("The curved pipe under the sink that traps smells", "U-bend", ["Hairpin bend", "Elbow", "Dog leg"]),
 ("The tank above the toilet", "Cistern", ["Cauldron", "Urn", "Vat"]),
 ("A rubber cup on a stick for unblocking", "Plunger", ["Plunge pool", "Plonker", "Prodder"]),
 ("Heats the water for the radiators", "Boiler", ["Kettle", "Toaster", "Freezer"]),
 ("The hot metal panel that warms the room", "Radiator", ["Refrigerator", "Generator", "Ventilator"]),
 ("Letting trapped air out of a radiator", "Bleed", ["Pump", "Prime", "Prune"]),
 ("Water dripping where it shouldn't", "Leak", ["Leek", "Lick", "Leap"]),
 ("Where the dirty water goes", "Drain", ["Chimney", "Flue", "Vent"]),
 ("The channel along the roof edge that catches the rain", "Gutter", ["Soffit", "Fascia", "Ridge"]),
 ("Carries the rain from the gutter to the ground", "Downpipe", ["Flue", "Chimney", "Vent"]),
 ("The chalky crust left by hard water", "Limescale", ["Plaque", "Rust", "Mould"]),
 ("The tool for tightening nuts", "Spanner", ["Trowel", "Chisel", "Plane"]),
 ("White tape wound round threads to seal a joint", "PTFE tape", ["Duct tape", "Masking tape", "Red tape"]),
 ("The electric element inside a hot-water tank", "Immersion heater", ["Fan heater", "Storage heater", "Patio heater"]),
 ("An underground tank for sewage where there's no mains drain", "Septic tank", ["Think tank", "Fish tank", "Petrol tank"]),
 ("A gadget that takes the calcium out of hard water", "Water softener", ["Fabric softener", "Water pistol", "Watermark"]),
 ("The trade named from the Latin for lead, which old pipes were made of", "Plumber", ["Fitter", "Joiner", "Glazier"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-168.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
