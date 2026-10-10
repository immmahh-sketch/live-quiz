# Bank session 10 Oct 2026: 20 more Put in order questions -> bank/order-6.json (albums, songs, novels, directors).
# Checked against every order question in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Music", ["Beyoncé", "albums"], "hard", "Put these Beyoncé solo albums in order of release, earliest first", ["Dangerously in Love", "B'Day", "I Am... Sasha Fierce", "4", "Beyoncé", "Lemonade", "Renaissance"], "earliest first")
o("Music", ["Kylie Minogue", "number ones"], "medium", "Put these Kylie Minogue number ones in order, earliest first", ["I Should Be So Lucky", "Especially for You", "Hand on Your Heart", "Tears on My Pillow", "Spinning Around", "Can't Get You Out of My Head", "Slow"], "earliest first")
o("Music", ["Robbie Williams", "albums"], "hard", "Put these Robbie Williams albums in order of release, earliest first", ["Life thru a Lens", "I've Been Expecting You", "Sing When You're Winning", "Swing When You're Winning", "Escapology", "Intensive Care", "Rudebox"], "earliest first")
o("Music", ["Madonna", "albums"], "medium", "Put these Madonna albums in order of release, earliest first", ["Like a Virgin", "True Blue", "Like a Prayer", "Erotica", "Ray of Light", "Music", "Confessions on a Dance Floor"], "earliest first")
o("Music", ["Pink Floyd", "albums"], "hard", "Put these Pink Floyd albums in order of release, earliest first", ["The Piper at the Gates of Dawn", "Meddle", "The Dark Side of the Moon", "Wish You Were Here", "Animals", "The Wall", "The Division Bell"], "earliest first")
o("Music", ["David Bowie", "albums"], "hard", "Put these David Bowie albums in order of release, earliest first", ["Hunky Dory", "The Rise and Fall of Ziggy Stardust and the Spiders from Mars", "Aladdin Sane", "Diamond Dogs", "Low", "Let's Dance", "Blackstar"], "earliest first")
o("Music", ["U2", "albums"], "medium", "Put these U2 albums in order of release, earliest first", ["Boy", "War", "The Joshua Tree", "Achtung Baby", "Pop", "All That You Can't Leave Behind", "How to Dismantle an Atomic Bomb"], "earliest first")
o("Music", ["Blur", "albums", "Britpop"], "hard", "Put these Blur albums in order of release, earliest first", ["Leisure", "Modern Life Is Rubbish", "Parklife", "The Great Escape", "Blur", "13", "Think Tank"], "earliest first")
o("Music", ["Oasis", "albums", "Britpop"], "medium", "Put these Oasis albums in order of release, earliest first", ["Definitely Maybe", "(What's the Story) Morning Glory?", "Be Here Now", "Standing on the Shoulder of Giants", "Heathen Chemistry", "Don't Believe the Truth", "Dig Out Your Soul"], "earliest first")
o("Music", ["ABBA", "albums"], "hard", "Put these ABBA albums in order of release, earliest first", ["Ring Ring", "Waterloo", "ABBA", "Arrival", "The Album", "Voulez-Vous", "Super Trouper"], "earliest first")
o("Music", ["Elton John", "songs"], "medium", "Put these Elton John songs in order of release, earliest first", ["Your Song", "Rocket Man", "Candle in the Wind", "Don't Go Breaking My Heart", "I'm Still Standing", "Sacrifice", "Cold Heart"], "earliest first")
o("Music", ["Whitney Houston", "songs"], "medium", "Put these Whitney Houston hits in order of release, earliest first", ["Saving All My Love for You", "I Wanna Dance with Somebody", "One Moment in Time", "I Will Always Love You", "It's Not Right but It's Okay"], "earliest first")
o("Books", ["Stephen King", "novels"], "medium", "Put these Stephen King novels in order of publication, earliest first", ["Carrie", "'Salem's Lot", "The Shining", "It", "Misery", "The Green Mile"], "earliest first")
o("Books", ["Agatha Christie", "novels"], "hard", "Put these Agatha Christie novels in order of publication, earliest first", ["The Mysterious Affair at Styles", "The Murder of Roger Ackroyd", "Murder on the Orient Express", "Death on the Nile", "And Then There Were None", "The Mirror Crack'd from Side to Side"], "earliest first")
o("Books", ["Thomas Hardy", "novels"], "hard", "Put these Thomas Hardy novels in order of publication, earliest first", ["Far from the Madding Crowd", "The Return of the Native", "The Mayor of Casterbridge", "Tess of the d'Urbervilles", "Jude the Obscure"], "earliest first")
o("Books", ["George Orwell"], "hard", "Put these George Orwell books in order of publication, earliest first", ["Down and Out in Paris and London", "Burmese Days", "Homage to Catalonia", "Animal Farm", "Nineteen Eighty-Four"], "earliest first")
o("Film", ["Steven Spielberg", "directors"], "medium", "Put these Steven Spielberg films in order of release, earliest first", ["Jaws", "Close Encounters of the Third Kind", "Raiders of the Lost Ark", "E.T. the Extra-Terrestrial", "Jurassic Park", "Saving Private Ryan", "Lincoln"], "earliest first")
o("Film", ["Christopher Nolan", "directors"], "medium", "Put these Christopher Nolan films in order of release, earliest first", ["Memento", "Batman Begins", "The Dark Knight", "Inception", "Interstellar", "Dunkirk", "Oppenheimer"], "earliest first")
o("Film", ["Quentin Tarantino", "directors"], "medium", "Put these Quentin Tarantino films in order of release, earliest first", ["Reservoir Dogs", "Pulp Fiction", "Jackie Brown", "Kill Bill: Volume 1", "Inglourious Basterds", "Django Unchained", "Once Upon a Time in Hollywood"], "earliest first")
o("Film", ["Alfred Hitchcock", "directors"], "hard", "Put these Hitchcock films from his Hollywood years in order, earliest first", ["Rebecca", "Rear Window", "Vertigo", "North by Northwest", "Psycho", "The Birds"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
