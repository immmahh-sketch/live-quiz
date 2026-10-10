# Bank session 10 Oct 2026: 27 more 1% Club puzzles -> bank/club-3.json. Logic, number and wordplay, each with a
# one-line "why". Checked against every club puzzle already in the live bank (the classics are all in there already).
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Wordplay", ["compound words"], "Which word goes in front of 'flake', 'ball' and 'man' to make three new words?", ["Snow"], "Snowflake, snowball, snowman.")
c(90, "Numbers", ["shapes"], "How many sides do three triangles and two squares have altogether?", ["17", "Seventeen"], "3 × 3 = 9 and 2 × 4 = 8: 9 + 8 = 17.")
c(80, "Numbers", ["arithmetic"], "I double a number and add 6, and get 20. What was the number?", ["7", "Seven"], "20 − 6 = 14, and half of 14 is 7.")
c(80, "Numbers", ["time"], "A train leaves at 10:50 and the journey takes 1 hour 25 minutes. What time does it arrive?", ["12:15", "Quarter past twelve", "12.15"], "10:50 plus an hour is 11:50; 25 minutes more is 12:15.")
c(70, "Wordplay", ["letters"], "How many times does the letter E appear in the word SEVENTEEN?", ["4", "Four"], "sEvEntEEn: four Es.")
c(70, "Logic", ["ordering"], "Ann is taller than Ben, Ben is taller than Cal, and Cal is taller than Dee. Who is the second shortest?", ["Cal"], "Shortest first: Dee, Cal, Ben, Ann.")
c(70, "Numbers", ["dice"], "What do all six faces of an ordinary dice add up to?", ["21", "Twenty-one"], "1 + 2 + 3 + 4 + 5 + 6 = 21.")
c(70, "Numbers", ["sequences"], "What number is missing: 3, 6, 12, 24, ___, 96?", ["48", "Forty-eight"], "Each number doubles: 24 × 2 = 48, and 48 × 2 = 96.")
c(60, "Numbers", ["time"], "How many minutes are there in a quarter of a day?", ["360", "Three hundred and sixty"], "A quarter of 24 hours is 6 hours, and 6 × 60 = 360.")
c(60, "Wordplay", ["numbers as words"], "Written as a word, which whole number from 1 to 20 has the most letters?", ["Seventeen", "17"], "SEVENTEEN has nine letters; thirteen, fourteen, eighteen and nineteen have eight.")
c(60, "Wordplay", ["hidden words"], "Which capital city is hidden in this sentence: 'The parish rose to the challenge'?", ["Paris"], "PARISh hides PARIS.")
c(50, "Wordplay", ["hidden words"], "Which country is hidden in this sentence: 'Each in a box goes to the post office'?", ["China"], "eaCH IN A hides CHINA.")
c(50, "Wordplay", ["hidden words"], "Which colour is hidden in this sentence: 'The cab lacked a spare tyre'?", ["Black"], "caB LACKed hides BLACK.")
c(50, "Wordplay", ["hidden words"], "Which farm animal is hidden in this sentence: 'Eric owed his friend a fiver'?", ["Cow"], "eriC OWed hides COW.")
c(50, "Logic", ["days"], "What day comes three days after the day before Friday?", ["Sunday"], "The day before Friday is Thursday, and three days after Thursday is Sunday.")
c(40, "Wordplay", ["hidden words"], "Which planet is hidden in this sentence: 'They paid their gym arsenal of fees'?", ["Mars"], "gyM ARSenal hides MARS.")
c(40, "Numbers", ["calendar"], "Counting both days, how many days are there from 1 July to 31 December?", ["184", "One hundred and eighty-four"], "31 + 31 + 30 + 31 + 30 + 31 = 184, whatever the year.")
c(40, "Numbers", ["digits"], "What is the smallest four-digit number you can make using each of 3, 0, 7 and 1 once?", ["1037", "1,037"], "It can't start with 0, so put 1 first, then 0, 3 and 7.")
c(30, "Numbers", ["sequences"], "What is the next number: 1, 8, 27, 64, ___?", ["125", "One hundred and twenty-five"], "They are cubes: 1³, 2³, 3³, 4³, so next is 5³ = 125.")
c(30, "Logic", ["alphabet"], "How many letters of the alphabet come after the letter that comes after Q?", ["8", "Eight"], "The letter after Q is R, and S to Z is eight letters.")
c(30, "Logic", ["days"], "A week from yesterday will be Tuesday. What day is it today?", ["Wednesday"], "A week from yesterday is the same weekday as yesterday, so yesterday was Tuesday and today is Wednesday.")
c(20, "Logic", ["shapes"], "A six-pointed star is drawn as two overlapping triangles. How many triangles can you count in it altogether?", ["8", "Eight"], "The two big triangles, plus the six small points: 8.")
c(20, "Logic", ["weights"], "A brick weighs 1 kilogram plus half a brick. How much does a whole brick weigh?", ["2 kilograms", "2kg", "2 kg", "2", "Two kilograms"], "If 1 kg is the other half of the brick, the whole brick is 2 kg.")
c(20, "Wordplay", ["numbers as words"], "Write the numbers one to ten as words. How many of them contain the letter E?", ["7", "Seven"], "One, three, five, seven, eight, nine and ten: two, four and six don't.")
c(5, "Numbers", ["time", "palindromes"], "A digital clock shows 12:51. How many minutes until the four digits next read the same backwards?", ["40", "Forty", "40 minutes"], "The next time that reads the same both ways is 13:31, 40 minutes later.")
c(5, "Wordplay", ["upside down"], "Which five-letter word, written in capital letters, still reads the same when you turn the page upside down?", ["SWIMS", "Swims"], "Turn SWIMS through 180 degrees and the S, W, I, M and S land back as SWIMS.")
c(1, "Wordplay", ["anagrams"], "Rearrange the letters of NEW DOOR to make just one word.", ["One word", "ONE WORD"], "NEW DOOR is an anagram of ONE WORD, which is exactly what you were asked for.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
