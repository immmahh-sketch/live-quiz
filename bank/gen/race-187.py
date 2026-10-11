# Bank session 11 Oct 2026: 3 more general races -> bank/race-187.json (boxing, athletics and decorating words). 20 rows each, target 10; wrong options are
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

race("what's this boxing word?", "Sport", "medium", ["boxing", "words"], [
 ("A quick straight punch with the lead hand", "Jab", ["Cross", "Swing", "Slap"]),
 ("A punch thrown round from the side", "Hook", ["Cross", "Lunge", "Prod"]),
 ("A rising punch to the chin", "Uppercut", ["Undercut", "Cross", "Overhand"]),
 ("A left-handed boxer", "Southpaw", ["Orthodox", "Sidewinder", "Backhand"]),
 ("Floored and not up by the count of ten", "Knockout", ["Walkover", "Split decision", "Draw"]),
 ("The referee stops it though the boxer's still standing", "Technical knockout", ["Walkover", "Split decision", "Unanimous decision"]),
 ("An illegal low punch", "Below the belt", ["Over the top", "Off the cuff", "Under the radar"]),
 ("Holding on so your opponent can't punch", "Clinch", ["Headlock", "Nelson", "Tackle"]),
 ("Practice fighting with a partner in training", "Sparring", ["Shadow boxing", "Skipping", "Roadwork"]),
 ("The day-before check that both fighters make the limit", "Weigh-in", ["Face-off", "Press call", "Line-up"]),
 ("The top weight division", "Heavyweight", ["Cruiserweight", "Middleweight", "Welterweight"]),
 ("Protects the teeth", "Gumshield", ["Chin strap", "Visor", "Nose clip"]),
 ("Where the boxer sits with the trainer between rounds", "Corner", ["Bench", "Dugout", "Pit"]),
 ("The corner man who stops the bleeding", "Cutman", ["Bagman", "Hitman", "Linesman"]),
 ("Rings to start and end each round", "Bell", ["Whistle", "Horn", "Klaxon"]),
 ("Each three-minute session of a pro fight", "Round", ["Quarter", "Innings", "Leg"]),
 ("The smaller fights before the main event", "Undercard", ["Wildcard", "Scorecard", "Red card"]),
 ("The prize money a boxer is paid", "Purse", ["Wallet", "Kitty", "Jackpot"]),
 ("Ali's trick of leaning on the ropes to tire Foreman out", "Rope-a-dope", ["Ali shuffle", "Rumble in the Jungle", "Rock-a-bye"]),
 ("A wild, all-or-nothing swinging punch", "Haymaker", ["Haystack", "Matchmaker", "Peacemaker"])])

race("what's this athletics word?", "Sport", "medium", ["athletics", "track and field", "words"], [
 ("What relay runners pass on", "Baton", ["Torch", "Flag", "Wand"]),
 ("The last runner in a relay team", "Anchor", ["Captain", "Skipper", "Sweeper"]),
 ("The long race with barriers and a water jump", "Steeplechase", ["Cross-country", "Obstacle course", "Assault course"]),
 ("The sprint over ten barriers", "Hurdles", ["Fences", "Gates", "Barricades"]),
 ("26.2 miles", "Marathon", ["Half marathon", "Ultramarathon", "Fun run"]),
 ("Ten events over two days", "Decathlon", ["Pentathlon", "Triathlon", "Biathlon"]),
 ("Seven events, for the women at the Olympics", "Heptathlon", ["Pentathlon", "Triathlon", "Biathlon"]),
 ("The spear you throw", "Javelin", ["Lance", "Trident", "Harpoon"]),
 ("Pushing a heavy metal ball away from the neck", "Shot put", ["Bowls", "Boules", "Curling"]),
 ("The heavy plate spun round and thrown", "Discus", ["Frisbee", "Quoit", "Saucer"]),
 ("A ball on a wire, whirled round and let go", "Hammer", ["Mace", "Flail", "Kettlebell"]),
 ("Clearing a bar with a long bendy pole", "Pole vault", ["Pole dance", "Pole position", "Caber toss"]),
 ("The event of the Fosbury flop", "High jump", ["Long jump", "Ski jump", "Bungee jump"]),
 ("Hop, skip and jump", "Triple jump", ["Long jump", "Hopscotch", "Leapfrog"]),
 ("What sprinters push off from at the start", "Starting blocks", ["Building blocks", "Stumbling blocks", "Chopping blocks"]),
 ("Going before the gun", "False start", ["Head start", "Jump start", "Kick start"]),
 ("A finish too close to call by eye", "Photo finish", ["Close shave", "Near miss", "Dead heat"]),
 ("What PB stands for", "Personal best", ["Peak burst", "Pace bonus", "Perfect ball"]),
 ("A runner hired to set the speed early on", "Pacemaker", ["Matchmaker", "Peacemaker", "Shoemaker"]),
 ("One full circuit of the 400-metre track", "Lap", ["Leg", "Stage", "Spin"])])

race("what's this decorating word?", "Lifestyle", "medium", ["DIY", "decorating", "words"], [
 ("The first coat, to help paint stick to bare surfaces", "Primer", ["Topcoat", "Lacquer", "Glaze"]),
 ("The coat beneath the gloss", "Undercoat", ["Overcoat", "Raincoat", "Petticoat"]),
 ("Shiny paint for doors and skirting", "Gloss", ["Distemper", "Whitewash", "Creosote"]),
 ("A flat finish with no shine", "Matt", ["Satin", "Silk", "Lacquer"]),
 ("Water-based paint for walls and ceilings", "Emulsion", ["Creosote", "Varnish", "Whitewash"]),
 ("Tape that stops paint going where it shouldn't", "Masking tape", ["Duct tape", "Sellotape", "Red tape"]),
 ("Covers the furniture and floor while you paint", "Dust sheet", ["Bed sheet", "Spreadsheet", "Balance sheet"]),
 ("Rolls paint onto walls quickly", "Roller", ["Squeegee", "Trowel", "Spatula"]),
 ("Rough paper for smoothing wood", "Sandpaper", ["Tissue paper", "Crêpe paper", "Greaseproof paper"]),
 ("Paste squeezed into cracks and holes", "Filler", ["Grout", "Mortar", "Glue"]),
 ("The board along the bottom of the walls", "Skirting board", ["Picture rail", "Architrave", "Sill"]),
 ("The rail round the wall at waist height", "Dado rail", ["Picture rail", "Curtain rail", "Handrail"]),
 ("Curved moulding where the wall meets the ceiling", "Coving", ["Architrave", "Plinth", "Lintel"]),
 ("The famous creamy paint colour of rented flats", "Magnolia", ["Mustard", "Avocado", "Duck egg"]),
 ("The cleaner for washing walls before painting", "Sugar soap", ["Washing soda", "Caustic soda", "Saddle soap"]),
 ("The solvent for cleaning oil-paint brushes", "White spirit", ["Surgical spirit", "Holy Spirit", "Team spirit"]),
 ("The bumpy textured wallpaper of the 1970s", "Woodchip", ["Wood stain", "Chipboard", "Hardboard"]),
 ("A folding ladder with flat steps", "Stepladder", ["Rope ladder", "Snakes and ladders", "Extension ladder"]),
 ("A cut-out sheet for painting a pattern", "Stencil", ["Doily", "Collage", "Mosaic"]),
 ("One wall painted in a bolder colour than the rest", "Feature wall", ["Party wall", "Dry-stone wall", "Firewall"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-187.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
