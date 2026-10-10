# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-45.json. A row of 5-7 cards each:
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

game("the numbers of Countdown", "TV", "medium", ["Countdown", "quiz shows"], [
 ("Year it began, as Channel 4's first show", "1982", 1982), ("Seconds on the clock", "30", 30), ("Letters in each letters round", "9", 9),
 ("Biggest possible target in the numbers round", "999", 999), ("Large numbers in the numbers deck", "4", 4)])
game("the numbers of Who Wants to Be a Millionaire?", "TV", "medium", ["Millionaire", "quiz shows"], [
 ("Questions to win the million", "15", 15), ("Lifelines in the original show", "3", 3), ("The first safe haven, in pounds", "1,000", 1000),
 ("The second safe haven, in pounds", "32,000", 32000), ("Year Judith Keppel became the first UK winner", "2000", 2000)])
game("the numbers of The Chase", "TV", "medium", ["The Chase", "quiz shows"], [
 ("Year it began", "2009", 2009), ("Chasers on the show these days", "6", 6), ("Seconds in the Cash Builder", "60", 60),
 ("Players in each team", "4", 4), ("Seconds in the Final Chase", "120", 120)])
game("the numbers of Pointless", "TV", "medium", ["Pointless", "quiz shows"], [
 ("Year it began", "2009", 2009), ("People asked each question", "100", 100), ("Pairs of contestants in each show", "4", 4),
 ("Pounds added to the jackpot each day", "1,000", 1000), ("Year Richard Osman stepped back from co-hosting", "2022", 2022)])
game("the numbers of Mastermind", "TV", "hard", ["Mastermind", "quiz shows"], [
 ("Year it began", "1972", 1972), ("Years Magnus Magnusson hosted it", "25", 25), ("Year John Humphrys took over", "2003", 2003),
 ("Contestants in each show", "4", 4), ("Year Clive Myrie took over", "2021", 2021)])
game("the numbers of University Challenge", "TV", "hard", ["University Challenge", "quiz shows"], [
 ("Year it began", "1962", 1962), ("Players in each team", "4", 4), ("Points for a starter question", "10", 10),
 ("Years Jeremy Paxman hosted it", "29", 29), ("Points for each bonus question", "5", 5)])
game("the numbers of Bullseye", "TV", "medium", ["Bullseye", "game shows"], [
 ("Year it began", "1981", 1981), ("Points for hitting the bull", "50", 50), ("Darts thrown in each turn", "3", 3),
 ("Score needed in the gamble to win the star prize", "101", 101), ("Darts thrown in that gamble", "6", 6)])
game("the numbers of Deal or No Deal", "TV", "medium", ["Deal or No Deal", "game shows"], [
 ("Boxes in play", "22", 22), ("Top prize, in pounds", "250,000", 250000), ("Year it began in the UK", "2005", 2005),
 ("Boxes opened in the first round", "5", 5), ("Smallest amount in a box, in pence", "1", 1)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-45.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
