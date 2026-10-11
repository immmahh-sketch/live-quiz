# Bank session 11 Oct 2026: 10 more Categorise questions -> bank/sort-15.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Music", ["The Beatles", "The Rolling Stones", "albums"], "medium", "A Beatles album or a Rolling Stones album?", "Beatles", "Rolling Stones", ["Revolver", "Abbey Road", "Rubber Soul", "Help!"], ["Sticky Fingers", "Exile on Main St.", "Let It Bleed", "Beggars Banquet"])
s("Books", ["Agatha Christie", "Sherlock Holmes"], "medium", "An Agatha Christie novel or a Sherlock Holmes story?", "Agatha Christie", "Sherlock Holmes", ["Death on the Nile", "The ABC Murders", "Evil Under the Sun", "Murder on the Orient Express"], ["The Speckled Band", "A Study in Scarlet", "The Sign of Four", "The Red-Headed League"])
s("Science", ["elements", "chemistry"], "medium", "A noble gas or a metal?", "Noble gas", "Metal", ["Neon", "Argon", "Krypton", "Xenon"], ["Sodium", "Copper", "Zinc", "Tin"])
s("History", ["US presidents", "Prime Ministers"], "medium", "A US President or a British Prime Minister?", "US President", "UK Prime Minister", ["Truman", "Eisenhower", "Nixon", "Carter"], ["Attlee", "Eden", "Macmillan", "Callaghan"])
s("Food and drink", ["sauces", "French food", "Italian food"], "medium", "A French sauce or an Italian sauce?", "French", "Italian", ["Béarnaise", "Hollandaise", "Béchamel", "Velouté"], ["Pesto", "Carbonara", "Arrabbiata", "Puttanesca"])
s("Art", ["colours"], "easy", "A shade of red or a shade of blue?", "Red", "Blue", ["Crimson", "Scarlet", "Maroon", "Vermilion"], ["Navy", "Cobalt", "Azure", "Cerulean"])
s("UK geography", ["counties", "England", "Wales"], "medium", "An English county or a Welsh county?", "England", "Wales", ["Shropshire", "Herefordshire", "Cheshire", "Gloucestershire"], ["Powys", "Gwynedd", "Pembrokeshire", "Ceredigion"])
s("Animals", ["Africa", "South America", "wildlife"], "easy", "An animal from Africa or from South America?", "Africa", "South America", ["Lion", "Zebra", "Giraffe", "Hippo"], ["Llama", "Jaguar", "Sloth", "Capybara"])
s("Film", ["Disney", "princesses", "villains"], "easy", "A Disney princess or a Disney villain?", "Princess", "Villain", ["Ariel", "Belle", "Mulan", "Jasmine"], ["Ursula", "Gaston", "Jafar", "Cruella"])
s("World geography", ["Germany", "Austria", "cities"], "medium", "A city in Germany or in Austria?", "Germany", "Austria", ["Munich", "Hamburg", "Cologne", "Dresden"], ["Vienna", "Salzburg", "Innsbruck", "Graz"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-15.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
