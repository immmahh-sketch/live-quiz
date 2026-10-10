# Bank session 10 Oct 2026: 4 more general races -> bank/race-42.json. 20 rows each, target 10; wrong options are
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

race("what does this first name originally mean?", "Words and language", "medium", ["names", "meanings"], [
 ("Sophia", "Wisdom", ["Grace", "Beauty", "Hope"]), ("Peter", "Rock", ["King", "Fisherman", "Shepherd"]),
 ("Philip", "Lover of horses", ["Lover of books", "Lover of the sea", "Lover of wine"]), ("Lucy", "Light", ["Moon", "Grace", "Joy"]),
 ("Margaret", "Pearl", ["Rose", "Diamond", "Silver"]), ("Leo", "Lion", ["Wolf", "Eagle", "Bear"]),
 ("Felix", "Lucky", ["Brave", "Noble", "Wise"]), ("Irene", "Peace", ["Hope", "Faith", "Joy"]),
 ("Barbara", "Stranger", ["Princess", "Warrior", "Queen"]), ("Andrew", "Manly", ["Gentle", "Wise", "Noble"]),
 ("George", "Farmer", ["Warrior", "Shepherd", "Sailor"]), ("Christopher", "Christ-bearer", ["Christ's servant", "Christ's friend", "Christ's soldier"]),
 ("Esther", "Star", ["Moon", "Flower", "Queen"]), ("Ursula", "Little bear", ["Little wolf", "Little dove", "Little queen"]),
 ("Stephen", "Crown", ["Sword", "Shield", "King"]), ("Amanda", "Worthy of love", ["Gift of God", "Full of grace", "Born in spring"]),
 ("Daniel", "God is my judge", ["God is gracious", "God is my strength", "God is with us"]), ("Oliver", "Olive tree", ["Oak tree", "Apple tree", "Holly bush"]),
 ("Melissa", "Honeybee", ["Butterfly", "Songbird", "Ladybird"]), ("Thomas", "Twin", ["Brother", "Firstborn", "Gift"])])

race("which county is this landmark in?", "Britain", "medium", ["landmarks", "counties", "England"], [
 ("Stonehenge", "Wiltshire", ["Hampshire", "Berkshire", "Gloucestershire"]), ("Blackpool Tower", "Lancashire", ["Merseyside", "Greater Manchester", "West Yorkshire"]),
 ("The Angel of the North", "Tyne and Wear", ["Cleveland", "West Yorkshire", "South Yorkshire"]), ("Cheddar Gorge", "Somerset", ["Devon", "Gloucestershire", "Herefordshire"]),
 ("Durdle Door", "Dorset", ["Devon", "Hampshire", "the Isle of Wight"]), ("The White Cliffs of Dover", "Kent", ["Essex", "West Sussex", "Surrey"]),
 ("Land's End", "Cornwall", ["Devon", "the Isle of Wight", "Hampshire"]), ("Warwick Castle", "Warwickshire", ["Worcestershire", "Leicestershire", "Staffordshire"]),
 ("Blenheim Palace", "Oxfordshire", ["Buckinghamshire", "Berkshire", "Gloucestershire"]), ("Chatsworth House", "Derbyshire", ["Nottinghamshire", "Staffordshire", "South Yorkshire"]),
 ("Whitby Abbey", "North Yorkshire", ["East Riding of Yorkshire", "West Yorkshire", "Cleveland"]), ("Alnwick Castle", "Northumberland", ["Cleveland", "East Riding of Yorkshire", "Berwickshire"]),
 ("Durham Cathedral", "County Durham", ["Cleveland", "West Yorkshire", "East Riding of Yorkshire"]), ("Sandringham House", "Norfolk", ["Lincolnshire", "Cambridgeshire", "Essex"]),
 ("Beachy Head", "East Sussex", ["West Sussex", "Surrey", "Hampshire"]), ("The Iron Bridge", "Shropshire", ["Staffordshire", "Herefordshire", "Worcestershire"]),
 ("Windermere", "Cumbria", ["Greater Manchester", "Merseyside", "West Yorkshire"]), ("Silverstone", "Northamptonshire", ["Bedfordshire", "Leicestershire", "Cambridgeshire"]),
 ("Sutton Hoo", "Suffolk", ["Essex", "Cambridgeshire", "Lincolnshire"]), ("Jodrell Bank", "Cheshire", ["Staffordshire", "Greater Manchester", "Merseyside"])])

race("what's the capital of this Indian state?", "World geography", "hard", ["India", "states", "capitals"], [
 ("Maharashtra", "Mumbai", ["Pune", "Nagpur", "Nashik"]), ("Karnataka", "Bengaluru", ["Mysuru", "Mangaluru", "Hubli"]),
 ("Tamil Nadu", "Chennai", ["Madurai", "Coimbatore", "Tiruchirappalli"]), ("West Bengal", "Kolkata", ["Darjeeling", "Siliguri", "Durgapur"]),
 ("Kerala", "Thiruvananthapuram", ["Kochi", "Kozhikode", "Thrissur"]), ("Rajasthan", "Jaipur", ["Udaipur", "Jodhpur", "Ajmer"]),
 ("Uttar Pradesh", "Lucknow", ["Agra", "Varanasi", "Kanpur"]), ("Gujarat", "Gandhinagar", ["Ahmedabad", "Surat", "Vadodara"]),
 ("Punjab", "Chandigarh", ["Amritsar", "Ludhiana", "Jalandhar"]), ("Goa", "Panaji", ["Margao", "Vasco da Gama", "Mapusa"]),
 ("Bihar", "Patna", ["Gaya", "Bhagalpur", "Muzaffarpur"]), ("Telangana", "Hyderabad", ["Warangal", "Visakhapatnam", "Vijayawada"]),
 ("Madhya Pradesh", "Bhopal", ["Indore", "Gwalior", "Jabalpur"]), ("Odisha", "Bhubaneswar", ["Cuttack", "Puri", "Rourkela"]),
 ("Assam", "Dispur", ["Silchar", "Dibrugarh", "Jorhat"]), ("Himachal Pradesh", "Shimla", ["Manali", "Kullu", "Mandi"]),
 ("Uttarakhand", "Dehradun", ["Haridwar", "Rishikesh", "Nainital"]), ("Jharkhand", "Ranchi", ["Jamshedpur", "Dhanbad", "Bokaro"]),
 ("Sikkim", "Gangtok", ["Darjeeling", "Pelling", "Namchi"]), ("Meghalaya", "Shillong", ["Tura", "Cherrapunji", "Jowai"])])

race("whose sidekick is this?", "Film and TV", "medium", ["sidekicks", "characters"], [
 ("Dr Watson", "Sherlock Holmes", ["Father Brown", "Albert Campion", "Inspector Clouseau"]), ("Captain Hastings", "Hercule Poirot", ["Miss Marple", "Father Brown", "Inspector Clouseau"]),
 ("Sergeant Lewis", "Inspector Morse", ["Inspector Frost", "Inspector Rebus", "Vera Stanhope"]), ("Sergeant Hathaway", "Inspector Lewis", ["Inspector Frost", "Inspector Rebus", "Vera Stanhope"]),
 ("Robin", "Batman", ["Superman", "Spider-Man", "Zorro"]), ("Tonto", "The Lone Ranger", ["Zorro", "Davy Crockett", "Buffalo Bill"]),
 ("Kato", "The Green Hornet", ["Zorro", "The Phantom", "The Shadow"]), ("Bunter", "Lord Peter Wimsey", ["Albert Campion", "Father Brown", "Lord Emsworth"]),
 ("Archie Goodwin", "Nero Wolfe", ["Columbo", "Philip Marlowe", "Sam Spade"]), ("Sergeant Troy", "Inspector Barnaby", ["Inspector Frost", "Vera Stanhope", "Inspector Rebus"]),
 ("Jeeves", "Bertie Wooster", ["Lord Emsworth", "Albert Campion", "Psmith"]), ("Sancho Panza", "Don Quixote", ["Gulliver", "Robinson Crusoe", "Tom Jones"]),
 ("Passepartout", "Phileas Fogg", ["Captain Nemo", "Professor Lidenbrock", "Robinson Crusoe"]), ("Igor", "Dr Frankenstein", ["Dracula", "Dr Jekyll", "Count Orlok"]),
 ("Chewbacca", "Han Solo", ["Luke Skywalker", "Lando Calrissian", "Obi-Wan Kenobi"]), ("Donkey", "Shrek", ["Puss in Boots", "Lord Farquaad", "Prince Charming"]),
 ("Baldrick", "Blackadder", ["Captain Mainwaring", "Rimmer", "Basil Fawlty"]), ("Goose", "Maverick", ["Iceman", "Viper", "Jester"]),
 ("Ron Weasley", "Harry Potter", ["Neville Longbottom", "Draco Malfoy", "Cedric Diggory"]), ("Sergeant Havers", "Inspector Lynley", ["Inspector Frost", "Vera Stanhope", "Inspector Rebus"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-42.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
