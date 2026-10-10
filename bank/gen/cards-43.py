# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-43.json. A row of 5-7 cards each:
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

game("the numbers of the Boat Race", "Sport", "hard", ["Boat Race", "rowing"], [
 ("Year of the first race", "1829", 1829), ("People in each boat, including the cox", "9", 9), ("Year of the only dead heat", "1877", 1877),
 ("Length of the course in miles, roughly", "4", 4), ("Year the women's race moved onto the same Thames course", "2015", 2015)])
game("the numbers of the Grand National", "Sport", "hard", ["Grand National", "horse racing"], [
 ("Year it was first run at Aintree", "1839", 1839), ("Jumps in the race", "30", 30), ("Times Red Rum won it", "3", 3),
 ("Most runners allowed, since 2024", "34", 34), ("Year it was declared void after a false start", "1993", 1993)])
game("the numbers of the London Marathon", "Sport", "hard", ["London Marathon", "running"], [
 ("Year of the first race", "1981", 1981), ("Distance in miles", "26.2", 26.2), ("Year Paula Radcliffe set her world record there", "2003", 2003),
 ("Her time: 2 hours and how many minutes?", "15", 15), ("Year the finish moved to The Mall", "1994", 1994)])
game("the numbers of Glastonbury Festival", "Music", "hard", ["Glastonbury", "festivals"], [
 ("Year of the first festival", "1970", 1970), ("Price of a ticket that first year, in pounds", "1", 1), ("Year the first Pyramid Stage went up", "1971", 1971),
 ("Tickets sold these days, in thousands, roughly", "210", 210), ("Year Jay-Z headlined, to Noel Gallagher's disgust", "2008", 2008)])
game("the numbers of the FA Cup", "Football", "hard", ["FA Cup", "football"], [
 ("Year of the first final", "1872", 1872), ("Clubs in the first competition", "15", 15), ("Year of the first final at Wembley", "1923", 1923),
 ("Fans said to have crammed into that 'White Horse Final', in thousands, roughly", "200", 200), ("Year of the first final at the new Wembley", "2007", 2007)])
game("the numbers of the Ashes", "Cricket", "hard", ["Ashes", "cricket"], [
 ("Year of the mock obituary that started it all", "1882", 1882), ("Height of the little urn, in centimetres, roughly", "11", 11), ("Tests in a usual Ashes series", "5", 5),
 ("Don Bradman's Test batting average", "99.94", 99.94), ("Year of the famous Flintoff series win", "2005", 2005)])
game("the numbers of the Monaco Grand Prix", "Sport", "hard", ["Monaco Grand Prix", "Formula One"], [
 ("Year of the first race", "1929", 1929), ("Laps in the race", "78", 78), ("Times Ayrton Senna won it", "6", 6),
 ("Length of a lap, in km, roughly", "3.3", 3.3), ("Year it joined the Formula One world championship", "1950", 1950)])
game("the numbers of the Ryder Cup", "Sport", "hard", ["Ryder Cup", "golf"], [
 ("Year of the first match", "1927", 1927), ("Players in each team", "12", 12), ("Points up for grabs", "28", 28),
 ("Year GB & Ireland became Team Europe", "1979", 1979), ("Points the holders need to keep the cup", "14", 14)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-43.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
