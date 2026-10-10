# Bank session 10 Oct 2026: 2 more general races -> bank/race-103.json (old football grounds, Prime Ministers' spouses). 20 rows each, target 10; wrong options are
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

race("whose old ground was this?", "Football", "hard", ["football", "grounds", "nostalgia"], [
 ("Highbury", "Arsenal", ["Chelsea", "Fulham", "QPR"]),
 ("White Hart Lane", "Tottenham", ["Leyton Orient", "Millwall", "Charlton"]),
 ("Maine Road", "Manchester City", ["Manchester United", "Stockport County", "Oldham"]),
 ("Upton Park (the Boleyn Ground)", "West Ham", ["Charlton", "Leyton Orient", "Millwall"]),
 ("Roker Park", "Sunderland", ["Newcastle", "Hartlepool", "Gateshead"]),
 ("Ayresome Park", "Middlesbrough", ["Hartlepool", "York City", "Scarborough"]),
 ("The Dell", "Southampton", ["Portsmouth", "Bournemouth", "Swindon"]),
 ("Filbert Street", "Leicester", ["Nottingham Forest", "Notts County", "Northampton"]),
 ("The Baseball Ground", "Derby", ["Nottingham Forest", "Notts County", "Burton Albion"]),
 ("Burnden Park", "Bolton", ["Bury", "Wigan", "Blackburn"]),
 ("The Goldstone Ground", "Brighton", ["Crystal Palace", "Portsmouth", "Gillingham"]),
 ("Highfield Road", "Coventry", ["Birmingham", "Aston Villa", "Wolves"]),
 ("Leeds Road", "Huddersfield", ["Leeds", "Bradford City", "Halifax"]),
 ("The original Plough Lane", "Wimbledon", ["Crystal Palace", "Fulham", "Brentford"]),
 ("Elm Park", "Reading", ["Oxford United", "Swindon", "Wycombe"]),
 ("The Victoria Ground", "Stoke City", ["Port Vale", "Crewe", "Wolves"]),
 ("Feethams", "Darlington", ["Hartlepool", "York City", "Scarborough"]),
 ("Saltergate", "Chesterfield", ["Mansfield", "Rotherham", "Sheffield Wednesday"]),
 ("Gay Meadow", "Shrewsbury", ["Wrexham", "Telford", "Hereford"]),
 ("Eastville", "Bristol Rovers", ["Bristol City", "Swindon", "Cheltenham"])])

race("which Prime Minister were they married to?", "Politics", "medium", ["Prime Ministers", "spouses"], [
 ("Denis", "Margaret Thatcher", ["Edward Heath", "Ramsay MacDonald", "Bonar Law"]),
 ("Cherie", "Tony Blair", ["Edward Heath", "Herbert Asquith", "Arthur Balfour"]),
 ("Norma", "John Major", ["Edward Heath", "Bonar Law", "Robert Peel"]),
 ("Samantha", "David Cameron", ["Edward Heath", "Arthur Balfour", "Lord Salisbury"]),
 ("Philip", "Theresa May", ["Edward Heath", "Ramsay MacDonald", "Robert Peel"]),
 ("Carrie", "Boris Johnson", ["Edward Heath", "Benjamin Disraeli", "Herbert Asquith"]),
 ("Akshata", "Rishi Sunak", ["Edward Heath", "Bonar Law", "William Gladstone"]),
 ("Victoria", "Keir Starmer", ["Edward Heath", "Robert Peel", "Lord Salisbury"]),
 ("Sarah", "Gordon Brown", ["Edward Heath", "Ramsay MacDonald", "Arthur Balfour"]),
 ("Hugh", "Liz Truss", ["Edward Heath", "Benjamin Disraeli", "Bonar Law"]),
 ("Mary, a poet", "Harold Wilson", ["Edward Heath", "Herbert Asquith", "William Gladstone"]),
 ("Clementine", "Winston Churchill", ["Lord Salisbury", "Herbert Asquith", "Arthur Balfour"]),
 ("Audrey", "James Callaghan", ["Edward Heath", "Ramsay MacDonald", "Robert Peel"]),
 ("Lady Dorothy", "Harold Macmillan", ["Arthur Balfour", "Lord Salisbury", "Bonar Law"]),
 ("Clarissa, Churchill's niece", "Anthony Eden", ["Herbert Asquith", "Arthur Balfour", "Ramsay MacDonald"]),
 ("Violet", "Clement Attlee", ["Ramsay MacDonald", "Bonar Law", "Herbert Asquith"]),
 ("Elizabeth", "Alec Douglas-Home", ["Edward Heath", "Lord Salisbury", "Arthur Balfour"]),
 ("Dame Margaret", "David Lloyd George", ["Herbert Asquith", "William Gladstone", "Benjamin Disraeli"]),
 ("Lucy", "Stanley Baldwin", ["Bonar Law", "Ramsay MacDonald", "Herbert Asquith"]),
 ("Anne", "Neville Chamberlain", ["Bonar Law", "Ramsay MacDonald", "Arthur Balfour"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-103.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
