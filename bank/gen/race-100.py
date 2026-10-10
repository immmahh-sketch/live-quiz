# Bank session 10 Oct 2026: 2 more general races -> bank/race-100.json (film taglines, kitchen tools). 20 rows each, target 10; wrong options are
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

race("which film had this tagline?", "Film", "medium", ["films", "taglines", "posters"], [
 ("In space no one can hear you scream", "Alien", ["Predator", "The Thing", "Event Horizon"]),
 ("You'll believe a man can fly", "Superman", ["Batman", "Flash Gordon", "The Rocketeer"]),
 ("Just when you thought it was safe to go back in the water", "Jaws 2", ["Piranha", "Orca", "Deep Blue Sea"]),
 ("Who you gonna call?", "Ghostbusters", ["Gremlins", "Beetlejuice", "The Goonies"]),
 ("Be afraid. Be very afraid.", "The Fly", ["Scream", "The Thing", "Hellraiser"]),
 ("The night HE came home", "Halloween", ["Friday the 13th", "A Nightmare on Elm Street", "Scream"]),
 ("An adventure 65 million years in the making", "Jurassic Park", ["King Kong", "Land of the Lost", "Mighty Joe Young"]),
 ("Collide with destiny", "Titanic", ["Pearl Harbor", "Poseidon", "Deep Impact"]),
 ("The true story of a real fake", "Catch Me If You Can", ["The Wolf of Wall Street", "American Hustle", "Ocean's Eleven"]),
 ("Don't get mad. Get everything.", "The First Wives Club", ["Thelma & Louise", "9 to 5", "Working Girl"]),
 ("Earth. It was fun while it lasted.", "Armageddon", ["Deep Impact", "Independence Day", "2012"]),
 ("Houston, we have a problem.", "Apollo 13", ["Gravity", "The Right Stuff", "First Man"]),
 ("Every man dies. Not every man really lives.", "Braveheart", ["Gladiator", "Rob Roy", "Troy"]),
 ("A long time ago in a galaxy far, far away...", "Star Wars", ["Star Trek", "Dune", "Flash Gordon"]),
 ("On every street in every city, there's a nobody who dreams of being a somebody", "Taxi Driver", ["Rocky", "Mean Streets", "Raging Bull"]),
 ("Fear can hold you prisoner. Hope can set you free.", "The Shawshank Redemption", ["The Green Mile", "Escape from Alcatraz", "Cool Hand Luke"]),
 ("Size does matter", "Godzilla", ["Cloverfield", "Pacific Rim", "King Kong"]),
 ("Love means never having to say you're sorry", "Love Story", ["Ghost", "The Notebook", "Dirty Dancing"]),
 ("They're here.", "Poltergeist", ["The Exorcist", "The Amityville Horror", "The Shining"]),
 ("The first casualty of war is innocence", "Platoon", ["Full Metal Jacket", "Apocalypse Now", "Born on the Fourth of July"])])

race("which kitchen tool is this?", "Food and drink", "easy", ["kitchen", "cooking"], [
 ("Bowl full of holes for draining boiled pasta", "Colander", ["Salad spinner", "Steamer", "Funnel"]),
 ("Fine mesh for sifting flour", "Sieve", ["Funnel", "Salad spinner", "Slotted spoon"]),
 ("Loops of wire for beating air into cream", "Whisk", ["Potato masher", "Muddler", "Fish slice"]),
 ("Flexible rubber blade for scraping the last of the mix from a bowl", "Spatula", ["Fish slice", "Slotted spoon", "Muddler"]),
 ("Deep long-handled spoon for serving soup", "Ladle", ["Slotted spoon", "Melon baller", "Funnel"]),
 ("Metal box with sharp-edged holes for cheese", "Grater", ["Egg slicer", "Cleaver", "Apple corer"]),
 ("Wooden cylinder for flattening pastry", "Rolling pin", ["Potato masher", "Muddler", "Trivet"]),
 ("Bowl and club for grinding spices by hand", "Pestle and mortar", ["Potato masher", "Muddler", "Nutcracker"]),
 ("Flat frame with a blade for wafer-thin slices", "Mandoline", ["Egg slicer", "Cleaver", "Pizza cutter"]),
 ("Little tool for scraping fine strips of citrus peel", "Zester", ["Apple corer", "Melon baller", "Egg slicer"]),
 ("Hinged grabbers for turning sausages", "Tongs", ["Nutcracker", "Fish slice", "Trivet"]),
 ("Swivel blade for taking the skin off a potato", "Peeler", ["Apple corer", "Cleaver", "Egg slicer"]),
 ("Turn its handle to cut round the top of a can", "Tin opener", ["Nutcracker", "Apple corer", "Bottle opener"]),
 ("Squeezes a clove through tiny holes", "Garlic press", ["Nutcracker", "Potato ricer", "Egg slicer"]),
 ("Metal spiral for getting into a bottle of wine", "Corkscrew", ["Bottle opener", "Muddler", "Nutcracker"]),
 ("Glass jug with a plunger for coffee", "Cafetière", ["Percolator", "Teapot", "Moka pot"]),
 ("Long thin spike for kebabs", "Skewer", ["Fondue fork", "Cocktail stick", "Meat thermometer"]),
 ("Rubber bulb and tube for squirting juices over the roast", "Baster", ["Funnel", "Meat thermometer", "Pipette"]),
 ("Used to glaze a pie with beaten egg", "Pastry brush", ["Piping bag", "Pastry cutter", "Muddler"]),
 ("Scottish wooden stick for stirring porridge", "Spurtle", ["Muddler", "Swizzle stick", "Dibber"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-100.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
