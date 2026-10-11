# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-66.json (singers and screen legends). A row of 5-7 cards each:
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

game("the numbers of Kate Bush", "Music", "medium", ["Kate Bush", "singers"], [
 ("Year she was born", "1958", 1958), ("Her age when 'Wuthering Heights' went to number one", "19", 19), ("Year it went to number one", "1978", 1978),
 ("Her studio albums", "10", 10), ("Year 'Running Up That Hill' finally reached number one", "2022", 2022)])
game("the numbers of Sir Billy Connolly", "TV", "medium", ["Billy Connolly", "comedians", "Scotland"], [
 ("Year he was born", "1942", 1942), ("Times he appeared on Parkinson", "15", 15), ("Year 'Mrs Brown' came out", "1997", 1997),
 ("Year he revealed he had Parkinson's", "2013", 2013), ("Year he was knighted", "2017", 2017)])
game("the numbers of Sir Bruce Forsyth", "TV", "medium", ["Bruce Forsyth", "presenters"], [
 ("Year he was born", "1928", 1928), ("Years his TV career spanned, a world record", "75", 75), ("Year he began hosting The Generation Game", "1971", 1971),
 ("Year he began hosting Strictly", "2004", 2004), ("Year he died", "2017", 2017)])
game("the numbers of Cilla Black", "Music", "medium", ["Cilla Black", "Liverpool", "TV"], [
 ("Year she was born", "1943", 1943), ("Her UK number ones", "2", 2), ("Year 'Anyone Who Had a Heart' went to number one", "1964", 1964),
 ("Year Blind Date began", "1985", 1985), ("Year she died", "2015", 2015)])
game("the numbers of Amy Winehouse", "Music", "medium", ["Amy Winehouse", "singers"], [
 ("Year she was born", "1983", 1983), ("Grammys she won on one night in 2008", "5", 5), ("Year 'Back to Black' came out", "2006", 2006),
 ("Her age when she died", "27", 27), ("Year she died", "2011", 2011)])
game("the numbers of Stevie Wonder", "Music", "medium", ["Stevie Wonder", "Motown"], [
 ("Year he was born", "1950", 1950), ("His age when 'Fingertips' topped the US charts", "13", 13), ("Year of that first hit", "1963", 1963),
 ("Grammy Awards he's won", "25", 25), ("Year 'I Just Called to Say I Love You' came out", "1984", 1984)])
game("the numbers of Tina Turner", "Music", "medium", ["Tina Turner", "singers"], [
 ("Year she was born", "1939", 1939), ("Her age when 'Private Dancer' came out", "44", 44), ("Year 'Private Dancer' came out", "1984", 1984),
 ("Year 'The Best' came out", "1989", 1989), ("Year she died", "2023", 2023)])
game("the numbers of Sir Michael Caine", "Film", "medium", ["Michael Caine", "actors"], [
 ("Year he was born", "1933", 1933), ("Oscars he won", "2", 2), ("Year 'Alfie' came out", "1966", 1966),
 ("Year 'The Italian Job' came out", "1969", 1969), ("Year he was knighted", "2000", 2000)])
game("the numbers of Dame Judi Dench", "Film", "medium", ["Judi Dench", "actors"], [
 ("Year she was born", "1934", 1934), ("Minutes she's on screen in her Oscar-winning role, roughly", "8", 8), ("Year she became a dame", "1988", 1988),
 ("Year she first played M", "1995", 1995), ("Year she won her Oscar", "1999", 1999)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-66.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
