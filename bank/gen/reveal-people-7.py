# Bank session 10 Oct 2026 (sixth pass): more Picture Reveal faces -> bank/reveal-people-7.json
# (Wikipedia title, accepted answers, difficulty). Nobody already in the live bank; mostly people whose Wikipedia lead
# photo is a portrait. Stock with PEOPLE=bank/reveal-people-7.json node tools/reveal-stock.mjs, then contact-sheet them.
import json, os
P = [
 # British TV and film
 ("Jamie Dornan", ["Jamie Dornan", "Dornan"], "medium"), ("Andrew Scott (actor)", ["Andrew Scott"], "medium"), ("James McAvoy", ["James McAvoy", "McAvoy"], "medium"),
 ("Michael Fassbender", ["Michael Fassbender", "Fassbender"], "medium"), ("Colin Farrell", ["Colin Farrell", "Farrell"], "medium"), ("Jason Isaacs", ["Jason Isaacs", "Isaacs"], "hard"),
 ("Phoebe Waller-Bridge", ["Phoebe Waller-Bridge", "Waller-Bridge"], "medium"), ("Vicky McClure", ["Vicky McClure", "McClure"], "medium"), ("Martin Compston", ["Martin Compston", "Compston"], "medium"),
 ("Adrian Dunbar", ["Adrian Dunbar", "Dunbar"], "medium"), ("Keeley Hawes", ["Keeley Hawes", "Hawes"], "medium"), ("Sarah Lancashire", ["Sarah Lancashire", "Lancashire"], "medium"),
 ("Jonathan Bailey (actor)", ["Jonathan Bailey"], "medium"), ("Nicola Coughlan", ["Nicola Coughlan", "Coughlan"], "medium"), ("Ruth Jones", ["Ruth Jones"], "medium"),
 # Hollywood
 ("Jodie Foster", ["Jodie Foster", "Foster"], "medium"), ("Glenn Close", ["Glenn Close"], "medium"), ("Bradley Cooper", ["Bradley Cooper", "Cooper"], "medium"),
 ("Jake Gyllenhaal", ["Jake Gyllenhaal", "Gyllenhaal"], "medium"), ("Lupita Nyong'o", ["Lupita Nyong'o", "Lupita Nyongo"], "medium"), ("Melissa McCarthy", ["Melissa McCarthy", "McCarthy"], "medium"),
 ("Tina Fey", ["Tina Fey", "Fey"], "medium"), ("Ethan Hawke", ["Ethan Hawke", "Hawke"], "medium"), ("Jennifer Coolidge", ["Jennifer Coolidge", "Coolidge"], "medium"),
 # football and sport
 ("Brian Clough", ["Brian Clough", "Clough", "Cloughie"], "medium"), ("Jack Charlton", ["Jack Charlton", "Big Jack"], "medium"), ("Bill Shankly", ["Bill Shankly", "Shankly"], "hard"),
 ("Sven-Göran Eriksson", ["Sven-Göran Eriksson", "Sven-Goran Eriksson", "Sven Goran Eriksson", "Sven"], "medium"), ("Roy Hodgson", ["Roy Hodgson", "Hodgson"], "medium"), ("Tony Adams", ["Tony Adams"], "medium"),
 ("Alan Hansen", ["Alan Hansen", "Hansen"], "medium"), ("Ian Rush", ["Ian Rush", "Rush"], "medium"), ("John Barnes", ["John Barnes", "Barnes"], "medium"),
 ("Stuart Pearce", ["Stuart Pearce", "Pearce", "Psycho"], "medium"), ("Jamie Vardy", ["Jamie Vardy", "Vardy"], "easy"), ("Harry Maguire", ["Harry Maguire", "Maguire"], "easy"),
 ("Trent Alexander-Arnold", ["Trent Alexander-Arnold", "Trent Alexander Arnold", "Alexander-Arnold"], "easy"), ("Paul Collingwood", ["Paul Collingwood", "Collingwood"], "hard"), ("Jonathan Edwards (athlete)", ["Jonathan Edwards"], "medium"),
 # music
 ("Seal (musician)", ["Seal"], "medium"), ("Sade (singer)", ["Sade", "Sade Adu"], "medium"), ("Alison Moyet", ["Alison Moyet", "Moyet"], "hard"),
 ("Kim Wilde", ["Kim Wilde", "Wilde"], "medium"), ("Toyah Willcox", ["Toyah Willcox", "Toyah"], "medium"), ("Will Young", ["Will Young"], "medium"),
 ("Shayne Ward", ["Shayne Ward"], "medium"), ("Alexandra Burke", ["Alexandra Burke", "Burke"], "medium"), ("Florence Welch", ["Florence Welch", "Florence"], "medium"),
 ("Emeli Sandé", ["Emeli Sandé", "Emeli Sande"], "medium"), ("KT Tunstall", ["KT Tunstall", "K.T. Tunstall", "Tunstall"], "hard"), ("Tom Grennan", ["Tom Grennan", "Grennan"], "medium"),
 ("Ian Brown", ["Ian Brown"], "hard"), ("Robert Smith (musician)", ["Robert Smith"], "medium"),
]
NO_PHOTO = {"Bill Shankly"}
# Stocked, then retired after the contact sheet (action/stage shot, sunglasses, or face too small or dark):
RETIRED = {"Alan Hansen", "Alison Moyet", "Jack Charlton", "James McAvoy", "Jonathan Bailey (actor)", "KT Tunstall", "Kim Wilde", "Michael Fassbender", "Paul Collingwood", "Shayne Ward", "Toyah Willcox", "Will Young"}
P = [p for p in P if p[0] not in RETIRED | NO_PHOTO]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": a, "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
