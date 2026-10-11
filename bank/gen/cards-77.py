# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-77.json (sporting greats and pop divas). A row of 5-7 cards each:
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

game("the numbers of Amir Khan", "Sport", "medium", ["Amir Khan", "boxing", "Bolton"], [
 ("Year he was born", "1986", 1986), ("His age when he won Olympic silver", "17", 17), ("Year of that Olympic silver", "2004", 2004),
 ("Year he retired", "2022", 2022), ("Year he first became world champion", "2009", 2009)])
game("the numbers of Steve Ovett", "Sport", "medium", ["Steve Ovett", "athletics", "Olympics"], [
 ("Year he was born", "1955", 1955), ("Olympic golds he won", "1", 1), ("Year he won Olympic 800 m gold", "1980", 1980),
 ("His age at the Moscow Olympics", "24", 24), ("Year of his last Olympics", "1984", 1984)])
game("the numbers of Denise Lewis", "Sport", "medium", ["Denise Lewis", "heptathlon", "Olympics"], [
 ("Year she was born", "1972", 1972), ("Year she won Olympic heptathlon gold", "2000", 2000), ("Year of her first Commonwealth gold", "1994", 1994),
 ("Her winning points total in Sydney", "6,584", 6584), ("Year she was on Strictly", "2008", 2008)])
game("the numbers of Chris Froome", "Sport", "medium", ["Chris Froome", "cycling", "Tour de France"], [
 ("Year he was born", "1985", 1985), ("Tour de France titles he won", "4", 4), ("Year of his first Tour win", "2013", 2013),
 ("Year of his career-changing crash", "2019", 2019), ("Year of his last Tour win", "2017", 2017)])
game("the numbers of Frankie Dettori", "Sport", "medium", ["Frankie Dettori", "horse racing"], [
 ("Year he was born", "1970", 1970), ("Winners he rode on one day at Ascot", "7", 7), ("Year of his 'Magnificent Seven'", "1996", 1996),
 ("Derby winners he rode", "2", 2), ("Year of his first Derby win", "2007", 2007)])
game("the numbers of Lady Gaga", "Music", "medium", ["Lady Gaga", "pop"], [
 ("Year she was born", "1986", 1986), ("Year she played the Super Bowl half-time show", "2017", 2017), ("Year 'Just Dance' came out", "2008", 2008),
 ("Year 'Shallow' won the Oscar", "2019", 2019), ("Year A Star Is Born came out", "2018", 2018)])
game("the numbers of Rihanna", "Music", "medium", ["Rihanna", "pop", "Barbados"], [
 ("Year she was born", "1988", 1988), ("Weeks 'Umbrella' spent at UK number one", "10", 10), ("Year 'Umbrella' came out", "2007", 2007),
 ("Year she headlined the Super Bowl half-time show", "2023", 2023), ("Year she launched Fenty Beauty", "2017", 2017)])
game("the numbers of Celine Dion", "Music", "medium", ["Celine Dion", "pop", "Canada"], [
 ("Year she was born", "1968", 1968), ("Her older brothers and sisters", "13", 13), ("Year she won Eurovision for Switzerland", "1988", 1988),
 ("Year she sang at the Paris Olympics opening", "2024", 2024), ("Year 'My Heart Will Go On' topped the UK chart", "1998", 1998)])
game("the numbers of Annie Lennox", "Music", "medium", ["Annie Lennox", "Eurythmics", "Scotland"], [
 ("Year she was born", "1954", 1954), ("Year 'Sweet Dreams' came out", "1983", 1983), ("Year Eurythmics formed", "1980", 1980),
 ("Year she won an Oscar", "2004", 2004), ("Year her solo album Diva came out", "1992", 1992)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-77.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
