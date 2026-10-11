# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-76.json (pop and rock stars, bands and Gareth Bale). A row of 5-7 cards each:
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

game("the numbers of Gary Barlow", "Music", "medium", ["Gary Barlow", "Take That"], [
 ("Year he was born", "1971", 1971), ("Take That's UK number ones", "12", 12), ("Year Take That formed", "1990", 1990),
 ("Year his solo number one 'Forever Love' came out", "1996", 1996), ("Year he became an X Factor judge", "2011", 2011)])
game("the numbers of Phil Collins", "Music", "medium", ["Phil Collins", "Genesis"], [
 ("Year he was born", "1951", 1951), ("Year 'In the Air Tonight' came out", "1981", 1981), ("Year he joined Genesis", "1970", 1970),
 ("Year he played Live Aid on both sides of the Atlantic", "1985", 1985), ("Year Disney's Tarzan, with his Oscar-winning song, came out", "1999", 1999)])
game("the numbers of George Michael", "Music", "medium", ["George Michael", "Wham!"], [
 ("Year he was born", "1963", 1963), ("Year 'Careless Whisper' came out", "1984", 1984), ("Year Wham! formed", "1981", 1981),
 ("Year he died", "2016", 2016), ("Year his album Faith came out", "1987", 1987)])
game("the numbers of Bon Jovi", "Music", "medium", ["Bon Jovi", "rock"], [
 ("Year Jon Bon Jovi was born", "1962", 1962), ("Year the band formed", "1983", 1983), ("Year 'It's My Life' came out", "2000", 2000),
 ("Year 'Slippery When Wet' came out", "1986", 1986), ("Year 'Always' came out", "1994", 1994)])
game("the numbers of Bruce Springsteen", "Music", "medium", ["Bruce Springsteen", "rock"], [
 ("Year he was born", "1949", 1949), ("His Grammy awards", "20", 20), ("Year 'Born to Run' came out", "1975", 1975),
 ("Year 'Born in the U.S.A.' came out", "1984", 1984), ("Year the E Street Band formed", "1972", 1972)])
game("the numbers of Whitney Houston", "Music", "medium", ["Whitney Houston", "pop"], [
 ("Year she was born", "1963", 1963), ("Weeks 'I Will Always Love You' spent at UK number one", "10", 10), ("Year her first album came out", "1985", 1985),
 ("Year she died", "2012", 2012), ("Year The Bodyguard came out", "1992", 1992)])
game("the numbers of Blur", "Music", "medium", ["Blur", "Britpop"], [
 ("Year Damon Albarn was born", "1968", 1968), ("Members of the band", "4", 4), ("Year Parklife came out", "1994", 1994),
 ("Year they played two nights at Wembley Stadium", "2023", 2023), ("Year 'Country House' beat Oasis to number one", "1995", 1995)])
game("the numbers of U2", "Music", "medium", ["U2", "rock", "Ireland"], [
 ("Year they formed in Dublin", "1976", 1976), ("Their Grammy awards", "22", 22), ("Year The Joshua Tree came out", "1987", 1987),
 ("Year they played Live Aid", "1985", 1985), ("Year Achtung Baby came out", "1991", 1991)])
game("the numbers of Gareth Bale", "Football", "medium", ["Gareth Bale", "Wales", "Real Madrid"], [
 ("Year he was born", "1989", 1989), ("Champions League titles he won", "5", 5), ("Year he joined Real Madrid", "2013", 2013),
 ("His Wales caps", "111", 111), ("Year he retired", "2023", 2023)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-76.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
