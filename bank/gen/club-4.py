# Bank session 9 Oct 2026 (third pass): 2 more 1% Club puzzles for 12 broad topics with 4–5 live. Genuine puzzles — a
# hidden word, a little working or a trap — each with a one-line "why". pct is from CLUB_PCTS; difficulty follows it.
# Writes bank/topics/<slug>__c4.json; check with tools/near-dup-sim.mjs, then import each with
#   FILE=<slug>__c4 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = {}
def c(slug, pct, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.setdefault(slug, []).append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff})

c("words-language", 10, "Take one letter at a time from STARTLING so that a real word is always left, until one letter remains. Which letter is it?", ["I"],
  "STARTLING, STARTING, STARING, STRING, STING, SING, SIN, IN, I.")
c("words-language", 20, "Which word of seven letters is full of letters?", ["Postbox", "Mailbox", "Letterbox"], "A postbox holds the post: letters.")

c("action-films", 60, "Which action film is hidden in this sentence: 'The courier rushed past speedily'?", ["Speed"], "SPEEDily hides SPEED.")
c("action-films", 40, "Bond is agent 007. Counting only the numbers between 001 and 007, not including either, how many agent numbers are there?", ["5", "Five"],
  "002, 003, 004, 005 and 006.")

c("animals", 40, "Which bird is hidden in this sentence: 'The show led to a standing ovation'?", ["Owl"], "shOW Led hides OWL.")
c("animals", 70, "An octopus has 8 arms and a starfish has 5. How many arms do 3 octopuses and 4 starfish have altogether?", ["44", "Forty-four"],
  "3 × 8 = 24 and 4 × 5 = 20: 24 + 20 = 44.")

c("beer-wine-spirits", 50, "Which spirit is hidden in this sentence: 'He beat the drum all night'?", ["Rum"], "dRUM hides RUM.")
c("beer-wine-spirits", 70, "A pint is 568 millilitres. How many millilitres are there in half a pint?", ["284", "284ml", "284 ml"], "568 ÷ 2 = 284.")

c("bonfire-night", 40, "If Bonfire Night, 5 November, falls on a Saturday, what day of the week is Halloween?", ["Monday"],
  "Halloween, 31 October, is five days earlier: Saturday back five days is Monday.")
c("bonfire-night", 70, "A bonfire is lit at 6:45pm and burns for 2 hours 40 minutes. What time does it go out?", ["9:25pm", "9:25", "21:25", "Twenty-five past nine"],
  "6:45 plus 2 hours is 8:45, plus 40 minutes is 9:25.")

c("books", 50, "Which Jane Austen novel is hidden in this sentence: 'It was quite a dilemma'?", ["Emma"], "dilEMMA hides EMMA.")
c("books", 40, "Which Dickens hero is hidden in this sentence: 'The chimp I promised you is tame'?", ["Pip"], "chimP I Promised hides PIP.")

c("boxing-combat", 40, "Which boxing punch is hidden in this sentence: 'Raj aboard the ship waved'?", ["Jab"], "raJ ABoard hides JAB.")
c("boxing-combat", 70, "A boxer weighs 70 kg and has to make 66.7 kg. How much weight must he lose?", ["3.3 kg", "3.3", "3.3kg"], "70 − 66.7 = 3.3 kg.")

c("boy-bands-girl-groups", 40, "Which boy band is hidden in this sentence: 'The bus tediously crawled along'?", ["Busted"], "BUS TEDiously hides BUSTED.")
c("boy-bands-girl-groups", 60, "One Direction started with five members and one left. If each who stayed made two solo albums, how many solo albums is that?", ["8", "Eight"],
  "Four stayed, and 4 × 2 = 8.")

c("british-films", 70, "Add the numbers in the titles '127 Hours' and '28 Days Later'.", ["155", "One hundred and fifty-five"], "127 + 28 = 155.")
c("british-films", 40, "Which film is hidden in this sentence: 'He won Kate's heart at last'?", ["Wonka"], "WON KAte's hides WONKA.")

c("british-food", 60, "A recipe uses 3 eggs to make 12 Yorkshire puddings. How many eggs do you need for 20?", ["5", "Five"],
  "That's one egg for every 4 puddings, and 20 ÷ 4 = 5.")
c("british-food", 50, "Which fish is hidden in this sentence: 'Their music odyssey began in Leeds'?", ["Cod"], "musiC ODyssey hides COD.")

c("british-history", 40, "Which Tudor queen's name is hidden in this sentence: 'Don't harm a rye field'?", ["Mary"], "harM A RYe hides MARY.")
c("british-history", 60, "The Battle of Hastings was in 1066 and the Battle of Waterloo in 1815. How many years apart were they?", ["749", "Seven hundred and forty-nine"], "1815 − 1066 = 749.")

c("british-sitcoms", 40, "Which sitcom character is hidden in this sentence: 'He sold elbow grease door to door'?", ["Del", "Del Boy"], "solD ELbow hides DEL.")
c("british-sitcoms", 70, "Fawlty Towers ran for two series of six episodes. How many episodes would three series have made?", ["18", "Eighteen"], "3 × 6 = 18.")

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__c4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'puzzles in', len(OUT), 'topics:', ' '.join(OUT))
