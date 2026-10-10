# Bank session 10 Oct 2026: 3 more general races -> bank/race-51.json. 20 rows each, target 10; wrong options are
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

race("which people built this?", "History", "hard", ["ancient civilisations", "archaeology"], [
 ("Machu Picchu", "The Inca", ["The Olmecs", "The Toltecs", "The Zapotecs"]), ("Chichén Itzá", "The Maya", ["The Olmecs", "The Zapotecs", "The Moche"]),
 ("Tenochtitlan", "The Aztecs", ["The Olmecs", "The Toltecs", "The Zapotecs"]), ("The temples of Karnak", "The ancient Egyptians", ["The Assyrians", "The Sumerians", "The Byzantines"]),
 ("The Parthenon", "The ancient Greeks", ["The Etruscans", "The Byzantines", "The Ottomans"]), ("The Colosseum", "The Romans", ["The Etruscans", "The Byzantines", "The Ottomans"]),
 ("Petra", "The Nabataeans", ["The Assyrians", "The Sumerians", "The Byzantines"]), ("Persepolis", "The Persians", ["The Assyrians", "The Sumerians", "The Ottomans"]),
 ("Angkor Wat", "The Khmer", ["The Mongols", "The Siamese", "The Ottomans"]), ("Great Zimbabwe", "The Shona", ["The Zulu", "The Ashanti", "The Moors"]),
 ("The palace of Knossos", "The Minoans", ["The Etruscans", "The Byzantines", "The Ottomans"]), ("The Lion Gate at Mycenae", "The Mycenaeans", ["The Etruscans", "The Byzantines", "The Ottomans"]),
 ("The first city of Carthage", "The Phoenicians", ["The Etruscans", "The Assyrians", "The Moors"]), ("The Ishtar Gate", "The Babylonians", ["The Assyrians", "The Sumerians", "The Ottomans"]),
 ("Hattusa", "The Hittites", ["The Assyrians", "The Sumerians", "The Byzantines"]), ("Mohenjo-daro", "The Indus Valley civilisation", ["The Sumerians", "The Mughals", "The Mongols"]),
 ("The Nazca Lines", "The Nazca", ["The Olmecs", "The Moche", "The Toltecs"]), ("The moai of Easter Island", "The Rapa Nui", ["The Maori", "The Olmecs", "The Moche"]),
 ("The cliff dwellings of Mesa Verde", "The Ancestral Puebloans", ["The Olmecs", "The Toltecs", "The Mississippians"]), ("The Sutton Hoo ship burial", "The Anglo-Saxons", ["The Vikings", "The Normans", "The Celts"])])

race("which language is this word or phrase from?", "Words and language", "medium", ["languages", "phrases"], [
 ("Hakuna matata", "Swahili", ["Zulu", "Amharic", "Yoruba"]), ("C'est la vie", "French", ["Catalan", "Romanian", "Breton"]),
 ("Carpe diem", "Latin", ["Greek", "Romanian", "Catalan"]), ("Mañana", "Spanish", ["Catalan", "Romanian", "Basque"]),
 ("La dolce vita", "Italian", ["Romanian", "Catalan", "Greek"]), ("Hygge", "Danish", ["Icelandic", "Polish", "Estonian"]),
 ("Schadenfreude", "German", ["Afrikaans", "Polish", "Czech"]), ("Aloha", "Hawaiian", ["Samoan", "Tongan", "Tagalog"]),
 ("Feng shui", "Chinese", ["Korean", "Thai", "Malay"]), ("Kia ora", "Maori", ["Samoan", "Tongan", "Tagalog"]),
 ("Shalom", "Hebrew", ["Amharic", "Persian", "Greek"]), ("Inshallah", "Arabic", ["Amharic", "Hungarian", "Greek"]),
 ("Lagom", "Swedish", ["Icelandic", "Estonian", "Polish"]), ("Sisu", "Finnish", ["Hungarian", "Icelandic", "Polish"]),
 ("Saudade", "Portuguese", ["Catalan", "Romanian", "Basque"]), ("Kawaii", "Japanese", ["Korean", "Thai", "Malay"]),
 ("Chutzpah", "Yiddish", ["Polish", "Czech", "Hungarian"]), ("Gezellig", "Dutch", ["Hungarian", "Czech", "Polish"]),
 ("Hwyl", "Welsh", ["Irish", "Scottish Gaelic", "Cornish"]), ("Babushka", "Russian", ["Ukrainian", "Polish", "Czech"])])

race("which city did this band come from?", "Music", "medium", ["bands", "cities"], [
 ("The Beatles", "Liverpool", ["Hamburg", "Bolton", "Preston"]), ("Oasis", "Manchester", ["Salford", "Bolton", "Stockport"]),
 ("Arctic Monkeys", "Sheffield", ["Rotherham", "Doncaster", "Barnsley"]), ("Lindisfarne", "Newcastle", ["Sunderland", "Durham", "Middlesbrough"]),
 ("Kaiser Chiefs", "Leeds", ["Bradford", "Wakefield", "Huddersfield"]), ("Duran Duran", "Birmingham", ["Wolverhampton", "Walsall", "Nottingham"]),
 ("Massive Attack", "Bristol", ["Bath", "Cardiff", "Swindon"]), ("Simple Minds", "Glasgow", ["Aberdeen", "Dundee", "Paisley"]),
 ("U2", "Dublin", ["Cork", "Belfast", "Galway"]), ("Pearl Jam", "Seattle", ["Portland", "San Francisco", "Vancouver"]),
 ("The Cranberries", "Limerick", ["Cork", "Galway", "Waterford"]), ("The Housemartins", "Hull", ["Grimsby", "Scarborough", "Doncaster"]),
 ("The Specials", "Coventry", ["Wolverhampton", "Leicester", "Northampton"]), ("Madness", "London", ["Brighton", "Reading", "Luton"]),
 ("Kings of Leon", "Nashville", ["Memphis", "Atlanta", "Austin"]), ("ABBA", "Stockholm", ["Gothenburg", "Oslo", "Copenhagen"]),
 ("The Killers", "Las Vegas", ["Los Angeles", "Phoenix", "Reno"]), ("The Bay City Rollers", "Edinburgh", ["Aberdeen", "Dundee", "Paisley"]),
 ("AC/DC", "Sydney", ["Melbourne", "Adelaide", "Perth"]), ("The B-52's", "Athens, Georgia", ["Atlanta", "Memphis", "Austin"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-51.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
