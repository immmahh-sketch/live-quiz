# Bank session 10 Oct 2026: 2 more general races -> bank/race-132.json (horse racing words, tennis words; none repeat the quickfire races). 20 rows each, target 10; wrong options are
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


race("what's this horse racing word?", "Sport", "medium", ["horse racing", "betting", "words"], [
 ("An eighth of a mile, the measure for race distances", "Furlong", ["Hand", "Length", "Chain"]),
 ("A bet split between the horse winning and it finishing in the places", "Each way", ["Forecast", "Tricast", "Nap"]),
 ("Odds where you'd win less than your stake, like 1-2", "Odds-on", ["Evens", "Lay", "Nap"]),
 ("The horse with the shortest odds in the race", "Favourite", ["Nap", "Novice", "Juvenile"]),
 ("A horse given long odds, not expected to win", "Outsider", ["Novice", "Maiden", "Juvenile"]),
 ("Too close to call, so the judge checks the camera", "Photo finish", ["Objection", "Tic-tac", "Short head"]),
 ("A jump race over fences, ditches and water", "Steeplechase", ["Bumper", "Hurdle", "Claimer"]),
 ("Where the horses are paraded so punters can look them over before the race", "Paddock", ["Weighing room", "Winning post", "Rails"]),
 ("The state of the ground, from heavy to firm", "Going", ["Draw", "Rails", "Tape"]),
 ("An investigation into possible interference before the result is confirmed", "Stewards' enquiry", ["Tic-tac", "Weigh-in", "Forecast"]),
 ("Two horses crossing the line at exactly the same moment", "Dead heat", ["Short head", "Nose", "Length"]),
 ("A young female horse", "Filly", ["Dam", "Sire", "Stallion"]),
 ("A young male horse that hasn't been gelded", "Colt", ["Sire", "Dam", "Stallion"]),
 ("A male horse that has been castrated", "Gelding", ["Sire", "Stallion", "Dam"]),
 ("An adult female horse", "Mare", ["Sire", "Stallion", "Cob"]),
 ("The coloured jacket and cap a jockey wears to show who owns the horse", "Silks", ["Blinkers", "Visor", "Saddle cloth"]),
 ("Pool betting, where your winnings depend on how much everyone has staked", "Tote", ["Tic-tac", "Lay", "Nap"]),
 ("One bet linking several races, all of which must win", "Accumulator", ["Forecast", "Tricast", "Nap"]),
 ("A race where the better horses carry more weight to even things up", "Handicap", ["Claimer", "Seller", "Bumper"]),
 ("The gates the horses burst out of at the start of a flat race", "Starting stalls", ["Tape", "Rails", "Winning post"])])

race("what's this tennis word?", "Sport", "medium", ["tennis", "words"], [
 ("A serve that clips the net and still lands in, so it's taken again", "Let", ["Net cord", "Hindrance", "Walkover"]),
 ("A high shot over the head of an opponent at the net", "Lob", ["Tweener", "Half volley", "Approach shot"]),
 ("Hitting the ball before it bounces", "Volley", ["Half volley", "Approach shot", "Tweener"]),
 ("A hard overhead shot hit downwards, like a serve", "Smash", ["Tweener", "Approach shot", "Chip and charge"]),
 ("A soft shot that barely clears the net and dies", "Drop shot", ["Approach shot", "Tweener", "Moonball"]),
 ("A first-to-seven-points decider at six games all", "Tie-break", ["Golden set", "Bisque", "Walkover"]),
 ("Slang for winning a set 6–0", "Bagel", ["Bread stick", "Golden set", "Walkover"]),
 ("Missing both serves and losing the point", "Double fault", ["Hindrance", "Code violation", "Net cord"]),
 ("A shot that whizzes past an opponent rushing the net", "Passing shot", ["Approach shot", "Moonball", "Chip and charge"]),
 ("Forward spin that makes the ball dip and then kick up high", "Topspin", ["Slice", "Flat", "Chip"]),
 ("The line at the very back of the court", "Baseline", ["Service line", "No man's land", "T"]),
 ("The extra strips down the sides, used only in doubles", "Tramlines", ["Service box", "No man's land", "T"]),
 ("The score when a player wins the point after deuce", "Advantage", ["Bread stick", "Bisque", "Hindrance"]),
 ("Stepping on the baseline while you serve", "Foot fault", ["Hindrance", "Code violation", "Net cord"]),
 ("The ball-tracking system players call on to check a line call", "Hawk-Eye", ["Cyclops", "Net cord", "Wildcard"]),
 ("Winning a game when your opponent is serving", "Break", ["Hold", "Walkover", "Bisque"]),
 ("Winning all four major titles in one calendar year", "Grand Slam", ["Wildcard", "Seed", "Walkover"]),
 ("All four majors plus Olympic gold in the same year, as Steffi Graf did in 1988", "Golden Slam", ["Wildcard", "Seed", "Walkover"]),
 ("A long exchange of shots back and forth", "Rally", ["Walkover", "Hold", "Bisque"]),
 ("A beaten qualifier who gets into the main draw when someone pulls out", "Lucky loser", ["Wildcard", "Seed", "Walkover"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-132.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
