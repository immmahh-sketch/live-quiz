# Bank session 10 Oct 2026: 4 more general races -> bank/race-45.json. 20 rows each, target 10; wrong options are
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

race("where was this famous person born?", "History", "hard", ["birthplaces", "famous people"], [
 ("Wolfgang Amadeus Mozart", "Salzburg", ["Vienna", "Innsbruck", "Munich"]), ("William Shakespeare", "Stratford-upon-Avon", ["Warwick", "Coventry", "Oxford"]),
 ("Pablo Picasso", "Málaga", ["Barcelona", "Seville", "Madrid"]), ("Albert Einstein", "Ulm", ["Munich", "Berlin", "Zurich"]),
 ("Ludwig van Beethoven", "Bonn", ["Vienna", "Cologne", "Leipzig"]), ("Napoleon Bonaparte", "Ajaccio", ["Bastia", "Marseille", "Nice"]),
 ("Christopher Columbus", "Genoa", ["Venice", "Lisbon", "Seville"]), ("Karl Marx", "Trier", ["Cologne", "Berlin", "London"]),
 ("Elvis Presley", "Tupelo", ["Memphis", "Nashville", "Jackson"]), ("Charles Dickens", "Portsmouth", ["Rochester", "London", "Chatham"]),
 ("Mahatma Gandhi", "Porbandar", ["Ahmedabad", "Delhi", "Rajkot"]), ("Galileo Galilei", "Pisa", ["Florence", "Padua", "Rome"]),
 ("Nicolaus Copernicus", "Toruń", ["Kraków", "Warsaw", "Gdańsk"]), ("Salvador Dalí", "Figueres", ["Cadaqués", "Barcelona", "Girona"]),
 ("Mother Teresa", "Skopje", ["Kolkata", "Tirana", "Belgrade"]), ("Freddie Mercury", "Zanzibar", ["Muscat", "Dar es Salaam", "Feltham"]),
 ("Audrey Hepburn", "Brussels", ["Amsterdam", "Arnhem", "London"]), ("Rudyard Kipling", "Bombay (Mumbai)", ["Calcutta", "Lahore", "Delhi"]),
 ("Winston Churchill", "Blenheim Palace", ["Chartwell", "Hatfield House", "Chatsworth"]), ("Sting", "Wallsend", ["Newcastle", "Sunderland", "North Shields"])])

race("which club has this mascot?", "Football", "medium", ["mascots", "football clubs"], [
 ("Gunnersaurus", "Arsenal", ["Fulham", "Burnley", "QPR"]), ("Mighty Red", "Liverpool", ["Nottingham Forest", "Bournemouth", "Southampton"]),
 ("Fred the Red", "Manchester United", ["Nottingham Forest", "Bristol City", "Bournemouth"]), ("Moonchester", "Manchester City", ["Stoke City", "Blackburn Rovers", "Bolton Wanderers"]),
 ("Stamford the Lion", "Chelsea", ["Millwall", "Charlton Athletic", "Fulham"]), ("Chirpy the Cockerel", "Tottenham Hotspur", ["Bolton Wanderers", "Ipswich Town", "West Bromwich Albion"]),
 ("Hammerhead", "West Ham United", ["Millwall", "Charlton Athletic", "Southampton"]), ("Monty Magpie", "Newcastle United", ["Notts County", "Bolton Wanderers", "Hartlepool United"]),
 ("Samson the Cat", "Sunderland", ["Hull City", "Stoke City", "Hartlepool United"]), ("Roary the Lion", "Middlesbrough", ["Millwall", "Hull City", "Bolton Wanderers"]),
 ("Filbert Fox", "Leicester City", ["Burnley", "Ipswich Town", "Bournemouth"]), ("Pete the Eagle", "Crystal Palace", ["Fulham", "QPR", "Reading"]),
 ("Wolfie", "Wolverhampton Wanderers", ["Burnley", "Bolton Wanderers", "Stoke City"]), ("Gully the Seagull", "Brighton & Hove Albion", ["Southampton", "Portsmouth", "Reading"]),
 ("Captain Canary", "Norwich City", ["Ipswich Town", "Bournemouth", "Southampton"]), ("Lucas the Kop Kat", "Leeds United", ["Hull City", "Bolton Wanderers", "Stoke City"]),
 ("Hercules the Lion", "Aston Villa", ["Millwall", "West Bromwich Albion", "Coventry City"]), ("Rammie", "Derby County", ["Stoke City", "Coventry City", "Nottingham Forest"]),
 ("Ozzie the Owl", "Sheffield Wednesday", ["Bolton Wanderers", "Burnley", "Blackburn Rovers"]), ("Changy the Elephant", "Everton", ["Coventry City", "Blackburn Rovers", "Bolton Wanderers"])])

race("which gallery or building is home to this famous artwork?", "Art and culture", "hard", ["paintings", "galleries"], [
 ("The Mona Lisa", "The Louvre", ["The Centre Pompidou", "The Musée Rodin", "The Pinacoteca di Brera"]),
 ("The Night Watch", "The Rijksmuseum", ["The Van Gogh Museum", "The Kunsthistorisches Museum", "The Alte Pinakothek"]),
 ("The Birth of Venus", "The Uffizi", ["The Accademia Gallery", "The Pinacoteca di Brera", "The Vatican Museums"]),
 ("Guernica", "The Reina Sofía", ["The Thyssen-Bornemisza", "The Musée Picasso, Paris", "The Museu Picasso, Barcelona"]),
 ("The Starry Night", "MoMA, New York", ["The Met", "The Guggenheim", "The Van Gogh Museum"]),
 ("Girl with a Pearl Earring", "The Mauritshuis", ["The Van Gogh Museum", "The Kunsthistorisches Museum", "The Alte Pinakothek"]),
 ("Las Meninas", "The Prado", ["The Thyssen-Bornemisza", "The Museu Picasso, Barcelona", "El Escorial"]),
 ("The Hay Wain", "The National Gallery, London", ["The V&A", "The Courtauld", "The National Portrait Gallery"]),
 ("Klimt's The Kiss", "The Belvedere, Vienna", ["The Kunsthistorisches Museum", "The Leopold Museum", "The Albertina"]),
 ("The Last Supper", "Santa Maria delle Grazie, Milan", ["The Pinacoteca di Brera", "The Vatican Museums", "Milan Cathedral"]),
 ("The Creation of Adam", "The Sistine Chapel", ["St Peter's Basilica", "The Pantheon", "The Galleria Borghese"]),
 ("American Gothic", "The Art Institute of Chicago", ["The Met", "The Guggenheim", "The Getty Center"]),
 ("Monet's giant Water Lilies panels", "The Musée de l'Orangerie", ["The Centre Pompidou", "The Musée Rodin", "The Petit Palais"]),
 ("Millais's Ophelia", "Tate Britain", ["Tate Modern", "The Courtauld", "The National Portrait Gallery"]),
 ("Wanderer above the Sea of Fog", "The Hamburger Kunsthalle", ["The Alte Pinakothek", "The Kunsthistorisches Museum", "The Neue Nationalgalerie"]),
 ("Dalí's Christ of Saint John of the Cross", "Kelvingrove, Glasgow", ["The Burrell Collection", "The Walker Art Gallery", "The Hunterian"]),
 ("The Laughing Cavalier", "The Wallace Collection", ["The Courtauld", "The National Portrait Gallery", "Kenwood House"]),
 ("Renoir's Bal du moulin de la Galette", "The Musée d'Orsay", ["The Centre Pompidou", "The Petit Palais", "The Musée Rodin"]),
 ("Monet's Impression, Sunrise", "The Musée Marmottan", ["The Petit Palais", "The Centre Pompidou", "The Musée Rodin"]),
 ("Landseer's The Monarch of the Glen", "The Scottish National Gallery", ["The Burrell Collection", "The Hunterian", "The Walker Art Gallery"])])

race("which country is this famous prison in?", "History", "medium", ["prisons", "countries"], [
 ("Alcatraz", "the USA", ["Canada", "Bermuda", "the Bahamas"]), ("Robben Island", "South Africa", ["Namibia", "Zimbabwe", "Mozambique"]),
 ("Spandau", "Germany", ["Austria", "Poland", "Czechia"]), ("The Château d'If", "France", ["Italy", "Spain", "Monaco"]),
 ("Kilmainham Gaol", "Ireland", ["Wales", "the Isle of Man", "Iceland"]), ("Hỏa Lò, the 'Hanoi Hilton'", "Vietnam", ["Laos", "Cambodia", "China"]),
 ("The Lubyanka", "Russia", ["Ukraine", "Belarus", "Kazakhstan"]), ("HMP Maze", "Northern Ireland", ["Wales", "the Isle of Man", "Iceland"]),
 ("Port Arthur", "Australia", ["New Zealand", "Fiji", "Papua New Guinea"]), ("Bang Kwang", "Thailand", ["Laos", "Cambodia", "Malaysia"]),
 ("Carandiru", "Brazil", ["Argentina", "Colombia", "Peru"]), ("HMP Barlinnie", "Scotland", ["Wales", "the Isle of Man", "Iceland"]),
 ("HMP Wormwood Scrubs", "England", ["Wales", "the Isle of Man", "Iceland"]), ("Bastøy, the island prison", "Norway", ["Sweden", "Denmark", "Finland"]),
 ("Lecumberri, 'the Black Palace'", "Mexico", ["Colombia", "Peru", "Guatemala"]), ("Insein Prison", "Myanmar", ["Bangladesh", "Laos", "Cambodia"]),
 ("Kerobokan", "Indonesia", ["Malaysia", "the Philippines", "Papua New Guinea"]), ("Changi", "Singapore", ["Malaysia", "the Philippines", "Brunei"]),
 ("Fuchu Prison", "Japan", ["South Korea", "Taiwan", "China"]), ("The Presidio Modelo", "Cuba", ["Jamaica", "Haiti", "the Dominican Republic"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-45.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
