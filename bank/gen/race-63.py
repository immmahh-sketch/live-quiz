# Bank session 10 Oct 2026: 2 more general races -> bank/race-63.json. 20 rows each, target 10; wrong options are
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

race("which famous Duke?", "History", "hard", ["dukes", "royals"], [
 ("The 'Iron Duke' who won at Waterloo", "Wellington", ["Beaufort", "Somerset", "Portland"]), ("Given Blenheim Palace for beating the French in 1704", "Marlborough", ["Beaufort", "Grafton", "Rutland"]),
 ("Prince Philip's title, given on his wedding day in 1947", "Edinburgh", ["Gloucester", "Connaught", "Albany"]), ("The grand old one who marched his ten thousand men up the hill", "York", ["Gloucester", "Albany", "Buckingham"]),
 ("Edward VIII's title after he abdicated", "Windsor", ["Gloucester", "Cambridge", "Albany"]), ("Prince Harry's title since his 2018 wedding", "Sussex", ["Cambridge", "Gloucester", "Albany"]),
 ("The Earl Marshal, who organises coronations and state funerals", "Norfolk", ["Somerset", "Suffolk", "Buckingham"]), ("Head of the Grosvenor family, who own much of Mayfair and Belgravia", "Westminster", ["Buckingham", "Portland", "Grafton"]),
 ("His Alnwick Castle doubled as Hogwarts", "Northumberland", ["Sutherland", "Roxburghe", "Buccleuch"]), ("Has Europe's only legal private army, his own Highlanders", "Atholl", ["Argyll", "Montrose", "Hamilton"]),
 ("Woburn Abbey and its safari park", "Bedford", ["Grafton", "Manchester", "Rutland"]), ("Charles II's son whose 1685 rebellion ended at Sedgemoor", "Monmouth", ["Buckingham", "Somerset", "Grafton"]),
 ("Said to have been drowned in a barrel of malmsey wine in the Tower", "Clarence", ["Gloucester", "Buckingham", "Somerset"]), ("Chatsworth House is the family seat", "Devonshire", ["Rutland", "Portland", "Leeds"]),
 ("'Butcher' who crushed the Jacobites at Culloden", "Cumberland", ["Hamilton", "Montrose", "Fife"]), ("The heir to the throne's title in England, with its own estate", "Cornwall", ["Albany", "Somerset", "Suffolk"]),
 ("The heir to the throne's title in Scotland", "Rothesay", ["Albany", "Fife", "Montrose"]), ("Hosts the Festival of Speed at Goodwood", "Richmond", ["Beaufort", "Rutland", "Grafton"]),
 ("The monarch's own title in Lancashire, toasted as 'the Duke'", "Lancaster", ["Leeds", "Manchester", "Suffolk"]), ("Presented the Wimbledon trophies for decades as All England Club president", "Kent", ["Gloucester", "Buckingham", "Suffolk"])])

race("which town or city is this shopping centre in?", "Britain", "medium", ["shopping centres", "towns"], [
 ("The Metrocentre", "Gateshead", ["South Shields", "Washington", "Middlesbrough"]), ("The Bullring", "Birmingham", ["Wolverhampton", "Coventry", "Derby"]),
 ("The Trafford Centre", "Manchester", ["Bolton", "Stockport", "Wigan"]), ("Meadowhall", "Sheffield", ["Doncaster", "Barnsley", "Chesterfield"]),
 ("Bluewater", "Dartford", ["Chatham", "Maidstone", "Romford"]), ("Lakeside", "Thurrock", ["Basildon", "Romford", "Chelmsford"]),
 ("Eldon Square", "Newcastle", ["Durham", "Middlesbrough", "Carlisle"]), ("St David's", "Cardiff", ["Swansea", "Newport", "Bath"]),
 ("Buchanan Galleries", "Glasgow", ["Dundee", "Stirling", "Inverness"]), ("Cribbs Causeway", "Bristol", ["Bath", "Swindon", "Exeter"]),
 ("White Rose", "Leeds", ["Bradford", "York", "Wakefield"]), ("Victoria Square, under its glass dome", "Belfast", ["Derry", "Lisburn", "Newry"]),
 ("St James Quarter", "Edinburgh", ["Dundee", "Stirling", "Perth"]), ("Highcross", "Leicester", ["Derby", "Northampton", "Coventry"]),
 ("Churchill Square", "Brighton", ["Worthing", "Eastbourne", "Hastings"]), ("The Bridges", "Sunderland", ["South Shields", "Washington", "Durham"]),
 ("The Victoria Centre", "Nottingham", ["Derby", "Lincoln", "Northampton"]), ("Union Square", "Aberdeen", ["Dundee", "Inverness", "Perth"]),
 ("Drake Circus", "Plymouth", ["Exeter", "Torquay", "Truro"]), ("WestQuay", "Southampton", ["Portsmouth", "Bournemouth", "Winchester"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-63.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
