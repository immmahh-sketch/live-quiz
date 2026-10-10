# Bank session 10 Oct 2026: 16 more Categorise questions -> bank/sort-2.json. Two groups, four items each (three for the
# colours). Each pair of categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Science", ["rocks"], "medium", "Igneous rock or sedimentary rock?", "Igneous", "Sedimentary", ["Granite", "Basalt", "Pumice", "Obsidian"], ["Sandstone", "Limestone", "Chalk", "Shale"])
s("Food and drink", ["vegetables"], "easy", "Grows above the ground or below it?", "Above ground", "Below ground", ["Broccoli", "Peas", "Cabbage", "Sweetcorn"], ["Potato", "Carrot", "Beetroot", "Parsnip"])
s("World geography", ["roads"], "medium", "Do they drive on the left or the right?", "Left", "Right", ["Japan", "Australia", "India", "Ireland"], ["France", "USA", "Spain", "Brazil"])
s("Nature", ["pets"], "easy", "Dog breed or cat breed?", "Dog", "Cat", ["Beagle", "Dachshund", "Whippet", "Weimaraner"], ["Persian", "Siamese", "Maine Coon", "Bengal"])
s("Sport", ["balls"], "easy", "Played with a round ball or an oval ball?", "Round ball", "Oval ball", ["Football", "Basketball", "Netball", "Volleyball"], ["Rugby union", "Rugby league", "American football", "Aussie rules"])
s("Nature", ["animals"], "easy", "Found wild in Australia or in Africa?", "Australia", "Africa", ["Kangaroo", "Koala", "Wombat", "Platypus"], ["Zebra", "Giraffe", "Hippopotamus", "Meerkat"])
s("World geography", ["countries", "size"], "medium", "A bigger country than the UK, or a smaller one (by area)?", "Bigger", "Smaller", ["France", "Spain", "Germany", "Japan"], ["Ireland", "Belgium", "Netherlands", "Portugal"])
s("Words and language", ["word origins"], "hard", "A word from Hindi/Urdu or from Arabic?", "Hindi/Urdu", "Arabic", ["Shampoo", "Bungalow", "Jungle", "Pyjamas"], ["Algebra", "Sofa", "Coffee", "Alcohol"])
s("Sport", ["equipment"], "medium", "Played with a racket or a bat?", "Racket", "Bat", ["Tennis", "Badminton", "Squash", "Racquetball"], ["Cricket", "Baseball", "Rounders", "Table tennis"])
s("Film", ["Disney", "Pixar"], "easy", "From 'Finding Nemo' or 'The Little Mermaid'?", "Finding Nemo", "The Little Mermaid", ["Nemo", "Dory", "Marlin", "Bruce"], ["Ariel", "Sebastian", "Flounder", "Ursula"])
s("Nature", ["farm animals"], "medium", "A breed of sheep or a breed of cattle?", "Sheep", "Cattle", ["Texel", "Suffolk", "Jacob", "Herdwick"], ["Hereford", "Aberdeen Angus", "Highland", "Jersey"])
s("Food and drink", ["drinks"], "medium", "Made from grapes or from grain?", "Grapes", "Grain", ["Brandy", "Port", "Champagne", "Sherry"], ["Whisky", "Beer", "Sake", "Bourbon"])
s("TV", ["sci-fi"], "easy", "A Doctor Who monster or a Star Trek alien race?", "Doctor Who", "Star Trek", ["Daleks", "Cybermen", "Sontarans", "Weeping Angels"], ["Klingons", "Vulcans", "Romulans", "The Borg"])
s("Food and drink", ["cooking"], "easy", "A spice or a herb?", "Spice", "Herb", ["Cinnamon", "Nutmeg", "Cumin", "Paprika"], ["Basil", "Parsley", "Thyme", "Rosemary"])
s("Art", ["colours"], "easy", "A primary colour or a secondary colour, in paint?", "Primary", "Secondary", ["Red", "Blue", "Yellow"], ["Green", "Orange", "Purple"])
s("London", ["transport"], "easy", "A London Tube line or a London mainline station?", "Tube line", "Mainline station", ["Bakerloo", "Jubilee", "Northern", "Metropolitan"], ["Paddington", "Euston", "King's Cross", "Marylebone"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
