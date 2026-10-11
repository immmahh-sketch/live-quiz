# Bank session 11 Oct 2026: more 20 Questions answers for places (North East and the wider world)
# -> bank/twenty-17.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-17.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- places ----
t("place", ["Morpeth"], "medium", "pl_uk pl_england pl_northeast pl_north pl_northumberland pl_city pl_river")
t("place", ["Berwick-upon-Tweed", "Berwick"], "medium", "pl_uk pl_england pl_northeast pl_north pl_northumberland pl_city pl_sea pl_river")
t("place", ["Gateshead"], "easy", "pl_uk pl_england pl_northeast pl_north pl_tyneside pl_city pl_river")
t("place", ["Middlesbrough"], "easy", "pl_uk pl_england pl_northeast pl_north pl_city pl_river pl_club")
t("place", ["Darlington"], "medium", "pl_uk pl_england pl_northeast pl_north pl_durham pl_city")
t("place", ["Inverness"], "medium", "pl_uk pl_scotland pl_city pl_river")
t("place", ["Mont Blanc"], "medium", "pl_europe pl_france pl_natural pl_mountain pl_snow pl_tourist")
t("place", ["Seville"], "medium", "pl_europe pl_spain pl_city pl_river pl_hot pl_tourist pl_club")
t("place", ["Kyoto"], "medium", "pl_asia pl_city pl_tourist pl_heritage pl_bigpop")
t("place", ["Table Mountain"], "medium", "pl_africa pl_natural pl_mountain pl_tourist")
t("place", ["Victoria Falls"], "medium", "pl_africa pl_natural pl_waterfeat pl_tourist pl_heritage pl_hot")
t("place", ["Petra"], "hard", "pl_asia pl_building pl_old pl_tourist pl_heritage pl_hot")
t("place", ["The Acropolis", "Acropolis"], "medium", "pl_europe pl_building pl_old pl_tourist pl_heritage pl_hot")
t("place", ["The Tower of London", "Tower of London"], "easy", "pl_uk pl_england pl_london pl_castle pl_building pl_old pl_tourist pl_heritage pl_river")
t("place", ["Westminster Abbey"], "easy", "pl_uk pl_england pl_london pl_religious pl_building pl_old pl_tourist pl_heritage")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-17.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
