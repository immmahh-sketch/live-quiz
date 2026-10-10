# Bank session 10 Oct 2026: 20 more 1% Club puzzles -> bank/club-6.json. Logic, number and wordplay, each with a
# one-line "why". Tested against every club puzzle in the live bank with a copy of the server's near-duplicate rule
# (word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})


c(90, "Numbers", ["pizza", "fractions"], "A pizza is cut into 8 slices and you eat 3 of them. How many slices are left?", ["5", "Five"], "8 − 3 = 5.")
c(80, "Logic", ["days", "calendar"], "If today is Monday, what day will it be three days from now?", ["Thursday"], "Tuesday, Wednesday, Thursday.")
c(70, "Wordplay", ["anagrams", "capitals"], "Unscramble NEDLON to find a capital city.", ["London"], "N-E-D-L-O-N rearranges to LONDON.")
c(40, "Numbers", ["chess", "squares"], "Counting only the small squares, how many squares are there on a chessboard?", ["64", "Sixty-four"], "An 8 × 8 board: 8 × 8 = 64.")
c(90, "Numbers", ["legs", "animals"], "An octopus and a spider meet on the seabed. How many legs do they have between them?", ["16", "Sixteen"], "An octopus has 8 arms or legs and a spider has 8 legs: 8 + 8 = 16.")
c(80, "Numbers", ["puppies", "adding"], "A family's dog has six puppies. They give two away, then she has three more. How many puppies do they have now?", ["7", "Seven"], "6 − 2 + 3 = 7.")
c(70, "Numbers", ["time"], "How many minutes pass between quarter to ten and quarter past eleven?", ["90", "Ninety"], "9:45 to 10:45 is 60 minutes, then 30 more to 11:15.")
c(70, "Wordplay", ["anagrams", "food"], "Rearrange the letters of TEAM to make something you might eat.", ["Meat"], "T-E-A-M makes MEAT.")
c(60, "Numbers", ["percentages", "shopping"], "A £20 shirt has 25% knocked off in a sale. What does it cost now?", ["£15", "15", "15 pounds"], "25% of £20 is £5, and £20 − £5 = £15.")
c(50, "Logic", ["ages"], "Kate is 8 and her brother is twice her age. When Kate turns 16, how old will her brother be?", ["24", "Twenty-four"], "He's 16 now, 8 years older; in 8 years he'll be 24, not double her age.")
c(40, "Numbers", ["patterns"], "Spot the pattern in the gaps: 3, 6, 11, 18, 27. Which number follows?", ["38", "Thirty-eight"], "The gaps go up by odd numbers, 3, 5, 7, 9, so the next gap is 11: 27 + 11 = 38.")
c(40, "Wordplay", ["compound words"], "Which word goes in front of BALL, PRINT and PATH to make three new words?", ["Foot"], "Football, footprint and footpath.")
c(30, "Logic", ["families", "siblings"], "Four brothers each have exactly one sister. How many children are in the family?", ["5", "Five"], "They all share the same sister: 4 boys + 1 girl = 5.")
c(20, "Numbers", ["percentages"], "Take ten per cent of 10,000, then ten per cent of that. What are you left with?", ["100", "One hundred"], "10% of 10,000 is 1,000, and 10% of 1,000 is 100.")
c(20, "Logic", ["shapes", "triangles"], "Draw a six-pointed star as two overlapping triangles. Counting big and small, how many triangles can you see?", ["8", "Eight"], "The two big triangles plus the six small points: 2 + 6 = 8.")
c(10, "Numbers", ["mental arithmetic", "tricks"], "Add these in your head: 1,000 + 40 + 1,000 + 30 + 1,000 + 20 + 1,000 + 10. What's the total?", ["4100", "4,100"], "Four thousands make 4,000 and 40 + 30 + 20 + 10 = 100: 4,100. Many say 5,000.")
c(1, "Numbers", ["squares", "grids"], "A board is four tiles wide and four tiles tall. Counting every square you can make from whole tiles, big and small, how many are there?", ["30", "Thirty"], "16 + 9 + 4 + 1 = 30.")

c(30, "Numbers", ["prime numbers"], "There's only one even prime number. What is it?", ["2", "Two"], "Every other even number divides by 2, so only 2 itself is prime.")
c(5, "Logic", ["ponds", "doubling"], "Lily pads on a pond double in area every day, and the pond is fully covered on day 30. On which day was it half covered?", ["29", "Day 29", "The 29th"], "It doubles overnight, so half covered is just one day earlier.")

c(30, "Numbers", ["money", "coins"], "Using normal UK coins, what is the fewest coins you need to pay exactly 88p?", ["6", "Six"], "50p + 20p + 10p + 5p + 2p + 1p = 88p.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
