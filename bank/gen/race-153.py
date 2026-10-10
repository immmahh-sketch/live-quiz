# Bank session 11 Oct 2026: 3 more general races -> bank/race-153.json (spy words, gym words, grammar words). 20 rows each, target 10; wrong options are
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

race("what's this spy word?", "History", "medium", ["spies", "espionage", "words"], [
 ("A spy planted deep inside an organisation", "Mole", ["Badger", "Vole", "Stoat"]),
 ("Pretends to spy for one side while really working for the other", "Double agent", ["Field agent", "Handler", "Courier"]),
 ("An agent who lives a normal life for years until called on", "Sleeper", ["Runner", "Tracker", "Watcher"]),
 ("A hidden spot where messages are left for another spy to collect", "Dead drop", ["Cold call", "Blind date", "Pigeonhole"]),
 ("A secret hideout where agents can lie low", "Safe house", ["Halfway house", "Lodge", "Bothy"]),
 ("The fake life story a spy pretends is true", "Cover story", ["Bedtime story", "Ghost story", "Shaggy-dog story"]),
 ("A secret name used on an operation instead of the real one", "Codename", ["Surname", "Maiden name", "Place name"]),
 ("Britain's foreign intelligence service, where James Bond works", "MI6", ["MI5", "Special Branch", "Scotland Yard"]),
 ("The Cheltenham listening and code-breaking centre", "GCHQ", ["MI5", "CIA", "Interpol"]),
 ("The Soviet Union's security and spy agency", "KGB", ["Stasi", "CIA", "Mossad"]),
 ("Where Alan Turing's team cracked German codes in the war", "Bletchley Park", ["Porton Down", "Greenham Common", "Menwith Hill"]),
 ("The German cipher machine they cracked", "Enigma", ["Colossus", "Bombe", "Babbage"]),
 ("A tiny hidden microphone", "Bug", ["Mite", "Tick", "Flea"]),
 ("A spy who switches sides and flees to the enemy", "Defector", ["Refugee", "Exile", "Emigrant"]),
 ("Philby, Burgess, Maclean, Blunt and Cairncross", "Cambridge Five", ["Birmingham Six", "Guildford Four", "Famous Five"]),
 ("Bond's gadget-maker, by a single letter", "Q", ["C", "X", "K"]),
 ("Writing that only shows when it's heated, made with lemon juice", "Invisible ink", ["Shorthand", "Morse code", "Braille"]),
 ("A secret code for scrambling messages", "Cipher", ["Sonnet", "Haiku", "Limerick"]),
 ("Using seduction to trap a target", "Honeytrap", ["Mousetrap", "Booby trap", "Speed trap"]),
 ("A person passing secrets to a spy's handler", "Asset", ["Liability", "Debit", "Overhead"])])

race("what's this gym word?", "Sport", "easy", ["gym", "fitness", "words"], [
 ("The running machine", "Treadmill", ["Exercise bike", "Stepper", "Cross-trainer"]),
 ("A short bar with a weight at each end, held in one hand", "Dumbbell", ["Baton", "Truncheon", "Rolling pin"]),
 ("A cannonball-shaped weight with a handle on top", "Kettlebell", ["Medicine ball", "Shot put", "Bowling ball"]),
 ("The long bar loaded with plates and lifted with both hands", "Barbell", ["Crowbar", "Handlebar", "Bar stool"]),
 ("How many times you lift in one go", "Reps", ["Rounds", "Heats", "Innings"]),
 ("Groups of those lifts, with a rest in between", "Sets", ["Matches", "Frames", "Legs"]),
 ("Lowering your hips as if sitting on an invisible chair", "Squat", ["Curtsey", "Plié", "Bow"]),
 ("Stepping forward and dropping the back knee", "Lunge", ["Leapfrog", "Hopscotch", "Skip"]),
 ("Holding your body straight on your forearms and toes", "Plank", ["Beam", "Joist", "Rafter"]),
 ("Squat, jump back, press-up, jump up, repeat", "Burpee", ["Hiccup", "Hokey cokey", "Twist"]),
 ("Pushing your body up off the floor with your arms", "Press-up", ["Pull-out", "Lift-off", "Drop-kick"]),
 ("Lying back and curling up to work your stomach", "Sit-up", ["Lie-in", "Sit-in", "Stand-off"]),
 ("A group workout on stationary bikes", "Spin class", ["Spin bowling", "Spin doctor", "Spin cycle"]),
 ("Someone you pay to coach you one-to-one", "Personal trainer", ["Personal shopper", "Personal assistant", "Valet"]),
 ("Slang for the stomach muscles", "Abs", ["Lats", "Glutes", "Quads"]),
 ("Slang for the chest muscles", "Pecs", ["Lats", "Glutes", "Quads"]),
 ("Gentle exercise at the end of a workout", "Cool-down", ["Warm-up", "Lie-down", "Shut-down"]),
 ("The machine where you pull a handle while sliding back and forth", "Rowing machine", ["Exercise bike", "Stepper", "Leg press"]),
 ("Short bursts of flat-out exercise, in four letters", "HIIT", ["BMI", "PB", "VO2"]),
 ("The drink downed after lifting weights, to build muscle", "Protein shake", ["Slush", "Cordial", "Squash"])])

race("what's this grammar word?", "Words and language", "medium", ["grammar", "punctuation", "English"], [
 ("The dot at the end of a sentence", "Full stop", ["Asterisk", "Tilde", "Bullet point"]),
 ("Separates the items in a list", "Comma", ["Slash", "Ampersand", "Dash"]),
 ("Shows something belongs, as in 'Tom's'", "Apostrophe", ["Asterisk", "Bracket", "Tilde"]),
 ("Two dots, one above the other, often before a list", "Colon", ["Umlaut", "Ampersand", "Asterisk"]),
 ("A dot above a comma, joining two closely linked sentences", "Semicolon", ["Ampersand", "Slash", "Dash"]),
 ("The short line in 'well-known'", "Hyphen", ["Underscore", "Slash", "Tilde"]),
 ("Ends a sentence that's shouted or surprising", "Exclamation mark", ["Question mark", "Asterisk", "Ampersand"]),
 ("Three dots that trail off...", "Ellipsis", ["Umlaut", "Bullet points", "Asterisk"]),
 ("A naming word, like 'table' or 'London'", "Noun", ["Article", "Prefix", "Preposition"]),
 ("A doing word, like 'run' or 'think'", "Verb", ["Article", "Suffix", "Preposition"]),
 ("Describes a noun, like 'big' or 'red'", "Adjective", ["Preposition", "Article", "Prefix"]),
 ("Describes how something's done, often ending in -ly", "Adverb", ["Suffix", "Article", "Preposition"]),
 ("Stands in for a noun, like 'she' or 'they'", "Pronoun", ["Article", "Prefix", "Preposition"]),
 ("A joining word, like 'and', 'but' or 'because'", "Conjunction", ["Preposition", "Article", "Interjection"]),
 ("A, E, I, O or U", "Vowel", ["Consonant", "Syllable", "Digraph"]),
 ("A word meaning the same as another", "Synonym", ["Homophone", "Acronym", "Anagram"]),
 ("A word meaning the opposite of another", "Antonym", ["Homophone", "Acronym", "Oxymoron"]),
 ("A comparison using 'like' or 'as', as in 'as brave as a lion'", "Simile", ["Hyperbole", "Idiom", "Alliteration"]),
 ("Saying one thing IS another, as in 'Life is a rollercoaster'", "Metaphor", ["Hyperbole", "Onomatopoeia", "Idiom"]),
 ("A word that reads the same both ways, like 'level'", "Palindrome", ["Anagram", "Acronym", "Homophone"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-153.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
