# Bank session 9 Oct 2026 (fourth pass): more 20 Questions answers for brands, titles, places, food and objects
# -> bank/twenty-5.json, several for Christmas. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-5.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- brands ----
t("brand", ["Audi"], "easy", "b_cars b_german b_old")
t("brand", ["Lamborghini"], "medium", "b_cars b_logo b_person b_luxury b_sportscar")
t("brand", ["Thorntons"], "medium", "b_food b_shop b_uk b_old b_person b_sweets")
t("brand", ["Haribo"], "medium", "b_food b_german b_old b_sweets")
t("brand", ["NatWest"], "easy", "b_bank b_uk b_highstreet")
t("brand", ["Halifax"], "medium", "b_bank b_uk b_old b_highstreet")
t("brand", ["PlayStation"], "easy", "b_tech b_japanese b_games")
t("brand", ["Fred Perry"], "medium", "b_clothes b_sport b_uk b_person")
t("brand", ["Dyson"], "medium", "b_tech b_uk b_person")

# ---- films, TV, books and songs ----
t("title", ["Elf"], "easy", "t_film t_e_00 t_american t_comedy t_christmas")
t("title", ["It's a Wonderful Life"], "medium", "t_film t_e_old t_american t_christmas")
t("title", ["Die Hard"], "medium", "t_film t_e_80 t_american t_series t_christmas t_crime")
t("title", ["Strictly Come Dancing", "Strictly"], "easy", "t_tv t_e_00 t_british t_bbc t_running t_long")
t("title", ["Match of the Day"], "easy", "t_tv t_e_old t_british t_sport t_bbc t_running t_long")
t("title", ["Blue Peter"], "easy", "t_tv t_e_old t_british t_kids t_bbc t_running t_long")
t("title", ["Friends"], "easy", "t_tv t_e_90 t_american t_comedy t_sitcom")
t("title", ["Stranger Things"], "easy", "t_tv t_e_10 t_american t_scary t_scifi t_drama t_netflix")
t("title", ["White Christmas"], "medium", "t_song t_e_old t_american t_christmas t_male t_slow t_filmsong")
t("title", ["Merry Xmas Everybody"], "easy", "t_song t_e_70 t_british t_christmas t_number1 t_xmas1 t_band t_male")
t("title", ["Charlie and the Chocolate Factory"], "easy", "t_book t_e_old t_british t_kids t_series t_named t_novel")
t("title", ["A Christmas Carol"], "easy", "t_book t_e_old t_british t_christmas t_novel t_classic")

# ---- places ----
t("place", ["Lapland"], "medium", "pl_europe pl_region pl_snow pl_tourist")
t("place", ["Bethlehem"], "medium", "pl_asia pl_city pl_hot pl_tourist pl_heritage")
t("place", ["Durham"], "easy", "pl_uk pl_england pl_northeast pl_north pl_durham pl_city pl_river pl_tourist pl_heritage")
t("place", ["Alnwick Castle"], "medium", "pl_uk pl_england pl_northeast pl_north pl_northumberland pl_building pl_castle pl_old pl_river pl_tourist")
t("place", ["Sunderland"], "easy", "pl_uk pl_england pl_northeast pl_north pl_sunderland pl_city pl_club pl_sea pl_river")
t("place", ["Newcastle upon Tyne", "Newcastle"], "easy", "pl_uk pl_england pl_northeast pl_north pl_tyneside pl_city pl_club pl_river pl_tourist")
t("place", ["London"], "easy", "pl_uk pl_england pl_london pl_city pl_capital pl_bigpop pl_olympics pl_club pl_river pl_tourist pl_heritage")
t("place", ["Scotland"], "easy", "pl_uk pl_scotland pl_country pl_bigpop pl_sea pl_snow pl_tourist pl_heritage")
t("place", ["Wales"], "easy", "pl_uk pl_wales pl_country pl_bigpop pl_sea pl_tourist pl_heritage")
t("place", ["New Zealand"], "easy", "pl_oceania pl_country pl_bigpop pl_english pl_island pl_sea pl_tourist pl_heritage")
t("place", ["The Alps", "Alps"], "easy", "pl_europe pl_natural pl_mountain pl_snow pl_tourist")
t("place", ["Athens"], "easy", "pl_europe pl_city pl_capital pl_olympics pl_club pl_hot pl_tourist pl_heritage")

# ---- food and drink ----
t("food", ["Brussels sprouts", "Sprouts"], "easy", "f_hot f_fruitveg f_christmas")
t("food", ["Roast turkey", "Turkey"], "easy", "f_hot f_meat f_christmas f_british")
t("food", ["Yule log", "Bûche de Noël"], "medium", "f_sweet f_chocolate f_cake f_christmas f_french")
t("food", ["Sherry"], "medium", "f_drink f_alcohol f_wine")
t("food", ["Pigs in blankets"], "easy", "f_hot f_meat f_pork f_christmas f_british")
t("food", ["Christmas cake"], "easy", "f_sweet f_cake f_christmas f_british")
t("food", ["Cranberry sauce"], "medium", "f_sweet f_christmas")
t("food", ["Tomato"], "easy", "f_fruitveg f_fruit f_raw f_round")
t("food", ["Potato"], "easy", "f_fruitveg f_potato")
t("food", ["Chips"], "easy", "f_hot f_potato f_fried f_takeaway f_british")
t("food", ["Gingerbread man"], "easy", "f_sweet f_cake f_hands f_christmas")
t("food", ["Cider"], "easy", "f_drink f_alcohol f_beer f_fizzy f_british")

# ---- objects ----
t("object", ["Christmas cracker", "Cracker"], "easy", "o_home o_paper o_sound")
t("object", ["Bauble", "Christmas bauble"], "easy", "o_home o_pocket o_glass o_round")
t("object", ["Kettle"], "easy", "o_home o_kitchen o_electric o_plug")
t("object", ["Washing machine"], "easy", "o_clean o_home o_electric o_plug o_moving o_sound")
t("object", ["Hairdryer", "Hair dryer"], "easy", "o_home o_electric o_plug o_hold o_plastic o_moving o_sound")
t("object", ["Sewing machine"], "medium", "o_tool o_home o_electric o_metal o_old o_moving o_sharp")
t("object", ["Spade"], "easy", "o_tool o_garden o_hold o_metal o_old")
t("object", ["Sailing boat", "Yacht", "Sailboat"], "easy", "o_vehicle o_heavy o_old o_moving o_boat")
t("object", ["Roller skates", "Rollerskates"], "easy", "o_wear o_old o_wheels o_moving o_feet")
t("object", ["Calculator"], "easy", "o_office o_electric o_screen o_pocket o_hold o_plastic")
t("object", ["Sleigh", "Sledge"], "medium", "o_vehicle o_wood o_old o_moving")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(B), 'items:', dict(Counter(x['what'] for x in B)))
