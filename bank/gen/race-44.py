# Bank session 10 Oct 2026: 4 more general races -> bank/race-44.json. 20 rows each, target 10; wrong options are
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

race("which country did this 21st-century leader lead?", "Politics", "medium", ["leaders", "21st century", "countries"], [
 ("Angela Merkel", "Germany", ["Austria", "Switzerland", "Luxembourg"]), ("Jacinda Ardern", "New Zealand", ["Fiji", "Samoa", "Iceland"]),
 ("Justin Trudeau", "Canada", ["the USA", "Iceland", "Denmark"]), ("Emmanuel Macron", "France", ["Belgium", "Luxembourg", "Switzerland"]),
 ("Narendra Modi", "India", ["Bangladesh", "Sri Lanka", "Nepal"]), ("Volodymyr Zelenskyy", "Ukraine", ["Belarus", "Moldova", "Georgia"]),
 ("Recep Tayyip Erdoğan", "Turkey", ["Iran", "Cyprus", "Greece"]), ("Luiz Inácio Lula da Silva", "Brazil", ["Portugal", "Chile", "Colombia"]),
 ("Silvio Berlusconi", "Italy", ["Spain", "Greece", "Malta"]), ("Viktor Orbán", "Hungary", ["Poland", "Slovakia", "Romania"]),
 ("Benjamin Netanyahu", "Israel", ["Lebanon", "Jordan", "Cyprus"]), ("Shinzo Abe", "Japan", ["Taiwan", "China", "the Philippines"]),
 ("Imran Khan", "Pakistan", ["Afghanistan", "Bangladesh", "Iran"]), ("Jacob Zuma", "South Africa", ["Zimbabwe", "Namibia", "Nigeria"]),
 ("Julia Gillard", "Australia", ["the UK", "Fiji", "Samoa"]), ("Leo Varadkar", "Ireland", ["the UK", "Iceland", "Malta"]),
 ("Mark Rutte", "the Netherlands", ["Belgium", "Denmark", "Luxembourg"]), ("Sanna Marin", "Finland", ["Estonia", "Sweden", "Norway"]),
 ("Javier Milei", "Argentina", ["Uruguay", "Chile", "Peru"]), ("Moon Jae-in", "South Korea", ["China", "Taiwan", "Vietnam"])])

race("who lives or works here?", "Politics", "hard", ["official residences", "buildings"], [
 ("10 Downing Street", "The UK Prime Minister", ["Leader of the Opposition", "Speaker of the Commons", "Foreign Secretary"]),
 ("11 Downing Street", "The Chancellor of the Exchequer", ["Home Secretary", "Foreign Secretary", "Leader of the Opposition"]),
 ("The White House", "The US President", ["US Vice President", "Speaker of the House", "Secretary of State"]),
 ("The Élysée Palace", "France's President", ["France's Prime Minister", "Mayor of Paris", "President of the Senate"]),
 ("Bute House, Edinburgh", "Scotland's First Minister", ["Wales's First Minister", "Secretary of State for Scotland", "Lord Provost of Edinburgh"]),
 ("The Lodge, Canberra", "Australia's Prime Minister", ["Australia's Governor-General", "Leader of the Opposition", "Speaker of the House"]),
 ("Áras an Uachtaráin, Dublin", "Ireland's President", ["The Taoiseach", "The Tánaiste", "The Ceann Comhairle"]),
 ("The Quirinal Palace, Rome", "Italy's President", ["Italy's Prime Minister", "President of the Senate", "Mayor of Rome"]),
 ("Bellevue Palace, Berlin", "Germany's President", ["Germany's Chancellor", "Mayor of Berlin", "Bundestag President"]),
 ("The Kantei, Tokyo", "Japan's Prime Minister", ["Japan's Emperor", "Governor of Tokyo", "Speaker of the House"]),
 ("Rashtrapati Bhavan, New Delhi", "India's President", ["India's Prime Minister", "Chief Justice of India", "Vice President of India"]),
 ("Lambeth Palace", "The Archbishop of Canterbury", ["Archbishop of York", "Dean of Westminster", "Bishop of London"]),
 ("Mansion House, London", "The Lord Mayor of London", ["Mayor of London", "Bishop of London", "Speaker of the Commons"]),
 ("The Casa Rosada", "Argentina's President", ["Argentina's Vice President", "Mayor of Buenos Aires", "Archbishop of Buenos Aires"]),
 ("Moncloa Palace, Madrid", "Spain's Prime Minister", ["Spain's King", "Mayor of Madrid", "Speaker of the Congress"]),
 ("Zhongnanhai, Beijing", "China's top leaders", ["Mayor of Beijing", "Hong Kong's Chief Executive", "Taiwan's President"]),
 ("The Alvorada Palace, Brasília", "Brazil's President", ["Brazil's Vice President", "Mayor of Rio de Janeiro", "Governor of São Paulo"]),
 ("The Kremlin", "Russia's President", ["Russia's Prime Minister", "Mayor of Moscow", "Patriarch of Moscow"]),
 ("The Apostolic Palace", "The Pope", ["Vatican Secretary of State", "Dean of the College of Cardinals", "Mayor of Rome"]),
 ("Rideau Hall, Ottawa", "Canada's Governor General", ["Canada's Prime Minister", "Mayor of Ottawa", "Speaker of the Senate"])])

race("which fairy tale features this?", "Books", "easy", ["fairy tales", "stories"], [
 ("A glass slipper", "Cinderella", ["The Red Shoes", "Beauty and the Beast", "The Frog Prince"]),
 ("A poisoned apple", "Snow White", ["Beauty and the Beast", "The Frog Prince", "The Snow Maiden"]),
 ("A prick from a spindle", "Sleeping Beauty", ["The Snow Maiden", "Beauty and the Beast", "The Frog Prince"]),
 ("Magic beans", "Jack and the Beanstalk", ["The Golden Goose", "Tom Thumb", "Puss in Boots"]),
 ("A house made of gingerbread", "Hansel and Gretel", ["The Gingerbread Man", "Tom Thumb", "Chicken Licken"]),
 ("Three bowls of porridge", "Goldilocks and the Three Bears", ["The Gingerbread Man", "Chicken Licken", "The Ugly Duckling"]),
 ("A pea under twenty mattresses", "The Princess and the Pea", ["The Frog Prince", "The Ugly Duckling", "The Nightingale"]),
 ("Straw spun into gold", "Rumpelstiltskin", ["The Golden Goose", "The Fisherman and His Wife", "Tom Thumb"]),
 ("A tower with no door", "Rapunzel", ["Beauty and the Beast", "The Snow Maiden", "The Frog Prince"]),
 ("A troll under a bridge", "The Three Billy Goats Gruff", ["The Ugly Duckling", "Chicken Licken", "The Gingerbread Man"]),
 ("Houses of straw, sticks and bricks", "The Three Little Pigs", ["Chicken Licken", "The Gingerbread Man", "The Ugly Duckling"]),
 ("A splinter from a magic mirror", "The Snow Queen", ["The Snow Maiden", "The Nightingale", "The Steadfast Tin Soldier"]),
 ("A voice traded for a pair of legs", "The Little Mermaid", ["The Fisherman and His Wife", "The Nightingale", "The Steadfast Tin Soldier"]),
 ("A key to a forbidden room", "Bluebeard", ["Ali Baba", "Aladdin", "Beauty and the Beast"]),
 ("Twelve pairs of shoes worn through every night", "The Twelve Dancing Princesses", ["The Red Shoes", "The Snow Maiden", "Beauty and the Beast"]),
 ("A bed made from a walnut shell", "Thumbelina", ["Tom Thumb", "The Steadfast Tin Soldier", "The Nightingale"]),
 ("Shirts knitted from nettles", "The Wild Swans", ["The Ugly Duckling", "The Nightingale", "The Snow Maiden"]),
 ("Leather left out overnight", "The Elves and the Shoemaker", ["The Red Shoes", "Puss in Boots", "Tom Thumb"]),
 ("A pipe that leads the rats away", "The Pied Piper of Hamelin", ["The Nightingale", "Tom Thumb", "Puss in Boots"]),
 ("A wolf in Grandma's nightgown", "Little Red Riding Hood", ["Peter and the Wolf", "The Boy Who Cried Wolf", "The Gingerbread Man"])])

race("which animal does this food come from?", "Food and drink", "hard", ["food", "animals"], [
 ("Venison", "Deer", ["Wild boar", "Pheasant", "Horse"]), ("Mutton", "Sheep", ["Horse", "Wild boar", "Ox"]),
 ("Veal", "Calf", ["Lamb", "Piglet", "Foal"]), ("Escargots", "Snail", ["Slug", "Mussel", "Whelk"]),
 ("Calamari", "Squid", ["Cuttlefish", "Prawn", "Scallop"]), ("Squab", "Pigeon", ["Quail", "Partridge", "Chicken"]),
 ("Capon", "Cockerel", ["Turkey", "Hen", "Guinea fowl"]), ("Kid", "Goat", ["Lamb", "Piglet", "Foal"]),
 ("Caviar", "Sturgeon", ["Salmon", "Herring", "Mackerel"]), ("Foie gras", "Duck or goose", ["Chicken", "Turkey", "Pheasant"]),
 ("Pulpo", "Octopus", ["Cuttlefish", "Crab", "Lobster"]), ("Lapin", "Rabbit", ["Hare", "Squirrel", "Guinea pig"]),
 ("Cuisses de grenouille", "Frog", ["Toad", "Newt", "Lizard"]), ("Unagi", "Eel", ["Salmon", "Tuna", "Mackerel"]),
 ("Bombay duck", "Lizardfish", ["Duck", "Chicken", "Goose"]), ("Ortolan", "Bunting", ["Sparrow", "Lark", "Quail"]),
 ("Langoustine", "Norway lobster", ["Prawn", "Crab", "Crayfish"]), ("Taramasalata", "Cod (its roe)", ["Salmon", "Herring", "Mackerel"]),
 ("Gammon", "Pig", ["Wild boar", "Ox", "Horse"]), ("Bresaola", "Cattle", ["Wild boar", "Turkey", "Ostrich"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-44.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
