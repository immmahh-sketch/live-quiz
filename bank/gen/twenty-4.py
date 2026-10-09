# Bank session 9 Oct 2026 (third pass): more 20 Questions answers for characters and people -> bank/twenty-4.json.
# Each item lists only the questions whose true answer is Yes; everything else is No. Ambiguous facts are left No.
# 'Famous before 19x0' keys are cumulative (famous before 1980 ⇒ also before 1990, 2000, 2010), as in the bank.
# Check with: node tools/twenty-check.mjs bank/twenty-4.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- fictional characters ----
t("character", ["Batman", "Bruce Wayne"], "easy", "c_human c_male c_hero c_american c_old c_comic")
t("character", ["Peter Rabbit"], "easy", "c_animal c_male c_hero c_kids c_british c_old c_book c_bookseries c_classic c_rabbit c_talks c_clothes")
t("character", ["Jerry", "Jerry Mouse"], "easy", "c_animal c_male c_hero c_kids c_animated c_american c_old c_tv c_mouse")
t("character", ["Del Boy", "Derek Trotter", "Del Boy Trotter"], "easy", "c_human c_male c_hero c_british c_tv c_sitcomc")
t("character", ["Basil Fawlty"], "easy", "c_human c_male c_british c_old c_tv c_sitcomc")
t("character", ["Luke Skywalker"], "easy", "c_human c_male c_hero c_powers c_american c_old c_film c_franchise c_starwars")
t("character", ["Princess Leia", "Leia"], "easy", "c_human c_female c_hero c_american c_old c_royal c_film c_franchise c_starwars")
t("character", ["Albus Dumbledore", "Dumbledore"], "easy", "c_human c_male c_hero c_powers c_british c_book c_bookseries c_potter c_wizard")
t("character", ["Wonder Woman"], "easy", "c_female c_hero c_powers c_american c_old c_royal c_comic c_super c_dc")
t("character", ["The Hulk", "Hulk", "The Incredible Hulk"], "easy", "c_human c_male c_hero c_powers c_american c_old c_comic c_super c_marvel")
t("character", ["Ariel", "The Little Mermaid"], "easy", "c_female c_hero c_kids c_animated c_american c_royal c_film c_disney")
t("character", ["Mowgli"], "medium", "c_human c_male c_hero c_kids c_british c_old c_book c_classic")
t("character", ["Kermit the Frog", "Kermit"], "easy", "c_animal c_male c_hero c_animated c_american c_old c_tv c_talks c_stopmotion c_muppet")
t("character", ["Sonic the Hedgehog", "Sonic"], "easy", "c_animal c_male c_hero c_kids c_powers c_game c_talks c_clothes")
t("character", ["Lisa Simpson"], "easy", "c_human c_female c_hero c_animated c_american c_school c_tv c_simpsons")
t("character", ["Dennis the Menace"], "medium", "c_human c_male c_kids c_british c_old c_comic")
t("character", ["Tracy Beaker"], "medium", "c_human c_female c_kids c_british c_school c_book c_bookseries")
t("character", ["Rupert Bear", "Rupert"], "medium", "c_animal c_male c_hero c_kids c_british c_old c_comic c_bear c_talks c_clothes")
t("character", ["Peter Pan"], "easy", "c_human c_male c_hero c_kids c_powers c_british c_old c_book c_classic c_fly")
t("character", ["Alice", "Alice in Wonderland"], "easy", "c_human c_female c_hero c_kids c_british c_old c_book c_classic")

# ---- real people ----
t("person", ["Kevin Keegan", "Keegan"], "easy", "p_man p_alive p_over50 p_over70 p_british p_english p_north p_sport p_b1980 p_b1990 p_b2000 p_b2010 p_football p_country p_captain p_retired p_pundit p_manager p_toon p_liverpool p_striker p_abroad p_ballon")
t("person", ["Paul Gascoigne", "Gazza"], "easy", "p_man p_alive p_over50 p_british p_english p_northeast p_north p_sport p_b1990 p_b2000 p_b2010 p_football p_country p_spoty p_retired p_toon p_prem p_spurs p_everton p_boro p_abroad")
t("person", ["Freddie Mercury"], "easy", "p_man p_british p_music p_b1980 p_b1990 p_b2000 p_b2010 p_band p_frontman p_number1 p_songwriter p_instrument p_rock p_queenband")
t("person", ["Elton John"], "easy", "p_man p_alive p_over50 p_over70 p_british p_knighted p_english p_london p_music p_b1980 p_b1990 p_b2000 p_b2010 p_solo p_number1 p_songwriter p_instrument p_pop p_brit p_grammy p_glasto")
t("person", ["Mick Jagger", "Jagger"], "easy", "p_man p_alive p_over50 p_over70 p_british p_knighted p_english p_music p_b1970 p_b1980 p_b1990 p_b2000 p_b2010 p_band p_frontman p_number1 p_songwriter p_rock p_acted p_glasto p_active p_stones")
t("person", ["Beyoncé", "Beyonce"], "easy", "p_woman p_alive p_american p_music p_b2000 p_b2010 p_band p_boyband p_solo p_number1 p_pop p_soul p_acted p_grammy p_glasto p_active")
t("person", ["Elvis Presley", "Elvis"], "easy", "p_man p_american p_music p_b1970 p_b1980 p_b1990 p_b2000 p_b2010 p_solo p_number1 p_rock p_acted p_grammy")
t("person", ["Madonna"], "easy", "p_woman p_alive p_over50 p_american p_music p_b1990 p_b2000 p_b2010 p_solo p_number1 p_songwriter p_pop p_dance p_acted p_grammy p_active p_bondtheme")
t("person", ["John Lennon", "Lennon"], "easy", "p_man p_british p_english p_north p_music p_b1970 p_b1980 p_b1990 p_b2000 p_b2010 p_band p_frontman p_solo p_number1 p_christmas1 p_songwriter p_instrument p_rock p_acted p_beatles")
t("person", ["Tony Blair", "Blair"], "easy", "p_man p_alive p_over50 p_over70 p_british p_knighted p_scottish p_politics p_b2000 p_b2010 p_pm p_mp p_labour")
t("person", ["Margaret Thatcher", "Thatcher"], "easy", "p_woman p_over50 p_over70 p_british p_english p_politics p_b1980 p_b1990 p_b2000 p_b2010 p_pm p_mp p_tory p_resigned")
t("person", ["King Charles III", "Charles III", "King Charles", "Prince Charles"], "easy", "p_man p_alive p_over50 p_over70 p_british p_english p_london p_royal p_b1970 p_b1980 p_b1990 p_b2000 p_b2010 p_monarch p_divorced")
t("person", ["William Shakespeare", "Shakespeare"], "easy", "p_man p_over50 p_history p_british p_english p_writer p_b1970 p_b1980 p_b1990 p_b2000 p_b2010 p_poet p_plays p_filmed")
t("person", ["Albert Einstein", "Einstein"], "easy", "p_man p_over50 p_over70 p_history p_science p_b1970 p_b1980 p_b1990 p_b2000 p_b2010 p_theory p_nobel")
t("person", ["Usain Bolt", "Bolt"], "easy", "p_man p_alive p_sport p_b2010 p_athletics p_country p_olympic p_world p_retired")
t("person", ["Muhammad Ali", "Ali", "Cassius Clay"], "easy", "p_man p_over50 p_over70 p_american p_sport p_b1970 p_b1980 p_b1990 p_b2000 p_b2010 p_boxing p_country p_olympic p_world p_retired")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(B), 'items:', dict(Counter(x['what'] for x in B)))
