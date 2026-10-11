# Bank session 11 Oct 2026: 3 more general races -> bank/race-162.json (panto, Bonfire Night and Scouting words). 20 rows each, target 10; wrong options are
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

race("what's this panto word?", "Entertainment", "easy", ["pantomime", "Christmas", "theatre"], [
 ("The man in a frock and a huge wig", "Dame", ["Ugly duckling", "Jester", "Clown"]),
 ("The hero, traditionally played by a young woman in tights", "Principal boy", ["Leading lady", "Understudy", "Chorus girl"]),
 ("The audience's reply to 'Oh yes it is!'", "Oh no it isn't!", ["Hip hip hooray!", "Encore!", "Bravo!"]),
 ("What everyone shouts when the villain sneaks up", "Behind you!", ["Bravo!", "Encore!", "Hip hip hooray!"]),
 ("What the audience does when the villain walks on", "Booing", ["Cheering", "Clapping", "Whistling"]),
 ("Two actors in one costume in Jack and the Beanstalk", "Pantomime cow", ["Pantomime dragon", "Pantomime goat", "Pantomime pig"]),
 ("The dame in Aladdin", "Widow Twankey", ["Mother Goose", "Dame Trott", "Sarah the Cook"]),
 ("Cinderella's loyal friend", "Buttons", ["Dandini", "Wishee Washee", "Idle Jack"]),
 ("The villain in Aladdin", "Abanazar", ["Fleshcreep", "Captain Hook", "Baron Hardup"]),
 ("The villain in Dick Whittington", "King Rat", ["Fleshcreep", "Captain Hook", "Baron Hardup"]),
 ("Dick Whittington's faithful companion", "Tommy the Cat", ["Puss in Boots", "Daisy the Cow", "Simple Simon"]),
 ("Cinderella's nasty stepsisters", "Ugly Sisters", ["Weird Sisters", "Andrews Sisters", "Pointer Sisters"]),
 ("Messy comedy with buckets of gunge and custard pies", "Slapstick", ["Stand-up", "Satire", "Mime"]),
 ("Thrown into the audience", "Sweets", ["Confetti", "Flowers", "Programmes"]),
 ("The lyrics lowered from above for a sing-along", "Song sheet", ["Cue card", "Autocue", "Libretto"]),
 ("Turns a pumpkin into a coach", "Fairy Godmother", ["Tooth Fairy", "Wicked Queen", "Snow Queen"]),
 ("Pops out of the lamp in Aladdin", "Genie", ["Leprechaun", "Imp", "Goblin"]),
 ("What Jack climbs", "Beanstalk", ["Ladder", "Drainpipe", "Rope"]),
 ("The season when most pantos run", "Christmas", ["Easter", "Halloween", "Midsummer"]),
 ("What Cinderella leaves behind at the ball", "Glass slipper", ["Ruby slipper", "Clog", "Wellington"])])

race("what's this Bonfire Night word?", "Bonfire Night and autumn", "easy", ["Bonfire Night", "Gunpowder Plot", "fireworks"], [
 ("Caught guarding the gunpowder in 1605", "Guy Fawkes", ["Thomas Percy", "Thomas Wintour", "Walter Raleigh"]),
 ("The leader of the Gunpowder Plot", "Robert Catesby", ["Thomas Percy", "Thomas Wintour", "Francis Drake"]),
 ("The king they tried to blow up", "James I", ["Charles I", "Henry VIII", "Elizabeth I"]),
 ("The building they tried to blow up", "Houses of Parliament", ["Tower of London", "Westminster Abbey", "Buckingham Palace"]),
 ("What filled the barrels under the House of Lords", "Gunpowder", ["Dynamite", "TNT", "Napalm"]),
 ("The stuffed figure burned on the bonfire", "Guy", ["Scarecrow", "Mannequin", "Puppet"]),
 ("What children used to ask for, showing off their stuffed figure", "Penny for the guy", ["Trick or treat", "Bob a job", "Knock knock"]),
 ("The handheld firework you write your name with", "Sparkler", ["Fountain", "Mine", "Flare"]),
 ("A tube firing coloured balls one after another", "Roman candle", ["Fountain", "Cake", "Flare"]),
 ("Spins round on a post", "Catherine wheel", ["Fountain", "Mine", "Cake"]),
 ("Shoots up into the sky on a stick", "Rocket", ["Mine", "Cake", "Flare"]),
 ("A sticky, red-coated treat on a stick", "Toffee apple", ["Candyfloss", "Lolly", "Corn dog"]),
 ("Sticky oaty gingerbread from Yorkshire", "Parkin", ["Flapjack", "Brack", "Lardy cake"]),
 ("Dark, brittle treacle sweet, also called plot toffee", "Bonfire toffee", ["Fudge", "Tablet", "Nougat"]),
 ("The opening words of the rhyme about the fifth of November", "Remember, remember", ["Ring a ring", "Twinkle, twinkle", "Hickory dickory"]),
 ("The Sussex town famous for its huge bonfire parades", "Lewes", ["Rye", "Hastings", "Brighton"]),
 ("Where the gunpowder was hidden, beneath the House of Lords", "Undercroft", ["Attic", "Belfry", "Turret"]),
 ("The crime the plotters were executed for", "Treason", ["Arson", "Piracy", "Fraud"]),
 ("The date of Bonfire Night", "Fifth of November", ["First of November", "Thirty-first of October", "Eleventh of November"]),
 ("Where you put a used sparkler", "Bucket of water", ["Bin", "Flower bed", "Pocket"])])

race("what's this Scouting word?", "Everyday life", "medium", ["Scouts", "Guides", "words"], [
 ("The founder of the Scouts", "Baden-Powell", ["Lord Kitchener", "Captain Scott", "Ernest Shackleton"]),
 ("The site of the first Scout camp, in 1907", "Brownsea Island", ["Lundy", "Holy Island", "Isle of Wight"]),
 ("The ring that holds the neckerchief in place", "Woggle", ["Toggle", "Brooch", "Cufflink"]),
 ("The scarf worn in the troop's colours", "Neckerchief", ["Cravat", "Cummerbund", "Stole"]),
 ("The Scout motto", "Be Prepared", ["Do Your Best", "Lend a Hand", "Be Kind"]),
 ("The section for 8 to 10½-year-olds", "Cubs", ["Squirrels", "Explorers", "Rovers"]),
 ("The section for 6 to 8-year-olds", "Beavers", ["Explorers", "Rovers", "Rangers"]),
 ("The name for a Cub leader, from The Jungle Book", "Akela", ["Mowgli", "Kaa", "Shere Khan"]),
 ("Earned for a skill and sewn on the uniform", "Badge", ["Medal", "Rosette", "Trophy"]),
 ("A huge international Scout gathering", "Jamboree", ["Jubilee", "Carnival", "Regatta"]),
 ("The old fundraising week doing chores for a shilling", "Bob-a-job", ["Penny for the guy", "Trick or treat", "Car boot"]),
 ("The Scouts' variety show, made famous by Ralph Reader", "Gang Show", ["Royal Variety", "Panto", "Talent show"]),
 ("Right over left, then left over right", "Reef knot", ["Granny knot", "Bowline", "Clove hitch"]),
 ("A small group of about six Scouts with its own leader", "Patrol", ["Platoon", "Squadron", "Brigade"]),
 ("What new Scouts make when they join", "Promise", ["Wager", "Toast", "Petition"]),
 ("Where you sing songs and toast marshmallows", "Campfire", ["Barbecue", "Beacon", "Brazier"]),
 ("The girls' movement founded in 1910 by Agnes Baden-Powell", "Guides", ["Women's Institute", "Townswomen's Guild", "Rangers"]),
 ("The younger section of Girlguiding, aged 7 to 10", "Brownies", ["Rainbows", "Rangers", "Pixies"]),
 ("Used with a map for orienteering", "Compass", ["Sextant", "Barometer", "Sundial"]),
 ("How many fingers the Scout salute uses", "Three", ["Two", "Four", "Five"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-162.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
