# Bank session 10 Oct 2026: 2 more general races -> bank/race-96.json (pasta names, collectors and lovers). 20 rows each, target 10; wrong options are
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

race("which pasta's name means this in Italian?", "Food and drink", "hard", ["pasta", "Italian", "words"], [
 ("Little butterflies", "Farfalle", ["Gemelli", "Campanelle", "Cappelletti"]),
 ("Little tongues", "Linguine", ["Tagliatelle", "Bucatini", "Pappardelle"]),
 ("Little ears", "Orecchiette", ["Cappelletti", "Mezzelune", "Anelli"]),
 ("Little worms", "Vermicelli", ["Bucatini", "Tagliolini", "Trofie"]),
 ("Quills or pens", "Penne", ["Ziti", "Macaroni", "Paccheri"]),
 ("Little strings", "Spaghetti", ["Bucatini", "Tagliolini", "Trofie"]),
 ("Shells", "Conchiglie", ["Lasagne", "Campanelle", "Casarecce"]),
 ("Big tubes", "Cannelloni", ["Manicotti", "Paccheri", "Ziti"]),
 ("Little ribbons", "Fettuccine", ["Tagliatelle", "Pappardelle", "Mafalde"]),
 ("Little spindles", "Fusilli", ["Casarecce", "Trofie", "Gemelli"]),
 ("Priest stranglers", "Strozzapreti", ["Paccheri", "Garganelli", "Cappelletti"]),
 ("Fine hair", "Capellini", ["Tagliolini", "Bucatini", "Cappelletti"]),
 ("Barley", "Orzo", ["Anelli", "Trofie", "Gnocchi"]),
 ("Snails", "Lumache", ["Conchigliette", "Campanelle", "Mezzelune"]),
 ("Corkscrews", "Cavatappi", ["Gemelli", "Casarecce", "Tortiglioni"]),
 ("Little wheels", "Rotelle", ["Anelli", "Mezzelune", "Campanelle"]),
 ("Little thimbles", "Ditalini", ["Cappelletti", "Anelli", "Paccheri"]),
 ("Radiators", "Radiatori", ["Garganelli", "Tortiglioni", "Campanelle"]),
 ("Little stars", "Stelline", ["Anelli", "Mezzelune", "Cappelletti"]),
 ("Big ridged ones", "Rigatoni", ["Tortiglioni", "Paccheri", "Ziti"])])

race("what's the word for someone who collects or loves this?", "Words and language", "hard", ["words", "collectors", "hobbies"], [
 ("Collects stamps", "Philatelist", ["Philologist", "Philanthropist", "Cartographer"]),
 ("Collects coins", "Numismatist", ["Numerologist", "Chronologist", "Philologist"]),
 ("Loves and collects books", "Bibliophile", ["Bibliographer", "Bibliopole", "Lexicographer"]),
 ("Loves wine", "Oenophile", ["Hydrophile", "Thalassophile", "Heliophile"]),
 ("Collects matchbox labels", "Phillumenist", ["Philologist", "Pyrophile", "Heliophile"]),
 ("Collects beer mats", "Tegestologist", ["Labeorphilist", "Zymologist", "Brewster"]),
 ("Collects postcards", "Deltiologist", ["Cartographer", "Topographer", "Calligrapher"]),
 ("Collects teddy bears", "Arctophile", ["Hippophile", "Xenophile", "Pogonophile"]),
 ("Collects banknotes", "Notaphilist", ["Numerologist", "Notary", "Chronologist"]),
 ("Collects cigarette cards", "Cartophilist", ["Cartographer", "Calligrapher", "Topographer"]),
 ("Collects and studies butterflies and moths", "Lepidopterist", ["Coleopterist", "Apiarist", "Arachnologist"]),
 ("Loves films", "Cinephile", ["Cinematographer", "Audiologist", "Xenophile"]),
 ("Loves England and all things English", "Anglophile", ["Germanophile", "Russophile", "Sinophile"]),
 ("Loves France and all things French", "Francophile", ["Hellenophile", "Sinophile", "Germanophile"]),
 ("Loves top-quality hi-fi sound", "Audiophile", ["Audiologist", "Hydrophile", "Xenophile"]),
 ("Loves cats", "Ailurophile", ["Ailurophobe", "Hippophile", "Cynophile"]),
 ("Loves words", "Logophile", ["Lexicographer", "Etymologist", "Calligrapher"]),
 ("Loves rain", "Pluviophile", ["Hydrophile", "Thalassophile", "Heliophile"]),
 ("Collects and mends clocks and watches", "Horologist", ["Chronologist", "Horticulturist", "Numerologist"]),
 ("Spots trains (railway slang)", "Gricer", ["Twitcher", "Gongoozler", "Bodger"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-96.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
