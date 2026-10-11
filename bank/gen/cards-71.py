# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-71.json (TV cooks, TV presenters, Rod Stewart and two Newcastle legends). A row of 5-7 cards each:
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

game("the numbers of Gordon Ramsay", "TV", "medium", ["Gordon Ramsay", "TV cooks"], [
 ("Year he was born", "1966", 1966), ("His children", "6", 6), ("Year Restaurant Gordon Ramsay opened in Chelsea", "1998", 1998),
 ("Michelin stars that restaurant holds", "3", 3), ("Year Ramsay's Kitchen Nightmares began", "2004", 2004)])
game("the numbers of Nigella Lawson", "TV", "medium", ["Nigella Lawson", "TV cooks"], [
 ("Year she was born", "1960", 1960), ("Her children", "2", 2), ("Year 'How to Eat' came out", "1998", 1998),
 ("Year her father Nigel became Chancellor", "1983", 1983), ("Year 'How to Be a Domestic Goddess' came out", "2000", 2000)])
game("the numbers of Keith Floyd", "TV", "medium", ["Keith Floyd", "TV cooks"], [
 ("Year he was born", "1943", 1943), ("Times he married", "4", 4), ("Year 'Floyd on Fish' began", "1985", 1985),
 ("His age when he died", "65", 65), ("Year he died", "2009", 2009)])
game("the numbers of the Hairy Bikers", "TV", "medium", ["Hairy Bikers", "TV cooks", "North East"], [
 ("Year Dave Myers was born", "1957", 1957), ("Bikers in the duo", "2", 2), ("Year their first BBC series began", "2004", 2004),
 ("Year Si King was born", "1967", 1967), ("Year Dave Myers died", "2024", 2024)])
game("the numbers of Sir Rod Stewart", "Music", "medium", ["Rod Stewart", "rock"], [
 ("Year he was born", "1945", 1945), ("His children", "8", 8), ("Year 'Maggie May' was number one", "1971", 1971),
 ("Year he was knighted", "2016", 2016), ("Year 'Sailing' was number one", "1975", 1975)])
game("the numbers of Sir Terry Wogan", "TV", "medium", ["Terry Wogan", "TV presenters", "Eurovision"], [
 ("Year he was born", "1938", 1938), ("Chart peak of his 'Floral Dance'", "21", 21), ("Year he began hosting Blankety Blank", "1979", 1979),
 ("Year of his last Eurovision commentary", "2008", 2008), ("Year he first fronted Children in Need", "1980", 1980)])
game("the numbers of Jeremy Clarkson", "TV", "medium", ["Jeremy Clarkson", "Top Gear"], [
 ("Year he was born", "1960", 1960), ("Year Clarkson's Farm began", "2021", 2021), ("Year the relaunched Top Gear began", "2002", 2002),
 ("Year he began hosting Who Wants to Be a Millionaire?", "2018", 2018), ("Year he left Top Gear", "2015", 2015)])
game("the numbers of Shay Given", "Football", "medium", ["Shay Given", "Newcastle United", "Ireland"], [
 ("Year he was born", "1976", 1976), ("His Republic of Ireland caps", "134", 134), ("Year he joined Newcastle", "1997", 1997),
 ("Year he played at the World Cup", "2002", 2002), ("Year he left for Manchester City", "2009", 2009)])
game("the numbers of Malcolm Macdonald", "Football", "medium", ["Malcolm Macdonald", "Supermac", "Newcastle United"], [
 ("Year he was born", "1950", 1950), ("Goals he scored for England against Cyprus in one game", "5", 5), ("Year he joined Newcastle", "1971", 1971),
 ("His England caps", "14", 14), ("Year he left for Arsenal", "1976", 1976)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-71.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
