# Bank session 11 Oct 2026: more Categorise questions -> bank/sort-25.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})


s("Football", ["managers", "Spain", "Italy"], "medium", "A Spanish football manager or an Italian one?", "Spanish", "Italian", ["Pep Guardiola", "Mikel Arteta", "Unai Emery", "Rafael Benítez"], ["Carlo Ancelotti", "Antonio Conte", "Claudio Ranieri", "Roberto Mancini"])
s("World geography", ["boroughs", "New York", "London"], "medium", "A New York borough or a London borough?", "New York", "London", ["Brooklyn", "Queens", "The Bronx", "Staten Island"], ["Camden", "Hackney", "Lambeth", "Islington"])
s("Animals", ["horses", "cattle", "breeds"], "medium", "A breed of horse or a breed of cattle?", "Horse", "Cattle", ["Shire", "Clydesdale", "Shetland", "Appaloosa"], ["Hereford", "Aberdeen Angus", "Highland", "Jersey"])
s("Football", ["Manchester United", "Manchester City", "legends"], "easy", "A Manchester United legend or a Manchester City legend?", "Manchester United", "Manchester City", ["Bobby Charlton", "George Best", "Ryan Giggs", "Paul Scholes"], ["Colin Bell", "Sergio Agüero", "Vincent Kompany", "David Silva"])
s("Film", ["James Bond", "villains", "henchmen"], "medium", "A Bond villain or a Bond villain's henchman?", "Villain", "Henchman", ["Blofeld", "Goldfinger", "Scaramanga", "Le Chiffre"], ["Oddjob", "Jaws", "Nick Nack", "May Day"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-25.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
