# Bank session 11 Oct 2026: 3 more general races -> bank/race-180.json (wrestling, talent show and horror film words). 20 rows each, target 10; wrong options are
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

race("what's this wrestling word?", "Sport", "medium", ["wrestling", "WWE", "words"], [
 ("Lifting and throwing your opponent flat onto the mat", "Body slam", ["Slam dunk", "Grand slam", "Door slam"]),
 ("Holding the shoulders down for a three-count", "Pin", ["Stitch", "Clip", "Tack"]),
 ("Pairs who swap in by touching hands", "Tag team", ["Tag rugby", "Price tag", "Dog tag"]),
 ("The padded corner post of the ring", "Turnbuckle", ["Belt buckle", "Swashbuckle", "Turntable"]),
 ("Wrestling's word for a villain", "Heel", ["Toe", "Sole", "Arch"]),
 ("Wrestling's word for a goodie", "Face", ["Mask", "Brow", "Chin"]),
 ("The British wrestler famous on Saturday-afternoon TV", "Big Daddy", ["Giant Haystacks", "Kendo Nagasaki", "Mick McManus"]),
 ("The ITV show where British wrestling went out on Saturdays", "World of Sport", ["Grandstand", "Sportsnight", "Superstars"]),
 ("The American wrestling company, by its initials", "WWE", ["NFL", "UFC", "NBA"]),
 ("The moustached star of 'Hulkamania'", "Hulk Hogan", ["André the Giant", "Randy Savage", "Ric Flair"]),
 ("Dwayne Johnson's ring name", "The Rock", ["The Stone", "The Boulder", "The Pebble"]),
 ("Making your opponent tap out", "Submission", ["Admission", "Permission", "Commission"]),
 ("A throw lifting the opponent overhead and falling backwards", "Suplex", ["Duplex", "Triplex", "Complex"]),
 ("The 30-man battle royal event", "Royal Rumble", ["Rumble in the Jungle", "Royal Variety", "Royal Flush"]),
 ("What the champion holds aloft", "Championship belt", ["Seat belt", "Black belt", "Green belt"]),
 ("Where the bout happens, surrounded by ropes", "Ring", ["Rink", "Court", "Pitch"]),
 ("Keeping up the pretence that it's all real", "Kayfabe", ["Kebab", "Kaftan", "Kaput"]),
 ("Swinging an outstretched arm into someone's neck", "Clothesline", ["Washing line", "Hemline", "Punchline"]),
 ("Climbing up to grab a prize hanging over the ring", "Ladder match", ["Snakes and ladders", "Stepladder", "Rope ladder"]),
 ("Counts '1, 2, 3!' slapping the mat", "Referee", ["Commentator", "Manager", "Valet"])])

race("what's this talent show word?", "TV", "easy", ["talent shows", "X Factor", "words"], [
 ("The first performance in front of the judges", "Audition", ["Addition", "Edition", "Ambition"]),
 ("The Britain's Got Talent button that sends an act straight to the live shows", "Golden buzzer", ["Golden ticket", "Golden handshake", "Golden goose"]),
 ("The X Factor stage where acts visit their mentor, often abroad", "Judges' houses", ["Big Brother house", "Halfway house", "Open house"]),
 ("The X Factor's tough stage between auditions and judges' houses", "Bootcamp", ["Base camp", "Holiday camp", "Boot sale"]),
 ("Saturday nights where the public votes", "Live shows", ["Roadshows", "Chat shows", "Peep shows"]),
 ("How viewers keep their favourites in", "Phone vote", ["Show of hands", "Coin toss", "Secret ballot"]),
 ("The bottom two perform again", "Sing-off", ["Dance-off", "Bake-off", "Face-off"]),
 ("A judge who coaches a category", "Mentor", ["Matron", "Steward", "Prefect"]),
 ("The red cross button pressed when an act flops", "Buzzer", ["Doorbell", "Klaxon", "Alarm clock"]),
 ("'Mr Nasty', the judge who created The X Factor", "Simon Cowell", ["Louis Walsh", "Piers Morgan", "Sharon Osbourne"]),
 ("The dance troupe that won BGT in 2009", "Diversity", ["Susan Boyle", "Ashley and Pudsey", "Flawless"]),
 ("The dancing dog who won BGT in 2012", "Pudsey", ["Gromit", "Lassie", "Scooby"]),
 ("The 2006 X Factor winner who hit number one with 'Bleeding Love'", "Leona Lewis", ["Alexandra Burke", "Shayne Ward", "Olly Murs"]),
 ("The first Pop Idol winner, in 2002", "Will Young", ["Gareth Gates", "Darius", "Michelle McManus"]),
 ("The show where judges turn their chairs", "The Voice", ["The Chair", "The Throne", "The Swivel"]),
 ("The sob story told before an act performs", "Backstory", ["Back pay", "Backstage", "Backdrop"]),
 ("The hosts of Britain's Got Talent", "Ant and Dec", ["Holly and Phil", "Richard and Judy", "Fearne and Reggie"]),
 ("A rejected act brought back for another chance", "Wildcard", ["Red card", "Postcard", "Scorecard"]),
 ("The last live show, where the winner is crowned", "Final", ["Opener", "Pilot", "Encore"]),
 ("What the winner signs with a record label", "Contract", ["Contraption", "Contrast", "Contraflow"])])

race("what's this horror film word?", "Film", "medium", ["horror films", "scary movies", "words"], [
 ("A sudden shock to make you leap from your seat", "Jump scare", ["Jump start", "Jump leads", "Jumpsuit"]),
 ("A ghost-filled home", "Haunted house", ["Farmhouse", "Penthouse", "Townhouse"]),
 ("The last survivor, who faces the killer", "Final girl", ["Final whistle", "Final score", "Final straw"]),
 ("A horror film with a masked killer and a knife", "Slasher", ["Thrasher", "Crasher", "Washer"]),
 ("An undead flesh-eater shuffling about", "Zombie", ["Banshee", "Poltergeist", "Gremlin"]),
 ("An undead blood-drinker", "Vampire", ["Banshee", "Poltergeist", "Ghoul"]),
 ("A man who turns into a wolf at full moon", "Werewolf", ["Banshee", "Gremlin", "Ghoul"]),
 ("When a demon takes over someone's body", "Possession", ["Procession", "Profession", "Obsession"]),
 ("The ritual to drive the demon out", "Exorcism", ["Exercise", "Excursion", "Extortion"]),
 ("A gathering to contact the dead", "Séance", ["Seesaw", "Sequence", "Scene"]),
 ("A board with letters for spelling out spirit messages", "Ouija board", ["Dartboard", "Chessboard", "Surfboard"]),
 ("The British studio famous for Dracula films with Christopher Lee", "Hammer", ["Ealing", "Pinewood", "Aardman"]),
 ("The author of Carrie, It and The Shining", "Stephen King", ["Dean Koontz", "James Herbert", "Clive Barker"]),
 ("A spooky setting full of tombstones", "Graveyard", ["Shipyard", "Farmyard", "Junkyard"]),
 ("Leatherface's weapon in Texas", "Chainsaw", ["Pitchfork", "Crowbar", "Sledgehammer"]),
 ("The style of The Blair Witch Project, as if filmed on a real camera", "Found footage", ["Stock footage", "Square footage", "Footnote"]),
 ("The killer doll in Child's Play", "Chucky", ["Barbie", "Sindy", "Cabbage Patch"]),
 ("When the werewolf transforms", "Full moon", ["Half moon", "New moon", "Blue moon"]),
 ("What wards off vampires", "Garlic", ["Ginger", "Onion", "Chilli"]),
 ("What kills a werewolf", "Silver bullet", ["Golden ticket", "Silver spoon", "Silver lining"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-180.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
