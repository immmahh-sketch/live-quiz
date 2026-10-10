# Bank session 10 Oct 2026: 4 more general races -> bank/race-23.json. 20 rows each, target 10; wrong options are
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

race("who created this detective?", "Books", "hard", ["detectives", "authors"], [
 ("Sherlock Holmes", "Arthur Conan Doyle", ["Edgar Allan Poe", "Wilkie Collins", "Ngaio Marsh"]), ("Hercule Poirot", "Agatha Christie", ["Margery Allingham", "Ngaio Marsh", "Ruth Rendell"]),
 ("Inspector Morse", "Colin Dexter", ["Reginald Hill", "Ruth Rendell", "Peter Robinson"]), ("Rebus", "Ian Rankin", ["Val McDermid", "Denise Mina", "Christopher Brookmyre"]),
 ("Maigret", "Georges Simenon", ["Émile Gaboriau", "Fred Vargas", "Gaston Leroux"]), ("Father Brown", "G. K. Chesterton", ["Edgar Allan Poe", "Wilkie Collins", "Hilaire Belloc"]),
 ("Lord Peter Wimsey", "Dorothy L. Sayers", ["Margery Allingham", "Ngaio Marsh", "Josephine Tey"]), ("Philip Marlowe", "Raymond Chandler", ["Mickey Spillane", "Ross Macdonald", "Rex Stout"]),
 ("Sam Spade", "Dashiell Hammett", ["Mickey Spillane", "Ross Macdonald", "Rex Stout"]), ("Jack Reacher", "Lee Child", ["James Patterson", "John Grisham", "David Baldacci"]),
 ("Harry Bosch", "Michael Connelly", ["James Patterson", "John Grisham", "David Baldacci"]), ("Kurt Wallander", "Henning Mankell", ["Jo Nesbø", "Stieg Larsson", "Camilla Läckberg"]),
 ("Adam Dalgliesh", "P. D. James", ["Ruth Rendell", "Peter James", "Reginald Hill"]), ("Inspector Lynley", "Elizabeth George", ["Ruth Rendell", "Peter James", "Martha Grimes"]),
 ("Vera Stanhope", "Ann Cleeves", ["Val McDermid", "Lynda La Plante", "Martina Cole"]), ("Cormoran Strike", "Robert Galbraith (J. K. Rowling)", ["Val McDermid", "Peter James", "Mark Billingham"]),
 ("Precious Ramotswe", "Alexander McCall Smith", ["Wilbur Smith", "Peter James", "Mark Billingham"]), ("Jackson Brodie", "Kate Atkinson", ["Val McDermid", "Denise Mina", "Lynda La Plante"]),
 ("Jack Frost", "R. D. Wingfield", ["Reginald Hill", "Peter Robinson", "Ruth Rendell"]), ("Brother Cadfael", "Ellis Peters", ["C. J. Sansom", "Umberto Eco", "Lindsey Davis"])])

race("name the villain of this Disney film", "Disney films", "medium", ["Disney", "villains"], [
 ("The Lion King", "Scar", ["Shere Khan", "Zira", "Sabor"]), ("Aladdin", "Jafar", ["Yzma", "Abis Mal", "Mozenrath"]),
 ("Snow White and the Seven Dwarfs", "The Evil Queen", ["The Queen of Hearts", "Madame Mim", "Cruella de Vil"]), ("The Little Mermaid", "Ursula", ["Morgana", "Madame Medusa", "Yzma"]),
 ("Sleeping Beauty", "Maleficent", ["Madame Mim", "The Queen of Hearts", "Cruella de Vil"]), ("Peter Pan", "Captain Hook", ["Mr. Smee", "Captain Gantu", "Long John Silver"]),
 ("Beauty and the Beast", "Gaston", ["LeFou", "Monsieur D'Arque", "Clayton"]), ("Tangled", "Mother Gothel", ["The Stabbington Brothers", "Madame Mim", "Cruella de Vil"]),
 ("Hercules", "Hades", ["Pain and Panic", "Chernabog", "Te Kā"]), ("Mulan", "Shan Yu", ["Chi-Fu", "Bori Khan", "Hayabusa"]),
 ("Pocahontas", "Governor Ratcliffe", ["Clayton", "Amos Slade", "McLeach"]), ("The Princess and the Frog", "Dr. Facilier", ["Mama Odie", "Lawrence", "Yzma"]),
 ("Up", "Charles Muntz", ["Waternoose", "Chick Hicks", "Stinky Pete"]), ("The Incredibles", "Syndrome", ["Mirage", "The Underminer", "Evelyn Deavor"]),
 ("Ratatouille", "Skinner", ["Anton Ego", "Colette", "Linguini"]), ("Zootopia", "Bellwether", ["Mr. Big", "Chief Bogo", "Duke Weaselton"]),
 ("Robin Hood", "Prince John", ["Sir Hiss", "The Sheriff of Nottingham", "King Richard"]), ("Cinderella", "Lady Tremaine", ["Drizella", "Anastasia", "Lucifer"]),
 ("Coco", "Ernesto de la Cruz", ["Héctor", "Chicharrón", "Abuelita"]), ("The Hunchback of Notre Dame", "Frollo", ["Clopin", "Phoebus", "Hugo"])])

race("what is this on a French menu?", "Food and drink", "easy", ["French", "food"], [
 ("Poulet", "Chicken", ["Turkey", "Goose", "Quail"]), ("Bœuf", "Beef", ["Veal", "Venison", "Ham"]), ("Agneau", "Lamb", ["Veal", "Goat", "Venison"]),
 ("Porc", "Pork", ["Veal", "Venison", "Turkey"]), ("Canard", "Duck", ["Goose", "Quail", "Turkey"]), ("Lapin", "Rabbit", ["Hare", "Venison", "Quail"]),
 ("Saumon", "Salmon", ["Trout", "Cod", "Tuna"]), ("Crevettes", "Prawns", ["Crab", "Lobster", "Oysters"]), ("Moules", "Mussels", ["Oysters", "Crab", "Squid"]),
 ("Escargots", "Snails", ["Frogs' legs", "Oysters", "Squid"]), ("Pommes de terre", "Potatoes", ["Apples", "Carrots", "Leeks"]), ("Champignons", "Mushrooms", ["Leeks", "Spinach", "Cabbage"]),
 ("Haricots verts", "Green beans", ["Spinach", "Leeks", "Cabbage"]), ("Petits pois", "Peas", ["Sprouts", "Spinach", "Carrots"]), ("Oignon", "Onion", ["Leeks", "Shallots", "Cabbage"]),
 ("Ail", "Garlic", ["Leeks", "Ginger", "Chives"]), ("Fromage", "Cheese", ["Butter", "Cream", "Yoghurt"]), ("Pain", "Bread", ["Rice", "Pasta", "Cake"]),
 ("Œuf", "Egg", ["Butter", "Cream", "Ham"]), ("Fraises", "Strawberries", ["Raspberries", "Cherries", "Blackcurrants"])])

race("who was captain of this ship?", "History and fiction", "medium", ["captains", "ships"], [
 ("The Pequod", "Ahab", ["Starbuck", "Ishmael", "Queequeg"]), ("The Nautilus", "Nemo", ["Professor Aronnax", "Ned Land", "Conseil"]),
 ("The Jolly Roger", "Hook", ["Mr. Smee", "Starkey", "Cecco"]), ("The original Starship Enterprise", "Kirk", ["Spock", "Sulu", "Scotty"]),
 ("The Black Pearl, in the first film", "Jack Sparrow", ["Joshamee Gibbs", "Will Turner", "Pintel"]), ("HMS Bounty", "William Bligh", ["Fletcher Christian", "John Fryer", "Peter Heywood"]),
 ("The Titanic", "Edward Smith", ["William Murdoch", "Charles Lightoller", "Bruce Ismay"]), ("The Orca in Jaws", "Quint", ["Brody", "Hooper", "Ben Gardner"]),
 ("The Millennium Falcon, in A New Hope", "Han Solo", ["Chewbacca", "Luke Skywalker", "Poe Dameron"]), ("The Flying Dutchman, in Pirates of the Caribbean", "Davy Jones", ["Bootstrap Bill", "Maccus", "Barbossa"]),
 ("HMS Endeavour", "James Cook", ["Joseph Banks", "Tobias Furneaux", "Charles Clerke"]), ("HMS Beagle, with Darwin aboard", "Robert FitzRoy", ["Charles Darwin", "Joseph Hooker", "Thomas Huxley"]),
 ("The Hispaniola in Treasure Island", "Captain Smollett", ["Long John Silver", "Billy Bones", "Squire Trelawney"]), ("Serenity", "Mal Reynolds", ["Zoe Washburne", "Jayne Cobb", "Wash"]),
 ("The Red October", "Marko Ramius", ["Jack Ryan", "Bart Mancuso", "Borodin"]), ("HMS Surprise", "Jack Aubrey", ["Stephen Maturin", "Horatio Hornblower", "Tom Pullings"]),
 ("The Nostromo in Alien", "Dallas", ["Ripley", "Kane", "Ash"]), ("The Starship Voyager", "Kathryn Janeway", ["Chakotay", "Seven of Nine", "Tuvok"]),
 ("The Mayflower", "Christopher Jones", ["William Bradford", "Myles Standish", "John Alden"]), ("The Enterprise-D", "Jean-Luc Picard", ["Riker", "Data", "Worf"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-23.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
