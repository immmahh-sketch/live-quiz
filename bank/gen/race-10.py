# Bank session 10 Oct 2026: 4 more general races -> bank/race-10.json. 20 rows each, target 10; wrong options are
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

race("name the famous duck", "Film and TV", "medium", ["ducks", "characters"], [
 ("Mickey's short-tempered friend in a sailor suit", "Donald", ["Goofy", "Pluto", "Gladstone"]), ("Bugs Bunny's lisping rival", "Daffy", ["Porky", "Elmer", "Sylvester"]),
 ("Donald's girlfriend", "Daisy", ["Minnie", "Clarabelle", "Della"]), ("The richest duck in the world", "Scrooge McDuck", ["Flintheart Glomgold", "Gladstone Gander", "Gyro Gearloose"]),
 ("Beatrix Potter's duck in a bonnet", "Jemima Puddle-Duck", ["Mrs. Tiggy-Winkle", "Mrs. Tittlemouse", "Pigling Bland"]), ("Marvel's cigar-chomping duck", "Howard the Duck", ["Rocket", "Groot", "Squirrel Girl"]),
 ("The vegetarian vampire duck", "Count Duckula", ["Igor", "Nanny", "Dracula"]), ("The Pokémon with a permanent headache", "Psyduck", ["Golduck", "Squirtle", "Pikachu"]),
 ("'Let's get dangerous!' — the caped duck", "Darkwing Duck", ["Negaduck", "Gosalyn", "Bushroot"]), ("Donald's professor uncle", "Ludwig Von Drake", ["Gyro Gearloose", "Gladstone Gander", "Gus Goose"]),
 ("Keith Harris's green duck who wished he could fly", "Orville", ["Cuddles", "Lord Charles", "Emu"]), ("The CBBC duck with a quiff", "Edd the Duck", ["Gordon the Gopher", "Otis the Aardvark", "Zig"]),
 ("Tiny Toons' green duck", "Plucky Duck", ["Buster Bunny", "Hamton", "Babs"]), ("The duck in Babe who wants to be a rooster", "Ferdinand", ["Rex", "Fly", "Maa"]),
 ("Scrooge's crash-prone pilot", "Launchpad McQuack", ["Fenton Crackshell", "Duckworth", "Gyro Gearloose"]), ("Scrooge's adventurous granddaughter-figure in DuckTales", "Webby Vanderquack", ["Lena", "Della", "Mrs. Beakley"]),
 ("Donald's nephew in red", "Huey", ["Dewey", "Louie", "Della"]), ("Thomas & Friends' Great Western tank engine", "Duck", ["Oliver", "Henry", "Toby"]),
 ("Chicken Little's best friend", "Abby Mallard", ["Runt of the Litter", "Fish Out of Water", "Foxy Loxy"]), ("Donald's gloomy, unlucky cousin", "Fethry Duck", ["Gladstone Gander", "Gus Goose", "Della"])])

race("which sport is this prize or trophy from?", "Sport", "medium", ["trophies", "sports"], [
 ("The Ashes urn", "Cricket", ["Bowls", "Croquet", "Hockey"]), ("The Ryder Cup", "Golf", ["Bowls", "Croquet", "Polo"]),
 ("The Davis Cup", "Tennis", ["Squash", "Croquet", "Volleyball"]), ("The Stanley Cup", "Ice hockey", ["Lacrosse", "Curling", "Hockey"]),
 ("The Webb Ellis Cup", "Rugby union", ["Australian rules", "Football", "Polo"]), ("The Yellow Jersey", "Cycling", ["Athletics", "Triathlon", "Skiing"]),
 ("The Sam Maguire Cup", "Gaelic football", ["Camogie", "Australian rules", "Handball"]), ("The Liam MacCarthy Cup", "Hurling", ["Camogie", "Lacrosse", "Handball"]),
 ("The Vince Lombardi Trophy", "American football", ["Australian rules", "Lacrosse", "Volleyball"]), ("The Larry O'Brien Trophy", "Basketball", ["Volleyball", "Netball", "Handball"]),
 ("The Commissioner's Trophy (World Series)", "Baseball", ["Softball", "Rounders", "Lacrosse"]), ("The Sid Waddell Trophy", "Darts", ["Snooker", "Bowls", "Pool"]),
 ("The America's Cup", "Sailing", ["Powerboating", "Windsurfing", "Canoeing"]), ("Doggett's Coat and Badge", "Rowing", ["Canoeing", "Swimming", "Kayaking"]),
 ("The Uber Cup", "Badminton", ["Squash", "Volleyball", "Netball"]), ("The Swaythling Cup", "Table tennis", ["Squash", "Snooker", "Bowls"]),
 ("The Lonsdale Belt", "Boxing", ["Wrestling", "Judo", "Fencing"]), ("The Melbourne Cup", "Horse racing", ["Greyhound racing", "Polo", "Show jumping"]),
 ("The Grey Cup", "Canadian football", ["Australian rules", "Lacrosse", "Curling"]), ("The Borg-Warner Trophy (Indy 500)", "Motor racing", ["Speedway", "Motocross", "Powerboating"])])

race("which country is this brand from?", "Brands", "medium", ["brands", "countries"], [
 ("IKEA", "Sweden", ["Norway", "Iceland", "Austria"]), ("Lego", "Denmark", ["Norway", "Iceland", "the USA"]),
 ("Nokia", "Finland", ["Norway", "Estonia", "Iceland"]), ("Samsung", "South Korea", ["Taiwan", "Vietnam", "Singapore"]),
 ("Zara", "Spain", ["Portugal", "Argentina", "Greece"]), ("Heineken", "the Netherlands", ["Austria", "Luxembourg", "Poland"]),
 ("Rolex", "Switzerland", ["Austria", "Luxembourg", "Liechtenstein"]), ("Nintendo", "Japan", ["Taiwan", "Singapore", "Thailand"]),
 ("Adidas", "Germany", ["Austria", "the USA", "Poland"]), ("Ferrari", "Italy", ["Portugal", "Greece", "Austria"]),
 ("Guinness", "Ireland", ["Scotland", "Wales", "Iceland"]), ("Tim Hortons", "Canada", ["the USA", "New Zealand", "Iceland"]),
 ("Vegemite", "Australia", ["New Zealand", "South Africa", "the USA"]), ("Havaianas", "Brazil", ["Argentina", "Portugal", "Chile"]),
 ("Corona", "Mexico", ["Argentina", "the USA", "Chile"]), ("Tata", "India", ["Pakistan", "Sri Lanka", "Bangladesh"]),
 ("Huawei", "China", ["Taiwan", "Singapore", "Vietnam"]), ("Škoda", "Czechia", ["Slovakia", "Poland", "Hungary"]),
 ("Lacoste", "France", ["Portugal", "Luxembourg", "Greece"]), ("Stella Artois", "Belgium", ["Luxembourg", "Austria", "Poland"])])

race("what's the Japanese word?", "Words and language", "hard", ["Japanese", "languages"], [
 ("Thank you", "Arigatō", ["Kanpai", "Sumimasen", "Gomen"]), ("Goodbye", "Sayōnara", ["Oyasumi", "Konbanwa", "Dōzo"]),
 ("Yes", "Hai", ["Ne", "Sō", "Ano"]), ("No", "Iie", ["Ano", "Ne", "Etto"]), ("Water", "Mizu", ["Mimi", "Mochi", "Mugi"]),
 ("Cat", "Neko", ["Nezumi", "Tori", "Kitsune"]), ("Dog", "Inu", ["Ushi", "Uma", "Kitsune"]), ("Mountain", "Yama", ["Kaze", "Kumo", "Shima"]),
 ("River", "Kawa", ["Kaze", "Kumo", "Mizuumi"]), ("Tree", "Ki", ["Te", "Me", "Hi"]), ("Book", "Hon", ["Kami", "Ji", "E"]),
 ("Car", "Kuruma", ["Densha", "Fune", "Hikōki"]), ("Friend", "Tomodachi", ["Sensei", "Kazoku", "Kodomo"]), ("Moon", "Tsuki", ["Hoshi", "Taiyō", "Kumo"]),
 ("Flower", "Hana", ["Ha", "Kusa", "Mori"]), ("Sea", "Umi", ["Shima", "Mizuumi", "Hama"]), ("Rain", "Ame", ["Kaze", "Kumo", "Kaminari"]),
 ("Snow", "Yuki", ["Kōri", "Fuyu", "Shimo"]), ("Sky", "Sora", ["Kumo", "Hoshi", "Taiyō"]), ("Good morning", "Ohayō", ["Konbanwa", "Oyasumi", "Konnichiwa"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
