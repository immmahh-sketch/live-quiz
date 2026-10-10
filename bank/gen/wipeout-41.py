# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-41.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Films starring Eddie Murphy", "Film", "medium", ["Eddie Murphy", "films"],
 ["Beverly Hills Cop", "Coming to America", "Trading Places", "48 Hrs.", "The Nutty Professor", "Doctor Dolittle", "Shrek", "Bowfinger", "Dreamgirls", "Mulan", "Daddy Day Care", "The Golden Child", "Norbit", "Dolemite Is My Name", "Harlem Nights"],
 ["Lethal Weapon", "Bad Boys", "Men in Black", "Rush Hour", "Ghostbusters"])
board("Films starring Adam Sandler", "Film", "medium", ["Adam Sandler", "films"],
 ["Happy Gilmore", "Billy Madison", "The Wedding Singer", "Big Daddy", "50 First Dates", "Click", "Grown Ups", "Mr. Deeds", "Anger Management", "The Waterboy", "Uncut Gems", "Hotel Transylvania", "Murder Mystery", "Hubie Halloween", "Pixels"],
 ["Dodgeball", "Zoolander", "Anchorman", "Old School", "Step Brothers"])
board("Films starring Ryan Gosling", "Film", "medium", ["Ryan Gosling", "films"],
 ["The Notebook", "La La Land", "Drive", "Crazy, Stupid, Love.", "Blade Runner 2049", "Barbie", "The Big Short", "Half Nelson", "Lars and the Real Girl", "The Ides of March", "Gangster Squad", "The Nice Guys", "First Man", "The Fall Guy", "Project Hail Mary"],
 ["Whiplash", "Nightcrawler", "Inception", "Her", "The Social Network"])
board("Films starring Liam Neeson", "Film", "medium", ["Liam Neeson", "films"],
 ["Schindler's List", "Taken", "Love Actually", "Michael Collins", "Rob Roy", "Star Wars: Episode I – The Phantom Menace", "Batman Begins", "Kinsey", "Gangs of New York", "Darkman", "The Grey", "Non-Stop", "Unknown", "Les Misérables", "The Naked Gun"],
 ["The Bourne Identity", "John Wick", "Commando", "Man on Fire", "The Equalizer"])
board("Films starring Christian Bale", "Film", "medium", ["Christian Bale", "films"],
 ["American Psycho", "Batman Begins", "The Dark Knight", "The Fighter", "The Big Short", "Vice", "Le Mans '66", "Empire of the Sun", "The Prestige", "The Machinist", "American Hustle", "Little Women", "Newsies", "3:10 to Yuma", "Thor: Love and Thunder"],
 ["Memento", "Fight Club", "Moneyball", "Se7en", "The Departed"])
board("Films starring Colin Firth", "Film", "medium", ["Colin Firth", "films"],
 ["Bridget Jones's Diary", "Love Actually", "The King's Speech", "Mamma Mia!", "Kingsman: The Secret Service", "A Single Man", "Shakespeare in Love", "The English Patient", "Fever Pitch", "Nanny McPhee", "St Trinian's", "Girl with a Pearl Earring", "Tinker Tailor Soldier Spy", "1917", "Mary Poppins Returns"],
 ["Notting Hill", "Four Weddings and a Funeral", "About a Boy", "Sense and Sensibility", "Atonement"])
board("Films starring Scarlett Johansson", "Film", "medium", ["Scarlett Johansson", "films"],
 ["Lost in Translation", "Lucy", "Her", "Under the Skin", "Marriage Story", "Jojo Rabbit", "Black Widow", "The Avengers", "Ghost World", "Girl with a Pearl Earring", "Match Point", "The Prestige", "Vicky Cristina Barcelona", "Ghost in the Shell", "Jurassic World Rebirth"],
 ["Black Swan", "Wonder Woman", "Captain Marvel", "Gone Girl", "La La Land"])
board("Films starring Ralph Fiennes", "Film", "hard", ["Ralph Fiennes", "films"],
 ["Schindler's List", "The English Patient", "The Grand Budapest Hotel", "Harry Potter and the Goblet of Fire", "Skyfall", "In Bruges", "The Constant Gardener", "Red Dragon", "Maid in Manhattan", "Quiz Show", "Wuthering Heights", "The Menu", "Conclave", "The End of the Affair", "The Reader"],
 ["The Pianist", "Atonement", "Shakespeare in Love", "Amadeus", "The Remains of the Day"])
board("Films starring Gary Oldman", "Film", "medium", ["Gary Oldman", "films"],
 ["Léon", "Darkest Hour", "The Dark Knight", "Harry Potter and the Prisoner of Azkaban", "Tinker Tailor Soldier Spy", "Bram Stoker's Dracula", "JFK", "The Fifth Element", "Sid and Nancy", "True Romance", "Air Force One", "Mank", "Hannibal", "Batman Begins", "Prick Up Your Ears"],
 ["Heat", "Se7en", "The Usual Suspects", "Fight Club", "Memento"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-41.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
