# Bank session 10 Oct 2026 (tenth pass): 1-2 more Match questions for the 8 topics with only 5 or 6 live.
# Writes bank/topics/<slug>__m11.json; import each with FILE=<slug>__m11 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})


m("brighton", "medium", "Match each Brighton landmark to what it is",
  ("Royal Pavilion", "The Prince Regent's Indian-style palace"), ("Volk's Electric Railway", "The oldest electric railway still running"), ("The Lanes", "Narrow alleys full of jewellers"), ("i360", "A moving observation tower"))
m("brighton", "hard", "Match each Brighton & Hove Albion home to its era",
  ("Goldstone Ground", "1902-1997"), ("Priestfield, Gillingham", "1997-1999"), ("Withdean Stadium", "1999-2011"), ("Amex Stadium", "2011 onwards"))

m("connections", "easy", "Match each comedian to their double-act partner",
  ("Eric Morecambe", "Ernie Wise"), ("Ronnie Barker", "Ronnie Corbett"), ("Jennifer Saunders", "Dawn French"), ("Peter Cook", "Dudley Moore"))
m("connections", "medium", "Match each group to the member who's missing",
  ("Sporty, Scary, Baby, Ginger", "Posh"), ("John, Paul, George", "Ringo"), ("Athos, Porthos, d'Artagnan", "Aramis"), ("Dopey, Grumpy, Happy, Sleepy, Sneezy, Bashful", "Doc"))

m("covid-19", "easy", "Match each Covid phrase to what it meant",
  ("Eat Out to Help Out", "Half-price meals in August 2020"), ("Rule of six", "A limit on social gatherings"), ("Support bubble", "A single-adult home teaming up with one other"), ("Furlough", "The government paying wages of staff sent home"))
m("covid-19", "medium", "Match each date to its Covid moment",
  ("23 March 2020", "The first national lockdown is announced"), ("8 December 2020", "The first vaccine jab, for Margaret Keenan"), ("19 July 2021", "'Freedom Day' in England"), ("24 February 2022", "England's last legal Covid rules end"))

m("no-such-thing-as-a-fish", "medium", "Match each animal to its surprising fact",
  ("Sea otter", "Holds hands while it sleeps"), ("Cow", "Has a best friend"), ("Snail", "Can sleep for three years"), ("Flamingo", "Turns pink from its food"))
m("no-such-thing-as-a-fish", "medium", "Match each product to what it was first invented for",
  ("Bubble wrap", "Textured wallpaper"), ("Play-Doh", "Cleaning soot off wallpaper"), ("Viagra", "Treating chest pain"), ("Coca-Cola", "A medicinal tonic"))

m("ripleys-believe-it-or-not", "hard", "Match each record-breaker to their record",
  ("Robert Wadlow", "Tallest man ever recorded"), ("Sultan Kösen", "Tallest man alive"), ("Jeanne Calment", "Oldest person ever, at 122"), ("Shridhar Chillal", "Longest fingernails on one hand"))
m("ripleys-believe-it-or-not", "medium", "Match each odd museum to its country",
  ("Museum of Broken Relationships", "Croatia"), ("Cumberland Pencil Museum", "England"), ("The Sewer Museum", "France"), ("The Mütter Museum of medical oddities", "USA"))

m("music-lyrics", "medium", "Match each lyric to its song",
  ("Just a small-town girl", "Don't Stop Believin'"), ("I got my first real six-string", "Summer of '69"), ("There's a fire starting in my heart", "Rolling in the Deep"), ("I've paid my dues", "We Are the Champions"))

m("handmaids-tale", "medium", "Match each Gilead phrase to its meaning",
  ("Blessed be the fruit", "A greeting, answered 'May the Lord open'"), ("Under His Eye", "A farewell: God is watching"), ("Nolite te bastardes carborundorum", "Don't let the bastards grind you down"), ("Praise be", "An all-purpose 'thank God'"))
m("handmaids-tale", "medium", "Match each man in 'The Handmaid's Tale' to the actor",
  ("Commander Fred Waterford", "Joseph Fiennes"), ("Commander Joseph Lawrence", "Bradley Whitford"), ("Nick Blaine", "Max Minghella"), ("Luke Bankole", "O-T Fagbenle"))

m("breaking-bad", "medium", "Match each 'Breaking Bad' character to how they die",
  ("Gus Fring", "A bomb in a nursing home"), ("Jane Margolis", "Choking in her sleep"), ("Lydia Rodarte-Quayle", "Ricin in her stevia"), ("Walter White", "Hit by his own rigged machine gun"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, qs in OUT.items():
    json.dump(qs, open(os.path.join(here, '..', 'topics', slug + '__m11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(len(q) for q in OUT.values()), 'match questions written for', len(OUT), 'topics')
