# Bank session 11 Oct 2026: 3 more general races -> bank/race-185.json (Star Wars, Bible and Lord of the Rings words). 20 rows each, target 10; wrong options are
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

race("what's this Star Wars word?", "Film", "medium", ["Star Wars", "sci-fi", "words"], [
 ("The energy field that binds the galaxy together", "The Force", ["The Spark", "The Flow", "The Light"]),
 ("A Jedi's glowing sword", "Lightsaber", ["Phaser", "Sonic screwdriver", "Beam sword"]),
 ("A Star Wars laser gun", "Blaster", ["Phaser", "Ray gun", "Proton pack"]),
 ("The order of peacekeeping warrior monks", "Jedi", ["Klingons", "Templars", "Samurai"]),
 ("Followers of the dark side, always two at a time", "Sith", ["Borg", "Daleks", "Nazgûl"]),
 ("A Jedi apprentice", "Padawan", ["Squire", "Cadet", "Page"]),
 ("Chewbacca's species", "Wookiee", ["Gungan", "Hutt", "Rodian"]),
 ("Furry little warriors on the forest moon of Endor", "Ewoks", ["Jawas", "Gungans", "Porgs"]),
 ("The moon-sized battle station", "Death Star", ["Starkiller Base", "Borg Cube", "Mothership"]),
 ("Han Solo's battered ship", "Millennium Falcon", ["Slave I", "Serenity", "Enterprise"]),
 ("The Rebel fighter Luke flies against the Death Star", "X-wing", ["Y-wing", "A-wing", "B-wing"]),
 ("The Empire's standard fighter, with its scream", "TIE fighter", ["Star Destroyer", "AT-AT", "Speeder bike"]),
 ("The Empire's white-armoured soldiers", "Stormtroopers", ["Cybermen", "Redcoats", "Centurions"]),
 ("The Star Wars word for a robot like R2-D2", "Droid", ["Cyborg", "Replicant", "Dalek"]),
 ("Faster-than-light travel the Falcon jumps into", "Hyperspace", ["Warp speed", "Wormhole", "Time vortex"]),
 ("The bar in Mos Eisley where Han meets Luke", "Cantina", ["Saloon", "Diner", "Bistro"]),
 ("Boba Fett's line of work", "Bounty hunter", ["Smuggler", "Senator", "Pod racer"]),
 ("What Han Solo is frozen in", "Carbonite", ["Kryptonite", "Adamantium", "Vibranium"]),
 ("Leia's side in the fight against the Empire", "Rebel Alliance", ["Galactic Republic", "Trade Federation", "First Order"]),
 ("The crystal at the heart of every lightsaber", "Kyber crystal", ["Dilithium crystal", "Infinity Stone", "Philosopher's Stone"])])

race("what's this Bible word?", "Religion and myth", "medium", ["Bible", "Christianity", "words"], [
 ("The first book of the Bible", "Genesis", ["Exodus", "Leviticus", "Numbers"]),
 ("The last book of the Bible", "Revelation", ["Acts", "Jude", "Malachi"]),
 ("The four books telling Jesus's life", "Gospels", ["Epistles", "Chronicles", "Lamentations"]),
 ("Jesus's twelve chosen followers", "Apostles", ["Prophets", "Elders", "Levites"]),
 ("The song-poems credited to King David", "Psalms", ["Hymns", "Carols", "Sonnets"]),
 ("A story Jesus told to teach a lesson", "Parable", ["Fable", "Riddle", "Ballad"]),
 ("The garden where Adam and Eve lived", "Eden", ["Gethsemane", "Babylon", "Canaan"]),
 ("The giant felled by David's sling", "Goliath", ["Herod", "Pharaoh", "Nebuchadnezzar"]),
 ("The tower where languages got confused", "Babel", ["Jericho", "Zion", "Bethel"]),
 ("Noah's boat", "Ark", ["Galleon", "Barge", "Coracle"]),
 ("Where baby Jesus was laid", "Manger", ["Cradle", "Basket", "Hammock"]),
 ("Gold, frankincense and ...", "Myrrh", ["Silver", "Saffron", "Amber"]),
 ("The ten rules given to Moses", "Commandments", ["Beatitudes", "Proverbs", "Miracles"]),
 ("The ten disasters sent on Egypt", "Plagues", ["Curses", "Trials", "Woes"]),
 ("The mountain where Moses received the tablets", "Sinai", ["Ararat", "Carmel", "Olympus"]),
 ("The man swallowed by a great fish", "Jonah", ["Job", "Noah", "Daniel"]),
 ("The town where Jesus was born", "Bethlehem", ["Nazareth", "Jerusalem", "Galilee"]),
 ("The disciple who betrayed Jesus for thirty pieces of silver", "Judas", ["Peter", "Andrew", "Matthew"]),
 ("The disciple who doubted until he saw the wounds", "Thomas", ["Philip", "James", "Bartholomew"]),
 ("The strong man whose hair was cut by Delilah", "Samson", ["Solomon", "Gideon", "Absalom"])])

race("what's this Lord of the Rings word?", "Books", "medium", ["Lord of the Rings", "Tolkien", "words"], [
 ("The hobbits' green homeland", "The Shire", ["Bree", "Dale", "Esgaroth"]),
 ("Sauron's dark land", "Mordor", ["Angmar", "Harad", "Rhûn"]),
 ("Elrond's hidden elven valley", "Rivendell", ["Lothlórien", "Mirkwood", "Valinor"]),
 ("The kingdom of the White City, Minas Tirith", "Gondor", ["Arnor", "Númenor", "Erebor"]),
 ("The land of the horse-lords", "Rohan", ["Dunland", "Eriador", "Ithilien"]),
 ("Where the One Ring was forged, and destroyed", "Mount Doom", ["Lonely Mountain", "Weathertop", "Misty Mountains"]),
 ("What Gollum calls the Ring", "Precious", ["Treasure", "Darling", "Beloved"]),
 ("Tree-herds like Treebeard", "Ents", ["Trolls", "Dryads", "Wargs"]),
 ("Sauron's brutish foot soldiers", "Orcs", ["Dwarves", "Elves", "Wizards"]),
 ("The nine Ringwraiths", "Nazgûl", ["Maiar", "Valar", "Dúnedain"]),
 ("The light silvery metal of Frodo's mail shirt", "Mithril", ["Valyrian steel", "Vibranium", "Dwarven gold"]),
 ("Elvish waybread", "Lembas", ["Mead", "Bannock", "Pemmican"]),
 ("A seeing-stone", "Palantír", ["Silmaril", "Arkenstone", "Evenstar"]),
 ("The nine walkers who set out from Rivendell", "Fellowship", ["Company", "Council", "Brotherhood"]),
 ("The fiery demon Gandalf fights in Moria", "Balrog", ["Smaug", "Shelob", "Witch-king"]),
 ("Saruman's fortress", "Isengard", ["Barad-dûr", "Dol Guldur", "Minas Morgul"]),
 ("The name of Tolkien's world", "Middle-earth", ["Narnia", "Westeros", "Earthsea"]),
 ("Frodo's elvish blade that glows blue near orcs", "Sting", ["Glamdring", "Andúril", "Orcrist"]),
 ("Saruman's bred super-orcs", "Uruk-hai", ["Haradrim", "Easterlings", "Corsairs"]),
 ("The hobbit meal straight after breakfast", "Second breakfast", ["Brunch", "Tiffin", "Supper"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-185.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
