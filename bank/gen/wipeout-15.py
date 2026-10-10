# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-15.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Towns and villages in Northumberland", "The North East", "medium", ["Northumberland", "towns"],
 ["Alnwick", "Morpeth", "Hexham", "Berwick-upon-Tweed", "Blyth", "Cramlington", "Ashington", "Bamburgh", "Amble", "Rothbury", "Seahouses", "Haltwhistle", "Ponteland", "Prudhoe", "Corbridge"],
 ["Consett", "Stanley", "Chester-le-Street", "Seaham", "Gateshead"])
board("Roman gods and goddesses", "Myths and legends", "medium", ["Roman gods", "mythology"],
 ["Jupiter", "Juno", "Mars", "Venus", "Mercury", "Neptune", "Minerva", "Apollo", "Diana", "Vulcan", "Ceres", "Bacchus", "Pluto", "Vesta", "Janus"],
 ["Zeus", "Hera", "Ares", "Athena", "Poseidon"])
board("Clubs that have won the European Cup or Champions League", "Football", "medium", ["Champions League", "European Cup", "clubs"],
 ["Real Madrid", "Barcelona", "Bayern Munich", "AC Milan", "Inter Milan", "Liverpool", "Manchester United", "Chelsea", "Manchester City", "Nottingham Forest", "Aston Villa", "Celtic", "Ajax", "Porto", "Paris Saint-Germain"],
 ["Arsenal", "Tottenham Hotspur", "Atlético Madrid", "Valencia", "Leeds United"])
board("Islands in the Caribbean Sea", "World geography", "medium", ["Caribbean", "islands"],
 ["Jamaica", "Barbados", "Trinidad", "Cuba", "Puerto Rico", "St Lucia", "Grenada", "Antigua", "Dominica", "Martinique", "Guadeloupe", "Aruba", "Curaçao", "Montserrat", "Grand Cayman"],
 ["Bermuda", "Madeira", "Tenerife", "Fiji", "Mauritius"])
board("Words that make a new word when you add 'fish' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Cat", "Gold", "Sword", "Star", "Jelly", "Cuttle", "Shell", "Monk", "Angel", "Cray", "Flat", "Sun", "Lion", "Self", "Parrot"],
 ["Tank", "Net", "River", "Bowl", "Hook"])
board("Words that make a new word when you put 'air' in front", "Words and language", "easy", ["wordplay", "compound words"],
 ["Port", "Line", "Craft", "Bag", "Bus", "Field", "Plane", "Ship", "Strip", "Way", "Lift", "Bed", "Tight", "Space", "Mail"],
 ["Train", "Car", "Road", "Rail", "Truck"])
board("Words that make a new word when you put 'butter' in front", "Words and language", "medium", ["wordplay", "compound words"],
 ["Fly", "Cup", "Milk", "Nut", "Scotch", "Fingers", "Cream", "Bean", "Ball", "Fat", "Wort", "Mint", "Head", "Bur", "Fish"],
 ["Toast", "Spread", "Jam", "Pan", "Cheese"])
board("German car makers, past and present", "Motoring", "medium", ["cars", "Germany", "brands"],
 ["Volkswagen", "BMW", "Mercedes-Benz", "Audi", "Porsche", "Opel", "Smart", "Maybach", "Trabant", "Wartburg", "NSU", "Borgward", "Horch", "DKW", "Alpina"],
 ["Škoda", "SEAT", "Volvo", "Fiat", "Saab"])
board("Desserts and sweet treats from Italy", "Food and drink", "medium", ["Italian food", "desserts"],
 ["Tiramisu", "Panna cotta", "Cannoli", "Gelato", "Zabaglione", "Affogato", "Semifreddo", "Panettone", "Biscotti", "Sfogliatella", "Torrone", "Granita", "Zuppa inglese", "Cassata", "Pandoro"],
 ["Churros", "Baklava", "Crème brûlée", "Pastel de nata", "Profiteroles"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-15.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
