# Bank session 11 Oct 2026: 3 more general races -> bank/race-200.json (Bake Off, I'm a Celebrity and Love Island words). 20 rows each, target 10; wrong options are
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

race("what's this Bake Off word?", "TV", "easy", ["Great British Bake Off", "baking", "words"], [
 ("The title for the best baker of the week", "Star Baker", ["Master Baker", "Head Chef", "Top Dog"]),
 ("The big final challenge each week", "Showstopper", ["Showboat", "Show-off", "Doorstopper"]),
 ("The blind bake with a bare-bones recipe", "Technical", ["Tactical", "Theoretical", "Topical"]),
 ("The first bake of the week, a tried-and-tested recipe", "Signature", ["Autograph", "Trademark", "Hallmark"]),
 ("The undercooked pastry base the judges dread", "Soggy bottom", ["Soft centre", "Burnt crust", "Sunken middle"]),
 ("Paul's rare seal of approval", "Hollywood handshake", ["Hollywood smile", "Golden handshake", "Hollywood star"]),
 ("Where it's all filmed", "The tent", ["The studio", "The kitchen", "The shed"]),
 ("The week of loaves, plaits and proving", "Bread Week", ["Cake Week", "Pastry Week", "Dessert Week"]),
 ("The warm drawer where dough rises", "Proving drawer", ["Bottom drawer", "Cutlery drawer", "Top drawer"]),
 ("The judge with the piercing blue eyes", "Paul Hollywood", ["Paul Rankin", "Paul Ainsworth", "Paul O'Grady"]),
 ("The original judge famous for her florals", "Mary Berry", ["Mary Portas", "Mary Beard", "Delia Smith"]),
 ("The judge who replaced her", "Prue Leith", ["Monica Galetti", "Delia Smith", "Nigella Lawson"]),
 ("The host with the goth hair and wild shirts", "Noel Fielding", ["Russell Brand", "Russell Kane", "Rhys Thomas"]),
 ("The original presenting duo", "Mel and Sue", ["Ant and Dec", "Richard and Judy", "French and Saunders"]),
 ("The channel it moved to in 2017", "Channel 4", ["BBC Two", "ITV", "Sky One"]),
 ("The 2015 winner who later baked the Queen's 90th birthday cake", "Nadiya Hussain", ["Candice Brown", "Rahul Mandal", "Jo Wheatley"]),
 ("The dessert at the heart of Iain's famous bin moment", "Baked Alaska", ["Arctic roll", "Bombe", "Pavlova"]),
 ("The pattern on the bunting and tablecloths", "Gingham", ["Tartan", "Paisley", "Polka dot"]),
 ("The words that start each bake", "On your marks, get set, bake!", ["Ready, steady, cook!", "Let battle commence!", "Lights, camera, action!"]),
 ("The spin-off for pastry chefs", "Bake Off: The Professionals", ["Junior Bake Off", "MasterChef", "Extra Slice"])])

race("what's this I'm a Celebrity word?", "TV", "easy", ["I'm a Celebrity", "reality TV", "words"], [
 ("Eating bugs or lying in a box of critters to win meals", "Bushtucker trial", ["Jungle drum", "Bush fire", "Outback test"]),
 ("The camp's diary room", "Bush Telegraph", ["Jungle Book", "Bush Radio", "Talk Shack"]),
 ("The presenting double act", "Ant and Dec", ["Mel and Sue", "Holly and Phil", "Dick and Dom"]),
 ("The winner's title", "King or Queen of the Jungle", ["Lord of the Flies", "Top Banana", "Head Honcho"]),
 ("Where the celebrities live", "Camp", ["Base", "Den", "Lodge"]),
 ("Two campmates answering questions to win a treat", "Dingo Dollar challenge", ["Kangaroo Court", "Dingo Dash", "Wallaby Run"]),
 ("The comedy shopkeeper at the challenge stall", "Kiosk Keith", ["Shop Steve", "Ticket Tony", "Counter Colin"]),
 ("The Welsh castle used during Covid", "Gwrych Castle", ["Conwy Castle", "Caernarfon Castle", "Bamburgh Castle"]),
 ("Where it's usually filmed", "Australia", ["New Zealand", "South Africa", "Borneo"]),
 ("Creepy-crawlies tipped over the celebrities", "Critters", ["Gremlins", "Minions", "Muppets"]),
 ("Being voted out", "Eviction", ["Ejection", "Exorcism", "Extradition"]),
 ("The very first winner, in 2002", "Tony Blackburn", ["Phil Tufnell", "Kerry Katona", "Joe Pasquale"]),
 ("The basic camp rations", "Rice and beans", ["Beans on toast", "Fish and chips", "Rice pudding"]),
 ("The infamous delicacy eaten in the trials", "Kangaroo testicles", ["Kangaroo court", "Kangaroo pouch", "Emu egg"]),
 ("The camp toilet, in Aussie slang", "Dunny", ["Dummy", "Dungeon", "Dinghy"]),
 ("The final-week game of giant slides and water", "Celebrity Cyclone", ["Celebrity Juice", "Celebrity Squares", "Cyclone Tracy"]),
 ("What each trial wins for the camp's meals", "Stars", ["Hearts", "Points", "Coins"]),
 ("What a celebrity shouts to quit a trial", "I'm a Celebrity, get me out of here!", ["I want my mummy!", "Beam me up, Scotty!", "Stop the world, I want to get off!"]),
 ("The campmate voted in to run things", "Camp leader", ["Shop steward", "Prefect", "Head boy"]),
 ("The MP who went in while still sitting, in 2022", "Matt Hancock", ["Nigel Farage", "Boris Johnson", "Michael Gove"])])

race("what's this Love Island word?", "TV", "easy", ["Love Island", "reality TV", "words"], [
 ("Where the Islanders live", "Villa", ["Chalet", "Lodge", "Castle"]),
 ("The ceremony where Islanders pick partners", "Recoupling", ["Reshuffle", "Re-run", "Retake"]),
 ("The second villa that tests the couples", "Casa Amor", ["Casa Blanca", "Casa Rosa", "Cosa Nostra"]),
 ("Working hard to win someone over", "Grafting", ["Crafting", "Drafting", "Rafting"]),
 ("A sudden turn-off", "Ick", ["Itch", "Tick", "Kick"]),
 ("Where they spill their thoughts to camera", "Beach Hut", ["Bus shelter", "Garden shed", "Phone box"]),
 ("Disrespected or made a fool of", "Mugged off", ["Mugged up", "Mug shot", "Teed off"]),
 ("Shouted the moment a phone buzzes", "I've got a text!", ["I've got mail!", "Answer the phone!", "Hold the line!"]),
 ("Where the recouplings and dumpings happen", "Firepit", ["Hot tub", "Kitchen", "Gym"]),
 ("Leaving the island against your will", "Dumped", ["Pardoned", "Crowned", "Married"]),
 ("The host since 2023", "Maya Jama", ["Caroline Flack", "Laura Whitmore", "Holly Willoughby"]),
 ("The Scottish comedian who narrates", "Iain Stirling", ["Kevin Bridges", "Frankie Boyle", "Limmy"]),
 ("The Spanish island the villa is on", "Mallorca", ["Ibiza", "Tenerife", "Lanzarote"]),
 ("When Islanders watch clips of each other's antics", "Movie night", ["Date night", "Fright night", "Quiz night"]),
 ("The private room for a couple", "Hideaway", ["Hideout", "Getaway", "Takeaway"]),
 ("Someone who ticks every box you'd look for", "My type on paper", ["My other half", "On the same page", "Paper tiger"]),
 ("Fancying someone new", "Head turned", ["Head over heels", "Heads up", "Head start"]),
 ("Getting closer to someone", "Cracking on", ["Cracking up", "Crackers", "Crack of dawn"]),
 ("Turned down or rejected", "Pied", ["Pie-eyed", "Pip", "Pied Piper"]),
 ("The prize the winning couple share", "£50,000", ["£10,000", "£100,000", "£1 million"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-200.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
