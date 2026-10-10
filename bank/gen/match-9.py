# Bank session 10 Oct 2026 (eighth pass): 2 more Match questions for 12 more topics that had 5 live. A Hogwarts-founders
# match was swapped for fantasy creatures: the bank already had it.
# Writes bank/topics/<slug>__m9.json; import each with FILE=<slug>__m9 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})

m("bridgerton", "medium", "Match each Bridgerton sibling to the one they fall for",
  ("Daphne", "Simon Basset"), ("Anthony", "Kate Sharma"), ("Colin", "Penelope Featherington"), ("Benedict", "Sophie Baek"))
m("bridgerton", "medium", "Match each Bridgerton sibling to their place in the family",
  ("Anthony", "Eldest"), ("Benedict", "Second"), ("Colin", "Third"), ("Daphne", "Fourth"))

m("crime-dramas", "easy", "Match each detective to their sidekick",
  ("Inspector Morse", "Lewis"), ("Sherlock Holmes", "Dr Watson"), ("Hercule Poirot", "Captain Hastings"), ("Dalziel", "Pascoe"))
m("crime-dramas", "medium", "Match each crime drama to its leading lady",
  ("Prime Suspect", "Helen Mirren"), ("Happy Valley", "Sarah Lancashire"), ("Vera", "Brenda Blethyn"), ("The Fall", "Gillian Anderson"))

m("dc-batman", "easy", "Match each actor to the Batman villain they played",
  ("Heath Ledger", "The Joker"), ("Tom Hardy", "Bane"), ("Danny DeVito", "The Penguin"), ("Jim Carrey", "The Riddler"))
m("dc-batman", "easy", "Match each hero to their secret identity",
  ("Superman", "Clark Kent"), ("Batman", "Bruce Wayne"), ("Wonder Woman", "Diana Prince"), ("The Flash", "Barry Allen"))

m("easter-spring", "medium", "Match each Easter food to the story behind it",
  ("Hot cross buns", "The cross of Good Friday"), ("Simnel cake", "Eleven marzipan balls for the apostles"), ("Easter eggs", "New life"), ("Pancakes", "Using up rich food before Lent"))
m("easter-spring", "medium", "Match each spring baby animal to its parent",
  ("Lamb", "Sheep"), ("Kid", "Goat"), ("Leveret", "Hare"), ("Cygnet", "Swan"))

m("new-year", "easy", "Match each city to how it famously sees in the New Year",
  ("Sydney", "Fireworks over the Harbour Bridge"), ("New York", "The ball drop in Times Square"), ("London", "Big Ben's chimes and fireworks on the Thames"), ("Edinburgh", "A Hogmanay street party"))
m("new-year", "medium", "Match each New Year song to its writer or singer",
  ("Auld Lang Syne", "Robert Burns"), ("Happy New Year", "ABBA"), ("New Year's Day", "U2"), ("What Are You Doing New Year's Eve?", "Ella Fitzgerald"))

m("one-hit-wonders", "easy", "Match each one-hit wonder to its act",
  ("Macarena", "Los del Río"), ("Mambo No. 5", "Lou Bega"), ("Spirit in the Sky", "Norman Greenbaum"), ("Video Killed the Radio Star", "The Buggles"))
m("one-hit-wonders", "medium", "Match each novelty number one to its year",
  ("Shaddap You Face", "1981"), ("Mr Blobby", "1993"), ("Can We Fix It?", "2000"), ("Axel F (Crazy Frog)", "2005"))

m("oscars", "hard", "Match each film to the number of Oscars it won",
  ("Titanic", "11"), ("Slumdog Millionaire", "8"), ("Oppenheimer", "7"), ("Gladiator", "5"))
m("oscars", "medium", "Match each British actor to the film that won him Best Actor",
  ("Eddie Redmayne", "The Theory of Everything"), ("Gary Oldman", "Darkest Hour"), ("Colin Firth", "The King's Speech"), ("Daniel Day-Lewis", "Lincoln"))

m("reality-tv", "hard", "Match each I'm a Celebrity winner to their year",
  ("Kerry Katona", "2004"), ("Joe Swash", "2008"), ("Stacey Solomon", "2010"), ("Jill Scott", "2022"))
m("reality-tv", "hard", "Match each Big Brother winner to their year",
  ("Craig Phillips", "2000"), ("Brian Dowling", "2001"), ("Kate Lawler", "2002"), ("Nadia Almada", "2004"))

m("the-office", "medium", "Match each boss to their workplace",
  ("David Brent", "Wernham Hogg"), ("Michael Scott", "Dunder Mifflin"), ("Mr Burns", "Springfield Nuclear Power Plant"), ("Captain Holt", "Brooklyn's 99th Precinct"))
m("the-office", "easy", "Match each workplace sitcom to its star",
  ("Black Books", "Dylan Moran"), ("The IT Crowd", "Chris O'Dowd"), ("Phoenix Nights", "Peter Kay"), ("Open All Hours", "Ronnie Barker"))

m("valentines", "easy", "Match each love song to its singer",
  ("I Will Always Love You", "Whitney Houston"), ("Something Stupid", "Frank and Nancy Sinatra"), ("Endless Love", "Diana Ross and Lionel Richie"), ("Perfect", "Ed Sheeran"))
m("valentines", "medium", "Match each famous lover to their beloved",
  ("Romeo", "Juliet"), ("Heathcliff", "Cathy"), ("Lancelot", "Guinevere"), ("Antony", "Cleopatra"))

m("game-of-thrones", "medium", "Match each Stark child to the actor who played them",
  ("Arya", "Maisie Williams"), ("Sansa", "Sophie Turner"), ("Bran", "Isaac Hempstead Wright"), ("Robb", "Richard Madden"))
m("game-of-thrones", "hard", "Match each castle to its region of Westeros",
  ("Winterfell", "The North"), ("Casterly Rock", "The Westerlands"), ("Highgarden", "The Reach"), ("Sunspear", "Dorne"))

m("lord-of-the-rings", "easy", "Match each Lord of the Rings character to the actor",
  ("Gandalf", "Ian McKellen"), ("Frodo", "Elijah Wood"), ("Aragorn", "Viggo Mortensen"), ("Gollum", "Andy Serkis"))
m("lord-of-the-rings", "medium", "Match each fantasy creature to the book it appears in",
  ("Aslan", "The Lion, the Witch and the Wardrobe"), ("Smaug", "The Hobbit"), ("Buckbeak", "Harry Potter and the Prisoner of Azkaban"), ("Falkor", "The NeverEnding Story"))
here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__m9.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'matches in', len(OUT), 'topics:', ' '.join(OUT))
