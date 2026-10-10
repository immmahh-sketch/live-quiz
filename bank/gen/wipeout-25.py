# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-25.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'craft' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Air", "Hover", "Space", "Hand", "Water", "State", "Witch", "Stage", "Wood", "Needle", "War", "Bush", "Leather", "Paper", "Word"],
 ["Car", "Ship", "Boat", "Train", "Bus"])
board("Words that make a new word when you add 'yard' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Back", "Grave", "Ship", "Church", "Farm", "Vine", "Court", "Barn", "Brick", "Junk", "Scrap", "School", "Boat", "Stock", "Dock"],
 ["Garden", "Field", "Lawn", "Park", "House"])
board("Words that make a new word when you add 'master' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Head", "Ring", "Quarter", "Post", "Station", "Band", "Task", "Toast", "Web", "Grand", "Choir", "Pay", "Quiz", "Harbour", "Scout"],
 ["King", "Boss", "Teacher", "Captain", "Chef"])
board("Films starring Hugh Jackman", "Film", "medium", ["Hugh Jackman", "actors"],
 ["X-Men", "The Greatest Showman", "Les Misérables", "Logan", "The Prestige", "Kate & Leopold", "Van Helsing", "Australia", "Real Steel", "Prisoners", "Swordfish", "The Fountain", "Eddie the Eagle", "Chappie", "Deadpool & Wolverine"],
 ["Gladiator", "A Beautiful Mind", "Master and Commander", "L.A. Confidential", "Cinderella Man"])
board("Films starring Cate Blanchett", "Film", "medium", ["Cate Blanchett", "actors"],
 ["Elizabeth", "The Lord of the Rings", "Blue Jasmine", "Carol", "The Aviator", "Tár", "Notes on a Scandal", "Babel", "Ocean's 8", "Thor: Ragnarok", "The Curious Case of Benjamin Button", "Cinderella", "Indiana Jones and the Kingdom of the Crystal Skull", "The Talented Mr. Ripley", "Don't Look Up"],
 ["Moulin Rouge!", "The Hours", "Eyes Wide Shut", "The Others", "Practical Magic"])
board("Films starring Johnny Depp", "Film", "medium", ["Johnny Depp", "actors"],
 ["Pirates of the Caribbean", "Edward Scissorhands", "Sweeney Todd", "Charlie and the Chocolate Factory", "Donnie Brasco", "Ed Wood", "Sleepy Hollow", "Finding Neverland", "Fear and Loathing in Las Vegas", "Chocolat", "Black Mass", "Public Enemies", "What's Eating Gilbert Grape", "Cry-Baby", "A Nightmare on Elm Street"],
 ["Beetlejuice", "Big Fish", "Mars Attacks!", "Batman", "Kingdom of Heaven"])
board("Songs Elvis Presley had hits with", "Music", "medium", ["Elvis Presley", "songs"],
 ["Hound Dog", "Jailhouse Rock", "Heartbreak Hotel", "Suspicious Minds", "Love Me Tender", "All Shook Up", "Return to Sender", "Can't Help Falling in Love", "Blue Suede Shoes", "In the Ghetto", "Burning Love", "Always on My Mind", "It's Now or Never", "Are You Lonesome Tonight?", "A Little Less Conversation"],
 ["Johnny B. Goode", "Great Balls of Fire", "Rock Around the Clock", "Tutti Frutti", "Peggy Sue"])
board("Songs by Adele", "Music", "medium", ["Adele", "songs"],
 ["Hello", "Someone Like You", "Rolling in the Deep", "Skyfall", "Set Fire to the Rain", "Chasing Pavements", "Make You Feel My Love", "Easy on Me", "Hometown Glory", "Rumour Has It", "When We Were Young", "Send My Love", "Water Under the Bridge", "Turning Tables", "Oh My God"],
 ["Rehab", "Back to Black", "Valerie", "Mercy", "Warwick Avenue"])
board("Varieties of pear", "Food and drink", "hard", ["pears", "fruit"],
 ["Conference", "Comice", "Williams", "Concorde", "Bosc", "Packham's Triumph", "Anjou", "Forelle", "Rocha", "Seckel", "Beurré Hardy", "Durondeau", "Onward", "Nashi", "Louise Bonne"],
 ["Bramley", "Braeburn", "Cox's Orange Pippin", "Gala", "Egremont Russet"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-25.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
