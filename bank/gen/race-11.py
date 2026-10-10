# Bank session 10 Oct 2026: 4 more general races -> bank/race-11.json. 20 rows each, target 10; wrong options are
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

race("name the famous pig", "Film, TV and books", "medium", ["pigs", "characters"], [
 ("The muddy-puddle-jumping pig", "Peppa", ["Suzy Sheep", "Rebecca Rabbit", "Candy Cat"]), ("Peppa's little brother", "George", ["Richard Rabbit", "Danny Dog", "Pedro Pony"]),
 ("The sheep-pig", "Babe", ["Rex", "Ferdinand", "Maa"]), ("Kermit's karate-chopping love", "Miss Piggy", ["Fozzie", "Gonzo", "Janice"]),
 ("Charlotte's Web's pig", "Wilbur", ["Templeton", "Avery", "Homer"]), ("Pooh's very small friend", "Piglet", ["Roo", "Eeyore", "Kanga"]),
 ("'Th-th-that's all, folks!'", "Porky", ["Petunia", "Elmer", "Daffy"]), ("The Animal Farm pig who becomes a tyrant", "Napoleon", ["Minimus", "Pinkeye", "Boxer"]),
 ("The Animal Farm pig chased off the farm", "Snowball", ["Minimus", "Pinkeye", "Moses"]), ("The old boar whose dream starts the revolution", "Old Major", ["Benjamin", "Minimus", "Mr Jones"]),
 ("Napoleon's smooth-talking spokespig", "Squealer", ["Minimus", "Pinkeye", "Moses"]), ("Toy Story's piggy bank", "Hamm", ["Rex", "Slinky", "Bullseye"]),
 ("Homer's pet in The Simpsons Movie", "Spider-Pig", ["Santa's Little Helper", "Snowball II", "Pinchy"]), ("Doctor Dolittle's pig", "Gub-Gub", ["Jip", "Dab-Dab", "Polynesia"]),
 ("Beatrix Potter's pig who goes to market", "Pigling Bland", ["Pig-wig", "Aunt Pettitoes", "Alexander"]), ("The 'super pig' in the Netflix film", "Okja", ["Mija", "Lucy Mirando", "Jay"]),
 ("Lord Emsworth's prize sow", "Empress of Blandings", ["Pride of Matchingham", "Queen of Matchingham", "Lady Bracknell"]), ("The fortune-telling pig in The Black Cauldron", "Hen Wen", ["Gurgi", "Taran", "Eilonwy"]),
 ("Gravity Falls' pet pig", "Waddles", ["Gompers", "Soos", "Stan"]), ("M&S's sweet pig", "Percy Pig", ["Colin the Caterpillar", "Penny Pig", "Freddo"])])

race("what's the NATO phonetic word for this letter?", "Words and language", "medium", ["NATO alphabet", "letters"], [
 ("B", "Bravo", ["Baker", "Beta", "Boston"]), ("C", "Charlie", ["Castle", "Coca", "Carlo"]), ("D", "Delta", ["Dog", "David", "Dixie"]),
 ("E", "Echo", ["Easy", "Edward", "Eagle"]), ("F", "Foxtrot", ["Fox", "Freddie", "Falcon"]), ("G", "Golf", ["George", "Gamma", "Gulf"]),
 ("H", "Hotel", ["How", "Harry", "Hector"]), ("J", "Juliett", ["Jig", "Jupiter", "Johnny"]), ("K", "Kilo", ["King", "Kansas", "Kitten"]),
 ("L", "Lima", ["Love", "London", "Lemon"]), ("M", "Mike", ["Mother", "Madrid", "Mexico"]), ("N", "November", ["Nan", "Nectar", "Norway"]),
 ("P", "Papa", ["Peter", "Paris", "Panama"]), ("Q", "Quebec", ["Queen", "Quiet", "Quilt"]), ("R", "Romeo", ["Roger", "Rome", "Robert"]),
 ("S", "Sierra", ["Sugar", "Samba", "Santiago"]), ("T", "Tango", ["Tare", "Toby", "Texas"]), ("U", "Uniform", ["Uncle", "Union", "Utah"]),
 ("V", "Victor", ["Violet", "Venus", "Vienna"]), ("W", "Whiskey", ["William", "Water", "Winter"])])

race("what does this text speak stand for?", "Words and language", "easy", ["abbreviations", "texting"], [
 ("LOL", "Laugh out loud", ["Lots of love", "Laughing online", "Loads of laughs"]), ("BRB", "Be right back", ["Be really brief", "Bring round beer", "Back real busy"]),
 ("IMO", "In my opinion", ["In my office", "If memory obliges", "I'm moving on"]), ("TBH", "To be honest", ["Text back home", "Talk between hours", "To be happy"]),
 ("FOMO", "Fear of missing out", ["Fear of moving on", "Friends of mine only", "Full of myself, obviously"]), ("SMH", "Shaking my head", ["So much hate", "Send me home", "Sorry, my heart"]),
 ("IRL", "In real life", ["I really love", "In red letters", "If really late"]), ("TL;DR", "Too long; didn't read", ["Talk later; don't reply", "Too late; don't rush", "Time lost; do redo"]),
 ("OMG", "Oh my God", ["On my go", "Out my gate", "Over my grave"]), ("NGL", "Not gonna lie", ["Never gonna leave", "Nice game, lads", "No good lately"]),
 ("IDK", "I don't know", ["I don't care", "I did know", "It doesn't count"]), ("FYI", "For your information", ["Find your inbox", "For your instance", "Fix your internet"]),
 ("BTW", "By the way", ["Back to work", "Before the weekend", "Better than wine"]), ("ASAP", "As soon as possible", ["Always say a please", "At some agreed point", "As slow as possible"]),
 ("DM", "Direct message", ["Daily mail", "Don't mention", "Deleted message"]), ("TTYL", "Talk to you later", ["Thanks to you lot", "Time to yawn loudly", "Try to stay late"]),
 ("ROFL", "Rolling on the floor laughing", ["Running out for lunch", "Really overly funny, lol", "Rather odd, full laugh"]), ("YOLO", "You only live once", ["You owe lots of", "Your old lady's out", "You obviously love others"]),
 ("GOAT", "Greatest of all time", ["Good on all teams", "Getting old at thirty", "Got our attention, thanks"]), ("BFF", "Best friends forever", ["Big fat favour", "Best for fun", "Back from France"])])

race("on which date is this saint's day?", "Faiths and festivals", "hard", ["saints", "dates"], [
 ("St David", "1 March", ["1 April", "1 February", "8 March"]), ("St Patrick", "17 March", ["7 March", "17 April", "27 March"]),
 ("St George", "23 April", ["23 March", "13 April", "23 May"]), ("St Andrew", "30 November", ["30 October", "1 December", "13 November"]),
 ("St Valentine", "14 February", ["14 March", "4 February", "12 February"]), ("St Swithin", "15 July", ["15 August", "5 July", "25 July"]),
 ("St Stephen", "26 December", ["27 December", "28 December", "26 November"]), ("St Nicholas", "6 December", ["8 December", "6 November", "16 December"]),
 ("St Crispin", "25 October", ["24 October", "15 October", "25 November"]), ("St John the Baptist", "24 June", ["21 June", "24 July", "4 June"]),
 ("St Joseph", "19 March", ["9 March", "29 March", "19 April"]), ("St Mark", "25 April", ["24 April", "15 April", "25 March"]),
 ("St Michael (Michaelmas)", "29 September", ["21 September", "29 August", "9 September"]), ("St Cuthbert", "20 March", ["20 February", "2 March", "10 March"]),
 ("St Bede", "25 May", ["5 May", "15 May", "25 June"]), ("St Aidan", "31 August", ["31 July", "1 September", "13 August"]),
 ("St Agnes", "21 January", ["12 January", "21 February", "1 January"]), ("St Dwynwen (Welsh Valentine's Day)", "25 January", ["5 January", "15 January", "25 February"]),
 ("St Lucy", "13 December", ["3 December", "13 November", "23 December"]), ("St Luke", "18 October", ["8 October", "18 November", "28 October"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
