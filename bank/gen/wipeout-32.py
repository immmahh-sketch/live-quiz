# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-25.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Films starring Michelle Pfeiffer", "Film", "medium", ["Michelle Pfeiffer", "actors"],
 ["Scarface", "Grease 2", "The Witches of Eastwick", "Dangerous Liaisons", "The Fabulous Baker Boys", "Batman Returns", "The Age of Innocence", "Dangerous Minds", "One Fine Day", "What Lies Beneath", "Hairspray", "Stardust", "Ant-Man and the Wasp", "Ladyhawke", "Frankie and Johnny"],
 ["Basic Instinct", "Casino", "Total Recall", "9½ Weeks", "L.A. Confidential"])
board("Films starring Al Pacino", "Film", "medium", ["Al Pacino", "actors"],
 ["The Godfather", "Scarface", "Serpico", "Dog Day Afternoon", "Heat", "Carlito's Way", "Scent of a Woman", "The Devil's Advocate", "Donnie Brasco", "Glengarry Glen Ross", "The Irishman", "Insomnia", "Any Given Sunday", "Ocean's Thirteen", "Sea of Love"],
 ["Taxi Driver", "Raging Bull", "Goodfellas", "The Deer Hunter", "Casino"])
board("Tina Turner hits, solo or with Ike", "Music", "medium", ["Tina Turner", "songs"],
 ["What's Love Got to Do with It", "The Best", "Private Dancer", "We Don't Need Another Hero", "Proud Mary", "River Deep – Mountain High", "Nutbush City Limits", "Let's Stay Together", "GoldenEye", "Steamy Windows", "I Don't Wanna Lose You", "It Takes Two", "Typical Male", "Better Be Good to Me", "One of the Living"],
 ["Addicted to Love", "I Will Survive", "Respect", "Chain of Fools", "Total Eclipse of the Heart"])
board("Songs by Madness", "Music", "medium", ["Madness", "songs", "ska"],
 ["Our House", "Baggy Trousers", "House of Fun", "It Must Be Love", "One Step Beyond", "My Girl", "Embarrassment", "Night Boat to Cairo", "Driving in My Car", "Wings of a Dove", "The Prince", "Grey Day", "Cardiac Arrest", "Michael Caine", "Shut Up"],
 ["Ghost Town", "Too Much Too Young", "Red Red Wine", "Too Nice to Talk To", "On My Radio"])
board("Songs by the Jam", "Music", "hard", ["The Jam", "songs", "Paul Weller"],
 ["Going Underground", "Town Called Malice", "The Eton Rifles", "Start!", "That's Entertainment", "Beat Surrender", "In the City", "Down in the Tube Station at Midnight", "David Watts", "Absolute Beginners", "Funeral Pyre", "The Bitterest Pill", "Precious", "Strange Town", "News of the World"],
 ["Long Hot Summer", "My Ever Changing Moods", "You're the Best Thing", "Wild Wood", "The Changingman"])
board("James Bond titles that Ian Fleming used for his own books", "Books", "hard", ["James Bond", "Ian Fleming"],
 ["Casino Royale", "Live and Let Die", "Moonraker", "Diamonds Are Forever", "From Russia, with Love", "Dr. No", "Goldfinger", "For Your Eyes Only", "Thunderball", "The Spy Who Loved Me", "On Her Majesty's Secret Service", "You Only Live Twice", "The Man with the Golden Gun", "Octopussy", "Quantum of Solace"],
 ["GoldenEye", "Tomorrow Never Dies", "The World Is Not Enough", "Licence to Kill", "Skyfall"])
board("Italian islands", "Places", "hard", ["islands", "Italy"],
 ["Sicily", "Sardinia", "Capri", "Elba", "Ischia", "Lampedusa", "Stromboli", "Murano", "Burano", "Lipari", "Procida", "Pantelleria", "Giglio", "Vulcano", "Salina"],
 ["Corsica", "Malta", "Gozo", "Mallorca", "Corfu"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-32.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
