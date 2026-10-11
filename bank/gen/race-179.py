# Bank session 11 Oct 2026: 3 more general races -> bank/race-179.json (sci-fi, superhero and perfume words). 20 rows each, target 10; wrong options are
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

race("what's this sci-fi word?", "Film", "medium", ["science fiction", "space", "words"], [
 ("A being from another planet", "Alien", ["Mutant", "Zombie", "Ghost"]),
 ("A robot built to look like a human", "Android", ["Golem", "Puppet", "Scarecrow"]),
 ("Part human, part machine", "Cyborg", ["Golem", "Mummy", "Puppet"]),
 ("A device for travelling to the past or future", "Time machine", ["Slot machine", "Fruit machine", "Sewing machine"]),
 ("Beam instantly from one place to another", "Teleport", ["Telescope", "Telegram", "Telethon"]),
 ("Faster than light, on the Enterprise", "Warp speed", ["Snail's pace", "Top gear", "Turbo boost"]),
 ("A Jedi's glowing sword", "Lightsaber", ["Cutlass", "Rapier", "Scimitar"]),
 ("What the Millennium Falcon jumps into", "Hyperspace", ["Cyberspace", "Outer space", "Headspace"]),
 ("A machine named from a Czech word for 'forced labour'", "Robot", ["Drone", "Golem", "Mannequin"]),
 ("A grim imagined future society", "Dystopia", ["Utopia", "Atlantis", "Shangri-La"]),
 ("A region of space that nothing can escape", "Black hole", ["Pothole", "Plughole", "Manhole"]),
 ("A tunnel through space-time, a shortcut across the universe", "Wormhole", ["Rabbit hole", "Loophole", "Porthole"]),
 ("An exact genetic copy", "Clone", ["Mimic", "Echo", "Shadow"]),
 ("A 3D image made of light, like Rimmer in Red Dwarf", "Hologram", ["Polaroid", "Silhouette", "Mirage"]),
 ("The Doctor's police box time machine", "TARDIS", ["DeLorean", "Enterprise", "Millennium Falcon"]),
 ("Make a planet more like the Earth", "Terraform", ["Transform", "Terracotta", "Terrarium"]),
 ("The distance light travels in a year", "Light year", ["Leap year", "Gap year", "Year dot"]),
 ("Frozen sleep for long space voyages", "Cryosleep", ["Power nap", "Lie-in", "Siesta"]),
 ("A huge alien craft that launches smaller ones", "Mothership", ["Flagship", "Battleship", "Friendship"]),
 ("The author of The Time Machine and The War of the Worlds", "H. G. Wells", ["Jules Verne", "Arthur C. Clarke", "Isaac Asimov"])])

race("what's this superhero word?", "Film", "easy", ["superheroes", "comics", "words"], [
 ("The flowing cloak worn by Superman", "Cape", ["Apron", "Poncho", "Shawl"]),
 ("Hides a hero's face", "Mask", ["Monocle", "Snorkel", "Veil"]),
 ("The everyday name a hero hides behind, like Clark Kent", "Secret identity", ["Stage name", "Pen name", "Nickname"]),
 ("The hero's young helper, like Robin", "Sidekick", ["Kickback", "Sidecar", "Kickstand"]),
 ("The hero's greatest foe, like the Joker", "Arch-enemy", ["Best friend", "Pen pal", "Second cousin"]),
 ("How the hero got their powers", "Origin story", ["Bedtime story", "Ghost story", "Cover story"]),
 ("The green crystal that weakens Superman", "Kryptonite", ["Adamantium", "Plutonium", "Uranium"]),
 ("Wakanda's metal, used in Captain America's shield", "Vibranium", ["Adamantium", "Titanium", "Mithril"]),
 ("The Dark Knight's car", "Batmobile", ["Popemobile", "Snowmobile", "Bookmobile"]),
 ("The hidden lair under Wayne Manor", "Batcave", ["Fortress of Solitude", "Stark Tower", "Baxter Building"]),
 ("Batman's gadget-packed belt", "Utility belt", ["Seat belt", "Black belt", "Green belt"]),
 ("The searchlight in the sky over Gotham", "Bat-signal", ["Smoke signal", "Turn signal", "Railway signal"]),
 ("Peter Parker's tingling danger warning", "Spider-sense", ["Sixth sense", "Common sense", "Horse sense"]),
 ("The battle cry of Marvel's team", "Avengers assemble!", ["Charge!", "Geronimo!", "To infinity and beyond!"]),
 ("Stan Lee's brief appearance in the Marvel films", "Cameo", ["Encore", "Montage", "Trailer"]),
 ("The six gems Thanos collects", "Infinity Stones", ["Rolling Stones", "Stepping stones", "Kidney stones"]),
 ("Batman's home city", "Gotham", ["Metropolis", "Star City", "Central City"]),
 ("Captain America's round weapon", "Shield", ["Hammer", "Bow", "Trident"]),
 ("Wonder Woman's golden rope that makes you tell the truth", "Lasso of Truth", ["Bullwhip", "Grappling hook", "Washing line"]),
 ("The stretchy fabric of the classic costume", "Spandex", ["Denim", "Tweed", "Corduroy"])])

race("what's this perfume word?", "Fashion", "medium", ["perfume", "fragrance", "words"], [
 ("The lighter, cheaper version of a fragrance", "Eau de toilette", ["Eau de vie", "Eau de Nil", "Eau Claire"]),
 ("The spray bottle for scent", "Atomiser", ["Moisturiser", "Fertiliser", "Tenderiser"]),
 ("The top, middle and base ___ of a scent", "Notes", ["Chords", "Keys", "Bars"]),
 ("The animal-like base note, once taken from deer", "Musk", ["Mask", "Must", "Mush"]),
 ("The French town known as the perfume capital of the world", "Grasse", ["Nice", "Cannes", "Lyon"]),
 ("Marilyn Monroe said she wore only this to bed", "Chanel No. 5", ["Opium", "Poison", "Shalimar"]),
 ("The nickname for an expert perfume maker", "Nose", ["Eye", "Ear", "Palate"]),
 ("The shop bottle you can spray to try", "Tester", ["Taster", "Toaster", "Teaser"]),
 ("The purple flower grown for scent in Provence and Norfolk", "Lavender", ["Heather", "Thistle", "Foxglove"]),
 ("The sweet note from an orchid pod", "Vanilla", ["Vinegar", "Vermouth", "Velvet"]),
 ("The creamy woody note from an Indian tree", "Sandalwood", ["Driftwood", "Boxwood", "Sherwood"]),
 ("The airport shop where perfume is cheaper", "Duty free", ["Tax return", "Fee-paying", "Free-range"]),
 ("The wrists and neck, where you dab the scent", "Pulse points", ["Brownie points", "Match points", "Talking points"]),
 ("The German city that gave its name to a fragrance", "Cologne", ["Hamburg", "Frankfurt", "Berlin"]),
 ("The citrus fruit that flavours Earl Grey and many scents", "Bergamot", ["Kumquat", "Ugli fruit", "Satsuma"]),
 ("The precious dark resin from agarwood, loved in the Middle East", "Oud", ["Odd", "Ode", "Oak"]),
 ("The one fragrance you always wear", "Signature scent", ["Signature dish", "Signature move", "Signature tune"]),
 ("The earthy hippy scent from a plant in the mint family", "Patchouli", ["Paprika", "Pistachio", "Papaya"]),
 ("Cheap all-over scent in an aerosol, like Lynx", "Body spray", ["Hairspray", "Fly spray", "Sea spray"]),
 ("The person who creates fragrances", "Perfumer", ["Brewer", "Baker", "Barber"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-179.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
