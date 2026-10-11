# Bank session 11 Oct 2026: 3 more general races -> bank/race-194.json (hair salon, playground and pub quiz words). 20 rows each, target 10; wrong options are
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

race("what's this hair salon word?", "Fashion", "medium", ["hairdressers", "beauty", "words"], [
 ("Streaks of lighter colour through the hair", "Highlights", ["Lowlights", "Spotlights", "Headlights"]),
 ("Hand-painted colour that fades in naturally", "Balayage", ["Barrage", "Badinage", "Collage"]),
 ("A chemical treatment for lasting curls", "Perm", ["Term", "Germ", "Firm"]),
 ("Styling with a hairdryer and round brush", "Blow-dry", ["Tumble dry", "Bone dry", "Dry run"]),
 ("The regrowth showing near the scalp", "Roots", ["Shoots", "Routes", "Boots"]),
 ("Frayed tips that need a trim", "Split ends", ["Loose ends", "Dead ends", "Weekends"]),
 ("Hot plates that flatten curls", "Straighteners", ["Crimpers", "Flatterers", "Stretchers"]),
 ("A hot barrel you wrap hair round for curls", "Curling tongs", ["Sugar tongs", "Salad tongs", "Crimpers"]),
 ("Curlers you might sleep in", "Rollers", ["Rolling pins", "High rollers", "Roller skates"]),
 ("The basin where you lean back to have your hair washed", "Backwash", ["Whitewash", "Mouthwash", "Hogwash"]),
 ("Strips wrapped round hair while the colour takes", "Foils", ["Spoils", "Coils", "Soils"]),
 ("Added hair for extra length", "Extensions", ["Pensions", "Tensions", "Detentions"]),
 ("The product that takes the brassiness out of blonde", "Toner", ["Tuner", "Loner", "Donor"]),
 ("Strips the colour out of hair", "Bleach", ["Beach", "Leech", "Breach"]),
 ("A quick tidy-up of the ends", "Trim", ["Prim", "Slim", "Brim"]),
 ("Cut at different lengths for volume", "Layers", ["Players", "Prayers", "Slayers"]),
 ("A mist that holds a style in place", "Hairspray", ["Body spray", "Pepper spray", "Sea spray"]),
 ("A spray-on powder that freshens hair between washes", "Dry shampoo", ["Dry cleaning", "Dry ice", "Dry rot"]),
 ("The big dome you sit under", "Hood dryer", ["Hood ornament", "Riding hood", "Hoodie"]),
 ("A dab of dye behind the ear 48 hours before colouring", "Patch test", ["Spot check", "Patch-up", "Litmus test"])])

race("what's this playground word?", "Lifestyle", "easy", ["playground", "childhood", "words"], [
 ("A plank that tips up and down with a child at each end", "See-saw", ["Rocking horse", "Merry-go-round", "Hammock"]),
 ("A spinning platform you push and jump on", "Roundabout", ["Turntable", "Lazy Susan", "Hula hoop"]),
 ("Bars you swing along hand over hand", "Monkey bars", ["Climbing wall", "Parallel bars", "Candy bars"]),
 ("Hopping along chalked squares", "Hopscotch", ["Butterscotch", "Hotchpotch", "Hop-on hop-off"]),
 ("Charging across the playground without getting caught", "British bulldog", ["British Lion", "Bulldog clip", "British Gas"]),
 ("The chasing game also called tag", "Tig", ["Twig", "Gig", "Pig"]),
 ("Tag where you stand frozen until someone frees you", "Stuck in the mud", ["Mud pie", "Muddy waters", "Stuck record"]),
 ("Creeping up behind someone asking the time", "What's the time, Mr Wolf?", ["Who's afraid of the big bad wolf?", "Wolf whistle", "Cry wolf"]),
 ("Tapping heads round a circle until one gets chased", "Duck, duck, goose", ["Wild goose chase", "Duck and dive", "Goosey goosey gander"]),
 ("Riding on someone's back", "Piggyback", ["Piggy bank", "Piggy in the middle", "Hogwash"]),
 ("Jumping as a rope turns", "Skipping rope", ["Tightrope", "Tow rope", "Jump leads"]),
 ("Glass balls flicked at each other", "Marbles", ["Bubbles", "Pebbles", "Baubles"]),
 ("Horse chestnuts on strings", "Conkers", ["Acorns", "Walnuts", "Coconuts"]),
 ("Little metal stars picked up between bounces of a ball", "Jacks", ["Dominoes", "Tiddlywinks", "Pick-up sticks"]),
 ("String shapes passed between fingers", "Cat's cradle", ["Cat's whiskers", "Cat flap", "Cradle snatcher"]),
 ("Calling first dibs on something", "Bagsy", ["Baggy", "Bugsy", "Patsy"]),
 ("Who served the school lunches", "Dinner lady", ["Tea lady", "Bag lady", "Cleaning lady"]),
 ("Who helped you cross the road", "Lollipop lady", ["Tea lady", "Bag lady", "First lady"]),
 ("Staying in at break because of the rain", "Wet play", ["Fair play", "Foul play", "Role play"]),
 ("Vaulting over each other's bent backs", "Leapfrog", ["Frogspawn", "Leap year", "Frogmarch"])])

race("what's this pub quiz word?", "Games", "easy", ["pub quiz", "quizzes", "words"], [
 ("The person reading out the questions", "Quizmaster", ["Ringmaster", "Postmaster", "Scoutmaster"]),
 ("A sheet of faces to name", "Picture round", ["Merry-go-round", "Milk round", "Paper round"]),
 ("Name that song from the opening bars", "Music round", ["Paper round", "Round robin", "Round of applause"]),
 ("The nearest-number question that splits a draw", "Tiebreak", ["Jailbreak", "Heartbreak", "Daybreak"]),
 ("The card you play to double one round's points", "Joker", ["Ace", "Queen", "Knave"]),
 ("Where you write your team's answers", "Answer sheet", ["Balance sheet", "Bed sheet", "Spreadsheet"]),
 ("The pun you agonise over, like 'Quiz Team Aguilera'", "Team name", ["Code name", "Pen name", "Stage name"]),
 ("The jackpot carried to next week when nobody wins", "Rollover", ["Pushover", "Hangover", "Changeover"]),
 ("The booby prize for coming last", "Wooden spoon", ["Silver spoon", "Greasy spoon", "Golden ticket"]),
 ("University Challenge's opening question", "Starter for ten", ["Ten-pin", "Perfect ten", "Top ten"]),
 ("The Millionaire lifeline where you ring a mate", "Phone a friend", ["Text a pal", "Call my bluff", "Ring a ding"]),
 ("The lifeline where the crowd votes", "Ask the audience", ["Ask Jeeves", "Ask the family", "Poll the room"]),
 ("The lifeline that removes two wrong answers", "Fifty-fifty", ["Half-time", "Double or quits", "Go halves"]),
 ("Mastermind's first-round topic you pick yourself", "Specialist subject", ["General knowledge", "Open book", "Hobby horse"]),
 ("The show where the lowest score wins", "Pointless", ["The Chase", "Eggheads", "Tipping Point"]),
 ("An extra question worth more points", "Bonus question", ["Bonus ball", "Trick question", "Leading question"]),
 ("Rearranged letters to unscramble", "Anagram", ["Telegram", "Hologram", "Diagram"]),
 ("The bell before closing time", "Last orders", ["Last post", "Last rites", "Last laugh"]),
 ("The call at the end of each round", "Pens down", ["Pins down", "Hands up", "Eyes down"]),
 ("Swapping sheets with the next table to check them", "Marking", ["Parking", "Barking", "Marketing"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-194.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
