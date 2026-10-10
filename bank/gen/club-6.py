# Bank session 10 Oct 2026: 24 more 1% Club puzzles -> bank/club-4.json. Logic, number and wordplay, each with a
# one-line "why". Checked against every club puzzle already in the live bank (the classics are all in there already).
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Wordplay", ["compound words"], "Which word goes in front of 'fly', 'cup' and 'milk' to make three new words?", ["Butter"], "Butterfly, buttercup, buttermilk.")
c(90, "Numbers", ["legs"], "How many legs do four ducks and two cows have altogether?", ["16", "Sixteen"], "4 × 2 = 8 and 2 × 4 = 8: 8 + 8 = 16.")
c(90, "General", ["colours"], "Which colour do you get when you mix blue paint with yellow paint?", ["Green"], "Blue and yellow make green.")
c(80, "Numbers", ["food", "fractions"], "A pizza is cut into 8 slices and 3 friends eat 2 slices each. How many slices are left over?", ["2", "Two"], "3 × 2 = 6 eaten, and 8 − 6 = 2.")
c(80, "Numbers", ["arithmetic"], "A baker cracks a dozen and a half eggs into a big sponge mixture. How many eggs is that?", ["18", "Eighteen"], "12 + 6 = 18.")
c(80, "Numbers", ["arithmetic"], "A bus has 20 passengers. At the first stop 5 get off and 3 get on. At the next, 6 get off and 8 get on. How many are on the bus now?", ["20", "Twenty"], "20 − 5 + 3 = 18, then 18 − 6 + 8 = 20.")
c(70, "Logic", ["days"], "It's Wednesday today and our holiday starts in exactly 10 days' time. On which weekday does it start?", ["Saturday"], "Seven days on is Wednesday again; three more is Saturday.")
c(70, "Numbers", ["odd one out", "squares"], "Spot the number that doesn't belong: 9, 16, 25, 30, 36.", ["30", "Thirty"], "The others are square numbers: 3², 4², 5², 6².")
c(60, "Wordplay", ["letters"], "Put one letter in front of ONE to make a word meaning 'not any'.", ["None", "NONE"], "N + ONE = NONE.")
c(60, "Numbers", ["time"], "A cooking timer is set for one fifth of an hour. How many minutes is that?", ["12", "Twelve"], "60 ÷ 5 = 12.")
c(60, "Logic", ["months"], "Which month comes three months after November?", ["February"], "December, January, February.")
c(50, "Numbers", ["arithmetic"], "Three whole numbers in a row add up to 72. What is the biggest of them?", ["25", "Twenty-five"], "23 + 24 + 25 = 72.")
c(50, "Numbers", ["arithmetic"], "What is 7 times 8, take away 7 times 7?", ["7", "Seven"], "56 − 49 = 7 (or simply 7 × 1).")
c(40, "Numbers", ["ages"], "A dad is four times as old as his son. In 20 years he'll be only twice as old. How old is the son now?", ["10", "Ten"], "Son 10, dad 40; in 20 years they're 30 and 60.")
c(40, "Logic", ["shapes", "triangles"], "Draw a square and both of its diagonals. How many triangles can you count?", ["8", "Eight"], "Four small triangles, plus four big ones, each half of the square.")
c(40, "Numbers", ["factors"], "What is the biggest number that divides exactly into both 24 and 36?", ["12", "Twelve"], "24 = 2 × 12 and 36 = 3 × 12; nothing bigger goes into both.")
c(40, "Numbers", ["calendar"], "In a leap year, how many days are there from January to March inclusive?", ["91", "Ninety-one"], "31 + 29 + 31 = 91.")
c(40, "Numbers", ["primes"], "Prime numbers have no factors except 1 and themselves. Which is the next prime after 23?", ["29", "Twenty-nine"], "24 to 28 all divide by 2 or 3 (25 by 5); 29 is prime.")
c(30, "Logic", ["alphabet"], "Which letter is three places before the letter that comes two after T?", ["S"], "Two after T is V; three before V is S.")
c(20, "Numbers", ["sequences"], "Find the value that should end this sequence: 2, 3, 5, 9, 17, ?", ["33", "Thirty-three"], "The gaps double: +1, +2, +4, +8, then +16.")
c(20, "Wordplay", ["riddles"], "Which word is spelled incorrectly in every dictionary?", ["Incorrectly"], "The word 'incorrectly' is always spelled I-N-C-O-R-R-E-C-T-L-Y.")
c(10, "Numbers", ["sequences", "squares"], "Here's a puzzling sequence: 61, 52, 63, 94, 46. Which number comes after 46?", ["18", "Eighteen"], "They're the squares 16, 25, 36, 49, 64 written backwards; 81 backwards is 18.")
c(10, "Numbers", ["sequences"], "Carry on this pattern of numbers: 1, 2, 6, 24, 120, then what?", ["720"], "Multiply by 2, 3, 4, 5, then 6: 120 × 6 = 720.")
c(5, "Logic", ["clocks"], "A wall clock with hands loses 10 minutes every day. How many days until it shows the right time again?", ["72", "Seventy-two"], "It must lose a full 12 hours, 720 minutes: 720 ÷ 10 = 72 days.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
