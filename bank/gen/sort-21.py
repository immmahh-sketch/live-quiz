# Bank session 11 Oct 2026: 8 more Categorise questions -> bank/sort-18.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Food and drink", ["cakes", "France", "Austria"], "hard", "A French cake or an Austrian cake?", "French", "Austrian", ["Éclair", "Madeleine", "Macaron", "Mille-feuille"], ["Sachertorte", "Apple strudel", "Linzer torte", "Kaiserschmarrn"])
s("Sport", ["rugby", "Wales", "Ireland"], "medium", "A Welsh rugby legend or an Irish one?", "Wales", "Ireland", ["Gareth Edwards", "Shane Williams", "Alun Wyn Jones", "Leigh Halfpenny"], ["Brian O'Driscoll", "Johnny Sexton", "Paul O'Connell", "Keith Earls"])
s("Music", ["Queen", "David Bowie"], "medium", "A Queen song or a David Bowie song?", "Queen", "David Bowie", ["Radio Ga Ga", "Killer Queen", "I Want to Break Free", "We Are the Champions"], ["Space Oddity", "Ziggy Stardust", "Ashes to Ashes", "Rebel Rebel"])
s("Music", ["Simon & Garfunkel", "The Beach Boys", "1960s"], "medium", "A Simon & Garfunkel song or a Beach Boys song?", "Simon & Garfunkel", "Beach Boys", ["Mrs. Robinson", "The Sound of Silence", "Bridge Over Troubled Water", "The Boxer"], ["Good Vibrations", "Surfin' U.S.A.", "God Only Knows", "Wouldn't It Be Nice"])
s("Business", ["brands", "Japan", "South Korea"], "medium", "A Japanese brand or a South Korean brand?", "Japan", "South Korea", ["Sony", "Panasonic", "Toyota", "Nintendo"], ["Samsung", "LG", "Hyundai", "Kia"])
s("Business", ["brands", "Denmark", "Sweden"], "medium", "A Danish brand or a Swedish brand?", "Denmark", "Sweden", ["Lego", "Carlsberg", "Pandora", "Bang & Olufsen"], ["IKEA", "H&M", "Volvo", "Spotify"])
s("Football", ["London", "Midlands"], "easy", "A London club or a Midlands club?", "London", "Midlands", ["Fulham", "Brentford", "QPR", "Millwall"], ["Aston Villa", "Wolves", "West Brom", "Coventry City"])
s("Sport", ["Formula One", "Germany", "Finland"], "medium", "A German Formula One driver or a Finnish one?", "Germany", "Finland", ["Sebastian Vettel", "Michael Schumacher", "Nico Hülkenberg", "Ralf Schumacher"], ["Kimi Räikkönen", "Mika Häkkinen", "Valtteri Bottas", "Heikki Kovalainen"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
