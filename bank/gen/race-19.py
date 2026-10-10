# Bank session 10 Oct 2026: 4 more general races -> bank/race-19.json. 20 rows each, target 10; wrong options are
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

race("name the famous bird", "Film, TV and books", "medium", ["birds", "characters"], [
 ("Sylvester's yellow canary", "Tweety", ["Sweetie", "Chirpy", "Granny"]), ("Snoopy's little yellow friend", "Woodstock", ["Lucy", "Linus", "Peppermint Patty"]),
 ("Jafar's parrot", "Iago", ["Abu", "Rajah", "Carpet"]), ("Harry's snowy owl", "Hedwig", ["Hermes", "Pigwidgeon", "Crookshanks"]),
 ("The Weasleys' ancient, crash-landing owl", "Errol", ["Hermes", "Pigwidgeon", "Scabbers"]), ("Sesame Street's eight-foot yellow bird", "Big Bird", ["Elmo", "Grover", "Oscar"]),
 ("'Meep meep!'", "Road Runner", ["Wile E. Coyote", "Speedy Gonzales", "Pepé Le Pew"]), ("The cartoon bird with the famous laugh", "Woody Woodpecker", ["Heckle", "Jeckle", "Buzz Buzzard"]),
 ("The giant bird in Up", "Kevin", ["Dug", "Russell", "Muntz"]), ("The Little Mermaid's know-it-all seagull", "Scuttle", ["Flounder", "Sebastian", "Max"]),
 ("Richard Bach's seagull who lives to fly", "Jonathan Livingston Seagull", ["Fletcher Lynd", "Chiang", "Sullivan"]), ("Watership Down's seagull", "Kehaar", ["Fiver", "Bigwig", "Holly"]),
 ("Dumbledore's phoenix", "Fawkes", ["Buckbeak", "Fluffy", "Aragog"]), ("Doctor Dolittle's parrot", "Polynesia", ["Jip", "Dab-Dab", "Gub-Gub"]),
 ("Long John Silver's parrot", "Captain Flint", ["Polly", "Billy Bones", "Ben Gunn"]), ("The leader of the Angry Birds", "Red", ["Chuck", "Bomb", "Terence"]),
 ("The rare macaw in Rio", "Blu", ["Jewel", "Nigel", "Rafael"]), ("The clay penguin who says 'Noot noot!'", "Pingu", ["Pinga", "Robby", "Pingg"]),
 ("Mufasa's hornbill adviser", "Zazu", ["Rafiki", "Timon", "Pumbaa"]), ("The wise bird of the Hundred Acre Wood", "Owl", ["Rabbit", "Eeyore", "Gopher"])])

race("which school do they go to?", "Film, TV and books", "medium", ["schools", "fiction"], [
 ("Harry Potter", "Hogwarts", ["Beauxbatons", "Durmstrang", "Ilvermorny"]), ("Matilda", "Crunchem Hall", ["Trunchbull Towers", "Wormwood Hall", "Honey Hall"]),
 ("Darrell Rivers", "Malory Towers", ["Whyteleafe", "The Chalet School", "Cliffe House"]), ("The wild girls of the Ealing comedies", "St Trinian's", ["St Custard's", "Whyteleafe", "The Chalet School"]),
 ("Billy Bunter", "Greyfriars", ["St Jim's", "Rookwood", "Linton Hall"]), ("Danny and Sandy in Grease", "Rydell High", ["Ridgemont High", "West Beverly High", "Hill Valley High"]),
 ("Zack Morris in Saved by the Bell", "Bayside High", ["Ridgemont High", "West Beverly High", "Hill Valley High"]), ("Bart Simpson", "Springfield Elementary", ["Shelbyville Elementary", "South Park Elementary", "Quahog Elementary"]),
 ("Buffy the Vampire Slayer", "Sunnydale High", ["Ridgemont High", "Mystic Falls High", "Hill Valley High"]), ("Will McKenzie in The Inbetweeners", "Rudge Park Comprehensive", ["Abbey Grove", "Waterloo Road", "Summerhill"]),
 ("The X-Men", "Xavier's School", ["Starfleet Academy", "Brakebills", "Wayne Academy"]), ("Wednesday Addams", "Nevermore Academy", ["Ravenwood Academy", "Miss Peregrine's Home", "Brakebills"]),
 ("Smike in Nicholas Nickleby", "Dotheboys Hall", ["Salem House", "Bleak House", "Satis House"]), ("Jane Eyre", "Lowood", ["Salem House", "Thornfield", "Gateshead Hall"]),
 ("Enid Blyton's O'Sullivan twins", "St Clare's", ["Whyteleafe", "The Chalet School", "Cliffe House"]), ("Dudley Dursley", "Smeltings", ["Stonewall High", "Eton", "Durmstrang"]),
 ("Tucker Jenkins", "Grange Hill", ["Waterloo Road", "Byker Grove", "Summerhill"]), ("Jessica and Elizabeth Wakefield", "Sweet Valley High", ["West Beverly High", "Ridgemont High", "Hill Valley High"]),
 ("The Breakfast Club", "Shermer High", ["Ridgemont High", "West Beverly High", "Hill Valley High"]), ("Troy and Gabriella in High School Musical", "East High", ["West High", "Ridgemont High", "Hill Valley High"])])

race("which Olympic sport is this from?", "The Olympics", "medium", ["Olympics", "sports", "terms"], [
 ("Épée", "Fencing", ["Karate", "Kendo", "Taekwondo"]), ("Pommel horse", "Gymnastics", ["Diving", "Wrestling", "Triathlon"]),
 ("Shuttlecock", "Badminton", ["Table tennis", "Squash", "Handball"]), ("Puck", "Ice hockey", ["Hockey", "Lacrosse", "Water polo"]),
 ("Coxless four", "Rowing", ["Triathlon", "Swimming", "Water polo"]), ("Javelin", "Athletics", ["Modern pentathlon", "Triathlon", "Biathlon"]),
 ("Stones and brooms", "Curling", ["Bobsleigh", "Speed skating", "Biathlon"]), ("Recurve bow", "Archery", ["Biathlon", "Modern pentathlon", "Triathlon"]),
 ("Lying feet-first on a sled", "Luge", ["Bobsleigh", "Biathlon", "Speed skating"]), ("Lying head-first on a sled", "Skeleton", ["Bobsleigh", "Biathlon", "Speed skating"]),
 ("Clay pigeons", "Shooting", ["Biathlon", "Modern pentathlon", "Triathlon"]), ("Dinghies", "Sailing", ["Triathlon", "Surfing", "Water polo"]),
 ("The peloton", "Cycling", ["Water polo", "Diving", "Handball"]), ("Tatami mats and ippons", "Judo", ["Taekwondo", "Wrestling", "Boxing"]),
 ("Kayaks", "Canoeing", ["Triathlon", "Swimming", "Water polo"]), ("Bunkers", "Golf", ["Hockey", "Rugby sevens", "Cricket"]),
 ("Dressage", "Equestrian", ["Diving", "Modern pentathlon", "Figure skating"]), ("The snatch", "Weightlifting", ["Wrestling", "Boxing", "Taekwondo"]),
 ("The libero", "Volleyball", ["Handball", "Water polo", "Basketball"]), ("Deuce", "Tennis", ["Basketball", "Handball", "Water polo"])])

race("which country is this wine region in?", "Food and drink", "hard", ["wine", "countries"], [
 ("Bordeaux", "France", ["Belgium", "Luxembourg", "Monaco"]), ("Rioja", "Spain", ["Andorra", "Mexico", "Uruguay"]),
 ("Chianti", "Italy", ["Croatia", "Slovenia", "Malta"]), ("Napa Valley", "the USA", ["Mexico", "Brazil", "Peru"]),
 ("The Barossa Valley", "Australia", ["Fiji", "Uruguay", "Brazil"]), ("Marlborough", "New Zealand", ["Wales", "Ireland", "Fiji"]),
 ("The Mosel", "Germany", ["Belgium", "the Netherlands", "Denmark"]), ("The Douro", "Portugal", ["Brazil", "Uruguay", "Mexico"]),
 ("Tokaj", "Hungary", ["Romania", "Czechia", "Bulgaria"]), ("Stellenbosch", "South Africa", ["Namibia", "Zimbabwe", "Kenya"]),
 ("Mendoza", "Argentina", ["Uruguay", "Peru", "Brazil"]), ("The Maipo Valley", "Chile", ["Peru", "Uruguay", "Bolivia"]),
 ("The Okanagan Valley", "Canada", ["Iceland", "Norway", "Denmark"]), ("The Wachau", "Austria", ["Czechia", "Slovenia", "Liechtenstein"]),
 ("Santorini", "Greece", ["Cyprus", "Turkey", "Malta"]), ("The Bekaa Valley", "Lebanon", ["Israel", "Syria", "Jordan"]),
 ("Lavaux", "Switzerland", ["Liechtenstein", "Luxembourg", "Belgium"]), ("Kakheti", "Georgia", ["Armenia", "Azerbaijan", "Ukraine"]),
 ("Sussex (for sparkling wine)", "England", ["Wales", "Ireland", "Denmark"]), ("The Cricova cellars", "Moldova", ["Romania", "Ukraine", "Bulgaria"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-19.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
