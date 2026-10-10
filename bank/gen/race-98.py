# Bank session 10 Oct 2026: 2 more general races -> bank/race-98.json (Mr Men, long-distance walks). 20 rows each, target 10; wrong options are
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

race("which Mr Men or Little Miss character is this?", "Children's books", "medium", ["Mr Men", "Little Miss", "children's books"], [
 ("Orange, with extraordinarily long arms he uses to tickle people", "Mr Tickle", ["Mr Nosey", "Mr Busy", "Mr Tall"]),
 ("Round and pink, and eats so much he grows enormous", "Mr Greedy", ["Mr Jelly", "Mr Bounce", "Mr Fussy"]),
 ("Round and yellow with a huge smile, living in Happyland", "Mr Happy", ["Mr Cheerful", "Mr Funny", "Mr Daydream"]),
 ("Blue, wrapped in bandages, always having accidents", "Mr Bump", ["Mr Clumsy", "Mr Dizzy", "Mr Muddle"]),
 ("Red, the strongest person in the world, thanks to eating eggs", "Mr Strong", ["Mr Impossible", "Mr Tall", "Mr Bounce"]),
 ("Covered in pink scribble until two neat brothers clean him up", "Mr Messy", ["Mr Muddle", "Mr Nonsense", "Mr Fussy"]),
 ("Scowls at everyone and tears pages out of books", "Mr Grumpy", ["Mr Mean", "Mr Worry", "Mr Fussy"]),
 ("Lives in Coldland and can't stop going 'Atishoo!'", "Mr Sneeze", ["Mr Snow", "Mr Dizzy", "Mr Worry"]),
 ("Tiny orange chap who once lived under a daisy", "Mr Small", ["Mr Quiet", "Mr Jelly", "Little Miss Shy"]),
 ("Red, with a voice so loud it frightens the birds", "Mr Noisy", ["Mr Rush", "Mr Funny", "Mr Nonsense"]),
 ("Wins Nonsenseland's prize for the silliest thing", "Mr Silly", ["Mr Funny", "Mr Mischief", "Mr Daydream"]),
 ("Does everything upside down, even walking on his hands", "Mr Topsy-Turvy", ["Mr Dizzy", "Mr Bounce", "Mr Rush"]),
 ("Lives in Sleepyland and can't be bothered to do anything", "Mr Lazy", ["Mr Slow", "Mr Daydream", "Mr Quiet"]),
 ("Can't remember a thing, not even the message he was given", "Mr Forgetful", ["Mr Muddle", "Mr Daydream", "Mr Dizzy"]),
 ("Rich and rude to everyone until a goblin teaches him manners", "Mr Uppity", ["Mr Mean", "Mr Fussy", "Mr Clever"]),
 ("Yellow with pigtails, always cheerful", "Little Miss Sunshine", ["Little Miss Giggles", "Little Miss Helpful", "Little Miss Splendid"]),
 ("Plays tricks on everyone until Mr Impossible teaches her a lesson", "Little Miss Naughty", ["Little Miss Trouble", "Little Miss Contrary", "Little Miss Ditzy"]),
 ("Orders everybody about", "Little Miss Bossy", ["Little Miss Splendid", "Little Miss Princess", "Little Miss Contrary"]),
 ("Simply never stops talking", "Little Miss Chatterbox", ["Little Miss Giggles", "Little Miss Late", "Little Miss Ditzy"]),
 ("Muddle-headed, gets everything mixed up", "Little Miss Scatterbrain", ["Little Miss Late", "Little Miss Somersault", "Little Miss Shy"])])

race("which long-distance walk is this?", "Britain", "hard", ["walking", "trails", "outdoors"], [
 ("Edale to Kirk Yetholm, along the backbone of England", "Pennine Way", ["Pennine Bridleway", "Dales Way", "Teesdale Way"]),
 ("Wallsend to Bowness-on-Solway, following the Romans", "Hadrian's Wall Path", ["Cumbria Way", "Dales Way", "Teesdale Way"]),
 ("St Bees to Robin Hood's Bay, devised by Alfred Wainwright", "Coast to Coast", ["Cumbria Way", "Dales Way", "Teesdale Way"]),
 ("Helmsley round the North York Moors and down the coast to Filey", "Cleveland Way", ["Dales Way", "Teesdale Way", "Esk Valley Walk"]),
 ("Milngavie to Fort William", "West Highland Way", ["Rob Roy Way", "Speyside Way", "John o' Groats Trail"]),
 ("Minehead round to Poole Harbour: England's longest", "South West Coast Path", ["Two Moors Way", "Saints' Way", "Macmillan Way"]),
 ("Prestatyn to Chepstow, along the England-Wales border", "Offa's Dyke Path", ["Wye Valley Walk", "Glyndŵr's Way", "Cambrian Way"]),
 ("St Dogmaels to Amroth, round Wales's far south-west", "Pembrokeshire Coast Path", ["Wye Valley Walk", "Glyndŵr's Way", "Cambrian Way"]),
 ("From the river's source in Gloucestershire to the Thames Barrier", "Thames Path", ["London Loop", "Capital Ring", "Grand Union Canal Walk"]),
 ("Winchester to Eastbourne over the chalk hills", "South Downs Way", ["North Downs Way", "Wealdway", "Greensand Way"]),
 ("Chipping Campden to Bath", "Cotswold Way", ["Heart of England Way", "Macmillan Way", "Monarch's Way"]),
 ("'Britain's oldest road', from near Avebury to Ivinghoe Beacon", "The Ridgeway", ["Icknield Way", "Wessex Ridgeway", "Greensand Way"]),
 ("Melrose Abbey to Holy Island, named after a Northumbrian saint", "St Cuthbert's Way", ["St Oswald's Way", "Borders Abbeys Way", "Northumberland Coast Path"]),
 ("Pilgrims' route across northern Spain to a cathedral city", "Camino de Santiago", ["Via Francigena", "St Olav's Way", "Kungsleden"]),
 ("Georgia to Maine along the eastern US mountains", "Appalachian Trail", ["Pacific Crest Trail", "Continental Divide Trail", "John Muir Trail"]),
 ("Ancient stone path up to Machu Picchu", "Inca Trail", ["Salkantay Trek", "Lares Trek", "W Trek"]),
 ("Fort William to Inverness, along Loch Ness", "Great Glen Way", ["Rob Roy Way", "Speyside Way", "John o' Groats Trail"]),
 ("Corsica's notoriously tough north-south mountain trek", "GR20", ["Haute Route", "Kungsleden", "Alta Via 1"]),
 ("A loop round western Europe's highest peak, through France, Italy and Switzerland", "Tour du Mont Blanc", ["Haute Route", "Alta Via 1", "Eiger Trail"]),
 ("Forty miles across the North York Moors in under 24 hours, Osmotherley to Ravenscar", "Lyke Wake Walk", ["Esk Valley Walk", "Dales Way", "White Rose Way"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-98.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
