# Bank session 9 Oct 2026: more 1% Club puzzles for the real topics with 3 or fewer unused in the live bank
# (3 each for General knowledge and Maths, which had none left; 2 each for the rest). Genuine puzzles: logic,
# observation or a little working, never a plain fact. pct is from CLUB_PCTS; difficulty follows it.
# Writes bank/topics/<slug>__c2.json; import with FILE=<slug>__c2 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = {}
def c(slug, pct, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.setdefault(slug, []).append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff})

c("general-knowledge", 50, "Sam is Ann's brother. Ann has two sisters and no other brothers. How many children are in the family?", ["4", "Four"],
  "Ann, her two sisters and Sam: Ann's sisters are girls, so Sam is the only boy.")
c("general-knowledge", 80, "A shop sells 3 pens for £2. How much do 12 pens cost?", ["£8", "8", "8 pounds", "Eight pounds"],
  "12 pens is 4 lots of 3, and 4 × £2 = £8.")
c("general-knowledge", 70, "If yesterday was Monday, what day is the day after tomorrow?", ["Thursday"],
  "Today is Tuesday, tomorrow Wednesday, so the day after tomorrow is Thursday.")

c("maths-numbers", 80, "What is half of a quarter of 400?", ["50", "Fifty"], "A quarter of 400 is 100, and half of that is 50.")
c("maths-numbers", 70, "I think of a number, double it and add 6. The answer is 20. What was my number?", ["7", "Seven"], "20 − 6 = 14, and half of 14 is 7.")
c("maths-numbers", 50, "What is the smallest number that both 6 and 8 divide into exactly?", ["24", "Twenty-four"],
  "Multiples of 8 are 8, 16, 24 …, and 24 is the first that 6 also divides.")

c("rugby", 60, "In union, a team scores three converted tries and a drop goal. How many points is that?", ["24", "Twenty-four"],
  "A converted try is 5 + 2 = 7, so 3 × 7 = 21, plus 3 for the drop goal.")
c("rugby", 50, "Counting both teams, how many more players are on the pitch for a 15-a-side union match than for a sevens match?", ["16", "Sixteen"],
  "30 players in union against 14 in sevens: 30 − 14 = 16.")

c("words-language", 40, "Which three-letter word is hidden in all of these: STAMP, CAMPING, CHAMPION?", ["Amp"],
  "stAMP, cAMPing and chAMPion all contain AMP.")
c("words-language", 70, "Which word for midday reads the same backwards?", ["Noon"], "NOON backwards is NOON.")

c("art", 60, "The Mona Lisa was started in about 1503. To the nearest whole number, how many centuries ago is that?", ["5", "Five"],
  "2026 − 1503 = 523 years, which is about 5 centuries.")
c("art", 40, "Which painter is hidden in this sentence: 'Her sandal is broken'?", ["Dali", "Dalí", "Salvador Dali"], "sanDAL IS hides DALI.")

c("australia", 60, "When Sydney is 11 hours ahead of London, a match kicks off at 7pm in Sydney. What time is it in London?", ["8am", "8 am", "8:00am", "0800", "08:00", "8 in the morning"],
  "Take 11 hours off 7pm and you get 8am the same day.")
c("australia", 80, "Australia's flag has 6 stars and New Zealand's has 4. If you lay one of each flag side by side, how many stars can you see?", ["10", "Ten"],
  "6 + 4 = 10: the two flags share none.")

c("cricket", 70, "A batter is out for a duck in the first innings and makes 50 in the second. What is their batting average for the match?", ["25", "Twenty-five"],
  "50 runs over two dismissals: 50 ÷ 2 = 25.")
c("cricket", 40, "A bowler takes a wicket with the last ball of one over and the first two balls of his next over. Is that a hat-trick?", ["Yes"],
  "A hat-trick is three wickets with consecutive balls by the same bowler, and that can span two overs.")

c("crime-dramas", 40, "Which TV detective is hidden in this sentence: 'I saw a worm or seaweed'?", ["Morse", "Inspector Morse"], "worM OR SEaweed hides MORSE.")
c("crime-dramas", 40, "Exactly one of three suspects is guilty, and only the guilty one lies. Ann says 'Bob is innocent.' Bob says 'Carl is guilty.' Carl says 'I'm innocent.' Who is guilty?", ["Carl"],
  "If Carl is guilty, his is the only false statement. Ann or Bob being guilty makes an innocent person lie.")

c("food-drink", 70, "A recipe for 4 people uses 300g of flour. How much flour do you need for 6 people?", ["450g", "450", "450 grams"],
  "That's 75g a person, and 6 × 75 = 450g.")
c("food-drink", 50, "Which fruit is hidden in this sentence: 'I can't keep earrings safe'?", ["Pear"], "keeP EARrings hides PEAR.")

c("football", 40, "A team gets 3 points for a win and 1 for a draw. After 10 games they're unbeaten on 22 points. How many have they won?", ["6", "Six"],
  "Every game is a win or a draw; 10 draws would be 10 points, and each win adds 2 more: (22 − 10) ÷ 2 = 6.")
c("football", 20, "A knockout cup starts with 64 teams and has no replays. How many matches does it take to find the winner?", ["63", "Sixty-three"],
  "Every match knocks out exactly one team, and 63 teams have to go.")

c("friends", 40, "Joey, Chandler and Ross squeeze onto a three-seat sofa. In how many different orders can they sit?", ["6", "Six"],
  "3 choices for the first seat, 2 for the next, 1 for the last: 3 × 2 × 1 = 6.")
c("friends", 40, "Which friend is hidden in this sentence: 'I'm off out for a Chelsea bun'?", ["Rachel"], "foR A CHELsea hides RACHEL.")

c("games-toys", 30, "You roll two dice. In how many ways can they add up to 7, counting a 3 then a 4 as different from a 4 then a 3?", ["6", "Six"],
  "1+6, 2+5, 3+4, 4+3, 5+2 and 6+1.")
c("games-toys", 60, "On a chessboard, how many squares are the same colour as the bottom-left corner?", ["32", "Thirty-two"],
  "The colours alternate, so exactly half of the 64 squares match it.")

c("nature-environment", 50, "A box holds 5 spiders and some beetles, with 58 legs in all. Beetles have 6 legs. How many beetles are there?", ["3", "Three"],
  "The spiders have 5 × 8 = 40 legs, leaving 18, and 18 ÷ 6 = 3.")
c("nature-environment", 40, "A patch of lilies doubles in size every day and covers the whole pond on day 30. On which day did it cover half the pond?", ["29", "Day 29", "Twenty-nine"],
  "It doubles overnight, so the day before it was full it covered half.")

c("reality-tv", 60, "A dating show has 6 boys and 6 girls, and every boy goes on one date with every girl. How many dates is that?", ["36", "Thirty-six"],
  "Each of the 6 boys has 6 dates: 6 × 6 = 36.")
c("reality-tv", 70, "A Big Brother series starts with 16 housemates. One is evicted each week and nobody new arrives. After how many weeks are only 2 left?", ["14", "Fourteen"],
  "14 have to go, at one a week.")

c("record-breakers", 70, "Robert Wadlow, the tallest man ever recorded, was 2.72 m tall. How many centimetres taller was he than a 1.80 m man?", ["92", "92cm", "92 cm", "Ninety-two"],
  "272 cm − 180 cm = 92 cm.")
c("record-breakers", 50, "The tallest sunflower on record was 9.17 m. To the nearest whole number, how many 1.83 m men would you stack up to match it?", ["5", "Five"],
  "9.17 ÷ 1.83 is just over 5.")

c("scotland", 50, "Which Scottish town is hidden in this sentence: 'Let's play rugby on Saturday'?", ["Ayr"], "plAY Rugby hides AYR.")
c("scotland", 70, "Edinburgh to Glasgow is about 47 miles. A train averages 47 miles an hour. How many minutes does the journey take?", ["60", "Sixty", "1 hour", "One hour"],
  "47 miles at 47 miles an hour is one hour.")

c("tennis-golf", 40, "A Wimbledon singles draw starts with 128 players. How many matches must the champion win?", ["7", "Seven"],
  "Each round halves the field: 128, 64, 32, 16, 8, 4, 2, then one champion — 7 rounds.")
c("tennis-golf", 50, "On a par-72 course, a golfer makes 4 birdies, 2 bogeys and pars every other hole. What is their score?", ["70", "Seventy"],
  "Four birdies take off 4 and two bogeys add 2: 72 − 4 + 2 = 70.")

c("world-cup", 10, "A squad of 22 players each shake hands with every other player once. How many handshakes is that?", ["231", "Two hundred and thirty-one"],
  "Each of the 22 shakes 21 hands, and every handshake involves two people: 22 × 21 ÷ 2 = 231.")
c("world-cup", 30, "World Cups run every four years and none were missed after 1966. Counting from 1970 to 2026, how many tournaments is that?", ["15", "Fifteen"],
  "(2026 − 1970) ÷ 4 = 14 gaps, so 15 tournaments.")

c("the-office", 80, "An office has 12 staff. Half are made redundant, then 2 new people are hired. How many staff are there now?", ["8", "Eight"],
  "12 ÷ 2 = 6, and 6 + 2 = 8.")
c("the-office", 60, "A salesman sells 30 reams of paper on Monday and 5 more each day than the day before. How many does he sell on Friday?", ["50", "Fifty"],
  "Monday 30, Tuesday 35, Wednesday 40, Thursday 45, Friday 50.")

c("olympics", 20, "The Olympic rings are blue, black and red on top, yellow and green below. How many of the five rings link with exactly two others?", ["3", "Three"],
  "Yellow links blue and black, green links black and red, and black links yellow and green. Blue and red link with only one ring each.")
c("olympics", 70, "The Summer Olympics are held every four years, and there was one in 2024. Will there be one in 2050?", ["No"],
  "2024, 2028 … 2044, 2048, 2052: 2050 isn't a multiple of four years on.")

c("usa", 80, "The US flag has 13 stripes and 50 stars. How many more stars than stripes is that?", ["37", "Thirty-seven"], "50 − 13 = 37.")
c("usa", 40, "Which US state is hidden in this sentence: 'Put a hat on before you go out'?", ["Utah"], "pUT A Hat hides UTAH.")

c("world-geography", 50, "Which country is hidden in this sentence: 'Can a dad cook dinner?'", ["Canada"], "CAN A DAd hides CANADA.")
c("world-geography", 50, "Which country is hidden in this sentence: 'Hope runs deep in this family'?", ["Peru"],
  "hoPE RUns hides PERU.")

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__c2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'puzzles in', len(OUT), 'topics:', ' '.join(OUT))
