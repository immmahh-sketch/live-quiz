# Bank session 9 Oct 2026: 10 more general races -> bank/race-2.json. 20 rows each, target 10; wrong options are the
# same kind of thing and never another row's right answer (no recycling).
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3, (title, q)
        bad = [w for w in wrong if w in rights]
        assert not bad, (title, q, 'recycled', bad)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("what's the main language spoken here?", "Geography", "medium", ["languages", "countries"], [
 ("Brazil", "Portuguese", ["Italian", "Catalan", "Basque"]), ("Austria", "German", ["Czech", "Polish", "Danish"]), ("Egypt", "Arabic", ["Kurdish", "Somali", "Hausa"]),
 ("Iran", "Persian", ["Kurdish", "Hindi", "Armenian"]), ("The Netherlands", "Dutch", ["Flemish", "Danish", "Afrikaans"]), ("Argentina", "Spanish", ["Italian", "Catalan", "Basque"]),
 ("Pakistan", "Urdu", ["Hindi", "Punjabi", "Tamil"]), ("Israel", "Hebrew", ["Yiddish", "Armenian", "Kurdish"]), ("Kenya", "Swahili", ["Zulu", "Hausa", "Somali"]),
 ("Ethiopia", "Amharic", ["Somali", "Zulu", "Hausa"]), ("Quebec, in Canada", "French", ["Latin", "Catalan", "Italian"]), ("Indonesia", "Indonesian", ["Malay", "Vietnamese", "Khmer"]),
 ("The Philippines", "Filipino", ["Malay", "Khmer", "Burmese"]), ("Bangladesh", "Bengali", ["Hindi", "Punjabi", "Tamil"]), ("Hungary", "Hungarian", ["Slovak", "Czech", "Polish"]),
 ("Malta", "Maltese", ["Italian", "Greek", "Latin"]), ("Thailand", "Thai", ["Lao", "Khmer", "Burmese"]), ("Turkey", "Turkish", ["Greek", "Armenian", "Kurdish"]),
 ("Finland", "Finnish", ["Russian", "Estonian", "Danish"]), ("Romania", "Romanian", ["Bulgarian", "Serbian", "Albanian"])])

race("what's the everyday name for this part of the body?", "The human body", "medium", ["body", "words"], [
 ("Patella", "Kneecap", ["Shin bone", "Elbow", "Heel"]), ("Clavicle", "Collarbone", ["Backbone", "Rib", "Cheekbone"]), ("Scapula", "Shoulder blade", ["Hip bone", "Rib", "Backbone"]),
 ("Sternum", "Breastbone", ["Backbone", "Hip bone", "Rib"]), ("Cranium", "Skull", ["Cheekbone", "Temple", "Backbone"]), ("Femur", "Thigh bone", ["Shin bone", "Funny bone", "Hip bone"]),
 ("Mandible", "Jawbone", ["Cheekbone", "Temple", "Adam's apple"]), ("Larynx", "Voice box", ["Tonsils", "Spleen", "Earlobe"]), ("Trachea", "Windpipe", ["Tonsils", "Spleen", "Appendix"]),
 ("Oesophagus", "Gullet", ["Appendix", "Spleen", "Tonsils"]), ("Hallux", "Big toe", ["Little toe", "Heel", "Instep"]), ("Pollex", "Thumb", ["Little finger", "Knuckle", "Palm"]),
 ("Tympanic membrane", "Eardrum", ["Earlobe", "Eyelid", "Temple"]), ("Coccyx", "Tailbone", ["Hip bone", "Funny bone", "Backbone"]), ("Umbilicus", "Belly button", ["Earlobe", "Instep", "Knuckle"]),
 ("Axilla", "Armpit", ["Elbow", "Instep", "Knuckle"]), ("Carpus", "Wrist", ["Elbow", "Knuckle", "Heel"]), ("Tarsus", "Ankle", ["Heel", "Instep", "Shin"]),
 ("Gluteus maximus", "Buttock", ["Calf", "Hamstring", "Thigh"]), ("Nares", "Nostrils", ["Earlobes", "Eyelids", "Tonsils"])])

race("where is this TV detective based?", "Film and TV", "medium", ["TV", "crime dramas"], [
 ("Inspector Morse", "Oxford", ["Cambridge", "Bath", "Brighton"]), ("Inspector Rebus", "Edinburgh", ["Aberdeen", "Dundee", "Inverness"]), ("Taggart", "Glasgow", ["Aberdeen", "Dundee", "Inverness"]),
 ("John Luther", "London", ["Liverpool", "Birmingham", "Leeds"]), ("Jim Bergerac", "Jersey", ["Guernsey", "Isle of Man", "Isle of Wight"]), ("Eddie Shoestring", "Bristol", ["Bath", "Cardiff", "Plymouth"]),
 ("Kurt Wallander", "Ystad", ["Malmö", "Stockholm", "Gothenburg"]), ("Jules Maigret", "Paris", ["Lyon", "Marseille", "Brussels"]), ("Columbo", "Los Angeles", ["San Francisco", "Chicago", "Miami"]),
 ("Kojak", "New York", ["Chicago", "Boston", "Philadelphia"]), ("Thomas Magnum", "Hawaii", ["Florida", "California", "Puerto Rico"]), ("Fitz, in Cracker", "Manchester", ["Liverpool", "Leeds", "Sheffield"]),
 ("Tom Mathias, in Hinterland", "Aberystwyth", ["Swansea", "Cardiff", "Bangor"]), ("Van der Valk", "Amsterdam", ["Rotterdam", "The Hague", "Antwerp"]), ("Sarah Lund, in The Killing", "Copenhagen", ["Stockholm", "Oslo", "Malmö"]),
 ("Inspector Montalbano", "Sicily", ["Sardinia", "Naples", "Corsica"]), ("Inspector Rex", "Vienna", ["Munich", "Berlin", "Zurich"]), ("Jimmy Perez", "Shetland", ["Orkney", "Isle of Skye", "Isle of Lewis"]),
 ("Dalziel and Pascoe", "Yorkshire", ["Lancashire", "Derbyshire", "Cumbria"]), ("Jessica Fletcher, in Murder, She Wrote", "Cabot Cove", ["Twin Peaks", "Stars Hollow", "Sunnydale"])])

race("which Shakespeare play is this character from?", "Books and literature", "hard", ["Shakespeare", "plays"], [
 ("Shylock", "The Merchant of Venice", ["Measure for Measure", "The Two Gentlemen of Verona", "Timon of Athens"]), ("Puck", "A Midsummer Night's Dream", ["Love's Labour's Lost", "The Merry Wives of Windsor", "Pericles"]),
 ("Prospero", "The Tempest", ["Pericles", "Measure for Measure", "King John"]), ("Iago", "Othello", ["Coriolanus", "Henry V", "Timon of Athens"]),
 ("Ophelia", "Hamlet", ["Coriolanus", "King John", "Henry V"]), ("Banquo", "Macbeth", ["Henry V", "King John", "Coriolanus"]),
 ("Mercutio", "Romeo and Juliet", ["The Two Gentlemen of Verona", "Love's Labour's Lost", "Measure for Measure"]), ("Cordelia", "King Lear", ["King John", "Coriolanus", "Timon of Athens"]),
 ("Malvolio", "Twelfth Night", ["Love's Labour's Lost", "All's Well That Ends Well", "The Merry Wives of Windsor"]), ("Petruchio", "The Taming of the Shrew", ["The Two Gentlemen of Verona", "All's Well That Ends Well", "Measure for Measure"]),
 ("Brutus", "Julius Caesar", ["Coriolanus", "Timon of Athens", "Troilus and Cressida"]), ("Benedick", "Much Ado About Nothing", ["All's Well That Ends Well", "Love's Labour's Lost", "Measure for Measure"]),
 ("Rosalind", "As You Like It", ["Love's Labour's Lost", "All's Well That Ends Well", "The Merry Wives of Windsor"]), ("Leontes", "The Winter's Tale", ["Pericles", "Measure for Measure", "Timon of Athens"]),
 ("Imogen", "Cymbeline", ["Pericles", "Troilus and Cressida", "King John"]), ("Aaron the Moor", "Titus Andronicus", ["Coriolanus", "Timon of Athens", "Henry V"]),
 ("Lady Anne", "Richard III", ["Henry VIII", "King John", "Henry V"]), ("Bolingbroke", "Richard II", ["King John", "Henry VIII", "Coriolanus"]),
 ("Enobarbus", "Antony and Cleopatra", ["Coriolanus", "Troilus and Cressida", "Timon of Athens"]), ("Dromio", "The Comedy of Errors", ["The Two Gentlemen of Verona", "Measure for Measure", "Love's Labour's Lost"])])

race("which car maker makes this model?", "Cars and motoring", "easy", ["cars", "brands"], [
 ("Fiesta", "Ford", ["Mazda", "Suzuki", "Chevrolet"]), ("Golf", "Volkswagen", ["Mazda", "Saab", "Subaru"]), ("Corsa", "Vauxhall", ["Mazda", "Suzuki", "Dacia"]),
 ("Clio", "Renault", ["Dacia", "Lancia", "Smart"]), ("Qashqai", "Nissan", ["Mitsubishi", "Subaru", "Suzuki"]), ("Yaris", "Toyota", ["Mazda", "Daihatsu", "Lexus"]),
 ("Civic", "Honda", ["Mitsubishi", "Mazda", "Subaru"]), ("911", "Porsche", ["Ferrari", "Lotus", "Maserati"]), ("Punto", "Fiat", ["Lancia", "Alfa Romeo", "Smart"]),
 ("Octavia", "Skoda", ["Lada", "Dacia", "Saab"]), ("Ibiza", "SEAT", ["Lancia", "Alfa Romeo", "Dacia"]), ("3 Series", "BMW", ["Mercedes-Benz", "Lexus", "Saab"]),
 ("A4", "Audi", ["Mercedes-Benz", "Lexus", "Infiniti"]), ("Defender", "Land Rover", ["Jeep", "Rover", "Suzuki"]), ("Model S", "Tesla", ["Chevrolet", "Polestar", "Genesis"]),
 ("208", "Peugeot", ["Dacia", "Smart", "Lancia"]), ("C3", "Citroën", ["Dacia", "Lancia", "Smart"]), ("Sportage", "Kia", ["Mitsubishi", "Suzuki", "SsangYong"]),
 ("Tucson", "Hyundai", ["Mitsubishi", "SsangYong", "Suzuki"]), ("XC90", "Volvo", ["Saab", "Lexus", "Infiniti"])])

race("which instrument is this musician famous for?", "Music", "medium", ["instruments", "musicians"], [
 ("Jimi Hendrix", "Guitar", ["Mandolin", "Synthesiser", "Double bass"]), ("Ringo Starr", "Drums", ["Xylophone", "Glockenspiel", "Tuba"]), ("Yo-Yo Ma", "Cello", ["Viola", "Double bass", "Oboe"]),
 ("Louis Armstrong", "Trumpet", ["French horn", "Tuba", "Euphonium"]), ("Charlie Parker", "Saxophone", ["Oboe", "Bassoon", "Euphonium"]), ("Larry Adler", "Harmonica", ["Recorder", "Piccolo", "Zither"]),
 ("Evelyn Glennie", "Percussion", ["Harpsichord", "Viola", "Oboe"]), ("Nicola Benedetti", "Violin", ["Viola", "Oboe", "Harpsichord"]), ("Paul McCartney", "Bass guitar", ["Mandolin", "Synthesiser", "Lute"]),
 ("Elton John", "Piano", ["Harpsichord", "Synthesiser", "Glockenspiel"]), ("Acker Bilk", "Clarinet", ["Oboe", "Bassoon", "Recorder"]), ("James Galway", "Flute", ["Recorder", "Oboe", "Bassoon"]),
 ("Glenn Miller", "Trombone", ["Tuba", "Euphonium", "French horn"]), ("Ravi Shankar", "Sitar", ["Lute", "Zither", "Mandolin"]), ("Bez, of the Happy Mondays", "Maracas", ["Tambourine", "Triangle", "Bongos"]),
 ("Harpo Marx", "Harp", ["Lyre", "Zither", "Harpsichord"]), ("Jimmy Shand", "Accordion", ["Bagpipes", "Mandolin", "Xylophone"]), ("Earl Scruggs", "Banjo", ["Mandolin", "Lute", "Zither"]),
 ("George Formby", "Ukulele", ["Mandolin", "Lute", "Zither"]), ("Reginald Dixon, at Blackpool Tower", "Organ", ["Harpsichord", "Synthesiser", "Glockenspiel"])])

race("which country has this capital?", "Geography", "medium", ["capitals", "countries"], [
 ("Canberra", "Australia", ["South Africa", "Fiji", "Papua New Guinea"]), ("Ottawa", "Canada", ["Finland", "Sweden", "Denmark"]), ("Wellington", "New Zealand", ["Fiji", "Papua New Guinea", "South Africa"]),
 ("Brasília", "Brazil", ["Argentina", "Colombia", "Venezuela"]), ("Ankara", "Turkey", ["Greece", "Cyprus", "Azerbaijan"]), ("Bern", "Switzerland", ["Austria", "Belgium", "Slovenia"]),
 ("Nairobi", "Kenya", ["Uganda", "Tanzania", "Ethiopia"]), ("Hanoi", "Vietnam", ["Cambodia", "Laos", "Thailand"]), ("Lima", "Peru", ["Chile", "Bolivia", "Colombia"]),
 ("Oslo", "Norway", ["Sweden", "Denmark", "Finland"]), ("Rabat", "Morocco", ["Algeria", "Tunisia", "Egypt"]), ("Kathmandu", "Nepal", ["Bhutan", "Bangladesh", "Laos"]),
 ("Reykjavík", "Iceland", ["Denmark", "Finland", "Sweden"]), ("Tallinn", "Estonia", ["Latvia", "Lithuania", "Finland"]), ("Bratislava", "Slovakia", ["Czechia", "Slovenia", "Hungary"]),
 ("Valletta", "Malta", ["Cyprus", "Greece", "Slovenia"]), ("Quito", "Ecuador", ["Bolivia", "Paraguay", "Uruguay"]), ("Accra", "Ghana", ["Nigeria", "Senegal", "Ivory Coast"]),
 ("Tbilisi", "Georgia", ["Armenia", "Azerbaijan", "Kazakhstan"]), ("Ulaanbaatar", "Mongolia", ["Kazakhstan", "Uzbekistan", "Bhutan"])])

race("which cheese is this?", "Food and drink", "medium", ["cheese", "food"], [
 ("Blue cheese that can only be made in Nottinghamshire, Derbyshire or Leicestershire", "Stilton", ["Shropshire Blue", "Danish Blue", "Cambozola"]),
 ("Hard Italian cheese from around Parma, grated over pasta", "Parmesan", ["Asiago", "Provolone", "Fontina"]),
 ("Soft white Italian cheese on a classic margherita pizza", "Mozzarella", ["Burrata", "Provolone", "Fontina"]),
 ("Crumbly salty cheese in a Greek salad", "Feta", ["Labneh", "Cottage cheese", "Cotija"]),
 ("Dutch cheese in a red wax coat", "Edam", ["Leerdammer", "Jarlsberg", "Raclette"]),
 ("Soft cheese from Normandy, sold in a little round wooden box", "Camembert", ["Port Salut", "Reblochon", "Boursin"]),
 ("Squeaky cheese from Cyprus that's often grilled", "Halloumi", ["Labneh", "Cotija", "Provolone"]),
 ("Swiss cheese famous for the holes in it", "Emmental", ["Gruyère", "Jarlsberg", "Raclette"]),
 ("Britain's favourite cheese, named after a village in Somerset", "Cheddar", ["Cheshire", "Caerphilly", "Double Gloucester"]),
 ("French blue cheese made from sheep's milk and aged in caves", "Roquefort", ["Danish Blue", "Cambozola", "Dolcelatte"]),
 ("Italian blue cheese, named after a town near Milan", "Gorgonzola", ["Taleggio", "Fontina", "Danish Blue"]),
 ("Creamy Italian cheese that goes into tiramisu", "Mascarpone", ["Burrata", "Boursin", "Cottage cheese"]),
 ("Soft French cheese from near Paris, once crowned 'the king of cheeses'", "Brie", ["Port Salut", "Reblochon", "Munster"]),
 ("Crumbly orange cheese from the East Midlands", "Red Leicester", ["Double Gloucester", "Cheshire", "Cornish Yarg"]),
 ("Crumbly Yorkshire cheese that Wallace loves, eaten with Christmas cake", "Wensleydale", ["Cheshire", "Caerphilly", "Lancashire"]),
 ("Spanish sheep's milk cheese from La Mancha", "Manchego", ["Asiago", "Comté", "Gruyère"]),
 ("Dutch cheese named after a town near Rotterdam", "Gouda", ["Leerdammer", "Jarlsberg", "Munster"]),
 ("Fresh Indian cheese cubed into curries like palak and mattar", "Paneer", ["Labneh", "Cotija", "Cottage cheese"]),
 ("Soft Italian cheese inside cannoli", "Ricotta", ["Burrata", "Taleggio", "Boursin"]),
 ("Hard sheep's milk cheese from Rome, used in a proper carbonara", "Pecorino", ["Asiago", "Provolone", "Comté"])])

race("what's this Roman numeral?", "Maths", "medium", ["numbers", "Roman numerals"], [
 ("XIV", "14", ["16", "6", "114"]), ("XL", "40", ["60", "10", "50"]), ("XC", "90", ["110", "190", "10"]), ("CD", "400", ["600", "1400", "500"]),
 ("MCMLXVI", "1966", ["1946", "1961", "1964"]), ("IX", "9", ["11", "8", "6"]), ("LXX", "70", ["20", "75", "60"]), ("XLII", "42", ["62", "38", "52"]),
 ("MM", "2000", ["1000", "200", "1100"]), ("DCC", "700", ["300", "600", "800"]), ("XIX", "19", ["21", "11", "29"]), ("CM", "900", ["1100", "800", "1500"]),
 ("LV", "55", ["45", "65", "56"]), ("XXIV", "24", ["26", "34", "22"]), ("MMXXVI", "2026", ["2024", "2016", "2046"]), ("XCIX", "99", ["109", "89", "101"]),
 ("CCL", "250", ["150", "350", "1250"]), ("LXXX", "80", ["30", "85", "130"]), ("MCM", "1900", ["2100", "1100", "1800"]), ("XXXIX", "39", ["41", "31", "49"])])

race("which spelling is right?", "Words and language", "medium", ["spelling", "words"], [
 ("Somewhere to stay", "Accommodation", ["Accomodation", "Acommodation", "Accommadation"]), ("Needed", "Necessary", ["Neccessary", "Necesary", "Neccesary"]), ("Strange, not normal", "Weird", ["Wierd", "Weerd", "Wiered"]),
 ("The day after today", "Tomorrow", ["Tommorow", "Tommorrow", "Tomorow"]), ("Apart, not together", "Separate", ["Seperate", "Seperete", "Separete"]), ("Without any doubt", "Definitely", ["Definately", "Definitly", "Defenitely"]),
 ("Make someone go red in the face", "Embarrass", ["Embarass", "Embaras", "Embarras"]), ("Happened", "Occurred", ["Occured", "Ocurred", "Ocured"]), ("The beat of a song", "Rhythm", ["Rythm", "Rhythym", "Rhytm"]),
 ("Be given something", "Receive", ["Recieve", "Receeve", "Recive"]), ("A thousand years", "Millennium", ["Millenium", "Milennium", "Milenium"]), ("The inner voice telling right from wrong", "Conscience", ["Concience", "Consience", "Conscence"]),
 ("A list of questions for a survey", "Questionnaire", ["Questionaire", "Questionairre", "Questionnair"]), ("Work with others and pass on messages", "Liaise", ["Liase", "Liaze", "Laise"]), ("Naughty in a playful way", "Mischievous", ["Mischievious", "Mischevious", "Mischivous"]),
 ("Red tape", "Bureaucracy", ["Beaurocracy", "Bureaucrasy", "Burocracy"]), ("An ancient Egyptian king", "Pharaoh", ["Pharoah", "Pharoh", "Faraoh"]), ("A promise that something will work", "Guarantee", ["Garantee", "Guarentee", "Gaurantee"]),
 ("Where you go to eat out", "Restaurant", ["Restraunt", "Resturant", "Restaurent"]), ("A careful move, like parking", "Manoeuvre", ["Manouvre", "Manoeuver", "Manuever"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written, all checked: 20 rows, no repeats, no recycled answers')
