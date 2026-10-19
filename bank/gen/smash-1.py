# Bank session 19 Oct 2026: 16 Answer Smash questions written by hand -> bank/smash-1.json (the first hand-written ones; the
# rest of the stock came from the topic writer). Picture answers are faces from today's races and sessions; the clue answer
# starts with the last letters of the name (at least two letters overlap, the server's rule). Checked against every picture
# answer already in the live bank; clue answers the bank had already used (Landlord, Mango, Ryanair...) were swapped for fresh ones. A face with no Wikipedia photo is dropped by the server at import.
import json, os, re
OUT = []
def sm(picture, clue_answer, text, diff="medium", cat="Wordplay"):
    la = re.sub(r'[^a-z0-9]', '', picture.lower()); lb = re.sub(r'[^a-z0-9]', '', clue_answer.lower())
    n = next((k for k in range(min(len(la), len(lb)) - 1, 0, -1) if la[-k:] == lb[:k]), 0)
    assert n >= 2, (picture, clue_answer)
    OUT.append({"type": "smash", "text": text, "pictureAnswer": picture, "clueAnswer": clue_answer, "category": cat, "tags": ["Answer Smash"], "difficulty": diff})

sm("Jools Holland", "Landlubber", "Sailor's word for someone who isn't used to the sea")
sm("Ian McShane", "Anecdote", "Short, amusing story about something that really happened")
sm("Paul Merton", "Tony Robinson", "Baldrick actor who fronted Time Team")
sm("Kevin Whately", "Lyrics", "The words of a song")
sm("Sandi Toksvig", "Vigilante", "Someone who takes the law into their own hands", "hard")
sm("Ian Hislop", "Lopsided", "Leaning to one side; uneven")
sm("Bob Mortimer", "Merseyside", "County that includes Liverpool", "easy")
sm("Noel Fielding", "Dinghy", "Small inflatable boat", "easy")
sm("John Nettles", "Lester Piggott", "Jockey who won the Derby a record nine times", "hard")
sm("Josh Widdicombe", "Bethlehem", "Town where Jesus was born, according to the Gospels", "hard")
sm("Adam Hills", "Hillsborough", "Sheffield Wednesday's home ground")
sm("Nick Berry", "Ryan Giggs", "Welsh winger who won a record 13 Premier League titles")
sm("Phill Jupitus", "Tuscany", "Italian region around Florence and Siena")
sm("Matt Dawson", "Sons and Lovers", "D. H. Lawrence novel about Paul Morel and his mother", "hard")
sm("Kerry Godliman", "Manuel", "Fawlty Towers waiter from Barcelona", "easy")
sm("Bill Bailey", "Baileys", "Irish cream liqueur, often drunk at Christmas", "easy")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'smash-1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'smash questions written')
