# Bank session 12 Oct 2026: new Wipeout boards -> bank/wipeout-80.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: other animals from the same stories and screens (Animal Farm's horse and donkey, a warthog, a hippo)
board("Famous fictional pigs", "Books", "medium", ["pigs", "fictional animals"],
 ["Babe", "Peppa Pig", "Miss Piggy", "Wilbur", "Napoleon", "Snowball", "Piglet", "Porky Pig", "Hamm", "Spider-Pig", "Pigling Bland", "Old Major", "Squealer", "Pinky and Perky", "Gub-Gub"],
 ["Pumbaa", "Boxer", "Benjamin", "Gloria", "Eeyore"])
# decoys: famous fictional foxes, wolves and a coyote
board("Famous fictional dogs", "TV", "easy", ["dogs", "fictional animals"],
 ["Lassie", "Snoopy", "Scooby-Doo", "Gromit", "K9", "Pluto", "Odie", "Toto", "Brian Griffin", "Santa's Little Helper", "Dougal", "Gnasher", "Nana", "Fang", "Snowy"],
 ["Fantastic Mr Fox", "Basil Brush", "Akela", "Wile E. Coyote", "Big Bad Wolf"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-80.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
