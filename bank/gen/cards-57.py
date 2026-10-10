# Bank session 10 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-57.json (famous lives). A row of 5-7 cards each:
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

game("the numbers of Mother Teresa", "History", "medium", ["Mother Teresa", "saints"], [
 ("Year she was born", "1910", 1910), ("Year she founded the Missionaries of Charity", "1950", 1950), ("Year she won the Nobel Peace Prize", "1979", 1979),
 ("Her age when she died", "87", 87), ("Year she died", "1997", 1997)])
game("the numbers of Mahatma Gandhi", "History", "medium", ["Gandhi", "India"], [
 ("Year he was born", "1869", 1869), ("Year of his Salt March", "1930", 1930), ("Miles he walked on the Salt March, roughly", "240", 240),
 ("Year India won independence", "1947", 1947), ("His age when he was killed", "78", 78), ("Year he died", "1948", 1948)])
game("the numbers of Rosa Parks", "History", "medium", ["Rosa Parks", "civil rights"], [
 ("Year she was born", "1913", 1913), ("Year she refused to give up her bus seat", "1955", 1955), ("Days the bus boycott that followed lasted", "381", 381),
 ("Her age when she died", "92", 92), ("Year she died", "2005", 2005)])
game("the numbers of Anne Frank", "History", "medium", ["Anne Frank", "Second World War"], [
 ("Year she was born", "1929", 1929), ("Year her family went into hiding", "1942", 1942), ("Days they spent in hiding, roughly", "761", 761),
 ("Her age when she died", "15", 15), ("Year her diary was first published", "1947", 1947)])
game("the numbers of Stephen Hawking", "Science", "medium", ["Stephen Hawking", "scientists"], [
 ("Year he was born", "1942", 1942), ("His age when he was diagnosed with motor neurone disease", "21", 21), ("Year 'A Brief History of Time' came out", "1988", 1988),
 ("His age when he died", "76", 76), ("Year he died", "2018", 2018)])
game("the numbers of Ernest Shackleton", "History", "hard", ["Ernest Shackleton", "explorers", "Antarctica"], [
 ("Year he was born", "1874", 1874), ("Men on his Endurance expedition", "28", 28), ("Year the Endurance set sail", "1914", 1914),
 ("Days his little boat took to reach South Georgia, roughly", "16", 16), ("Year he died", "1922", 1922), ("His age when he died", "47", 47)])
game("the numbers of Lionel Messi", "Football", "medium", ["Lionel Messi", "Argentina", "Barcelona"], [
 ("Year he was born", "1987", 1987), ("Ballon d'Or awards he's won", "8", 8), ("Year he made his Barcelona debut", "2004", 2004),
 ("His goals for Barcelona", "672", 672), ("Year he won the World Cup", "2022", 2022)])
game("the numbers of Cristiano Ronaldo", "Football", "medium", ["Cristiano Ronaldo", "Portugal", "Manchester United"], [
 ("Year he was born", "1985", 1985), ("Ballon d'Or awards he's won", "5", 5), ("Year he joined Manchester United", "2003", 2003),
 ("Year he won his first Ballon d'Or", "2008", 2008), ("Year Portugal won the Euros with him", "2016", 2016)])
game("the numbers of Serena Williams", "Sport", "medium", ["Serena Williams", "tennis"], [
 ("Year she was born", "1981", 1981), ("Grand Slam singles titles she won", "23", 23), ("Year of her first Grand Slam title", "1999", 1999),
 ("Her Olympic gold medals", "4", 4), ("Year she retired", "2022", 2022)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-57.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
