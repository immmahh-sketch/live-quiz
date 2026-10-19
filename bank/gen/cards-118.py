# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-118.json (Neighbours, Casualty, the Isle of Skye).
# Probed against every cards game in the live bank first (soaps appear only in 'year each ended' and 'legend first appeared' games;
# no Casualty or Skye games). Numbers are the commonly quoted ones.
# A row of 5-7 cards each: what's on the card, what it shows when it flips, and the number compared. No equal neighbours.
import json, os
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    assert len({l for l, _, _ in cards}) == len(cards), (text, 'repeated card')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("the numbers of Neighbours", "Television", "medium", ["Neighbours", "soaps"], [
 ("Year it began", "1985", 1985), ("Years Stefan Dennis had played Paul Robinson by 2022", "37", 37), ("Year Scott and Charlene married", "1987", 1987),
 ("Year it moved to Channel 5 in the UK", "2008", 2008), ("Year of the 'final' episode before the revival", "2022", 2022)])
game("the numbers of Casualty", "Television", "hard", ["Casualty", "TV drama", "BBC"], [
 ("Year it began", "1986", 1986), ("Anniversary it marked in 2016", "30th", 30), ("Year its spin-off Holby City began", "1999", 1999),
 ("Year it moved its filming to Cardiff", "2011", 2011), ("Year the police spin-off Holby Blue began", "2007", 2007)])
game("the numbers of the Isle of Skye", "Geography", "hard", ["Skye", "Scotland", "islands"], [
 ("Area in square km, roughly", "1,656", 1656), ("Year the Skye Bridge opened", "1995", 1995), ("Height in metres of its highest peak, Sgùrr Alasdair", "992", 992),
 ("Munros in the Cuillin, roughly", "12", 12), ("People who live there, roughly", "10,000", 10000)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-118.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
