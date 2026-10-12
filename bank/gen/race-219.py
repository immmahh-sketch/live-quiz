# Bank session 12 Oct 2026: 1 more general race -> bank/race-219.json (monastery words). Checked against the church, Bible,
# religion, Tudor and Anglo-Saxon races: no right answer repeats theirs.
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

race("what's this monastery word?", "History", "medium", ["monks", "monasteries", "religion", "words"], [
 ("The head of an abbey", "Abbot", ["Bishop", "Deacon", "Curate"]),
 ("Second in command at an abbey, or head of a priory", "Prior", ["Canon", "Dean", "Rector"]),
 ("A new monk still in training", "Novice", ["Acolyte", "Postulant", "Deacon"]),
 ("The covered walkway round a square garden", "Cloister", ["Arcade", "Colonnade", "Portico"]),
 ("Where the monks ate together", "Refectory", ["Scullery", "Buttery", "Larder"]),
 ("The room where monks copied books by hand", "Scriptorium", ["Sacristy", "Solarium", "Oratory"]),
 ("Where the monks slept", "Dormitory", ["Almonry", "Calefactory", "Sacristy"]),
 ("Where sick and elderly monks were cared for", "Infirmary", ["Almonry", "Calefactory", "Sacristy"]),
 ("The first service of the day, in the small hours", "Matins", ["Mass", "Angelus", "Lauds"]),
 ("The evening service, sung at sunset", "Vespers", ["Mass", "Angelus", "Lauds"]),
 ("The last service of the day, before bed", "Compline", ["Mass", "Angelus", "Lauds"]),
 ("The long robe a monk wears", "Habit", ["Cassock", "Surplice", "Chasuble"]),
 ("The shaved patch on top of a monk's head", "Tonsure", ["Mullet", "Topknot", "Buzz cut"]),
 ("A promise never to speak", "Vow of silence", ["Vow of chastity", "Gag order", "Lock-in"]),
 ("The room where the monks met each day to run the abbey", "Chapter house", ["Boardroom", "Counting house", "Guildhall"]),
 ("Monks who follow the Rule of St Benedict", "Benedictine", ["Franciscan", "Dominican", "Jesuit"]),
 ("Silent monks famous for brewing beer", "Trappist", ["Carthusian", "Augustinian", "Carmelite"]),
 ("A brother who works out in the world, like Tuck", "Friar", ["Hermit", "Pilgrim", "Pardoner"]),
 ("Henry VIII's closing of the monasteries", "Dissolution", ["Restoration", "Abolition", "Enclosure"]),
 ("Decorated with gold and colour, like a monk's manuscript", "Illuminated", ["Laminated", "Embossed", "Engraved"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-219.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
