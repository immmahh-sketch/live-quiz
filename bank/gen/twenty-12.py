# Bank session 11 Oct 2026: more 20 Questions answers for titles and brands (now the two thinnest kinds)
# -> bank/twenty-12.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-12.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- titles ----
t("title", ["E.T. the Extra-Terrestrial", "E.T.", "ET"], "easy", "t_film t_e_80 t_american t_kids t_scifi t_named")
t("title", ["Kes"], "medium", "t_film t_e_old t_british t_animal t_named t_bookfirst")
t("title", ["The Full Monty"], "medium", "t_film t_e_90 t_british t_comedy")
t("title", ["The Royle Family"], "medium", "t_tv t_e_90 t_british t_comedy t_sitcom t_bbc")
t("title", ["Thunderbirds"], "medium", "t_tv t_e_old t_british t_kids t_scifi t_itv")
t("title", ["Yesterday"], "medium", "t_song t_e_old t_british t_band t_male t_slow t_beatles")
t("title", ["Shape of You"], "easy", "t_song t_e_10 t_british t_number1 t_male t_dance")
t("title", ["I Will Always Love You"], "easy", "t_song t_e_90 t_american t_number1 t_slow t_filmsong t_cover t_love")
t("title", ["The Hound of the Baskervilles"], "medium", "t_book t_novel t_classic t_e_old t_british t_crime t_series t_scary t_animal")
t("title", ["Frankenstein"], "medium", "t_book t_novel t_classic t_e_old t_british t_scary t_scifi t_named")
t("title", ["Grand Theft Auto", "GTA"], "medium", "t_game t_e_90 t_british t_series t_crime")
t("title", ["FIFA", "EA Sports FC"], "medium", "t_game t_e_90 t_american t_series t_sport")

# ---- brands ----
t("brand", ["Fiat"], "medium", "b_cars b_old b_letters")
t("brand", ["Wetherspoons", "J D Wetherspoon", "Spoons"], "easy", "b_food b_uk b_highstreet b_person")
t("brand", ["Deliveroo"], "easy", "b_food b_online b_uk")
t("brand", ["Superdry"], "medium", "b_clothes b_uk b_highstreet")
t("brand", ["X", "Twitter"], "easy", "b_tech b_social b_online b_american b_letters")
t("brand", ["Zoom"], "medium", "b_tech b_online b_american")
t("brand", ["Red Bull"], "easy", "b_food b_drinks b_logo b_red")
t("brand", ["Gillette"], "medium", "b_american b_old b_person")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-12.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
