# Bank session 10 Oct 2026: 4 more general races -> bank/race-30.json. 20 rows each, target 10; wrong options are
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

race("which part of the body is inflamed?", "Science and nature", "hard", ["the body", "medicine", "-itis"], [
 ("Hepatitis", "Liver", ["Spleen", "Pancreas", "Gallbladder"]), ("Nephritis", "Kidneys", ["Spleen", "Adrenal glands", "Lymph nodes"]),
 ("Gingivitis", "Gums", ["Teeth", "Lips", "Tonsils"]), ("Conjunctivitis", "Eyes", ["Sinuses", "Tonsils", "Lips"]),
 ("Otitis", "Ears", ["Sinuses", "Tonsils", "Teeth"]), ("Gastritis", "Stomach", ["Small intestine", "Gallbladder", "Pancreas"]),
 ("Colitis", "Colon", ["Small intestine", "Appendix", "Spleen"]), ("Bronchitis", "Airways of the lungs", ["Ribs", "Diaphragm", "Thyroid"]),
 ("Laryngitis", "Voice box", ["Tonsils", "Thyroid", "Windpipe"]), ("Rhinitis", "Nose", ["Tonsils", "Throat", "Lips"]),
 ("Dermatitis", "Skin", ["Hair", "Nails", "Sweat glands"]), ("Arthritis", "Joints", ["Arteries", "Tendons", "Ligaments"]),
 ("Mastitis", "Breast", ["Thyroid", "Lymph nodes", "Ovaries"]), ("Cystitis", "Bladder", ["Ovaries", "Prostate", "Appendix"]),
 ("Encephalitis", "Brain", ["Spinal cord", "Thyroid", "Lymph nodes"]), ("Carditis", "Heart", ["Arteries", "Lungs", "Diaphragm"]),
 ("Phlebitis", "Veins", ["Arteries", "Nerves", "Lymph nodes"]), ("Osteitis", "Bones", ["Tendons", "Ligaments", "Cartilage"]),
 ("Myositis", "Muscles", ["Tendons", "Nerves", "Cartilage"]), ("Glossitis", "Tongue", ["Lips", "Teeth", "Tonsils"])])

race("which country is this company from?", "Business", "medium", ["companies", "brands", "countries"], [
 ("IKEA", "Sweden", ["Norway", "Iceland", "Estonia"]), ("Nokia", "Finland", ["Norway", "Estonia", "Iceland"]),
 ("Samsung", "South Korea", ["Vietnam", "Singapore", "Thailand"]), ("Lego", "Denmark", ["Norway", "Belgium", "Iceland"]),
 ("Nestlé", "Switzerland", ["Belgium", "Luxembourg", "Czechia"]), ("Philips", "the Netherlands", ["Belgium", "Luxembourg", "Norway"]),
 ("Zara", "Spain", ["Portugal", "Argentina", "Greece"]), ("Siemens", "Germany", ["Czechia", "Luxembourg", "Poland"]),
 ("Sony", "Japan", ["Singapore", "Thailand", "Vietnam"]), ("Huawei", "China", ["Singapore", "Vietnam", "Malaysia"]),
 ("Tata", "India", ["Pakistan", "Singapore", "Malaysia"]), ("Benetton", "Italy", ["Greece", "Portugal", "Belgium"]),
 ("L'Oréal", "France", ["Belgium", "Luxembourg", "Portugal"]), ("Red Bull", "Austria", ["Czechia", "Poland", "Hungary"]),
 ("Bombardier", "Canada", ["the USA", "New Zealand", "Norway"]), ("Havaianas", "Brazil", ["Portugal", "Argentina", "Colombia"]),
 ("Billabong", "Australia", ["New Zealand", "South Africa", "the USA"]), ("Acer", "Taiwan", ["Singapore", "Malaysia", "Vietnam"]),
 ("Kerrygold", "Ireland", ["Iceland", "New Zealand", "Norway"]), ("Bimbo, the baker", "Mexico", ["Argentina", "Colombia", "Chile"])])

race("which mountain range is this peak in?", "World geography", "hard", ["mountains", "peaks"], [
 ("Everest", "Himalayas", ["Pamirs", "Tian Shan", "Altai"]), ("Mont Blanc", "Alps", ["Dolomites", "Jura", "Vosges"]),
 ("Aconcagua", "Andes", ["Sierra Madre", "Cascades", "Brooks Range"]), ("Elbrus", "Caucasus", ["Zagros", "Altai", "Pamirs"]),
 ("Ben Nevis", "Grampians", ["Cairngorms", "Cheviots", "Mourne Mountains"]), ("K2", "Karakoram", ["Pamirs", "Tian Shan", "Altai"]),
 ("Mount Whitney", "Sierra Nevada", ["Cascades", "Sierra Madre", "Ozarks"]), ("Pikes Peak", "Rocky Mountains", ["Cascades", "Ozarks", "Brooks Range"]),
 ("Mount Mitchell", "Appalachians", ["Ozarks", "Cascades", "Sierra Madre"]), ("Gerlachovský štít", "Tatras", ["Sudetes", "Ore Mountains", "Harz"]),
 ("Aneto", "Pyrenees", ["Jura", "Vosges", "Cantabrian Mountains"]), ("Toubkal", "Atlas", ["Drakensberg", "Ruwenzori", "Simien Mountains"]),
 ("Mount Kosciuszko", "Great Dividing Range", ["Kaikoura Ranges", "Flinders Ranges", "MacDonnell Ranges"]), ("Aoraki / Mount Cook", "Southern Alps", ["Kaikoura Ranges", "Flinders Ranges", "Blue Mountains"]),
 ("Pen y Fan", "Brecon Beacons", ["Cambrian Mountains", "Black Mountains", "Clwydian Range"]), ("Cross Fell", "Pennines", ["Cheviots", "Cambrian Mountains", "Cairngorms"]),
 ("Corno Grande", "Apennines", ["Dolomites", "Pindus", "Dinaric Alps"]), ("Moldoveanu", "Carpathians", ["Balkan Mountains", "Rila", "Dinaric Alps"]),
 ("Narodnaya", "Urals", ["Altai", "Tian Shan", "Zagros"]), ("Tirich Mir", "Hindu Kush", ["Zagros", "Pamirs", "Tian Shan"])])

race("what's the American word for this?", "Words and language", "easy", ["American English", "words"], [
 ("Pavement", "Sidewalk", ["Crosswalk", "Stoop", "Freeway"]), ("Lift", "Elevator", ["Dumbwaiter", "Stoop", "Escalator"]),
 ("Flat", "Apartment", ["Townhouse", "Ranch", "Cabin"]), ("Car boot", "Trunk", ["Fender", "Muffler", "Dashboard"]),
 ("Car bonnet", "Hood", ["Fender", "Muffler", "Hubcap"]), ("Petrol", "Gas", ["Kerosene", "Propane", "Gasket"]),
 ("Lorry", "Truck", ["Station wagon", "Minivan", "Trailer"]), ("Nappy", "Diaper", ["Onesie", "Bassinet", "Bib"]),
 ("Dummy", "Pacifier", ["Rattle", "Onesie", "Bassinet"]), ("Rubbish", "Trash", ["Dumpster", "Hamper", "Lint"]),
 ("Torch", "Flashlight", ["Flashbulb", "Lantern", "Nightlight"]), ("Postcode", "Zip code", ["Area code", "Mailbox", "Return address"]),
 ("Holiday", "Vacation", ["Furlough", "Sabbatical", "Weekend"]), ("Autumn", "Fall", ["Harvest", "Indian summer", "Thanksgiving"]),
 ("Jumper", "Sweater", ["Cardigan", "Hoodie", "Tank top"]), ("Waistcoat", "Vest", ["Suspenders", "Tank top", "Tuxedo"]),
 ("Tap", "Faucet", ["Plunger", "Drain", "Sink"]), ("Cot", "Crib", ["Bassinet", "Playpen", "Highchair"]),
 ("Pram or pushchair", "Stroller", ["Playpen", "Highchair", "Car seat"]), ("Windscreen", "Windshield", ["Dashboard", "Fender", "Hubcap"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-30.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
