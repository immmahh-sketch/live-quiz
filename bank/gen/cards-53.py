# Bank session 10 Oct 2026: 10 more Play Your Cards Right games -> bank/cards-53.json (famous lives, North East heroes). A row of 5-7 cards each:
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

game("the numbers of Alan Shearer", "Football", "medium", ["Alan Shearer", "Newcastle United", "North East"], [
 ("Year he was born", "1970", 1970), ("His Premier League goals", "260", 260), ("His England caps", "63", 63),
 ("His Newcastle goals in all competitions", "206", 206), ("His England goals", "30", 30), ("Year he joined Newcastle", "1996", 1996)])
game("the numbers of Kevin Keegan", "Football", "medium", ["Kevin Keegan", "Newcastle United", "North East"], [
 ("Year he was born", "1951", 1951), ("Times he was European Footballer of the Year", "2", 2), ("Year he joined Newcastle as a player", "1982", 1982),
 ("His England caps", "63", 63), ("Year he first became Newcastle manager", "1992", 1992), ("Points Newcastle led the league by in January 1996", "12", 12)])
game("the numbers of Paul Gascoigne", "Football", "medium", ["Paul Gascoigne", "Gazza", "North East"], [
 ("Year he was born, in Gateshead", "1967", 1967), ("His England caps", "57", 57), ("Year he joined Tottenham", "1988", 1988),
 ("His England goals", "10", 10), ("Year of his tears at the World Cup", "1990", 1990), ("Year of his famous goal against Scotland", "1996", 1996)])
game("the numbers of Napoleon", "History", "medium", ["Napoleon", "France"], [
 ("Year he was born", "1769", 1769), ("Year he crowned himself emperor", "1804", 1804), ("Year of the Battle of Waterloo", "1815", 1815),
 ("Years he spent exiled on St Helena, roughly", "6", 6), ("Year he died", "1821", 1821), ("His age when he died", "51", 51)])
game("the numbers of Christopher Columbus", "History", "medium", ["Christopher Columbus", "explorers"], [
 ("Year he was born, roughly", "1451", 1451), ("Ships on his first voyage", "3", 3), ("Year he first reached the Americas", "1492", 1492),
 ("Voyages he made across the Atlantic", "4", 4), ("Year he died", "1506", 1506), ("Days his first crossing took from the Canary Islands", "36", 36)])
game("the numbers of Horatio Nelson", "History", "medium", ["Horatio Nelson", "Royal Navy"], [
 ("Year he was born", "1758", 1758), ("His age when he joined the navy", "12", 12), ("Year he lost his right arm", "1797", 1797),
 ("His age when he died", "47", 47), ("Year of the Battle of Trafalgar", "1805", 1805), ("Height of Nelson's Column in metres, roughly", "52", 52)])
game("the numbers of David Bowie", "Music", "medium", ["David Bowie", "pop stars"], [
 ("Year he was born", "1947", 1947), ("Year 'Space Oddity' came out", "1969", 1969), ("His age when he died", "69", 69),
 ("Year 'Let's Dance' came out", "1983", 1983), ("Year he died", "2016", 2016)])
game("the numbers of Captain Scott", "History", "hard", ["Captain Scott", "explorers", "Antarctica"], [
 ("Year he was born", "1868", 1868), ("Men in his South Pole party", "5", 5), ("Year he set sail on the Terra Nova", "1910", 1910),
 ("Days after Amundsen that he reached the Pole", "34", 34), ("Year he reached the Pole", "1912", 1912), ("His age when he died", "43", 43)])
game("the numbers of Isambard Kingdom Brunel", "History", "hard", ["Isambard Kingdom Brunel", "engineers"], [
 ("Year he was born", "1806", 1806), ("Miles of his Great Western Railway, London to Bristol, roughly", "118", 118), ("Year his SS Great Britain was launched", "1843", 1843),
 ("His age when he died", "53", 53), ("Year his Clifton Suspension Bridge finally opened", "1864", 1864)])
game("the numbers of George Stephenson", "North East England", "hard", ["George Stephenson", "railways", "North East"], [
 ("Year he was born, in Wylam", "1781", 1781), ("Year the Stockton and Darlington Railway opened", "1825", 1825), ("Miles of that first line, roughly", "26", 26),
 ("Year Rocket won the Rainhill Trials", "1829", 1829), ("Rocket's top speed in mph, roughly", "30", 30), ("Year he died", "1848", 1848)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-53.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
