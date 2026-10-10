# Bank session 10 Oct 2026: 2 more general races -> bank/race-80.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Water'?", "General knowledge", "medium", ["water", "wordplay"], [
 ("Napoleon's final defeat, in 1815", "Waterloo", ["Austerlitz", "Leipzig", "Wagram"]), ("Deep Purple's riff about a fire at Montreux", "Smoke on the Water", ["Highway Star", "Black Night", "Child in Time"]),
 ("Simon & Garfunkel's 1970 hit", "Bridge over Troubled Water", ["The Sound of Silence", "Mrs. Robinson", "The Boxer"]), ("Handel's suite for George I's barge trip on the Thames", "Water Music", ["Music for the Royal Fireworks", "Messiah", "Zadok the Priest"]),
 ("Kevin Costner's 1995 flop set on a flooded Earth", "Waterworld", ["The Postman", "Dances with Wolves", "Robin Hood: Prince of Thieves"]), ("Guillermo del Toro's Best Picture winner", "The Shape of Water", ["Pan's Labyrinth", "The Favourite", "Green Book"]),
 ("Richard Adams's 1972 novel about rabbits", "Watership Down", ["Tarka the Otter", "The Plague Dogs", "The Animals of Farthing Wood"]), ("Charles Kingsley's tale of Tom the chimney sweep", "The Water-Babies", ["The Wind in the Willows", "Black Beauty", "The Secret Garden"]),
 ("Water made with deuterium, used in nuclear reactors", "Heavy water", ["Dense water", "Deep water", "Salt water"]), ("Water full of calcium that furs up your kettle", "Hard water", ["Soft water", "Mineral water", "Tap water"]),
 ("The fizzy mixer flavoured with quinine", "Tonic water", ["Soda water", "Ginger ale", "Bitter lemon"]), ("England's deepest lake", "Wastwater", ["Windermere", "Haweswater", "Ennerdale Water"]),
 ("Where Donald Campbell died in Bluebird K7 in 1967", "Coniston Water", ["Windermere", "Ullswater", "Loch Ness"]), ("England's biggest reservoir by area, in the East Midlands", "Rutland Water", ["Kielder Water", "Grafham Water", "Carsington Water"]),
 ("The ball game played in a swimming pool", "Water polo", ["Underwater rugby", "Aquathlon", "Canoe polo"]), ("What a priest uses at a baptism", "Holy water", ["Chrism", "Spring water", "Myrrh"]),
 ("The fragrant flavouring in Turkish delight", "Rose water", ["Vanilla", "Almond", "Mint"]), ("The band behind 'The Whole of the Moon'", "The Waterboys", ["The Proclaimers", "Simple Minds", "Big Country"]),
 ("Edinburgh's own river", "Water of Leith", ["River Almond", "River Esk", "Union Canal"]), ("The Irish city famous for its crystal", "Waterford", ["Wexford", "Tipperary", "Galway"])])

race("which famous 'Horse'?", "General knowledge", "medium", ["horses", "wordplay"], [
 ("The Greeks' wooden trick at Troy", "Trojan Horse", ["Greek Horse", "Spartan Bull", "Athenian Ox"]), ("An unexpected contender", "Dark horse", ["Black sheep", "Lame duck", "White elephant"]),
 ("Michael Morpurgo's novel about Joey", "War Horse", ["Private Peaceful", "Kensuke's Kingdom", "Born to Run"]), ("Britain's oldest chalk hill figure, in Oxfordshire", "The Uffington White Horse", ["The Long Man of Wilmington", "The Cerne Abbas Giant", "The Westbury White Horse"]),
 ("A pet subject someone keeps going on about", "Hobby horse", ["Soapbox", "Pet hate", "Party piece"]), ("A folding frame for drying laundry", "Clothes horse", ["Washing line", "Mangle", "Peg bag"]),
 ("An American name for a sudden cramp in the leg", "Charley horse", ["Dead leg", "Pins and needles", "Stitch"]), ("What you get on when you act all superior", "High horse", ["High chair", "High road", "High ground"]),
 ("Never look one in the mouth", "Gift horse", ["Pack horse", "Cart horse", "Old nag"]), ("The Lakota leader at Little Bighorn", "Crazy Horse", ["Sitting Bull", "Red Cloud", "Geronimo"]),
 ("Agatha Christie's novel about a sinister former pub", "The Pale Horse", ["The Mirror Crack'd", "Endless Night", "Crooked House"]), ("America's 1971 song about the desert", "A Horse with No Name", ["Ventura Highway", "Sister Golden Hair", "Tin Man"]),
 ("The Rolling Stones' 1971 ballad", "Wild Horses", ["Angie", "Ruby Tuesday", "Beast of Burden"]), ("The upright fish with a horse-like head", "Seahorse", ["Clownfish", "Angelfish", "Swordfish"]),
 ("The old unit of engine power", "Horsepower", ["Kilowatt", "Torque", "Brake force"]), ("The hot root sauce served with roast beef", "Horseradish", ["Mustard", "Wasabi", "Mint sauce"]),
 ("Where Trooping the Colour takes place", "Horse Guards Parade", ["The Mall", "Wellington Barracks", "St James's Park"]), ("The lucky charm hung above a door", "Horseshoe", ["Four-leaf clover", "Rabbit's foot", "Wishbone"]),
 ("A tireless, reliable machine or person", "Workhorse", ["Dogsbody", "Gofer", "Jobsworth"]), ("A candidate who stands to test the water for someone else", "Stalking horse", ["Straw man", "Sacrificial lamb", "Red herring"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-80.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
