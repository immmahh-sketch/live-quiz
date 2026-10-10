# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-9.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Characters in Wallace & Gromit (watch for impostors)", "Film and TV", "medium", ["Wallace & Gromit", "Aardman"],
 ["Wallace", "Gromit", "Feathers McGraw", "Shaun", "Preston", "Lady Tottington", "Victor Quartermaine", "Hutch", "Wendolene", "Piella Bakewell", "Fluffles", "PC Mackintosh", "Norbot", "Mrs. Mulch", "Philip"],
 ["Mr. Bunkers", "Lady Cheddar", "Colonel Crumpet", "Feathers McFly", "Inspector Gouda"])
board("Characters in Mamma Mia! (watch for impostors)", "Musicals", "medium", ["Mamma Mia!", "musicals"],
 ["Donna", "Sophie", "Sky", "Sam", "Bill", "Harry", "Tanya", "Rosie", "Ali", "Lisa", "Pepper", "Eddie", "Ruby", "Fernando", "Young Donna"],
 ["Marco", "Carlos", "Bianca", "Ricky", "Elena"])
board("Characters in the Shrek films (watch for impostors)", "Film", "medium", ["Shrek", "DreamWorks"],
 ["Shrek", "Donkey", "Fiona", "Puss in Boots", "Lord Farquaad", "Dragon", "Gingy", "Pinocchio", "Fairy Godmother", "Prince Charming", "King Harold", "Queen Lillian", "Rumpelstiltskin", "Doris", "Mongo"],
 ["Lord Farthing", "Sir Grumble", "Duke Dagwood", "Princess Petunia", "Gingerella"])
board("Characters in the Frozen films (watch for impostors)", "Film", "medium", ["Frozen", "Disney"],
 ["Elsa", "Anna", "Olaf", "Kristoff", "Sven", "Hans", "The Duke of Weselton", "Oaken", "Grand Pabbie", "Marshmallow", "Bulda", "King Agnarr", "Queen Iduna", "Bruni", "Honeymaren"],
 ["Prince Frederik", "Queen Astrid", "Ingrid", "Bjorn", "Lars"])
board("Clubs in the 2025–26 Championship", "Football", "hard", ["Championship", "clubs"],
 ["Birmingham City", "Blackburn Rovers", "Bristol City", "Charlton Athletic", "Coventry City", "Derby County", "Hull City", "Ipswich Town", "Leicester City", "Middlesbrough", "Millwall", "Norwich City", "Portsmouth", "Wrexham", "Southampton"],
 ["Luton Town", "Plymouth Argyle", "Cardiff City", "Sunderland", "Leeds United"])
board("Blue Peter pets", "Nostalgia", "hard", ["Blue Peter", "pets"],
 ["Petra", "Shep", "Goldie", "Bonnie", "Mabel", "Lucy", "Meg", "Socks", "Cookie", "Barney", "Jason", "Jack", "Jill", "Freda", "George"],
 ["Rover", "Biscuit", "Patch", "Timmy", "Sooty"])
board("Characters in Grease", "Musicals", "medium", ["Grease", "musicals"],
 ["Danny Zuko", "Sandy Olsson", "Rizzo", "Kenickie", "Frenchy", "Marty", "Jan", "Doody", "Sonny", "Putzie", "Cha-Cha", "Patty Simcox", "Eugene", "Coach Calhoun", "Teen Angel"],
 ["Johnny Castle", "Ren McCormack", "Tony Manero", "Baby Houseman", "Ariel Moore"])
board("Characters in Dad's Army (watch for impostors)", "Comedy", "medium", ["Dad's Army", "sitcoms"],
 ["Captain Mainwaring", "Sergeant Wilson", "Lance Corporal Jones", "Private Frazer", "Private Godfrey", "Private Pike", "Private Walker", "ARP Warden Hodges", "The Vicar", "The Verger", "Mrs Pike", "Private Sponge", "Mrs Fox", "Captain Square", "Elizabeth Mainwaring"],
 ["Corporal Cummings", "Private Parker", "Sergeant Bristow", "Major Pritchard", "Private Gibbs"])
board("Characters in The Lion King films", "Film", "easy", ["The Lion King", "Disney"],
 ["Simba", "Mufasa", "Scar", "Nala", "Timon", "Pumbaa", "Rafiki", "Zazu", "Sarabi", "Shenzi", "Banzai", "Ed", "Kiara", "Kovu", "Zira"],
 ["Kimba", "Sabor", "Diego", "Alex", "Aslan"])
board("Sidekicks of British TV detectives", "Film and TV", "hard", ["detectives", "sidekicks"],
 ["Lewis", "Hathaway", "Hastings", "Watson", "Troy", "Pascoe", "George Toolan", "Siobhan Clarke", "Joe Ashworth", "Aiden Healy", "Maddy Magellan", "Mike Leckie", "Robin Ellacott", "Bunter", "Barbara Havers"],
 ["Sergeant Price", "Constable Wright", "DS Fowler", "DC Hughes", "Sergeant Dawes"])
board("Characters in Bluey (watch for impostors)", "Film and TV", "medium", ["Bluey", "children's TV"],
 ["Bluey", "Bingo", "Bandit", "Chilli", "Muffin", "Socks", "Stripe", "Trixie", "Nana", "Uncle Rad", "Coco", "Chloe", "Mackenzie", "Calypso", "Rusty"],
 ["Bongo", "Biscuit", "Pippa", "Scout", "Bailey"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-9.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
