# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-63.json (TV shows and films). A row of 5-7 cards each:
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

game("the numbers of Blue Peter", "TV", "medium", ["Blue Peter", "children's TV"], [
 ("Year it first aired", "1958", 1958), ("Minutes the first show lasted", "15", 15), ("Year Petra the dog joined", "1962", 1962),
 ("Year Shep the dog joined", "1971", 1971), ("Year it moved to Salford", "2012", 2012)])
game("the numbers of EastEnders", "TV", "medium", ["EastEnders", "soaps"], [
 ("Year it first aired", "1985", 1985), ("Millions who watched Den hand Angie the divorce papers", "30", 30), ("Year Phil and Grant Mitchell arrived", "1990", 1990),
 ("The Queen Vic's number in Albert Square", "46", 46), ("Year Barbara Windsor joined as Peggy", "1994", 1994)])
game("the numbers of Top Gear", "TV", "medium", ["Top Gear", "cars"], [
 ("Year the original Top Gear began", "1977", 1977), ("Year it was relaunched with the studio and track", "2002", 2002), ("Series with Clarkson, Hammond and May", "22", 22),
 ("Year of Richard Hammond's jet-car crash", "2006", 2006), ("Year that trio's last series aired", "2015", 2015)])
game("the numbers of Only Fools and Horses", "TV", "medium", ["Only Fools and Horses", "sitcoms"], [
 ("Year it first aired", "1981", 1981), ("Floor of Nelson Mandela House the Trotters live on", "12th", 12), ("Year they finally became millionaires", "1996", 1996),
 ("Wheels on the Trotters' van", "3", 3), ("Millions who watched them strike it rich", "24", 24)])
game("the numbers of The Simpsons", "TV", "medium", ["The Simpsons", "cartoons"], [
 ("Year the first full episode aired", "1989", 1989), ("Bart's age", "10", 10), ("Year The Simpsons Movie came out", "2007", 2007),
 ("Lisa's age", "8", 8), ("Homer's sector at the power plant", "7G", 7)])
game("the numbers of Toy Story", "Film", "medium", ["Toy Story", "Pixar"], [
 ("Year the first film came out", "1995", 1995), ("Eyes on each of the Little Green Men", "3", 3), ("Year Toy Story 3 came out", "2010", 2010),
 ("Toy Story films, up to 2025", "4", 4), ("Year Toy Story 4 came out", "2019", 2019)])
game("the numbers of Shrek", "Film", "medium", ["Shrek", "DreamWorks"], [
 ("Year the first film came out", "2001", 2001), ("Shrek films, up to 2025", "4", 4), ("Year it won the first ever Best Animated Feature Oscar", "2002", 2002),
 ("Year Shrek 2 came out", "2004", 2004), ("Year Shrek the Musical opened on Broadway", "2008", 2008)])
game("the numbers of Mary Poppins", "Film", "medium", ["Mary Poppins", "Disney"], [
 ("Year the first book came out", "1934", 1934), ("Oscars the 1964 film won", "5", 5), ("Year the film came out", "1964", 1964),
 ("Julie Andrews's age when it came out", "28", 28), ("Year Mary Poppins Returns came out", "2018", 2018)])
game("the numbers of Thunderbirds", "TV", "medium", ["Thunderbirds", "Gerry Anderson"], [
 ("Year it first aired", "1965", 1965), ("Numbered Thunderbird craft", "5", 5), ("Year the live-action film came out", "2004", 2004),
 ("Episodes of the original series", "32", 32), ("Year Thunderbirds Are Go began", "2015", 2015)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-63.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
