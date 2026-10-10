# Bank session 10 Oct 2026: more 20 Questions answers for food and places (now the two thinnest kinds)
# -> bank/twenty-10.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-10.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- food and drink ----
t("food", ["Espresso"], "easy", "f_drink f_hotdrink f_caffeine f_italian")
t("food", ["Piña colada", "Pina colada"], "medium", "f_drink f_alcohol f_cocktail f_sweet")
t("food", ["Avocado"], "medium", "f_fruitveg f_fruit f_tropical f_raw")
t("food", ["Onion"], "medium", "f_fruitveg f_round")
t("food", ["Bangers and mash", "Sausage and mash"], "easy", "f_meat f_pork f_potato f_hot f_british")
t("food", ["Macaroni cheese", "Mac and cheese"], "easy", "f_rice f_cheese f_dairy f_hot")
t("food", ["Burrito"], "medium", "f_mexican f_hands f_rice f_hot f_meat")
t("food", ["Croque monsieur"], "hard", "f_french f_bread f_cheese f_dairy f_pork f_meat f_hot")
t("food", ["Spaghetti carbonara", "Carbonara"], "medium", "f_italian f_rice f_egg f_cheese f_dairy f_pork f_meat f_hot")
t("food", ["Onion bhaji"], "medium", "f_indian f_fried f_hot f_snack f_takeaway f_hands")
t("food", ["Bourbon biscuit", "Bourbon"], "medium", "f_sweet f_chocolate f_cake f_british f_hands f_snack")
t("food", ["Kipper", "Kippers"], "medium", "f_meat f_fish f_breakfast f_british f_hot")
t("food", ["Hash brown", "Hash browns"], "medium", "f_potato f_fried f_breakfast f_hot")
t("food", ["Prawn cocktail"], "medium", "f_meat f_fish f_british")
t("food", ["Mushy peas"], "easy", "f_fruitveg f_hot f_british")
t("food", ["Cheesecake"], "easy", "f_sweet f_cake f_dairy f_cheese")

# ---- places ----
t("place", ["Hexham"], "hard", "pl_uk pl_england pl_northeast pl_northumberland pl_city pl_river")
t("place", ["Seaham"], "medium", "pl_uk pl_england pl_northeast pl_durham pl_city pl_sea")
t("place", ["Whitley Bay"], "easy", "pl_uk pl_england pl_northeast pl_tyneside pl_city pl_sea")
t("place", ["Penshaw Monument"], "medium", "pl_uk pl_england pl_northeast pl_sunderland pl_building")
t("place", ["Beamish Museum", "Beamish"], "easy", "pl_uk pl_england pl_northeast pl_durham pl_building pl_tourist")
t("place", ["The Cheviot", "Cheviot"], "hard", "pl_uk pl_england pl_northeast pl_northumberland pl_natural pl_mountain")
t("place", ["Vienna"], "medium", "pl_europe pl_city pl_capital pl_bigpop pl_river pl_tourist")
t("place", ["Dublin"], "easy", "pl_europe pl_city pl_capital pl_english pl_river pl_sea pl_tourist")
t("place", ["Toronto"], "medium", "pl_americas pl_canada pl_city pl_bigpop pl_english")
t("place", ["Mexico"], "easy", "pl_americas pl_country pl_bigpop pl_hot pl_olympics pl_sea")
t("place", ["The Sagrada Família", "Sagrada Familia", "Sagrada Família"], "medium", "pl_europe pl_spain pl_building pl_religious pl_tall pl_tourist pl_heritage")
t("place", ["The Leaning Tower of Pisa", "Leaning Tower of Pisa"], "easy", "pl_europe pl_italy pl_building pl_old pl_tourist pl_heritage")
t("place", ["Greece"], "easy", "pl_europe pl_country pl_hot pl_sea pl_olympics pl_bigpop pl_tourist")
t("place", ["Singapore"], "medium", "pl_asia pl_country pl_island pl_hot pl_bigpop pl_english pl_sea")
t("place", ["Old Trafford"], "easy", "pl_uk pl_england pl_north pl_building pl_stadium")
t("place", ["Cambridge"], "easy", "pl_uk pl_england pl_city pl_river pl_tourist")
t("place", ["Morocco"], "medium", "pl_africa pl_country pl_hot pl_bigpop pl_sea pl_tourist")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
