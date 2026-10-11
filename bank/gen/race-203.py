# Bank session 11 Oct 2026: 3 more general races -> bank/race-203.json (Coronation Street, Blackadder and Father Ted words). 20 rows each, target 10; wrong options are
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

race("what's this Coronation Street word?", "TV", "easy", ["Coronation Street", "soaps", "words"], [
 ("The pub", "Rovers Return", ["Queen Vic", "Woolpack", "Nag's Head"]),
 ("The fictional town", "Weatherfield", ["Walford", "Holby", "Ambridge"]),
 ("The longest-serving character, there since 1960", "Ken Barlow", ["Jack Duckworth", "Mike Baldwin", "Alf Roberts"]),
 ("The actor who plays him", "William Roache", ["William Shatner", "Bill Tarmey", "Roy Hudd"]),
 ("The café", "Roy's Rolls", ["Rita's Rolls", "Dev's Deli", "Betty's Buns"]),
 ("Rita's newsagent", "The Kabin", ["The Corner Shop", "The Bookies", "The Chippy"]),
 ("The nosy Kabin assistant", "Norris Cole", ["Fred Elliott", "Percy Sugden", "Curly Watts"]),
 ("The knicker factory", "Underworld", ["Overworld", "Netherworld", "Undercroft"]),
 ("The famous dish served at the Rovers", "Betty's hotpot", ["Betty's pie", "Lancashire stew", "Scouse"]),
 ("The cleaner with curlers and flying ducks on her wall", "Hilda Ogden", ["Ena Sharples", "Annie Walker", "Elsie Tanner"]),
 ("The barmaid famous for leopard print and big earrings", "Bet Lynch", ["Raquel Watts", "Liz McDonald", "Annie Walker"]),
 ("The couple with the pigeons", "Jack and Vera Duckworth", ["Jack and Rose", "Ken and Deirdre", "Fred and Rose"]),
 ("Ken's wife with the big glasses", "Deirdre", ["Doreen", "Dolly", "Deborah"]),
 ("The campaign when she was wrongly jailed", "Free the Weatherfield One", ["Free the Birmingham Six", "Free Willy", "Free Nelson Mandela"]),
 ("The garage mechanic", "Kevin Webster", ["Steve McDonald", "Curly Watts", "Martin Platt"]),
 ("The woman married more times than anyone else on the Street", "Gail Platt", ["Rita Sullivan", "Deirdre Barlow", "Sally Webster"]),
 ("The year it started", "1960", ["1955", "1965", "1972"]),
 ("The TV company that made it", "Granada", ["Thames", "Tyne Tees", "Yorkshire"]),
 ("What the street is paved with", "Cobbles", ["Tarmac", "Gravel", "Flagstones"]),
 ("The 2010 disaster for the 50th anniversary", "Tram crash", ["Train crash", "Plane crash", "Bus crash"])])

race("what's this Blackadder word?", "TV", "medium", ["Blackadder", "sitcoms", "words"], [
 ("The dogsbody", "Baldrick", ["Badger", "Bodkin", "Bumble"]),
 ("What he always has", "Cunning plan", ["Bright spark", "Golden ticket", "Lucky charm"]),
 ("His favourite vegetable", "Turnip", ["Parsnip", "Swede", "Potato"]),
 ("Blackadder's first name", "Edmund", ["Edward", "Edgar", "Edwin"]),
 ("Lord ..., Edmund's dim friend in series two", "Percy", ["Pip", "Perkins", "Piers"]),
 ("Elizabeth I's nickname, played by Miranda Richardson", "Queenie", ["Liz", "Bessie", "Betty"]),
 ("Her batty old nurse", "Nursie", ["Matron", "Granny", "Sister"]),
 ("Stephen Fry's blustering general", "Melchett", ["Montgomery", "Haig", "Kitchener"]),
 ("Captain ..., Melchett's sidekick", "Darling", ["Darcy", "Dashwood", "Dorling"]),
 ("The dim Prince Regent in series three", "George", ["Frederick", "William", "Albert"]),
 ("The girl disguised as a boy", "Bob", ["Sam", "Jo", "Charlie"]),
 ("Lord ..., Rik Mayall's show-off", "Flashheart", ["Flashman", "Flash Gordon", "Fleetfoot"]),
 ("The coffee shop owner", "Mrs Miggins", ["Mrs Doyle", "Mrs Brown", "Mrs Overall"]),
 ("The era of the first series", "Middle Ages", ["Stone Age", "Iron Age", "Space Age"]),
 ("The era of series two", "Elizabethan", ["Victorian", "Edwardian", "Georgian"]),
 ("The final series, in the First World War trenches", "Blackadder Goes Forth", ["Blackadder the Third", "Blackadder Back & Forth", "Blackadder Rides Out"]),
 ("Played Edmund", "Rowan Atkinson", ["Rowan Williams", "Ronnie Barker", "Rik Mayall"]),
 ("Played Baldrick", "Tony Robinson", ["Tim McInnerny", "Robbie Coltrane", "Patrick Barlow"]),
 ("Played George", "Hugh Laurie", ["Hugh Grant", "Hugh Dennis", "Stephen Fry"]),
 ("The co-writer alongside Ben Elton", "Richard Curtis", ["Richard Osman", "Ricky Gervais", "John Sullivan"])])

race("what's this Father Ted word?", "TV", "medium", ["Father Ted", "sitcoms", "words"], [
 ("Where the parochial house is", "Craggy Island", ["Fantasy Island", "Rugged Island", "Rocky Island"]),
 ("Ted's dim young sidekick", "Dougal", ["Dermot", "Declan", "Desmond"]),
 ("The drunk who shouts 'Drink! Feck! Arse!'", "Father Jack", ["Father Brown", "Father Dowling", "Father Christmas"]),
 ("Father Jack's favourite word", "Feck", ["Heck", "Flip", "Bother"]),
 ("The housekeeper who insists 'Go on, go on, go on'", "Mrs Doyle", ["Mrs Brown", "Mrs Mop", "Mrs Overall"]),
 ("What she's always forcing on people", "Tea", ["Coffee", "Toast", "Scones"]),
 ("The furious bishop Ted kicks up the arse", "Bishop Brennan", ["Bishop Tutu", "Bishop Auckland", "Bishop's Stortford"]),
 ("The contest Ted and Dougal enter", "Eurovision", ["Britain's Got Talent", "Opportunity Knocks", "The X Factor"]),
 ("Their entry", "My Lovely Horse", ["My Little Pony", "My Old Man's a Dustman", "Horse with No Name"]),
 ("Ted's lesson with toy cows: these are small, those are ...", "Far away", ["Big", "Tall", "Fake"]),
 ("The beauty contest Ted judges", "Lovely Girls", ["Miss World", "Pretty Woman", "Fair Maidens"]),
 ("The placard Ted and Dougal carry in protest", "Down with this sort of thing", ["Not in my name", "Make love not war", "Ban the bomb"]),
 ("The hyper youth priest played by Graham Norton", "Father Noel", ["Father Dougal", "Father Damo", "Father Larry"]),
 ("Played Ted", "Dermot Morgan", ["Dermot O'Leary", "Brendan O'Carroll", "Graham Norton"]),
 ("Played Dougal", "Ardal O'Hanlon", ["Frank Kelly", "Chris O'Dowd", "Jason Byrne"]),
 ("Played Mrs Doyle", "Pauline McLynn", ["Pauline Quirke", "Pauline Collins", "Brenda Fricker"]),
 ("Co-writer with Arthur Mathews", "Graham Linehan", ["Graham Taylor", "Graham Kendrick", "Graham Fellows"]),
 ("The channel it aired on", "Channel 4", ["RTÉ", "BBC Two", "ITV"]),
 ("The country it's set in", "Ireland", ["Scotland", "Wales", "Isle of Man"]),
 ("Ted's job", "Priest", ["Vicar", "Rabbi", "Monk"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-203.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
