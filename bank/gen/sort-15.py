# Bank session 11 Oct 2026: 12 more Categorise questions -> bank/sort-12.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("UK geography", ["North East England", "North West England", "towns"], "medium", "A town in the North East or the North West?", "North East", "North West", ["Hexham", "Morpeth", "Hartlepool", "Darlington"], ["Wigan", "Blackburn", "Kendal", "Warrington"])
s("Food and drink", ["breakfast", "chocolate"], "easy", "A breakfast cereal or a chocolate bar?", "Cereal", "Chocolate bar", ["Shreddies", "Weetabix", "Cheerios", "Frosties"], ["Twix", "Picnic", "Boost", "Lion Bar"])
s("Film", ["Daniel Day-Lewis", "Tom Hanks", "actors"], "medium", "Played by Daniel Day-Lewis or by Tom Hanks?", "Daniel Day-Lewis", "Tom Hanks", ["Abraham Lincoln", "Daniel Plainview", "Christy Brown", "Bill the Butcher"], ["Forrest Gump", "Andrew Beckett", "Captain Miller", "Chuck Noland"])
s("Education", ["universities", "Oxford", "Ivy League"], "medium", "An Ivy League university or an Oxford college?", "Ivy League", "Oxford college", ["Harvard", "Yale", "Princeton", "Cornell"], ["Balliol", "Magdalen", "Christ Church", "Exeter"])
s("Music", ["dance", "Latin America", "Europe"], "medium", "A dance from Latin America or from Europe?", "Latin America", "Europe", ["Tango", "Samba", "Salsa", "Rumba"], ["Waltz", "Polka", "Flamenco", "Can-can"])
s("Football", ["Tottenham", "Arsenal", "north London"], "medium", "A Tottenham legend or an Arsenal legend?", "Tottenham", "Arsenal", ["Glenn Hoddle", "Jimmy Greaves", "Gary Mabbutt", "Harry Kane"], ["Thierry Henry", "Tony Adams", "Ian Wright", "Dennis Bergkamp"])
s("Football", ["Liverpool", "Manchester United", "managers"], "easy", "Managed Liverpool or managed Manchester United?", "Liverpool", "Manchester United", ["Bill Shankly", "Bob Paisley", "Jürgen Klopp", "Rafael Benítez"], ["Matt Busby", "Alex Ferguson", "Ole Gunnar Solskjær", "Erik ten Hag"])
s("Famous people", ["Scotland", "Ireland", "birthplaces"], "medium", "Born in Scotland or in the Republic of Ireland?", "Scotland", "Republic of Ireland", ["Sean Connery", "Billy Connolly", "Annie Lennox", "Ewan McGregor"], ["Bono", "Colin Farrell", "Pierce Brosnan", "Enya"])
s("Books", ["Harry Potter", "Hogwarts"], "easy", "A Hogwarts teacher or a Hogwarts pupil?", "Teacher", "Pupil", ["Snape", "McGonagall", "Flitwick", "Lupin"], ["Neville Longbottom", "Luna Lovegood", "Cedric Diggory", "Cho Chang"])
s("Animals", ["birds", "flight"], "easy", "A bird that can fly, or one that can't?", "Can fly", "Can't fly", ["Albatross", "Swift", "Puffin", "Golden eagle"], ["Ostrich", "Emu", "Kiwi", "Penguin"])
s("Sport", ["stadiums", "rugby union", "football"], "medium", "A football ground or a rugby union ground?", "Football", "Rugby union", ["Anfield", "Molineux", "Craven Cottage", "Selhurst Park"], ["Twickenham", "Murrayfield", "Kingsholm", "Welford Road"])
s("TV", ["Strictly Come Dancing", "Bake Off"], "easy", "A Strictly judge, or a Bake Off judge or host?", "Strictly", "Bake Off", ["Craig Revel Horwood", "Shirley Ballas", "Motsi Mabuse", "Bruno Tonioli"], ["Paul Hollywood", "Prue Leith", "Noel Fielding", "Alison Hammond"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-12.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
