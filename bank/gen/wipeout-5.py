# Bank session 9 Oct 2026 (third pass): 9 new Wipeout boards -> bank/wipeout-5.json, several for the Christmas season.
# 15 right and 5 wrong each. Decoys need knowledge of the subject (memory: live-quiz-wipeout-decoys): mixed-up names,
# near-misses from the same world, or famous things that look right but aren't.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Genuine EastEnders characters (watch for mixed-up names)", "Film and TV", "medium", ["soaps", "EastEnders"],
 ["Dot Cotton", "Phil Mitchell", "Grant Mitchell", "Peggy Mitchell", "Ian Beale", "Pauline Fowler", "Den Watts", "Angie Watts", "Pat Butcher", "Frank Butcher", "Sharon Watts", "Kat Slater", "Alfie Moon", "Bianca Jackson", "Max Branning"],
 ["Dot Beale", "Phil Butcher", "Peggy Fowler", "Den Branning", "Pat Mitchell"])
board("Songs that were the UK Christmas number one", "Music", "medium", ["Christmas", "number ones"],
 ["Merry Xmas Everybody", "Lonely This Christmas", "Bohemian Rhapsody", "Mull of Kintyre", "Do They Know It's Christmas?", "Merry Christmas Everyone", "Always on My Mind", "Mistletoe and Wine", "Saviour's Day", "Mr Blobby", "Stay Another Day", "Earth Song", "2 Become 1", "Mad World", "Killing in the Name"],
 ["Last Christmas", "Fairytale of New York", "All I Want for Christmas Is You", "Wonderful Christmastime", "Step into Christmas"])
board("Things that go into a traditional Christmas pudding", "Food and drink", "medium", ["Christmas", "baking"],
 ["Suet", "Raisins", "Currants", "Sultanas", "Candied peel", "Breadcrumbs", "Flour", "Eggs", "Brown sugar", "Black treacle", "Brandy", "Nutmeg", "Cinnamon", "Mixed spice", "Stout"],
 ["Marzipan", "Royal icing", "Custard", "Cocoa powder", "Vanilla pods"])
board("Words that make a new word when you put 'sun' in front", "Words and language", "medium", ["wordplay"],
 ["Flower", "Shine", "Burn", "Set", "Rise", "Glasses", "Bed", "Dial", "Light", "Bathe", "Roof", "Block", "Spot", "Day", "Down"],
 ["Rain", "Storm", "Water", "Field", "Clock"])
board("Words that make a new word when you put 'foot' in front", "Words and language", "medium", ["wordplay"],
 ["Ball", "Path", "Print", "Step", "Note", "Wear", "Man", "Bridge", "Lights", "Hill", "Rest", "Stool", "Sore", "Fall", "Hold"],
 ["Sock", "Walk", "Room", "Table", "Line"])
board("Dances you'd see on Strictly Come Dancing", "Film and TV", "medium", ["Strictly", "dance"],
 ["Waltz", "Viennese Waltz", "Foxtrot", "Quickstep", "Tango", "Argentine Tango", "Cha-cha-cha", "Rumba", "Samba", "Jive", "Paso Doble", "Salsa", "Charleston", "American Smooth", "Couple's Choice"],
 ["Polka", "Flamenco", "Bolero", "Mambo", "Hornpipe"])
board("Shakespeare villains", "Books and literature", "hard", ["Shakespeare"],
 ["Iago", "Richard III", "Lady Macbeth", "Edmund", "Goneril", "Regan", "Claudius", "Shylock", "Aaron", "Don John", "Angelo", "Iachimo", "Tamora", "Antonio (The Tempest)", "The Duke of Cornwall"],
 ["Horatio", "Banquo", "Cordelia", "Desdemona", "Benvolio"])
board("Pantomimes you might see at a British theatre at Christmas", "Christmas", "easy", ["Christmas", "panto"],
 ["Cinderella", "Aladdin", "Jack and the Beanstalk", "Dick Whittington", "Puss in Boots", "Peter Pan", "Snow White", "Sleeping Beauty", "Beauty and the Beast", "Mother Goose", "Goldilocks and the Three Bears", "Robin Hood", "Babes in the Wood", "Sinbad", "Little Red Riding Hood"],
 ["The Nutcracker", "Swan Lake", "Oliver!", "Annie", "Bugsy Malone"])
board("Signals a cricket umpire makes", "Sport", "hard", ["cricket"],
 ["Out", "Four", "Six", "Wide", "No-ball", "Bye", "Leg bye", "Dead ball", "Short run", "Free hit", "Penalty runs", "Revoke last signal", "New ball", "Last hour", "One short"],
 ["Maiden", "Duck", "Hat-trick", "Declaration", "Follow-on"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
