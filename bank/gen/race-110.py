# Bank session 10 Oct 2026: 2 more general races -> bank/race-110.json (car badges, fashion designers). 20 rows each, target 10; wrong options are
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

race("which car maker's badge is this?", "Cars and motoring", "medium", ["cars", "logos", "badges"], [
 ("A three-pointed star in a circle", "Mercedes-Benz", ["Chrysler", "Infiniti", "Genesis"]),
 ("Four interlocking rings", "Audi", ["Porsche", "Seat", "Smart"]),
 ("A blue and white roundel", "BMW", ["Mini", "Porsche", "Cupra"]),
 ("A gold 'bow tie'", "Chevrolet", ["Cadillac", "Dodge", "Buick"]),
 ("A blue oval", "Ford", ["Kia", "Dacia", "Nissan"]),
 ("Two overlapping Rs", "Rolls-Royce", ["Lotus", "Jaguar", "Land Rover"]),
 ("A letter B with wings", "Bentley", ["MG", "Lotus", "Bugatti"]),
 ("Neptune's trident", "Maserati", ["Ferrari", "Lamborghini", "Fiat"]),
 ("A silver diamond", "Renault", ["Dacia", "Peugeot", "Seat"]),
 ("Two upturned chevrons", "Citroën", ["Peugeot", "Dacia", "Seat"]),
 ("The six stars of the Pleiades", "Subaru", ["Mazda", "Nissan", "Suzuki"]),
 ("Three red diamonds", "Mitsubishi", ["Mazda", "Suzuki", "Nissan"]),
 ("A pair of outstretched wings with the name across them", "Aston Martin", ["Lotus", "Jaguar", "McLaren"]),
 ("A stylised L inside an oval", "Lexus", ["Lotus", "Lincoln", "Land Rover"]),
 ("A lightning bolt in a circle", "Opel", ["Vauxhall", "Kia", "Dacia"]),
 ("Three overlapping ovals", "Toyota", ["Honda", "Nissan", "Mazda"]),
 ("A slanted, stylised H", "Hyundai", ["Honda", "Kia", "Genesis"]),
 ("A circle with an arrow pointing up and to the right", "Volvo", ["Polestar", "Scania", "Seat"]),
 ("A winged arrow", "Škoda", ["Seat", "Kia", "Cupra"]),
 ("A stylised T, like a cross-section of an electric motor", "Tesla", ["Polestar", "Lucid", "Rivian"])])

race("which designer or fashion house is famous for this?", "Fashion", "medium", ["fashion", "designers"], [
 ("No. 5 perfume and the little black dress", "Chanel", ["Yves Saint Laurent", "Lanvin", "Balenciaga"]),
 ("The 'New Look' of 1947", "Dior", ["Balenciaga", "Yves Saint Laurent", "Lanvin"]),
 ("The miniskirt, in 1960s London", "Mary Quant", ["Biba", "Ossie Clark", "Zandra Rhodes"]),
 ("Punk clothes for the Sex Pistols", "Vivienne Westwood", ["Zandra Rhodes", "John Galliano", "Jasper Conran"]),
 ("High heels with red soles", "Christian Louboutin", ["Jimmy Choo", "Kurt Geiger", "Prada"]),
 ("The Birkin bag", "Hermès", ["Mulberry", "Fendi", "Prada"]),
 ("A Medusa head logo", "Versace", ["Armani", "Valentino", "Dolce & Gabbana"]),
 ("The wrap dress, from 1974", "Diane von Furstenberg", ["Vera Wang", "Michael Kors", "Halston"]),
 ("A polo player logo", "Ralph Lauren", ["Tommy Hilfiger", "Fred Perry", "Hackett"]),
 ("The trench coat and a famous camel check", "Burberry", ["Aquascutum", "Mulberry", "Belstaff"]),
 ("Interlocking Gs", "Gucci", ["Prada", "Fendi", "Armani"]),
 ("The LV monogram", "Louis Vuitton", ["Mulberry", "Fendi", "Coach"]),
 ("Princess Diana's 1981 wedding dress", "David and Elizabeth Emanuel", ["Bruce Oldfield", "Catherine Walker", "Zandra Rhodes"]),
 ("Catherine's 2011 wedding dress, by Sarah Burton", "Alexander McQueen", ["Jenny Packham", "Bruce Oldfield", "Vera Wang"]),
 ("Audrey Hepburn's black dress in 'Breakfast at Tiffany's'", "Givenchy", ["Yves Saint Laurent", "Balenciaga", "Valentino"]),
 ("Madonna's cone bra", "Jean Paul Gaultier", ["Thierry Mugler", "John Galliano", "Moschino"]),
 ("The shoes Carrie Bradshaw calls 'Manolos'", "Manolo Blahnik", ["Jimmy Choo", "Kurt Geiger", "Salvatore Ferragamo"]),
 ("The waxed jacket made in South Shields", "Barbour", ["Belstaff", "Hunter", "Aquascutum"]),
 ("Vegetarian fashion, from a Beatle's daughter", "Stella McCartney", ["Victoria Beckham", "Jasper Conran", "Phoebe Philo"]),
 ("The 501 jeans", "Levi's", ["Wrangler", "Lee", "Diesel"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-110.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
