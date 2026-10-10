# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-25.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'hole' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Pot", "Key", "Bolt", "Button", "Peep", "Arm", "Loop", "Man", "Pin", "Pigeon", "Sink", "Port", "Plug", "Worm", "Fox"],
 ["Mouse", "Cave", "Pit", "Gap", "Tunnel"])
board("Films starring Russell Crowe", "Film", "medium", ["Russell Crowe", "actors"],
 ["Gladiator", "A Beautiful Mind", "Master and Commander", "L.A. Confidential", "Cinderella Man", "The Insider", "Robin Hood", "Les Misérables", "Noah", "3:10 to Yuma", "American Gangster", "Man of Steel", "The Nice Guys", "Romper Stomper", "Proof of Life"],
 ["The Prestige", "Logan", "The Greatest Showman", "Australia", "Van Helsing"])
board("Films starring Sigourney Weaver", "Film", "medium", ["Sigourney Weaver", "actors"],
 ["Alien", "Aliens", "Ghostbusters", "Gorillas in the Mist", "Working Girl", "Avatar", "Galaxy Quest", "The Ice Storm", "Copycat", "Holes", "Paul", "Finding Dory", "Dave", "Death and the Maiden", "Avatar: The Way of Water"],
 ["Halloween", "True Lies", "Trading Places", "The Terminator", "A Fish Called Wanda"])
board("Films starring Bill Murray", "Film", "medium", ["Bill Murray", "actors"],
 ["Ghostbusters", "Groundhog Day", "Lost in Translation", "Caddyshack", "Scrooged", "Stripes", "What About Bob?", "Rushmore", "The Royal Tenenbaums", "Space Jam", "Zombieland", "Tootsie", "The Grand Budapest Hotel", "Moonrise Kingdom", "Broken Flowers"],
 ["The Blues Brothers", "Driving Miss Daisy", "National Lampoon's Vacation", "Fletch", "Spies Like Us"])
board("ABBA hits that never reached number one in the UK", "Music", "hard", ["ABBA", "songs"],
 ["SOS", "Money, Money, Money", "Chiquitita", "Gimme! Gimme! Gimme!", "Voulez-Vous", "Does Your Mother Know", "I Have a Dream", "Lay All Your Love on Me", "One of Us", "Summer Night City", "Thank You for the Music", "Ring Ring", "I Do, I Do, I Do, I Do, I Do", "The Day Before You Came", "Angeleyes"],
 ["Dancing Queen", "Waterloo", "Fernando", "Mamma Mia", "Super Trouper"])
board("Songs Prince released himself", "Music", "hard", ["Prince", "songs"],
 ["Purple Rain", "When Doves Cry", "Kiss", "1999", "Little Red Corvette", "Raspberry Beret", "Let's Go Crazy", "Cream", "Sign o' the Times", "Alphabet St.", "Diamonds and Pearls", "The Most Beautiful Girl in the World", "Batdance", "Controversy", "U Got the Look"],
 ["Nothing Compares 2 U", "Manic Monday", "I Feel for You", "The Glamorous Life", "Jungle Love"])
board("Breeds of pig", "Nature", "hard", ["pigs", "farm animals"],
 ["Large White", "Gloucestershire Old Spot", "Tamworth", "Berkshire", "Saddleback", "Middle White", "Large Black", "Hampshire", "Landrace", "Duroc", "Pietrain", "Kunekune", "Mangalitsa", "Oxford Sandy and Black", "Welsh"],
 ["Aberdeen Angus", "Hereford", "Jersey", "Suffolk", "Texel"])
board("Types of bean", "Food and drink", "medium", ["beans", "vegetables"],
 ["Kidney", "Butter", "Broad", "Runner", "Haricot", "Pinto", "Black-eyed", "Borlotti", "Cannellini", "Mung", "Soya", "French", "Lima", "Adzuki", "Navy"],
 ["Lentil", "Petits pois", "Mangetout", "Split pea", "Sugar snap"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-29.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
