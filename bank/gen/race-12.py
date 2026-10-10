# Bank session 10 Oct 2026: 4 more general races -> bank/race-12.json. 20 rows each, target 10; wrong options are
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

race("name the famous rabbit", "Film, TV and books", "medium", ["rabbits", "characters"], [
 ("'Eh, what's up, doc?'", "Bugs Bunny", ["Daffy", "Porky", "Elmer"]), ("Mr. McGregor's garden raider in the blue jacket", "Peter Rabbit", ["Flopsy", "Mopsy", "Cottontail"]),
 ("Peter Rabbit's cousin", "Benjamin Bunny", ["Flopsy", "Mopsy", "Cottontail"]), ("The toon framed for murder in 1988", "Roger Rabbit", ["Baby Herman", "Benny the Cab", "Jessica"]),
 ("Bambi's foot-stamping friend", "Thumper", ["Flower", "Faline", "Friend Owl"]), ("'I'm late!' — in Wonderland", "The White Rabbit", ["The March Hare", "The Dormouse", "The Cheshire Cat"]),
 ("The trickster of the briar patch", "Br'er Rabbit", ["Br'er Fox", "Br'er Bear", "Tar-Baby"]), ("Watership Down's leader", "Hazel", ["Blackberry", "Dandelion", "Holly"]),
 ("Watership Down's seer, who foresees the danger", "Fiver", ["Pipkin", "Blackberry", "Silver"]), ("Watership Down's big fighter", "Bigwig", ["Holly", "Silver", "Dandelion"]),
 ("The tyrant of Efrafa in Watership Down", "General Woundwort", ["Campion", "Vervain", "Chervil"]), ("Dick Bruna's little rabbit", "Miffy", ["Snuffy", "Boris", "Poppy Pig"]),
 ("James Stewart's invisible six-foot friend", "Harvey", ["Elwood", "Veta", "Wilson"]), ("Pooh's fussy gardening friend", "Rabbit", ["Owl", "Eeyore", "Gopher"]),
 ("Zootopia's bunny cop", "Judy Hopps", ["Nick Wilde", "Chief Bogo", "Clawhauser"]), ("Disney's 'Lucky Rabbit' from before Mickey", "Oswald", ["Ortensia", "Mortimer", "Pete"]),
 ("The stuffed toy made Real by a boy's love", "The Velveteen Rabbit", ["The Skin Horse", "Corduroy", "Raggedy Ann"]), ("The rabbit who swaps minds with Wallace in Curse of the Were-Rabbit", "Hutch", ["Feathers McGraw", "Preston", "Fluffles"]),
 ("The Secret Life of Pets' mad bunny", "Snowball", ["Max", "Duke", "Gidget"]), ("Bugs's basketball-playing girlfriend in Space Jam", "Lola Bunny", ["Honey Bunny", "Babs", "Petunia"])])

race("which -ology is the study of this?", "Words and language", "hard", ["-ologies", "science"], [
 ("Birds", "Ornithology", ["Oology", "Apiology", "Aerology"]), ("Insects", "Entomology", ["Arachnology", "Helminthology", "Malacology"]),
 ("Earthquakes", "Seismology", ["Volcanology", "Glaciology", "Hydrology"]), ("Weather", "Meteorology", ["Cosmology", "Hydrology", "Astrology"]),
 ("Fossils", "Palaeontology", ["Archaeology", "Anthropology", "Mineralogy"]), ("Skin", "Dermatology", ["Haematology", "Neurology", "Rheumatology"]),
 ("The heart", "Cardiology", ["Haematology", "Neurology", "Urology"]), ("Eyes", "Ophthalmology", ["Audiology", "Otology", "Rhinology"]),
 ("Mushrooms and fungi", "Mycology", ["Pomology", "Bryology", "Phycology"]), ("Wine", "Oenology", ["Pomology", "Horology", "Cetology"]),
 ("Bells and bell-ringing", "Campanology", ["Horology", "Phonology", "Organology"]), ("Handwriting", "Graphology", ["Phrenology", "Philology", "Cryptology"]),
 ("Old age", "Gerontology", ["Neonatology", "Endocrinology", "Chronology"]), ("Shells", "Conchology", ["Oology", "Lithology", "Mineralogy"]),
 ("Caves", "Speleology", ["Glaciology", "Lithology", "Hydrology"]), ("Kidneys", "Nephrology", ["Hepatology", "Gastroenterology", "Pulmonology"]),
 ("Fish", "Ichthyology", ["Cetology", "Malacology", "Limnology"]), ("Reptiles and amphibians", "Herpetology", ["Mammalogy", "Primatology", "Cetology"]),
 ("Flags", "Vexillology", ["Semiology", "Philology", "Iconology"]), ("Where words come from", "Etymology", ["Phonology", "Morphology", "Cryptology"])])

race("whose national anthem is this?", "Music", "medium", ["anthems", "countries"], [
 ("God Save the King", "the United Kingdom", ["Liechtenstein", "Norway", "Denmark"]), ("La Marseillaise", "France", ["Belgium", "Monaco", "Luxembourg"]),
 ("The Star-Spangled Banner", "the USA", ["Mexico", "Liberia", "Brazil"]), ("Advance Australia Fair", "Australia", ["Fiji", "Samoa", "Papua New Guinea"]),
 ("O Canada", "Canada", ["Jamaica", "the Bahamas", "Iceland"]), ("Flower of Scotland (at the rugby)", "Scotland", ["Northern Ireland", "the Isle of Man", "Norway"]),
 ("Hen Wlad Fy Nhadau", "Wales", ["Northern Ireland", "the Isle of Man", "Iceland"]), ("Amhrán na bhFiann", "Ireland", ["Northern Ireland", "the Isle of Man", "Iceland"]),
 ("Das Lied der Deutschen", "Germany", ["Austria", "Liechtenstein", "Luxembourg"]), ("Il Canto degli Italiani", "Italy", ["San Marino", "Malta", "Croatia"]),
 ("Kimigayo", "Japan", ["South Korea", "Taiwan", "Vietnam"]), ("Het Wilhelmus", "the Netherlands", ["Belgium", "Denmark", "Luxembourg"]),
 ("Nkosi Sikelel' iAfrika", "South Africa", ["Kenya", "Nigeria", "Namibia"]), ("Jana Gana Mana", "India", ["Pakistan", "Bangladesh", "Sri Lanka"]),
 ("March of the Volunteers", "China", ["Taiwan", "Vietnam", "South Korea"]), ("Hatikvah", "Israel", ["Jordan", "Lebanon", "Egypt"]),
 ("God Defend New Zealand", "New Zealand", ["Fiji", "Samoa", "Tonga"]), ("Marcha Real (it has no words)", "Spain", ["Mexico", "Argentina", "Andorra"]),
 ("A Portuguesa", "Portugal", ["Brazil", "Angola", "Mozambique"]), ("Mazurek Dąbrowskiego", "Poland", ["Czechia", "Slovakia", "Hungary"])])

race("which constellation is this star in?", "Space", "hard", ["stars", "constellations"], [
 ("Sirius", "Canis Major", ["Ursa Major", "Lepus", "Monoceros"]), ("Betelgeuse", "Orion", ["Lepus", "Monoceros", "Hercules"]),
 ("Polaris", "Ursa Minor", ["Ursa Major", "Draco", "Cassiopeia"]), ("Vega", "Lyra", ["Hercules", "Draco", "Cassiopeia"]),
 ("Aldebaran", "Taurus", ["Aries", "Pisces", "Cancer"]), ("Antares", "Scorpius", ["Sagittarius", "Libra", "Ophiuchus"]),
 ("Spica", "Virgo", ["Libra", "Cancer", "Aries"]), ("Arcturus", "Boötes", ["Hercules", "Corona Borealis", "Ursa Major"]),
 ("Deneb", "Cygnus", ["Andromeda", "Pegasus", "Cassiopeia"]), ("Altair", "Aquila", ["Sagittarius", "Hercules", "Pegasus"]),
 ("Regulus", "Leo", ["Cancer", "Hydra", "Libra"]), ("Pollux", "Gemini", ["Cancer", "Aries", "Lepus"]),
 ("Capella", "Auriga", ["Andromeda", "Pegasus", "Cassiopeia"]), ("Procyon", "Canis Minor", ["Lepus", "Monoceros", "Hydra"]),
 ("Fomalhaut", "Piscis Austrinus", ["Aquarius", "Capricornus", "Pisces"]), ("Achernar", "Eridanus", ["Hydra", "Columba", "Lepus"]),
 ("Canopus", "Carina", ["Crux", "Columba", "Lupus"]), ("Algol", "Perseus", ["Andromeda", "Cassiopeia", "Pegasus"]),
 ("Mira", "Cetus", ["Pisces", "Aquarius", "Aries"]), ("Alpha Centauri", "Centaurus", ["Crux", "Lupus", "Hydra"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-12.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
