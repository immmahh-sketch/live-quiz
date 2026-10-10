# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-25.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'box' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Post", "Letter", "Jack", "Juke", "Sand", "Tool", "Lunch", "Match", "Shoe", "Ice", "Chatter", "Fuse", "Gear", "Soap", "Strong"],
 ["Crate", "Chest", "Carton", "Parcel", "Basket"])
board("Words that make a new word when you add 'back' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Hunch", "Horse", "Paper", "Hard", "Feed", "Pay", "Flash", "Hatch", "Throw", "Set", "Draw", "Quarter", "Half", "Out", "Razor"],
 ["Front", "Spine", "Shoulder", "Chair", "Body"])
board("Words that make a new word when you add 'some' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Hand", "Awe", "Lone", "Tire", "Whole", "Trouble", "Fear", "Win", "Bother", "Tooth", "Burden", "Meddle", "Loath", "Two", "Four"],
 ["Happy", "Good", "Sad", "Kind", "Brave"])
board("Words that make a new word when you add 'ware' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Soft", "Hard", "Kitchen", "Silver", "Glass", "Table", "Earthen", "Cook", "Oven", "Firm", "Spy", "Free", "Share", "Stone", "Tin"],
 ["Plate", "Cup", "Bowl", "Spoon", "Pan"])
board("Words that make a new word when you add 'proof' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Water", "Fire", "Sound", "Bullet", "Child", "Fool", "Shower", "Wind", "Bomb", "Burglar", "Rust", "Damp", "Shatter", "Weather", "Future"],
 ["Dry", "Safe", "Strong", "Wet", "Steel"])
board("Films starring Michael Caine", "Film", "medium", ["Michael Caine", "actors"],
 ["Zulu", "The Italian Job", "Get Carter", "Alfie", "The Ipcress File", "Educating Rita", "Hannah and Her Sisters", "The Cider House Rules", "Sleuth", "The Dark Knight", "Inception", "The Muppet Christmas Carol", "Interstellar", "Dirty Rotten Scoundrels", "The Eagle Has Landed"],
 ["The Untouchables", "Highlander", "The Rock", "The Name of the Rose", "Entrapment"])
board("Films starring Jim Carrey", "Film", "medium", ["Jim Carrey", "actors"],
 ["Ace Ventura: Pet Detective", "The Mask", "Dumb and Dumber", "Liar Liar", "The Truman Show", "Man on the Moon", "Me, Myself & Irene", "How the Grinch Stole Christmas", "Bruce Almighty", "Eternal Sunshine of the Spotless Mind", "Lemony Snicket's A Series of Unfortunate Events", "Yes Man", "Batman Forever", "Sonic the Hedgehog", "The Cable Guy"],
 ["Evan Almighty", "Night at the Museum", "Zoolander", "Meet the Parents", "There's Something About Mary"])
board("Films starring Anthony Hopkins", "Film", "medium", ["Anthony Hopkins", "actors"],
 ["The Silence of the Lambs", "Hannibal", "Red Dragon", "The Remains of the Day", "Shadowlands", "The Elephant Man", "Legends of the Fall", "Nixon", "The Mask of Zorro", "Meet Joe Black", "Thor", "The Two Popes", "The Father", "Howards End", "Bram Stoker's Dracula"],
 ["The Madness of King George", "Gandhi", "A Room with a View", "Chariots of Fire", "The English Patient"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-26.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
