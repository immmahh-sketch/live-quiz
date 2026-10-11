# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-72.json (North East stars and sporting greats). A row of 5-7 cards each:
# what's on the card, what it shows when it flips, and the number compared. The numbers zig-zag, no equal neighbours.
# Titles must be new to the bank (the import skips a repeated title as a duplicate).
import json, os
# Sir Ian Botham was dropped after import: an "Ian Botham" game was already live (retired q_c68dfc65).
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    assert len({l for l, _, _ in cards}) == len(cards), (text, 'repeated card')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("the numbers of Ant and Dec", "TV", "medium", ["Ant and Dec", "North East", "TV presenters"], [
 ("Year they were both born", "1975", 1975), ("Year 'Let's Get Ready to Rhumble' finally hit number one", "2013", 2013), ("Year they met on Byker Grove", "1989", 1989),
 ("Year I'm a Celebrity began", "2002", 2002), ("Year 'Let's Get Ready to Rhumble' first came out", "1994", 1994)])
game("the numbers of Cheryl", "Music", "medium", ["Cheryl", "Girls Aloud", "North East"], [
 ("Year she was born", "1983", 1983), ("Her solo UK number ones", "5", 5), ("Year Girls Aloud formed on Popstars: The Rivals", "2002", 2002),
 ("Year 'Fight for This Love' was number one", "2009", 2009), ("Year she joined The X Factor as a judge", "2008", 2008)])
game("the numbers of Mark Knopfler", "Music", "medium", ["Mark Knopfler", "Dire Straits", "North East"], [
 ("Year he was born", "1949", 1949), ("Year 'Brothers in Arms' came out", "1985", 1985), ("Year Dire Straits formed", "1977", 1977),
 ("Year of his Local Hero soundtrack", "1983", 1983), ("Year 'Sultans of Swing' first came out", "1978", 1978)])
game("the numbers of Tom Daley", "Sport", "medium", ["Tom Daley", "diving", "Olympics"], [
 ("Year he was born", "1994", 1994), ("His age at his first Olympics", "14", 14), ("Year of his first Olympics", "2008", 2008),
 ("His Olympic medals in all", "5", 5), ("Year he won Olympic gold, in Tokyo", "2021", 2021)])
game("the numbers of Sir Steve Redgrave", "Sport", "medium", ["Steve Redgrave", "rowing", "Olympics"], [
 ("Year he was born", "1962", 1962), ("His Olympic gold medals", "5", 5), ("Year of his first Olympic gold", "1984", 1984),
 ("Year he was knighted", "2001", 2001), ("Year of his last Olympic gold", "2000", 2000)])
game("the numbers of Phil Taylor", "Sport", "medium", ["Phil Taylor", "darts"], [
 ("Year he was born", "1960", 1960), ("His world titles", "16", 16), ("Year of his first world title", "1990", 1990),
 ("Year he retired", "2018", 2018), ("Year of his last world title", "2013", 2013)])
game("the numbers of Michael Schumacher", "Sport", "medium", ["Michael Schumacher", "Formula One"], [
 ("Year he was born", "1969", 1969), ("His world titles", "7", 7), ("Year of his first world title", "1994", 1994),
 ("His Grand Prix wins", "91", 91), ("Year of his skiing accident", "2013", 2013)])
game("the numbers of Nigel Mansell", "Sport", "medium", ["Nigel Mansell", "Formula One"], [
 ("Year he was born", "1953", 1953), ("His Grand Prix wins", "31", 31), ("Year he became world champion", "1992", 1992),
 ("Year he made his F1 debut", "1980", 1980), ("Year he won the IndyCar title", "1993", 1993)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-72.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
