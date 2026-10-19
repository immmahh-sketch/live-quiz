# Bank session 19 Oct 2026: more 20 Questions people -> bank/twenty-28.json (faces from today's cop-show and soap races, plus
# the Australian stars they launched). Only the Yes questions are listed; anything arguable is left No (Nicole Kidman's US
# citizenship, Dennis Waterman as a singer, whether the Neighbours/Home and Away stars were famous before 2010). The Australians
# answer No to every nationality question, as there's no Australian one.
# Check with: node tools/twenty-check.mjs bank/twenty-28.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

t("person", ["David Jason"], "easy", "p_man p_alive p_over50 p_over70 p_british p_english p_london p_actor p_sitcom p_funny p_knighted p_voice p_b1980 p_b1990 p_b2000 p_b2010")
t("person", ["Dennis Waterman"], "medium", "p_man p_over50 p_over70 p_british p_english p_london p_actor p_b1980 p_b1990 p_b2000 p_b2010")
t("person", ["Martin Shaw"], "hard", "p_man p_alive p_over50 p_over70 p_british p_english p_actor p_b1980 p_b1990 p_b2000 p_b2010")
t("person", ["Jason Donovan"], "medium", "p_man p_alive p_over50 p_actor p_soap p_music p_solo p_number1 p_pop p_sang p_acted p_b1990 p_b2000 p_b2010")
t("person", ["Margot Robbie"], "medium", "p_woman p_alive p_actor p_hollywood p_soap p_superhero")
t("person", ["Chris Hemsworth"], "medium", "p_man p_alive p_actor p_hollywood p_soap p_superhero p_marvel p_action")
t("person", ["Ray Winstone"], "medium", "p_man p_alive p_over50 p_british p_english p_london p_actor p_hollywood p_b1990 p_b2000 p_b2010")
t("person", ["Ricky Tomlinson"], "medium", "p_man p_alive p_over50 p_over70 p_british p_english p_north p_actor p_sitcom p_funny p_soap p_b1990 p_b2000 p_b2010")
t("person", ["Anna Friel"], "hard", "p_woman p_alive p_over50 p_british p_english p_north p_actor p_soap p_b2000 p_b2010")
t("person", ["Shane Richie"], "medium", "p_man p_alive p_over50 p_british p_english p_london p_actor p_soap p_eastenders p_tv p_gameshow p_jungle p_b1990 p_b2000 p_b2010")
t("person", ["Russell Crowe"], "medium", "p_man p_alive p_over50 p_actor p_hollywood p_oscar p_action p_b2000 p_b2010")
t("person", ["Hugh Jackman"], "easy", "p_man p_alive p_over50 p_actor p_hollywood p_superhero p_marvel p_sang p_action p_b2010")
t("person", ["Nicole Kidman"], "medium", "p_woman p_alive p_over50 p_actor p_hollywood p_oscar p_sang p_b2000 p_b2010")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-28.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
