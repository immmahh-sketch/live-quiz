# Bank session 10 Oct 2026: 3 more general races -> bank/race-150.json (cinema words, sports officials, ice cream words). 20 rows each, target 10; wrong options are
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

race("what's this cinema word?", "Film", "easy", ["cinema", "film", "words"], [
 ("A short advert for a film that's coming soon", "Trailer", ["Spoiler", "Montage", "Outtake"]),
 ("The salty or sweet snack eaten by the bucket", "Popcorn", ["Candyfloss", "Pretzels", "Toffee apples"]),
 ("Shows you to your seat with a torch", "Usher", ["Projectionist", "Clapper loader", "Gaffer"]),
 ("Where you buy your tickets", "Box office", ["Foyer", "Stalls", "Projection booth"]),
 ("Beams the film onto the screen from the back", "Projector", ["Clapperboard", "Boom mic", "Green screen"]),
 ("The glitzy first showing, with the stars there in person", "Premiere", ["Matinée", "Encore", "Curtain call"]),
 ("A huge, big-budget hit", "Blockbuster", ["B-movie", "Short", "Art-house film"]),
 ("Part two of the story", "Sequel", ["Prequel", "Spin-off", "Reboot"]),
 ("Words along the bottom of the screen translating the dialogue", "Subtitles", ["Voiceover", "Storyboard", "Script"]),
 ("Replacing the actors' voices with another language", "Dubbing", ["Montage", "Cutaway", "Outtake"]),
 ("The list of names that rolls at the end", "Credits", ["Programme", "Libretto", "Script"]),
 ("A longer version of the film, the way its maker wanted it", "Director's cut", ["Outtake", "Montage", "Cutaway"]),
 ("Wear these to make things leap off the screen", "3D glasses", ["Opera glasses", "Binoculars", "Monocle"]),
 ("A big cinema with lots of screens", "Multiplex", ["Drive-in", "Art house", "Picture palace"]),
 ("Help yourself to sweets by the scoop", "Pick 'n' mix", ["Choc ice", "Candyfloss", "Toffee apples"]),
 ("The rating, like PG or 15, saying who can watch", "Certificate", ["Ticket stub", "Programme", "Script"]),
 ("Where the stars pose for the photographers on the big night", "Red carpet", ["Green room", "Dressing room", "Stage door"]),
 ("A film that loses money because nobody goes to see it", "Flop", ["Sleeper hit", "Cult classic", "B-movie"]),
 ("A film telling the true life story of a real person", "Biopic", ["Rom-com", "Whodunnit", "Western"]),
 ("A new version of an old film", "Remake", ["Spin-off", "Prequel", "Parody"])])

race("who's this sports official?", "Sport", "medium", ["sport", "officials", "referees"], [
 ("Runs a football match and blows the whistle", "Referee", ["Coach", "Captain", "Physio"]),
 ("Gives a cricket batter out with a raised finger", "Umpire", ["Coach", "Selector", "Groundsman"]),
 ("Runs the touchline with a flag for offside", "Linesman", ["Kit man", "Physio", "Ball boy"]),
 ("Holds up the board showing the added time", "Fourth official", ["Kit man", "Physio", "Mascot"]),
 ("Fires the gun to begin a race", "Starter", ["Pacemaker", "Coach", "Selector"]),
 ("Waves the flags around the circuit at a motor race", "Marshal", ["Mascot", "Pundit", "Groundsman"]),
 ("Rings the bell at the end of each boxing round", "Timekeeper", ["Coach", "Pundit", "Physio"]),
 ("Calls whether a tennis ball has landed in or out on a line", "Line judge", ["Ball boy", "Coach", "Pundit"]),
 ("Watches the TV replays to settle run-outs in cricket", "Third umpire", ["Selector", "Groundsman", "Commentator"]),
 ("Rugby's video referee, who checks whether a try was grounded", "Television match official", ["Commentator", "Pundit", "Selector"]),
 ("Settles disputes at a chess tournament", "Arbiter", ["Coach", "Captain", "Commentator"]),
 ("Runs a racecourse on the day of a horse race", "Clerk of the course", ["Groundsman", "Selector", "Pundit"]),
 ("Keeps the book of runs in a cricket match", "Scorer", ["Selector", "Groundsman", "Kit man"]),
 ("Sits up high and calls the score at Wimbledon", "Chair umpire", ["Ball boy", "Commentator", "Coach"]),
 ("The video team that reviews goals and red cards in football", "VAR", ["Kit man", "Pundit", "Commentator"]),
 ("Score a boxing bout on points from ringside", "Judges", ["Seconds", "Cutmen", "Promoters"]),
 ("Announces 'One hundred and eighty!' at the darts", "Caller", ["Commentator", "Pundit", "Mascot"]),
 ("Investigates incidents and hands out penalties in Formula One", "Stewards", ["Pit crew", "Engineers", "Mechanics"]),
 ("Rugby's flag-waving official on the touchline, by its traditional name", "Touch judge", ["Kit man", "Physio", "Ball boy"]),
 ("Checks every runner crosses the line, and in what order", "Finish judge", ["Pacemaker", "Coach", "Physio"])])

race("what's this ice cream word?", "Food and drink", "easy", ["ice cream", "desserts", "seaside"], [
 ("The crispy cone your ice cream sits in", "Cornet", ["Ramekin", "Tumbler", "Goblet"]),
 ("A flat, crisp biscuit sandwiching a slab of ice cream", "Wafer", ["Shortbread", "Digestive", "Brandy snap"]),
 ("The crumbly chocolate stick pushed into a cone", "Flake", ["Twix", "Curly Wurly", "Wispa"]),
 ("A whippy cone with a chocolate stick pushed in", "99", ["Calippo", "Feast", "Magnum"]),
 ("Scoops in a tall glass with sauce, nuts and a cherry on top", "Sundae", ["Trifle", "Syllabub", "Fool"]),
 ("A dairy-free frozen fruit ice", "Sorbet", ["Frozen yoghurt", "Kulfi", "Blancmange"]),
 ("Italy's dense, silky ice cream", "Gelato", ["Kulfi", "Frozen yoghurt", "Panna cotta"]),
 ("Layers of ice cream, fruit and cream in a very tall glass, with a long spoon", "Knickerbocker glory", ["Trifle", "Eton mess", "Syllabub"]),
 ("Ice cream between the two halves of a banana", "Banana split", ["Eton mess", "Pavlova", "Profiterole"]),
 ("A block of vanilla ice cream coated in chocolate, with no stick", "Choc ice", ["Magnum", "Feast", "Calippo"]),
 ("A plastic cone of ice cream with a bubblegum ball at the bottom", "Screwball", ["Calippo", "Feast", "Magnum"]),
 ("Soft-serve ice cream from the van", "Mr Whippy", ["Milkshake", "Slush", "Ice pop"]),
 ("The North East name for the bright red raspberry sauce on a 99", "Monkey blood", ["Butterscotch", "Chocolate sauce", "Toffee sauce"]),
 ("Tiny coloured sugar strands scattered on top", "Sprinkles", ["Butterscotch", "Toffee sauce", "Chocolate sauce"]),
 ("Strawberry, vanilla and chocolate side by side in one block", "Neapolitan", ["Tutti frutti", "Rum and raisin", "Mint choc chip"]),
 ("Sponge rolled round a log of ice cream, a 1980s pudding favourite", "Arctic roll", ["Baked Alaska", "Swiss roll", "Yule log"]),
 ("A scoop of vanilla drowned in hot espresso", "Affogato", ["Panna cotta", "Crème brûlée", "Profiterole"]),
 ("A big, crunchy cone with a criss-cross pattern", "Waffle cone", ["Ramekin", "Tumbler", "Goblet"]),
 ("Vanilla ice cream swirled with streaks of red fruit sauce", "Raspberry ripple", ["Tutti frutti", "Rum and raisin", "Mint choc chip"]),
 ("The rounded ball of ice cream, and the tool that makes it", "Scoop", ["Wedge", "Slab", "Brick"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-150.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
