# Bank session 11 Oct 2026: 6 more Only One prompts (sport line-ups and classic games) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name one of the seven events in the women's heptathlon", ["100 metres hurdles/100m hurdles/Hurdles", "High jump", "Shot put/Shot", "200 metres/200m", "Long jump", "Javelin", "800 metres/800m"]),
 ("Name a playing position in a rugby union team", ["Prop/Loosehead prop/Tighthead prop", "Hooker", "Lock/Second row", "Flanker/Blindside flanker/Openside flanker", "Number 8/Number eight", "Scrum-half", "Fly-half/Outside half/Stand-off", "Centre/Inside centre/Outside centre", "Wing/Winger", "Full-back"]),
 ("Name a card colour or an action card in Uno", ["Red", "Yellow", "Green", "Blue", "Skip", "Reverse", "Draw Two/Draw 2/+2", "Wild", "Wild Draw Four/Wild Draw 4/+4"]),
 ("Name a colour or a body part the spinner calls in Twister", ["Red", "Yellow", "Green", "Blue", "Left hand", "Right hand", "Left foot", "Right foot"]),
 ("Name one of the 24 faces in the original Guess Who?", ["Alex", "Alfred", "Anita", "Anne", "Bernard", "Bill", "Charles", "Claire", "David", "Eric", "Frans", "George", "Herman", "Joe", "Maria", "Max", "Paul", "Peter", "Philip", "Richard", "Robert", "Sam", "Susan", "Tom"]),
 ("Name one of the 22 Major Arcana tarot cards", ["The Fool/Fool", "The Magician/Magician", "The High Priestess/High Priestess", "The Empress/Empress", "The Emperor/Emperor", "The Hierophant/Hierophant", "The Lovers/Lovers", "The Chariot/Chariot", "Strength", "The Hermit/Hermit", "Wheel of Fortune/The Wheel of Fortune", "Justice", "The Hanged Man/Hanged Man", "Death", "Temperance", "The Devil/Devil", "The Tower/Tower", "The Star/Star", "The Moon/Moon", "The Sun/Sun", "Judgement/Judgment", "The World/World"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
