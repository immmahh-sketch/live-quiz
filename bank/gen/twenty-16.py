# Bank session 11 Oct 2026: more 20 Questions answers for characters
# -> bank/twenty-16.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-16.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- characters ----
t("character", ["Aladdin"], "easy", "c_human c_male c_hero c_animated c_film c_disney")
t("character", ["Belle"], "easy", "c_human c_female c_hero c_animated c_film c_disney c_royal")
t("character", ["Mulan"], "medium", "c_human c_female c_hero c_animated c_film c_disney")
t("character", ["Stitch"], "easy", "c_alien c_powers c_animated c_film c_disney c_hero c_kids")
t("character", ["Puss in Boots"], "medium", "c_animal c_cat c_male c_hero c_animated c_film c_talks c_clothes c_hat c_franchise")
t("character", ["Patrick Star", "Patrick"], "medium", "c_animal c_male c_hero c_animated c_tv c_kids c_talks c_american")
t("character", ["Gru"], "medium", "c_human c_male c_animated c_film c_franchise")
t("character", ["Daffy Duck"], "medium", "c_animal c_bird c_male c_animated c_old c_american c_talks c_kids")
t("character", ["Tweety", "Tweety Pie"], "medium", "c_hero c_animal c_bird c_male c_animated c_old c_american c_talks c_kids")
t("character", ["Popeye"], "medium", "c_human c_male c_hero c_animated c_old c_american c_comic c_hat")
t("character", ["Danger Mouse"], "medium", "c_animal c_mouse c_male c_hero c_animated c_british c_old c_tv c_kids c_detective c_talks c_clothes")
t("character", ["Hyacinth Bucket", "Hyacinth"], "medium", "c_human c_female c_british c_tv c_sitcomc")
t("character", ["Victor Meldrew"], "medium", "c_human c_male c_british c_tv c_sitcomc")
t("character", ["Dot Cotton"], "medium", "c_human c_female c_british c_tv c_soapc")
t("character", ["Asterix"], "medium", "c_human c_male c_hero c_comic c_old c_powers c_hat")
t("character", ["Morph"], "medium", "c_animated c_stopmotion c_british c_old c_tv c_kids")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
