# Bank session 10 Oct 2026: 2 more general races -> bank/race-106.json (album covers, nursery rhymes). 20 rows each, target 10; wrong options are
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

race("which album has this cover?", "Music", "medium", ["albums", "album covers"], [
 ("Four men walking over a zebra crossing", "Abbey Road", ["Let It Be", "Revolver", "Help!"]),
 ("A baby swimming after a dollar bill", "Nevermind", ["In Utero", "Bleach", "Ten"]),
 ("A beam of light split by a prism", "The Dark Side of the Moon", ["Wish You Were Here", "Meddle", "The Wall"]),
 ("A pig floating over Battersea Power Station", "Animals", ["The Wall", "Meddle", "Wish You Were Here"]),
 ("A crowd of cut-out famous faces round a drum", "Sgt. Pepper's Lonely Hearts Club Band", ["Magical Mystery Tour", "Rubber Soul", "Revolver"]),
 ("A man smashing his bass guitar on stage", "London Calling", ["Give 'Em Enough Rope", "Combat Rock", "Sandinista!"]),
 ("A man's back and jeans in front of the Stars and Stripes", "Born in the U.S.A.", ["Born to Run", "The River", "Nebraska"]),
 ("Mick Fleetwood and Stevie Nicks, with wooden balls hanging from his belt", "Rumours", ["Tusk", "Tango in the Night", "Mirage"]),
 ("Racing greyhounds at a dog track", "Parklife", ["The Great Escape", "Modern Life Is Rubbish", "Leisure"]),
 ("Two men passing on a busy Soho street", "(What's the Story) Morning Glory?", ["Be Here Now", "Heathen Chemistry", "Dig Out Your Soul"]),
 ("The band lounging in a living room with a globe and a Burt Bacharach photo", "Definitely Maybe", ["Be Here Now", "Heathen Chemistry", "Dig Out Your Soul"]),
 ("A man in a white suit lying beside a tiger cub", "Thriller", ["Bad", "Off the Wall", "Dangerous"]),
 ("A singer on a purple motorbike", "Purple Rain", ["1999", "Sign o' the Times", "Parade"]),
 ("White lines from a pulsar on a black background", "Unknown Pleasures", ["Closer", "Power, Corruption & Lies", "Substance"]),
 ("A motorbike bursting out of a grave", "Bat Out of Hell", ["Dead Ringer", "Welcome to My Nightmare", "Hysteria"]),
 ("A banana by Andy Warhol", "The Velvet Underground & Nico", ["White Light/White Heat", "Loaded", "Transformer"]),
 ("Pink and yellow, with ransom-note lettering", "Never Mind the Bollocks", ["Damned Damned Damned", "Pink Flag", "The Clash"]),
 ("A New York tenement with cut-out windows", "Physical Graffiti", ["Houses of the Holy", "Led Zeppelin IV", "Presence"]),
 ("A face with a red and blue lightning bolt across it", "Aladdin Sane", ["The Rise and Fall of Ziggy Stardust", "Hunky Dory", "Heroes"]),
 ("A cow standing in a field, and no words at all", "Atom Heart Mother", ["Ummagumma", "Obscured by Clouds", "More"])])

race("which nursery rhyme is this line from?", "Children's books", "easy", ["nursery rhymes", "childhood"], [
 ("Went up the hill to fetch a pail of water", "Jack and Jill", ["Doctor Foster", "Jack Sprat", "Lucy Locket"]),
 ("Sat on a wall and had a great fall", "Humpty Dumpty", ["Rock-a-bye Baby", "Simple Simon", "Goosey Goosey Gander"]),
 ("The cow jumped over the moon", "Hey Diddle Diddle", ["Twinkle Twinkle Little Star", "Wee Willie Winkie", "Lavender's Blue"]),
 ("Three bags full", "Baa Baa Black Sheep", ["Little Boy Blue", "Goosey Goosey Gander", "Lavender's Blue"]),
 ("Sat on a tuffet, eating her curds and whey", "Little Miss Muffet", ["Lucy Locket", "Polly Put the Kettle On", "Pease Porridge Hot"]),
 ("Its fleece was white as snow", "Mary Had a Little Lamb", ["Little Boy Blue", "Lavender's Blue", "Goosey Goosey Gander"]),
 ("The mouse ran up the clock", "Hickory Dickory Dock", ["The Muffin Man", "This Old Man", "Wee Willie Winkie"]),
 ("Went to the cupboard to fetch her poor dog a bone", "Old Mother Hubbard", ["There Was an Old Woman Who Lived in a Shoe", "Polly Put the Kettle On", "Lucy Locket"]),
 ("Sat in the corner eating his Christmas pie", "Little Jack Horner", ["Little Tommy Tucker", "Simple Simon", "Jack Sprat"]),
 ("Four and twenty blackbirds baked in a pie", "Sing a Song of Sixpence", ["Simple Simon", "Hot Cross Buns", "Little Tommy Tucker"]),
 ("The farmer's wife cut off their tails with a carving knife", "Three Blind Mice", ["This Old Man", "The Muffin Man", "Rub-a-dub-dub"]),
 ("Kissed the girls and made them cry", "Georgie Porgie", ["Bobby Shafto", "Tom, Tom, the Piper's Son", "Simple Simon"]),
 ("Has lost her sheep and doesn't know where to find them", "Little Bo Peep", ["Little Boy Blue", "Lucy Locket", "Goosey Goosey Gander"]),
 ("A pocket full of posies; atishoo, atishoo", "Ring a Ring o' Roses", ["Lavender's Blue", "London Bridge Is Falling Down", "Pat-a-Cake"]),
 ("He had ten thousand men and marched them up to the top of the hill", "The Grand Old Duke of York", ["Tom, Tom, the Piper's Son", "This Old Man", "Bobby Shafto"]),
 ("Half a pound of tuppenny rice, half a pound of treacle", "Pop Goes the Weasel", ["Pease Porridge Hot", "Hot Cross Buns", "Polly Put the Kettle On"]),
 ("Say the bells of St Clement's", "Oranges and Lemons", ["London Bridge Is Falling Down", "Lavender's Blue", "Pat-a-Cake"]),
 ("Pussy's in the well", "Ding Dong Bell", ["Pussy Cat, Pussy Cat", "Doctor Foster", "Ladybird Ladybird"]),
 ("A merry old soul, who called for his pipe and his bowl", "Old King Cole", ["Simple Simon", "Tom, Tom, the Piper's Son", "The Muffin Man"]),
 ("Silver bells and cockle shells, and pretty maids all in a row", "Mary, Mary, Quite Contrary", ["Lavender's Blue", "Lucy Locket", "Ladybird Ladybird"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-106.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
