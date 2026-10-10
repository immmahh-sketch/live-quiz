# Bank session 10 Oct 2026: 4 more general races -> bank/race-46.json. 20 rows each, target 10; wrong options are
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

race("who came up with this scientific idea?", "Science and nature", "hard", ["scientists", "theories"], [
 ("Evolution by natural selection", "Charles Darwin", ["Jean-Baptiste Lamarck", "Thomas Huxley", "Carl Linnaeus"]),
 ("Special relativity", "Albert Einstein", ["Niels Bohr", "Paul Dirac", "Richard Feynman"]),
 ("The law of universal gravitation", "Isaac Newton", ["Galileo Galilei", "Edmond Halley", "Tycho Brahe"]),
 ("A Sun-centred Solar System", "Nicolaus Copernicus", ["Galileo Galilei", "Ptolemy", "Tycho Brahe"]),
 ("The uncertainty principle", "Werner Heisenberg", ["Niels Bohr", "Paul Dirac", "Enrico Fermi"]),
 ("The periodic table", "Dmitri Mendeleev", ["Antoine Lavoisier", "John Dalton", "J. J. Thomson"]),
 ("The laws of planetary motion", "Johannes Kepler", ["Tycho Brahe", "Galileo Galilei", "Edmond Halley"]),
 ("The germ theory of disease", "Louis Pasteur", ["Joseph Lister", "Edward Jenner", "Alexander Fleming"]),
 ("Electromagnetic induction", "Michael Faraday", ["Alessandro Volta", "André-Marie Ampère", "Georg Ohm"]),
 ("The equations of electromagnetism", "James Clerk Maxwell", ["Nikola Tesla", "Thomas Edison", "André-Marie Ampère"]),
 ("The 'primeval atom', the first Big Bang idea", "Georges Lemaître", ["Fred Hoyle", "William Herschel", "Edmond Halley"]),
 ("The expanding universe", "Edwin Hubble", ["William Herschel", "Edmond Halley", "Galileo Galilei"]),
 ("Continental drift", "Alfred Wegener", ["Charles Lyell", "James Hutton", "Alexander von Humboldt"]),
 ("The laws of inheritance, from pea plants", "Gregor Mendel", ["Jean-Baptiste Lamarck", "Carl Linnaeus", "Thomas Huxley"]),
 ("The atomic nucleus", "Ernest Rutherford", ["J. J. Thomson", "James Chadwick", "John Dalton"]),
 ("Energy comes in 'quanta'", "Max Planck", ["Niels Bohr", "Paul Dirac", "Enrico Fermi"]),
 ("The double helix of DNA", "Watson & Crick", ["Pauling & Corey", "Banting & Best", "Hodgkin & Perutz"]),
 ("Black holes give off radiation", "Stephen Hawking", ["Roger Penrose", "Richard Feynman", "Fred Hoyle"]),
 ("The cat in the box that's both alive and dead", "Erwin Schrödinger", ["Niels Bohr", "Paul Dirac", "Max Born"]),
 ("The exclusion principle", "Wolfgang Pauli", ["Niels Bohr", "Paul Dirac", "Enrico Fermi"])])

race("whose fans are called this?", "Music", "medium", ["fans", "pop stars"], [
 ("Beliebers", "Justin Bieber", ["Shawn Mendes", "Jonas Brothers", "Jason Derulo"]), ("Swifties", "Taylor Swift", ["Olivia Rodrigo", "Sabrina Carpenter", "Billie Eilish"]),
 ("Little Monsters", "Lady Gaga", ["Madonna", "Britney Spears", "Christina Aguilera"]), ("The Beyhive", "Beyoncé", ["Jennifer Lopez", "Christina Aguilera", "Shakira"]),
 ("Arianators", "Ariana Grande", ["Sabrina Carpenter", "Olivia Rodrigo", "Camila Cabello"]), ("Directioners", "One Direction", ["The Wanted", "Westlife", "Take That"]),
 ("Mixers", "Little Mix", ["Girls Aloud", "Sugababes", "Spice Girls"]), ("The Barbz", "Nicki Minaj", ["Doja Cat", "Cardi B", "Lizzo"]),
 ("The Navy", "Rihanna", ["Doja Cat", "Cardi B", "Shakira"]), ("KatyCats", "Katy Perry", ["Pink", "Kesha", "Avril Lavigne"]),
 ("Selenators", "Selena Gomez", ["Demi Lovato", "Hilary Duff", "Camila Cabello"]), ("Sheerios", "Ed Sheeran", ["Lewis Capaldi", "James Arthur", "George Ezra"]),
 ("ARMY", "BTS", ["EXO", "Twice", "Stray Kids"]), ("Blinks", "Blackpink", ["Twice", "Red Velvet", "NewJeans"]),
 ("Deadheads", "Grateful Dead", ["The Doors", "Jefferson Airplane", "The Allman Brothers Band"]), ("Lambs", "Mariah Carey", ["Whitney Houston", "Celine Dion", "Christina Aguilera"]),
 ("Smilers", "Miley Cyrus", ["Demi Lovato", "Hilary Duff", "Kesha"]), ("The Kiss Army", "Kiss", ["Aerosmith", "Bon Jovi", "Mötley Crüe"]),
 ("Hooligans", "Bruno Mars", ["Jason Derulo", "Pharrell Williams", "The Weeknd"]), ("Harries", "Harry Styles", ["Louis Tomlinson", "Niall Horan", "Zayn"])])

race("which country did this monarch reign over in 2025?", "World geography", "hard", ["monarchs", "royal families", "countries"], [
 ("King Felipe VI", "Spain", ["Portugal", "Andorra", "Luxembourg"]), ("King Willem-Alexander", "the Netherlands", ["Luxembourg", "Austria", "Finland"]),
 ("King Philippe", "Belgium", ["Luxembourg", "Austria", "Andorra"]), ("King Frederik X", "Denmark", ["Iceland", "Finland", "Estonia"]),
 ("King Carl XVI Gustaf", "Sweden", ["Finland", "Iceland", "Estonia"]), ("King Harald V", "Norway", ["Iceland", "Finland", "Estonia"]),
 ("Emperor Naruhito", "Japan", ["South Korea", "Taiwan", "Cambodia"]), ("King Vajiralongkorn", "Thailand", ["Cambodia", "Laos", "Myanmar"]),
 ("King Abdullah II", "Jordan", ["Syria", "Iraq", "Kuwait"]), ("King Mohammed VI", "Morocco", ["Algeria", "Tunisia", "Egypt"]),
 ("King Salman", "Saudi Arabia", ["Kuwait", "the UAE", "Bahrain"]), ("Sultan Hassanal Bolkiah", "Brunei", ["Malaysia", "Indonesia", "Singapore"]),
 ("King Mswati III", "Eswatini", ["South Africa", "Botswana", "Mozambique"]), ("King Letsie III", "Lesotho", ["South Africa", "Botswana", "Namibia"]),
 ("King Tupou VI", "Tonga", ["Fiji", "Samoa", "Vanuatu"]), ("Prince Albert II", "Monaco", ["Andorra", "Luxembourg", "San Marino"]),
 ("Prince Hans-Adam II", "Liechtenstein", ["Luxembourg", "Austria", "Andorra"]), ("King Jigme Khesar Namgyel Wangchuck", "Bhutan", ["Nepal", "Sikkim", "Myanmar"]),
 ("Sultan Haitham bin Tariq", "Oman", ["Yemen", "the UAE", "Bahrain"]), ("Emir Tamim bin Hamad", "Qatar", ["Bahrain", "Kuwait", "the UAE"])])

race("what kind of animal is this?", "Animals", "hard", ["animals", "unusual animals"], [
 ("Axolotl", "Salamander", ["Eel", "Frog", "Catfish"]), ("Pangolin", "Scaly mammal", ["Armadillo", "Reptile", "Hedgehog"]),
 ("Okapi", "Giraffe family", ["Zebra", "Horse family", "Deer"]), ("Aye-aye", "Lemur", ["Bat", "Squirrel", "Opossum"]),
 ("Quokka", "Small wallaby", ["Rat", "Koala", "Possum"]), ("Capybara", "Rodent", ["Pig family", "Deer", "Bear"]),
 ("Narwhal", "Whale", ["Walrus", "Seal", "Shark"]), ("Dugong", "Sea cow", ["Walrus", "Seal", "Dolphin"]),
 ("Gharial", "Crocodilian", ["Snake", "Turtle", "Eel"]), ("Kakapo", "Parrot", ["Owl", "Penguin", "Kiwi"]),
 ("Komodo dragon", "Lizard", ["Snake", "Turtle", "Dinosaur"]), ("Coati", "Raccoon family", ["Monkey", "Weasel family", "Cat"]),
 ("Fossa", "Mongoose family", ["Dog family", "Weasel family", "Bear"]), ("Binturong", "Civet family", ["Bear", "Cat", "Monkey"]),
 ("Caracal", "Wild cat", ["Dog family", "Hyena", "Fox"]), ("Takin", "Goat-antelope", ["Cattle", "Deer", "Bear"]),
 ("Shoebill", "Bird", ["Dinosaur", "Pterosaur", "Bat"]), ("Tarsier", "Primate", ["Bat", "Owl", "Possum"]),
 ("Blobfish", "Fish", ["Jellyfish", "Octopus", "Sea slug"]), ("Tardigrade", "Microscopic animal", ["Insect", "Spider", "Bacterium"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-46.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
