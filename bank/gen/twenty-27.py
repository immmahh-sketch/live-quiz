# Bank session 19 Oct 2026: more 20 Questions people -> bank/twenty-27.json (faces from today's TV sessions: panel shows,
# Morse, Lovejoy, The Tube, Deal or No Deal). Only the Yes questions are listed; anything arguable is left No (is Sandi Toksvig
# British? she was born in Copenhagen and is Danish-British, so British/English are left off; Jools Holland's honours left off).
# Check with: node tools/twenty-check.mjs bank/twenty-27.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

t("person", ["Bob Mortimer"], "medium", "p_man p_alive p_over50 p_british p_english p_northeast p_north p_comedy p_tv p_panel p_double p_characters p_gameshow p_b1990 p_b2000 p_b2010")
t("person", ["Paul Merton"], "medium", "p_man p_alive p_over50 p_british p_english p_london p_comedy p_standup p_panel p_b1990 p_b2000 p_b2010")
t("person", ["Ian Hislop"], "medium", "p_man p_alive p_over50 p_british p_english p_tv p_news p_writer p_b1990 p_b2000 p_b2010")
t("person", ["Sandi Toksvig"], "medium", "p_woman p_alive p_over50 p_comedy p_tv p_gameshow p_bakeoff p_writer p_b1990 p_b2000 p_b2010")
t("person", ["Bill Bailey"], "medium", "p_man p_alive p_over50 p_british p_english p_comedy p_standup p_panel p_csitcom p_tv p_strictly p_b2000 p_b2010")
t("person", ["Noel Fielding"], "medium", "p_man p_alive p_over50 p_british p_english p_london p_comedy p_characters p_panel p_csitcom p_tv p_bakeoff p_b2010")
t("person", ["John Thaw"], "hard", "p_man p_over50 p_british p_english p_north p_actor p_sitcom p_b1980 p_b1990 p_b2000")
t("person", ["Kevin Whately"], "hard", "p_man p_alive p_over50 p_over70 p_british p_english p_northeast p_north p_actor p_b1990 p_b2000 p_b2010")
t("person", ["Ian McShane"], "hard", "p_man p_alive p_over50 p_over70 p_british p_english p_north p_actor p_hollywood p_voice p_b1990 p_b2000 p_b2010")
t("person", ["Jools Holland"], "medium", "p_man p_alive p_over50 p_british p_english p_london p_music p_band p_instrument p_tv p_b1990 p_b2000 p_b2010")
t("person", ["Noel Edmonds"], "easy", "p_man p_alive p_over50 p_over70 p_british p_english p_london p_tv p_gameshow p_saturday p_b1980 p_b1990 p_b2000 p_b2010")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-27.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
