# Bank session 9 Oct 2026 (second pass): 2 more 1% Club puzzles for 15 topics that had 4. Genuine puzzles — a
# hidden word, a little working or a trap — each with a one-line "why". pct is from CLUB_PCTS; difficulty follows it.
# Writes bank/topics/<slug>__c3.json; import with FILE=<slug>__c3 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = {}
def c(slug, pct, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.setdefault(slug, []).append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff})

c("us-tv", 40, "Which US sitcom is hidden in this sentence: 'The coach praised the cheer squad'?", ["Cheers"], "cheER Squad hides CHEERS.")
c("us-tv", 40, "The six Friends each send a Christmas card to every other Friend. How many cards are sent?", ["30", "Thirty"],
  "Each of the 6 sends 5 cards: 6 × 5 = 30. (A card goes one way, unlike a hug.)")

c("anagrams-wordplay", 50, "Which word can go in front of BALL, BOARD and SHOE?", ["Snow"], "Snowball, snowboard and snowshoe.")
c("anagrams-wordplay", 60, "Which letter can go in front of IRD, OWL and EAR to make three words?", ["B"], "B gives BIRD, BOWL and BEAR.")

c("ancient-history", 10, "Julius Caesar was killed in 44 BC and Augustus died in AD 14. How many years apart were those events?", ["57", "Fifty-seven"],
  "There was no year 0, so 44 + 14 − 1 = 57.")
c("ancient-history", 40, "Which Greek letter is hidden in this sentence: 'His model tank won a prize'?", ["Delta"], "moDEL TAnk hides DELTA.")

c("pixar-animation", 40, "Which Pixar film is hidden in this sentence: 'The cobra very nearly bit me'?", ["Brave"], "coBRA VEry hides BRAVE.")
c("pixar-animation", 40, "Which Pixar fish is hidden in this sentence: 'She sent a kitten emoji'?", ["Nemo"], "kitteN EMOji hides NEMO.")

c("brands-logos", 50, "Which supermarket is hidden in this sentence: 'Has dad got the car keys?'", ["Asda"], "hAS DAd hides ASDA.")
c("brands-logos", 70, "The Audi logo has four rings and the Olympic logo has five. How many rings are there in two Audi logos and one Olympic logo?", ["13", "Thirteen"],
  "2 × 4 = 8, plus 5 = 13.")

c("kids-tv", 50, "Bob is a builder, Sam is a fireman and Pat is a postman. How many letters are there in those three jobs altogether?", ["21", "Twenty-one"],
  "BUILDER, FIREMAN and POSTMAN have 7 letters each: 3 × 7 = 21.")
c("kids-tv", 80, "A pack of 52 cards is dealt out equally between 4 players. How many cards does each player get?", ["13", "Thirteen"], "52 ÷ 4 = 13.")

c("days-that-shook-the-world", 30, "The Berlin Wall stood from 1961 to 1989. In how many different calendar years was it standing?", ["29", "Twenty-nine"],
  "Count both ends: 1989 − 1961 + 1 = 29.")
c("days-that-shook-the-world", 80, "Neil Armstrong walked on the Moon in 1969. In what year was the 50th anniversary?", ["2019"], "1969 + 50 = 2019.")

c("dexter", 40, "Which Dexter character is hidden in this sentence: 'Team spirit and luck won the day'?", ["Rita"], "spiRIT And hides RITA.")
c("dexter", 70, "Dexter keeps one blood slide per victim. At 3 victims a season for 8 seasons, how many slides does he collect?", ["24", "Twenty-four"], "3 × 8 = 24.")

c("doctor-who", 40, "The Doctor could originally regenerate 12 times. How many different Doctors did that allow?", ["13", "Thirteen"],
  "The first Doctor plus 12 regenerations makes 13 lives.")
c("doctor-who", 40, "Which Doctor Who enemy is hidden in this sentence: 'The pub had ale kegs stacked outside'?", ["Dalek", "Daleks"], "haD ALE Kegs hides DALEK.")

c("maths-numbers", 70, "What is 15% of 80?", ["12", "Twelve"], "10% is 8 and 5% is 4: 8 + 4 = 12.")
c("maths-numbers", 30, "Which is the first prime bigger than 89?", ["97", "Ninety-seven"],
  "90 to 96 all divide by 2, 3 or 5, and 91 is 7 × 13; 97 has no factors.")

c("quiz-shows", 80, "On Mastermind, a contender scores 14 on their specialist subject and 13 on general knowledge. What is their total?", ["27", "Twenty-seven"], "14 + 13 = 27.")
c("quiz-shows", 90, "On Pointless the lowest score wins. Four answers score 12, 3, 27 and 0. Which score wins?", ["0", "Zero", "Nought"], "0 is the lowest: a pointless answer.")

c("the-2000s", 40, "Which 2000s gadget is hidden in this sentence: 'Hip odes are fun to write'?", ["iPod"], "hIP ODes hides IPOD.")
c("the-2000s", 80, "England beat Australia 20–17 in the 2003 Rugby World Cup final. How many points were scored in the match?", ["37", "Thirty-seven"], "20 + 17 = 37.")

c("uk-geography", 50, "Which English city is hidden in this sentence: 'The cut bleeds a lot'?", ["Leeds"], "bLEEDS hides LEEDS.")
c("uk-geography", 30, "The 280-mile run from Newcastle to London is done at a steady hundred mph. How long does that take, in hours and minutes?", ["2 hours 48 minutes", "2h 48m", "2:48", "168 minutes"],
  "280 ÷ 100 = 2.8 hours, and 0.8 of an hour is 48 minutes.")

c("video-games", 70, "Every Tetris piece is made of four squares. How many squares are there in one of each of the seven different pieces?", ["28", "Twenty-eight"], "7 × 4 = 28.")
c("video-games", 40, "Which Nintendo princess is hidden in this sentence: 'The slope a child slid down was icy'?", ["Peach", "Princess Peach"], "sloPE A CHild hides PEACH.")

c("wales", 60, "Which Welsh city is hidden in this sentence: 'I saw a swan sea-bound'?", ["Swansea"], "SWAN SEA-bound hides SWANSEA.")
c("wales", 80, "Wales has 22 council areas. If each sends 3 choirs to an eisteddfod, how many choirs is that?", ["66", "Sixty-six"], "22 × 3 = 66.")

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__c3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'puzzles in', len(OUT), 'topics:', ' '.join(OUT))
