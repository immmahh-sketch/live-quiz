# Bank session 9 Oct 2026 (second pass): more 20 Questions answers for the thinnest kinds -> bank/twenty-3.json.
# Each item lists only the questions whose true answer is Yes; everything else is No. Ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-3.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- animals ----
t("animal", ["Cow"], "easy", "a_mammal a_farm a_bigger a_fourlegs a_plants a_horns a_tail a_herd a_eat a_africa a_asia a_australia a_americas a_hooves")
t("animal", ["Chicken", "Hen"], "easy", "a_bird a_farm a_meat a_plants a_eggs a_eat a_africa a_asia a_australia a_americas")
t("animal", ["Goldfish"], "easy", "a_fish a_pet a_small a_water a_plants a_eggs a_asia")
t("animal", ["Wasp"], "easy", "a_insect a_wildbritain a_small a_fly a_meat a_plants a_stripes a_herd a_eggs a_hibernate a_africa a_asia a_australia a_americas a_sting")
t("animal", ["Salmon"], "medium", "a_fish a_wildbritain a_water a_sea a_meat a_eggs a_eat a_asia a_americas")
t("animal", ["Seal"], "easy", "a_mammal a_wildbritain a_zoo a_water a_sea a_meat a_africa a_asia a_australia a_americas a_whale")
t("animal", ["Killer whale", "Orca"], "medium", "a_mammal a_bigger a_water a_sea a_meat a_blackwhite a_herd a_africa a_asia a_australia a_americas a_whale")
t("animal", ["Chimpanzee", "Chimp"], "easy", "a_mammal a_zoo a_meat a_plants a_danger a_herd a_endangered a_africa a_ape")
t("animal", ["Moose", "Elk"], "medium", "a_mammal a_bigger a_fourlegs a_plants a_danger a_horns a_asia a_americas a_hooves")
t("animal", ["Emu"], "medium", "a_bird a_zoo a_plants a_eggs a_fast a_australia a_flightless")
t("animal", ["Pelican"], "medium", "a_bird a_zoo a_fly a_water a_meat a_herd a_eggs a_africa a_asia a_australia a_americas a_swims")
t("animal", ["Magpie"], "easy", "a_bird a_wildbritain a_fly a_meat a_plants a_blackwhite a_tail a_eggs a_asia a_americas a_garden")
t("animal", ["Alligator"], "medium", "a_reptile a_zoo a_bigger a_water a_meat a_danger a_tail a_eggs a_asia a_americas")
t("animal", ["Rat"], "easy", "a_mammal a_wildbritain a_small a_fourlegs a_meat a_plants a_tail a_nocturnal a_africa a_asia a_australia a_americas a_rodent")
t("animal", ["Turtle", "Sea turtle"], "medium", "a_reptile a_water a_sea a_meat a_plants a_eggs a_endangered a_africa a_asia a_australia a_americas a_shell")

# ---- places ----
t("place", ["Manchester"], "easy", "pl_uk pl_england pl_north pl_city pl_club pl_river")
t("place", ["Glasgow"], "easy", "pl_uk pl_scotland pl_city pl_club pl_river")
t("place", ["York"], "easy", "pl_uk pl_england pl_north pl_city pl_river pl_tourist")
t("place", ["Cornwall"], "easy", "pl_uk pl_england pl_region pl_sea pl_tourist pl_heritage")
t("place", ["Amsterdam"], "easy", "pl_europe pl_city pl_capital pl_olympics pl_club pl_river pl_tourist pl_heritage")
t("place", ["Sydney"], "easy", "pl_oceania pl_city pl_bigpop pl_english pl_olympics pl_sea pl_hot pl_tourist pl_heritage")
t("place", ["Rio de Janeiro", "Rio"], "easy", "pl_americas pl_city pl_bigpop pl_olympics pl_club pl_sea pl_hot pl_tourist pl_heritage")
t("place", ["Egypt"], "easy", "pl_africa pl_country pl_bigpop pl_sea pl_river pl_hot pl_tourist pl_heritage")
t("place", ["Iceland"], "easy", "pl_europe pl_country pl_island pl_sea pl_snow pl_tourist pl_heritage")
t("place", ["The Golden Gate Bridge", "Golden Gate Bridge"], "easy", "pl_americas pl_usa pl_building pl_bridge pl_tall pl_sea pl_tourist")
t("place", ["The Great Wall of China", "Great Wall of China"], "easy", "pl_asia pl_building pl_old pl_tourist pl_heritage")

# ---- food and drink ----
t("food", ["Milk"], "easy", "f_drink f_milk")
t("food", ["Mojito"], "medium", "f_drink f_alcohol f_cocktail f_fizzy")
t("food", ["Carrot"], "easy", "f_fruitveg f_orange")
t("food", ["Full English breakfast", "Full English", "Fry-up"], "easy", "f_hot f_meat f_pork f_egg f_bread f_fried f_breakfast f_british")
t("food", ["Fajitas", "Fajita"], "medium", "f_hot f_meat f_chicken f_bread f_hands f_mexican")
t("food", ["Ramen"], "medium", "f_hot f_meat f_pork f_egg f_rice f_japanese")
t("food", ["Pease pudding"], "medium", "f_british f_northeast")
t("food", ["Panettone"], "medium", "f_sweet f_cake f_bread f_christmas f_italian")
t("food", ["Steak pie", "Steak and kidney pie"], "easy", "f_hot f_meat f_beef f_pastry f_british")
t("food", ["Kit Kat", "KitKat"], "easy", "f_sweet f_chocolate f_cake f_hands f_snack f_brand")

# ---- objects ----
t("object", ["Fork"], "easy", "o_eat o_home o_kitchen o_pocket o_hold o_metal o_old o_sharp")
t("object", ["Book"], "easy", "o_home o_hold o_paper o_old")
t("object", ["Pillow"], "easy", "o_home o_bedroom o_fabric o_old")
t("object", ["Motorbike", "Motorcycle"], "easy", "o_vehicle o_heavy o_metal o_old o_wheels o_moving o_light o_sound o_engine")
t("object", ["Helicopter"], "easy", "o_vehicle o_heavy o_metal o_moving o_light o_sound o_engine o_flies")
t("object", ["Skis"], "medium", "o_sport o_old")
t("object", ["Basketball"], "easy", "o_sport o_hold o_old o_round o_ball")
t("object", ["Clarinet"], "medium", "o_music o_hold o_wood o_old o_sound o_blow o_keys")
t("object", ["Pen"], "easy", "o_write o_home o_office o_pocket o_hold o_plastic o_old")
t("object", ["Necklace"], "easy", "o_wear o_pocket o_metal o_old o_jewel")
t("object", ["Gloves", "Glove"], "easy", "o_wear o_pocket o_fabric o_old o_warm")
t("object", ["Torch", "Flashlight"], "easy", "o_home o_electric o_hold o_plastic o_light")
t("object", ["Vacuum cleaner", "Hoover", "Vacuum"], "easy", "o_clean o_home o_electric o_plug o_wheels o_moving o_sound")

# ---- films, TV, books and songs ----
t("title", ["Avatar"], "easy", "t_film t_e_00 t_american t_series t_scifi")
t("title", ["Oppenheimer"], "medium", "t_film t_e_10 t_american t_real t_war t_named t_bookfirst t_bestpic")
t("title", ["Emmerdale"], "easy", "t_tv t_e_70 t_british t_soap t_itv t_running t_long")
t("title", ["The Traitors"], "easy", "t_tv t_e_10 t_british t_reality t_bbc t_running")
t("title", ["Do They Know It's Christmas?", "Do They Know It's Christmas"], "easy", "t_song t_e_80 t_british t_christmas t_number1 t_xmas1 t_band")
t("title", ["Sex on Fire"], "medium", "t_song t_e_00 t_american t_number1 t_band t_male")
t("title", ["Someone Like You"], "easy", "t_song t_e_10 t_british t_love t_number1 t_slow")
t("title", ["Billie Jean"], "easy", "t_song t_e_80 t_american t_named t_number1 t_male t_dance")
t("title", ["The Very Hungry Caterpillar", "Very Hungry Caterpillar"], "easy", "t_book t_e_old t_american t_kids t_animal t_picture")
t("title", ["Animal Farm"], "medium", "t_book t_e_old t_british t_animal t_novel")

# ---- brands and companies ----
t("brand", ["Morrisons"], "easy", "b_food b_shop b_clothes b_uk b_old b_person b_supermarket")
t("brand", ["Waitrose"], "easy", "b_food b_shop b_uk b_old b_person b_supermarket")
t("brand", ["Pizza Hut"], "easy", "b_food b_american b_red b_highstreet b_fastfood")
t("brand", ["Honda"], "easy", "b_cars b_japanese b_person")
t("brand", ["Porsche"], "easy", "b_cars b_german b_old b_logo b_person b_luxury b_sportscar")
t("brand", ["Land Rover"], "medium", "b_cars b_uk b_ukfactory")
t("brand", ["Next"], "easy", "b_shop b_clothes b_uk b_highstreet")
t("brand", ["Ben & Jerry's", "Ben and Jerry's"], "medium", "b_food b_american b_person")
t("brand", ["Jet2"], "easy", "b_airline b_uk b_red")
t("brand", ["Umbro"], "medium", "b_clothes b_sport b_uk b_old")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(B), 'items:', dict(Counter(x['what'] for x in B)))
