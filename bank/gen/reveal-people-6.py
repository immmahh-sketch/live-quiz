# Bank session 10 Oct 2026 (fifth pass): more Picture Reveal faces -> bank/reveal-people-6.json
# (Wikipedia title, accepted answers, difficulty). Nobody already in the live bank; mostly people whose Wikipedia lead
# photo is a portrait. Stock with PEOPLE=bank/reveal-people-6.json node tools/reveal-stock.mjs, then contact-sheet them.
import json, os
P = [
 # the North East
 ("Sam Fender", ["Sam Fender", "Fender"], "medium"), ("Brian Johnson", ["Brian Johnson"], "hard"), ("Lauren Laverne", ["Lauren Laverne", "Laverne"], "medium"),
 ("Tim Healy", ["Tim Healy", "Healy"], "hard"), ("Kevin Whately", ["Kevin Whately", "Whately"], "medium"), ("Jill Halfpenny", ["Jill Halfpenny", "Halfpenny"], "medium"),
 ("Charlie Hunnam", ["Charlie Hunnam", "Hunnam"], "medium"), ("Chris Ramsey (comedian)", ["Chris Ramsey"], "medium"), ("Brendan Foster", ["Brendan Foster"], "hard"),
 ("Steve Cram", ["Steve Cram", "Cram"], "medium"), ("Peter Beardsley", ["Peter Beardsley", "Beardsley"], "medium"), ("Chris Waddle", ["Chris Waddle", "Waddle"], "medium"),
 ("Neil Tennant", ["Neil Tennant", "Tennant"], "medium"), ("Hank Marvin", ["Hank Marvin"], "medium"), ("Eric Burdon", ["Eric Burdon", "Burdon"], "hard"),
 ("Joe McElderry", ["Joe McElderry", "McElderry"], "medium"), ("Denise Welch", ["Denise Welch", "Welch"], "medium"),
 # Hollywood's golden age
 ("Marlon Brando", ["Marlon Brando", "Brando"], "medium"), ("Humphrey Bogart", ["Humphrey Bogart", "Bogart", "Bogie"], "medium"), ("Cary Grant", ["Cary Grant"], "medium"),
 ("Grace Kelly", ["Grace Kelly", "Princess Grace"], "medium"), ("Elizabeth Taylor", ["Elizabeth Taylor", "Liz Taylor"], "medium"), ("James Dean", ["James Dean"], "medium"),
 ("Steve McQueen", ["Steve McQueen", "McQueen"], "medium"), ("Paul Newman", ["Paul Newman", "Newman"], "medium"), ("Robert Redford", ["Robert Redford", "Redford"], "medium"),
 ("Judy Garland", ["Judy Garland", "Garland"], "medium"), ("Sophia Loren", ["Sophia Loren", "Loren"], "medium"), ("Brigitte Bardot", ["Brigitte Bardot", "Bardot"], "medium"),
 ("Barbra Streisand", ["Barbra Streisand", "Streisand", "Barbara Streisand"], "medium"),
 # film and TV today
 ("Emily Blunt", ["Emily Blunt", "Blunt"], "medium"), ("Rachel Weisz", ["Rachel Weisz", "Weisz"], "medium"), ("Daisy Ridley", ["Daisy Ridley", "Ridley"], "medium"),
 ("Mark Hamill", ["Mark Hamill", "Hamill"], "medium"), ("Chadwick Boseman", ["Chadwick Boseman", "Boseman"], "medium"), ("Viola Davis", ["Viola Davis"], "medium"),
 ("Sydney Sweeney", ["Sydney Sweeney", "Sweeney"], "medium"), ("Jacob Elordi", ["Jacob Elordi", "Elordi"], "hard"),
 # sport
 ("Jayne Torvill", ["Jayne Torvill", "Torvill"], "medium"), ("Christopher Dean", ["Christopher Dean", "Chris Dean"], "medium"), ("Sally Gunnell", ["Sally Gunnell", "Gunnell"], "medium"),
 ("Denise Lewis", ["Denise Lewis"], "medium"), ("Tanni Grey-Thompson", ["Tanni Grey-Thompson", "Tanni Grey Thompson"], "medium"), ("Dennis Bergkamp", ["Dennis Bergkamp", "Bergkamp"], "medium"),
 ("Didier Drogba", ["Didier Drogba", "Drogba"], "easy"), ("Luka Modrić", ["Luka Modrić", "Luka Modric", "Modric"], "medium"), ("Jack Nicklaus", ["Jack Nicklaus", "Nicklaus"], "medium"),
 ("Alex Higgins", ["Alex Higgins", "Hurricane Higgins", "Higgins"], "medium"), ("Eric Bristow", ["Eric Bristow", "Bristow"], "hard"), ("Ruud Gullit", ["Ruud Gullit", "Gullit"], "medium"),
]
NO_PHOTO = {"Jill Halfpenny", "Jacob Elordi"}
# Stocked, then retired after the contact sheet (action/stage shot, sunglasses, or face too small or dark):
RETIRED = {"Alex Higgins", "Brendan Foster", "Christopher Dean", "Chris Waddle", "Hank Marvin", "Eric Burdon", "Lauren Laverne", "Tim Healy", "Steve McQueen"}
P = [p for p in P if p[0] not in RETIRED | NO_PHOTO]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": a, "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
