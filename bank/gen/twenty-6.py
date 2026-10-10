# Bank session 10 Oct 2026 : more 20 Questions answers for animals, food, objects and brands
# -> bank/twenty-6.json, several for Christmas. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-6.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- animals ----
t("animal", ["Leopard"], "medium", "a_mammal a_zoo a_fourlegs a_meat a_danger a_stripes a_tail a_nocturnal a_africa a_asia a_catfam")
t("animal", ["Hare"], "medium", "a_mammal a_wildbritain a_fourlegs a_plants a_fast a_africa a_asia a_australia a_americas")
t("animal", ["Woodpecker"], "medium", "a_bird a_wildbritain a_fly a_small a_eggs a_garden a_africa a_asia a_americas")
t("animal", ["Vulture"], "medium", "a_bird a_fly a_meat a_eggs a_zoo a_prey a_africa a_asia a_americas")
t("animal", ["Scorpion"], "medium", "a_insect a_small a_meat a_danger a_venom a_tail a_nocturnal a_sting a_eightlegs a_africa a_asia a_australia a_americas")
t("animal", ["Bison", "Buffalo"], "medium", "a_mammal a_bigger a_fourlegs a_plants a_herd a_horns a_danger a_hooves a_americas")
t("animal", ["Meerkat"], "easy", "a_mammal a_small a_fourlegs a_zoo a_herd a_meat a_africa")
t("animal", ["Orangutan"], "medium", "a_mammal a_zoo a_plants a_endangered a_ape a_asia")
t("animal", ["Komodo dragon"], "medium", "a_reptile a_bigger a_fourlegs a_meat a_danger a_venom a_tail a_eggs a_zoo a_endangered a_asia")

# ---- food and drink ----
t("food", ["Bread and butter pudding"], "medium", "f_sweet f_hot f_cake f_bread f_egg f_dairy f_british")
t("food", ["Lancashire hotpot"], "medium", "f_hot f_meat f_potato f_british")
t("food", ["Crème brûlée", "Creme brulee"], "medium", "f_sweet f_cake f_egg f_dairy f_french")
t("food", ["Spring roll"], "medium", "f_fried f_hands f_takeaway f_snack f_chinese")
t("food", ["Cappuccino"], "easy", "f_drink f_hotdrink f_milk f_caffeine f_italian")
t("food", ["Margarita"], "medium", "f_drink f_alcohol f_cocktail f_mexican")
t("food", ["Mango"], "easy", "f_fruitveg f_fruit f_tropical f_raw f_sweet f_orange")
t("food", ["Quiche"], "medium", "f_egg f_dairy f_cheese f_pastry f_round f_french")
t("food", ["Bubble and squeak"], "medium", "f_hot f_fried f_potato f_british")

# ---- objects ----
t("object", ["Saucepan"], "easy", "o_cook o_home o_kitchen o_metal o_hold o_old")
t("object", ["Watch", "Wristwatch"], "easy", "o_time o_wear o_pocket o_moving")
t("object", ["Skateboard"], "easy", "o_sport o_wheels o_wood o_moving")
t("object", ["Rocking horse"], "medium", "o_toy o_wood o_moving o_old")
t("object", ["Smartwatch"], "medium", "o_time o_wear o_electric o_screen o_internet o_new o_pocket")
t("object", ["Canoe"], "medium", "o_vehicle o_boat o_old")
t("object", ["Dartboard"], "medium", "o_sport o_round o_old")

# ---- brands ----
t("brand", ["Kellogg's"], "easy", "b_food b_american b_old b_red b_person")
t("brand", ["Volvo"], "medium", "b_cars b_old")
t("brand", ["Chanel"], "medium", "b_clothes b_french b_old b_person b_luxury")
t("brand", ["Sports Direct"], "medium", "b_shop b_sport b_clothes b_uk b_highstreet")
t("brand", ["Fenwick"], "hard", "b_shop b_uk b_northeast b_old b_person")
t("brand", ["Barbour"], "hard", "b_clothes b_uk b_northeast b_old b_person")
t("brand", ["TikTok"], "easy", "b_tech b_online b_social")
t("brand", ["YouTube"], "easy", "b_tech b_american b_online b_red")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
