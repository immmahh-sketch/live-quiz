# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-49.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Characters in the Sherlock Holmes stories (not Poirot)", "Books", "medium", ["Sherlock Holmes", "detectives", "Arthur Conan Doyle"],
 ["Sherlock Holmes", "Dr Watson", "Mrs Hudson", "Moriarty", "Mycroft", "Inspector Lestrade", "Irene Adler", "Inspector Gregson", "Toby", "Wiggins", "Colonel Moran", "Mary Morstan", "Billy the page", "Sir Henry Baskerville", "Charles Augustus Milverton"],
 ["Captain Hastings", "Inspector Japp", "Miss Lemon", "Ariadne Oliver", "George the valet"])
board("South Park characters (not Futurama)", "TV", "medium", ["South Park", "cartoons", "American TV"],
 ["Stan", "Kyle", "Cartman", "Kenny", "Butters", "Mr Garrison", "Chef", "Randy Marsh", "Wendy", "Token", "Timmy", "Jimmy", "Mr Mackey", "Mr Hankey", "Towelie"],
 ["Fry", "Leela", "Bender", "Zoidberg", "Professor Farnsworth"])
board("Sweets with no chocolate in them", "Food and drink", "medium", ["sweets", "confectionery"],
 ["Fruit Pastilles", "Wine Gums", "Jelly Babies", "Liquorice Allsorts", "Rhubarb and Custard", "Sherbet Lemons", "Fruit Salads", "Black Jacks", "Flying Saucers", "Drumstick lollies", "Refreshers", "Love Hearts", "Parma Violets", "Midget Gems", "Starburst"],
 ["Smarties", "Revels", "Rolo", "Munchies", "Minstrels"])
board("Crustaceans (watch out for molluscs and impostors)", "Animals", "hard", ["crustaceans", "sea life", "animals"],
 ["Crab", "Lobster", "Shrimp", "Prawn", "Crayfish", "Langoustine", "Barnacle", "Krill", "Woodlouse", "Hermit crab", "Spider crab", "Water flea", "Copepod", "Mantis shrimp", "Sand hopper"],
 ["Octopus", "Squid", "Mussel", "Scallop", "Horseshoe crab"])
board("Characters in Postman Pat (not Fireman Sam)", "TV", "medium", ["Postman Pat", "children's TV"],
 ["Postman Pat", "Jess", "Mrs Goggins", "Ted Glen", "Reverend Timms", "PC Selby", "Alf Thompson", "Dorothy Thompson", "Bill Thompson", "Miss Hubbard", "Dr Gilbertson", "Major Forbes", "Peter Fogg", "Sara", "Julian"],
 ["Norman Price", "Dilys Price", "Station Officer Steele", "Elvis Cridlington", "Trevor Evans"])
board("Towns and cities in Northern Ireland (not the Republic)", "UK geography", "medium", ["Northern Ireland", "towns"],
 ["Belfast", "Derry", "Lisburn", "Newry", "Armagh", "Enniskillen", "Coleraine", "Omagh", "Bangor", "Ballymena", "Portrush", "Larne", "Newtownards", "Strabane", "Downpatrick"],
 ["Dundalk", "Donegal", "Sligo", "Letterkenny", "Monaghan"])
board("Words that make a new word when you put 'post' in front", "Words and language", "medium", ["wordplay", "compound words"],
 ["Card", "Man", "Code", "Box", "Mark", "Mortem", "Script", "Graduate", "Age", "Master", "Pone", "Natal", "War", "Office", "Woman"],
 ["Stamp", "Letter", "Parcel", "Route", "Tray"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-49.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
