# Bank session 18 Oct 2026: more Picture Reveal faces -> bank/reveal-people-19.json
# (Wikipedia title, accepted answers, difficulty). Checked against every answer in the live bank. Guessable names only: hosts and
# faces from the game shows written up as races today. Stock with PEOPLE=bank/reveal-people-19.json node tools/reveal-stock.mjs, then
# contact-sheet them (wrong person, tiny face, small image -> RETIRED below).
import json, os
P = [
 ("Philippa Forrester", ["Philippa Forrester", "Forrester"], "hard"), ("Angela Scanlon", ["Angela Scanlon", "Scanlon"], "hard"),
 ("Les Dawson", ["Les Dawson", "Dawson"], "medium"), ("Richard O'Brien", ["Richard O'Brien", "O'Brien"], "medium"),
 ("Jim Davidson", ["Jim Davidson", "Davidson"], "medium"), ("John Virgo", ["John Virgo", "Virgo"], "hard"),
 ("Leslie Crowther", ["Leslie Crowther", "Crowther"], "hard"), ("Joe Pasquale", ["Joe Pasquale", "Pasquale"], "medium"),
 ("Bob Barker", ["Bob Barker", "Barker"], "hard"), ("Drew Carey", ["Drew Carey", "Carey"], "medium"),
 ("Amol Rajan", ["Amol Rajan", "Rajan"], "medium"), ("Sally Magnusson", ["Sally Magnusson", "Magnusson"], "hard"),
 ("Peter Snow", ["Peter Snow"], "medium"), ("Barry Humphries", ["Barry Humphries", "Humphries", "Dame Edna"], "medium"),
 ("Sacha Baron Cohen", ["Sacha Baron Cohen", "Baron Cohen", "Borat", "Ali G"], "easy"), ("Giles Coren", ["Giles Coren", "Coren"], "hard"),
 ("Kirsty Gallacher", ["Kirsty Gallacher", "Gallacher"], "hard"), ("Gail Porter", ["Gail Porter", "Porter"], "medium"),
]
NO_PICTURE = {"Bob Holness", "Magnus Magnusson", "Larry Grayson", "Dale Winton", "Michael Aspel", "Richard Whiteley", "Bob Monkhouse", "Matthew Kelly", "Mel Giedroyc"}
RETIRED = {"Roy Walker", "Des O'Connor"}
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-19.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
