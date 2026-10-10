# Bank session 10 Oct 2026 : more 20 Questions answers for animals and places (the two thinnest kinds)
# -> bank/twenty-7.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-7.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- animals ----
t("animal", ["Snow leopard"], "medium", "a_mammal a_zoo a_fourlegs a_meat a_stripes a_tail a_asia a_catfam")
t("animal", ["Brown bear", "Grizzly bear", "Grizzly"], "medium", "a_mammal a_bigger a_fourlegs a_meat a_plants a_danger a_hibernate a_zoo a_asia a_americas a_bear")
t("animal", ["Mole"], "medium", "a_mammal a_small a_fourlegs a_meat a_wildbritain")
t("animal", ["Hummingbird"], "medium", "a_bird a_small a_fly a_eggs a_plants a_colourful a_americas")
t("animal", ["Swallow"], "medium", "a_bird a_small a_fly a_eggs a_meat a_wildbritain a_africa a_asia")
t("animal", ["Crow"], "medium", "a_bird a_fly a_eggs a_meat a_plants a_wildbritain a_garden a_africa a_asia a_americas")
t("animal", ["Lobster"], "medium", "a_water a_sea a_meat a_eat a_wildbritain")
t("animal", ["Snail"], "easy", "a_small a_plants a_wildbritain")
t("animal", ["Stingray"], "medium", "a_fish a_water a_sea a_meat a_danger a_venom a_tail")
t("animal", ["Platypus", "Duck-billed platypus"], "medium", "a_mammal a_fourlegs a_water a_meat a_venom a_eggs a_australia")
t("animal", ["Goat"], "easy", "a_mammal a_farm a_fourlegs a_plants a_horns a_hooves a_herd")
t("animal", ["Duck"], "easy", "a_bird a_fly a_swims a_eggs a_farm a_eat a_plants a_water a_wildbritain")
t("animal", ["Mosquito"], "medium", "a_insect a_small a_fly a_danger a_eggs a_wildbritain a_africa a_asia a_australia a_americas")

# ---- places ----
t("place", ["Lisbon"], "medium", "pl_europe pl_city pl_capital pl_sea pl_river pl_club pl_tourist pl_heritage")
t("place", ["Madrid"], "medium", "pl_europe pl_spain pl_city pl_capital pl_bigpop pl_club pl_tourist pl_heritage")
t("place", ["Prague"], "medium", "pl_europe pl_city pl_capital pl_bigpop pl_river pl_tourist pl_heritage")
t("place", ["Moscow"], "medium", "pl_europe pl_city pl_capital pl_bigpop pl_river pl_snow pl_olympics pl_club pl_tourist pl_heritage")
t("place", ["Beijing", "Peking"], "medium", "pl_asia pl_city pl_capital pl_bigpop pl_olympics pl_tourist pl_heritage")
t("place", ["Cairo"], "medium", "pl_africa pl_city pl_capital pl_bigpop pl_river pl_hot pl_tourist pl_heritage")
t("place", ["Hadrian's Wall"], "medium", "pl_uk pl_england pl_north pl_northeast pl_northumberland pl_building pl_old pl_tourist pl_heritage")
t("place", ["Lake Garda"], "medium", "pl_europe pl_italy pl_natural pl_waterfeat pl_tourist")
t("place", ["Hawaii"], "medium", "pl_americas pl_usa pl_oceania pl_region pl_island pl_sea pl_hot pl_english pl_tourist pl_heritage")
t("place", ["Jamaica"], "easy", "pl_americas pl_country pl_island pl_sea pl_hot pl_english pl_tourist pl_heritage")
t("place", ["Florence"], "medium", "pl_europe pl_italy pl_city pl_river pl_club pl_tourist pl_heritage")
t("place", ["Scarborough"], "medium", "pl_uk pl_england pl_north pl_city pl_sea")
t("place", ["Tynemouth"], "medium", "pl_uk pl_england pl_north pl_northeast pl_tyneside pl_city pl_sea pl_river")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
