# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-25.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'ward' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Home", "Back", "Fore", "Up", "Down", "In", "Out", "After", "Sea", "East", "West", "Wind", "Lee", "Way", "Sky"],
 ["Left", "Right", "Over", "Under", "Middle"])
board("Words that make a new word when you add 'stand' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Band", "Grand", "Hat", "Hand", "Kick", "Night", "News", "Under", "With", "Wash", "Ink", "Head", "Cake", "Coat", "Hall"],
 ["Sit", "Lie", "Kneel", "Walk", "Run"])
board("Films starring Helen Mirren", "Film", "medium", ["Helen Mirren", "actors"],
 ["The Queen", "Calendar Girls", "Gosford Park", "The Long Good Friday", "Excalibur", "The Madness of King George", "Red", "The Hundred-Foot Journey", "Woman in Gold", "Trumbo", "Eye in the Sky", "Hitchcock", "The Last Station", "Golda", "The Cook, the Thief, His Wife & Her Lover"],
 ["Philomena", "Mrs Brown", "Iris", "The Lady in the Van", "Ladies in Lavender"])
board("Films starring Samuel L. Jackson", "Film", "medium", ["Samuel L. Jackson", "actors"],
 ["Pulp Fiction", "Jackie Brown", "Snakes on a Plane", "Die Hard with a Vengeance", "Django Unchained", "Jurassic Park", "The Avengers", "Unbreakable", "The Hateful Eight", "Kingsman: The Secret Service", "Coach Carter", "Shaft", "A Time to Kill", "Deep Blue Sea", "Captain Marvel"],
 ["The Matrix", "Boyz n the Hood", "Se7en", "The Shawshank Redemption", "Driving Miss Daisy"])
board("Songs by the Kinks", "Music", "medium", ["The Kinks", "songs", "1960s"],
 ["You Really Got Me", "Waterloo Sunset", "Lola", "Sunny Afternoon", "All Day and All of the Night", "Days", "Dedicated Follower of Fashion", "Tired of Waiting for You", "Autumn Almanac", "Victoria", "Apeman", "Come Dancing", "A Well Respected Man", "Dead End Street", "See My Friends"],
 ["My Generation", "Substitute", "Itchycoo Park", "All or Nothing", "Lazy Sunday"])
board("Songs by Blondie", "Music", "medium", ["Blondie", "songs"],
 ["Heart of Glass", "Call Me", "Atomic", "Sunday Girl", "Denis", "Hanging on the Telephone", "The Tide Is High", "Rapture", "Maria", "Dreaming", "Picture This", "Union City Blue", "One Way or Another", "Island of Lost Souls", "Good Boys"],
 ["Brass in Pocket", "Don't You Want Me", "Kids in America", "Wuthering Heights", "Gloria"])
board("Sea fish (not shellfish) you'd see on a British fishmonger's slab", "Food and drink", "medium", ["fish", "seafood"],
 ["Cod", "Haddock", "Plaice", "Mackerel", "Sole", "Halibut", "Hake", "Pollock", "Sea bass", "Turbot", "Monkfish", "Herring", "Sardine", "Skate", "Whiting"],
 ["Squid", "Prawn", "Lobster", "Mussel", "Scallop"])
board("Italian car makers, past and present", "Transport", "hard", ["cars", "Italy"],
 ["Ferrari", "Lamborghini", "Maserati", "Alfa Romeo", "Fiat", "Lancia", "Pagani", "Abarth", "De Tomaso", "Iso", "Autobianchi", "Innocenti", "Cisitalia", "Iveco", "Dallara"],
 ["Porsche", "SEAT", "Škoda", "Citroën", "Volvo"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-31.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
