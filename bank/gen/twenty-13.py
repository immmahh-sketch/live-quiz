# Bank session 11 Oct 2026: more 20 Questions answers for fictional characters and real people
# -> bank/twenty-13.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-13.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- characters ----
t("character", ["Eeyore"], "medium", "c_animal c_male c_talks c_book c_old c_kids c_british c_bookseries")
t("character", ["Nemo"], "easy", "c_animal c_male c_hero c_talks c_kids c_animated c_pixar c_film")
t("character", ["Lightning McQueen"], "easy", "c_male c_hero c_kids c_animated c_pixar c_film")
t("character", ["Donkey (from Shrek)", "Donkey"], "easy", "c_animal c_male c_hero c_talks c_kids c_animated c_film c_franchise")
t("character", ["Thor"], "easy", "c_male c_hero c_powers c_super c_marvel c_comic c_american c_old c_royal")
t("character", ["The Penguin"], "medium", "c_human c_male c_villain c_hat c_comic c_american c_old")
t("character", ["Ron Weasley", "Ron"], "easy", "c_human c_male c_hero c_powers c_wizard c_british c_school c_book c_bookseries c_potter")
t("character", ["Severus Snape", "Snape"], "easy", "c_human c_male c_powers c_wizard c_british c_book c_bookseries c_potter")
t("character", ["Bilbo Baggins", "Bilbo"], "medium", "c_male c_hero c_book c_british c_old c_bookseries")
t("character", ["Maleficent"], "medium", "c_female c_villain c_powers c_wizard c_disney c_animated c_film c_old")
t("character", ["Tintin"], "medium", "c_human c_male c_hero c_comic c_old")
t("character", ["Desperate Dan"], "medium", "c_human c_male c_hero c_comic c_british c_old c_hat")

# ---- people ----
t("person", ["Michael McIntyre"], "easy", "p_man p_alive p_over50 p_british p_english p_london p_comedy p_standup p_tv p_saturday p_bgt p_b2010")
t("person", ["Sarah Millican"], "medium", "p_woman p_alive p_over50 p_british p_english p_northeast p_comedy p_standup p_panel p_b2010")
t("person", ["Ross Noble"], "hard", "p_man p_alive p_over50 p_british p_english p_northeast p_comedy p_standup p_panel p_b2000")
t("person", ["Lewis Capaldi"], "easy", "p_man p_alive p_under30 p_british p_scottish p_music p_solo p_number1 p_songwriter p_instrument p_pop p_brit p_glasto p_active")
t("person", ["Raheem Sterling"], "medium", "p_man p_alive p_british p_english p_london p_sport p_football p_country p_prem p_liverpool p_mancity p_chelsea p_arsenal")
t("person", ["Jack Grealish"], "medium", "p_man p_alive p_british p_english p_sport p_football p_country p_prem p_mancity p_everton")
t("person", ["Steph Houghton"], "hard", "p_woman p_alive p_british p_english p_northeast p_sport p_football p_country p_captain p_olympic p_retired p_mancity")
t("person", ["Ant Middleton"], "hard", "p_man p_alive p_over50 p_british p_english p_tv p_reality p_hero p_war")
t("person", ["Joe Wicks"], "easy", "p_man p_alive p_british p_english p_london p_tv p_daytime")
t("person", ["Rylan Clark"], "medium", "p_man p_alive p_british p_english p_london p_tv p_reality p_daytime p_thismorning")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
