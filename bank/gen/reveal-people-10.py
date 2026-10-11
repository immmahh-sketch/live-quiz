# Bank session 11 Oct 2026 (ninth pass): more Picture Reveal faces -> bank/reveal-people-10.json
# (Wikipedia title, accepted answers, difficulty). Each name was checked against every answer already in the live bank.
# Stock with PEOPLE=bank/reveal-people-10.json node tools/reveal-stock.mjs, then contact-sheet them.
import json, os
P = [
 # TV, news and food
 ("Nick Robinson (journalist)", ["Nick Robinson"], "medium"), ("Laura Kuenssberg", ["Laura Kuenssberg", "Kuenssberg"], "medium"), ("Emily Maitlis", ["Emily Maitlis", "Maitlis"], "medium"),
 ("Naga Munchetty", ["Naga Munchetty", "Munchetty"], "medium"), ("Charlie Stayt", ["Charlie Stayt"], "hard"), ("Dan Walker (broadcaster)", ["Dan Walker"], "medium"),
 ("Louise Minchin", ["Louise Minchin"], "medium"), ("Bill Turnbull", ["Bill Turnbull"], "medium"), ("Jenny Ryan (quizzer)", ["Jenny Ryan", "The Vixen"], "medium"),
 ("Sara Pascoe", ["Sara Pascoe"], "hard"), ("Roisin Conaty", ["Roisin Conaty"], "hard"), ("David Baddiel", ["David Baddiel", "Baddiel"], "medium"),
 ("Michaela Strachan", ["Michaela Strachan"], "medium"), ("Charlie Dimmock", ["Charlie Dimmock"], "medium"), ("Si King", ["Si King", "Simon King"], "medium"),
 ("Dave Myers (presenter)", ["Dave Myers"], "medium"), ("Tom Kerridge", ["Tom Kerridge", "Kerridge"], "medium"), ("Lisa Faulkner", ["Lisa Faulkner"], "medium"),
 ("Keith Floyd", ["Keith Floyd", "Floyd"], "hard"), ("Nigel Slater", ["Nigel Slater"], "hard"), ("Marcus Wareing", ["Marcus Wareing", "Wareing"], "medium"),
 ("Michel Roux Jr", ["Michel Roux Jr", "Michel Roux"], "medium"), ("Grace Dent", ["Grace Dent"], "medium"), ("Sarah Beeny", ["Sarah Beeny"], "medium"),
 ("George Clarke (architect)", ["George Clarke"], "medium"), ("Judy Finnigan", ["Judy Finnigan"], "medium"), ("Ruth Langsford", ["Ruth Langsford"], "medium"),
 ("Zara Larsson", ["Zara Larsson"], "hard"), ("Emeli Sandé", ["Emeli Sande", "Emeli Sandé"], "medium"),
 # sport
 ("Mark Wood (cricketer)", ["Mark Wood"], "hard"), ("Moeen Ali", ["Moeen Ali", "Moeen", "Mo Ali"], "medium"), ("Chris Woakes", ["Chris Woakes", "Woakes"], "hard"),
 ("Eoin Morgan", ["Eoin Morgan"], "medium"), ("Ellis Genge", ["Ellis Genge", "Genge"], "hard"), ("Marcus Smith (rugby union)", ["Marcus Smith"], "hard"),
 ("Antoine Dupont", ["Antoine Dupont", "Dupont"], "hard"), ("Alun Wyn Jones", ["Alun Wyn Jones"], "medium"), ("Shane Williams", ["Shane Williams"], "medium"),
 ("Laura Muir", ["Laura Muir"], "medium"), ("Matthew Hudson-Smith", ["Matt Hudson-Smith", "Matthew Hudson-Smith"], "hard"), ("Alex Yee", ["Alex Yee"], "hard"),
 ("Hannah Cockroft", ["Hannah Cockroft"], "medium"), ("Ben Ainslie", ["Ben Ainslie", "Ainslie"], "medium"), ("Rebecca Adlington", ["Rebecca Adlington", "Becky Adlington"], "medium"),
 ("Victoria Pendleton", ["Victoria Pendleton", "Pendleton"], "medium"), ("Colin Jackson", ["Colin Jackson"], "medium"), ("Sebastian Coe", ["Seb Coe", "Sebastian Coe", "Lord Coe"], "medium"),
 ("Matthew Pinsent", ["Matthew Pinsent", "Pinsent"], "medium"), ("Ian Thorpe", ["Ian Thorpe", "Thorpe"], "medium"), ("Greg Rutherford", ["Greg Rutherford"], "medium"),
 ("Nigel Benn", ["Nigel Benn"], "medium"), ("Naseem Hamed", ["Naseem Hamed", "Prince Naseem", "Prince Naz"], "medium"),

]
# After stocking: no usable or matching photo for these, or skipped as already in the bank under another spelling,
NOT_STOCKED = {"Charlie Stayt", "Bill Turnbull", "Jenny Ryan (quizzer)", "Charlie Dimmock", "Si King", "Keith Floyd", "Nigel Slater", "Sarah Beeny",
               "Judy Finnigan", "Emeli Sandé", "Matthew Hudson-Smith"}
# and these were retired from the contact sheet (action shots, small faces, or a photo of a plaque instead of the person).
RETIRED = {"Alex Yee", "Dave Myers (presenter)", "George Clarke (architect)", "Greg Rutherford", "Hannah Cockroft", "Mark Wood (cricketer)",
           "Shane Williams", "Laura Muir", "Rebecca Adlington"}
P = [p for p in P if p[0] not in NOT_STOCKED | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
