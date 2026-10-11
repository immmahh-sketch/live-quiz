# Bank session 11 Oct 2026: 3 more general races -> bank/race-178.json (university, tattoo and spa words). 20 rows each, target 10; wrong options are
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

race("what's this university word?", "Education", "medium", ["university", "students", "words"], [
 ("A first-year student", "Fresher", ["Senior", "Veteran", "Prefect"]),
 ("Someone who's finished their degree", "Graduate", ["Undergraduate", "Apprentice", "Trainee"]),
 ("First-year student accommodation", "Halls", ["Barracks", "Hotels", "Wards"]),
 ("A talk given to a big room of students", "Lecture", ["Sermon", "Assembly", "Briefing"]),
 ("A small discussion group", "Seminar", ["Sermon", "Assembly", "Rally"]),
 ("A small session with your own tutor", "Tutorial", ["Sermon", "Assembly", "Rally"]),
 ("The long essay written in the final year", "Dissertation", ["Dissection", "Disinfection", "Distraction"]),
 ("The service you apply to university through", "UCAS", ["NHS", "DVLA", "HMRC"]),
 ("Borrowed money for fees, paid back later", "Student loan", ["Mortgage", "Overdraft", "Pay rise"]),
 ("The week of parties at the start of the year", "Freshers' Week", ["Rag Week", "Reading Week", "Holy Week"]),
 ("What graduates wear with a mortarboard", "Gown", ["Tutu", "Kilt", "Toga"]),
 ("The flat square graduation hat", "Mortarboard", ["Skateboard", "Clipboard", "Breadboard"]),
 ("The top degree grade", "First", ["Gold", "Ace", "Premier"]),
 ("Oxford and Cambridge together", "Oxbridge", ["Russell Group", "Ivy League", "Sorbonne"]),
 ("Victorian universities in big industrial cities, like Liverpool", "Redbrick", ["Plate glass", "Ivory tower", "Blue chip"]),
 ("The distance-learning university founded in 1969", "Open University", ["Night school", "Sixth form", "Grammar school"]),
 ("Former students", "Alumni", ["Aluminium", "Allotments", "Allies"]),
 ("The highest academic rank", "Professor", ["Lecturer", "Prefect", "Bursar"]),
 ("A year off before university", "Gap year", ["Leap year", "Light year", "Lean year"]),
 ("Students' ___: the bar and club building", "Union", ["League", "Lodge", "Senate"])])

race("what's this tattoo word?", "Art", "medium", ["tattoos", "body art", "words"], [
 ("Slang for tattoos", "Ink", ["Paint", "Dye", "Graffiti"]),
 ("The buzzing machine with needles", "Tattoo gun", ["Staple gun", "Glue gun", "Nail gun"]),
 ("Tattoos covering a whole arm", "Sleeve", ["Collar", "Cuff", "Glove"]),
 ("Ready-made designs on the parlour wall", "Flash", ["Bang", "Crash", "Spark"]),
 ("The shop where you get tattooed", "Parlour", ["Salon", "Surgery", "Boutique"]),
 ("Temporary brown body art from a plant dye", "Henna", ["Hemp", "Hessian", "Heather"]),
 ("Getting rid of an unwanted tattoo", "Laser removal", ["Hair removal", "Stain removal", "Snow removal"]),
 ("The outline transferred onto the skin first", "Stencil", ["Stapler", "Pencil", "Tinsel"]),
 ("Wrapped over a fresh tattoo", "Cling film", ["Tin foil", "Bubble wrap", "Greaseproof paper"]),
 ("The classic sailor's tattoo", "Anchor", ["Ladder", "Kettle", "Clock"]),
 ("The legendary American tattooist of old-school designs", "Sailor Jerry", ["Sailor Moon", "Popeye", "Captain Birdseye"]),
 ("Bold lines and bright colours, the traditional style", "Old school", ["Old hat", "Old money", "Old flame"]),
 ("Thick black swirling patterns", "Tribal", ["Paisley", "Tartan", "Gingham"]),
 ("The Māori facial tattoo", "Tā moko", ["Haka", "Hula", "Kava"]),
 ("The region 'tattoo' comes from, via Tahiti", "Polynesia", ["Scandinavia", "Siberia", "Patagonia"]),
 ("Edinburgh's display of massed bands, not body art", "Military tattoo", ["Highland Games", "Changing of the Guard", "Trooping the Colour"]),
 ("Looking after the healing skin", "Aftercare", ["Childcare", "Healthcare", "Daycare"]),
 ("Redoing a faded patch", "Touch-up", ["Pick-up", "Catch-up", "Make-up"]),
 ("A sideways figure of eight", "Infinity symbol", ["Pi sign", "Hashtag", "Ampersand"]),
 ("The bird sailors got inked for every 5,000 miles at sea", "Swallow", ["Robin", "Sparrow", "Wren"])])

race("what's this spa word?", "Everyday life", "easy", ["spas", "pampering", "words"], [
 ("A hot wooden room of dry heat", "Sauna", ["Igloo", "Larder", "Cellar"]),
 ("A misty room of wet heat", "Steam room", ["Igloo", "Larder", "Darkroom"]),
 ("The bubbling hot tub", "Jacuzzi", ["Paddling pool", "Birdbath", "Water butt"]),
 ("Kneading your aching muscles", "Massage", ["Message", "Mileage", "Mirage"]),
 ("A treatment cleaning and moisturising your face", "Facial", ["Facelift", "Facepalm", "Face-off"]),
 ("A treatment for the hands and nails", "Manicure", ["Manifesto", "Manacle", "Mandolin"]),
 ("A treatment for the feet", "Pedicure", ["Pedigree", "Pedalo", "Pedestal"]),
 ("The fluffy dressing gown they hand out", "Robe", ["Tabard", "Poncho", "Cagoule"]),
 ("Slices placed over the eyes", "Cucumber", ["Courgette", "Gherkin", "Celery"]),
 ("Coating the body in mineral clay", "Mud wrap", ["Mudslide", "Mudflat", "Mud pie"]),
 ("Warm smooth pebbles placed on the back", "Hot stones", ["Hot cross buns", "Hot potatoes", "Hot coals"]),
 ("An ice-cold dip after the sauna", "Plunge pool", ["Rock pool", "Car pool", "Typing pool"]),
 ("A treatment using scented oils", "Aromatherapy", ["Hydrotherapy", "Physiotherapy", "Hypnotherapy"]),
 ("Pressing points on the feet linked to the rest of the body", "Reflexology", ["Chiropody", "Podiatry", "Osteopathy"]),
 ("The Roman spa city in Somerset", "Bath", ["Cheltenham", "Leamington", "Harrogate"]),
 ("Cleansing the body of toxins", "Detox", ["Botox", "Decoy", "Deluxe"]),
 ("What you shuffle about in", "Slippers", ["Flippers", "Clippers", "Kippers"]),
 ("The quiet lounge for lying about after treatments", "Relaxation room", ["Waiting room", "Boardroom", "Panic room"]),
 ("A ticket for using the spa just for the day", "Day pass", ["Boarding pass", "Bus pass", "Free pass"]),
 ("The word comes from this Belgian town famous for its springs", "Spa", ["Vichy", "Evian", "Perrier"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-178.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
