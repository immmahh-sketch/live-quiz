# Bank session 10 Oct 2026: 20 more Only One prompts (story characters, countries, sport, languages) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a city in Asia that has hosted a Summer or Winter Olympics, up to 2026", ["Tokyo", "Seoul", "Beijing", "Sapporo", "Nagano", "Pyeongchang/PyeongChang"]),
 ("Name a country whose English name ends in 'land' (England, Scotland and Northern Ireland count)", ["England", "Scotland", "Northern Ireland", "Finland", "Iceland", "Ireland", "New Zealand", "Poland", "Switzerland", "Thailand"]),
 ("Name a character in Shakespeare's Hamlet", ["Hamlet", "Claudius", "Gertrude", "Ophelia", "Polonius", "Laertes", "Horatio", "Rosencrantz", "Guildenstern", "Fortinbras", "Yorick", "Osric", "Marcellus", "Bernardo", "The Ghost/Ghost/Old Hamlet"]),
 ("Name a character in Shakespeare's Macbeth", ["Macbeth", "Lady Macbeth", "Banquo", "Fleance", "Duncan", "Malcolm", "Donalbain", "Macduff", "Lady Macduff", "Ross", "Lennox", "Hecate", "The witches/Witches/Weird Sisters", "The Porter/Porter", "Seyton"]),
 ("Name a character in Shakespeare's Romeo and Juliet", ["Romeo", "Juliet", "Mercutio", "Tybalt", "Benvolio", "Friar Laurence/Friar Lawrence", "The Nurse/Nurse", "Paris", "Lord Capulet/Capulet", "Lady Capulet", "Lord Montague/Montague", "Lady Montague", "Prince Escalus/Escalus", "Balthasar", "Friar John", "Peter", "Sampson", "Gregory", "Rosaline"]),
 ("Name a character in Dickens's A Christmas Carol", ["Ebenezer Scrooge/Scrooge", "Bob Cratchit", "Tiny Tim", "Jacob Marley/Marley", "Fred", "Mr Fezziwig/Fezziwig", "Mrs Fezziwig", "Belle", "Mrs Cratchit", "Fan", "The Ghost of Christmas Past", "The Ghost of Christmas Present", "The Ghost of Christmas Yet to Come"]),
 ("Name a character in Dickens's Oliver Twist", ["Oliver Twist/Oliver", "Fagin", "The Artful Dodger/Artful Dodger/Dodger/Jack Dawkins", "Nancy", "Bill Sikes", "Mr Bumble/Bumble", "Mr Brownlow/Brownlow", "Noah Claypole", "Charley Bates", "Bull's-eye/Bullseye", "Mrs Corney/Widow Corney", "Mr Sowerberry", "Monks", "Rose Maylie"]),
 ("Name a character in Dickens's Great Expectations", ["Pip", "Estella", "Miss Havisham", "Joe Gargery", "Abel Magwitch/Magwitch", "Herbert Pocket", "Mr Jaggers/Jaggers", "Mrs Joe", "Biddy", "Wemmick", "Pumblechook", "Orlick", "Bentley Drummle", "Compeyson"]),
 ("Name a character in Jane Austen's Pride and Prejudice", ["Elizabeth Bennet/Lizzy/Elizabeth", "Mr Darcy/Darcy", "Jane Bennet/Jane", "Mr Bingley/Bingley", "Mr Bennet", "Mrs Bennet", "Lydia", "Kitty", "Mary", "Mr Wickham/Wickham", "Mr Collins/Collins", "Lady Catherine de Bourgh/Lady Catherine", "Charlotte Lucas", "Caroline Bingley", "Georgiana Darcy", "Colonel Fitzwilliam", "Mr Gardiner", "Mrs Gardiner", "Anne de Bourgh"]),
 ("Name a character in Alice's Adventures in Wonderland or Through the Looking-Glass", ["Alice", "The White Rabbit/White Rabbit", "The Mad Hatter/Hatter", "The March Hare/March Hare", "The Dormouse/Dormouse", "The Cheshire Cat/Cheshire Cat", "The Queen of Hearts/Queen of Hearts", "The King of Hearts", "The Knave of Hearts", "The Caterpillar", "The Duchess", "The Mock Turtle", "The Gryphon", "Tweedledum", "Tweedledee", "Humpty Dumpty", "The Red Queen", "The White Queen", "The White Knight", "The Jabberwock", "Bill the Lizard"]),
 ("Name a character in the Paddington books or films", ["Paddington", "Mr Brown/Henry Brown", "Mrs Brown/Mary Brown", "Judy", "Jonathan", "Mrs Bird", "Mr Gruber", "Aunt Lucy", "Uncle Pastuzo", "Mr Curry", "Millicent Clyde", "Phoenix Buchanan"]),
 ("Name a home stadium of a men's Six Nations rugby team", ["Twickenham/Allianz Stadium", "Murrayfield/Scottish Gas Murrayfield", "Principality Stadium/Millennium Stadium", "Aviva Stadium/Lansdowne Road", "Stade de France", "Stadio Olimpico"]),
 ("Name a European country or Crown Dependency where they drive on the left", ["United Kingdom/UK/Britain", "Ireland", "Malta", "Cyprus", "Isle of Man", "Jersey", "Guernsey"]),
 ("Name a UK Christmas number one single from 2010 to 2019", ["When We Collide", "Wherever You Are", "He Ain't Heavy, He's My Brother", "Skyscraper", "Something I Need", "A Bridge over You", "Rockabye", "Perfect", "We Built This City", "I Don't Care/I Love Sausage Rolls"]),
 ("Name one of the five basic tastes your tongue can detect", ["Sweet", "Sour", "Salty", "Bitter", "Umami/Savoury"]),
 ("Name one of men's tennis's 'Big Four', or one of the Williams sisters", ["Roger Federer/Federer", "Rafael Nadal/Nadal", "Novak Djokovic/Djokovic", "Andy Murray/Murray", "Venus Williams/Venus", "Serena Williams/Serena"]),
 ("Name a month of the year in Spanish", ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre/Setiembre", "Octubre", "Noviembre", "Diciembre"]),
 ("Name a number from one to ten in Italian", ["Uno", "Due", "Tre", "Quattro", "Cinque", "Sei", "Sette", "Otto", "Nove", "Dieci"]),
 ("Name one of the three starter Pokémon from the first games, or Pikachu", ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"]),
 ("Name a planet or moon visited in the nine main Star Wars 'Skywalker saga' films", ["Tatooine", "Alderaan", "Yavin 4/Yavin", "Hoth", "Dagobah", "Bespin", "Endor", "Naboo", "Coruscant", "Kamino", "Geonosis", "Mustafar", "Kashyyyk", "Utapau", "Felucia", "Mygeeto", "Jakku", "Takodana", "Starkiller Base", "D'Qar", "Ahch-To", "Cantonica/Canto Bight", "Crait", "Pasaana", "Kijimi", "Kef Bir", "Exegol", "Ajan Kloss", "Polis Massa", "Saleucami", "Cato Neimoidia"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
