# Bank session 11 Oct 2026: more 20 Questions answers for objects, food and animals
# -> bank/twenty-15.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-15.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- objects ----
t("object", ["Tambourine"], "medium", "o_music o_sound o_hold o_round o_old")
t("object", ["Dice", "Die"], "easy", "o_toy o_pocket o_old o_hold")
t("object", ["Tractor"], "easy", "o_vehicle o_engine o_wheels o_heavy o_metal o_moving o_sound")
t("object", ["Submarine"], "medium", "o_vehicle o_engine o_heavy o_metal o_boat o_moving")
t("object", ["Headphones"], "easy", "o_electric o_wear o_head o_sound o_home")
t("object", ["Remote control", "TV remote"], "easy", "o_electric o_hold o_pocket o_home o_living o_plastic")
t("object", ["Dishwasher"], "easy", "o_home o_kitchen o_electric o_plug o_clean o_moving")

# ---- food and drink ----
t("food", ["Ice cream"], "easy", "f_sweet f_dairy")
t("food", ["Naan bread", "Naan"], "easy", "f_bread f_indian f_takeaway f_hot f_hands")
t("food", ["Poppadom", "Poppadum"], "medium", "f_indian f_takeaway f_fried f_hands f_round f_snack")
t("food", ["Chow mein"], "medium", "f_chinese f_takeaway f_hot f_fried")
t("food", ["Egg fried rice"], "medium", "f_chinese f_takeaway f_hot f_rice f_fried f_egg")
t("food", ["Coconut"], "medium", "f_fruitveg f_fruit f_tropical f_round f_raw")
t("food", ["Milkshake"], "easy", "f_drink f_milk f_dairy f_sweet")
t("food", ["Chilli con carne"], "medium", "f_meat f_beef f_hot f_rice")
t("food", ["Fish pie"], "medium", "f_meat f_fish f_hot f_potato f_british f_dairy")

# ---- animals ----
t("animal", ["Budgie", "Budgerigar"], "easy", "a_bird a_fly a_pet a_small a_colourful a_talkbird a_eggs a_plants a_australia")
t("animal", ["Guinea pig"], "easy", "a_mammal a_pet a_small a_rodent a_fourlegs a_plants")
t("animal", ["Toucan"], "medium", "a_bird a_fly a_colourful a_americas a_zoo a_eggs a_plants")
t("animal", ["Squid"], "medium", "a_sea a_water a_meat a_eat")
t("animal", ["Tuna"], "medium", "a_fish a_sea a_water a_eat a_meat a_fast a_eggs")
t("animal", ["Lemur"], "medium", "a_mammal a_zoo a_tail a_plants a_herd a_fourlegs")
t("animal", ["Pigeon"], "easy", "a_bird a_fly a_garden a_wildbritain a_eggs a_plants a_herd")
t("animal", ["Baboon"], "medium", "a_mammal a_ape a_africa a_zoo a_herd a_fourlegs a_tail a_plants a_meat")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-15.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
