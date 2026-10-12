# Bank session 12 Oct 2026: 1 more general race -> bank/race-216.json (Diwali words). No race covers Diwali; Christmas dinner was
# dropped as too close to the Sunday roast race.
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

race("what's this Diwali word?", "Religion", "medium", ["Diwali", "Hinduism", "festivals", "words"], [
 ("Diwali's English nickname", "Festival of Lights", ["Festival of Colours", "Festival of Lanterns", "Festival of Bells"]),
 ("The small clay oil lamp lit at Diwali", "Diya", ["Lantern", "Tealight", "Torch"]),
 ("Colourful patterns made on the floor from powder or rice", "Rangoli", ["Mehndi", "Mandala", "Bindi"]),
 ("The goddess of wealth worshipped at Diwali", "Lakshmi", ["Durga", "Kali", "Saraswati"]),
 ("The elephant-headed god also worshipped at Diwali", "Ganesh", ["Garuda", "Nandi", "Jambavan"]),
 ("The prince whose return home Diwali celebrates", "Rama", ["Krishna", "Shiva", "Arjuna"]),
 ("Rama's wife, rescued from the demon king", "Sita", ["Radha", "Parvati", "Draupadi"]),
 ("The ten-headed demon king", "Ravana", ["Kansa", "Mahishasura", "Holika"]),
 ("The monkey god who helped rescue Sita", "Hanuman", ["Garuda", "Nandi", "Jambavan"]),
 ("Rama's home city, lit up for his return", "Ayodhya", ["Varanasi", "Agra", "Jaipur"]),
 ("The epic poem that tells Rama's story", "Ramayana", ["Mahabharata", "Bhagavad Gita", "Rig Veda"]),
 ("Indian sweets shared with family and friends", "Mithai", ["Chapati", "Pakora", "Samosa"]),
 ("The British city famous for its huge Diwali celebrations", "Leicester", ["Bradford", "Glasgow", "Cardiff"]),
 ("The Sikh festival celebrated at the same time", "Bandi Chhor Divas", ["Vaisakhi", "Gurpurab", "Lohri"]),
 ("The religion whose biggest festival it is", "Hindu", ["Buddhist", "Muslim", "Christian"]),
 ("The Hindu month in which Diwali falls", "Kartik", ["Shravan", "Chaitra", "Magh"]),
 ("How many days the festival lasts", "Five", ["Two", "Seven", "Ten"]),
 ("The first day, when people buy gold and new pots and pans", "Dhanteras", ["Navratri", "Holi", "Onam"]),
 ("A prayer ritual, like the one offered to Lakshmi", "Puja", ["Bhajan", "Yoga", "Karma"]),
 ("What Diwali also marks for many Gujarati families and businesses", "New Year", ["Harvest", "Spring", "Midsummer"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-216.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
