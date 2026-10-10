# Bank session 10 Oct 2026: more 20 Questions answers for characters and objects (now the two thinnest kinds)
# -> bank/twenty-9.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-9.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- characters ----
t("character", ["Alan Partridge"], "medium", "c_human c_male c_british c_tv c_sitcomc c_film")
t("character", ["Cinderella"], "easy", "c_human c_female c_hero c_kids c_animated c_royal c_old c_film c_book c_classic c_disney")
t("character", ["Fred Flintstone", "Fred"], "easy", "c_human c_male c_kids c_animated c_american c_old c_tv")
t("character", ["Miss Marple", "Jane Marple", "Marple"], "medium", "c_human c_female c_hero c_british c_old c_detective c_book c_bookseries")
t("character", ["Babe (the pig)", "Babe"], "easy", "c_animal c_pig c_male c_hero c_kids c_talks c_film c_book")
t("character", ["Captain America", "Steve Rogers"], "medium", "c_human c_male c_hero c_powers c_super c_marvel c_american c_old c_comic c_film c_franchise")
t("character", ["Cruella de Vil", "Cruella"], "easy", "c_human c_female c_villain c_animated c_disney c_film c_book c_british c_old")
t("character", ["Bagpuss"], "medium", "c_animal c_cat c_male c_kids c_animated c_stopmotion c_british c_old c_tv c_talks")
t("character", ["Hannibal Lecter", "Hannibal"], "medium", "c_human c_male c_villain c_american c_film c_book c_bookseries c_franchise")
t("character", ["Mr Darcy", "Fitzwilliam Darcy", "Darcy"], "medium", "c_human c_male c_hero c_british c_old c_book c_classic")
t("character", ["Tom (from Tom and Jerry)", "Tom", "Tom the cat"], "easy", "c_animal c_cat c_male c_kids c_animated c_american c_old c_tv")
t("character", ["Dorothy Gale", "Dorothy"], "medium", "c_human c_female c_hero c_kids c_american c_old c_film c_book c_classic c_bookseries")
t("character", ["Draco Malfoy", "Draco", "Malfoy"], "easy", "c_human c_male c_villain c_school c_powers c_wizard c_british c_film c_book c_potter c_bookseries c_franchise")

# ---- objects ----
t("object", ["Hairbrush"], "medium", "o_home o_hold o_old")
t("object", ["Ironing board"], "medium", "o_home o_metal")
t("object", ["Boxing gloves"], "medium", "o_sport o_wear o_hit o_old")
t("object", ["Recorder"], "easy", "o_music o_blow o_plastic o_hold o_old o_sound o_office")
t("object", ["Electric guitar"], "easy", "o_music o_strings o_electric o_plug o_hold o_sound o_wood")
t("object", ["Skipping rope"], "medium", "o_toy o_hold o_old")
t("object", ["Wheelie bin", "Bin"], "medium", "o_home o_plastic o_wheels")
t("object", ["Tram"], "medium", "o_vehicle o_public o_rails o_electric o_heavy o_wheels o_old o_moving")
t("object", ["Electric toothbrush"], "medium", "o_home o_bathroom o_electric o_hold o_plastic o_moving o_clean")
t("object", ["E-reader", "Kindle", "eReader"], "medium", "o_electric o_screen o_internet o_new o_hold o_plastic")
t("object", ["Sat nav", "Satnav", "GPS"], "medium", "o_electric o_screen o_new o_plastic")
t("object", ["Rolling pin"], "medium", "o_cook o_home o_kitchen o_wood o_hold o_old")
t("object", ["Tea towel"], "medium", "o_home o_kitchen o_fabric o_clean o_hold o_old")
t("object", ["Doorbell"], "medium", "o_home o_sound o_electric o_old")
t("object", ["Hard hat", "Safety helmet"], "medium", "o_wear o_head o_plastic o_office")
t("object", ["Flip-flops", "Flip flops"], "medium", "o_wear o_feet")
t("object", ["Crayon"], "medium", "o_write o_hold o_pocket o_old o_office")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-9.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
