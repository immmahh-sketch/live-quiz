# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-48.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Pizzas on an Italian pizzeria's menu (not other Italian dishes)", "Food and drink", "medium", ["pizza", "Italian food"],
 ["Margherita", "Marinara", "Quattro formaggi", "Quattro stagioni", "Capricciosa", "Diavola", "Napoletana", "Calzone", "Fiorentina", "Funghi", "Romana", "Bianca", "Prosciutto e funghi", "Vegetariana", "Siciliana"],
 ["Bruschetta", "Focaccia", "Arancini", "Panzanella", "Gnocchi"])
board("Crisps and corn snacks (not crackers)", "Food and drink", "easy", ["crisps", "snacks", "brands"],
 ["Walkers", "Golden Wonder", "McCoy's", "Pringles", "Kettle", "Tyrrells", "Monster Munch", "Wotsits", "Quavers", "Hula Hoops", "Skips", "Frazzles", "Space Raiders", "Doritos", "Seabrook"],
 ["Mini Cheddars", "Ritz", "TUC", "Jacob's Cream Crackers", "Ryvita"])
board("Marvel characters (watch out for DC)", "Film", "easy", ["Marvel", "superheroes"],
 ["Spider-Man", "Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye", "Black Panther", "Doctor Strange", "Ant-Man", "Wolverine", "Deadpool", "Groot", "Scarlet Witch", "Daredevil"],
 ["Aquaman", "The Flash", "Green Lantern", "Cyborg", "Shazam"])
board("Characters who appear in 'The Lord of the Rings' (not just 'The Hobbit')", "Books", "medium", ["Tolkien", "Lord of the Rings", "fantasy"],
 ["Frodo", "Sam", "Gandalf", "Aragorn", "Legolas", "Gimli", "Boromir", "Merry", "Pippin", "Gollum", "Saruman", "Sauron", "Galadriel", "Elrond", "Arwen"],
 ["Smaug", "Thorin Oakenshield", "Bard the Bowman", "Beorn", "Azog"])
board("'Family Guy' characters (not 'American Dad')", "TV", "medium", ["Family Guy", "cartoons", "American TV"],
 ["Peter Griffin", "Lois Griffin", "Meg Griffin", "Chris Griffin", "Stewie", "Brian", "Quagmire", "Cleveland", "Joe Swanson", "Bonnie Swanson", "Mort Goldman", "Tom Tucker", "Herbert", "Consuela", "Carter Pewterschmidt"],
 ["Stan Smith", "Francine Smith", "Roger", "Klaus", "Steve Smith"])
board("Places in Cornwall (not Devon)", "UK geography", "medium", ["Cornwall", "seaside", "England"],
 ["Penzance", "St Ives", "Truro", "Newquay", "Falmouth", "Padstow", "Bodmin", "Looe", "Fowey", "Bude", "Mevagissey", "Launceston", "Redruth", "Camborne", "Tintagel"],
 ["Plymouth", "Salcombe", "Torquay", "Ilfracombe", "Dartmouth"])
board("Sports at the Summer Paralympics (not the Winter Games)", "Sport", "medium", ["Paralympics", "disability sport"],
 ["Wheelchair basketball", "Boccia", "Goalball", "Sitting volleyball", "Wheelchair rugby", "Para swimming", "Para cycling", "Wheelchair tennis", "Wheelchair fencing", "Blind football", "Para archery", "Powerlifting", "Para athletics", "Para rowing", "Para canoe"],
 ["Wheelchair curling", "Para ice hockey", "Para alpine skiing", "Para biathlon", "Para snowboard"])
board("Engines on the Island of Sodor (not coaches, buses or helicopters)", "TV", "medium", ["Thomas the Tank Engine", "children's TV"],
 ["Thomas", "Edward", "Henry", "Gordon", "James", "Percy", "Toby", "Duck", "Donald", "Douglas", "Oliver", "Emily", "Diesel", "Bill", "Ben"],
 ["Annie", "Clarabel", "Bertie", "Harold", "Terence"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-48.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
