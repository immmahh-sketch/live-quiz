# Bank session 11 Oct 2026: 3 more general races -> bank/race-191.json (Chinese takeaway, Italian restaurant and chocolate words). 20 rows each, target 10; wrong options are
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

race("what's this Chinese takeaway word?", "Food and drink", "easy", ["Chinese food", "takeaway", "words"], [
 ("Fried noodles with meat and veg", "Chow mein", ["Chop suey", "Pad Thai", "Ramen"]),
 ("Battered pork in a bright red-orange sauce", "Sweet and sour", ["Jerk", "Tikka", "Teriyaki"]),
 ("Puffy crisps that swell in hot oil", "Prawn crackers", ["Poppadoms", "Pork scratchings", "Tortilla chips"]),
 ("Shredded duck rolled in thin pancakes with cucumber", "Crispy aromatic duck", ["Duck à l'orange", "Duck confit", "Duck pâté"]),
 ("The thick sweet sauce served with it", "Hoisin", ["Worcestershire", "Tabasco", "Teriyaki"]),
 ("Veg wrapped in pastry and deep-fried", "Spring roll", ["Sausage roll", "Swiss roll", "Bread roll"]),
 ("A crisp biscuit with a message inside", "Fortune cookie", ["Party popper", "Christmas cracker", "Jaffa Cake"]),
 ("Small steamed parcels in bamboo baskets", "Dim sum", ["Tapas", "Mezze", "Antipasti"]),
 ("Dumplings floating in soup", "Wonton", ["Gnocchi", "Croutons", "Noodles"]),
 ("Red, sticky Cantonese barbecue pork", "Char siu", ["Chorizo", "Pastrami", "Biltong"]),
 ("The spicy Chinese province famous for its peppercorns", "Sichuan", ["Shanghai", "Canton", "Beijing"]),
 ("Chips tossed with salt, chilli and onion, a North East favourite", "Salt and pepper chips", ["Cheesy chips", "Curry chips", "Chip butty"]),
 ("The round steel pan for stir-frying", "Wok", ["Paella pan", "Skillet", "Tagine"]),
 ("Pork ribs in a sticky glaze", "Spare ribs", ["Rack of lamb", "Ribeye", "Chops"]),
 ("Rice fried with scrambled egg", "Egg fried rice", ["Pilau rice", "Risotto", "Paella"]),
 ("A set meal for several people", "Banquet", ["Buffet", "Platter", "Picnic"]),
 ("A fluffy egg dish with fillings", "Foo yung", ["Frittata", "Crêpe", "Soufflé"]),
 ("Peanut sauce on skewers", "Satay", ["Pesto", "Tahini", "Hummus"]),
 ("Salted fermented beans made into a sauce", "Black bean", ["Baked bean", "Kidney bean", "Coffee bean"]),
 ("The two sticks you eat with", "Chopsticks", ["Drumsticks", "Cocktail sticks", "Matchsticks"])])

race("what's this Italian restaurant word?", "Food and drink", "medium", ["Italian food", "restaurants", "words"], [
 ("The starters", "Antipasti", ["Tapas", "Mezze", "Hors d'oeuvres"]),
 ("Toasted bread topped with tomato and garlic", "Bruschetta", ["Crostata", "Ciabatta", "Brioche"]),
 ("Pasta in egg, cheese and pancetta", "Carbonara", ["Primavera", "Marinara", "Alfredo"]),
 ("Pasta in a fiery tomato sauce", "Arrabbiata", ["Primavera", "Alfredo", "Vongole"]),
 ("The pizza with just tomato, mozzarella and basil", "Margherita", ["Marinara", "Fiorentina", "Quattro stagioni"]),
 ("A pizza folded over into a half-moon", "Calzone", ["Panzanella", "Cannelloni", "Crostini"]),
 ("Coffee-soaked sponge layered with mascarpone", "Tiramisu", ["Zabaglione", "Cassata", "Semifreddo"]),
 ("A set, wobbly cream pudding", "Panna cotta", ["Crème brûlée", "Blancmange", "Trifle"]),
 ("Italian ice cream", "Gelato", ["Granita", "Kulfi", "Frozen yogurt"]),
 ("Pasta cooked 'to the tooth'", "Al dente", ["Al fresco", "Al forno", "À la carte"]),
 ("Creamy rice stirred with hot stock", "Risotto", ["Paella", "Pilaf", "Congee"]),
 ("Basil, pine nuts and Parmesan sauce", "Pesto", ["Salsa verde", "Tapenade", "Gremolata"]),
 ("Lemon liqueur served ice-cold after dinner", "Limoncello", ["Amaretto", "Sambuca", "Grappa"]),
 ("Espresso poured over a scoop of ice cream", "Affogato", ["Macchiato", "Cortado", "Frappé"]),
 ("Dry-cured ham served in wafer-thin slices", "Prosciutto", ["Pancetta", "Salami", "Mortadella"]),
 ("Flat, oily bread topped with rosemary", "Focaccia", ["Ciabatta", "Naan", "Pitta"]),
 ("A simple, family-run Italian eatery", "Trattoria", ["Bodega", "Brasserie", "Taverna"]),
 ("Pasta parcels with a filling", "Ravioli", ["Penne", "Fusilli", "Rigatoni"]),
 ("Layers of pasta, ragù and béchamel", "Lasagne", ["Cannelloni", "Moussaka", "Gratin"]),
 ("What the waiter says as your food arrives", "Buon appetito", ["Buongiorno", "Arrivederci", "Mamma mia"])])

race("what's this chocolate word?", "Food and drink", "medium", ["chocolate", "sweets", "words"], [
 ("The bean chocolate is made from", "Cocoa bean", ["Coffee bean", "Vanilla pod", "Carob"]),
 ("Chocolate melted into cream, for filling and icing", "Ganache", ["Gnocchi", "Garnish", "Galette"]),
 ("A filling of caramelised sugar and ground nuts", "Praline", ["Marzipan", "Nougat", "Fondant"]),
 ("A cocoa-dusted round chocolate named after a fungus", "Truffle", ["Morel", "Chanterelle", "Button"]),
 ("Heating and cooling chocolate so it snaps and shines", "Tempering", ["Tampering", "Tempting", "Tumbling"]),
 ("The whitish film on old chocolate", "Bloom", ["Blush", "Mould", "Frost"]),
 ("Chocolate with no cocoa solids at all", "White chocolate", ["Milk chocolate", "Dark chocolate", "Ruby chocolate"]),
 ("The fat pressed out of the beans", "Cocoa butter", ["Peanut butter", "Shea butter", "Ghee"]),
 ("Cadbury's model village near Birmingham", "Bournville", ["Port Sunlight", "Saltaire", "New Earswick"]),
 ("The York firm that first made the KitKat", "Rowntree's", ["Fry's", "Thorntons", "Mackintosh's"]),
 ("The York firm behind the Chocolate Orange", "Terry's", ["Fry's", "Thorntons", "Galaxy"]),
 ("Someone who makes fine chocolates", "Chocolatier", ["Sommelier", "Barista", "Couturier"]),
 ("The ancient people who drank chocolate and called it 'xocolatl'", "Aztecs", ["Incas", "Romans", "Vikings"]),
 ("The cocoa tree's Latin name, meaning 'food of the gods'", "Theobroma", ["Ambrosia", "Nectar", "Manna"]),
 ("A rich, fudgy chocolate cake cut into squares", "Brownie", ["Blondie", "Flapjack", "Rocky road"]),
 ("The Christmas tin of wrapped sweets with the purple one", "Quality Street", ["Roses", "Heroes", "Celebrations"]),
 ("Windows opened each day in December", "Advent calendar", ["Christmas card", "Stocking", "Cracker"]),
 ("Small crunchy bits of crushed cocoa bean", "Cocoa nibs", ["Hundreds and thousands", "Sprinkles", "Coco Pops"]),
 ("A light, airy chocolate dessert", "Mousse", ["Moose", "Mouse", "Mess"]),
 ("A mug of it with marshmallows on top", "Hot chocolate", ["Horlicks", "Bovril", "Cappuccino"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-191.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
