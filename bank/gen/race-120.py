# Bank session 10 Oct 2026: 2 more general races -> bank/race-120.json (art movements, ballets). 20 rows each, target 10; wrong options are
# the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("which art movement was this artist part of?", "Art", "hard", ["art", "artists", "movements"], [
 ("Claude Monet", "Impressionism", ["Realism", "Symbolism", "Rococo"]),
 ("Pablo Picasso, with Georges Braque", "Cubism", ["Vorticism", "Constructivism", "Symbolism"]),
 ("Salvador Dalí", "Surrealism", ["Symbolism", "Mannerism", "Constructivism"]),
 ("Andy Warhol", "Pop Art", ["Minimalism", "Conceptual art", "Photorealism"]),
 ("Jackson Pollock", "Abstract Expressionism", ["Minimalism", "Conceptual art", "Constructivism"]),
 ("Vincent van Gogh", "Post-Impressionism", ["Realism", "Symbolism", "Neoclassicism"]),
 ("Caravaggio", "Baroque", ["Mannerism", "Rococo", "Neoclassicism"]),
 ("Marcel Duchamp, with his urinal 'Fountain'", "Dada", ["Vorticism", "Constructivism", "Minimalism"]),
 ("Umberto Boccioni", "Futurism", ["Vorticism", "Constructivism", "Symbolism"]),
 ("Piet Mondrian", "De Stijl", ["Bauhaus", "Constructivism", "Minimalism"]),
 ("Henri Matisse", "Fauvism", ["Symbolism", "Rococo", "Realism"]),
 ("Edvard Munch", "Expressionism", ["Realism", "Rococo", "Mannerism"]),
 ("John Constable", "Romanticism", ["Neoclassicism", "Rococo", "Mannerism"]),
 ("Damien Hirst", "Young British Artists", ["Minimalism", "Photorealism", "Arts and Crafts"]),
 ("Mark Rothko", "Colour Field", ["Minimalism", "Photorealism", "Constructivism"]),
 ("Dante Gabriel Rossetti", "Pre-Raphaelites", ["Neoclassicism", "Rococo", "Symbolism"]),
 ("Georges Seurat", "Pointillism", ["Realism", "Rococo", "Symbolism"]),
 ("Gustav Klimt", "Vienna Secession", ["Bauhaus", "Art Deco", "Constructivism"]),
 ("Sandro Botticelli", "Renaissance", ["Mannerism", "Gothic", "Rococo"]),
 ("Bridget Riley", "Op Art", ["Minimalism", "Photorealism", "Constructivism"])])

race("which ballet is this?", "Theatre", "hard", ["ballet", "dance", "music"], [
 ("Odette and Odile, danced by the same ballerina", "Swan Lake", ["Raymonda", "Les Sylphides", "Sylvia"]),
 ("Clara and the Sugar Plum Fairy", "The Nutcracker", ["Paquita", "Sylvia", "Raymonda"]),
 ("A peasant girl dies of a broken heart and returns as a ghostly Wili", "Giselle", ["Les Sylphides", "Paquita", "Raymonda"]),
 ("Princess Aurora pricks her finger on a spindle", "The Sleeping Beauty", ["Raymonda", "Sylvia", "Paquita"]),
 ("A life-size dancing doll, to music by Delibes", "Coppélia", ["Sylvia", "Paquita", "La Fille mal gardée"]),
 ("A pagan sacrifice that caused a riot in Paris in 1913", "The Rite of Spring", ["Les Noces", "Apollo", "Daphnis and Chloé"]),
 ("A magical bird with glowing feathers, by Stravinsky", "The Firebird", ["Apollo", "Les Noces", "Agon"]),
 ("A puppet who comes to life at a Russian fair", "Petrushka", ["Apollo", "Les Noces", "Agon"]),
 ("A slave revolt against Rome, by Khachaturian", "Spartacus", ["Le Corsaire", "Raymonda", "Apollo"]),
 ("Prokofiev's star-crossed lovers in Verona", "Romeo and Juliet", ["Daphnis and Chloé", "Sylvia", "Le Corsaire"]),
 ("Prokofiev's girl with the glass slipper", "Cinderella", ["Raymonda", "Sylvia", "La Fille mal gardée"]),
 ("A Scottish farmer bewitched by a forest spirit", "La Sylphide", ["Les Sylphides", "Raymonda", "Sylvia"]),
 ("A temple dancer in India and a warrior's broken vow", "La Bayadère", ["Le Corsaire", "Paquita", "Raymonda"]),
 ("Kitri and Basilio, from a Cervantes novel", "Don Quixote", ["Paquita", "Le Corsaire", "La Fille mal gardée"]),
 ("Crown Prince Rudolf's tragic affair, by Kenneth MacMillan", "Mayerling", ["Enigma Variations", "Façade", "Pineapple Poll"]),
 ("A young courtesan in 18th-century Paris, by MacMillan", "Manon", ["Enigma Variations", "Façade", "Pineapple Poll"]),
 ("Pushkin's bored aristocrat, choreographed by John Cranko", "Onegin", ["Raymonda", "Jewels", "Apollo"]),
 ("Ravel's ever-repeating, ever-louder piece, written as a ballet", "Boléro", ["Daphnis and Chloé", "La Valse", "Jewels"]),
 ("Dancing shoes that won't let their wearer stop", "The Red Shoes", ["The Dying Swan", "Jewels", "Façade"]),
 ("A tumble down a rabbit hole, for the Royal Ballet in 2011", "Alice's Adventures in Wonderland", ["The Winter's Tale", "Jewels", "Enigma Variations"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-120.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
