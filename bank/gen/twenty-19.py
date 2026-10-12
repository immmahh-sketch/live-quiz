# Bank session 12 Oct 2026: more 20 Questions answers for titles (the thinnest kind, 109 in the bank)
# -> bank/twenty-19.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-19.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- films ----
t("title", ["Forrest Gump"], "easy", "t_film t_e_90 t_american t_bestpic t_named t_bookfirst")
t("title", ["Chariots of Fire"], "medium", "t_film t_e_80 t_british t_bestpic t_real t_sport")
t("title", ["The Exorcist"], "medium", "t_film t_e_70 t_american t_scary t_bookfirst")
t("title", ["Slumdog Millionaire"], "medium", "t_film t_e_00 t_british t_bestpic t_love t_bookfirst")
t("title", ["Skyfall"], "medium", "t_film t_e_10 t_british t_bond t_series t_london")
t("title", ["Bend It Like Beckham"], "medium", "t_film t_e_00 t_british t_comedy t_sport t_london")

t("title", ["Dirty Dancing"], "easy", "t_film t_e_80 t_american t_love")
t("title", ["The Shining"], "medium", "t_film t_e_80 t_american t_scary t_bookfirst")

# ---- TV ----
t("title", ["Tipping Point"], "easy", "t_tv t_e_10 t_british t_quiz t_itv t_running")
t("title", ["Teletubbies"], "easy", "t_tv t_e_90 t_british t_kids t_bbc")
t("title", ["The Inbetweeners", "Inbetweeners"], "easy", "t_tv t_e_00 t_british t_comedy t_sitcom t_series")
t("title", ["Countdown"], "easy", "t_tv t_e_80 t_british t_quiz t_long t_running")
t("title", ["Squid Game"], "medium", "t_tv t_e_10 t_drama t_netflix")
t("title", ["Bluey"], "easy", "t_tv t_e_10 t_kids t_animated t_animal t_named")

# ---- songs ----
t("title", ["Hotel California"], "medium", "t_song t_e_70 t_american t_band t_male")
t("title", ["Livin' on a Prayer", "Living on a Prayer"], "easy", "t_song t_e_80 t_american t_band t_male t_dance")
t("title", ["Sweet Caroline"], "easy", "t_song t_e_old t_american t_male t_dance")
t("title", ["Never Gonna Give You Up"], "easy", "t_song t_e_80 t_british t_number1 t_male t_dance")
t("title", ["Fog on the Tyne"], "medium", "t_song t_e_70 t_british t_band t_male t_northeast")
t("title", ["Angels"], "easy", "t_song t_e_90 t_british t_male t_slow")

t("title", ["Yellow Submarine"], "easy", "t_song t_e_old t_british t_band t_male t_number1 t_beatles")
t("title", ["Africa"], "medium", "t_song t_e_80 t_american t_band t_male")

# ---- books ----
t("title", ["Black Beauty"], "medium", "t_book t_novel t_classic t_e_old t_british t_animal t_named")
t("title", ["The Da Vinci Code", "Da Vinci Code"], "medium", "t_book t_novel t_e_00 t_american t_crime t_series")
t("title", ["Gangsta Granny"], "medium", "t_book t_e_10 t_british t_kids t_comedy")

# ---- games ----
t("title", ["Pac-Man", "Pacman"], "easy", "t_game t_e_80 t_series t_named")
t("title", ["Tetris"], "medium", "t_game t_e_80")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-19.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
