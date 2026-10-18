# Bank session 19 Oct 2026: more 20 Questions brands (the thinnest kind in the files, 126) -> bank/twenty-24.json.
# Only the Yes questions are listed; anything arguable (is Mini British now BMW owns it? is Tango's logo red?) is left No.
# At most one Yes per group (what it sells / country). Dropped: Iceland (already in), and Bentley, Domino's and Weetabix
# (same answers as Rolls-Royce, Subway and Marmite). Check with: node tools/twenty-check.mjs bank/twenty-24.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

t("brand", ["Vauxhall"], "easy", "b_cars b_uk b_old b_ukfactory")
t("brand", ["Mini"], "medium", "b_cars b_ukfactory")
t("brand", ["Lotus"], "medium", "b_cars b_uk b_sportscar b_ukfactory b_old")
t("brand", ["Currys", "Currys PC World"], "medium", "b_shop b_uk b_old b_person")
t("brand", ["Innocent", "Innocent Drinks"], "medium", "b_food b_drinks b_uk")
t("brand", ["Lucozade"], "medium", "b_food b_drinks b_uk b_old")
t("brand", ["Emirates"], "medium", "b_airline b_red")
t("brand", ["Lufthansa"], "medium", "b_airline b_german b_old b_logo")
t("brand", ["Converse"], "medium", "b_clothes b_sport b_american b_old b_person")
t("brand", ["Pringles"], "easy", "b_food b_sweets b_american b_logo")
t("brand", ["Warburtons"], "medium", "b_food b_uk b_old b_person")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-24.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
