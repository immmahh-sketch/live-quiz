# Bank session 12 Oct 2026: new Wipeout boards -> bank/wipeout-79.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: blues and rock'n'roll greats from the same era
board("Jazz musicians and singers", "Music", "medium", ["jazz", "music"],
 ["Louis Armstrong", "Miles Davis", "Ella Fitzgerald", "Billie Holiday", "Duke Ellington", "Charlie Parker", "Dizzy Gillespie", "John Coltrane", "Count Basie", "Benny Goodman", "Thelonious Monk", "Chet Baker", "Dave Brubeck", "Herbie Hancock", "Jamie Cullum"],
 ["Muddy Waters", "B.B. King", "Chuck Berry", "Elvis Presley", "Little Richard"])
# decoys: the great soul acts of Stax, Atlantic and King, Motown's rivals
board("Acts who recorded for Motown", "Music", "medium", ["Motown", "soul", "music"],
 ["The Supremes", "The Temptations", "Marvin Gaye", "Stevie Wonder", "The Jackson 5", "Smokey Robinson", "The Four Tops", "Martha and the Vandellas", "Gladys Knight & the Pips", "The Marvelettes", "Mary Wells", "Diana Ross", "Lionel Richie", "The Commodores", "Rick James"],
 ["Otis Redding", "Aretha Franklin", "Wilson Pickett", "Sam & Dave", "James Brown"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-79.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
