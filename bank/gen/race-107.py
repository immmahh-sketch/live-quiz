# Bank session 10 Oct 2026: 2 more general races -> bank/race-107.json (video game characters, faces on banknotes). 20 rows each, target 10; wrong options are
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

race("which video game series features this character?", "Video games", "medium", ["video games", "characters"], [
 ("Link, in a green tunic", "The Legend of Zelda", ["Fable", "Kingdom Hearts", "Dark Souls"]),
 ("Master Chief", "Halo", ["Destiny", "Gears of War", "Mass Effect"]),
 ("Lara Croft", "Tomb Raider", ["Prince of Persia", "Far Cry", "Dead Space"]),
 ("Kratos, the Ghost of Sparta", "God of War", ["Devil May Cry", "Diablo", "Elden Ring"]),
 ("Solid Snake", "Metal Gear Solid", ["Splinter Cell", "Max Payne", "Call of Duty"]),
 ("Pikachu", "Pokémon", ["Animal Crossing", "Persona", "Dragon Quest"]),
 ("Samus Aran, a bounty hunter in a power suit", "Metroid", ["Mass Effect", "Destiny", "Borderlands"]),
 ("Cloud Strife, with a giant Buster Sword", "Final Fantasy VII", ["Dragon Quest", "Persona", "Dark Souls"]),
 ("Steve, forever running from Creepers", "Minecraft", ["Terraria", "Roblox", "Fortnite"]),
 ("Nathan Drake", "Uncharted", ["Prince of Persia", "Far Cry", "Watch Dogs"]),
 ("Geralt of Rivia", "The Witcher", ["Skyrim", "Dark Souls", "Dragon Age"]),
 ("Arthur Morgan", "Red Dead Redemption 2", ["Mafia", "Far Cry", "Fallout"]),
 ("Ezio Auditore", "Assassin's Creed", ["Prince of Persia", "Ghost of Tsushima", "Dishonored"]),
 ("Joel and Ellie", "The Last of Us", ["Dead Space", "Days Gone", "Silent Hill"]),
 ("Niko Bellic", "Grand Theft Auto IV", ["Mafia", "Sleeping Dogs", "Saints Row"]),
 ("Gordon Freeman, with his crowbar", "Half-Life", ["Doom", "BioShock", "Quake"]),
 ("Ryu and Chun-Li", "Street Fighter", ["Tekken", "Soulcalibur", "Dead or Alive"]),
 ("Sub-Zero and Scorpion", "Mortal Kombat", ["Tekken", "Killer Instinct", "Soulcalibur"]),
 ("Agent 47", "Hitman", ["Splinter Cell", "Max Payne", "Deus Ex"]),
 ("Jill Valentine, fighting zombies in Raccoon City", "Resident Evil", ["Silent Hill", "Dead Rising", "Left 4 Dead"])])

race("whose face is on this Bank of England note?", "History", "hard", ["banknotes", "money", "famous Britons"], [
 ("The plastic £5 from 2016", "Winston Churchill", ["Clement Attlee", "David Lloyd George", "Horatio Nelson"]),
 ("The plastic £10 from 2017", "Jane Austen", ["Charlotte Brontë", "Mary Shelley", "George Eliot"]),
 ("The plastic £20 from 2020", "J. M. W. Turner", ["John Constable", "Thomas Gainsborough", "William Blake"]),
 ("The plastic £50 from 2021", "Alan Turing", ["Charles Babbage", "Ada Lovelace", "Tim Berners-Lee"]),
 ("The paper £10 from 2000, with a hummingbird and HMS Beagle", "Charles Darwin", ["Alfred Russel Wallace", "David Attenborough", "Captain Cook"]),
 ("The paper £20 from 2007, with a pin factory", "Adam Smith", ["John Maynard Keynes", "David Hume", "Robert Owen"]),
 ("The paper £5 from 2002, reading to prisoners at Newgate", "Elizabeth Fry", ["Mary Seacole", "Emmeline Pankhurst", "Octavia Hill"]),
 ("The paper £50 from 2011, a pair of steam-engine pioneers", "Boulton and Watt", ["Wedgwood and Arkwright", "Brunel and Telford", "Stephenson and Trevithick"]),
 ("The paper £10 from 1992, with a cricket match from Pickwick", "Charles Dickens", ["Thomas Hardy", "Anthony Trollope", "William Thackeray"]),
 ("The paper £20 from 1991, lecturing at the Royal Institution", "Michael Faraday", ["Joseph Lister", "Humphry Davy", "Edward Jenner"]),
 ("The paper £5 from 1990, with the Rocket locomotive", "George Stephenson", ["Isambard Kingdom Brunel", "Richard Trevithick", "Robert Stephenson"]),
 ("The paper £20 from 1999, with Worcester Cathedral", "Edward Elgar", ["Henry Purcell", "Ralph Vaughan Williams", "Gustav Holst"]),
 ("The 1975 £10, with a lamp on a hospital ward", "Florence Nightingale", ["Mary Seacole", "Edith Cavell", "Elizabeth Garrett Anderson"]),
 ("The 1978 £1 note, the last one", "Isaac Newton", ["Edmond Halley", "Robert Hooke", "Stephen Hawking"]),
 ("The 1971 £5, with a battle scene", "The Duke of Wellington", ["Horatio Nelson", "The Duke of Marlborough", "Oliver Cromwell"]),
 ("The 1981 £50, with St Paul's Cathedral", "Christopher Wren", ["Inigo Jones", "Nicholas Hawksmoor", "John Nash"]),
 ("The 1994 £50: the Bank's first Governor", "John Houblon", ["William Paterson", "Mervyn King", "Montagu Norman"]),
 ("The 1970 £20, with a scene from Romeo and Juliet", "William Shakespeare", ["Christopher Marlowe", "Geoffrey Chaucer", "John Milton"]),
 ("The front of every note issued from 1960 until 2024", "Elizabeth II", ["Queen Victoria", "George VI", "Prince Philip"]),
 ("The front of the new notes from 2024", "King Charles III", ["Prince William", "Queen Victoria", "George VI"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-107.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
