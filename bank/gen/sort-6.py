# Bank session 10 Oct 2026: 14 more Categorise questions -> bank/sort-3.json. Two groups, four items each (three for the
# colours). Each pair of categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Music", ["Britpop", "Oasis", "Blur"], "easy", "Oasis song or Blur song?", "Oasis", "Blur", ["Wonderwall", "Don't Look Back in Anger", "Supersonic", "Champagne Supernova"], ["Parklife", "Song 2", "Country House", "The Universal"])
s("The human body", ["bones"], "medium", "Bone in the arm or bone in the leg?", "Arm", "Leg", ["Humerus", "Radius", "Ulna"], ["Femur", "Tibia", "Fibula", "Patella"])
s("UK geography", ["Yorkshire", "Lancashire"], "medium", "In Yorkshire or in Lancashire?", "Yorkshire", "Lancashire", ["Whitby", "Harrogate", "Scarborough", "Skipton"], ["Blackpool", "Lancaster", "Preston", "Burnley"])
s("Books", ["Dickens", "Hardy", "novels"], "medium", "Charles Dickens novel or Thomas Hardy novel?", "Dickens", "Hardy", ["Bleak House", "Great Expectations", "Little Dorrit", "Hard Times"], ["Tess of the d'Urbervilles", "Far from the Madding Crowd", "Jude the Obscure", "The Mayor of Casterbridge"])
s("Music", ["Rolling Stones", "The Who"], "medium", "Rolling Stones song or The Who song?", "Rolling Stones", "The Who", ["(I Can't Get No) Satisfaction", "Paint It Black", "Angie", "Brown Sugar"], ["My Generation", "Pinball Wizard", "Baba O'Riley", "Substitute"])
s("Music", ["Elton John", "Rod Stewart"], "easy", "Elton John hit or Rod Stewart hit?", "Elton John", "Rod Stewart", ["Rocket Man", "Your Song", "Tiny Dancer", "Candle in the Wind"], ["Maggie May", "Sailing", "Baby Jane", "Hot Legs"])
s("Nature", ["birds"], "medium", "Bird of prey or seabird?", "Bird of prey", "Seabird", ["Kestrel", "Buzzard", "Osprey", "Peregrine falcon"], ["Puffin", "Gannet", "Kittiwake", "Guillemot"])
s("UK geography", ["mountains", "Scotland", "Wales"], "medium", "Mountain in Scotland or mountain in Wales?", "Scotland", "Wales", ["Ben Nevis", "Ben Macdui", "Cairn Gorm", "Schiehallion"], ["Yr Wyddfa (Snowdon)", "Pen y Fan", "Cadair Idris", "Tryfan"])
s("Games and toys", ["Monopoly", "London"], "medium", "On the London Monopoly board or not?", "On the board", "Not on the board", ["Old Kent Road", "Pall Mall", "Vine Street", "Whitehall"], ["Carnaby Street", "Kensington High Street", "Baker Street", "Abbey Road"])
s("Music", ["Madonna", "Kylie Minogue"], "easy", "Madonna hit or Kylie hit?", "Madonna", "Kylie", ["Vogue", "Like a Prayer", "Holiday", "Material Girl"], ["Spinning Around", "Can't Get You Out of My Head", "I Should Be So Lucky", "Better the Devil You Know"])
s("Film", ["Hitchcock", "Spielberg", "directors"], "easy", "Directed by Alfred Hitchcock or by Steven Spielberg?", "Hitchcock", "Spielberg", ["Psycho", "Vertigo", "The Birds", "Rear Window"], ["Jaws", "E.T.", "Jurassic Park", "Schindler's List"])
s("Science", ["elements", "wow"], "hard", "Element named after a place or after a person?", "A place", "A person", ["Americium", "Germanium", "Polonium", "Francium"], ["Einsteinium", "Curium", "Nobelium", "Mendelevium"])
s("UK geography", ["Shipping Forecast", "sea"], "hard", "A Shipping Forecast sea area or not?", "Sea area", "Not a sea area", ["Dogger", "Fisher", "German Bight", "Viking"], ["Solent", "Mersey", "Cardigan Bay", "Morecambe"])
s("British sitcoms", ["Blackadder", "Only Fools and Horses"], "easy", "'Blackadder' character or 'Only Fools and Horses' character?", "Blackadder", "Only Fools and Horses", ["Baldrick", "Percy", "General Melchett", "Captain Darling"], ["Trigger", "Boycie", "Denzil", "Uncle Albert"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
