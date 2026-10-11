# Bank session 11 Oct 2026: 7 more Put in order questions -> bank/order-16.json (talent show winners, presenters, Speakers and sporting winners).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
o("TV", ["The X Factor", "talent shows"], "medium", "Put these X Factor winners in order, earliest first", ["Steve Brookstein", "Shayne Ward", "Leona Lewis", "Leon Jackson", "Alexandra Burke", "Joe McElderry", "Matt Cardle"], "earliest first")
o("TV", ["Britain's Got Talent", "talent shows"], "medium", "Put these Britain's Got Talent winners in order, earliest first", ["Paul Potts", "George Sampson", "Diversity", "Spelbound", "Jai McDowall", "Ashleigh and Pudsey", "Attraction"], "earliest first")
o("TV", ["Love Island", "reality TV"], "hard", "Put these Love Island winning couples in order, earliest first", ["Jess and Max", "Cara and Nathan", "Amber and Kem", "Dani and Jack", "Amber and Greg", "Millie and Liam", "Ekin-Su and Davide"], "earliest first")
o("Football", ["Match of the Day", "presenters"], "medium", "Put these Match of the Day presenters in the order they took over, earliest first", ["Kenneth Wolstenholme", "David Coleman", "Jimmy Hill", "Des Lynam", "Gary Lineker"], "earliest first")
o("Politics", ["Speaker", "House of Commons"], "hard", "Put these Speakers of the House of Commons in order, earliest first", ["George Thomas", "Bernard Weatherill", "Betty Boothroyd", "Michael Martin", "John Bercow", "Lindsay Hoyle"], "earliest first")
o("Sport", ["Grand National", "horse racing"], "hard", "Put these Grand National winners in order of their first win, earliest first", ["Foinavon", "Red Rum", "Aldaniti", "Party Politics", "Tiger Roll", "Minella Times"], "earliest first")
o("Football", ["European Cup", "Champions League", "English clubs"], "medium", "Put these English clubs in order of their first European Cup or Champions League win, earliest first", ["Manchester United", "Liverpool", "Nottingham Forest", "Aston Villa", "Chelsea", "Manchester City"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
