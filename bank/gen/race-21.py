# Bank session 10 Oct 2026: 4 more general races -> bank/race-21.json. 20 rows each, target 10; wrong options are
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

race("name the heroine of this Disney film", "Disney films", "medium", ["Disney", "characters"], [
 ("Sleeping Beauty", "Aurora", ["Odette", "Anastasia", "Thumbelina"]), ("The Little Mermaid", "Ariel", ["Melody", "Vanessa", "Attina"]),
 ("Beauty and the Beast", "Belle", ["Babette", "Bella", "Rose"]), ("Aladdin", "Jasmine", ["Scheherazade", "Leila", "Yasmin"]),
 ("Tangled", "Rapunzel", ["Mother Gothel", "Cassandra", "Ruby"]), ("Brave", "Merida", ["Elinor", "Morag", "Isla"]),
 ("The Princess and the Frog", "Tiana", ["Charlotte", "Mama Odie", "Eudora"]), ("The Hunchback of Notre Dame", "Esmeralda", ["Fleur-de-Lys", "Clopin", "Djali"]),
 ("Hercules", "Megara", ["Calliope", "Thalia", "Persephone"]), ("Tarzan", "Jane", ["Kala", "Terk", "Clayton"]),
 ("Atlantis: The Lost Empire", "Kida", ["Audrey", "Helga", "Mrs. Packard"]), ("Enchanted", "Giselle", ["Nancy", "Narissa", "Pip"]),
 ("Wish", "Asha", ["Sakina", "Dahlia", "Amaya"]), ("Encanto", "Mirabel", ["Isabela", "Luisa", "Dolores"]),
 ("The Aristocats", "Duchess", ["Marie", "Frou-Frou", "Abigail"]), ("Peter Pan", "Wendy", ["Tinker Bell", "Tiger Lily", "Mary Darling"]),
 ("Wreck-It Ralph", "Vanellope", ["Taffyta", "Calhoun", "Shank"]), ("Robin Hood", "Maid Marian", ["Lady Kluck", "Skippy", "Sis"]),
 ("101 Dalmatians", "Perdita", ["Anita", "Lucky", "Rolly"]), ("The Rescuers", "Penny", ["Bianca", "Madame Medusa", "Orville"])])

race("which country is this bridge in?", "Famous landmarks", "medium", ["bridges", "countries"], [
 ("The Golden Gate Bridge", "the USA", ["Mexico", "Cuba", "Brazil"]), ("The Charles Bridge", "Czechia", ["Slovakia", "Austria", "Poland"]),
 ("The Ponte Vecchio", "Italy", ["Croatia", "Malta", "Greece"]), ("Tower Bridge", "England", ["Belgium", "the Isle of Man", "Denmark"]),
 ("Sydney Harbour Bridge", "Australia", ["New Zealand", "South Africa", "Fiji"]), ("The Pont du Gard", "France", ["Belgium", "Luxembourg", "Monaco"]),
 ("Stari Most, Mostar", "Bosnia and Herzegovina", ["Croatia", "Serbia", "Montenegro"]), ("The Chain Bridge", "Hungary", ["Austria", "Slovakia", "Romania"]),
 ("The Akashi Kaikyō Bridge", "Japan", ["South Korea", "Taiwan", "China"]), ("The Forth Bridge", "Scotland", ["Northern Ireland", "the Isle of Man", "Denmark"]),
 ("The Menai Bridge", "Wales", ["Northern Ireland", "the Isle of Man", "Denmark"]), ("The Ha'penny Bridge", "Ireland", ["Northern Ireland", "the Isle of Man", "Denmark"]),
 ("The Puente Nuevo, Ronda", "Spain", ["Mexico", "Argentina", "Andorra"]), ("The Vasco da Gama Bridge", "Portugal", ["Brazil", "Mozambique", "Angola"]),
 ("The Erasmus Bridge", "the Netherlands", ["Belgium", "Germany", "Denmark"]), ("The Helix Bridge", "Singapore", ["Malaysia", "Thailand", "Indonesia"]),
 ("The Confederation Bridge", "Canada", ["Iceland", "Greenland", "Denmark"]), ("Storseisundet, the 'road to nowhere'", "Norway", ["Sweden", "Finland", "Iceland"]),
 ("The Kapellbrücke", "Switzerland", ["Austria", "Germany", "Liechtenstein"]), ("The Galata Bridge", "Turkey", ["Greece", "Cyprus", "Bulgaria"])])

race("which Shakespeare play is set here?", "Shakespeare", "hard", ["Shakespeare", "settings"], [
 ("Elsinore", "Hamlet", ["King Lear", "Richard III", "Cymbeline"]), ("Verona", "Romeo and Juliet", ["Titus Andronicus", "Coriolanus", "All's Well That Ends Well"]),
 ("Scotland, Dunsinane and Birnam Wood", "Macbeth", ["King Lear", "Richard III", "Henry IV"]), ("Illyria", "Twelfth Night", ["All's Well That Ends Well", "Cymbeline", "King John"]),
 ("The Forest of Arden", "As You Like It", ["Cymbeline", "Timon of Athens", "King Lear"]), ("A fairy wood near Athens", "A Midsummer Night's Dream", ["Cymbeline", "Titus Andronicus", "King John"]),
 ("Messina", "Much Ado About Nothing", ["Cymbeline", "King John", "Richard II"]), ("Padua", "The Taming of the Shrew", ["The Two Gentlemen of Verona", "All's Well That Ends Well", "Coriolanus"]),
 ("Alexandria", "Antony and Cleopatra", ["Titus Andronicus", "Coriolanus", "Timon of Athens"]), ("Sicilia and Bohemia", "The Winter's Tale", ["Cymbeline", "All's Well That Ends Well", "King Lear"]),
 ("Navarre", "Love's Labour's Lost", ["All's Well That Ends Well", "Henry VIII", "Richard II"]), ("Vienna", "Measure for Measure", ["The Two Gentlemen of Verona", "King John", "Cymbeline"]),
 ("Ephesus, with two sets of twins", "The Comedy of Errors", ["Timon of Athens", "Titus Andronicus", "Coriolanus"]), ("Troy", "Troilus and Cressida", ["Titus Andronicus", "Coriolanus", "Timon of Athens"]),
 ("Tyre", "Pericles", ["Timon of Athens", "Cymbeline", "Titus Andronicus"]), ("Belmont, where Portia lives", "The Merchant of Venice", ["The Two Gentlemen of Verona", "All's Well That Ends Well", "Cymbeline"]),
 ("Cyprus, where a general is fooled by Iago", "Othello", ["Titus Andronicus", "Cymbeline", "King John"]), ("Prospero's remote island", "The Tempest", ["Cymbeline", "King Lear", "All's Well That Ends Well"]),
 ("Rome, on the Ides of March", "Julius Caesar", ["King Lear", "Richard III", "Henry IV"]), ("Agincourt", "Henry V", ["Henry IV", "Richard II", "King John"])])

race("which city is home to this US team?", "Sport", "hard", ["US sport", "cities"], [
 ("The Lakers (basketball)", "Los Angeles", ["Sacramento", "Oakland", "San Diego"]), ("The Celtics (basketball)", "Boston", ["Philadelphia", "Washington", "Providence"]),
 ("The Yankees (baseball)", "New York", ["Philadelphia", "Washington", "Newark"]), ("The Cowboys (American football)", "Dallas", ["San Antonio", "Austin", "Oklahoma City"]),
 ("The Bulls (basketball)", "Chicago", ["Milwaukee", "Cleveland", "Cincinnati"]), ("The 49ers (American football)", "San Francisco", ["Oakland", "San Diego", "Sacramento"]),
 ("The Packers (American football)", "Green Bay", ["Milwaukee", "Madison", "Cleveland"]), ("The Steelers (American football)", "Pittsburgh", ["Philadelphia", "Cleveland", "Cincinnati"]),
 ("The Heat (basketball)", "Miami", ["Orlando", "Tampa", "Jacksonville"]), ("The Rockets (basketball)", "Houston", ["San Antonio", "Austin", "Oklahoma City"]),
 ("The Broncos (American football)", "Denver", ["Salt Lake City", "Kansas City", "Las Vegas"]), ("The Seahawks (American football)", "Seattle", ["Portland", "Vancouver", "Sacramento"]),
 ("The Saints (American football)", "New Orleans", ["Memphis", "Nashville", "Jacksonville"]), ("The Raptors (basketball)", "Toronto", ["Montreal", "Vancouver", "Ottawa"]),
 ("The Cardinals (baseball)", "St. Louis", ["Kansas City", "Cincinnati", "Milwaukee"]), ("The Tigers (baseball)", "Detroit", ["Cleveland", "Cincinnati", "Milwaukee"]),
 ("The Braves (baseball)", "Atlanta", ["Charlotte", "Nashville", "Jacksonville"]), ("The Suns (basketball)", "Phoenix", ["Las Vegas", "Salt Lake City", "Albuquerque"]),
 ("The Vikings (American football)", "Minneapolis", ["Milwaukee", "Kansas City", "Omaha"]), ("The Colts (American football)", "Indianapolis", ["Cincinnati", "Louisville", "Columbus"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
