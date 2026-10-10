# Bank session 10 Oct 2026: 2 more general races -> bank/race-94.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Diamond'?", "General knowledge", "medium", ["diamonds", "wordplay"], [
 ("Elizabeth II's 60 years on the throne, celebrated in 2012", "Diamond Jubilee", ["Golden Jubilee", "Platinum Jubilee", "Ruby Jubilee"]), ("Sean Connery's last official Bond film, from 1971", "Diamonds Are Forever", ["Thunderball", "You Only Live Twice", "Live and Let Die"]),
 ("The singer of 'Sweet Caroline'", "Neil Diamond", ["Neil Young", "Barry Manilow", "Billy Joel"]), ("Athletics' yearly series of top meetings", "Diamond League", ["Golden League", "Grand Prix", "Super Series"]),
 ("The 'cursed' blue gem in the Smithsonian", "Hope Diamond", ["Koh-i-Noor", "Cullinan", "Star of India"]), ("Marilyn Monroe's song in Gentlemen Prefer Blondes", "Diamonds Are a Girl's Best Friend", ["I Wanna Be Loved by You", "Happy Birthday, Mr. President", "Bye Bye Baby"]),
 ("David Bowie's 1974 album", "Diamond Dogs", ["Aladdin Sane", "Ziggy Stardust", "Young Americans"]), ("Sade's 1984 debut album", "Diamond Life", ["Promise", "Stronger Than Pride", "Love Deluxe"]),
 ("Leonardo DiCaprio's 2006 film set in Sierra Leone", "Blood Diamond", ["The Departed", "Body of Lies", "The Constant Gardener"]), ("The strong white cider of 1990s park benches", "Diamond White", ["White Lightning", "Strongbow", "Frosty Jack's"]),
 ("The 60th wedding anniversary", "Diamond", ["Platinum", "Golden", "Emerald"]), ("Pink Floyd's tribute to Syd Barrett", "Shine On You Crazy Diamond", ["Wish You Were Here", "Comfortably Numb", "Money"]),
 ("Rihanna's 2012 hit", "Diamonds", ["Umbrella", "Work", "Only Girl (In the World)"]), ("A good-hearted person with rough manners", "Rough diamond", ["Black sheep", "Dark horse", "Loose cannon"]),
 ("A thoroughly decent bloke, in London slang", "Diamond geezer", ["Wide boy", "Jack the lad", "Barrow boy"]), ("The infield of a baseball park", "Baseball diamond", ["Pitcher's mound", "Bullpen", "Dugout"]),
 ("The flash of sunlight just before totality in a solar eclipse", "Diamond ring", ["Baily's beads", "Corona", "Halo"]), ("The American rattlesnake with patterned scales", "Diamondback", ["Sidewinder", "Copperhead", "Cottonmouth"]),
 ("The Beatles song on Sgt. Pepper, some say about LSD", "Lucy in the Sky with Diamonds", ["Strawberry Fields Forever", "I Am the Walrus", "Across the Universe"]), ("The cruise ship quarantined off Japan in early 2020", "Diamond Princess", ["Ruby Princess", "Queen Mary 2", "Oasis of the Seas"])])

race("which famous 'Crown'?", "General knowledge", "medium", ["crowns", "wordplay"], [
 ("Netflix's drama about Elizabeth II", "The Crown", ["Victoria", "The Windsors", "Downton Abbey"]), ("Kept under guard in the Tower of London", "The Crown Jewels", ["The Stone of Destiny", "The Great Seal", "The Royal Standard"]),
 ("The Six Nations prize for a home nation that beats the other three", "Triple Crown", ["Grand Slam", "Calcutta Cup", "Wooden spoon"]), ("Where serious criminal cases are tried in England", "Crown Court", ["Magistrates' Court", "High Court", "County Court"]),
 ("The bowls played on a domed green, popular in the north", "Crown green bowls", ["Flat green bowls", "Croquet", "Pétanque"]), ("Fine bone china made in Derby", "Royal Crown Derby", ["Royal Doulton", "Wedgwood", "Spode"]),
 ("The body that prosecutes crimes in England and Wales", "Crown Prosecution Service", ["Serious Fraud Office", "Ministry of Justice", "Home Office"]), ("The landlord of Regent Street and most of the UK seabed", "The Crown Estate", ["Duchy of Lancaster", "Duchy of Cornwall", "National Trust"]),
 ("Jersey, Guernsey and the Isle of Man", "Crown Dependencies", ["Overseas Territories", "Commonwealth Realms", "Home Counties"]), ("The old coin worth two shillings and sixpence", "Half a crown", ["Florin", "Shilling", "Sixpence"]),
 ("The starfish eating away the Great Barrier Reef", "Crown-of-thorns", ["Sunflower star", "Brittle star", "Sea urchin"]), ("The heir to a throne", "Crown Prince", ["Viceroy", "Regent", "Archduke"]),
 ("The 1968 heist film with Steve McQueen, remade with Pierce Brosnan", "The Thomas Crown Affair", ["The Italian Job", "Bullitt", "The Getaway"]), ("The crown placed on the monarch's head at the coronation", "St Edward's Crown", ["Crown of Scotland", "Tudor Crown", "Coronet of George"]),
 ("The crown the monarch wears to open Parliament", "Imperial State Crown", ["Crown of Scotland", "Tudor Crown", "State Diadem"]), ("The British paint brand", "Crown Paints", ["Dulux", "Farrow & Ball", "Johnstone's"]),
 ("The old pub dice game with card suits on the dice", "Crown and Anchor", ["Shut the Box", "Liar's dice", "Yahtzee"]), ("The hotel chain from the same group as Holiday Inn", "Crowne Plaza", ["Premier Inn", "Travelodge", "Hilton"]),
 ("What a dentist fits over a broken tooth", "Crown", ["Filling", "Veneer", "Bridge"]), ("The BBC's films of Shakespeare's history plays", "The Hollow Crown", ["Wolf Hall", "The White Queen", "The Last Kingdom"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-94.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
