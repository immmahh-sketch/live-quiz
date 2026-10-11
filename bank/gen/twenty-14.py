# Bank session 11 Oct 2026: more 20 Questions answers for brands, food and objects
# -> bank/twenty-14.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-14.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- brands ----
t("brand", ["Argos"], "easy", "b_shop b_uk b_highstreet b_red")
t("brand", ["H&M"], "easy", "b_clothes b_highstreet b_letters b_red")
t("brand", ["Uniqlo"], "medium", "b_clothes b_japanese b_highstreet b_red")
t("brand", ["ASOS"], "medium", "b_clothes b_online b_uk b_letters")
t("brand", ["Krispy Kreme"], "easy", "b_food b_sweets b_american b_old")
t("brand", ["Papa John's"], "medium", "b_food b_fastfood b_american b_person")
t("brand", ["Burger King"], "easy", "b_food b_fastfood b_american b_red")
t("brand", ["Halfords"], "medium", "b_shop b_uk b_old b_highstreet")
t("brand", ["Holland & Barrett"], "medium", "b_shop b_uk b_old b_highstreet b_person")
t("brand", ["Waterstones"], "medium", "b_shop b_uk b_highstreet b_person")
# ---- food ----
t("food", ["Cottage pie"], "easy", "f_meat f_beef f_hot f_potato f_british")
t("food", ["Treacle tart"], "medium", "f_sweet f_cake f_pastry f_british f_hot")
t("food", ["Battenberg", "Battenberg cake"], "medium", "f_sweet f_cake f_british f_egg")
t("food", ["Chicken Kiev"], "medium", "f_meat f_chicken f_hot f_fried f_dairy")
t("food", ["Beans on toast"], "easy", "f_hot f_bread f_british f_breakfast")
t("food", ["Rice pudding"], "easy", "f_sweet f_cake f_hot f_dairy f_rice f_british")
# ---- objects ----
t("object", ["Corkscrew"], "medium", "o_home o_kitchen o_eat o_metal o_hold o_pocket o_sharp o_old o_moving")
t("object", ["Iron"], "easy", "o_home o_electric o_plug o_hold o_metal")
t("object", ["Lamp"], "easy", "o_home o_living o_electric o_plug o_light")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
