# Bank session 10 Oct 2026: 4 more general races -> bank/race-49.json. 20 rows each, target 10; wrong options are
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

race("which US state is this university in?", "World geography", "hard", ["USA", "universities", "states"], [
 ("Harvard", "Massachusetts", ["Vermont", "Maine", "Delaware"]), ("Yale", "Connecticut", ["Vermont", "Maine", "Delaware"]),
 ("Princeton", "New Jersey", ["Delaware", "Ohio", "Virginia"]), ("Stanford", "California", ["Oregon", "Arizona", "Nevada"]),
 ("Duke", "North Carolina", ["Virginia", "Kentucky", "West Virginia"]), ("Notre Dame", "Indiana", ["Ohio", "Michigan", "Wisconsin"]),
 ("Johns Hopkins", "Maryland", ["Delaware", "Virginia", "West Virginia"]), ("Cornell", "New York", ["Vermont", "Ohio", "Delaware"]),
 ("The University of Pennsylvania", "Pennsylvania", ["Ohio", "Delaware", "Virginia"]), ("Brown", "Rhode Island", ["Vermont", "Maine", "Delaware"]),
 ("Dartmouth", "New Hampshire", ["Vermont", "Maine", "Delaware"]), ("Vanderbilt", "Tennessee", ["Kentucky", "Mississippi", "Arkansas"]),
 ("Rice", "Texas", ["Oklahoma", "Arizona", "New Mexico"]), ("Emory", "Georgia", ["Florida", "Mississippi", "Kentucky"]),
 ("Tulane", "Louisiana", ["Mississippi", "Arkansas", "Florida"]), ("Northwestern", "Illinois", ["Wisconsin", "Michigan", "Ohio"]),
 ("Washington University in St Louis", "Missouri", ["Kansas", "Iowa", "Arkansas"]), ("Brigham Young (BYU)", "Utah", ["Arizona", "Nevada", "Colorado"]),
 ("Clemson", "South Carolina", ["Virginia", "Florida", "Kentucky"]), ("Auburn", "Alabama", ["Mississippi", "Florida", "Arkansas"])])

race("which opera is this character from?", "Music", "hard", ["opera", "characters"], [
 ("Violetta", "La traviata", ["Manon", "Norma", "Lucia di Lammermoor"]), ("Mimì", "La bohème", ["Manon", "Rusalka", "Werther"]),
 ("Cio-Cio-San", "Madama Butterfly", ["The Mikado", "The Pearl Fishers", "Lakmé"]), ("Papageno", "The Magic Flute", ["Fidelio", "Die Fledermaus", "Orpheus in the Underworld"]),
 ("Escamillo the toreador", "Carmen", ["The Pearl Fishers", "Manon", "Faust"]), ("Radamès", "Aida", ["Nabucco", "Otello", "Samson and Delilah"]),
 ("Prince Calaf", "Turandot", ["Prince Igor", "Nabucco", "Lakmé"]), ("Leporello", "Don Giovanni", ["Fidelio", "Falstaff", "Die Fledermaus"]),
 ("Cherubino", "The Marriage of Figaro", ["Fidelio", "Falstaff", "Die Fledermaus"]), ("Rosina", "The Barber of Seville", ["Falstaff", "Lucia di Lammermoor", "Norma"]),
 ("Tatyana", "Eugene Onegin", ["Boris Godunov", "Prince Igor", "Rusalka"]), ("Gilda", "Rigoletto", ["Falstaff", "Otello", "Nabucco"]),
 ("Ellen Orford", "Peter Grimes", ["Billy Budd", "The Turn of the Screw", "The Rake's Progress"]), ("Despina", "Così fan tutte", ["Fidelio", "Die Fledermaus", "Falstaff"]),
 ("Baron Scarpia", "Tosca", ["Otello", "Falstaff", "Manon"]), ("Azucena", "Il trovatore", ["Nabucco", "Otello", "Norma"]),
 ("Nedda", "Pagliacci", ["Falstaff", "Manon", "Werther"]), ("Santuzza", "Cavalleria rusticana", ["Norma", "Manon", "Lucia di Lammermoor"]),
 ("Belinda", "Dido and Aeneas", ["The Fairy Queen", "The Rake's Progress", "Billy Budd"]), ("The Marschallin", "Der Rosenkavalier", ["Salome", "Die Fledermaus", "Fidelio"])])

race("which chef is behind this restaurant?", "Food and drink", "hard", ["chefs", "restaurants"], [
 ("The Fat Duck, Bray", "Heston Blumenthal", ["Gordon Ramsay", "Marco Pierre White", "Tom Kerridge"]),
 ("Noma, Copenhagen", "René Redzepi", ["Magnus Nilsson", "Joël Robuchon", "Alain Ducasse"]),
 ("El Bulli, Catalonia", "Ferran Adrià", ["Joan Roca", "Alain Ducasse", "Paul Bocuse"]),
 ("The French Laundry, California", "Thomas Keller", ["Wolfgang Puck", "Anthony Bourdain", "Jean-Georges Vongerichten"]),
 ("Le Manoir aux Quat'Saisons", "Raymond Blanc", ["Marco Pierre White", "Gary Rhodes", "Gordon Ramsay"]),
 ("The River Café, London", "Ruth Rogers & Rose Gray", ["Nigella Lawson", "Delia Smith", "Antonio Carluccio"]),
 ("Fifteen, London", "Jamie Oliver", ["Hugh Fearnley-Whittingstall", "Gordon Ramsay", "Ainsley Harriott"]),
 ("The Seafood Restaurant, Padstow", "Rick Stein", ["Nathan Outlaw", "Paul Ainsworth", "Keith Floyd"]),
 ("The Waterside Inn, Bray", "Michel Roux", ["Marco Pierre White", "Gary Rhodes", "Marcus Wareing"]),
 ("Le Gavroche, in its later years", "Michel Roux Jr", ["Marcus Wareing", "Angela Hartnett", "Gordon Ramsay"]),
 ("L'Enclume, Cartmel", "Simon Rogan", ["Tom Kerridge", "Nathan Outlaw", "Paul Ainsworth"]),
 ("Momofuku, New York", "David Chang", ["Wolfgang Puck", "Anthony Bourdain", "Jean-Georges Vongerichten"]),
 ("Eleven Madison Park, New York", "Daniel Humm", ["Wolfgang Puck", "Jean-Georges Vongerichten", "Anthony Bourdain"]),
 ("Osteria Francescana, Modena", "Massimo Bottura", ["Antonio Carluccio", "Gennaro Contaldo", "Alain Ducasse"]),
 ("The Ledbury, London", "Brett Graham", ["Marcus Wareing", "Angela Hartnett", "Tom Kerridge"]),
 ("Hibiscus, London", "Claude Bosi", ["Joël Robuchon", "Alain Ducasse", "Marcus Wareing"]),
 ("Le Bernardin, New York", "Eric Ripert", ["Jean-Georges Vongerichten", "Wolfgang Puck", "Joël Robuchon"]),
 ("Alinea, Chicago", "Grant Achatz", ["Wolfgang Puck", "Anthony Bourdain", "Jean-Georges Vongerichten"]),
 ("Restaurant Story, London", "Tom Sellers", ["Tom Kerridge", "Marcus Wareing", "Angela Hartnett"]),
 ("Midsummer House, Cambridge", "Daniel Clifford", ["Gary Rhodes", "Tom Kerridge", "Marcus Wareing"])])

race("which city is this football stadium in?", "Football", "medium", ["stadiums", "cities"], [
 ("San Siro", "Milan", ["Genoa", "Bergamo", "Bologna"]), ("The Camp Nou", "Barcelona", ["Bilbao", "Girona", "Zaragoza"]),
 ("The Santiago Bernabéu", "Madrid", ["Bilbao", "Zaragoza", "Málaga"]), ("Anfield", "Liverpool", ["Leeds", "Newcastle", "Birmingham"]),
 ("Signal Iduna Park", "Dortmund", ["Gelsenkirchen", "Cologne", "Düsseldorf"]), ("The Allianz Arena", "Munich", ["Stuttgart", "Nuremberg", "Frankfurt"]),
 ("The Parc des Princes", "Paris", ["Lyon", "Lille", "Nice"]), ("The Olympiastadion where the 2006 World Cup final was held", "Berlin", ["Hamburg", "Leipzig", "Cologne"]),
 ("The Johan Cruyff Arena", "Amsterdam", ["Utrecht", "The Hague", "Arnhem"]), ("The Estádio da Luz", "Lisbon", ["Porto", "Braga", "Coimbra"]),
 ("Celtic Park", "Glasgow", ["Edinburgh", "Aberdeen", "Dundee"]), ("Old Trafford", "Manchester", ["Leeds", "Newcastle", "Birmingham"]),
 ("The Mestalla", "Valencia", ["Bilbao", "Málaga", "Zaragoza"]), ("The Ramón Sánchez-Pizjuán", "Seville", ["Málaga", "Granada", "Cádiz"]),
 ("The Stadio Olimpico", "Rome", ["Naples", "Florence", "Bologna"]), ("Juventus's Allianz Stadium", "Turin", ["Genoa", "Bergamo", "Florence"]),
 ("The Stade Vélodrome", "Marseille", ["Lyon", "Nice", "Bordeaux"]), ("The Philips Stadion", "Eindhoven", ["Utrecht", "Arnhem", "The Hague"]),
 ("De Kuip", "Rotterdam", ["Utrecht", "The Hague", "Arnhem"]), ("The Ernst Happel Stadion", "Vienna", ["Salzburg", "Graz", "Linz"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-49.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
