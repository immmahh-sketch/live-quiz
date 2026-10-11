# Bank session 11 Oct 2026: more 20 Questions answers for people
# -> bank/twenty-18.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-18.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- people ----
t("person", ["Kevin Phillips"], "medium", "p_man p_alive p_over50 p_british p_english p_sport p_football p_mackem p_prem p_striker p_country p_retired p_b2000 p_b2010")
t("person", ["Niall Quinn"], "medium", "p_man p_alive p_over50 p_irish p_sport p_football p_mackem p_prem p_striker p_country p_retired p_pundit p_arsenal p_mancity p_b1990 p_b2000 p_b2010")
t("person", ["Peter Beardsley"], "medium", "p_man p_alive p_over50 p_british p_english p_northeast p_north p_sport p_football p_toon p_liverpool p_everton p_prem p_country p_retired p_b1990 p_b2000 p_b2010")
t("person", ["Brendan Foster"], "hard", "p_man p_alive p_over50 p_over70 p_british p_english p_northeast p_north p_sport p_athletics p_olympic p_country p_retired p_pundit p_b1980 p_b1990 p_b2000 p_b2010")
t("person", ["Robson Green"], "medium", "p_man p_alive p_over50 p_british p_english p_northeast p_north p_actor p_music p_number1 p_tv p_b2000 p_b2010")
t("person", ["Tess Daly"], "easy", "p_woman p_alive p_over50 p_british p_english p_north p_tv p_saturday p_b2010")
t("person", ["Claudia Winkleman"], "easy", "p_woman p_alive p_over50 p_british p_english p_london p_tv p_saturday p_b2010")
t("person", ["Alan Titchmarsh"], "medium", "p_man p_alive p_over50 p_over70 p_british p_english p_north p_tv p_writer p_chat p_daytime p_b2000 p_b2010")
t("person", ["Ricky Gervais"], "easy", "p_man p_alive p_over50 p_british p_english p_comedy p_actor p_sitcom p_funny p_writer p_hollywood p_standup p_b2010 p_b2000")
t("person", ["Victoria Beckham", "Posh Spice"], "easy", "p_woman p_alive p_over50 p_british p_english p_music p_band p_boyband p_spice p_number1 p_christmas1 p_business p_b2000 p_b2010")
t("person", ["Billie Eilish"], "medium", "p_woman p_alive p_under30 p_american p_music p_solo p_songwriter p_pop p_grammy p_bondtheme p_glasto p_active p_number1")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
