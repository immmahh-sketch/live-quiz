# Bank session 11 Oct 2026: 3 more general races -> bank/race-161.json (Roman, ancient Egypt and cat words). 20 rows each, target 10; wrong options are
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

race("what's this Roman word?", "History", "medium", ["Romans", "ancient Rome", "words"], [
 ("A Roman army unit of about 5,000 soldiers", "Legion", ["Phalanx", "Battalion", "Regiment"]),
 ("The officer in charge of about 80 men", "Centurion", ["Legate", "Tribune", "Praetor"]),
 ("Fought in the arena to entertain the crowd", "Gladiator", ["Senator", "Vestal", "Tribune"]),
 ("Rome's giant amphitheatre", "Colosseum", ["Pantheon", "Circus Maximus", "Parthenon"]),
 ("A Roman town's main square and marketplace", "Forum", ["Agora", "Piazza", "Plaza"]),
 ("A bridge-like channel carrying water into town", "Aqueduct", ["Viaduct", "Causeway", "Culvert"]),
 ("The draped white robe worn by Roman citizens", "Toga", ["Tunic", "Sari", "Kaftan"]),
 ("The council that governed the Roman Republic", "Senate", ["Parliament", "Congress", "Witan"]),
 ("Augustus was the first of these", "Emperor", ["Pharaoh", "Consul", "Tsar"]),
 ("Underfloor heating in a Roman villa", "Hypocaust", ["Atrium", "Portico", "Peristyle"]),
 ("A floor picture made of tiny coloured tiles", "Mosaic", ["Fresco", "Tapestry", "Collage"]),
 ("A tall two-handled jar for wine or olive oil", "Amphora", ["Urn", "Flagon", "Chalice"]),
 ("The 73-mile frontier across northern Britain", "Hadrian's Wall", ["Antonine Wall", "Offa's Dyke", "Great Wall"]),
 ("The Iceni queen who led a revolt against Rome", "Boudicca", ["Cartimandua", "Cleopatra", "Matilda"]),
 ("Roman London", "Londinium", ["Eboracum", "Camulodunum", "Deva"]),
 ("The Roman name for France", "Gaul", ["Hispania", "Germania", "Britannia"]),
 ("Letters on legion standards: 'the Senate and People of Rome'", "SPQR", ["AD", "BC", "RIP"]),
 ("'I came, I saw, I conquered', in Latin", "Veni, vidi, vici", ["Carpe diem", "Et tu, Brute?", "Alea iacta est"]),
 ("Stabbed on the Ides of March, 44 BC", "Julius Caesar", ["Mark Antony", "Brutus", "Augustus"]),
 ("The town buried in ash when Vesuvius erupted in AD 79", "Pompeii", ["Ostia", "Paestum", "Ravenna"])])

race("what's this ancient Egypt word?", "History", "medium", ["ancient Egypt", "pharaohs", "words"], [
 ("Egypt's god-king", "Pharaoh", ["Sultan", "Shah", "Caesar"]),
 ("A giant tomb with four triangular sides", "Pyramid", ["Ziggurat", "Pagoda", "Stupa"]),
 ("A tall, thin, four-sided stone pillar with a pointed top", "Obelisk", ["Menhir", "Totem pole", "Minaret"]),
 ("A body preserved and wrapped in linen", "Mummy", ["Effigy", "Relic", "Zombie"]),
 ("A stone coffin", "Sarcophagus", ["Crypt", "Ossuary", "Urn"]),
 ("Picture-writing on temple walls", "Hieroglyphics", ["Cuneiform", "Runes", "Sanskrit"]),
 ("The slab that helped crack hieroglyphs, now in the British Museum", "Rosetta Stone", ["Blarney Stone", "Stone of Scone", "Elgin Marbles"]),
 ("Paper made from reeds", "Papyrus", ["Parchment", "Vellum", "Bark cloth"]),
 ("A lion with a human head, guarding Giza", "Sphinx", ["Griffin", "Chimera", "Manticore"]),
 ("The river Egypt depends on", "Nile", ["Euphrates", "Tigris", "Jordan"]),
 ("The boy king whose tomb was found in 1922", "Tutankhamun", ["Ramesses", "Akhenaten", "Khufu"]),
 ("The archaeologist who found that tomb", "Howard Carter", ["Lord Carnarvon", "Flinders Petrie", "Indiana Jones"]),
 ("The last ruler of ancient Egypt, lover of Mark Antony", "Cleopatra", ["Nefertiti", "Hatshepsut", "Boudicca"]),
 ("The sun god", "Ra", ["Osiris", "Horus", "Thoth"]),
 ("The jackal-headed god of the dead", "Anubis", ["Osiris", "Horus", "Thoth"]),
 ("The burial place of the pharaohs near Luxor", "Valley of the Kings", ["Valley of the Dolls", "Valley of Death", "Death Valley"]),
 ("A sacred dung beetle charm", "Scarab", ["Locust", "Ladybird", "Mantis"]),
 ("A cross with a loop on top: the symbol of life", "Ankh", ["Celtic cross", "Crescent", "Caduceus"]),
 ("The oval loop drawn around a pharaoh's name", "Cartouche", ["Halo", "Wreath", "Monogram"]),
 ("Pots that held the mummy's organs", "Canopic jars", ["Amphorae", "Urns", "Pithoi"])])

race("what's this cat word?", "Animals", "easy", ["cats", "pets", "words"], [
 ("A baby cat", "Kitten", ["Cub", "Kid", "Pup"]),
 ("A male cat", "Tom", ["Jack", "Buck", "Billy"]),
 ("A female cat kept for breeding", "Queen", ["Duchess", "Nanny", "Jenny"]),
 ("The rumbling sound of a happy cat", "Purr", ["Growl", "Bark", "Howl"]),
 ("The angry sound with the ears flat back", "Hiss", ["Bleat", "Coo", "Trill"]),
 ("The long feelers on a cat's face", "Whiskers", ["Antennae", "Bristles", "Tentacles"]),
 ("Where an indoor cat does its business", "Litter tray", ["Bird bath", "Dog bowl", "Hamster wheel"]),
 ("The plant that sends cats wild", "Catnip", ["Bindweed", "Dandelion", "Nettle"]),
 ("The little swinging door in the back door", "Cat flap", ["Cat's eye", "Catwalk", "Cat's cradle"]),
 ("Where a cat sharpens its claws", "Scratching post", ["Goalpost", "Signpost", "Lamppost"]),
 ("What a cat coughs up after grooming", "Hairball", ["Snowball", "Meatball", "Pom-pom"]),
 ("A striped coat, often with an M on the forehead", "Tabby", ["Siamese", "Persian", "Maine Coon"]),
 ("A mottled black and ginger coat, almost always on a female", "Tortoiseshell", ["Siamese", "Persian", "Maine Coon"]),
 ("The hairless breed", "Sphynx", ["Siamese", "Persian", "Maine Coon"]),
 ("How many lives a cat supposedly has", "Nine", ["Seven", "Three", "Twelve"]),
 ("The word meaning 'cat-like'", "Feline", ["Canine", "Bovine", "Equine"]),
 ("A lover of cats", "Ailurophile", ["Bibliophile", "Cinephile", "Audiophile"]),
 ("The cat who's been Chief Mouser at 10 Downing Street since 2011", "Larry", ["Humphrey", "Palmerston", "Sybil"]),
 ("The lasagne-loving cartoon cat", "Garfield", ["Felix", "Sylvester", "Top Cat"]),
 ("Pushing the paws in and out on a soft blanket, like making bread", "Kneading", ["Scratching", "Grooming", "Stalking"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-161.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
