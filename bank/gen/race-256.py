# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-256.json (Black Books; Phoenix Nights).
# Checked against every race in stock with lqsql/audit/race-overlap.py before importing.
# raceOk: 20 rows, 20 different right answers, no right answer among another row's options, no wrong option on 3+ rows.
import json, os
from collections import Counter
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    over = [w for w, n in Counter(w for _, _, wrong in rows for w in wrong).items() if n > 2]
    assert not over, (title, 'wrong option on 3+ rows', over)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("Black Books - name it", "Television", "medium", ["Black Books", "sitcoms", "Channel 4"], [
 ("The grumpy shop owner", "Bernard Black", ["Bernard Bresslaw", "Bernard Woolley", "Bernard Cribbins"]),
 ("The actor who played him", "Dylan Moran", ["Dylan Thomas", "Dylan Jones", "Dylan Hartley"]),
 ("His nationality", "Irish", ["Scottish", "Welsh", "English"]),
 ("His two vices", "Wine and cigarettes", ["Beer and crisps", "Tea and biscuits", "Coffee and cake"]),
 ("His shop", "A second-hand bookshop", ["A record shop", "A video shop", "An antique shop"]),
 ("The part of London it's in", "Bloomsbury", ["Camden", "Soho", "Notting Hill"]),
 ("His assistant", "Manny Bianco", ["Manny Russo", "Manny Rossi", "Manny Costa"]),
 ("The actor who played him", "Bill Bailey", ["Bill Oddie", "Bill Nighy", "Bill Paterson"]),
 ("Manny's old job", "Accountant", ["Lawyer", "Banker", "Teacher"]),
 ("The book Manny swallows", "The Little Book of Calm", ["The Little Book of Peace", "The Little Book of Zen", "The Little Book of Joy"]),
 ("The music quiz where that actor was a team captain", "Never Mind the Buzzcocks", ["Shooting Stars", "Pop Quiz", "A Question of Pop"]),
 ("The show he won in 2020", "Strictly Come Dancing", ["The Great British Bake Off", "I'm a Celebrity", "Dancing on Ice"]),
 ("Their friend next door", "Fran Katzenjammer", ["Fran Fine", "Fran Cosgrave", "Fran Kirby"]),
 ("The actress who played her", "Tamsin Greig", ["Tamsin Egerton", "Tamsin Outhwaite", "Tamsin Grey"]),
 ("Her gift shop", "Nifty Gifty", ["Gift Rift", "Present Tense", "Knick Knack"]),
 ("The writers", "Dylan Moran and Graham Linehan", ["Simon Pegg and Jessica Hynes", "Peter Kay and Paddy McGuinness", "Armando Iannucci and Chris Morris"]),
 ("The channel", "Channel 4", ["BBC Two", "ITV", "E4"]),
 ("The year it began", "2000", ["1996", "2004", "2008"]),
 ("Series made", "3", ["2", "4", "5"]),
 ("The award it won for best sitcom in 2001", "BAFTA", ["Emmy", "Golden Globe", "Oscar"])])

race("Phoenix Nights - name it", "Television", "medium", ["Phoenix Nights", "sitcoms", "Channel 4"], [
 ("The club", "The Phoenix Club", ["The Wheeltappers Club", "The Rovers Return", "The Nag's Head"]),
 ("Why it's called the Phoenix", "His last club burned down", ["It's on Phoenix Street", "It's named after a band", "It's a lucky name"]),
 ("The town it's in", "Bolton", ["Wigan", "Preston", "Blackburn"]),
 ("The owner", "Brian Potter", ["Brian Conley", "Brian Clough", "Brian Cant"]),
 ("The actor who played him", "Peter Kay", ["Peter Andre", "Peter Davison", "Peter Crouch"]),
 ("How the owner gets about", "A wheelchair", ["Crutches", "A walking stick", "A mobility scooter"]),
 ("The bouncers", "Max and Paddy", ["Mick and Mack", "Bill and Ben", "Pip and Squeak"]),
 ("The actor who played Paddy", "Paddy McGuinness", ["Paddy Considine", "Patrick Kielty", "Paddy Doherty"]),
 ("Their spin-off", "Max and Paddy's Road to Nowhere", ["Max and Paddy's Big Night Out", "Max and Paddy on Tour", "Max and Paddy Go East"]),
 ("Jerry 'the Saint' St Clair's job", "Compère", ["Barman", "Cook", "Treasurer"]),
 ("The co-writer who played him", "Dave Spikey", ["Dave Gorman", "Dave Lamb", "Dave Vitty"]),
 ("The resident band", "Les Alanos", ["The Alan Brothers", "Les Mis", "The Two Lesleys"]),
 ("The rival club owner", "Den Perry", ["Ken Perry", "Den Watts", "Dave Perry"]),
 ("His club", "The Banana Grove", ["The Coconut Grove", "The Mango Club", "The Banana Club"]),
 ("The channel", "Channel 4", ["BBC Two", "ITV", "BBC Three"]),
 ("The year it began", "2001", ["1997", "2004", "2008"]),
 ("Series made", "2", ["3", "4", "5"]),
 ("Peter Kay's earlier show", "That Peter Kay Thing", ["The Peter Kay Show", "Peter Kay's Britain", "Kay's Kitchen"]),
 ("His later sitcom with Sian Gibson", "Car Share", ["Benidorm", "Early Doors", "Shameless"]),
 ("His 2005 charity number one", "(Is This the Way to) Amarillo", ["Come On Eileen", "Mr Blue Sky", "Living Next Door to Alice"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-256.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
