# Bank session 12 Oct 2026: 1 more general race -> bank/race-213.json (Anglo-Saxon words). Checked against the Viking, Roman,
# knight, royal and North East races: no right answer repeats theirs.
# 20 rows each, target 10; wrong options are the same kind of thing, never another row's right answer, and never also right for that row.
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

race("what's this Anglo-Saxon word?", "History", "hard", ["Anglo-Saxons", "Northumbria", "North East", "words"], [
 ("The Jarrow monk who wrote the first history of the English", "Bede", ["Alcuin", "Aidan", "Wilfrid"]),
 ("The glittering book made on Holy Island around 700", "Lindisfarne Gospels", ["Book of Kells", "Domesday Book", "Magna Carta"]),
 ("The kingdom stretching from the Humber up to the Forth", "Northumbria", ["Mercia", "East Anglia", "Kent"]),
 ("Alfred the Great's kingdom in the south-west", "Wessex", ["Mercia", "Essex", "Sussex"]),
 ("The Suffolk ship burial packed with treasure", "Sutton Hoo", ["Staffordshire Hoard", "Mildenhall Treasure", "Snettisham Hoard"]),
 ("The Old English poem about a hero who kills Grendel", "Beowulf", ["Gawain", "Brutus", "Ivanhoe"]),
 ("The great bank and ditch a Mercian king built along the Welsh border", "Offa's Dyke", ["Hadrian's Wall", "Antonine Wall", "Wat's Dyke"]),
 ("The king's council of wise men", "Witan", ["Senate", "Parliament", "Thing"]),
 ("A noble who held land in return for serving the king", "Thegn", ["Serf", "Squire", "Yeoman"]),
 ("The local official who ran a shire or an estate for the king", "Reeve", ["Constable", "Steward", "Abbot"]),
 ("The price paid to a victim's family for killing them", "Wergild", ["Danegeld", "Tithe", "Ransom"]),
 ("A lord's great feasting hall, like Heorot", "Mead hall", ["Longhouse", "Tavern", "Abbey"]),
 ("An Anglo-Saxon county, still found in many place names", "Shire", ["Hundred", "Parish", "Province"]),
 ("A fortified town Alfred built to hold off the Danes", "Burh", ["Motte", "Broch", "Kraal"]),
 ("Northumbria's favourite saint, buried in Durham Cathedral", "St Cuthbert", ["St Aidan", "St Oswald", "St Wilfrid"]),
 ("Where the synod of 664 settled how to date Easter", "Whitby", ["Jarrow", "Hexham", "Durham"]),
 ("Alfred's grandson, the first king of all England", "Athelstan", ["Edgar", "Edmund", "Æthelred"]),
 ("The battle in 1066 that ended Anglo-Saxon England", "Hastings", ["Stamford Bridge", "Fulford", "Bosworth"]),
 ("The last crowned Anglo-Saxon king", "Harold Godwinson", ["Edward the Confessor", "Edgar Ætheling", "William the Conqueror"]),
 ("The language Beowulf is written in", "Old English", ["Middle English", "Old Norse", "Latin"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-213.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
