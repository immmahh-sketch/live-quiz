# Bank session 9 Oct 2026 (restart): 20 more Play Your Cards Right games -> bank/cards-3.json. A row of 5-7 cards each:
# what's on the card, what it shows when it flips, and the number compared. The numbers zig-zag, no equal neighbours.
import json, os
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    assert len({l for l, _, _ in cards}) == len(cards), (text, 'repeated card')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("how many official Bond films did each actor make?", "James Bond", "medium", ["Bond", "actors"], [
 ("George Lazenby", "1", 1), ("Roger Moore", "7", 7), ("Timothy Dalton", "2", 2), ("Sean Connery", "6", 6), ("Pierce Brosnan", "4", 4), ("Daniel Craig", "5", 5)])
game("the year each Harry Potter book came out", "Harry Potter", "medium", ["books", "years"], [
 ("Order of the Phoenix", "2003", 2003), ("Philosopher's Stone", "1997", 1997), ("Deathly Hallows", "2007", 2007),
 ("Prisoner of Azkaban", "1999", 1999), ("Half-Blood Prince", "2005", 2005), ("Chamber of Secrets", "1998", 1998)])
game("the year each North East landmark opened", "The North East", "medium", ["North East", "years"], [
 ("The Tyne Bridge", "1928", 1928), ("The Angel of the North", "1998", 1998), ("The Tyne and Wear Metro", "1980", 1980),
 ("Sage Gateshead", "2004", 2004), ("The Stadium of Light", "1997", 1997), ("The Baltic art gallery", "2002", 2002)])
game("Grand Slam singles titles, up to 2025", "Tennis", "hard", ["tennis"], [
 ("Andy Murray", "3", 3), ("Roger Federer", "20", 20), ("Emma Raducanu", "1", 1), ("Rafael Nadal", "22", 22), ("Virginia Wade", "3", 3), ("Serena Williams", "23", 23)])
game("how many times has each club won the FA Cup, up to 2025?", "Football", "hard", ["FA Cup", "clubs"], [
 ("Sunderland", "2", 2), ("Arsenal", "14", 14), ("Newcastle United", "6", 6), ("Manchester United", "13", 13), ("Crystal Palace", "1", 1), ("Manchester City", "7", 7)])
game("how many in the adult human body?", "The human body", "easy", ["body"], [
 ("Lungs", "2", 2), ("Bones", "206", 206), ("Chambers in the heart", "4", 4), ("Teeth (a full set)", "32", 32), ("Kidneys", "2", 2), ("Ribs", "24", 24)])
game("what each scores on a dartboard", "Darts", "medium", ["darts"], [
 ("The outer bull", "25", 25), ("The most with three darts", "180", 180), ("The bullseye", "50", 50),
 ("The highest checkout", "170", 170), ("Double top", "40", 40), ("Treble 20", "60", 60)])
game("what each is worth in snooker", "Snooker", "easy", ["snooker"], [
 ("A red", "1", 1), ("The black", "7", 7), ("The yellow", "2", 2), ("The pink", "6", 6), ("The green", "3", 3), ("A maximum break", "147", 147)])
game("which wedding anniversary is it, in years?", "Weddings", "medium", ["anniversaries"], [
 ("Paper", "1st", 1), ("Golden", "50th", 50), ("Tin", "10th", 10), ("Diamond", "60th", 60), ("Silver", "25th", 25), ("Ruby", "40th", 40)])
game("what each Roman numeral is worth", "Maths and numbers", "easy", ["Roman numerals"], [
 ("V", "5", 5), ("M", "1,000", 1000), ("X", "10", 10), ("D", "500", 500), ("L", "50", 50), ("C", "100", 100)])
game("the year each Bond film came out", "James Bond", "medium", ["Bond", "years"], [
 ("Dr. No", "1962", 1962), ("Skyfall", "2012", 2012), ("Goldfinger", "1964", 1964),
 ("Casino Royale (Daniel Craig)", "2006", 2006), ("The Spy Who Loved Me", "1977", 1977), ("GoldenEye", "1995", 1995)])
game("the year each was born", "Famous people in history", "medium", ["birthdays", "years"], [
 ("William Shakespeare", "1564", 1564), ("Beyoncé", "1981", 1981), ("Winston Churchill", "1874", 1874),
 ("David Beckham", "1975", 1975), ("Elizabeth II", "1926", 1926), ("Elvis Presley", "1935", 1935)])
game("how many Olympic gold medals did each Briton win?", "The Olympics", "hard", ["Olympics", "Team GB"], [
 ("Tom Daley", "1", 1), ("Jason Kenny", "7", 7), ("Kelly Holmes", "2", 2), ("Chris Hoy", "6", 6), ("Mo Farah", "4", 4), ("Laura Kenny", "5", 5)])
game("the national speed limit for a car, in mph", "Driving", "easy", ["roads", "speed limits"], [
 ("A 20 zone", "20", 20), ("A motorway", "70", 70), ("A built-up area with street lights", "30", 30),
 ("A single carriageway", "60", 60), ("A lorry over 7.5 tonnes on an English single carriageway", "50", 50)])
game("how old were they when they came to the throne?", "Kings and queens", "hard", ["monarchs", "ages"], [
 ("Queen Victoria", "18", 18), ("Charles III", "73", 73), ("Edward VI", "9", 9), ("George VI", "40", 40), ("Henry VIII", "17", 17), ("Elizabeth II", "25", 25)])
game("Premier League goals in their whole career", "Football", "hard", ["Premier League", "goals"], [
 ("Thierry Henry", "175", 175), ("Alan Shearer", "260", 260), ("Frank Lampard", "177", 177),
 ("Harry Kane", "213", 213), ("Andy Cole", "187", 187), ("Wayne Rooney", "208", 208)])
game("how hot or cold, in °C?", "Science and nature", "medium", ["temperature"], [
 ("Normal body temperature", "37°C", 37), ("Water boils (at sea level)", "100°C", 100), ("Water freezes", "0°C", 0),
 ("The UK's hottest day on record (2022)", "40.3°C", 40.3), ("Absolute zero", "−273°C", -273), ("Inside a typical fridge", "about 4°C", 4)])
game("how many old pennies in each?", "Nostalgia", "hard", ["old money", "pre-decimal"], [
 ("A shilling", "12", 12), ("A pound", "240", 240), ("A sixpence", "6", 6), ("A guinea", "252", 252), ("A florin", "24", 24), ("Half a crown", "30", 30)])
game("the numbers in imperial measures", "Maths and numbers", "medium", ["imperial", "measures"], [
 ("Feet in a yard", "3", 3), ("Yards in a mile", "1,760", 1760), ("Pints in a gallon", "8", 8),
 ("Ounces in a pound", "16", 16), ("Inches in a foot", "12", 12), ("Pounds in a stone", "14", 14)])
game("the year each club moved into its home ground", "Football", "hard", ["stadiums", "years"], [
 ("Middlesbrough: the Riverside", "1995", 1995), ("Tottenham: the Tottenham Hotspur Stadium", "2019", 2019), ("Newcastle United: St James' Park", "1892", 1892),
 ("Arsenal: the Emirates", "2006", 2006), ("Sunderland: the Stadium of Light", "1997", 1997), ("Manchester City: the Etihad", "2003", 2003)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
