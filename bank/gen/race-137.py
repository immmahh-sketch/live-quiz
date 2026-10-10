# Bank session 10 Oct 2026: 2 more general races -> bank/race-137.json (football words, darts and snooker words; none repeat the quickfire races). 20 rows each, target 10; wrong options are
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


race("what's this football word?", "Football", "medium", ["football", "words"], [
 ("Playing the ball through an opponent's legs", "Nutmeg", ["Elastico", "Cruyff turn", "Step-over"]),
 ("An acrobatic overhead kick with your back to goal", "Bicycle kick", ["Scorpion kick", "Toe-poke", "Half-volley"]),
 ("A penalty chipped softly down the middle as the keeper dives", "Panenka", ["Toe-poke", "Half-volley", "Step-over"]),
 ("Kicking the ball with one leg wrapped behind the other", "Rabona", ["Elastico", "Cruyff turn", "Marseille turn"]),
 ("When a goalkeeper and defence let in no goals all match", "Clean sheet", ["Treble", "Double", "Golden Boot"]),
 ("Accidentally scoring for the other side", "Own goal", ["Drop ball", "Goal kick", "Professional foul"]),
 ("A centre-forward who drops deep into midfield", "False nine", ["Regista", "Target man", "Poacher"]),
 ("A defender who roams behind the back line to mop up", "Sweeper", ["Regista", "Wing-back", "Holding midfielder"]),
 ("Barcelona and Spain's style of endless short passing", "Tiki-taka", ["Gegenpress", "Catenaccio", "Long ball"]),
 ("Put every player behind the ball to protect a lead", "Park the bus", ["Gegenpress", "Long ball", "Rondo"]),
 ("Sir Alex Ferguson's furious half-time dressing-down", "Hairdryer treatment", ["Rondo", "Gegenpress", "Booking"]),
 ("Ferguson's name for the nervy end of a title race", "Squeaky bum time", ["Rondo", "Gegenpress", "Super-sub"]),
 ("Dropping down a division after finishing near the bottom", "Relegation", ["Treble", "Double", "Advantage"]),
 ("Knockout matches for the last promotion place", "Play-offs", ["Treble", "Double", "Drop ball"]),
 ("The times of year when clubs may buy and sell players", "Transfer window", ["Drop ball", "Advantage", "Booking"]),
 ("A match between two local rivals", "Derby", ["Treble", "Double", "Drop ball"]),
 ("Falling over on purpose to win a free kick or penalty", "Dive", ["Professional foul", "Booking", "Advantage"]),
 ("Two goals by the same player in one match", "Brace", ["Treble", "Double", "Golden Boot"]),
 ("The old rule where the first goal in extra time won the match", "Golden goal", ["Drop ball", "Advantage", "Super-sub"]),
 ("A badly weighted pass that leaves a team-mate about to get clattered", "Hospital pass", ["Drop ball", "Goal kick", "Throw-in"])])

race("what's this darts or snooker word?", "Sport", "hard", ["darts", "snooker", "words"], [
 ("The double 20 segment at the top of the dartboard", "Double top", ["Ton", "Wire", "Bullseye"]),
 ("Hitting a single, double and treble of the same number with three darts", "Shanghai", ["Robin Hood", "Splash", "Ton-80"]),
 ("Darts slang for scoring 26, once said to be the price of a night's B&B", "Bed and breakfast", ["Ton", "Robin Hood", "Splash"]),
 ("Being left needing double 1, the hardest finish of all", "Madhouse", ["Ton", "Wire", "Bullseye"]),
 ("Scoring more than you need, so your turn doesn't count", "Bust", ["Splash", "Wire", "Robin Hood"]),
 ("One game of 501 in darts", "Leg", ["Set", "Session", "Match"]),
 ("A perfect leg of 501 in the fewest throws possible", "Nine-darter", ["Robin Hood", "Ton-80", "Splash"]),
 ("The final throw that finishes a leg on a double", "Checkout", ["Set", "Ton", "Wire"]),
 ("The little fins at the back of a dart", "Flight", ["Barrel", "Shaft", "Tip"]),
 ("When the cue ball only just touches another ball", "Kiss", ["Stun", "Screw shot", "Jaws"]),
 ("Hitting one red into another so the second one goes in", "Plant", ["Stun", "Screw shot", "Swerve"]),
 ("A ball that goes in by lucky accident", "Fluke", ["Stun", "Clearance", "Century"]),
 ("Playing to leave your opponent nothing easy instead of going for a pot", "Safety shot", ["Clearance", "Century", "Stun"]),
 ("The X-headed stick that props up the cue for long shots", "Rest", ["Extension", "Chalk", "Jaws"]),
 ("The rubber edge round the table that balls bounce off", "Cushion", ["Pocket", "Knuckle", "Jaws"]),
 ("One game of snooker", "Frame", ["Century", "Clearance", "Session"]),
 ("The area behind the line at the top end of the table, where the cue ball starts", "Baulk", ["Knuckle", "Jaws", "Pocket"]),
 ("The very first shot of a frame", "Break-off", ["Clearance", "Century", "Free ball"]),
 ("When the cue ball drops into a pocket after hitting a ball", "In-off", ["Free ball", "Stun", "Jaws"]),
 ("Called by the referee when a player hasn't made a good enough effort to hit the right ball", "Miss", ["Free ball", "Clearance", "Stun"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-137.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
