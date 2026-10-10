# Bank session 10 Oct 2026: 20 more Put in order questions -> bank/order-5.json (albums, books, the North East, sport and TV). A criminal-case
# question was dropped: order-3 already had it.
# the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Football", ["English football", "leagues"], "easy", "Put these leagues in order of the English football pyramid, top tier first", ["Premier League", "Championship", "League One", "League Two", "National League", "National League North", "Northern Premier League"], "top tier first")
o("History", ["royal houses", "monarchy"], "medium", "Put these royal houses in the order they first took the English or British throne, earliest first", ["Normandy", "Plantagenet", "Tudor", "Stuart", "Hanover", "Saxe-Coburg and Gotha", "Windsor"], "earliest first")
o("Food and drink", ["Starbucks", "coffee"], "easy", "Put these Starbucks cup sizes in order, smallest first", ["Short", "Tall", "Grande", "Venti"], "smallest first")
o("Animals", ["horses", "riding"], "easy", "Put these paces of a horse in order, slowest first", ["Walk", "Trot", "Canter", "Gallop"], "slowest first")
o("Sport", ["swimming", "Olympics"], "medium", "Put these strokes in the order they're swum in an individual medley race", ["Butterfly", "Backstroke", "Breaststroke", "Freestyle"], "first leg first")
o("TV", ["The X Factor", "talent shows"], "easy", "Put these stages of 'The X Factor' in the order a contestant goes through them", ["Auditions", "Bootcamp", "Judges' houses", "Live shows", "The final"], "first to last")
o("Music", ["Little Mix", "albums"], "medium", "Put these Little Mix albums in order of release, earliest first", ["DNA", "Salute", "Get Weird", "Glory Days", "LM5", "Confetti"], "earliest first")
o("Books", ["The Hunger Games", "Suzanne Collins"], "medium", "Put these Hunger Games books in order of publication, earliest first", ["The Hunger Games", "Catching Fire", "Mockingjay", "The Ballad of Songbirds and Snakes", "Sunrise on the Reaping"], "earliest first")
o("Music", ["Adele", "albums"], "easy", "Put Adele's albums in order of release, earliest first", ["19", "21", "25", "30"], "earliest first")
o("Music", ["Ed Sheeran", "albums"], "medium", "Put these Ed Sheeran albums in order of release, earliest first", ["+ (Plus)", "× (Multiply)", "÷ (Divide)", "= (Equals)", "− (Subtract)", "Play"], "earliest first")
o("Music", ["Taylor Swift", "albums"], "medium", "Put these Taylor Swift albums in order of release, earliest first", ["Fearless", "Speak Now", "Red", "1989", "Reputation", "Folklore", "Midnights"], "earliest first")
o("Music", ["Coldplay", "albums"], "hard", "Put these Coldplay albums in order of release, earliest first", ["Parachutes", "A Rush of Blood to the Head", "X&Y", "Viva la Vida", "Mylo Xyloto", "Ghost Stories", "A Head Full of Dreams"], "earliest first")
o("Music", ["Arctic Monkeys", "albums"], "hard", "Put these Arctic Monkeys albums in order of release, earliest first", ["Whatever People Say I Am, That's What I'm Not", "Favourite Worst Nightmare", "Humbug", "Suck It and See", "AM", "Tranquility Base Hotel & Casino", "The Car"], "earliest first")
o("Music", ["ABBA", "number ones"], "medium", "Put these ABBA number ones in order, earliest first", ["Waterloo", "Mamma Mia", "Dancing Queen", "Knowing Me, Knowing You", "Take a Chance on Me", "The Winner Takes It All", "Super Trouper"], "earliest first")
o("North East England", ["Hadrian's Wall", "Romans"], "hard", "Put these places along Hadrian's Wall in order, going from east to west", ["Wallsend", "Newcastle", "Heddon-on-the-Wall", "Chesters", "Housesteads", "Birdoswald", "Bowness-on-Solway"], "east to west")
o("North East England", ["coast", "seaside"], "medium", "Put these places on the North East coast in order, going from north to south", ["Berwick-upon-Tweed", "Bamburgh", "Amble", "Whitley Bay", "South Shields", "Seaham", "Hartlepool"], "north to south")
o("North East England", ["River Wear", "rivers"], "hard", "Put these places on the River Wear in order, from its source to the sea", ["Wearhead", "Stanhope", "Wolsingham", "Bishop Auckland", "Durham", "Chester-le-Street", "Sunderland"], "source to sea")
o("North East England", ["River Tees", "rivers"], "hard", "Put these places on the River Tees in order, from its source to the sea", ["Middleton-in-Teesdale", "Barnard Castle", "Yarm", "Stockton-on-Tees", "Middlesbrough"], "source to sea")
o("Books", ["Charles Dickens", "novels"], "hard", "Put these Charles Dickens books in order of publication, earliest first", ["The Pickwick Papers", "Oliver Twist", "A Christmas Carol", "David Copperfield", "Bleak House", "A Tale of Two Cities", "Great Expectations"], "earliest first")
o("Books", ["Jane Austen", "novels"], "hard", "Put these Jane Austen novels in order of publication, earliest first", ["Sense and Sensibility", "Pride and Prejudice", "Mansfield Park", "Emma", "Persuasion"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
