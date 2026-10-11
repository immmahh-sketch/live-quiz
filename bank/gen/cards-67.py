# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-67.json (screen legends). A row of 5-7 cards each:
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

game("the numbers of Sir Ian McKellen", "Film", "medium", ["Ian McKellen", "actors"], [
 ("Year he was born", "1939", 1939), ("Films he played Gandalf in", "6", 6), ("Year he was knighted", "1991", 1991),
 ("Year 'The Fellowship of the Ring' came out", "2001", 2001), ("Year the first X-Men film came out", "2000", 2000)])
game("the numbers of Dame Helen Mirren", "Film", "medium", ["Helen Mirren", "actors"], [
 ("Year she was born", "1945", 1945), ("Year Prime Suspect began", "1991", 1991), ("Year she became a dame", "2003", 2003),
 ("Oscars she's won", "1", 1), ("Year 'The Queen' came out", "2006", 2006)])
game("the numbers of Joanna Lumley", "TV", "medium", ["Joanna Lumley", "actors"], [
 ("Year she was born", "1946", 1946), ("Year she played Purdey in The New Avengers", "1976", 1976), ("Year Absolutely Fabulous began", "1992", 1992),
 ("Year she won the Gurkhas the right to settle in Britain", "2009", 2009), ("Year she became a dame", "2022", 2022)])
game("the numbers of Sir Patrick Stewart", "TV", "medium", ["Patrick Stewart", "actors", "Star Trek"], [
 ("Year he was born", "1940", 1940), ("Year Star Trek: The Next Generation began", "1987", 1987), ("Seasons of that show", "7", 7),
 ("Year he first played Professor X", "2000", 2000), ("Year he was knighted", "2010", 2010)])
game("the numbers of Sir Anthony Hopkins", "Film", "medium", ["Anthony Hopkins", "actors", "Wales"], [
 ("Year he was born", "1937", 1937), ("Oscars he's won", "2", 2), ("Year 'The Silence of the Lambs' came out", "1991", 1991),
 ("Year he was knighted", "1993", 1993), ("Year he won his second Oscar", "2021", 2021)])
game("the numbers of Sir Sean Connery", "Film", "medium", ["Sean Connery", "James Bond", "Scotland"], [
 ("Year he was born", "1930", 1930), ("Official Bond films he made", "6", 6), ("Year 'Dr. No' came out", "1962", 1962),
 ("Year he won his Oscar", "1988", 1988), ("Year he was knighted", "2000", 2000)])
game("the numbers of Sir Roger Moore", "Film", "medium", ["Roger Moore", "James Bond"], [
 ("Year he was born", "1927", 1927), ("Bond films he made", "7", 7), ("Year 'The Saint' began on TV", "1962", 1962),
 ("Year of his first Bond film", "1973", 1973), ("His age in his last Bond film", "57", 57)])
game("the numbers of Daniel Craig", "Film", "medium", ["Daniel Craig", "James Bond"], [
 ("Year he was born", "1968", 1968), ("Bond films he made", "5", 5), ("Year 'Casino Royale' came out", "2006", 2006),
 ("His age when it came out", "38", 38), ("Year 'No Time to Die' came out", "2021", 2021)])
game("the numbers of Sir Lenny Henry", "TV", "medium", ["Lenny Henry", "comedians", "Comic Relief"], [
 ("Year he was born", "1958", 1958), ("His age when he won New Faces", "16", 16), ("Year he co-founded Comic Relief", "1985", 1985),
 ("Year he was knighted", "2015", 2015), ("Year he stepped back from hosting Red Nose Day", "2023", 2023)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-67.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
