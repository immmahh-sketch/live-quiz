# Bank session 10 Oct 2026: 14 more Categorise questions -> bank/sort-10.json. Two groups, four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Football", ["Scotland", "Wales", "clubs"], "medium", "A Scottish football club or a Welsh one?", "Scottish", "Welsh", ["Hearts", "Hibernian", "Motherwell", "Kilmarnock"], ["Wrexham", "Swansea City", "Cardiff City", "Newport County"])
s("Animals", ["dog breeds", "Germany", "France"], "hard", "A dog breed from Germany or from France?", "Germany", "France", ["Dachshund", "Rottweiler", "Dobermann", "Schnauzer"], ["Bichon Frisé", "Basset Hound", "Dogue de Bordeaux", "Papillon"])
s("Film", ["villains", "James Bond", "Batman"], "easy", "A Bond villain or a Batman villain?", "Bond", "Batman", ["Blofeld", "Goldfinger", "Oddjob", "Le Chiffre"], ["The Joker", "The Penguin", "The Riddler", "Bane"])
s("Words and language", ["Greek", "Latin", "word origins"], "hard", "An English word from ancient Greek or from Latin?", "Greek", "Latin", ["Telephone", "Democracy", "Biology", "Photograph"], ["Agenda", "Video", "Data", "Status"])
s("Food and drink", ["baking", "cakes", "bread"], "easy", "A cake or a bread?", "Cake", "Bread", ["Victoria sponge", "Battenberg", "Madeira", "Black Forest gateau"], ["Focaccia", "Ciabatta", "Sourdough", "Soda bread"])
s("Sport", ["American sport", "NFL", "NBA"], "medium", "An NFL team or an NBA team?", "NFL", "NBA", ["Dallas Cowboys", "Green Bay Packers", "New England Patriots", "Kansas City Chiefs"], ["Los Angeles Lakers", "Chicago Bulls", "Boston Celtics", "Golden State Warriors"])
s("Sport", ["Formula One", "circuits"], "medium", "A Formula One circuit in Europe or elsewhere?", "Europe", "Elsewhere", ["Silverstone", "Monza", "Spa-Francorchamps", "Monaco"], ["Suzuka", "Interlagos", "Albert Park", "Marina Bay"])
s("Food and drink", ["chocolate", "Mars", "Nestlé"], "medium", "A Mars bar brand or a Nestlé one?", "Mars", "Nestlé", ["Snickers", "Twix", "Bounty", "Milky Way"], ["KitKat", "Aero", "Yorkie", "Milkybar"])
s("Music", ["Elvis Presley", "Cliff Richard"], "easy", "An Elvis song or a Cliff Richard song?", "Elvis", "Cliff Richard", ["Hound Dog", "Jailhouse Rock", "Suspicious Minds", "Return to Sender"], ["Living Doll", "Summer Holiday", "Congratulations", "Mistletoe and Wine"])
s("Theatre", ["Gilbert and Sullivan", "Andrew Lloyd Webber", "musicals"], "medium", "Gilbert and Sullivan or Andrew Lloyd Webber?", "Gilbert and Sullivan", "Lloyd Webber", ["The Mikado", "HMS Pinafore", "The Pirates of Penzance", "The Gondoliers"], ["Cats", "Evita", "Starlight Express", "Sunset Boulevard"])
s("TV", ["Doctor Who", "Blue Peter"], "medium", "A Doctor Who companion or a Blue Peter presenter?", "Doctor Who companion", "Blue Peter presenter", ["Rose Tyler", "Donna Noble", "Amy Pond", "Clara Oswald"], ["Valerie Singleton", "John Noakes", "Konnie Huq", "Matt Baker"])
s("World geography", ["islands", "Mediterranean", "Caribbean"], "easy", "An island in the Mediterranean or the Caribbean?", "Mediterranean", "Caribbean", ["Malta", "Crete", "Sardinia", "Corsica"], ["Barbados", "Jamaica", "Antigua", "St Lucia"])
s("Games and toys", ["Pokémon", "Digimon"], "hard", "A Pokémon or a Digimon?", "Pokémon", "Digimon", ["Pikachu", "Charizard", "Jigglypuff", "Snorlax"], ["Agumon", "Gabumon", "Patamon", "Tentomon"])
s("TV", ["Gladiators", "wrestling"], "medium", "A 1990s 'Gladiator' or a WWE wrestler?", "Gladiator", "WWE wrestler", ["Wolf", "Jet", "Lightning", "Shadow"], ["The Undertaker", "Hulk Hogan", "The Rock", "Stone Cold Steve Austin"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
