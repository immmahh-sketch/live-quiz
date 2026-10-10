# Bank session 10 Oct 2026: 4 more general races -> bank/race-37.json. 20 rows each, target 10; wrong options are
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

race("which two sang this duet?", "Music", "medium", ["duets", "songs"], [
 ("Islands in the Stream", "Kenny Rogers & Dolly Parton", ["Kenny Rogers & Sheena Easton", "Dolly Parton & Porter Wagoner", "Johnny Cash & June Carter"]),
 ("Don't Go Breaking My Heart", "Elton John & Kiki Dee", ["Elton John & George Michael", "Cliff Richard & Sarah Brightman", "Kiki Dee & Rod Stewart"]),
 ("Under Pressure", "Queen & David Bowie", ["Queen & Elton John", "David Bowie & Bing Crosby", "Queen & Annie Lennox"]),
 ("Ebony and Ivory", "Paul McCartney & Stevie Wonder", ["Paul McCartney & Michael Jackson", "Stevie Wonder & Diana Ross", "Lionel Richie & Michael Jackson"]),
 ("Shallow", "Lady Gaga & Bradley Cooper", ["Lady Gaga & Tony Bennett", "Lady Gaga & Beyoncé", "Lady Gaga & Ariana Grande"]),
 ("Fairytale of New York", "The Pogues & Kirsty MacColl", ["The Pogues & The Dubliners", "Shane MacGowan & Sinéad O'Connor", "Kirsty MacColl & Billy Bragg"]),
 ("Especially for You", "Kylie Minogue & Jason Donovan", ["Kylie Minogue & Robbie Williams", "Kylie Minogue & Nick Cave", "Sonia & Jason Donovan"]),
 ("Endless Love", "Diana Ross & Lionel Richie", ["Diana Ross & Marvin Gaye", "Roberta Flack & Peabo Bryson", "Lionel Richie & Michael Jackson"]),
 ("Up Where We Belong", "Joe Cocker & Jennifer Warnes", ["Bill Medley & Jennifer Warnes", "Patrick Swayze & Wendy Fraser", "Kenny Rogers & Sheena Easton"]),
 ("Don't Give Up", "Peter Gabriel & Kate Bush", ["Phil Collins & Philip Bailey", "Kate Bush & David Gilmour", "Annie Lennox & Al Green"]),
 ("Barcelona", "Freddie Mercury & Montserrat Caballé", ["Andrea Bocelli & Sarah Brightman", "José Carreras & Sarah Brightman", "Plácido Domingo & John Denver"]),
 ("You're the One That I Want", "John Travolta & Olivia Newton-John", ["Olivia Newton-John & Cliff Richard", "Olivia Newton-John & ELO", "Barry Gibb & Barbra Streisand"]),
 ("Picture", "Kid Rock & Sheryl Crow", ["Kenny Chesney & Grace Potter", "Tim McGraw & Faith Hill", "Garth Brooks & Trisha Yearwood"]),
 ("Dancing in the Street", "David Bowie & Mick Jagger", ["Mick Jagger & Tina Turner", "Rod Stewart & Tina Turner", "David Bowie & Bing Crosby"]),
 ("Señorita", "Shawn Mendes & Camila Cabello", ["Ed Sheeran & Justin Bieber", "Zayn & Taylor Swift", "Camila Cabello & Ed Sheeran"]),
 ("Ain't No Mountain High Enough", "Marvin Gaye & Tammi Terrell", ["Marvin Gaye & Kim Weston", "Marvin Gaye & Mary Wells", "Smokey Robinson & Diana Ross"]),
 ("I Knew You Were Waiting (For Me)", "Aretha Franklin & George Michael", ["Elton John & George Michael", "Aretha Franklin & Annie Lennox", "Whitney Houston & George Michael"]),
 ("Stop Draggin' My Heart Around", "Stevie Nicks & Tom Petty", ["Stevie Nicks & Don Henley", "Linda Ronstadt & Aaron Neville", "Tom Petty & Bob Dylan"]),
 ("Empire State of Mind", "Jay-Z & Alicia Keys", ["Jay-Z & Beyoncé", "Alicia Keys & Usher", "Eminem & Rihanna"]),
 ("Uptown Funk", "Mark Ronson & Bruno Mars", ["Bruno Mars & Anderson .Paak", "Mark Ronson & Amy Winehouse", "Pharrell Williams & Daft Punk"])])

race("which city hosted this world's fair?", "History", "hard", ["world's fairs", "Expo", "cities"], [
 ("The Great Exhibition of 1851", "London", ["Manchester", "Edinburgh", "Birmingham"]), ("Expo 67", "Montreal", ["Toronto", "Quebec City", "Ottawa"]),
 ("Expo 58, which gave us the Atomium", "Brussels", ["Antwerp", "Amsterdam", "Luxembourg"]), ("The 1889 fair that gave us the Eiffel Tower", "Paris", ["Lyon", "Marseille", "Bordeaux"]),
 ("The World's Columbian Exposition of 1893", "Chicago", ["New York", "Boston", "Detroit"]), ("The 1962 fair that gave us the Space Needle", "Seattle", ["Portland", "Denver", "Los Angeles"]),
 ("Expo '70", "Osaka", ["Tokyo", "Kyoto", "Nagoya"]), ("Expo '92", "Seville", ["Madrid", "Valencia", "Granada"]),
 ("Expo 2000", "Hanover", ["Berlin", "Munich", "Frankfurt"]), ("Expo 2010", "Shanghai", ["Beijing", "Hong Kong", "Guangzhou"]),
 ("Expo 2015", "Milan", ["Rome", "Turin", "Florence"]), ("Expo 2020 (held in 2021–22)", "Dubai", ["Abu Dhabi", "Doha", "Riyadh"]),
 ("Expo 86", "Vancouver", ["Calgary", "Toronto", "Victoria"]), ("Expo '98", "Lisbon", ["Porto", "Madrid", "Faro"]),
 ("The Louisiana Purchase Exposition of 1904", "St Louis", ["Kansas City", "New Orleans", "Memphis"]), ("The Panama–Pacific Exposition of 1915", "San Francisco", ["Los Angeles", "Sacramento", "Portland"]),
 ("World Expo 88", "Brisbane", ["Sydney", "Melbourne", "Perth"]), ("The International Exposition of 1929", "Barcelona", ["Madrid", "Valencia", "Bilbao"]),
 ("The Centennial Exposition of 1876", "Philadelphia", ["Boston", "New York", "Baltimore"]), ("The Weltausstellung of 1873", "Vienna", ["Berlin", "Munich", "Budapest"])])

race("in which city is this organisation based?", "Politics", "hard", ["organisations", "headquarters", "cities"], [
 ("The United Nations", "New York", ["Chicago", "Boston", "Toronto"]), ("The World Health Organization", "Geneva", ["Bern", "Basel", "Luxembourg"]),
 ("UNESCO", "Paris", ["Madrid", "Amsterdam", "Copenhagen"]), ("The International Atomic Energy Agency", "Vienna", ["Berlin", "Bonn", "Prague"]),
 ("The UN's Food and Agriculture Organization", "Rome", ["Milan", "Madrid", "Naples"]), ("NATO", "Brussels", ["Luxembourg", "Amsterdam", "Copenhagen"]),
 ("The International Criminal Court", "The Hague", ["Amsterdam", "Rotterdam", "Luxembourg"]), ("The European Central Bank", "Frankfurt", ["Berlin", "Bonn", "Munich"]),
 ("The International Monetary Fund", "Washington, DC", ["Chicago", "Boston", "Toronto"]), ("The International Olympic Committee", "Lausanne", ["Bern", "Basel", "Monaco"]),
 ("FIFA", "Zurich", ["Bern", "Basel", "Munich"]), ("UEFA", "Nyon", ["Bern", "Basel", "Monaco"]),
 ("Interpol", "Lyon", ["Marseille", "Luxembourg", "Bonn"]), ("The Council of Europe", "Strasbourg", ["Luxembourg", "Bonn", "Basel"]),
 ("The Commonwealth Secretariat", "London", ["Edinburgh", "Ottawa", "Dublin"]), ("The Arab League", "Cairo", ["Riyadh", "Beirut", "Doha"]),
 ("The African Union", "Addis Ababa", ["Lagos", "Johannesburg", "Accra"]), ("ASEAN", "Jakarta", ["Kuala Lumpur", "Singapore", "Bangkok"]),
 ("The UN Environment Programme", "Nairobi", ["Lagos", "Kampala", "Johannesburg"]), ("The World Anti-Doping Agency", "Montreal", ["Toronto", "Ottawa", "Bern"])])

race("which country are these ancient remains in?", "History", "medium", ["ancient sites", "archaeology", "countries"], [
 ("Petra", "Jordan", ["Syria", "Lebanon", "Saudi Arabia"]), ("Angkor Wat", "Cambodia", ["Thailand", "Laos", "Vietnam"]),
 ("Machu Picchu", "Peru", ["Bolivia", "Ecuador", "Chile"]), ("Chichén Itzá", "Mexico", ["Belize", "Honduras", "Colombia"]),
 ("Great Zimbabwe", "Zimbabwe", ["Mozambique", "Zambia", "Botswana"]), ("Persepolis", "Iran", ["Afghanistan", "Uzbekistan", "Syria"]),
 ("Ephesus", "Turkey", ["Cyprus", "Bulgaria", "Syria"]), ("Pompeii", "Italy", ["Malta", "Croatia", "Spain"]),
 ("Knossos", "Greece", ["Cyprus", "Malta", "Croatia"]), ("Carthage", "Tunisia", ["Algeria", "Morocco", "Lebanon"]),
 ("Babylon", "Iraq", ["Syria", "Kuwait", "Saudi Arabia"]), ("Mohenjo-daro", "Pakistan", ["India", "Afghanistan", "Bangladesh"]),
 ("Borobudur", "Indonesia", ["Malaysia", "the Philippines", "Thailand"]), ("Bagan", "Myanmar", ["Thailand", "Laos", "Bangladesh"]),
 ("Tikal", "Guatemala", ["Belize", "Honduras", "Colombia"]), ("Skara Brae", "Scotland", ["Norway", "Wales", "Iceland"]),
 ("Newgrange", "Ireland", ["Wales", "the Isle of Man", "Iceland"]), ("Leptis Magna", "Libya", ["Algeria", "Morocco", "Sudan"]),
 ("Abu Simbel", "Egypt", ["Sudan", "Eritrea", "Saudi Arabia"]), ("Lalibela's rock churches", "Ethiopia", ["Eritrea", "Sudan", "Kenya"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-37.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
