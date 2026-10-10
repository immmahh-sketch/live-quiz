# Bank session 10 Oct 2026: 4 more general races -> bank/race-22.json. 20 rows each, target 10; wrong options are
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

race("name the famous robot", "Film and TV", "medium", ["robots", "characters"], [
 ("The beeping astromech droid", "R2-D2", ["R5-D4", "Chopper", "D-O"]), ("The fussy golden protocol droid", "C-3PO", ["K-2SO", "L3-37", "IG-88"]),
 ("The rubbish-compacting robot left on Earth", "WALL-E", ["M-O", "AUTO", "BURN-E"]), ("WALL-E's sleek white robot love", "EVE", ["AUTO", "M-O", "GO-4"]),
 ("The Doctor's robot dog", "K9", ["Gizmo", "Bleep", "Kamelion"]), ("The paranoid android", "Marvin", ["Eddie", "Deep Thought", "Zaphod"]),
 ("Forbidden Planet's robot", "Robby the Robot", ["Gort", "Robot B-9", "Huey"]), ("Star Trek's android officer", "Data", ["Lore", "Worf", "Spock"]),
 ("Futurama's beer-swilling robot", "Bender", ["Calculon", "Roberto", "Hedonismbot"]), ("The Autobots' leader", "Optimus Prime", ["Megatron", "Bumblebee", "Starscream"]),
 ("Big Hero 6's inflatable healthcare robot", "Baymax", ["Hiro", "Fred", "Wasabi"]), ("The metal giant who befriends Hogarth", "The Iron Giant", ["Gort", "Robot B-9", "Talos"]),
 ("The robot who comes 'alive' in Short Circuit", "Johnny 5", ["Robot B-9", "Gort", "Chappie"]), ("2001's murderous computer", "HAL 9000", ["Skynet", "Deep Thought", "Mother"]),
 ("Red Dwarf's mechanoid", "Kryten", ["Holly", "Talkie Toaster", "Hudzen 10"]), ("The 1980s TV robot who said 'Boogie boogie!'", "Metal Mickey", ["Sir Killalot", "Matilda", "Sgt. Bash"]),
 ("Buck Rogers' 'bidi-bidi-bidi' robot", "Twiki", ["Dr. Theopolis", "Robot B-9", "Huey"]), ("The Jetsons' robot maid", "Rosie", ["Astro", "Elroy", "Judy"]),
 ("The rolling orange-and-white droid", "BB-8", ["R5-D4", "Chopper", "D-O"]), ("Will Smith's robot ally in I, Robot", "Sonny", ["VIKI", "NS-4", "Ava"])])

race("who lived here?", "History", "hard", ["houses", "famous people"], [
 ("Chartwell", "Winston Churchill", ["Clement Attlee", "Neville Chamberlain", "Anthony Eden"]), ("Down House", "Charles Darwin", ["Isaac Newton", "Alfred Russel Wallace", "Thomas Huxley"]),
 ("Hill Top", "Beatrix Potter", ["Enid Blyton", "Alison Uttley", "Kenneth Grahame"]), ("Dove Cottage", "William Wordsworth", ["Samuel Taylor Coleridge", "Robert Southey", "John Keats"]),
 ("Haworth Parsonage", "The Brontës", ["Jane Austen", "George Eliot", "Elizabeth Gaskell"]), ("Max Gate", "Thomas Hardy", ["D. H. Lawrence", "George Eliot", "John Fowles"]),
 ("Monk's House", "Virginia Woolf", ["Vanessa Bell", "Vita Sackville-West", "E. M. Forster"]), ("Abbotsford", "Walter Scott", ["Robert Burns", "Robert Louis Stevenson", "James Hogg"]),
 ("Bateman's", "Rudyard Kipling", ["H. G. Wells", "Arthur Conan Doyle", "J. M. Barrie"]), ("Cragside", "Lord Armstrong", ["George Stephenson", "Charles Parsons", "Joseph Swan"]),
 ("Gad's Hill Place", "Charles Dickens", ["William Thackeray", "Wilkie Collins", "Anthony Trollope"]), ("Strawberry Hill", "Horace Walpole", ["Alexander Pope", "Samuel Johnson", "William Beckford"]),
 ("Clouds Hill", "T. E. Lawrence", ["D. H. Lawrence", "Siegfried Sassoon", "Wilfred Owen"]), ("Greenway", "Agatha Christie", ["Dorothy L. Sayers", "Daphne du Maurier", "P. D. James"]),
 ("Mendips, Woolton", "John Lennon", ["Ringo Starr", "George Harrison", "Brian Epstein"]), ("20 Forthlin Road", "Paul McCartney", ["George Harrison", "Ringo Starr", "Gerry Marsden"]),
 ("Hughenden Manor", "Benjamin Disraeli", ["William Gladstone", "Lord Salisbury", "Robert Peel"]), ("Osborne House", "Queen Victoria", ["Edward VII", "George III", "William IV"]),
 ("Graceland", "Elvis Presley", ["Johnny Cash", "Jerry Lee Lewis", "Buddy Holly"]), ("Neverland Ranch", "Michael Jackson", ["Prince", "Lionel Richie", "Diana Ross"])])

race("where in Britain does this tradition happen?", "Britain", "hard", ["traditions", "places"], [
 ("The Hoppings fair on the Town Moor", "Newcastle", ["Sunderland", "Gateshead", "Durham"]), ("Goose Fair", "Nottingham", ["Derby", "Leicester", "Lincoln"]),
 ("Up Helly Aa, the Viking fire festival", "Lerwick", ["Stornoway", "Wick", "Thurso"]), ("Chasing a cheese down a hill", "Cooper's Hill, Gloucestershire", ["The Malvern Hills", "Box Hill", "Bredon Hill"]),
 ("Running with flaming tar barrels", "Ottery St Mary", ["Exeter", "Honiton", "Sidmouth"]), ("England's biggest Bonfire Night parades", "Lewes", ["Brighton", "Hastings", "Rye"]),
 ("The International Eisteddfod", "Llangollen", ["Bangor", "Aberystwyth", "Wrexham"]), ("The World Bog Snorkelling Championships", "Llanwrtyd Wells", ["Builth Wells", "Brecon", "Llandrindod Wells"]),
 ("The 'Obby 'Oss on May Day", "Padstow", ["Newquay", "St Ives", "Penzance"]), ("The Furry Dance", "Helston", ["Falmouth", "Truro", "Penzance"]),
 ("The Straw Bear festival", "Whittlesey", ["Peterborough", "Ely", "March"]), ("The World Gurning Championships", "Egremont", ["Whitehaven", "Workington", "Keswick"]),
 ("The Shrove Tuesday pancake race since 1445", "Olney", ["Bedford", "Buckingham", "Newport Pagnell"]), ("Royal Shrovetide Football", "Ashbourne", ["Bakewell", "Buxton", "Matlock"]),
 ("Hurling the Silver Ball", "St Columb", ["Newquay", "Bodmin", "Truro"]), ("Easter Monday bottle kicking", "Hallaton", ["Melton Mowbray", "Oakham", "Market Harborough"]),
 ("Well dressing, which began here in 1349", "Tissington", ["Chester", "Harrogate", "Bath"]), ("Glastonbury Festival (the actual farm)", "Pilton", ["Shepton Mallet", "Wells", "Frome"]),
 ("The Christmas and New Year Ba' game", "Kirkwall", ["Stornoway", "Wick", "Stromness"]), ("The Fringe every August", "Edinburgh", ["Glasgow", "Aberdeen", "Dundee"])])

race("what's the Welsh name for this place?", "Words and language", "hard", ["Welsh", "place names"], [
 ("Cardiff", "Caerdydd", ["Caerffili", "Caerllion", "Caerwys"]), ("Swansea", "Abertawe", ["Aberdaugleddau", "Abergele", "Aberdâr"]),
 ("Newport", "Casnewydd", ["Caerllion", "Casllwchwr", "Caerffili"]), ("Wrexham", "Wrecsam", ["Rhuthun", "Treffynnon", "Penarlâg"]),
 ("Carmarthen", "Caerfyrddin", ["Caerffili", "Caerllion", "Caerwys"]), ("Holyhead", "Caergybi", ["Caernarfon", "Cemaes", "Biwmares"]),
 ("Fishguard", "Abergwaun", ["Aberdaugleddau", "Abergele", "Aberdâr"]), ("Brecon", "Aberhonddu", ["Y Fenni", "Aberdâr", "Aberdaugleddau"]),
 ("Monmouth", "Trefynwy", ["Y Fenni", "Rhaglan", "Brynbuga"]), ("Cardigan", "Aberteifi", ["Aberdaugleddau", "Aberdâr", "Abergele"]),
 ("Bridgend", "Pen-y-bont ar Ogwr", ["Pontypridd", "Penarth", "Pen-y-groes"]), ("Snowdon", "Yr Wyddfa", ["Y Garn", "Tryfan", "Cadair Idris"]),
 ("Anglesey", "Ynys Môn", ["Ynys Enlli", "Ynys Gybi", "Ynys Dewi"]), ("Pembroke", "Penfro", ["Dinbych-y-pysgod", "Aberdaugleddau", "Arberth"]),
 ("Chepstow", "Cas-gwent", ["Brynbuga", "Rhaglan", "Y Fenni"]), ("Haverfordwest", "Hwlffordd", ["Arberth", "Aberdaugleddau", "Dinbych-y-pysgod"]),
 ("Neath", "Castell-nedd", ["Caerffili", "Pontypridd", "Castellnewydd Emlyn"]), ("Denbigh", "Dinbych", ["Dinbych-y-pysgod", "Rhuthun", "Treffynnon"]),
 ("Mold", "Yr Wyddgrug", ["Rhuthun", "Treffynnon", "Penarlâg"]), ("Welshpool", "Y Trallwng", ["Y Drenewydd", "Llanidloes", "Machynlleth"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-22.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
