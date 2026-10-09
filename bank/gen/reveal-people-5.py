# Bank session 9 Oct 2026 (fourth pass): more Picture Reveal faces -> bank/reveal-people-5.json
# (Wikipedia title, accepted answers, difficulty). Nobody already in the live bank; mostly people whose Wikipedia lead
# photo is a portrait. Stock with PEOPLE=bank/reveal-people-5.json node tools/reveal-stock.mjs, then contact-sheet them.
import json, os
P = [
 # soaps and British TV drama
 ("Ross Kemp", ["Ross Kemp", "Kemp"], "medium"), ("Steve McFadden", ["Steve McFadden", "McFadden"], "hard"), ("Adam Woodyatt", ["Adam Woodyatt", "Woodyatt"], "hard"),
 ("Shane Richie", ["Shane Richie", "Richie"], "medium"), ("Letitia Dean", ["Letitia Dean"], "hard"), ("Martine McCutcheon", ["Martine McCutcheon", "McCutcheon"], "medium"),
 ("Patsy Palmer", ["Patsy Palmer"], "hard"), ("Anita Dobson", ["Anita Dobson", "Dobson"], "hard"), ("William Roache", ["William Roache", "Bill Roache", "Roache"], "medium"),
 ("Helen Worth", ["Helen Worth"], "hard"), ("Sally Dynevor", ["Sally Dynevor", "Sally Whittaker"], "hard"), ("Penelope Keith", ["Penelope Keith"], "hard"),
 ("Felicity Kendal", ["Felicity Kendal", "Kendal"], "hard"), ("Lesley Joseph", ["Lesley Joseph"], "medium"), ("Su Pollard", ["Su Pollard", "Pollard"], "medium"),
 # US TV
 ("Jennifer Garner", ["Jennifer Garner", "Garner"], "medium"), ("Kate Hudson", ["Kate Hudson"], "medium"), ("Jessica Alba", ["Jessica Alba", "Alba"], "medium"),
 ("Eva Longoria", ["Eva Longoria", "Longoria"], "medium"), ("Sarah Jessica Parker", ["Sarah Jessica Parker", "SJP"], "medium"), ("Lisa Kudrow", ["Lisa Kudrow", "Kudrow"], "medium"),
 ("Courteney Cox", ["Courteney Cox", "Courtney Cox"], "medium"), ("Matthew Perry", ["Matthew Perry"], "medium"), ("David Schwimmer", ["David Schwimmer", "Schwimmer"], "medium"),
 ("Matt LeBlanc", ["Matt LeBlanc", "LeBlanc"], "medium"), ("Kelsey Grammer", ["Kelsey Grammer", "Grammer"], "medium"), ("Ted Danson", ["Ted Danson", "Danson"], "hard"),
 ("Bryan Cranston", ["Bryan Cranston", "Cranston"], "medium"), ("Aaron Paul", ["Aaron Paul"], "hard"), ("Kiefer Sutherland", ["Kiefer Sutherland", "Sutherland"], "medium"),
 # quiz shows and presenters
 ("Mark Labbett", ["Mark Labbett", "The Beast", "Labbett"], "easy"), ("Anne Hegerty", ["Anne Hegerty", "The Governess", "Hegerty"], "easy"), ("Shaun Wallace", ["Shaun Wallace", "The Dark Destroyer"], "medium"),
 ("Jenny Ryan", ["Jenny Ryan", "The Vixen"], "medium"), ("Paul Sinha", ["Paul Sinha", "The Sinnerman", "Sinha"], "easy"), ("Darragh Ennis", ["Darragh Ennis", "The Menace"], "medium"),
 ("Carol Vorderman", ["Carol Vorderman", "Vorderman"], "easy"), ("Rachel Riley", ["Rachel Riley", "Riley"], "easy"), ("Nick Hewer", ["Nick Hewer", "Hewer"], "medium"),
 ("Susie Dent", ["Susie Dent", "Dent"], "medium"), ("Victoria Coren Mitchell", ["Victoria Coren Mitchell", "Victoria Coren"], "medium"), ("Gyles Brandreth", ["Gyles Brandreth", "Brandreth"], "medium"),
 ("Rob Rinder", ["Rob Rinder", "Judge Rinder", "Rinder"], "medium"), ("Mary Beard", ["Mary Beard", "Beard"], "medium"), ("Chris Kamara", ["Chris Kamara", "Kammy"], "easy"),
 ("Jeff Stelling", ["Jeff Stelling", "Stelling"], "medium"), ("John Motson", ["John Motson", "Motty"], "medium"),
 # politics
 ("Ed Balls", ["Ed Balls"], "medium"), ("Angela Rayner", ["Angela Rayner", "Rayner"], "easy"), ("Matt Hancock", ["Matt Hancock", "Hancock"], "easy"),
 ("Ann Widdecombe", ["Ann Widdecombe", "Widdecombe"], "medium"), ("John Bercow", ["John Bercow", "Bercow"], "easy"), ("Sadiq Khan", ["Sadiq Khan"], "easy"),
 ("Andy Burnham", ["Andy Burnham", "Burnham"], "medium"), ("Alastair Campbell", ["Alastair Campbell"], "medium"), ("Priti Patel", ["Priti Patel", "Patel"], "medium"),
 ("Jeremy Hunt", ["Jeremy Hunt", "Hunt"], "medium"),
 # pop
 ("Mark Owen", ["Mark Owen"], "medium"), ("Howard Donald", ["Howard Donald"], "hard"), ("Shane Filan", ["Shane Filan", "Filan"], "medium"),
 ("Nicky Byrne", ["Nicky Byrne"], "hard"), ("Duncan James", ["Duncan James"], "hard"), ("Nadine Coyle", ["Nadine Coyle", "Coyle"], "medium"),
 ("Nicola Roberts", ["Nicola Roberts"], "medium"), ("Kimberley Walsh", ["Kimberley Walsh"], "medium"), ("Sarah Harding", ["Sarah Harding"], "medium"),
 ("Jade Thirlwall", ["Jade Thirlwall", "Jade"], "medium"), ("Perrie Edwards", ["Perrie Edwards", "Perrie"], "medium"), ("Jesy Nelson", ["Jesy Nelson"], "medium"),
 ("Leigh-Anne Pinnock", ["Leigh-Anne Pinnock", "Leigh-Anne"], "medium"),
 # sport
 ("Jermain Defoe", ["Jermain Defoe", "Defoe"], "medium"), ("Steph Houghton", ["Steph Houghton", "Houghton"], "hard"), ("Ellen White", ["Ellen White"], "medium"),
 ("Mark Selby", ["Mark Selby", "Selby"], "hard"), ("Justin Rose", ["Justin Rose"], "hard"), ("Ian Poulter", ["Ian Poulter", "Poulter"], "medium"),
 ("Tommy Fleetwood", ["Tommy Fleetwood", "Fleetwood"], "medium"), ("Gareth Thomas (rugby, born 1974)", ["Gareth Thomas", "Alfie"], "medium"), ("Carl Froch", ["Carl Froch", "Froch"], "medium"),
 ("David Haye", ["David Haye", "Haye"], "medium"), ("Amir Khan (boxer)", ["Amir Khan"], "medium"),
]
NO_PHOTO = {"Letitia Dean", "Helen Worth", "Sally Dynevor", "Jenny Ryan", "Darragh Ennis"}
# Stocked, then retired after the contact sheet (action/stage shot, sunglasses, or face too small or dark):
RETIRED = {"Ian Poulter", "Amir Khan (boxer)", "David Haye", "Ellen White", "Mark Owen", "Nadine Coyle", "Nicola Roberts", "Sarah Harding",
           "Lesley Joseph", "Patsy Palmer", "Felicity Kendal", "Howard Donald", "Carl Froch"}
P = [p for p in P if p[0] not in RETIRED | NO_PHOTO]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": a, "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
