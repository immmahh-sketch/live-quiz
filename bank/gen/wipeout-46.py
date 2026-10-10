# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-46.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Things you'd find on a British beach", "Everyday life", "easy", ["seaside", "beach"],
 ["Sand", "Pebbles", "Seaweed", "Shells", "Deckchair", "Windbreak", "Lifeguard", "Donkeys", "Beach hut", "Groyne", "Rock pool", "Sandcastle", "Ice cream van", "Seagull", "Bucket and spade"],
 ["Cactus", "Igloo", "Glacier", "Stalactite", "Avalanche"])
board("Playground games", "Games and toys", "easy", ["playground", "games", "childhood"],
 ["Tig", "Hopscotch", "Skipping", "British Bulldog", "What's the Time, Mr Wolf?", "Duck, Duck, Goose", "Hide and seek", "Stuck in the mud", "Conkers", "Marbles", "Leapfrog", "Kiss chase", "Piggy in the middle", "Simon Says", "Grandmother's Footsteps"],
 ["Chess", "Snooker", "Bridge", "Darts", "Monopoly"])
board("Things you'd find in a bathroom", "Everyday life", "easy", ["home", "bathroom"],
 ["Toothbrush", "Toothpaste", "Towel", "Soap", "Shampoo", "Bath mat", "Shower curtain", "Loo roll", "Mirror", "Plunger", "Sponge", "Razor", "Bubble bath", "Flannel", "Bathroom scales"],
 ["Kettle", "Toaster", "Colander", "Rolling pin", "Oven glove"])
board("Words that make a new word when you put 'black' in front", "Words and language", "medium", ["wordplay", "compound words"],
 ["Bird", "Board", "Berry", "Smith", "Mail", "Out", "Jack", "Pool", "Head", "Currant", "List", "Ball", "Leg", "Guard", "Thorn"],
 ["Tree", "Cup", "Rain", "Sock", "Nose"])
board("Words that make a new word when you add 'day' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Birth", "Holi", "Yester", "Week", "Mid", "Dooms", "Pay", "Hey", "Some", "Every", "Work", "To", "Wash", "May", "Sun"],
 ["Night", "Cake", "Moon", "Star", "Lunch"])
board("Things you'd find in a garden shed", "Everyday life", "easy", ["garden", "home"],
 ["Lawnmower", "Spade", "Rake", "Hoe", "Watering can", "Wheelbarrow", "Hedge trimmer", "Secateurs", "Trowel", "Garden fork", "Plant pots", "Bag of compost", "Strimmer", "Hosepipe", "Seed trays"],
 ["Toaster", "Kettle", "Sofa", "Duvet", "Hairdryer"])
board("Things you'd find at an airport", "Travel", "easy", ["airports", "flying"],
 ["Departure lounge", "Check-in desk", "Baggage carousel", "Duty free", "Passport control", "Security scanner", "Runway", "Control tower", "Boarding gate", "Departures board", "Customs", "Travelator", "Hangar", "Air bridge", "Arrivals hall"],
 ["Platform", "Ticket barrier", "Signal box", "Buffers", "Level crossing"])
board("Things you'd pack in a picnic hamper", "Food and drink", "easy", ["picnics", "food"],
 ["Sandwiches", "Scotch eggs", "Sausage rolls", "Crisps", "Flask of tea", "Pork pie", "Strawberries", "Paper plates", "Napkins", "Picnic blanket", "Quiche", "Coleslaw", "Lemonade", "Cake", "Grapes"],
 ["Roast turkey", "Gravy", "Lasagne", "Custard", "Christmas pudding"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-46.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
