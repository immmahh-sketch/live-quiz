# Bank session 11 Oct 2026: 3 more general races -> bank/race-181.json (Wild West, dinosaur and wine words). 20 rows each, target 10; wrong options are
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

race("what's this Wild West word?", "Film", "medium", ["Wild West", "westerns", "words"], [
 ("The elected lawman in charge of a county", "Sheriff", ["Mayor", "Judge", "Ranger"]),
 ("A ranch hand who herds cattle on horseback", "Cowboy", ["Prospector", "Trapper", "Blacksmith"]),
 ("A band of townsfolk sworn in to chase outlaws", "Posse", ["Gang", "Mob", "Troop"]),
 ("The bar with swinging doors", "Saloon", ["Diner", "Chapel", "Bank"]),
 ("A rope loop thrown to catch cattle", "Lasso", ["Bridle", "Stirrup", "Saddle"]),
 ("A leather holder for a gun on the hip", "Holster", ["Scabbard", "Quiver", "Satchel"]),
 ("A show of bronco riding and steer roping", "Rodeo", ["Regatta", "Gymkhana", "Jamboree"]),
 ("Spiked wheels on the heels of a cowboy's boots", "Spurs", ["Studs", "Cleats", "Buckles"]),
 ("A wanted criminal on the run", "Outlaw", ["Deputy", "Ranger", "Drifter"]),
 ("The 1849 scramble to California for gold", "Gold rush", ["Land grab", "Dust bowl", "Gold standard"]),
 ("Cattle bolting in a panic", "Stampede", ["Roundup", "Cattle drive", "Barn dance"]),
 ("A final face-off between two gunfighters", "Showdown", ["Hoedown", "Breakdown", "Lowdown"]),
 ("A big cattle farm", "Ranch", ["Croft", "Allotment", "Vineyard"]),
 ("The wide-brimmed cowboy hat", "Stetson", ["Bowler", "Trilby", "Beret"]),
 ("Leather leg coverings worn over trousers", "Chaps", ["Gaiters", "Spats", "Puttees"]),
 ("A horse-drawn coach carrying mail and passengers between towns", "Stagecoach", ["Hackney", "Charabanc", "Tram"]),
 ("The horseback mail relay of 1860 and 1861", "Pony Express", ["Royal Mail", "Penny Post", "Iron Horse"]),
 ("A deserted town left behind when the mine closed", "Ghost town", ["New town", "Market town", "Twin town"]),
 ("A wild horse of the American plains", "Mustang", ["Shire", "Clydesdale", "Shetland"]),
 ("The dried plant that rolls across the desert", "Tumbleweed", ["Bracken", "Thistledown", "Heather"])])

race("what's this dinosaur word?", "Science", "medium", ["dinosaurs", "fossils", "words"], [
 ("A scientist who studies fossils", "Palaeontologist", ["Archaeologist", "Geologist", "Anthropologist"]),
 ("The 'tyrant lizard king'", "Tyrannosaurus rex", ["Allosaurus", "Spinosaurus", "Megalosaurus"]),
 ("The three-horned plant-eater", "Triceratops", ["Pachycephalosaurus", "Iguanodon", "Oviraptor"]),
 ("Plates along its back and spikes on its tail", "Stegosaurus", ["Iguanodon", "Parasaurolophus", "Gallimimus"]),
 ("Armoured all over, with a club on its tail", "Ankylosaurus", ["Iguanodon", "Pachycephalosaurus", "Parasaurolophus"]),
 ("The long-necked giant nicknamed 'Dippy' at the Natural History Museum", "Diplodocus", ["Brachiosaurus", "Brontosaurus", "Argentinosaurus"]),
 ("The 'swift thief' made famous by Jurassic Park", "Velociraptor", ["Compsognathus", "Gallimimus", "Oviraptor"]),
 ("Flying reptiles that lived alongside dinosaurs", "Pterosaurs", ["Ichthyosaurs", "Mosasaurs", "Ammonites"]),
 ("The long-necked sea reptile often linked to Nessie", "Plesiosaur", ["Ichthyosaur", "Mosasaur", "Ammonite"]),
 ("The period that gave Jurassic Park its name", "Jurassic", ["Triassic", "Permian", "Devonian"]),
 ("The period at the end of which the dinosaurs died out", "Cretaceous", ["Triassic", "Carboniferous", "Cambrian"]),
 ("Dinosaur dung turned to stone", "Coprolite", ["Flint", "Jet", "Chalk"]),
 ("What most scientists think wiped out the dinosaurs", "Asteroid", ["Ice age", "Flood", "Plague"]),
 ("Fossilised tree resin that can trap insects", "Amber", ["Jet", "Coral", "Pearl"]),
 ("The famous fossil hunter of Lyme Regis", "Mary Anning", ["Mary Shelley", "Mary Seacole", "Mary Leakey"]),
 ("The stretch of Dorset and Devon shoreline famous for fossils", "Jurassic Coast", ["Heritage Coast", "Gold Coast", "Causeway Coast"]),
 ("The scientist who coined the word 'dinosaur'", "Richard Owen", ["Charles Darwin", "David Attenborough", "Thomas Huxley"]),
 ("What 'dinosaur' means", "Terrible lizard", ["Thunder lizard", "Giant lizard", "Ancient beast"]),
 ("The living animals descended from dinosaurs", "Birds", ["Crocodiles", "Lizards", "Snakes"]),
 ("A meat-eating dinosaur", "Carnivore", ["Herbivore", "Omnivore", "Insectivore"])])

race("what's this wine word?", "Food and drink", "medium", ["wine", "drinks", "words"], [
 ("The restaurant's wine expert", "Sommelier", ["Maître d'", "Barista", "Concierge"]),
 ("The smell of a wine", "Bouquet", ["Body", "Tannin", "Palate"]),
 ("The year the grapes were harvested", "Vintage", ["Varietal", "Reserve", "Cuvée"]),
 ("Spoiled, with a musty, damp-cardboard smell", "Corked", ["Mulled", "Chilled", "Aerated"]),
 ("Pink wine", "Rosé", ["Blanc", "Claret", "Tawny"]),
 ("The taste that lingers after you swallow", "Finish", ["Body", "Tannin", "Palate"]),
 ("A bottle holding two normal bottles' worth", "Magnum", ["Jeroboam", "Nebuchadnezzar", "Methuselah"]),
 ("Pouring wine into a jug to let it breathe", "Decanting", ["Fining", "Blending", "Pressing"]),
 ("The word for a wine that isn't sweet", "Dry", ["Rich", "Jammy", "Fruity"]),
 ("Fizzy", "Sparkling", ["Still", "Fortified", "Mulled"]),
 ("The study of wine", "Oenology", ["Ornithology", "Etymology", "Mycology"]),
 ("A wine estate in Bordeaux", "Château", ["Palazzo", "Schloss", "Manor"]),
 ("The grape used for Chablis", "Chardonnay", ["Merlot", "Shiraz", "Malbec"]),
 ("Spain's sparkling wine", "Cava", ["Crémant", "Sekt", "Asti"]),
 ("Italy's best-selling sparkling wine, from the Veneto", "Prosecco", ["Rioja", "Chianti", "Retsina"]),
 ("The fortified wine from Portugal's Douro valley", "Port", ["Marsala", "Vermouth", "Brandy"]),
 ("The fortified wine from Jerez in Spain", "Sherry", ["Madeira", "Marsala", "Cognac"]),
 ("Where wine is kept to age, underground", "Cellar", ["Attic", "Larder", "Pantry"]),
 ("The streaks that run down the inside of the glass", "Legs", ["Arms", "Fingers", "Stripes"]),
 ("Grapes crushed by foot in a big vat", "Treading", ["Kneading", "Churning", "Threshing"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-181.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
