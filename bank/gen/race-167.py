# Bank session 11 Oct 2026: 3 more general races -> bank/race-167.json (Formula One, skateboarding and seafood words). 20 rows each, target 10; wrong options are
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

race("what's this Formula One word?", "Sport", "medium", ["Formula One", "motor racing", "words"], [
 ("When the car dives in for new tyres", "Pit stop", ["Pit pony", "Pit bull", "Pitfall"]),
 ("The road past the garages, with a speed limit", "Pit lane", ["Slip road", "Hard shoulder", "Bus lane"]),
 ("Where the team bosses sit watching screens", "Pit wall", ["Sea wall", "Firewall", "Paywall"]),
 ("Starting first on the grid", "Pole position", ["Pole vault", "Pole dance", "North Pole"]),
 ("Waved as the winner crosses the line", "Chequered flag", ["Black flag", "White flag", "Green flag"]),
 ("The flag that stops the race completely", "Red flag", ["Black flag", "White flag", "Green flag"]),
 ("Danger ahead: slow down and no overtaking", "Yellow flag", ["Black flag", "White flag", "Green flag"]),
 ("Let the faster car that's lapping you go by", "Blue flag", ["Black flag", "White flag", "Green flag"]),
 ("Leads the field slowly round after a crash", "Safety car", ["Pace setter", "Tow truck", "Course car"]),
 ("The rear-wing flap that opens to help overtaking, by its initials", "DRS", ["KERS", "ERS", "ABS"]),
 ("Tyres with no tread, for dry weather", "Slicks", ["Retreads", "Remoulds", "Radials"]),
 ("Where the cars line up at the start", "Grid", ["Kerb", "Gravel trap", "Run-off"]),
 ("The VIP area behind the garages", "Paddock", ["Grandstand", "Tribune", "Terrace"]),
 ("The title won by the team rather than the driver", "Constructors' Championship", ["Drivers' Championship", "Nations Cup", "Team Trophy"]),
 ("The street race round a tiny principality's harbour", "Monaco", ["Monza", "Spa", "Baku"]),
 ("The home of the British Grand Prix", "Silverstone", ["Brands Hatch", "Donington", "Goodwood"]),
 ("Pitting before your rival to get ahead on fresh tyres", "Undercut", ["Overcut", "Uppercut", "Shortcut"]),
 ("The rules stopping teams changing the car after qualifying", "Parc fermé", ["Carte blanche", "Faux pas", "Coup d'état"]),
 ("Held a sign in front of the car at old-style pit stops", "Lollipop man", ["Flag marshal", "Pit boss", "Ice cream man"]),
 ("Where the top three spray the champagne", "Podium", ["Pulpit", "Plinth", "Balcony"])])

race("what's this skateboarding word?", "Sport", "medium", ["skateboarding", "skate parks", "words"], [
 ("Jumping with the board without using your hands", "Ollie", ["Wheelie", "Bunny hop", "Hopscotch"]),
 ("Spinning the board under your feet with a flick of the toe", "Kickflip", ["Backflip", "Somersault", "Cartwheel"]),
 ("Rolling along on just the back two wheels", "Manual", ["Automatic", "Handbook", "Handbrake"]),
 ("A U-shaped ramp", "Half-pipe", ["Quarter pipe", "Drainpipe", "Bagpipe"]),
 ("Sliding along a rail on the board's metal axles", "Grind", ["Grate", "Grime", "Groan"]),
 ("The metal axles holding the wheels", "Trucks", ["Lorries", "Vans", "Wagons"]),
 ("The wooden board you stand on", "Deck", ["Hull", "Bench", "Shelf"]),
 ("The sandpapery sheet on top for grip", "Grip tape", ["Duct tape", "Red tape", "Ticker tape"]),
 ("The legend who landed the first 900", "Tony Hawk", ["Rodney Mullen", "Bam Margera", "Shaun White"]),
 ("The British teenager who won Olympic bronze in 2021, aged 13", "Sky Brown", ["Bethany Shriever", "Keely Hodgkinson", "Emma Raducanu"]),
 ("A concrete playground of ramps and bowls", "Skate park", ["Car park", "Theme park", "Business park"]),
 ("A deep, rounded dip like an empty pool", "Bowl", ["Basin", "Trough", "Crater"]),
 ("Jumping off the board when a trick goes wrong", "Bail", ["Bow out", "Opt out", "Sign off"]),
 ("Skating on stairs, rails and benches around town", "Street", ["Park", "Vert", "Freestyle"]),
 ("Little steel balls inside the wheels", "Bearings", ["Marbles", "Pellets", "Beads"]),
 ("The front end of the board", "Nose", ["Bow", "Prow", "Snout"]),
 ("The back end, kicked down for an ollie", "Tail", ["Stern", "Rump", "Heel"]),
 ("Riding with your left foot forward", "Regular", ["Goofy", "Fakie", "Switch"]),
 ("The PlayStation game series that began in 1999", "Tony Hawk's Pro Skater", ["SSX", "Skate", "Grind Session"]),
 ("The famous skateboarding magazine with the flame logo", "Thrasher", ["Kerrang!", "Smash Hits", "The Face"])])

race("what's this seafood word?", "Food and drink", "medium", ["seafood", "fish", "words"], [
 ("Breaded langoustine tails", "Scampi", ["Croquettes", "Goujons", "Nuggets"]),
 ("Rings of fried squid", "Calamari", ["Onion rings", "Hoops", "Fritters"]),
 ("Tiny whole fish, deep-fried", "Whitebait", ["Crispy seaweed", "Scratchings", "Croutons"]),
 ("Split, smoked herring for breakfast", "Kippers", ["Arbroath smokies", "Finnan haddie", "Gravlax"]),
 ("The 1970s starter with Marie Rose sauce", "Prawn cocktail", ["Prawn toast", "Prawn crackers", "Fish cocktail"]),
 ("Lobster baked in a creamy, mustardy sauce", "Lobster Thermidor", ["Lobster bisque", "Lobster roll", "Lobster pot"]),
 ("Shellfish swallowed raw, famously from Whitstable", "Oysters", ["Cockles", "Whelks", "Winkles"]),
 ("Shellfish served as moules marinière", "Mussels", ["Clams", "Scallops", "Razor clams"]),
 ("Its 'dressed' meat is famous from Cromer", "Crab", ["Lobster", "Crayfish", "Langoustine"]),
 ("Cod in breadcrumbs, made famous by Birds Eye", "Fish finger", ["Goujon", "Fish ball", "Fish slice"]),
 ("Flaked fish mixed with mash and fried", "Fish cake", ["Fish pie", "Fish ball", "Fish slice"]),
 ("Rice with smoked haddock and egg, a breakfast from the Raj", "Kedgeree", ["Paella", "Risotto", "Biryani"]),
 ("Expensive salted fish eggs", "Caviar", ["Taramasalata", "Tapenade", "Pâté"]),
 ("Japanese vinegared rice topped with raw fish", "Sushi", ["Sashimi", "Tempura", "Teriyaki"]),
 ("Pink slices on a bagel with cream cheese", "Smoked salmon", ["Gravlax", "Ham", "Pastrami"]),
 ("The East End dish served cold in jelly", "Jellied eels", ["Pie and mash", "Whelks", "Faggots"]),
 ("Wrapped in paper, with salt and vinegar", "Fish and chips", ["Pie and peas", "Bangers and mash", "Bubble and squeak"]),
 ("Many northerners' chippy favourite, ahead of cod", "Haddock", ["Plaice", "Pollock", "Hake"]),
 ("The shop or person selling fresh fish", "Fishmonger", ["Ironmonger", "Costermonger", "Cheesemonger"]),
 ("Steak and lobster on one plate", "Surf and turf", ["Bed and breakfast", "Rock and roll", "Fish and fowl"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-167.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
