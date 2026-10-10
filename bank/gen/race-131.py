# Bank session 10 Oct 2026: 2 more general races -> bank/race-131.json (cricket words, golf words; none repeat the quickfire races). 20 rows each, target 10; wrong options are
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


race("what's this cricket word?", "Cricket", "hard", ["cricket", "words"], [
 ("A leg-spinner's trick ball that turns the 'wrong' way", "Googly", ["Doosra", "Flipper", "Teesra"]),
 ("A short ball that rears up towards the batter's head", "Bouncer", ["Beamer", "Slower ball", "Flipper"]),
 ("A close fielding spot between the slips and point", "Gully", ["Third man", "Fine leg", "Square leg"]),
 ("A brave fielder crouched just off the bat on the off side", "Silly point", ["Short leg", "Mid-wicket", "Cover"]),
 ("A lower-order batter sent in late in the day to protect a better one", "Nightwatchman", ["Pinch hitter", "Runner", "Twelfth man"]),
 ("Made to bat again straight away after falling far behind", "Follow-on", ["Super over", "Retired hurt", "Free hit"]),
 ("The captain ends his side's innings early, with wickets still in hand", "Declare", ["Retired hurt", "Timed out", "Concede"]),
 ("Three wickets with three balls in a row", "Hat-trick", ["Five-for", "Maiden", "Ton"]),
 ("Out because the keeper broke the wicket while you'd wandered out of your crease", "Stumped", ["Caught behind", "Timed out", "Obstructing the field"]),
 ("Out because the stumps were broken before you made your ground going for a run", "Run out", ["Caught behind", "Timed out", "Hit wicket"]),
 ("Out first ball, without scoring", "Golden duck", ["Pair", "Ton", "Five-for"]),
 ("The 'unlucky' score of 111, when umpire David Shepherd would hop on one leg", "Nelson", ["Ton", "Pair", "Five-for"]),
 ("A ball bowled too far from the batter to reach, giving away a run", "Wide", ["Bye", "Dead ball", "Free hit"]),
 ("An illegal delivery, often for overstepping the crease", "No-ball", ["Dead ball", "Bye", "Overthrow"]),
 ("A run scored after the ball hits the batter's body rather than the bat", "Leg bye", ["Bye", "Overthrow", "Free hit"]),
 ("Trash talk from fielders to put the batter off", "Sledging", ["Chin music", "Corridor of uncertainty", "Dibbly-dobbly"]),
 ("One of the weakest batters, coming in at the bottom of the order", "Tail-ender", ["Pinch hitter", "Runner", "Twelfth man"]),
 ("The overs at the start of a one-day innings when fielders must stay inside the circle", "Powerplay", ["Super over", "Free hit", "Dead ball"]),
 ("Six balls bowled from one end", "Over", ["Spell", "Session", "Innings"]),
 ("A shot played down on one knee, swinging the ball round behind square", "Sweep", ["Cover drive", "Hook", "Cut"])])

race("what's this golf word?", "Sport", "medium", ["golf", "words"], [
 ("Three under par on a single hole", "Albatross", ["Condor", "Snowman", "Bandit"]),
 ("Two under par on a single hole", "Eagle", ["Condor", "Snowman", "Scramble"]),
 ("One over par on a single hole", "Bogey", ["Snowman", "Condor", "Duff"]),
 ("An unofficial free do-over after a bad shot", "Mulligan", ["Provisional", "Scramble", "Skins"]),
 ("The lump of turf you dig out with a shot", "Divot", ["Fringe", "Collar", "Lip"]),
 ("The little peg you balance the ball on for your first shot", "Tee", ["Ball marker", "Flagstick", "Lip"]),
 ("The neatly mown strip between the tee and the green", "Fairway", ["Fringe", "Apron", "Collar"]),
 ("The longer grass either side of that neatly mown strip", "Rough", ["Fringe", "Apron", "Collar"]),
 ("A hole that bends sharply to the left or right", "Dogleg", ["Pin high", "Out of bounds", "Lip"]),
 ("The number of shots a weaker player gets to level things up", "Handicap", ["Bandit", "Medal", "Nassau"]),
 ("A shot that curves badly away to the right, for a right-hander", "Slice", ["Draw", "Hook", "Duff"]),
 ("A horror shot off the neck of the club that shoots off sideways", "Shank", ["Skull", "Thin", "Duff"]),
 ("A short putt your opponent lets you skip", "Gimme", ["Scramble", "Skins", "Nassau"]),
 ("A seaside course on sandy ground, like St Andrews", "Links", ["Parkland", "Heathland", "Moorland"]),
 ("A scoring system giving points for each hole instead of counting total strokes", "Stableford", ["Medal", "Matchplay", "Skins"]),
 ("The club with the biggest head, for the longest shots off the tee", "Driver", ["Hybrid", "Spoon", "Mashie"]),
 ("A steep-faced club for short, high shots and getting out of sand", "Wedge", ["Hybrid", "Spoon", "Mashie"]),
 ("Holes 10 to 18", "Back nine", ["Front nine", "Turn", "Scramble"]),
 ("Nervy twitching that ruins short putts", "Yips", ["Snowman", "Lip", "Duff"]),
 ("A very high, soft lob over a bunker that lands dead", "Flop shot", ["Worm burner", "Punch shot", "Bump and run"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-131.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
