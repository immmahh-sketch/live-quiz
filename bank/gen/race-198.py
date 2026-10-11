# Bank session 11 Oct 2026: 3 more general races -> bank/race-198.json (time, advertising and sports day words). 20 rows each, target 10; wrong options are
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

race("what's this time word?", "Science", "easy", ["time", "calendar", "words"], [
 ("Two weeks", "Fortnight", ["Fortnite", "Sennight", "Weekend"]),
 ("Ten years", "Decade", ["Score", "Dozen", "Gross"]),
 ("A hundred years", "Century", ["Centurion", "Score", "Jubilee"]),
 ("A thousand years", "Millennium", ["Millipede", "Milestone", "Millimetre"]),
 ("A year with 366 days", "Leap year", ["Light year", "Gap year", "School year"]),
 ("When day and night are the same length", "Equinox", ["Eclipse", "Zenith", "Perigee"]),
 ("The longest or shortest day of the year", "Solstice", ["Eclipse", "Zenith", "Sabbatical"]),
 ("The dim light just after sunset", "Dusk", ["Husk", "Musk", "Rusk"]),
 ("The first light of morning", "Dawn", ["Drawn", "Lawn", "Yawn"]),
 ("Twelve o'clock in the day", "Noon", ["Moon", "Spoon", "Soon"]),
 ("The witching hour", "Midnight", ["Midday", "Midweek", "Midway"]),
 ("Greenwich Mean Time, by its letters", "GMT", ["GPS", "GSM", "GDP"]),
 ("What Britain switches to when the clocks go forward", "British Summer Time", ["Central European Time", "Daylight Robbery", "Summertime Blues"]),
 ("Tells the time by a shadow", "Sundial", ["Sunbed", "Sunroof", "Barometer"]),
 ("Sand trickling between two glass bulbs", "Hourglass", ["Wine glass", "Spyglass", "Glasshouse"]),
 ("A very short moment, as in 'back in a ...'", "Jiffy", ["Jaffa", "Jacuzzi", "Jigsaw"]),
 ("A public day off, often a Monday", "Bank holiday", ["Bank statement", "Busman's holiday", "Bank account"]),
 ("A long, distinct period of history", "Epoch", ["Epic", "Echo", "Ethic"]),
 ("A billionth of a second", "Nanosecond", ["Nanny goat", "Millisecond", "Microsecond"]),
 ("A page for every month on the kitchen wall", "Calendar", ["Colander", "Cylinder", "Lavender"])])

race("what's this advertising word?", "Lifestyle", "easy", ["adverts", "marketing", "words"], [
 ("A catchy phrase like 'Because you're worth it'", "Slogan", ["Sermon", "Sonnet", "Saga"]),
 ("A short catchy tune in an advert", "Jingle", ["Jangle", "Jungle", "Jingo"]),
 ("A giant poster by the roadside", "Billboard", ["Blackboard", "Skateboard", "Sideboard"]),
 ("A brand's symbol, like the Nike tick", "Logo", ["Lego", "Lingo", "Limbo"]),
 ("A character like Tony the Tiger", "Mascot", ["Muscat", "Mascara", "Masquerade"]),
 ("When the programme stops for commercials", "Ad break", ["Tea break", "Jailbreak", "Daybreak"]),
 ("A brand slipped into a film or show on purpose", "Product placement", ["Product recall", "Work placement", "Place setting"]),
 ("A company paying to put its name on shirts or events", "Sponsorship", ["Scholarship", "Citizenship", "Censorship"]),
 ("A long TV advert dressed up as a programme", "Infomercial", ["Infographic", "Intermission", "Interview"]),
 ("A social media star paid to promote products", "Influencer", ["Infiltrator", "Inspector", "Invigilator"]),
 ("An ad that springs up in a new window", "Pop-up", ["Pop-Tart", "Pop quiz", "Popcorn"]),
 ("Ad boards worn front and back by someone walking the streets", "Sandwich board", ["Sandwich bag", "Ironing board", "Drawing board"]),
 ("The people an advert is aimed at", "Target audience", ["Studio audience", "Target practice", "Captive audience"]),
 ("The watchdog that bans misleading adverts, by its letters", "ASA", ["ABTA", "ACAS", "AA"]),
 ("A sensational headline written just to get clicks", "Clickbait", ["Click and collect", "Bait and switch", "Fish bait"]),
 ("Unwanted junk email", "Spam", ["Spud", "Spat", "Scam"]),
 ("A folded flyer pushed through your door", "Leaflet", ["Leafblower", "Ringlet", "Omelette"]),
 ("Phoning strangers to sell them something", "Cold calling", ["Cold feet", "Cold shoulder", "Cold snap"]),
 ("John Lewis's yearly tear-jerker", "Christmas advert", ["Christmas card", "Christmas cracker", "Christmas jumper"]),
 ("A taster handed out to try for nothing", "Free sample", ["Free kick", "Free spirit", "Free fall"])])

race("what's this sports day word?", "Sport", "easy", ["sports day", "school", "words"], [
 ("Balancing something fragile on cutlery while you run", "Egg and spoon race", ["Bacon and egg", "Spoon and fork", "Egg hunt"]),
 ("Jumping along inside a hessian bag", "Sack race", ["Sack of potatoes", "Rat race", "Sack truck"]),
 ("Running with your ankle tied to a partner's", "Three-legged race", ["Three-wheeler", "Two-step", "Four-poster"]),
 ("Walking on your hands while someone holds your legs", "Wheelbarrow race", ["Handstand", "Wheelie bin", "Crab walk"]),
 ("Two teams heaving on a rope", "Tug of war", ["Tugboat", "Man of war", "War of words"]),
 ("Passing a baton between teammates", "Relay", ["Replay", "Delay", "Rally"]),
 ("Crawling under nets and over barriers", "Obstacle course", ["Golf course", "Main course", "Crash course"]),
 ("When the mums and dads go flat out", "Parents' race", ["Arms race", "Boat race", "Space race"]),
 ("'Ready, steady ...'", "Go", ["Stop", "Now", "Wait"]),
 ("A ribbon award pinned on the winners", "Rosette", ["Roulette", "Rosemary", "Rosetta Stone"]),
 ("What your team, named after a colour or a famous person, earns", "House points", ["House arrest", "House party", "Brownie points"]),
 ("Where the long jump lands", "Sandpit", ["Cockpit", "Snake pit", "Mosh pit"]),
 ("The ribbon the winner breaks across the line", "Finishing tape", ["Red tape", "Masking tape", "Duct tape"]),
 ("A big orange bouncy ball with handles", "Space hopper", ["Grasshopper", "Hip hop", "Hopscotch"]),
 ("Balanced on your head in one of the races", "Bean bag", ["Tea bag", "Doggy bag", "Sandbag"]),
 ("Jumping a turning rope as you run", "Skipping race", ["Rope swing", "Tightrope", "Boat race"]),
 ("Small barriers to leap over", "Hurdles", ["Huddles", "Hurdy-gurdy", "Hustles"]),
 ("What everyone gets for taking part", "Sticker", ["Medal", "Trophy", "Cup"]),
 ("Slapped on by teachers on a hot afternoon", "Sun cream", ["Ice cream", "Salad cream", "Clotted cream"]),
 ("What the teacher keeps the scores on", "Clipboard", ["Cupboard", "Skateboard", "Clipper"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-198.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
