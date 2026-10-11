# Bank session 11 Oct 2026: 3 more general races -> bank/race-173.json (lawn bowls, triathlon and crossword words). 20 rows each, target 10; wrong options are
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

race("what's this bowls word?", "Sport", "medium", ["lawn bowls", "bowls", "words"], [
 ("The small white target ball", "Jack", ["Cue ball", "Shuttlecock", "Puck"]),
 ("The lopsided weighting that makes a bowl curve", "Bias", ["Spin", "Swing", "Grip"]),
 ("The lawn the game is played on", "Green", ["Pitch", "Court", "Fairway"]),
 ("One round of bowling in one direction", "End", ["Frame", "Over", "Leg"]),
 ("A strip of the green for one game, and a team of four", "Rink", ["Lane", "Bay", "Track"]),
 ("The team captain, who bowls last", "Skip", ["Anchor", "Sweeper", "Pivot"]),
 ("The player who bowls first", "Lead", ["Opener", "Starter", "Server"]),
 ("A bowl that touches the jack", "Toucher", ["Kisser", "Nudger", "Toppler"]),
 ("The rubber square you stand on to bowl", "Mat", ["Doormat", "Coaster", "Placemat"]),
 ("Sir Francis ___, who finished his game before facing the Armada", "Drake", ["Raleigh", "Hawkins", "Frobisher"]),
 ("Where that legendary game was played", "Plymouth Hoe", ["Brighton Pier", "Hampton Court", "Tilbury Docks"]),
 ("Bowls on a green that rises in the middle, popular in the north", "Crown green", ["Village green", "Putting green", "Bowling alley"]),
 ("The trench round the edge of the green", "Ditch", ["Moat", "Gutter", "Bunker"]),
 ("Bowling gently to stop right by the jack", "Draw", ["Lob", "Chip", "Putt"]),
 ("Firing a fast bowl to scatter the others", "Drive", ["Lob", "Chip", "Putt"]),
 ("The cluster of bowls around the jack", "Head", ["Pack", "Huddle", "Scrum"]),
 ("A bowl nearer the jack than any of the other side's", "Shot", ["Strike", "Spare", "Birdie"]),
 ("Bowls played on carpet in the winter", "Indoor", ["Beach", "Ten-pin", "Floodlit"]),
 ("The traditional all-white clothing", "Whites", ["Blues", "Reds", "Blacks"]),
 ("The old name for bowls, from what they were made of", "Woods", ["Irons", "Stones", "Pins"])])

race("what's this triathlon word?", "Sport", "medium", ["triathlon", "endurance sport", "words"], [
 ("The first of the three legs", "Swim", ["Row", "Ski", "Climb"]),
 ("The middle leg", "Cycle", ["Row", "Ski", "Paddle"]),
 ("The final leg", "Run", ["Row", "Ski", "Climb"]),
 ("Changing from one sport to the next", "Transition", ["Translation", "Transmission", "Transfusion"]),
 ("Alistair and Jonny, Yorkshire's triathlon brothers", "Brownlee", ["Murray", "Kenny", "Charlton"]),
 ("A 2.4-mile swim, 112-mile ride and a full marathon", "Ironman", ["Iron Lady", "Superman", "Tin Man"]),
 ("The shortest race distance", "Sprint", ["Marathon", "Ultra", "Endurance"]),
 ("1.5 km swim, 40 km ride, 10 km run", "Olympic distance", ["Marathon distance", "Ironman distance", "Cross-country"]),
 ("A training session going straight from a ride into a run", "Brick", ["Block", "Slab", "Wall"]),
 ("Handlebar extensions you lean on", "Aero bars", ["Monkey bars", "Parallel bars", "Crossbars"]),
 ("Swimming in a lake or the sea rather than a pool", "Open water", ["Deep end", "Lido", "Splash zone"]),
 ("Riding close behind another to save energy", "Drafting", ["Doodling", "Sketching", "Tracing"]),
 ("The five-sport event with fencing and riding", "Pentathlon", ["Heptathlon", "Decathlon", "Duathlon"]),
 ("Skiing and shooting", "Biathlon", ["Duathlon", "Aquathlon", "Heptathlon"]),
 ("Where the bikes hang in the transition area", "Bike rack", ["Hat rack", "Toast rack", "Roof rack"]),
 ("Home of the Ironman World Championship at Kona", "Hawaii", ["Florida", "California", "Fiji"]),
 ("The timing device worn on the ankle", "Chip", ["Pager", "Badge", "Bracelet"]),
 ("A painful muscle spasm", "Cramp", ["Blister", "Chafe", "Bruise"]),
 ("A sharp pain in your side when running", "Stitch", ["Blister", "Chafe", "Bruise"]),
 ("The rubber suit for the swim, banned when the water's warm", "Wetsuit", ["Tracksuit", "Jumpsuit", "Spacesuit"])])

race("what's this crossword word?", "Words and language", "medium", ["crosswords", "puzzles", "words"], [
 ("The hint for each answer", "Clue", ["Cue", "Glue", "Claw"]),
 ("Answers written left to right", "Across", ["Over", "Along", "Upwards"]),
 ("Answers written top to bottom", "Down", ["Under", "Below", "Beneath"]),
 ("The pattern of squares", "Grid", ["Board", "Map", "Chart"]),
 ("The kind with tricky wordplay clues", "Cryptic", ["Graphic", "Lyric", "Classic"]),
 ("The simple, straightforward kind", "Quick", ["Junior", "Starter", "Practice"]),
 ("A clue where the letters are rearranged", "Anagram", ["Acronym", "Palindrome", "Spoonerism"]),
 ("The person who writes the crossword", "Setter", ["Editor", "Printer", "Compositor"]),
 ("The person who fills it in", "Solver", ["Reader", "Subscriber", "Proofreader"]),
 ("The filled-in blocks between the answers", "Black squares", ["Blind spots", "Black holes", "Dark horses"]),
 ("The newspaper famous for its daily cryptic, The ___", "Times", ["Mirror", "Sun", "Express"]),
 ("What a setter writes under", "Pen name", ["Nickname", "Codename", "Stage name"]),
 ("A clue where the answer is tucked inside the words", "Hidden word", ["Hidden track", "Hidden gem", "Hidden agenda"]),
 ("'We hear': a clue for a word that sounds like another", "Homophone", ["Synonym", "Antonym", "Acronym"]),
 ("A clue with two meanings and no wordplay", "Double definition", ["Double take", "Double cream", "Double agent"]),
 ("The numbers in brackets giving the word lengths", "Enumeration", ["Equation", "Estimation", "Elimination"]),
 ("Wise to use until you're sure", "Pencil", ["Biro", "Crayon", "Highlighter"]),
 ("The weekend puzzle you can send in to win", "Prize crossword", ["Prize draw", "Raffle", "Sweepstake"]),
 ("The daily five-letter puzzle with six guesses", "Wordle", ["Sudoku", "Boggle", "Scrabble"]),
 ("The man who published the first crossword, in 1913", "Arthur Wynne", ["Lewis Carroll", "Peter Roget", "Noah Webster"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-173.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
