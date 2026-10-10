# Bank session 10 Oct 2026: 3 more general races -> bank/race-143.json (music genres, art words, jewellery words). 20 rows each, target 10; wrong options are
# the same kind of thing, never another row's right answer, and never also right for that row. The art race leaves out
# fresco and still life, which 'art attack' already asks.
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

race("which music genre is this?", "Music", "medium", ["music", "genres"], [
 ("Bob Marley's laid-back Jamaican sound", "Reggae", ["Zydeco", "Fado", "Salsa"]),
 ("Seattle's sludgy early-90s rock of Nirvana and Pearl Jam", "Grunge", ["Nu metal", "Glam rock", "Krautrock"]),
 ("Mid-90s British guitar music of Blur, Oasis and Pulp", "Britpop", ["New Romantic", "Glam rock", "Skiffle"]),
 ("Fast, loud, three-chord rebellion of the Sex Pistols", "Punk", ["New Romantic", "Skiffle", "Rockabilly"]),
 ("The upbeat Jamaican sound revived by the Specials and Madness", "Ska", ["Zydeco", "Salsa", "Highlife"]),
 ("Glittering 1970s dance music of the Bee Gees and Donna Summer", "Disco", ["Swing", "Bebop", "Synthwave"]),
 ("The Detroit soul label of the Supremes and Stevie Wonder", "Motown", ["Doo-wop", "Bebop", "Rockabilly"]),
 ("Banjo-and-fiddle country music from Kentucky", "Bluegrass", ["Zydeco", "Cajun", "Rockabilly"]),
 ("Fast, gritty London rap of Dizzee Rascal and Stormzy", "Grime", ["Dubstep", "Garage", "Trap"]),
 ("Super-fast breakbeats with heavy basslines, born in UK raves", "Drum and bass", ["Dubstep", "Trance", "Techno"]),
 ("The moody, slow Bristol sound of Massive Attack and Portishead", "Trip hop", ["Acid jazz", "Lo-fi", "Synthwave"]),
 ("Slick South Korean pop of BTS and Blackpink", "K-pop", ["J-pop", "Afrobeat", "Synthwave"]),
 ("Rare American soul records danced to all night at Wigan Casino", "Northern soul", ["Acid jazz", "Doo-wop", "Swing"]),
 ("The late-80s Manchester scene of the Stone Roses and Happy Mondays", "Madchester", ["New Romantic", "Krautrock", "Skiffle"]),
 ("Dreamy, noisy guitar music played staring at the floor, like My Bloody Valentine", "Shoegaze", ["Krautrock", "Lo-fi", "Synthwave"]),
 ("Heart-on-sleeve 2000s rock of My Chemical Romance", "Emo", ["Nu metal", "Glam rock", "Skiffle"]),
 ("Christian choir music rooted in African-American churches", "Gospel", ["Doo-wop", "Swing", "Bebop"]),
 ("Gentle Brazilian jazz, like 'The Girl from Ipanema'", "Bossa nova", ["Tango", "Fado", "Salsa"]),
 ("Fiery Spanish guitar, singing and dancing from Andalusia", "Flamenco", ["Tango", "Fado", "Mariachi"]),
 ("Trinidad's witty, rhythmic songs, often with steel pans", "Calypso", ["Mariachi", "Tango", "Highlife"])])

race("what's this art word?", "Art", "medium", ["art", "painting", "words"], [
 ("A huge painting straight onto a wall", "Mural", ["Diorama", "Plinth", "Maquette"]),
 ("A picture made from tiny tiles of glass or stone", "Mosaic", ["Impasto", "Gesso", "Pointillism"]),
 ("Scraps of paper and photos glued together into one picture", "Collage", ["Diorama", "Impasto", "Gesso"]),
 ("A picture of a person, usually showing their face", "Portrait", ["Diorama", "Maquette", "Frieze"]),
 ("A painting of the countryside", "Landscape", ["Diorama", "Frieze", "Maquette"]),
 ("Paint you thin with water, often used for soft washes", "Watercolour", ["Tempera", "Impasto", "Gesso"]),
 ("The wooden stand that holds a painting while you work", "Easel", ["Plinth", "Gesso", "Fixative"]),
 ("The board an artist mixes paints on", "Palette", ["Plinth", "Gesso", "Fixative"]),
 ("Stretched cloth that an oil painting is made on", "Canvas", ["Gesso", "Plinth", "Fixative"]),
 ("Art carved or modelled in three dimensions", "Sculpture", ["Fixative", "Impasto", "Chiaroscuro"]),
 ("A print made from a metal plate scratched and bathed in acid", "Etching", ["Tempera", "Impasto", "Gesso"]),
 ("Words or pictures sprayed on walls, like Banksy's", "Graffiti", ["Trompe l'oeil", "Chiaroscuro", "Sfumato"]),
 ("An artist's picture of themselves, like Van Gogh's with his bandaged ear", "Self-portrait", ["Diorama", "Maquette", "Trompe l'oeil"]),
 ("Art that doesn't try to show real things, just shapes and colours", "Abstract", ["Trompe l'oeil", "Chiaroscuro", "Sfumato"]),
 ("A picture in three hinged panels", "Triptych", ["Diptych", "Frieze", "Diorama"]),
 ("A dark outline of someone against a light background", "Silhouette", ["Chiaroscuro", "Sfumato", "Impasto"]),
 ("Burnt sticks of wood used for smudgy black drawings", "Charcoal", ["Pastel", "Gesso", "Tempera"]),
 ("Making things shrink into the distance so a picture looks deep", "Perspective", ["Chiaroscuro", "Sfumato", "Impasto"]),
 ("An artist's greatest work", "Masterpiece", ["Maquette", "Diorama", "Frieze"]),
 ("A funny drawing that exaggerates someone's features", "Caricature", ["Trompe l'oeil", "Sfumato", "Diorama"])])

race("what's this jewellery word?", "Fashion", "medium", ["jewellery", "words"], [
 ("How a diamond's weight, or gold's purity, is measured", "Carat", ["Bezel", "Prong", "Filigree"]),
 ("The tiny stamp proving gold or silver is genuine", "Hallmark", ["Bezel", "Filigree", "Cabochon"]),
 ("Opens up to hold a tiny photo, worn on a chain", "Locket", ["Fob", "Armlet", "Torc"]),
 ("Fasten the sleeves of a smart shirt", "Cufflinks", ["Tie pin", "Tie clip", "Fob"]),
 ("Pinned onto a coat or dress", "Brooch", ["Fob", "Armlet", "Torc"]),
 ("A jewelled half-crown worn by brides and royals", "Tiara", ["Torc", "Armlet", "Fob"]),
 ("A ring engraved with a family crest, once pressed into sealing wax", "Signet ring", ["Claddagh ring", "Mood ring", "Puzzle ring"]),
 ("A rigid bracelet that slips over your hand", "Bangle", ["Armlet", "Torc", "Fob"]),
 ("A chain worn round the ankle", "Anklet", ["Armlet", "Torc", "Toe ring"]),
 ("A necklace that fits snugly round the neck", "Choker", ["Rivière", "Sautoir", "Torc"]),
 ("A charm or stone hanging from a necklace", "Pendant", ["Torc", "Armlet", "Bezel"]),
 ("A band set with stones all the way round, often given on an anniversary", "Eternity ring", ["Claddagh ring", "Mood ring", "Puzzle ring"]),
 ("A ring with a single diamond", "Solitaire", ["Cabochon", "Baguette", "Parure"]),
 ("A carved profile of a head, set in a brooch or ring", "Cameo", ["Cabochon", "Filigree", "Baguette"]),
 ("A bracelet hung with little trinkets", "Charm bracelet", ["Armlet", "Torc", "Fob"]),
 ("The catch that fastens a necklace", "Clasp", ["Bezel", "Prong", "Filigree"]),
 ("Given when someone pops the question", "Engagement ring", ["Mood ring", "Puzzle ring", "Toe ring"]),
 ("Small earrings that sit flat on the lobe", "Studs", ["Toe ring", "Armlet", "Torc"]),
 ("Earrings shaped like rings", "Hoops", ["Toe ring", "Armlet", "Torc"]),
 ("A gem linked to the month you were born, like garnet for January", "Birthstone", ["Cabochon", "Baguette", "Parure"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-143.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
