# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-68.json (stars of stage, screen and song). A row of 5-7 cards each:
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

game("the numbers of Dame Maggie Smith", "Film", "medium", ["Maggie Smith", "actors"], [
 ("Year she was born", "1934", 1934), ("Oscars she won", "2", 2), ("Year she won her first", "1970", 1970),
 ("Year Downton Abbey began", "2010", 2010), ("Year she died", "2024", 2024)])
game("the numbers of Sir Cliff Richard", "Music", "medium", ["Cliff Richard", "singers"], [
 ("Year he was born", "1940", 1940), ("His UK number ones", "14", 14), ("Year 'Living Doll' went to number one", "1959", 1959),
 ("Year 'Congratulations' came second at Eurovision", "1968", 1968), ("Year he was knighted", "1995", 1995)])
game("the numbers of Dame Barbara Windsor", "TV", "medium", ["Barbara Windsor", "EastEnders", "Carry On"], [
 ("Year she was born", "1937", 1937), ("Carry On films she made", "9", 9), ("Year she first played Peggy Mitchell", "1994", 1994),
 ("Year she became a dame", "2016", 2016), ("Year she died", "2020", 2020)])
game("the numbers of Sir Mick Jagger", "Music", "medium", ["Mick Jagger", "The Rolling Stones"], [
 ("Year he was born", "1943", 1943), ("The Rolling Stones' UK number one singles", "8", 8), ("Year the Stones formed", "1962", 1962),
 ("Year '(I Can't Get No) Satisfaction' came out", "1965", 1965), ("Year he was knighted", "2003", 2003)])
game("the numbers of Sir Ringo Starr", "Music", "medium", ["Ringo Starr", "The Beatles"], [
 ("Year he was born", "1940", 1940), ("His age when he joined the Beatles", "22", 22), ("Year he joined", "1962", 1962),
 ("Year he began narrating Thomas the Tank Engine", "1984", 1984), ("Year he was knighted", "2018", 2018)])
game("the numbers of Ozzy Osbourne", "Music", "medium", ["Ozzy Osbourne", "Black Sabbath"], [
 ("Year he was born", "1948", 1948), ("Studio albums the original Black Sabbath line-up made", "8", 8), ("Year Black Sabbath formed", "1968", 1968),
 ("Year 'The Osbournes' began on MTV", "2002", 2002), ("Year he died", "2025", 2025)])
game("the numbers of Stephen Fry", "TV", "medium", ["Stephen Fry", "QI"], [
 ("Year he was born", "1957", 1957), ("Series of QI he hosted", "13", 13), ("Year Jeeves and Wooster began", "1990", 1990),
 ("Year QI began", "2003", 2003), ("Year he handed QI to Sandi Toksvig", "2016", 2016)])
game("the numbers of David Walliams", "TV", "medium", ["David Walliams", "comedians", "authors"], [
 ("Year he was born", "1971", 1971), ("Miles he swam down the Thames for Sport Relief", "140", 140), ("Year Little Britain began on TV", "2003", 2003),
 ("Year his first children's book came out", "2008", 2008), ("Year he became a Britain's Got Talent judge", "2012", 2012)])
game("the numbers of Dame Joan Collins", "TV", "medium", ["Joan Collins", "actors"], [
 ("Year she was born", "1933", 1933), ("Times she has married", "5", 5), ("Year 'The Stud' came out", "1978", 1978),
 ("Year Dynasty began", "1981", 1981), ("Year she became a dame", "2015", 2015)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-68.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
