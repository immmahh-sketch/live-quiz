# Bank session 10 Oct 2026: 2 more general races -> bank/race-74.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Abbey'?", "Britain", "hard", ["abbeys", "wordplay"], [
 ("Julian Fellowes's drama about the Crawley family", "Downton", ["Highclere", "Gosford", "Brideshead"]), ("Where English monarchs are crowned", "Westminster", ["St Albans", "Winchester", "Canterbury"]),
 ("Jane Austen's gothic spoof starring Catherine Morland", "Northanger", ["Mansfield", "Udolpho", "Sanditon"]), ("The abbey with angels climbing ladders on its front, beside the Roman Baths", "Bath", ["Wells", "Bristol", "Sherborne"]),
 ("The clifftop ruin that inspired Bram Stoker's Dracula", "Whitby", ["Lindisfarne", "Tynemouth", "Scarborough"]), ("The Wye Valley ruin of Wordsworth's poem", "Tintern", ["Neath", "Valle Crucis", "Llanthony"]),
 ("Yorkshire's great Cistercian ruin beside Studley Royal", "Fountains", ["Rievaulx", "Byland", "Jervaulx"]), ("The Northumberland abbey with St Wilfrid's 7th-century crypt", "Hexham", ["Lindisfarne", "Brinkburn", "Tynemouth"]),
 ("The Duke of Bedford's home, with its safari park", "Woburn", ["Longleat", "Wilton", "Knebworth"]), ("The Somerset abbey where monks claimed to find King Arthur's grave", "Glastonbury", ["Wells", "Muchelney", "Cleeve"]),
 ("The Borders abbey where Robert the Bruce's heart is buried", "Melrose", ["Dryburgh", "Jedburgh", "Kelso"]), ("The Devon abbey whose monks make a famous tonic wine", "Buckfast", ["Buckland", "Tavistock", "Torre"]),
 ("The Wiltshire abbey of Hogwarts corridors and Fox Talbot's first photo", "Lacock", ["Wilton", "Stanley", "Bradenstoke"]), ("The Sussex abbey built where the Battle of Hastings was fought", "Battle", ["Hastings", "Pevensey", "Lewes"]),
 ("The Hebridean abbey founded by St Columba", "Iona", ["Mull", "Skye", "Lindisfarne"]), ("Home of Brother Cadfael, Ellis Peters's monk detective", "Shrewsbury", ["Ludlow", "Chester", "Tewkesbury"]),
 ("The Hampshire abbey where Lord Mountbatten is buried", "Romsey", ["Beaulieu", "Netley", "Winchester"]), ("Connemara's castle-like abbey on a lake", "Kylemore", ["Clonmacnoise", "Glendalough", "Mount Melleray"]),
 ("The Italian hilltop abbey destroyed in a 1944 battle", "Monte Cassino", ["Subiaco", "San Galgano", "Assisi"]), ("The Wiltshire abbey where a monk tried to fly from the tower around 1010", "Malmesbury", ["Sherborne", "Tewkesbury", "Pershore"])])

race("which famous 'Head'?", "General knowledge", "hard", ["heads", "wordplay"], [
 ("Britain's highest chalk sea cliff, in Sussex", "Beachy Head", ["Seven Sisters", "Birling Gap", "Old Harry Rocks"]), ("The great chalk headland on the Yorkshire coast near Bridlington", "Flamborough Head", ["Filey Brigg", "Ravenscar", "Saltburn"]),
 ("Hawaii's volcanic crater above Waikiki", "Diamond Head", ["Pearl Harbor", "Haleakalā", "Mauna Kea"]), ("The real north-east tip of mainland Britain, near John o' Groats", "Duncansby Head", ["Dunnet Head", "Cape Wrath", "Noss Head"]),
 ("The Toy Story toy with a face you can rearrange", "Mr Potato Head", ["Mr Tomato Head", "Mr Turnip Head", "Mr Pumpkin Head"]), ("The Oxford band behind OK Computer", "Radiohead", ["Supergrass", "Foals", "Ride"]),
 ("Lemmy's heavy metal band", "Motörhead", ["Saxon", "Venom", "Hawkwind"]), ("David Byrne's band", "Talking Heads", ["Television", "Blondie", "Ramones"]),
 ("Beavis's cartoon sidekick on MTV", "Butt-Head", ["Stimpy", "Daria", "Bart"]), ("The South Carolina golf island resort", "Hilton Head", ["Kiawah", "Myrtle Beach", "Amelia"]),
 ("Yorkshire's thin shingle spit at the mouth of the Humber", "Spurn Head", ["Blakeney Point", "Orford Ness", "Dungeness"]), ("The Cumbrian cliffs where the Coast to Coast walk begins", "St Bees Head", ["Robin Hood's Bay", "Maryport", "Silloth"]),
 ("Llandudno's limestone headland, with its tramway", "Great Orme's Head", ["Little Orme's Head", "Penmon Point", "Rhossili"]), ("The wooden carving on a ship's bow", "Figurehead", ["Bowsprit", "Masthead", "Prow"]),
 ("A brainy, bookish person", "Egghead", ["Bighead", "Blockhead", "Bonehead"]), ("A scatterbrained person, and a chewy American sweet", "Airhead", ["Bighead", "Redhead", "Skinhead"]),
 ("Someone with a quick temper", "Hothead", ["Bighead", "Redhead", "Skinhead"]), ("A devoted fan of the Grateful Dead", "Deadhead", ["Deadbeat", "Dead Ringer", "Deadeye"]),
 ("The seabird cliffs of the Scottish Borders near Eyemouth", "St Abb's Head", ["Fast Castle", "Dunbar", "Eyemouth"]), ("The explosive tip of a missile", "Warhead", ["Payload", "Detonator", "Fuse"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-74.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
