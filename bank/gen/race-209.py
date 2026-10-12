# Bank session 12 Oct 2026: 1 more general race -> bank/race-209.json (jazz words). Checked against the orchestra, singing
# and gig races for repeated answers.
# 20 rows each, target 10; wrong options are the same kind of thing, never another row's right answer, and never also right for that row.
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

race("what's this jazz word?", "Music", "medium", ["jazz", "music", "words"], [
 ("Singing nonsense syllables like 'doo-be-doo'", "Scat", ["Rap", "Yodel", "Beatbox"]),
 ("Making the music up on the spot", "Improvisation", ["Composition", "Arrangement", "Transcription"]),
 ("The bouncy big-band style of the 1930s and '40s", "Swing", ["Grunge", "Disco", "Ska"]),
 ("Fast, tricky jazz of Charlie Parker and Dizzy Gillespie", "Bebop", ["Hip hop", "Doo-wop", "Skiffle"]),
 ("A large jazz orchestra with sections of brass and saxes", "Big band", ["Boy band", "Brass band", "Skiffle group"]),
 ("The early piano style of Scott Joplin", "Ragtime", ["Rock and roll", "Calypso", "Bossa nova"]),
 ("The US city seen as the birthplace of jazz", "New Orleans", ["Nashville", "Memphis", "Detroit"]),
 ("An informal get-together where musicians play along", "Jam session", ["Soundcheck", "Rehearsal", "Recital"]),
 ("A short, catchy repeated phrase", "Riff", ["Chorus", "Bridge", "Verse"]),
 ("Stressing the off-beats, the heartbeat of jazz", "Syncopation", ["Crescendo", "Legato", "Staccato"]),
 ("Satchmo, the gravel-voiced trumpeter of 'What a Wonderful World'", "Louis Armstrong", ["Dizzy Gillespie", "Chet Baker", "Wynton Marsalis"]),
 ("The singer known as the 'First Lady of Song'", "Ella Fitzgerald", ["Nina Simone", "Sarah Vaughan", "Etta James"]),
 ("The singer of 'Strange Fruit', known as Lady Day", "Billie Holiday", ["Nina Simone", "Sarah Vaughan", "Etta James"]),
 ("The trumpeter behind the album 'Kind of Blue'", "Miles Davis", ["Dizzy Gillespie", "Chet Baker", "Wynton Marsalis"]),
 ("The famous London jazz club on Frith Street", "Ronnie Scott's", ["The Cavern", "The Marquee", "The 100 Club"]),
 ("A classic, much-played tune like 'Autumn Leaves'", "Standard", ["Anthem", "Single", "B-side"]),
 ("Duke Ellington's instrument", "Piano", ["Trumpet", "Trombone", "Vibraphone"]),
 ("Benny Goodman, the 'King of Swing', played this", "Clarinet", ["Saxophone", "Oboe", "Flute"]),
 ("The sad, 12-bar style that fed into jazz", "Blues", ["Soul", "Funk", "Gospel"]),
 ("The laid-back West Coast style, the opposite of 'hot'", "Cool jazz", ["Acid jazz", "Free jazz", "Smooth jazz"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-209.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
