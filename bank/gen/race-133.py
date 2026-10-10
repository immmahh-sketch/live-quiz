# Bank session 10 Oct 2026: 2 more general races -> bank/race-133.json (school words, coffee drinks). 20 rows each, target 10; wrong options are
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


race("what's this school word?", "Everyday life", "easy", ["school", "words", "nostalgia"], [
 ("Being kept behind after school as a punishment", "Detention", ["Lines", "Exclusion", "Expulsion"]),
 ("Taken first thing each morning to check who's in", "Register", ["Open day", "Year group", "Key stage"]),
 ("An older pupil given a badge and the power to keep order", "Prefect", ["Governor", "Bursar", "Caretaker"]),
 ("The top pupil, chosen to lead the prefects", "Head boy", ["Governor", "Bursar", "Deputy head"]),
 ("Where pupils buy sweets and snacks at break", "Tuck shop", ["Staff room", "Lunchbox", "Pencil case"]),
 ("Skipping school without permission", "Truanting", ["Exclusion", "Expulsion", "Lines"]),
 ("The whole school gathers in the hall for notices and a hymn", "Assembly", ["Speech day", "Open day", "Prize-giving"]),
 ("A stand-in teacher who covers when yours is off", "Supply teacher", ["Teaching assistant", "Head of year", "Deputy head"]),
 ("A week off in the middle of a term", "Half term", ["Key stage", "Year group", "Open day"]),
 ("A day when the pupils stay home while the teachers have training", "Inset day", ["Open day", "Speech day", "Field trip"]),
 ("She visited classes to check heads for lice", "Nit nurse", ["Caretaker", "Bursar", "Governor"]),
 ("The inspectors who grade schools in England", "Ofsted", ["SATs", "Key stage", "Year group"]),
 ("Sent home at the end of the year with every teacher's comments", "School report", ["Prize-giving", "Open day", "Key stage"]),
 ("Serves lunches and keeps an eye on the playground at dinnertime", "Dinner lady", ["Caretaker", "Bursar", "Teaching assistant"]),
 ("Helps children cross the road outside school with a big round sign", "Lollipop lady", ["Caretaker", "Bursar", "Governor"]),
 ("Egg-and-spoon and sack races on the field in summer", "Sports day", ["Speech day", "Open day", "Field trip"]),
 ("The teacher who takes your register and looks after your class each morning", "Form tutor", ["Bursar", "Governor", "Teaching assistant"]),
 ("A leather school bag with a flap and a shoulder strap", "Satchel", ["Pencil case", "Lunchbox", "Blazer"]),
 ("Practice exams before the real GCSEs", "Mocks", ["SATs", "Key stage", "Field trip"]),
 ("When mums and dads come in to hear how you're getting on", "Parents' evening", ["Open day", "Speech day", "Prize-giving"])])

race("which coffee is this?", "Food and drink", "medium", ["coffee", "drinks", "cafés"], [
 ("A small, strong shot forced through finely ground coffee under pressure", "Espresso", ["Red eye", "Bicerin", "Kopi luwak"]),
 ("Espresso topped up with lots of steamed milk and a thin layer of foam", "Latte", ["Bicerin", "Marocchino", "Antoccino"]),
 ("Espresso with steamed milk and a thick cap of foam, often dusted with chocolate", "Cappuccino", ["Bicerin", "Breve", "Vienna coffee"]),
 ("An Australian and New Zealand favourite: a double shot with a thin layer of velvety milk", "Flat white", ["Red eye", "Bicerin", "Vienna coffee"]),
 ("Espresso topped up with hot water, said to be named after American soldiers in Italy", "Americano", ["Red eye", "Café bombón", "Vienna coffee"]),
 ("Espresso 'stained' with just a dash of milk foam", "Macchiato", ["Bicerin", "Breve", "Café bombón"]),
 ("A latte with chocolate added", "Mocha", ["Breve", "Red eye", "Vienna coffee"]),
 ("Spanish espresso 'cut' with a roughly equal amount of warm milk", "Cortado", ["Café bombón", "Red eye", "Vienna coffee"]),
 ("A scoop of vanilla ice cream 'drowned' in a shot of espresso", "Affogato", ["Café bombón", "Vienna coffee", "Marocchino"]),
 ("Hot coffee, whiskey and sugar with cream floated on top", "Irish coffee", ["Café bombón", "Vienna coffee", "Red eye"]),
 ("A 'restricted' espresso made with less water, so it's even stronger", "Ristretto", ["Red eye", "Breve", "Café bombón"]),
 ("A 'long' espresso, pulled with more water", "Lungo", ["Red eye", "Breve", "Antoccino"]),
 ("A double shot of espresso", "Doppio", ["Red eye", "Breve", "Antoccino"]),
 ("Very fine coffee boiled in a little long-handled pot and served with the grounds still in", "Turkish coffee", ["Kopi luwak", "Vienna coffee", "Café bombón"]),
 ("French breakfast coffee: brewed coffee and hot milk half and half, often in a bowl", "Café au lait", ["Café bombón", "Vienna coffee", "Red eye"]),
 ("Frothy warm milk with chocolate on top, made for children", "Babyccino", ["Antoccino", "Breve", "Marocchino"]),
 ("Coffee with the caffeine taken out", "Decaf", ["Kopi luwak", "Red eye", "Breve"]),
 ("Grounds steeped in cold water for many hours", "Cold brew", ["Red eye", "Breve", "Kopi luwak"]),
 ("Starbucks' blended iced coffee drink, topped with whipped cream", "Frappuccino", ["Antoccino", "Marocchino", "Breve"]),
 ("The whipped coffee that went viral during the 2020 lockdown", "Dalgona coffee", ["Antoccino", "Bicerin", "Café bombón"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-133.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
