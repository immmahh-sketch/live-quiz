# Bank session 11 Oct 2026: 3 more general races -> bank/race-163.json (coal mining, poetry and opera words). 20 rows each, target 10; wrong options are
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

race("what's this coal mining word?", "North East England", "medium", ["coal mining", "North East", "pits"], [
 ("Another name for a coal mine", "Pit", ["Quarry", "Kiln", "Foundry"]),
 ("The old North East word for a miner", "Pitman", ["Navvy", "Ganger", "Docker"]),
 ("The dialect of the Durham and Northumberland coalfield", "Pitmatic", ["Geordie", "Mackem", "Smoggie"]),
 ("The vertical tunnel down into the mine", "Shaft", ["Adit", "Drift", "Sump"]),
 ("A layer of coal in the rock", "Seam", ["Vein", "Lode", "Strata"]),
 ("The lift that carries the men down the shaft", "Cage", ["Bucket", "Cradle", "Gondola"]),
 ("The bird taken underground to warn of gas", "Canary", ["Budgie", "Pigeon", "Robin"]),
 ("The safety lamp named after a Cornish scientist", "Davy lamp", ["Tilley lamp", "Hurricane lamp", "Anglepoise"]),
 ("George Stephenson's rival safety lamp, which some say gave Tynesiders their name", "Geordie lamp", ["Tilley lamp", "Hurricane lamp", "Storm lantern"]),
 ("The horse that hauled coal underground", "Pit pony", ["Dray horse", "Carthorse", "Packhorse"]),
 ("The North East word for a miner's packed lunch", "Bait", ["Tiffin", "Elevenses", "Brunch"]),
 ("The miner who cut the coal at the face", "Hewer", ["Banksman", "Deputy", "Onsetter"]),
 ("The miner who pushed the coal tubs", "Putter", ["Banksman", "Deputy", "Onsetter"]),
 ("Where the coal is actually cut", "Coalface", ["Pithead", "Spoil heap", "Colliery yard"]),
 ("A great tip of waste rock beside the pit", "Slag heap", ["Compost heap", "Scrap heap", "Rubbish dump"]),
 ("The 'Big Meeting' every July, with brass bands and banners", "Durham Miners' Gala", ["The Hoppings", "Great North Run", "Sunderland Air Show"]),
 ("The year-long dispute of 1984 to 1985", "Strike", ["Lockout", "Sit-in", "Boycott"]),
 ("The miners' union leader in that dispute", "Arthur Scargill", ["Ian MacGregor", "Neil Kinnock", "Joe Gormley"]),
 ("The explosive methane gas in a mine", "Firedamp", ["Blackdamp", "Afterdamp", "Whitedamp"]),
 ("The huge embroidered flag paraded by each pit village", "Banner", ["Bunting", "Pennant", "Tapestry"])])

race("what's this poetry word?", "Books", "medium", ["poetry", "poets", "words"], [
 ("Words that end with the same sound", "Rhyme", ["Pun", "Echo", "Chorus"]),
 ("A verse, or group of lines", "Stanza", ["Paragraph", "Chapter", "Scene"]),
 ("A poem of 14 lines", "Sonnet", ["Ode", "Villanelle", "Ballad"]),
 ("Three lines of 5, 7 and 5 syllables", "Haiku", ["Ode", "Villanelle", "Ballad"]),
 ("Five funny lines that rhyme AABBA", "Limerick", ["Ode", "Villanelle", "Ballad"]),
 ("Two rhyming lines in a row", "Couplet", ["Tercet", "Quatrain", "Octave"]),
 ("Repeating the first sound: 'Peter Piper picked'", "Alliteration", ["Assonance", "Hyperbole", "Irony"]),
 ("Words that sound like what they mean, like 'buzz'", "Onomatopoeia", ["Assonance", "Hyperbole", "Irony"]),
 ("The King's official poet", "Poet Laureate", ["Lord Chancellor", "Master of the Rolls", "Astronomer Royal"]),
 ("Wrote 'I wandered lonely as a cloud'", "Wordsworth", ["Coleridge", "Keats", "Shelley"]),
 ("Wrote 'The Charge of the Light Brigade'", "Tennyson", ["Browning", "Byron", "Blake"]),
 ("Wrote 'If—'", "Kipling", ["Hardy", "Housman", "Auden"]),
 ("The First World War poet of 'Dulce et Decorum Est'", "Wilfred Owen", ["Siegfried Sassoon", "Rupert Brooke", "Edward Thomas"]),
 ("Scotland's national poet", "Robert Burns", ["Walter Scott", "James Hogg", "Hugh MacDiarmid"]),
 ("The Welsh poet of 'Do not go gentle into that good night'", "Dylan Thomas", ["R. S. Thomas", "Edward Thomas", "Gerard Manley Hopkins"]),
 ("'Oh, I wish I'd looked after me teeth'", "Pam Ayres", ["Wendy Cope", "Carol Ann Duffy", "Benjamin Zephaniah"]),
 ("'Come, friendly bombs, and fall on Slough!'", "John Betjeman", ["Philip Larkin", "Ted Hughes", "John Cooper Clarke"]),
 ("Poetry with no fixed rhyme or rhythm", "Free verse", ["Blank verse", "Light verse", "Nursery rhyme"]),
 ("The regular pattern of beats in a line", "Metre", ["Litre", "Gram", "Furlong"]),
 ("A collection of poems by different poets", "Anthology", ["Biography", "Glossary", "Almanac"])])

race("what's this opera word?", "Music", "medium", ["opera", "classical music", "words"], [
 ("The highest female voice", "Soprano", ["Contralto", "Mezzo-soprano", "Alto"]),
 ("The highest common male voice", "Tenor", ["Bass", "Baritone", "Basso profundo"]),
 ("A solo song in an opera", "Aria", ["Chorus", "Recitative", "Finale"]),
 ("The words of an opera", "Libretto", ["Score", "Synopsis", "Programme"]),
 ("A man singing in the alto range", "Countertenor", ["Baritone", "Bass", "Castrato"]),
 ("What you shout at the end of a great performance", "Bravo", ["Olé", "Bingo", "Cheers"]),
 ("The orchestral piece played before the curtain rises", "Overture", ["Coda", "Finale", "Interlude"]),
 ("Small binoculars for the stalls", "Opera glasses", ["Monocle", "Spectacles", "Goggles"]),
 ("Bizet's opera about a fiery cigarette girl", "Carmen", ["Tosca", "Aida", "Norma"]),
 ("Puccini's opera set in Nagasaki", "Madama Butterfly", ["Turandot", "Tosca", "La bohème"]),
 ("The aria that became the theme of Italia 90", "Nessun dorma", ["O sole mio", "Ave Maria", "Time to Say Goodbye"]),
 ("The Italian among the Three Tenors", "Pavarotti", ["Domingo", "Carreras", "Bocelli"]),
 ("The opera festival in a Sussex country-house garden", "Glyndebourne", ["Aldeburgh", "Henley", "Cheltenham"]),
 ("Covent Garden's opera house", "Royal Opera House", ["London Coliseum", "Royal Albert Hall", "Wigmore Hall"]),
 ("The translation shown above the stage", "Surtitles", ["Footnotes", "Headlines", "Credits"]),
 ("The composer of the 15-hour Ring Cycle", "Wagner", ["Verdi", "Puccini", "Mozart"]),
 ("The Mozart opera with Papageno the bird-catcher", "The Magic Flute", ["The Marriage of Figaro", "Don Giovanni", "Così fan tutte"]),
 ("A lighter, shorter opera, like Gilbert and Sullivan's", "Operetta", ["Oratorio", "Cantata", "Requiem"]),
 ("'It ain't over till the ___ sings'", "Fat lady", ["Big man", "Chorus", "Organist"]),
 ("The lead female singer, and a word for a self-important person", "Prima donna", ["Ballerina", "Femme fatale", "Grande dame"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-163.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
