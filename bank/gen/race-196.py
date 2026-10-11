# Bank session 11 Oct 2026: 3 more general races -> bank/race-196.json (birthday party, Sunday roast and badminton words). 20 rows each, target 10; wrong options are
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

race("what's this birthday party word?", "Lifestyle", "easy", ["birthdays", "parties", "words"], [
 ("Unwrapping a layer each time the music stops", "Pass the parcel", ["Pass the port", "Pass the buck", "Pass the hat"]),
 ("One seat fewer each time the music stops", "Musical chairs", ["Musical beds", "Deckchairs", "Armchairs"]),
 ("Freezing on the spot when the music stops", "Musical statues", ["Musical bumps", "Hokey-cokey", "Conga"]),
 ("Blindfolded, trying to stick it in the right place", "Pin the tail on the donkey", ["Blind man's buff", "Pin the tail on the pig", "Donkey derby"]),
 ("The goodie bag you take home", "Party bag", ["Doggy bag", "Bean bag", "Tote bag"]),
 ("A papier-mâché figure you whack for sweets", "Piñata", ["Pinafore", "Pinto", "Pinnacle"]),
 ("The inflatable everyone jumps on", "Bouncy castle", ["Sandcastle", "Bouncy ball", "Castle keep"]),
 ("Blown out on the cake", "Candles", ["Matches", "Lanterns", "Torches"]),
 ("Pull the string for a bang and streamers", "Party poppers", ["Christmas crackers", "Bubble wrap", "Popcorn"]),
 ("Turning up as a pirate or a princess", "Fancy dress", ["Black tie", "Smart casual", "Dress code"]),
 ("Lifting the birthday child once for every year", "The bumps", ["The bends", "The jumps", "The lumps"]),
 ("The classic party pudding", "Jelly and ice cream", ["Jam and cream", "Strawberries and cream", "Fish and chips"]),
 ("A cone of card held on with elastic", "Party hat", ["Top hat", "Hard hat", "Bobble hat"]),
 ("Friends staying the night", "Sleepover", ["Hangover", "Takeover", "Leftover"]),
 ("Pinned on the card, saying 'I am 7'", "Badge", ["Medal", "Rosette", "Sticker"]),
 ("The entertainer who pulls a rabbit from a hat", "Magician", ["Clown", "Juggler", "Ventriloquist"]),
 ("Twisting balloons into sausage dogs", "Balloon modelling", ["Origami", "Papier-mâché", "Plasticine"]),
 ("The card asking your friends to come", "Invitation", ["Invoice", "Inspection", "Invention"]),
 ("The song everybody sings", "Happy Birthday", ["Auld Lang Syne", "Jingle Bells", "Here Comes the Bride"]),
 ("What you make as you blow out the candles", "Wish", ["Toast", "Speech", "Promise"])])

race("what's this Sunday roast word?", "Food and drink", "easy", ["Sunday roast", "British food", "words"], [
 ("Batter that puffs up in hot fat", "Yorkshire pudding", ["Spotted dick", "Bread pudding", "Black pudding"]),
 ("The sauce made from the meat juices", "Gravy", ["Custard", "Béchamel", "Ketchup"]),
 ("The famous brand of gravy granules", "Bisto", ["Bovril", "Marmite", "Horlicks"]),
 ("The jug the gravy is served in", "Gravy boat", ["Saucepan", "Teapot", "Ramekin"]),
 ("The crispy skin on roast pork", "Crackling", ["Crumble", "Crust", "Croutons"]),
 ("The sage and onion mix cooked with the chicken", "Stuffing", ["Dumplings", "Croutons", "Couscous"]),
 ("The hot sauce served with roast beef", "Horseradish", ["Tartare sauce", "Salad cream", "Brown sauce"]),
 ("Served with roast lamb", "Mint sauce", ["Tartare sauce", "Salad cream", "Cranberry sauce"]),
 ("Served with roast pork", "Apple sauce", ["Tartare sauce", "Salad cream", "Brown sauce"]),
 ("The milky, clove-scented sauce for roast chicken or turkey", "Bread sauce", ["Hollandaise", "Tartare sauce", "Salsa"]),
 ("Fluffy inside, crispy outside", "Roast potatoes", ["Jacket potatoes", "Mash", "Chips"]),
 ("The pub where a chef slices the meat for you", "Carvery", ["Cavalry", "Cavern", "Brewery"]),
 ("The whole piece of meat you roast", "Joint", ["Slab", "Hunk", "Slice"]),
 ("Spooning the juices over the meat as it cooks", "Basting", ["Boasting", "Wasting", "Toasting"]),
 ("Leaving the meat to stand before carving", "Resting", ["Nesting", "Testing", "Wresting"]),
 ("The long blade for slicing the joint", "Carving knife", ["Butter knife", "Penknife", "Palette knife"]),
 ("Florets baked in a cheesy sauce", "Cauliflower cheese", ["Macaroni cheese", "Welsh rarebit", "Cheese on toast"]),
 ("Sausages wrapped in bacon", "Pigs in blankets", ["Toad in the hole", "Scotch eggs", "Sausage rolls"]),
 ("Sweet pale roots, roasted with honey", "Parsnips", ["Turnips", "Radishes", "Beetroot"]),
 ("What becomes Monday's bubble and squeak", "Leftovers", ["Takeaways", "Starters", "Seconds"])])

race("what's this badminton word?", "Sport", "medium", ["badminton", "racket sports", "words"], [
 ("The feathered thing you hit", "Shuttlecock", ["Puck", "Ball", "Dart"]),
 ("What a top-quality shuttle's skirt is made of", "Feathers", ["Silk", "Leather", "Straw"]),
 ("How many feathers a shuttlecock has", "16", ["8", "12", "20"]),
 ("A steep, powerful downward hit", "Smash", ["Lob", "Slice", "Dink"]),
 ("A high, deep shot to the back of the court", "Clear", ["Dink", "Slice", "Chip"]),
 ("A gentle shot that drops just over the net", "Drop shot", ["Drop goal", "Drop kick", "Long shot"]),
 ("A fast, flat shot skimming the net", "Drive", ["Lob", "Dink", "Spin"]),
 ("An exchange of shots until a point is won", "Rally", ["Relay", "Raffle", "Round"]),
 ("Points needed to win a game, with a two-point lead", "21", ["11", "15", "25"]),
 ("A man and a woman on each side", "Mixed doubles", ["Mixed grill", "Mixed bag", "Mixed martial arts"]),
 ("The famous championships held in Birmingham", "All England Open", ["British Open", "Queen's Club", "Wimbledon"]),
 ("Must be hit underarm, below the waist", "Serve", ["Toss", "Throw-in", "Bowl"]),
 ("The point is replayed, say if the shuttle gets stuck", "Let", ["Deuce", "Advantage", "Rerun"]),
 ("An illegal shot or serve that loses the rally", "Fault", ["Offside", "No-ball", "Handball"]),
 ("What you hit it with", "Racket", ["Bat", "Club", "Paddle"]),
 ("A delicate tap just over the net from close in", "Net shot", ["Net curtain", "Net profit", "Long shot"]),
 ("The country with the most Olympic badminton golds", "China", ["Japan", "India", "Thailand"]),
 ("The extra strips down the sides of a doubles court", "Tramlines", ["Bus lanes", "Gutters", "Wings"]),
 ("Hitting it up from low down to the back of the court", "Lift", ["Elevator", "Hoist", "Shove"]),
 ("The American name for the shuttlecock", "Birdie", ["Eagle", "Bogey", "Robin"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-196.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
