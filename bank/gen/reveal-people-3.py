# Bank session 9 Oct 2026 (second pass): more Picture Reveal faces -> bank/reveal-people-3.json
# (Wikipedia title, accepted answers, difficulty). Nobody already in the live bank. Leans on people whose Wikipedia
# lead photo is a portrait (actors, presenters, politicians, painted portraits): reviewers rejected distant stage
# and race shots, and local gimmes, before. Stock with PEOPLE=bank/reveal-people-3.json node tools/reveal-stock.mjs
import json, os
P = [
 # film
 ("Kevin Bacon", ["Kevin Bacon", "Bacon"], "medium"), ("Nicolas Cage", ["Nicolas Cage", "Nic Cage", "Cage"], "medium"), ("Halle Berry", ["Halle Berry", "Berry"], "medium"),
 ("Cameron Diaz", ["Cameron Diaz", "Diaz"], "medium"), ("Drew Barrymore", ["Drew Barrymore", "Barrymore"], "medium"), ("Reese Witherspoon", ["Reese Witherspoon", "Witherspoon"], "medium"),
 ("Gwyneth Paltrow", ["Gwyneth Paltrow", "Paltrow"], "medium"), ("Natalie Portman", ["Natalie Portman", "Portman"], "medium"), ("Christopher Walken", ["Christopher Walken", "Walken"], "hard"),
 ("Steve Martin", ["Steve Martin"], "medium"), ("Michael J. Fox", ["Michael J. Fox", "Michael J Fox", "Michael Fox"], "medium"), ("Tom Selleck", ["Tom Selleck", "Selleck"], "medium"),
 ("Jeff Goldblum", ["Jeff Goldblum", "Goldblum"], "medium"), ("Joaquin Phoenix", ["Joaquin Phoenix", "Phoenix"], "hard"), ("Christian Bale", ["Christian Bale", "Bale"], "medium"),
 ("Gal Gadot", ["Gal Gadot", "Gadot"], "medium"), ("Chris Pratt", ["Chris Pratt", "Pratt"], "medium"), ("Mark Ruffalo", ["Mark Ruffalo", "Ruffalo"], "hard"),
 ("Paul Rudd", ["Paul Rudd", "Rudd"], "medium"), ("Jamie Foxx", ["Jamie Foxx", "Foxx"], "medium"), ("Kevin Hart", ["Kevin Hart", "Hart"], "medium"),
 ("Owen Wilson", ["Owen Wilson"], "medium"), ("Kristen Stewart", ["Kristen Stewart", "Stewart"], "medium"), ("Anya Taylor-Joy", ["Anya Taylor-Joy", "Anya Taylor Joy"], "hard"),
 ("Saoirse Ronan", ["Saoirse Ronan", "Ronan"], "hard"), ("Andrew Garfield", ["Andrew Garfield", "Garfield"], "medium"),
 # British TV and comedy
 ("Lenny Henry", ["Lenny Henry"], "easy"), ("Lee Evans (comedian)", ["Lee Evans"], "medium"), ("Jason Manford", ["Jason Manford", "Manford"], "medium"),
 ("Rhod Gilbert", ["Rhod Gilbert"], "hard"), ("Joel Dommett", ["Joel Dommett", "Dommett"], "hard"),
 ("Adrian Edmondson", ["Adrian Edmondson", "Ade Edmondson", "Edmondson"], "hard"), ("Ricky Tomlinson", ["Ricky Tomlinson", "Tomlinson"], "medium"), ("Jennifer Saunders", ["Jennifer Saunders", "Saunders"], "medium"),
 ("Vic Reeves", ["Vic Reeves", "Jim Moir"], "hard"), ("Amanda Holden", ["Amanda Holden", "Holden"], "easy"), ("Alesha Dixon", ["Alesha Dixon", "Dixon"], "medium"),
 ("Louis Walsh", ["Louis Walsh", "Walsh"], "medium"), ("Dannii Minogue", ["Dannii Minogue", "Danni Minogue"], "medium"), ("Craig Revel Horwood", ["Craig Revel Horwood", "Revel Horwood"], "medium"),
 ("Shirley Ballas", ["Shirley Ballas", "Ballas"], "medium"), ("Len Goodman", ["Len Goodman", "Goodman"], "medium"), ("Bruno Tonioli", ["Bruno Tonioli", "Tonioli", "Bruno"], "medium"),
 ("Anton Du Beke", ["Anton Du Beke", "Anton du Beke"], "medium"), ("Motsi Mabuse", ["Motsi Mabuse", "Mabuse"], "hard"), ("Gok Wan", ["Gok Wan"], "medium"),
 ("Heston Blumenthal", ["Heston Blumenthal", "Heston", "Blumenthal"], "medium"), ("Marco Pierre White", ["Marco Pierre White"], "hard"), ("James Martin (chef)", ["James Martin"], "hard"),
 # music
 ("Sam Smith", ["Sam Smith"], "medium"), ("Jason Donovan", ["Jason Donovan", "Donovan"], "medium"), ("Simon Le Bon", ["Simon Le Bon", "Le Bon"], "hard"),
 ("Björk", ["Björk", "Bjork"], "medium"), ("Prince (musician)", ["Prince (the singer)", "Prince"], "medium"), ("Christina Aguilera", ["Christina Aguilera", "Aguilera"], "medium"),
 ("Enrique Iglesias", ["Enrique Iglesias", "Iglesias", "Enrique"], "medium"), ("Frank Sinatra", ["Frank Sinatra", "Sinatra"], "medium"), ("Johnny Cash", ["Johnny Cash"], "medium"),
 ("Kenny Rogers", ["Kenny Rogers"], "hard"), ("Morrissey", ["Morrissey"], "hard"), ("Noddy Holder", ["Noddy Holder", "Holder"], "medium"),
 # sport
 ("Mohamed Salah", ["Mohamed Salah", "Mo Salah", "Salah"], "easy"), ("Kevin De Bruyne", ["Kevin De Bruyne", "De Bruyne"], "medium"), ("Virgil van Dijk", ["Virgil van Dijk", "Van Dijk"], "medium"),
 ("Son Heung-min", ["Son Heung-min", "Son"], "medium"), ("Neymar", ["Neymar"], "medium"), ("Ronaldinho", ["Ronaldinho"], "medium"),
 ("Paul Scholes", ["Paul Scholes", "Scholes"], "medium"), ("Jamie Carragher", ["Jamie Carragher", "Carragher"], "medium"), ("Peter Schmeichel", ["Peter Schmeichel", "Schmeichel"], "medium"),
 ("David Seaman", ["David Seaman", "Seaman"], "medium"), ("Shane Warne", ["Shane Warne", "Warne"], "medium"), ("Kevin Pietersen", ["Kevin Pietersen", "Pietersen", "KP"], "medium"),
 ("Stuart Broad", ["Stuart Broad", "Broad"], "hard"), ("Seve Ballesteros", ["Seve Ballesteros", "Seve", "Ballesteros"], "hard"), ("Venus Williams", ["Venus Williams"], "medium"),
 ("Boris Becker", ["Boris Becker", "Becker"], "medium"), ("Ricky Hatton", ["Ricky Hatton", "Hatton"], "medium"), ("Joe Calzaghe", ["Joe Calzaghe", "Calzaghe"], "hard"),
 ("Sebastian Coe", ["Sebastian Coe", "Seb Coe", "Lord Coe", "Coe"], "medium"), ("Stephen Hendry", ["Stephen Hendry", "Hendry"], "medium"), ("Damon Hill", ["Damon Hill"], "medium"),
 ("Max Verstappen", ["Max Verstappen", "Verstappen"], "medium"),
 # public life and history
 ("Nigel Farage", ["Nigel Farage", "Farage"], "easy"), ("Liz Truss", ["Liz Truss", "Truss"], "easy"), ("Jeremy Corbyn", ["Jeremy Corbyn", "Corbyn"], "easy"),
 ("John Major", ["John Major"], "medium"), ("Angela Merkel", ["Angela Merkel", "Merkel"], "medium"), ("Emmanuel Macron", ["Emmanuel Macron", "Macron"], "medium"),
 ("Volodymyr Zelenskyy", ["Volodymyr Zelenskyy", "Zelenskyy", "Zelensky"], "easy"), ("Bill Clinton", ["Bill Clinton", "Clinton"], "easy"), ("Ronald Reagan", ["Ronald Reagan", "Reagan"], "medium"),
 ("Mikhail Gorbachev", ["Mikhail Gorbachev", "Gorbachev"], "medium"), ("Henry VIII", ["Henry VIII", "Henry the Eighth", "Henry 8th"], "easy"), ("Elizabeth I", ["Elizabeth the First", "Elizabeth I", "Queen Elizabeth I"], "medium"),
 ("Queen Victoria", ["Queen Victoria", "Victoria"], "medium"), ("Marie Curie", ["Marie Curie", "Curie"], "hard"), ("Isaac Newton", ["Isaac Newton", "Newton"], "medium"),
 ("William Shakespeare", ["William Shakespeare", "Shakespeare"], "easy"), ("Vincent van Gogh", ["Vincent van Gogh", "Van Gogh"], "medium"), ("Napoleon", ["Napoleon", "Napoleon Bonaparte", "Bonaparte"], "medium"),
 ("Kim Kardashian", ["Kim Kardashian", "Kardashian"], "medium"),
]
# Stocked, then retired after a contact-sheet check (face too small, full-length painting, action/stage shot, or masked):
RETIRED = {"Björk", "Henry VIII", "Heston Blumenthal", "Elizabeth I", "Napoleon", "Seve Ballesteros", "Stephen Hendry",
           "Rhod Gilbert", "Len Goodman", "Paul Scholes", "Dannii Minogue", "Motsi Mabuse", "Jason Donovan"}
P = [p for p in P if p[0] not in RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": a, "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
