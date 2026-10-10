# Bank session 10 Oct 2026: 4 more general races -> bank/race-39.json. 20 rows each, target 10; wrong options are
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

race("who made this sculpture?", "Art and culture", "hard", ["sculpture", "artists"], [
 ("The Thinker", "Auguste Rodin", ["Camille Claudel", "Aristide Maillol", "Henri Matisse"]),
 ("The David in Florence's Accademia", "Michelangelo", ["Donatello", "Verrocchio", "Ghiberti"]),
 ("The Angel of the North", "Antony Gormley", ["Barbara Hepworth", "Rachel Whiteread", "Thomas Heatherwick"]),
 ("Balloon Dog", "Jeff Koons", ["Claes Oldenburg", "Andy Warhol", "Yayoi Kusama"]),
 ("The Little Mermaid, Copenhagen", "Edvard Eriksen", ["Gustav Vigeland", "Carl Milles", "Bertel Thorvaldsen"]),
 ("Christ the Redeemer", "Paul Landowski", ["Oscar Niemeyer", "Aleijadinho", "Gutzon Borglum"]),
 ("The Statue of Liberty", "Frédéric Bartholdi", ["Augustus Saint-Gaudens", "Daniel Chester French", "Gutzon Borglum"]),
 ("The Kelpies", "Andy Scott", ["Eduardo Paolozzi", "Barbara Hepworth", "Thomas Heatherwick"]),
 ("The Reclining Figure series", "Henry Moore", ["Barbara Hepworth", "Jacob Epstein", "Eduardo Paolozzi"]),
 ("The Ecstasy of Saint Teresa", "Gian Lorenzo Bernini", ["Donatello", "Borromini", "Verrocchio"]),
 ("Perseus with the Head of Medusa", "Benvenuto Cellini", ["Donatello", "Giambologna", "Ghiberti"]),
 ("Maman, the giant spider", "Louise Bourgeois", ["Yayoi Kusama", "Tracey Emin", "Barbara Hepworth"]),
 ("Cloud Gate ('The Bean')", "Anish Kapoor", ["Claes Oldenburg", "Thomas Heatherwick", "Richard Serra"]),
 ("Fountain, the signed urinal", "Marcel Duchamp", ["Man Ray", "Salvador Dalí", "René Magritte"]),
 ("Walking Man", "Alberto Giacometti", ["Jean Arp", "Aristide Maillol", "Ossip Zadkine"]),
 ("Bird in Space", "Constantin Brâncuși", ["Jean Arp", "Barbara Hepworth", "Naum Gabo"]),
 ("The shark in formaldehyde", "Damien Hirst", ["Tracey Emin", "Marc Quinn", "Banksy"]),
 ("Charging Bull, Wall Street", "Arturo Di Modica", ["Kristen Visbal", "Claes Oldenburg", "Richard Serra"]),
 ("Little Dancer Aged Fourteen", "Edgar Degas", ["Pierre-Auguste Renoir", "Édouard Manet", "Claude Monet"]),
 ("The Three Graces (1814–17)", "Antonio Canova", ["Bertel Thorvaldsen", "Donatello", "Giambologna"])])

race("which architect designed this building?", "Art and culture", "hard", ["architecture", "architects"], [
 ("St Paul's Cathedral", "Christopher Wren", ["Nicholas Hawksmoor", "Inigo Jones", "Robert Adam"]),
 ("The London Aquatics Centre", "Zaha Hadid", ["Rem Koolhaas", "Jean Nouvel", "David Chipperfield"]),
 ("The Guggenheim Bilbao", "Frank Gehry", ["Richard Meier", "Jean Nouvel", "Rem Koolhaas"]),
 ("The Sagrada Família", "Antoni Gaudí", ["Lluís Domènech i Montaner", "Josep Puig i Cadafalch", "Andrea Palladio"]),
 ("The Sydney Opera House", "Jørn Utzon", ["Alvar Aalto", "Eero Saarinen", "Arne Jacobsen"]),
 ("The Louvre Pyramid", "I. M. Pei", ["Jean Nouvel", "Philip Johnson", "Tadao Ando"]),
 ("The Gherkin", "Norman Foster", ["Terry Farrell", "David Chipperfield", "Rem Koolhaas"]),
 ("The Shard", "Renzo Piano", ["Terry Farrell", "Jean Nouvel", "Richard Meier"]),
 ("Fallingwater", "Frank Lloyd Wright", ["Louis Sullivan", "Philip Johnson", "Walter Gropius"]),
 ("The Palace of Westminster (after the 1834 fire)", "Charles Barry", ["Decimus Burton", "Robert Adam", "John Soane"]),
 ("The Lloyd's building", "Richard Rogers", ["Terry Farrell", "James Stirling", "Denys Lasdun"]),
 ("The Royal Pavilion, Brighton", "John Nash", ["Robert Adam", "John Soane", "Decimus Burton"]),
 ("The Seagram Building", "Mies van der Rohe", ["Walter Gropius", "Louis Sullivan", "Le Corbusier"]),
 ("The Cathedral of Brasília", "Oscar Niemeyer", ["Le Corbusier", "Lúcio Costa", "Alvar Aalto"]),
 ("The dome of Florence Cathedral", "Filippo Brunelleschi", ["Michelangelo", "Bramante", "Leon Battista Alberti"]),
 ("Valencia's City of Arts and Sciences", "Santiago Calatrava", ["Rafael Moneo", "Ricardo Bofill", "Jean Nouvel"]),
 ("Beijing's Bird's Nest stadium", "Herzog & de Meuron", ["Rem Koolhaas", "Kengo Kuma", "Tadao Ando"]),
 ("The Chrysler Building", "William Van Alen", ["Louis Sullivan", "Philip Johnson", "Cass Gilbert"]),
 ("Newcastle Central Station", "John Dobson", ["Richard Grainger", "Thomas Oliver", "Robert Stephenson"]),
 ("The new Coventry Cathedral", "Basil Spence", ["Frederick Gibberd", "Giles Gilbert Scott", "Denys Lasdun"])])

race("which country is this stadium in?", "Sport", "medium", ["stadiums", "countries"], [
 ("The Maracanã", "Brazil", ["Uruguay", "Colombia", "Chile"]), ("The Camp Nou", "Spain", ["Andorra", "Belgium", "Greece"]),
 ("San Siro", "Italy", ["Switzerland", "Greece", "Croatia"]), ("The Allianz Arena", "Germany", ["Switzerland", "Belgium", "Czechia"]),
 ("The Estadio Azteca", "Mexico", ["Colombia", "Chile", "the USA"]), ("The MCG", "Australia", ["Fiji", "England", "Samoa"]),
 ("Eden Park", "New Zealand", ["Fiji", "Samoa", "England"]), ("Ellis Park", "South Africa", ["Namibia", "Zimbabwe", "Kenya"]),
 ("Croke Park", "Ireland", ["Scotland", "Wales", "England"]), ("The Stade de France", "France", ["Belgium", "Switzerland", "Monaco"]),
 ("The Johan Cruyff Arena", "the Netherlands", ["Belgium", "Luxembourg", "Sweden"]), ("The Estádio da Luz", "Portugal", ["Andorra", "Greece", "Uruguay"]),
 ("La Bombonera", "Argentina", ["Uruguay", "Chile", "Colombia"]), ("The Rungrado May Day Stadium", "North Korea", ["South Korea", "China", "Mongolia"]),
 ("The Luzhniki", "Russia", ["Ukraine", "Belarus", "Poland"]), ("The Lusail Stadium", "Qatar", ["Saudi Arabia", "the UAE", "Bahrain"]),
 ("Eden Gardens", "India", ["Pakistan", "Sri Lanka", "Bangladesh"]), ("Parken", "Denmark", ["Sweden", "Norway", "Iceland"]),
 ("The Ernst Happel Stadium", "Austria", ["Switzerland", "Czechia", "Slovakia"]), ("The Puskás Aréna", "Hungary", ["Romania", "Slovakia", "Serbia"])])

race("which country is this waterfall in?", "World geography", "medium", ["waterfalls", "countries"], [
 ("Angel Falls", "Venezuela", ["Colombia", "Brazil", "Ecuador"]), ("Gullfoss", "Iceland", ["Greenland", "the Faroe Islands", "Finland"]),
 ("Sutherland Falls", "New Zealand", ["Australia", "Fiji", "Chile"]), ("The Plitvice Lakes falls", "Croatia", ["Slovenia", "Bosnia and Herzegovina", "Montenegro"]),
 ("Kaieteur Falls", "Guyana", ["Suriname", "Colombia", "Brazil"]), ("Tugela Falls", "South Africa", ["Lesotho", "Namibia", "Zimbabwe"]),
 ("Yosemite Falls", "the USA", ["Canada", "Mexico", "Chile"]), ("The Rhine Falls", "Switzerland", ["Germany", "Liechtenstein", "France"]),
 ("Jog Falls", "India", ["Sri Lanka", "Nepal", "Bangladesh"]), ("Huangguoshu Falls", "China", ["Vietnam", "Laos", "Mongolia"]),
 ("The Blue Nile Falls", "Ethiopia", ["Sudan", "Egypt", "Kenya"]), ("Murchison Falls", "Uganda", ["Kenya", "Tanzania", "Rwanda"]),
 ("Kegon Falls", "Japan", ["South Korea", "Taiwan", "the Philippines"]), ("Gocta Falls", "Peru", ["Ecuador", "Bolivia", "Colombia"]),
 ("The Krimml Falls", "Austria", ["Germany", "Liechtenstein", "Slovenia"]), ("Vøringsfossen", "Norway", ["Sweden", "Finland", "Denmark"]),
 ("High Force", "England", ["Scotland", "Ireland", "the Isle of Man"]), ("Swallow Falls", "Wales", ["Scotland", "Ireland", "the Isle of Man"]),
 ("Erawan Falls", "Thailand", ["Laos", "Cambodia", "Myanmar"]), ("The Cascata delle Marmore", "Italy", ["Slovenia", "Malta", "Greece"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-39.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
