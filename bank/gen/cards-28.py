# Bank session 10 Oct 2026: 18 more Play Your Cards Right games -> bank/cards-28.json. A row of 5-7 cards each:
# what's on the card, what it shows when it flips, and the number compared. The numbers zig-zag, no equal neighbours.
# Titles must be new to the bank (the import skips a repeated title as a duplicate).
import json, os
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    assert len({l for l, _, _ in cards}) == len(cards), (text, 'repeated card')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("the year each famous ship sank", "History", "medium", ["ships", "shipwrecks", "years"], [
 ("The Mary Rose", "1545", 1545), ("The Costa Concordia", "2012", 2012), ("The Vasa", "1628", 1628),
 ("The Bismarck", "1941", 1941), ("The Titanic", "1912", 1912), ("The Herald of Free Enterprise", "1987", 1987)])
game("how many numbered symphonies did each composer write?", "Music", "hard", ["classical music", "composers"], [
 ("Haydn", "104", 104), ("Brahms", "4", 4), ("Mozart", "41", 41), ("Tchaikovsky", "6", 6), ("Beethoven", "9", 9), ("Sibelius", "7", 7)])
game("how many times did each marry?", "Celebrities", "medium", ["marriages", "famous people"], [
 ("Henry VIII", "6", 6), ("Paul McCartney", "3", 3), ("Elizabeth Taylor", "8", 8), ("Donald Trump", "3", 3), ("Jennifer Lopez", "4", 4), ("Larry King", "8", 8)])
game("how old was each at their first world snooker title?", "Sport", "hard", ["snooker", "ages"], [
 ("Stephen Hendry", "21", 21), ("Mark Selby", "30", 30), ("Steve Davis", "23", 23), ("Judd Trump", "29", 29), ("Ronnie O'Sullivan", "25", 25), ("Zhao Xintong", "28", 28)])
game("Test wickets taken in a whole career", "Cricket", "hard", ["cricket", "Test cricket", "bowlers"], [
 ("Muttiah Muralitharan", "800", 800), ("Ian Botham", "383", 383), ("Shane Warne", "708", 708), ("Stuart Broad", "604", 604), ("James Anderson", "704", 704), ("Anil Kumble", "619", 619)])
game("Test centuries in a whole career", "Cricket", "hard", ["cricket", "Test cricket", "batters"], [
 ("Sachin Tendulkar", "51", 51), ("Don Bradman", "29", 29), ("Jacques Kallis", "45", 45), ("Alastair Cook", "33", 33), ("Ricky Ponting", "41", 41), ("Brian Lara", "34", 34)])
game("how many children did each monarch have?", "The royal family", "medium", ["monarchs", "children"], [
 ("George III", "15", 15), ("Charles III", "2", 2), ("Victoria", "9", 9), ("Elizabeth II", "4", 4), ("George V", "6", 6), ("George VI", "2", 2)])
game("roughly how many years was each Prime Minister in office, in total?", "Politics", "medium", ["Prime Ministers", "years"], [
 ("Margaret Thatcher", "11", 11), ("Gordon Brown", "3", 3), ("Tony Blair", "10", 10), ("David Cameron", "6", 6), ("Harold Wilson", "8", 8), ("Theresa May", "3", 3)])
game("how tall is each statue, in metres?", "Famous landmarks", "hard", ["statues", "metres"], [
 ("The Statue of Unity, India", "182 m", 182), ("The Angel of the North", "20 m", 20), ("The Spring Temple Buddha, China", "128 m", 128),
 ("Christ the Redeemer (the figure)", "30 m", 30), ("The Motherland Calls, Volgograd", "85 m", 85), ("The Statue of Liberty (the figure)", "46 m", 46)])
game("how many floors in each skyscraper?", "Famous landmarks", "medium", ["skyscrapers", "buildings"], [
 ("The Burj Khalifa", "163", 163), ("The Gherkin", "41", 41), ("The Empire State Building", "102", 102),
 ("One Canada Square, Canary Wharf", "50", 50), ("Taipei 101", "101", 101), ("The Petronas Towers", "88", 88)])
game("how many teeth in a full set?", "Animals", "medium", ["teeth", "animals"], [
 ("A dog", "42", 42), ("A child (milk teeth)", "20", 20), ("A pig", "44", 44), ("A cat", "30", 30), ("An adult human", "32", 32)])
game("the numbers in nursery rhymes and songs", "Nostalgia", "easy", ["nursery rhymes", "children's songs"], [
 ("The Grand Old Duke of York's men", "10,000", 10000), ("Blind mice", "3", 3), ("Blackbirds baked in a pie", "24", 24),
 ("Little ducks that went swimming one day", "5", 5), ("Green bottles hanging on the wall", "10", 10), ("Old King Cole's fiddlers", "3", 3)])
game("how many does each word mean?", "Words and language", "medium", ["numbers", "words"], [
 ("A score", "20", 20), ("A brace", "2", 2), ("A gross", "144", 144), ("A baker's dozen", "13", 13), ("A century", "100", 100), ("A dozen", "12", 12)])
game("how old was each royal on 1 January 2026?", "The royal family", "medium", ["royals", "ages"], [
 ("King Charles III", "77", 77), ("Prince George", "12", 12), ("Princess Anne", "75", 75), ("Prince Harry", "41", 41), ("Prince William", "43", 43), ("Princess Charlotte", "10", 10)])
game("which Apollo mission number was it?", "Space", "medium", ["Apollo", "space missions"], [
 ("'Houston, we've had a problem'", "13", 13), ("The launch-pad fire", "1", 1), ("The last men on the Moon", "17", 17),
 ("The first crew to orbit the Moon", "8", 8), ("The first Moon landing", "11", 11), ("The first lunar rover", "15", 15)])
game("how many stripes on each?", "Flags", "hard", ["flags", "stripes"], [
 ("The flag of Malaysia", "14", 14), ("The Adidas logo", "3", 3), ("The flag of the United States", "13", 13),
 ("The flag of Thailand", "5", 5), ("The flag of Liberia", "11", 11), ("The flag of Greece", "9", 9)])
game("how old is each character in the story?", "Books", "hard", ["characters", "ages", "books"], [
 ("Methuselah, when he died", "969", 969), ("Alice in Through the Looking-Glass", "7½", 7.5), ("Bilbo at his farewell party", "111", 111),
 ("Harry Potter, when his Hogwarts letter arrives", "11", 11), ("Frodo, at that same party", "33", 33), ("Juliet", "13", 13)])
game("the number of each famous road", "Britain", "medium", ["roads", "motorways"], [
 ("Route ___, across America", "66", 66), ("The A___, the Great North Road", "1", 1), ("The M___, round London", "25", 25),
 ("The A___, Perth to Inverness", "9", 9), ("The M___, across the Pennines", "62", 62), ("The M___, Toll road", "6", 6)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-28.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
