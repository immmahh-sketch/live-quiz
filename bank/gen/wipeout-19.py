# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-19.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you put 'hand' in front", "Words and language", "easy", ["wordplay", "compound words"],
 ["Bag", "Book", "Cuff", "Shake", "Writing", "Rail", "Stand", "Brake", "Ball", "Made", "Out", "Set", "Some", "Kerchief", "Gun"],
 ["Glove", "Nail", "Wrist", "Finger", "Ring"])
board("Words that make a new word when you put 'eye' in front", "Words and language", "easy", ["wordplay", "compound words"],
 ["Ball", "Brow", "Lash", "Lid", "Liner", "Sight", "Sore", "Witness", "Glass", "Shadow", "Piece", "Opener", "Wash", "Tooth", "Drop"],
 ["Nose", "Lens", "Tear", "Cheek", "Blink"])
board("Words that make a new word when you add 'berry' to the end", "Words and language", "medium", ["wordplay", "fruit"],
 ["Straw", "Blue", "Rasp", "Black", "Goose", "Cran", "Elder", "Mul", "Logan", "Huckle", "Bil", "Cloud", "Boysen", "Dew", "Bar"],
 ["Grape", "Cherry", "Lemon", "Plum", "Apple"])
board("Words that make a new word when you put 'moon' in front", "Words and language", "medium", ["wordplay", "compound words"],
 ["Light", "Beam", "Walk", "Shine", "Stone", "Struck", "Lit", "Rise", "Shot", "Scape", "Calf", "Raker", "Set", "Flower", "Fish"],
 ["Star", "Sky", "Night", "Dark", "Cloud"])
board("Films starring Meryl Streep", "Film", "medium", ["Meryl Streep", "actors"],
 ["The Devil Wears Prada", "Mamma Mia!", "Out of Africa", "Sophie's Choice", "Kramer vs. Kramer", "The Iron Lady", "The Deer Hunter", "Julie & Julia", "It's Complicated", "Doubt", "The Post", "Little Women", "Into the Woods", "The Bridges of Madison County", "Death Becomes Her"],
 ["Notes on a Scandal", "The Queen", "Shirley Valentine", "Calendar Girls", "Mrs Brown"])
board("Films starring Harrison Ford", "Film", "medium", ["Harrison Ford", "actors"],
 ["Star Wars", "Raiders of the Lost Ark", "Blade Runner", "The Fugitive", "Witness", "Air Force One", "Patriot Games", "Clear and Present Danger", "Working Girl", "What Lies Beneath", "Six Days, Seven Nights", "The Mosquito Coast", "Frantic", "Presumed Innocent", "American Graffiti"],
 ["Escape from New York", "Die Hard", "Lethal Weapon", "Mad Max", "Commando"])
board("Models made by Vauxhall", "Motoring", "medium", ["cars", "Vauxhall"],
 ["Corsa", "Astra", "Vectra", "Cavalier", "Nova", "Insignia", "Zafira", "Mokka", "Viva", "Chevette", "Carlton", "Senator", "Frontera", "Meriva", "Calibra"],
 ["Fiesta", "Focus", "Mondeo", "Escort", "Sierra"])
board("Models made by Toyota", "Motoring", "medium", ["cars", "Toyota"],
 ["Corolla", "Yaris", "Prius", "Camry", "RAV4", "Land Cruiser", "Hilux", "Supra", "Celica", "Aygo", "Auris", "Avensis", "C-HR", "MR2", "Previa"],
 ["Civic", "Jazz", "Micra", "Qashqai", "Accord"])
board("Countries where French is an official language", "World geography", "hard", ["French", "languages", "countries"],
 ["France", "Belgium", "Switzerland", "Canada", "Luxembourg", "Monaco", "Senegal", "Ivory Coast", "Cameroon", "Madagascar", "Haiti", "DR Congo", "Rwanda", "Seychelles", "Vanuatu"],
 ["Morocco", "Algeria", "Tunisia", "Vietnam", "Lebanon"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-19.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
