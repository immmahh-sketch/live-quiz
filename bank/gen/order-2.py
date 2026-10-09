# Bank session 9 Oct 2026: 3 more Put in Order questions for each topic with 3 or fewer unused in the live bank.
# Items are listed in the right order. Writes bank/topics/<slug>__o2.json; import each with
#   FILE=<slug>__o2 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def o(slug, diff, text, *items, hint=None):
    assert 4 <= len(items) <= 5 and len(set(items)) == len(items), text
    q = {"type": "order", "text": text, "items": list(items), "difficulty": diff}
    if hint: q["hint"] = hint
    OUT.setdefault(slug, []).append(q)

o("anagrams-wordplay", "medium", "Put this word ladder in order, from COLD to WARM", "COLD", "CORD", "CARD", "WARD", "WARM", hint="One letter changes at each step")
o("anagrams-wordplay", "medium", "Put these Q words in alphabetical order", "Quay", "Queue", "Quick", "Quiz")
o("anagrams-wordplay", "easy", "Put these palindromes in order of length, shortest first", "Eye", "Level", "Racecar", "Rotavator")

o("connections", "medium", "Put these Doctors in the order they took over the TARDIS", "Tom Baker", "Peter Davison", "David Tennant", "Matt Smith", "Jodie Whittaker")
o("connections", "easy", "Put these colours in rainbow order, starting nearest red", "Yellow", "Green", "Blue", "Indigo", "Violet")
o("connections", "medium", "Put these Monopoly squares in order round the board, starting from GO", "Old Kent Road", "The Angel Islington", "Pall Mall", "Trafalgar Square", "Mayfair")

o("europe", "medium", "Put these western European countries in order of area, largest first", "France", "Spain", "Germany", "Italy", "United Kingdom")
o("europe", "medium", "Put these European capitals in order from west to east", "Lisbon", "Madrid", "Paris", "Berlin", "Warsaw")
o("europe", "hard", "Put these European rivers in order of length, longest first", "Volga", "Danube", "Rhine", "Loire", "Thames")

o("world-geography", "easy", "Put these mountains in order of height, highest first", "Everest", "K2", "Kilimanjaro", "Mont Blanc", "Ben Nevis")
o("world-geography", "medium", "Put the five oceans in order of size, largest first", "Pacific", "Atlantic", "Indian", "Southern", "Arctic")
o("world-geography", "medium", "Put the world's most populous countries in order, largest first", "India", "China", "USA", "Indonesia", "Pakistan")

o("bonfire-night", "easy", "Put these dates in order, earliest first", "The autumn equinox", "The clocks go back", "Bonfire Night", "St Andrew's Day", "The winter solstice")
o("bonfire-night", "medium", "Put these Tudor and Stuart monarchs in order, earliest first", "Henry VIII", "Elizabeth I", "James I", "Charles I", hint="James I was the king the plotters tried to blow up")
o("bonfire-night", "medium", "Put these star signs in calendar order, earliest first", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn")

o("days-that-shook-the-world", "medium", "Put these wars in order of when they began, earliest first", "The Crimean War", "The American Civil War", "The Boer War", "The First World War", "The Korean War")
o("days-that-shook-the-world", "medium", "Put these disasters in order, earliest first", "The Titanic sinks", "The Hindenburg burns", "Aberfan", "Piper Alpha")
o("days-that-shook-the-world", "medium", "Put these revolutions in order, earliest first", "The American Revolution", "The French Revolution", "The Russian Revolution", "The Cuban Revolution", "The Iranian Revolution")

o("disney", "medium", "Put these Disney villains in order of their film's release, earliest first", "Maleficent", "Cruella de Vil", "Ursula", "Scar", "Mother Gothel")
o("disney", "hard", "Put these Disney theme parks in order of opening, earliest first", "Disneyland, California", "Walt Disney World, Florida", "Tokyo Disneyland", "Disneyland Paris", "Shanghai Disneyland")
o("disney", "hard", "Put these live-action Disney films in order of release, earliest first", "Alice in Wonderland", "Maleficent", "Cinderella", "Beauty and the Beast", "The Little Mermaid")

o("famous-people", "easy", "Put these queens in order of their reigns, earliest first", "Elizabeth I", "Queen Anne", "Queen Victoria", "Elizabeth II")
o("famous-people", "medium", "Put these artists in order of birth, earliest first", "Leonardo da Vinci", "Rembrandt", "Vincent van Gogh", "Pablo Picasso", "Andy Warhol")
o("famous-people", "medium", "Put these great composers in order of birth, earliest first", "Bach", "Mozart", "Beethoven", "Tchaikovsky")

o("no-such-thing-as-a-fish", "medium", "Put these animals in order of how long they usually live, shortest first", "Adult mayfly", "Mouse", "Dog", "Elephant", "Greenland shark")
o("no-such-thing-as-a-fish", "hard", "Put these in order of how many bones they have, fewest first", "Shark", "Adult human", "Newborn baby", "Python")
o("no-such-thing-as-a-fish", "easy", "Put these in order of top speed, slowest first", "Garden snail", "Usain Bolt", "Cheetah", "Diving peregrine falcon")

o("20th-century", "easy", "Put these 20th-century Prime Ministers in order, earliest first", "David Lloyd George", "Neville Chamberlain", "Anthony Eden", "Edward Heath", "John Major")
o("20th-century", "medium", "Put these moments in order, earliest first", "The first powered flight", "The Titanic sinks", "Women get the vote on equal terms with men", "The NHS is founded", "England win the World Cup")
o("20th-century", "medium", "Put these British moments in order, earliest first", "Decimal currency arrives", "Britain joins the Common Market", "The miners' strike begins", "The Channel Tunnel opens")

o("the-beatles", "medium", "Put these five Beatles albums in order of release, earliest first", "Please Please Me", "Rubber Soul", "Sgt. Pepper's Lonely Hearts Club Band", "The White Album", "Abbey Road")
o("the-beatles", "hard", "Put these solo hits in order of release, earliest first", "My Sweet Lord", "Imagine", "Live and Let Die", "Mull of Kintyre")
o("the-beatles", "medium", "Put these Beatles number ones in order, earliest first", "From Me to You", "Can't Buy Me Love", "We Can Work It Out", "Paperback Writer", "Get Back")

o("usa", "hard", "Put these states in the order they joined the Union, earliest first", "Delaware", "Texas", "California", "Alaska", "Hawaii")
o("usa", "easy", "Put these American cities in order from west to east", "San Francisco", "Las Vegas", "Denver", "Chicago", "New York")
o("usa", "easy", "Put these modern presidents in order, earliest first", "Richard Nixon", "Ronald Reagan", "Bill Clinton", "George W. Bush", "Donald Trump")

o("uk-geography", "easy", "Put the highest peaks of the four home nations in order of height, highest first", "Ben Nevis", "Snowdon", "Scafell Pike", "Slieve Donard")
o("uk-geography", "medium", "Put these rivers in order of length, longest first, from the Severn down to the Tyne", "Severn", "Thames", "Trent", "Tyne")
o("uk-geography", "easy", "Put these North East towns in order from north to south", "Berwick-upon-Tweed", "Alnwick", "Newcastle upon Tyne", "Durham", "Darlington")

o("number-ones", "medium", "Put these Christmas chart-toppers in order, earliest first", "Mull of Kintyre", "Do They Know It's Christmas?", "Mr Blobby", "Killing in the Name", "We Built This City (LadBaby)")
o("number-ones", "medium", "Put these 2010s number ones in order, earliest first", "Someone Like You", "Gangnam Style", "Happy", "Shape of You", "Old Town Road")
o("number-ones", "easy", "Put these number ones from five decades in order, earliest first", "Bohemian Rhapsody", "Relax", "Vogue", "Wannabe", "Crazy (Gnarls Barkley)")

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__o2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'orders in', len(OUT), 'topics:', ' '.join(OUT))
