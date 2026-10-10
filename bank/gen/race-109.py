# Bank session 10 Oct 2026: 2 more general races -> bank/race-109.json (mottos, medical names). 20 rows each, target 10; wrong options are
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

race("whose motto is this?", "General knowledge", "hard", ["mottos", "Latin", "clubs"], [
 ("Superbia in Proelio ('pride in battle')", "Manchester City", ["Manchester United", "Aston Villa", "Chelsea"]),
 ("Audere est Facere ('to dare is to do')", "Tottenham Hotspur", ["West Ham", "Chelsea", "Leeds United"]),
 ("Nil Satis Nisi Optimum ('only the best is good enough')", "Everton", ["Aston Villa", "Middlesbrough", "Leeds United"]),
 ("Victoria Concordia Crescit ('victory through harmony')", "Arsenal", ["Chelsea", "West Ham", "Aston Villa"]),
 ("You'll Never Walk Alone, on the club crest", "Liverpool", ["Manchester United", "Leeds United", "Middlesbrough"]),
 ("Consectatio Excellentiae ('in pursuit of excellence')", "Sunderland AFC", ["Middlesbrough", "Leeds United", "Aston Villa"]),
 ("Per ardua ad astra ('through adversity to the stars')", "The RAF", ["The Royal Navy", "The Army Air Corps", "The Parachute Regiment"]),
 ("Who Dares Wins", "The SAS", ["The Parachute Regiment", "The Coldstream Guards", "The French Foreign Legion"]),
 ("Be Prepared", "The Scouts", ["The Boys' Brigade", "St John Ambulance", "The Army Cadets"]),
 ("Per Mare, Per Terram ('by sea, by land')", "The Royal Marines", ["The Royal Navy", "The Parachute Regiment", "The Coldstream Guards"]),
 ("Semper Fidelis ('always faithful')", "The US Marines", ["The US Navy", "The French Foreign Legion", "The US Army Rangers"]),
 ("Citius, Altius, Fortius ('faster, higher, stronger')", "The Olympic Games", ["The Paralympic Games", "The Commonwealth Games", "The Tour de France"]),
 ("Draco dormiens nunquam titillandus ('never tickle a sleeping dragon')", "Hogwarts", ["Beauxbatons", "Durmstrang", "Ilvermorny"]),
 ("Hear Me Roar!", "House Lannister", ["House Stark", "House Targaryen", "House Baratheon"]),
 ("Honi soit qui mal y pense ('shame on him who thinks evil of it')", "The Order of the Garter", ["The Order of the Bath", "The Order of the Thistle", "The Order of Merit"]),
 ("Ich dien ('I serve')", "The Prince of Wales", ["The Duke of Edinburgh", "The Princess Royal", "The Duke of York"]),
 ("Fortiter Defendit Triumphans ('triumphing by brave defence')", "Newcastle upon Tyne", ["Durham", "Edinburgh", "York"]),
 ("Veritas ('truth')", "Harvard", ["Stanford", "Princeton", "MIT"]),
 ("Dominus illuminatio mea ('the Lord is my light')", "The University of Oxford", ["The University of Cambridge", "Durham University", "Trinity College Dublin"]),
 ("Fluctuat nec mergitur ('tossed by the waves but never sunk')", "Paris", ["Venice", "Rome", "Amsterdam"])])

race("what's the everyday name for this condition?", "Science", "medium", ["health", "medicine", "words"], [
 ("Varicella", "Chickenpox", ["Measles", "Mumps", "Scarlet fever"]),
 ("Rubella", "German measles", ["Measles", "Scarlet fever", "Mumps"]),
 ("Pertussis", "Whooping cough", ["Croup", "Tonsillitis", "Hay fever"]),
 ("Myopia", "Short-sightedness", ["Long-sightedness", "Colour blindness", "Vertigo"]),
 ("Hypertension", "High blood pressure", ["Low blood pressure", "A heart murmur", "Migraine"]),
 ("Epistaxis", "A nosebleed", ["A bruise", "A cold sore", "Hay fever"]),
 ("Singultus", "Hiccups", ["Snoring", "Heartburn", "Cramp"]),
 ("Halitosis", "Bad breath", ["Tooth decay", "Mouth ulcers", "Heartburn"]),
 ("Alopecia", "Hair loss", ["Dandruff", "Ringworm", "Hives"]),
 ("Somnambulism", "Sleepwalking", ["Sleep talking", "Insomnia", "Snoring"]),
 ("Tinnitus", "Ringing in the ears", ["Earache", "Vertigo", "Hay fever"]),
 ("Infectious mononucleosis", "Glandular fever", ["Tonsillitis", "Scarlet fever", "Croup"]),
 ("Hallux valgus", "A bunion", ["A corn", "An ingrown toenail", "Gout"]),
 ("Pes planus", "Flat feet", ["Chilblains", "Gout", "A corn"]),
 ("Tinea pedis", "Athlete's foot", ["Ringworm", "Chilblains", "An ingrown toenail"]),
 ("Herpes zoster", "Shingles", ["A cold sore", "Hives", "Ringworm"]),
 ("Coryza", "The common cold", ["Hay fever", "A sore throat", "Croup"]),
 ("Sternutation", "Sneezing", ["Snoring", "Coughing", "Yawning"]),
 ("Pruritus", "Itching", ["A rash", "Hives", "Dandruff"]),
 ("Pyrexia", "A fever", ["Chills", "Cramp", "A stitch"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-109.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
