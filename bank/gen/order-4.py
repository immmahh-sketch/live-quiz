# Bank session 9 Oct 2026 (third pass): 2 more Put in Order questions for 11 broad topics that had 5 live.
# Items are listed in the right order; wording is specific so it can't clash with another topic's.
# Writes bank/topics/<slug>__o4.json; import each with FILE=<slug>__o4 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def o(slug, diff, text, *items):
    assert 4 <= len(items) <= 5 and len(set(items)) == len(items), text
    OUT.setdefault(slug, []).append({"type": "order", "text": text, "items": list(items), "difficulty": diff})

o("action-films", "medium", "Put these Mission: Impossible films in release order, earliest first", "Mission: Impossible", "Mission: Impossible 2", "Ghost Protocol", "Fallout", "Dead Reckoning")
o("action-films", "medium", "Put these Arnold Schwarzenegger films in release order, earliest first", "The Terminator", "Predator", "Total Recall", "True Lies", "Jingle All the Way")

o("us-tv", "medium", "Put these US sitcoms in the order their final episode was shown, earliest first", "Cheers", "Seinfeld", "Friends", "The Office (US)", "The Big Bang Theory")
o("us-tv", "medium", "Put these HBO dramas in order of first broadcast, earliest first", "The Sopranos", "The Wire", "Game of Thrones", "True Detective", "Succession")

o("ancient-history", "hard", "Put these Wonders of the Ancient World in the order they were built, earliest first", "The Great Pyramid of Giza", "The Temple of Artemis", "The Statue of Zeus", "The Mausoleum at Halicarnassus", "The Colossus of Rhodes")
o("ancient-history", "medium", "Put these Egyptian rulers in the order they reigned, earliest first", "Khufu", "Hatshepsut", "Tutankhamun", "Ramesses II", "Cleopatra")

o("animals", "medium", "Put these animals in order of how long they're pregnant, shortest first", "Mouse", "Cat", "Human", "Horse", "Elephant")
o("animals", "easy", "Put these birds in order of size, smallest first", "Wren", "Robin", "Pigeon", "Swan", "Ostrich")

o("pixar-animation", "medium", "Put these Disney princesses in order of their film's release, earliest first", "Snow White", "Cinderella", "Aurora", "Ariel", "Moana")
o("pixar-animation", "medium", "Put these Wallace & Gromit films in release order, earliest first", "A Grand Day Out", "The Wrong Trousers", "A Close Shave", "The Curse of the Were-Rabbit", "Vengeance Most Fowl")

o("art", "medium", "Put these masterpieces, from the Mona Lisa to Guernica, in the order they were painted", "Mona Lisa", "The Night Watch", "The Hay Wain", "The Starry Night", "Guernica")
o("art", "hard", "Put these London art institutions in the order they opened, earliest first", "The Royal Academy", "The National Gallery", "Tate Britain", "The Hayward Gallery", "Tate Modern")

o("beer-wine-spirits", "medium", "Put the stages of brewing beer in order", "Malting", "Mashing", "Boiling with hops", "Fermenting", "Conditioning")
o("beer-wine-spirits", "easy", "Put the stages of making wine in order", "Harvesting the grapes", "Crushing", "Fermenting", "Ageing", "Bottling")

o("books", "hard", "Put these Narnia books in the order they were published, earliest first", "The Lion, the Witch and the Wardrobe", "Prince Caspian", "The Voyage of the Dawn Treader", "The Silver Chair", "The Last Battle")
o("books", "medium", "Put these Roald Dahl books from the 1980s in the order they were published", "The Twits", "George's Marvellous Medicine", "The BFG", "The Witches", "Matilda")

o("boxing-combat", "hard", "Put these British boxers in the order they first won a world title, earliest first", "Barry McGuigan", "Lennox Lewis", "Naseem Hamed", "Joe Calzaghe", "Tyson Fury")
o("boxing-combat", "medium", "Put these Rocky and Creed films in release order, earliest first", "Rocky III", "Rocky IV", "Rocky Balboa", "Creed", "Creed II")

o("boy-bands-girl-groups", "medium", "Put these One Direction albums in release order, earliest first", "Up All Night", "Take Me Home", "Midnight Memories", "Four", "Made in the A.M.")
o("boy-bands-girl-groups", "medium", "Put these Girls Aloud singles in release order, earliest first", "Sound of the Underground", "Jump", "Biology", "Something Kinda Ooooh", "The Promise")

o("brands-logos", "medium", "Put these British supermarket chains in the order they were founded", "Sainsbury's", "Morrisons", "Tesco", "Asda")
o("brands-logos", "medium", "Put these car makers in order of founding, earliest first", "Ford", "Rolls-Royce", "BMW", "Toyota", "Tesla")

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__o4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'orders in', len(OUT), 'topics:', ' '.join(OUT))
