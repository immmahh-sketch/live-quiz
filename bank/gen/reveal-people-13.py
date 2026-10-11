# Bank session 11 Oct 2026 (twelfth pass): more Picture Reveal faces -> bank/reveal-people-13.json
# (Wikipedia title, accepted answers, difficulty). Each name was checked against every answer already in the live bank
# and every name retired or not stocked in earlier passes. Stock with PEOPLE=bank/reveal-people-13.json node tools/reveal-stock.mjs, then contact-sheet them.
import json, os
P = [
 # sport
 ("Charlotte Dujardin", ["Charlotte Dujardin", "Dujardin"], "hard"), ("Alistair Brownlee", ["Alistair Brownlee"], "medium"), ("Jonny Brownlee", ["Jonny Brownlee"], "hard"),
 ("Helen Glover (rower)", ["Helen Glover"], "hard"), ("Emma Finucane", ["Emma Finucane", "Finucane"], "hard"), ("Mike Tindall", ["Mike Tindall", "Tindall"], "medium"),
 # royals
 ("Prince Edward, Duke of Edinburgh", ["Prince Edward", "Edward", "Duke of Edinburgh"], "medium"), ("Zara Tindall", ["Zara Tindall", "Zara Phillips"], "medium"),
 # politics and public life
 ("Ed Davey", ["Ed Davey", "Sir Ed Davey", "Davey"], "medium"), ("Michelle O'Neill", ["Michelle O'Neill"], "hard"), ("Wes Streeting", ["Wes Streeting", "Streeting"], "medium"),
 ("Yvette Cooper", ["Yvette Cooper"], "medium"), ("Dominic Raab", ["Dominic Raab", "Raab"], "medium"), ("Suella Braverman", ["Suella Braverman", "Braverman"], "medium"),
 ("Chris Whitty", ["Chris Whitty", "Professor Chris Whitty", "Whitty"], "easy"), ("Patrick Vallance", ["Patrick Vallance", "Sir Patrick Vallance", "Vallance"], "medium"),
 # entertainment
 ("Jorja Smith", ["Jorja Smith"], "hard"), ("Daisy Edgar-Jones", ["Daisy Edgar-Jones"], "medium"), ("Emily Atack", ["Emily Atack"], "medium"),
 ("Olly Alexander", ["Olly Alexander", "Years & Years"], "medium"), ("Mae Muller", ["Mae Muller"], "hard"),
]
# After stocking: names skipped as already in the bank or with no usable photo, and those retired from the contact sheet.
ALREADY = set()
RETIRED = {"Charlotte Dujardin", "Emily Atack", "Jorja Smith"}  # face too small: on horseback, full-length stage costume, dim stage shot
P = [p for p in P if p[0] not in ALREADY | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
