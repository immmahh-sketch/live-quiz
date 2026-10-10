# Bank session 10 Oct 2026: 4 more general races -> bank/race-9.json. 20 rows each, target 10; wrong options are
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

race("what's the Dutch word?", "Words and language", "medium", ["Dutch", "languages"], [
 ("Bicycle", "Fiets", ["Fles", "Feest", "Vis"]), ("Cheese", "Kaas", ["Kast", "Kaart", "Kers"]), ("Dog", "Hond", ["Hand", "Hout", "Hoed"]),
 ("House", "Huis", ["Huid", "Huur", "Hoes"]), ("Bread", "Brood", ["Broer", "Bord", "Brug"]), ("Friend", "Vriend", ["Vrede", "Vrij", "Vreemd"]),
 ("Thank you", "Dank je", ["Doei", "Alstublieft", "Dag"]), ("Good morning", "Goedemorgen", ["Goedenavond", "Goedenacht", "Welterusten"]),
 ("Sea", "Zee", ["Zon", "Zout", "Zeep"]), ("Street", "Straat", ["Strand", "Staart", "Stad"]), ("Church", "Kerk", ["Kers", "Kaars", "Kerst"]),
 ("Red", "Rood", ["Rok", "Roos", "Rond"]), ("Small", "Klein", ["Kleur", "Klok", "Kleed"]), ("Big", "Groot", ["Grond", "Groen", "Grot"]),
 ("Egg", "Ei", ["Eik", "Eis", "Uil"]), ("Book", "Boek", ["Boer", "Boot", "Boom"]), ("Night", "Nacht", ["Nagel", "Naald", "Nat"]),
 ("Woman", "Vrouw", ["Vrucht", "Vraag", "Vlucht"]), ("Child", "Kind", ["Kin", "Kist", "Keuken"]), ("Tomorrow", "Morgen", ["Middag", "Maandag", "Moeder"])])

race("name the famous bear", "Film and TV", "easy", ["bears", "characters"], [
 ("The bear from darkest Peru", "Paddington", ["Barnaby", "Aloysius", "Corduroy"]), ("Christopher Robin's bear", "Winnie-the-Pooh", ["Bertie", "Corduroy", "Humphrey"]),
 ("The Jungle Book's laid-back bear", "Baloo", ["Bagheera", "Shere Khan", "Kaa"]), ("The bear in yellow checked trousers", "Rupert", ["Biffo", "Bertie", "Barnaby"]),
 ("Jellystone Park's picnic thief", "Yogi", ["Cindy", "Ranger Smith", "Huckleberry"]), ("The Muppets' joke-telling bear", "Fozzie", ["Gonzo", "Animal", "Sweetums"]),
 ("Children in Need's mascot", "Pudsey", ["Blush", "Barnaby", "Bertie"]), ("Rainbow's bear", "Bungle", ["Zippy", "George", "Geoffrey"]),
 ("Harry Corbett's glove puppet bear", "Sooty", ["Sweep", "Soo", "Scampi"]), ("Mr. Bean's teddy", "Teddy", ["Irma Gobb", "Bertie", "Mini"]),
 ("The foul-mouthed bear in Mark Wahlberg's film", "Ted", ["Barney", "Bruno", "Freddy"]), ("Brother Bear's hero, turned into a bear", "Kenai", ["Koda", "Rutt", "Tuke"]),
 ("Kung Fu Panda's hero", "Po", ["Tigress", "Shifu", "Tai Lung"]), ("Merida's mum in Brave, turned into a bear", "Elinor", ["Merida", "Mor'du", "Fergus"]),
 ("His Dark Materials' armoured bear", "Iorek Byrnison", ["Iofur Raknison", "Lee Scoresby", "Pantalaimon"]), ("Play School's bigger teddy", "Big Ted", ["Hamble", "Jemima", "Humpty"]),
 ("Yogi's little sidekick", "Boo-Boo", ["Ranger Smith", "Cindy", "Huckleberry"]), ("The blue Care Bear with a rain cloud on his tummy", "Grumpy Bear", ["Bedtime Bear", "Tenderheart Bear", "Cheer Bear"]),
 ("The bear in Disney's Robin Hood", "Little John", ["Friar Tuck", "Sir Hiss", "Prince John"]), ("Toy Story 3's strawberry-scented villain", "Lotso", ["Chunk", "Big Baby", "Stretch"])])

race("what number is this in French?", "Words and language", "medium", ["French", "numbers"], [
 ("Cinq", "5", ["4", "6", "7"]), ("Huit", "8", ["6", "7", "18"]), ("Neuf", "9", ["19", "6", "10"]), ("Onze", "11", ["10", "1", "21"]),
 ("Douze", "12", ["2", "22", "10"]), ("Treize", "13", ["3", "23", "33"]), ("Quatorze", "14", ["4", "24", "44"]), ("Quinze", "15", ["25", "55", "51"]),
 ("Seize", "16", ["6", "7", "26"]), ("Dix-sept", "17", ["7", "27", "71"]), ("Vingt", "20", ["2", "22", "200"]), ("Trente", "30", ["3", "33", "300"]),
 ("Quarante", "40", ["4", "44", "400"]), ("Cinquante", "50", ["55", "500", "25"]), ("Soixante", "60", ["6", "66", "600"]), ("Soixante-dix", "70", ["76", "7", "160"]),
 ("Quatre-vingts", "80", ["24", "84", "420"]), ("Quatre-vingt-dix", "90", ["84", "94", "99"]), ("Cent", "100", ["1", "10", "101"]), ("Mille", "1,000", ["1", "10,000", "2,000"])])

race("name the famous mouse", "Film and TV", "medium", ["mice", "characters"], [
 ("Tom's rival in the cartoons", "Jerry", ["Tuffy", "Spike", "Butch"]), ("Mickey's girlfriend", "Minnie", ["Daisy", "Clarabelle", "Millie"]),
 ("Disney's first mouse star", "Mickey", ["Morty", "Ferdie", "Oswald"]), ("The mouse adopted by the Little family", "Stuart", ["Snowbell", "George", "Margalo"]),
 ("The secret-agent mouse with an eyepatch", "Danger Mouse", ["Penfold", "Greenback", "Stiletto"]), ("The fastest mouse in all Mexico", "Speedy Gonzales", ["Slowpoke Rodriguez", "Pepé Le Pew", "Daffy"]),
 ("Narnia's swashbuckling mouse", "Reepicheep", ["Trumpkin", "Puddleglum", "Tumnus"]), ("The hero of An American Tail", "Fievel", ["Tiger", "Tanya", "Warren T. Rat"]),
 ("Dumbo's mouse friend", "Timothy", ["Casey Junior", "Mr. Stork", "Ringmaster"]), ("The cheese-loving mouse in The Aristocats", "Roquefort", ["Toulouse", "Berlioz", "Edgar"]),
 ("The Great Mouse Detective", "Basil", ["Dawson", "Ratigan", "Olivia"]), ("The Rescuers' Hungarian agent", "Bianca", ["Bernard", "Penny", "Madame Medusa"]),
 ("Cinderella's chubby mouse friend", "Gus", ["Jaq", "Lucifer", "Bruno"]), ("The Simpsons' cartoon mouse", "Itchy", ["Scratchy", "Poochie", "Krusty"]),
 ("The lab mouse who wants to take over the world", "The Brain", ["Pinky", "Snowball", "Dexter"]), ("Beatrix Potter's tidy mouse", "Mrs. Tittlemouse", ["Mrs. Tiggy-Winkle", "Tabitha Twitchit", "Jemima Puddle-Duck"]),
 ("The ballerina mouse in the children's books", "Angelina", ["Maisy", "Olivia", "Clarice"]), ("The widowed mouse in The Secret of NIMH", "Mrs. Brisby", ["Jenner", "Nicodemus", "Jeremy"]),
 ("The greedy boy turned into a mouse in The Witches", "Bruno Jenkins", ["Augustus Gloop", "Mike Teavee", "The Grand High Witch"]), ("The flying superhero mouse", "Mighty Mouse", ["Atom Ant", "Underdog", "Secret Squirrel"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-9.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
