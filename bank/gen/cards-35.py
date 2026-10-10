# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-35.json. A row of 5-7 cards each:
# what's on the card, what it shows when it flips, and the number compared. The numbers zig-zag, no equal neighbours.
# Titles must be new to the bank (the import skips a repeated title as a duplicate).
import json, os
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    assert len({l for l, _, _ in cards}) == len(cards), (text, 'repeated card')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("the numbers of the Moon", "Space", "medium", ["the Moon", "space"], [
 ("People who have walked on it", "12", 12), ("Apollo missions that landed", "6", 6), ("Days it takes to go round the Earth, roughly", "27", 27),
 ("Its gravity, as a percentage of Earth's", "16.6", 16.6), ("Its width, in kilometres", "3,474", 3474)])
game("the numbers of Mount Everest", "World geography", "medium", ["Everest", "mountains"], [
 ("Its height in metres (2020 survey)", "8,849", 8849), ("Year it was first climbed", "1953", 1953), ("People in the first pair to reach the top", "2", 2),
 ("Height of South Base Camp, roughly, in metres", "5,364", 5364), ("Peaks in the world over 8,000 metres", "14", 14)])
game("the numbers of the Pyramids of Giza", "History", "hard", ["Egypt", "pyramids"], [
 ("Original height of the Great Pyramid, in metres", "146", 146), ("Main pyramids at Giza", "3", 3), ("Wonders of the Ancient World", "7", 7),
 ("Sides of a pyramid's base", "4", 4), ("Stone blocks in the Great Pyramid, in millions", "2.3", 2.3)])
game("the numbers of Wimbledon", "Sport", "medium", ["Wimbledon", "tennis"], [
 ("Year it was first held", "1877", 1877), ("Height the grass is cut to, in millimetres", "8", 8), ("Grass courts used for the Championships", "18", 18),
 ("Seats on Centre Court, roughly", "15,000", 15000), ("Sets in a men's singles match (best of)", "5", 5)])
game("the numbers in the story of Noah's Ark", "Religion", "medium", ["Bible", "Noah"], [
 ("Days and nights it rained", "40", 40), ("Animals of each kind, two by two", "2", 2), ("Noah's sons", "3", 3),
 ("Noah's age when the flood came", "600", 600), ("Length of the ark, in cubits", "300", 300), ("People on board", "8", 8)])
game("the numbers of the Lake District", "Britain", "hard", ["Lake District", "Cumbria"], [
 ("Wainwright fells", "214", 214), ("Waters officially called a 'lake'", "1", 1), ("Height of Scafell Pike, in metres", "978", 978),
 ("Year it became a national park", "1951", 1951), ("Length of Windermere, in miles", "10.5", 10.5)])
game("the numbers of Hadrian's Wall", "History", "hard", ["Hadrian's Wall", "Romans"], [
 ("Length, in miles", "73", 73), ("Year building began (AD)", "122", 122), ("Milecastles, roughly", "80", 80),
 ("Main forts along it", "16", 16), ("Year it became a World Heritage Site", "1987", 1987)])
game("the numbers of the Angel of the North", "The North East", "medium", ["Angel of the North", "Gateshead"], [
 ("Height, in metres", "20", 20), ("Wingspan, in metres", "54", 54), ("Tonnes of steel", "200", 200),
 ("Year it went up", "1998", 1998), ("Wind speed it was built to stand, in mph", "100", 100)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-35.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
