# Bank session 18 Oct 2026: more 20 Questions foods (one of the thinnest kinds in the files, 126) -> bank/twenty-23.json.
# Only the Yes questions are listed; anything arguable (is a bagel American? is popcorn sweet?) is left No.
# At most one Yes per group (drink / meat type / country). Check with: node tools/twenty-check.mjs bank/twenty-23.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

t("food", ["Churros", "Churro"], "medium", "f_sweet f_hot f_fried f_hands f_snack")
t("food", ["Apple strudel", "Strudel"], "medium", "f_sweet f_cake f_pastry f_hot")
t("food", ["Profiteroles", "Profiterole"], "medium", "f_sweet f_cake f_pastry f_chocolate f_dairy f_egg f_french")
t("food", ["Hot dog", "Hotdog"], "easy", "f_hot f_meat f_pork f_bread f_hands f_american")
t("food", ["Bagel"], "easy", "f_bread f_round f_hands f_breakfast")
t("food", ["Kedgeree"], "hard", "f_hot f_meat f_fish f_egg f_rice f_breakfast f_british")
t("food", ["Eggs Benedict", "Eggs Benny"], "medium", "f_hot f_egg f_meat f_pork f_bread f_dairy f_breakfast f_american")
t("food", ["Lager"], "easy", "f_drink f_alcohol f_beer f_fizzy")
t("food", ["Garlic bread"], "easy", "f_hot f_bread f_dairy f_italian")
t("food", ["Popcorn"], "easy", "f_snack f_hands")
t("food", ["Bombay mix"], "medium", "f_indian f_snack f_hands f_fried")
t("food", ["Roast beef"], "easy", "f_hot f_meat f_beef f_british")
t("food", ["Pretzel"], "medium", "f_bread f_hands f_snack")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-23.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
