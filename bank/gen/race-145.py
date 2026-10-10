# Bank session 10 Oct 2026: 3 more general races -> bank/race-145.json (Christmas words, pirate words, horse and riding words). 20 rows each, target 10; wrong options are
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

race("what's this Christmas word?", "Christmas", "easy", ["Christmas", "words"], [
 ("Open a little door each day in December", "Advent calendar", ["Lantern", "Bunting", "Piñata"]),
 ("Glittery strands draped round the tree", "Tinsel", ["Bunting", "Streamer", "Sparkler"]),
 ("A shiny ball hung on the tree", "Bauble", ["Lantern", "Piñata", "Sparkler"]),
 ("Kiss under it", "Mistletoe", ["Poinsettia", "Amaryllis", "Ivy"]),
 ("Prickly leaves with bright red berries", "Holly", ["Poinsettia", "Amaryllis", "Ivy"]),
 ("A ring of greenery hung on the front door", "Wreath", ["Bunting", "Lantern", "Piñata"]),
 ("The school play with Mary, Joseph, shepherds and a tea towel on every head", "Nativity", ["Masque", "Mummers' play", "Passion play"]),
 ("Hung at the end of the bed for Father Christmas to fill", "Stocking", ["Piñata", "Lantern", "Bunting"]),
 ("Pulled with a bang, hiding a paper hat and a bad joke", "Cracker", ["Sparkler", "Piñata", "Streamer"]),
 ("A chocolate sponge roll decorated to look like a piece of wood", "Yule log", ["Stollen", "Panettone", "Simnel cake"]),
 ("A little pastry case of dried fruit and spices", "Mince pie", ["Stollen", "Panettone", "Simnel cake"]),
 ("The 26th of December", "Boxing Day", ["Candlemas", "Michaelmas", "Lammas"]),
 ("'Oh no it isn't!' Theatre with a dame and a principal boy", "Panto", ["Masque", "Passion play", "Mummers' play"]),
 ("Going door to door singing and drinking toasts, an old English custom", "Wassailing", ["Morris dancing", "Maypole dancing", "Beating the bounds"]),
 ("The evening of 5 January, when the decorations should come down", "Twelfth Night", ["Candlemas", "Michaelmas", "Lammas"]),
 ("A box of chocolate bars given to children", "Selection box", ["Piñata", "Stollen", "Lantern"]),
 ("Pulling a name out of a hat and buying that person a present", "Secret Santa", ["Lucky dip", "Tombola", "Raffle"]),
 ("The 24th of December", "Christmas Eve", ["Candlemas", "Michaelmas", "Lammas"]),
 ("6 January, when the Three Kings reached Bethlehem", "Epiphany", ["Candlemas", "Michaelmas", "Lammas"]),
 ("A sweet, boozy spread served with Christmas pudding", "Brandy butter", ["Clotted cream", "Lemon curd", "Marmalade"])])

race("what's this pirate word?", "History", "easy", ["pirates", "words"], [
 ("The skull-and-crossbones flag", "Jolly Roger", ["Ensign", "Pennant", "Burgee"]),
 ("A Spanish gold coin, the pirate's prize", "Doubloon", ["Ducat", "Guinea", "Sovereign"]),
 ("Spanish silver dollars, squawked about by Long John Silver's parrot", "Pieces of eight", ["Ducats", "Guineas", "Sovereigns"]),
 ("Forced off the side of the ship, blindfolded, into the sea", "Walk the plank", ["Keelhaul", "Run the gauntlet", "Flogging"]),
 ("The lookout platform high up the mast", "Crow's nest", ["Poop deck", "Bilge", "Hold"]),
 ("A short, curved sword", "Cutlass", ["Musket", "Blunderbuss", "Flintlock"]),
 ("Worn over a missing eye", "Eye patch", ["Spyglass", "Sextant", "Tricorn hat"]),
 ("X marks the spot", "Treasure map", ["Sextant", "Spyglass", "Logbook"]),
 ("A Caribbean pirate of the 1600s", "Buccaneer", ["Bosun", "Quartermaster", "Purser"]),
 ("The treasure a pirate crew shares out", "Booty", ["Bilge", "Ballast", "Rigging"]),
 ("The disease sailors got without fruit and vitamin C", "Scurvy", ["Rickets", "Beriberi", "Gout"]),
 ("Rum watered down for sailors", "Grog", ["Hardtack", "Ship's biscuit", "Bilge"]),
 ("A pirate's insult for someone who doesn't know the sea", "Landlubber", ["Bosun", "Purser", "Quartermaster"]),
 ("The bottom of the sea, where drowned sailors end up", "Davy Jones' locker", ["Brig", "Hold", "Bilge"]),
 ("When the crew rise up against their captain", "Mutiny", ["Keelhaul", "Flogging", "Run the gauntlet"]),
 ("Left alone on a desert island as a punishment", "Marooned", ["Keelhauled", "Flogged", "Press-ganged"]),
 ("A pirate's cry of shock", "Shiver me timbers", ["Ahoy", "Avast", "Yo-ho-ho"]),
 ("In 'Treasure Island', the mark handed to a pirate who's to be killed", "Black Spot", ["Ensign", "Pennant", "Burgee"]),
 ("Perched on Long John Silver's shoulder", "Parrot", ["Monkey", "Mynah bird", "Albatross"]),
 ("The youngest member of the crew, running errands", "Cabin boy", ["Bosun", "Purser", "Quartermaster"])])

race("what's this horse word?", "Animals", "medium", ["horses", "riding", "words"], [
 ("A baby horse", "Foal", ["Cob", "Hack", "Hunter"]),
 ("The unit a horse's height is measured in", "Hand", ["Stride", "Cubit", "Span"]),
 ("Headgear with the bit and reins, for steering", "Bridle", ["Halter", "Girth", "Crupper"]),
 ("The seat strapped onto the horse's back", "Saddle", ["Numnah", "Girth", "Surcingle"]),
 ("The footrest hanging from each side of the saddle", "Stirrup", ["Girth", "Crupper", "Numnah"]),
 ("The straps the rider holds to steer", "Reins", ["Halter", "Girth", "Crupper"]),
 ("The metal bar in the horse's mouth", "Bit", ["Hackamore", "Girth", "Crupper"]),
 ("The person who fits the horseshoes", "Farrier", ["Groom", "Ostler", "Jockey"]),
 ("'Horse ballet': precise movements judged for elegance", "Dressage", ["Eventing", "Hacking", "Point-to-point"]),
 ("A fun day of mounted races and games for young riders", "Gymkhana", ["Eventing", "Point-to-point", "Hacking"]),
 ("The long hair along a horse's neck", "Mane", ["Forelock", "Fetlock", "Pastern"]),
 ("The hard foot a horse stands on", "Hoof", ["Fetlock", "Pastern", "Withers"]),
 ("The vehicle that takes horses to shows", "Horsebox", ["Tack room", "Paddock", "Livery"]),
 ("Riding without a saddle", "Bareback", ["Side-saddle", "Hacking", "Eventing"]),
 ("A grey coat marked with darker rings", "Dapple grey", ["Palomino", "Piebald", "Skewbald"]),
 ("A small, tough pony from the Scottish islands", "Shetland", ["Cob", "Thoroughbred", "Palomino"]),
 ("Cleaning out the stable's dirty bedding", "Mucking out", ["Hacking", "Grooming", "Tacking up"]),
 ("A strap that stops a horse throwing its head up too high", "Martingale", ["Crupper", "Surcingle", "Numnah"]),
 ("A string bag of hay hung up for the horse to munch", "Hay net", ["Numnah", "Tack room", "Girth"]),
 ("Nailed onto the hoof, and hung up for luck", "Horseshoe", ["Crupper", "Girth", "Numnah"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-145.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
