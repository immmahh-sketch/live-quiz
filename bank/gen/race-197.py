# Bank session 11 Oct 2026: 3 more general races -> bank/race-197.json (first aid, Burns Night and Lake District words). 20 rows each, target 10; wrong options are
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

race("what's this first aid word?", "Science", "medium", ["first aid", "health", "words"], [
 ("A sticky dressing for a small cut", "Plaster", ["Poultice", "Compress", "Stencil"]),
 ("A strip of cloth wrapped round a wound", "Bandage", ["Bandana", "Banner", "Bangle"]),
 ("A triangular bandage cradling an injured arm", "Sling", ["Hammock", "Lasso", "Garter"]),
 ("Chest compressions and rescue breaths, by its letters", "CPR", ["GPS", "CRB", "RSI"]),
 ("Lying an unconscious person safely on their side", "Recovery position", ["Lotus position", "Starting position", "Pole position"]),
 ("The machine that shocks the heart back into rhythm", "Defibrillator", ["Dehumidifier", "Pacemaker", "Ventilator"]),
 ("A rigid support strapped to a broken limb", "Splint", ["Splinter", "Sprint", "Spline"]),
 ("A band tightened above a severe bleed", "Tourniquet", ["Turnkey", "Tournament", "Turban"]),
 ("Abdominal thrusts for someone who's choking", "Heimlich manoeuvre", ["Pincer movement", "Three-point turn", "Hokey-cokey"]),
 ("The UK's emergency number", "999", ["101", "111", "123"]),
 ("An ambulance crew member trained in emergency care", "Paramedic", ["Paralegal", "Paratrooper", "Parasite"]),
 ("The first aid charity at football grounds and events", "St John Ambulance", ["St John's Wort", "St Andrews", "St Trinian's"]),
 ("Checked at the wrist or the neck", "Pulse", ["Pupil", "Pore", "Pitch"]),
 ("Pressed on a sprain to bring the swelling down", "Ice pack", ["Ice cube", "Six-pack", "Ice bucket"]),
 ("What you pull out a splinter with", "Tweezers", ["Pliers", "Clippers", "Scissors"]),
 ("What you cool a burn under for twenty minutes", "Cold running water", ["Butter", "Ice-cold milk", "Vinegar"]),
 ("A brain injury from a bang on the head", "Concussion", ["Percussion", "Conclusion", "Contusion"]),
 ("Kills the germs in a wound", "Antiseptic", ["Antacid", "Antihistamine", "Anaesthetic"]),
 ("The green box with a white cross on it", "First aid kit", ["Toolkit", "Kit Kat", "Sewing kit"]),
 ("Pale, clammy and faint after an injury: they may be in ...", "Shock", ["Awe", "Denial", "Trouble"])])

race("what's this Burns Night word?", "Scotland", "medium", ["Burns Night", "Scotland", "words"], [
 ("The 'great chieftain o' the puddin'-race'", "Haggis", ["Black pudding", "White pudding", "Scotch pie"]),
 ("The mashed swede served with it", "Neeps", ["Parsnips", "Kale", "Leeks"]),
 ("The mashed potatoes served with it", "Tatties", ["Chips", "Dumplings", "Oatcakes"]),
 ("The date of Burns Night", "25 January", ["30 November", "1 March", "31 December"]),
 ("The poem recited before cutting into the haggis", "Address to a Haggis", ["Ode to Joy", "Ode to a Nightingale", "To Autumn"]),
 ("The musician who plays the haggis in", "Piper", ["Drummer", "Fiddler", "Bugler"]),
 ("The small knife tucked into the sock", "Sgian-dubh", ["Claymore", "Dirk", "Cutlass"]),
 ("The short prayer said before the meal", "Selkirk Grace", ["Lord's Prayer", "Amazing Grace", "Grace Kelly"]),
 ("The main speech about Burns' life and work", "Immortal Memory", ["Eternal Sunshine", "Total Recall", "Memory Lane"]),
 ("The cheeky speech by a man about the women present", "Toast to the Lassies", ["Toast to the Bride", "Vote of thanks", "Best man's speech"]),
 ("The Burns song everyone sings at the end of the night", "Auld Lang Syne", ["Flower of Scotland", "Loch Lomond", "Scotland the Brave"]),
 ("Burns' birthplace in Ayrshire", "Alloway", ["Alloa", "Ayr", "Dumfries"]),
 ("His poem about a drunken farmer chased by witches", "Tam o' Shanter", ["Tam Lin", "Tom Thumb", "Tam Dalyell"]),
 ("The dram everyone toasts with", "Whisky", ["Gin", "Brandy", "Mead"]),
 ("Pudding of cream, raspberries, honey, oats and whisky", "Cranachan", ["Cranberry sauce", "Crannog", "Clafoutis"]),
 ("A Scottish dance party", "Ceilidh", ["Hootenanny", "Rave", "Disco"]),
 ("The tartan worn by the men", "Kilt", ["Sarong", "Kaftan", "Toga"]),
 ("Burns' nickname, from his farming roots", "Ploughman Poet", ["Bard of Avon", "Poet Laureate", "Lake Poet"]),
 ("Scotland's national poet", "Robert Burns", ["Walter Scott", "Robert Louis Stevenson", "Robert the Bruce"]),
 ("His poem with 'the best-laid schemes o' mice an' men'", "To a Mouse", ["The Mousetrap", "Of Mice and Men", "Three Blind Mice"])])

race("what's this Lake District word?", "UK geography", "medium", ["Lake District", "Cumbria", "words"], [
 ("The Lakeland word for a mountain or hill", "Fell", ["Moor", "Dale", "Tor"]),
 ("A small mountain lake", "Tarn", ["Loch", "Lough", "Llyn"]),
 ("A Lakeland stream", "Beck", ["Burn", "Bourne", "Wadi"]),
 ("The Lakeland word for a waterfall, as in Aira ...", "Force", ["Spout", "Linn", "Rapids"]),
 ("Loose stones on a steep slope", "Scree", ["Screed", "Shingle", "Gravel"]),
 ("The lake word in Buttermere and Thirlmere", "Mere", ["Mare", "Moor", "Marsh"]),
 ("A peaked summit, as in Scafell ...", "Pike", ["Tor", "Ben", "Knoll"]),
 ("The tough Lakeland breed of sheep", "Herdwick", ["Swaledale", "Cheviot", "Texel"]),
 ("The sugary energy bar taken up Everest", "Kendal Mint Cake", ["Eccles cake", "Mint Imperial", "Kendal Calling"]),
 ("The spicy treat from Sarah Nelson's shop", "Grasmere gingerbread", ["Parkin", "Bath bun", "Shortbread"]),
 ("The author who farmed at Hill Top", "Beatrix Potter", ["Enid Blyton", "Arthur Ransome", "Roald Dahl"]),
 ("The poet of 'I wandered lonely as a cloud'", "Wordsworth", ["Coleridge", "Southey", "Keats"]),
 ("His cottage home in Grasmere", "Dove Cottage", ["Hill Top", "Rose Cottage", "Brantwood"]),
 ("The fell climbed by Striding Edge", "Helvellyn", ["Skiddaw", "Blencathra", "Great Gable"]),
 ("Donald Campbell's boat that crashed on Coniston", "Bluebird", ["Bluebell", "Kingfisher", "Golden Hind"]),
 ("England's largest natural lake", "Windermere", ["Ullswater", "Derwentwater", "Coniston Water"]),
 ("The town with the Derwent Pencil Museum", "Keswick", ["Kendal", "Penrith", "Ambleside"]),
 ("A long, coiled banger", "Cumberland sausage", ["Lincolnshire sausage", "Saveloy", "Black pudding"]),
 ("One of England's steepest roads, with hairpin bends", "Hardknott Pass", ["Khyber Pass", "Boarding pass", "Bus pass"]),
 ("The fellwalker whose hand-drawn guides cover 214 fells", "Wainwright", ["Wainscot", "Wheelwright", "Shipwright"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-197.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
