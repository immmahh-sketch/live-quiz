# Bank session 19 Oct 2026: more 20 Questions people (the thinnest kind in the files, 131) -> bank/twenty-26.json.
# Only the Yes questions are listed; anything arguable (was Peter Kay a chart act? was Flintoff famous before 2000?) is left No.
# At most one Yes per group (nationality / kind of fame). Check with: node tools/twenty-check.mjs bank/twenty-26.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

t("person", ["Peter Kay"], "easy", "p_man p_alive p_over50 p_british p_english p_north p_comedy p_standup p_csitcom p_characters p_b2010")
t("person", ["Victoria Wood"], "medium", "p_woman p_over50 p_british p_english p_north p_comedy p_standup p_csitcom p_writer p_plays p_b1990 p_b2000 p_b2010")
t("person", ["Nicholas Lyndhurst"], "medium", "p_man p_alive p_over50 p_british p_english p_london p_actor p_sitcom p_funny p_b1980 p_b1990 p_b2000 p_b2010")
t("person", ["Penelope Keith"], "medium", "p_woman p_alive p_over50 p_over70 p_british p_english p_actor p_sitcom p_funny p_knighted p_b1980 p_b1990 p_b2000 p_b2010")
t("person", ["Hugh Dennis"], "medium", "p_man p_alive p_over50 p_british p_english p_comedy p_panel p_csitcom p_b2000 p_b2010")
t("person", ["Lee Mack"], "easy", "p_man p_alive p_over50 p_british p_english p_north p_comedy p_standup p_panel p_csitcom p_tv p_gameshow p_b2010")
t("person", ["Victoria Coren Mitchell", "Victoria Coren"], "medium", "p_woman p_alive p_over50 p_british p_english p_london p_tv p_gameshow p_b2010")
t("person", ["Sacha Baron Cohen"], "medium", "p_man p_alive p_over50 p_british p_english p_london p_comedy p_characters p_cfilm p_actor p_hollywood p_b2000 p_b2010")
t("person", ["Brendan O'Carroll"], "medium", "p_man p_alive p_over50 p_over70 p_irish p_comedy p_characters p_csitcom p_writer p_b2010")
t("person", ["Jim Davidson"], "medium", "p_man p_alive p_over50 p_over70 p_british p_english p_london p_comedy p_standup p_tv p_gameshow p_saturday p_b1980 p_b1990 p_b2000 p_b2010")
t("person", ["Freddie Flintoff", "Andrew Flintoff"], "easy", "p_man p_alive p_british p_english p_north p_sport p_cricket p_country p_captain p_spoty p_retired p_tv p_topgear p_gameshow p_b2010")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-26.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
