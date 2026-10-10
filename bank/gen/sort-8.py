# Bank session 10 Oct 2026: 14 more Categorise questions -> bank/sort-5.json. Two groups, four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Music", ["Beyoncé", "Rihanna"], "easy", "Beyoncé hit or Rihanna hit?", "Beyoncé", "Rihanna", ["Crazy in Love", "Halo", "Single Ladies", "Irreplaceable"], ["Umbrella", "Diamonds", "We Found Love", "Rude Boy"])
s("Football", ["Liverpool", "Everton", "Merseyside"], "medium", "Liverpool legend or Everton legend?", "Liverpool", "Everton", ["Ian Rush", "Kenny Dalglish", "Steven Gerrard", "Jamie Carragher"], ["Dixie Dean", "Neville Southall", "Tim Cahill", "Duncan Ferguson"])
s("World geography", ["Canada", "USA", "cities"], "medium", "City in Canada or the USA?", "Canada", "USA", ["Calgary", "Winnipeg", "Halifax", "Ottawa"], ["Denver", "Portland", "Boston", "Phoenix"])
s("Europe", ["Spain", "Portugal", "cities"], "medium", "City in Spain or Portugal?", "Spain", "Portugal", ["Seville", "Valencia", "Bilbao", "Granada"], ["Porto", "Faro", "Coimbra", "Braga"])
s("Europe", ["islands", "Italy", "Greece"], "easy", "Italian island or Greek island?", "Italian", "Greek", ["Sicily", "Sardinia", "Capri", "Elba"], ["Crete", "Rhodes", "Corfu", "Santorini"])
s("Europe", ["Austria", "Switzerland", "cities"], "medium", "City in Austria or Switzerland?", "Austria", "Switzerland", ["Salzburg", "Innsbruck", "Graz", "Linz"], ["Zurich", "Geneva", "Bern", "Lucerne"])
s("Europe", ["Norway", "Sweden", "cities"], "medium", "City in Norway or Sweden?", "Norway", "Sweden", ["Bergen", "Tromsø", "Stavanger", "Trondheim"], ["Gothenburg", "Malmö", "Uppsala", "Stockholm"])
s("Food and drink", ["meat"], "easy", "Comes from a cow or from a pig?", "Cow", "Pig", ["Brisket", "Silverside", "Rump steak", "Oxtail"], ["Gammon", "Crackling", "Chorizo", "Black pudding"])
s("Music", ["Beatles", "Monkees", "1960s"], "medium", "Beatles song or Monkees song?", "Beatles", "Monkees", ["Help!", "Penny Lane", "Something", "Let It Be"], ["I'm a Believer", "Daydream Believer", "Last Train to Clarksville", "Pleasant Valley Sunday"])
s("Film", ["Star Wars", "Star Trek"], "easy", "Star Wars character or Star Trek character?", "Star Wars", "Star Trek", ["Han Solo", "Lando Calrissian", "Darth Maul", "Yoda"], ["Spock", "Captain Kirk", "Uhura", "Jean-Luc Picard"])
s("UK geography", ["Wales", "Cornwall", "seaside"], "easy", "Welsh town or Cornish town?", "Wales", "Cornwall", ["Aberystwyth", "Llandudno", "Tenby", "Pwllheli"], ["Penzance", "Padstow", "St Ives", "Truro"])
s("UK geography", ["lakes", "lochs"], "easy", "Lake District lake or Scottish loch?", "Lake District", "Scotland", ["Windermere", "Coniston Water", "Ullswater", "Derwentwater"], ["Loch Lomond", "Loch Ness", "Loch Tay", "Loch Katrine"])
s("Music", ["Elvis Presley", "Buddy Holly", "1950s"], "medium", "Elvis Presley song or Buddy Holly song?", "Elvis", "Buddy Holly", ["Hound Dog", "Jailhouse Rock", "Suspicious Minds", "Return to Sender"], ["Peggy Sue", "That'll Be the Day", "Everyday", "Rave On"])
s("Film", ["Pixar", "Studio Ghibli", "animation"], "medium", "Pixar film or Studio Ghibli film?", "Pixar", "Studio Ghibli", ["Up", "Coco", "Cars", "Brave"], ["Spirited Away", "My Neighbour Totoro", "Ponyo", "Princess Mononoke"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
