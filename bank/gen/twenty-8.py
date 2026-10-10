# Bank session 10 Oct 2026: more 20 Questions answers for titles and brands (the two thinnest kinds)
# -> bank/twenty-8.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-8.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- titles ----
t("title", ["The Jungle Book"], "easy", "t_film t_e_old t_american t_kids t_disney t_animated t_musical t_animal t_bookfirst")
t("title", ["The Incredibles"], "easy", "t_film t_e_00 t_american t_kids t_animated t_pixar t_superhero t_series t_comedy")
t("title", ["Back to the Future"], "easy", "t_film t_e_80 t_american t_comedy t_series t_scifi")
t("title", ["Phoenix Nights"], "medium", "t_tv t_e_00 t_british t_comedy t_sitcom")
t("title", ["Geordie Shore"], "easy", "t_tv t_e_10 t_british t_reality t_northeast t_running")
t("title", ["Smells Like Teen Spirit"], "medium", "t_song t_e_90 t_american t_band")
t("title", ["Mr. Blue Sky", "Mr Blue Sky"], "medium", "t_song t_e_70 t_british t_band")
t("title", ["Waterloo"], "easy", "t_song t_e_70 t_number1 t_band t_abba")
t("title", ["Wannabe"], "easy", "t_song t_e_90 t_british t_number1 t_band t_dance")
t("title", ["The Hobbit"], "medium", "t_book t_e_old t_british t_novel t_series t_scifi t_kids")
t("title", ["Matilda"], "easy", "t_book t_e_80 t_british t_kids t_novel t_named")
t("title", ["Ghosts"], "medium", "t_tv t_e_10 t_british t_comedy t_sitcom t_bbc")
t("title", ["Wallace & Gromit: The Curse of the Were-Rabbit", "The Curse of the Were-Rabbit"], "medium", "t_film t_e_00 t_british t_kids t_comedy t_animated t_series t_animal")

# ---- brands ----
t("brand", ["Gucci"], "medium", "b_clothes b_luxury b_person b_old")
t("brand", ["Lacoste"], "medium", "b_clothes b_sport b_french b_logo b_person b_old")
t("brand", ["Aston Martin"], "medium", "b_cars b_uk b_sportscar b_ukfactory b_old b_luxury")
t("brand", ["Wagamama"], "medium", "b_food b_uk b_highstreet")
t("brand", ["Pret A Manger", "Pret"], "medium", "b_food b_coffee b_uk b_highstreet")
t("brand", ["Monzo"], "medium", "b_bank b_uk b_online")
t("brand", ["eBay"], "easy", "b_shop b_american b_online")
t("brand", ["Xbox"], "easy", "b_tech b_games b_american")
t("brand", ["Disney+", "Disney Plus"], "easy", "b_tech b_stream b_american b_online")
t("brand", ["Tunnock's", "Tunnocks"], "medium", "b_food b_sweets b_uk b_old b_person b_logo")
t("brand", ["Specsavers"], "easy", "b_shop b_uk b_highstreet")
t("brand", ["WHSmith", "WH Smith", "Smiths"], "medium", "b_shop b_uk b_old b_highstreet b_person b_letters")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
