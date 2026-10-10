# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-39.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Songs by Ed Sheeran", "Music", "easy", ["Ed Sheeran", "songs"],
 ["Shape of You", "Perfect", "Thinking Out Loud", "Castle on the Hill", "The A Team", "Galway Girl", "Bad Habits", "Shivers", "Photograph", "Sing", "Lego House", "Don't", "Happier", "Give Me Love", "Eyes Closed"],
 ["Someone You Loved", "Let Her Go", "Hold Back the River", "Budapest", "Say You Won't Let Go"])
board("Songs by U2", "Music", "medium", ["U2", "songs"],
 ["With or Without You", "One", "Beautiful Day", "Vertigo", "Pride (In the Name of Love)", "Sunday Bloody Sunday", "I Still Haven't Found What I'm Looking For", "Where the Streets Have No Name", "Desire", "Elevation", "Mysterious Ways", "The Sweetest Thing", "Stay (Faraway, So Close!)", "New Year's Day", "Even Better Than the Real Thing"],
 ["Don't You (Forget About Me)", "Alive and Kicking", "Chasing Cars", "Linger", "Zombie"])
board("Songs by Sam Fender", "Music", "medium", ["Sam Fender", "North East", "songs"],
 ["Hypersonic Missiles", "Seventeen Going Under", "Will We Talk?", "Dead Boys", "Play God", "The Borders", "Spit of You", "Getting Started", "Get You Down", "Howdon Aldi Death Queue", "Leave Fast", "People Watching", "Arm's Length", "Wild Long Lie", "Remember My Name"],
 ["Canter", "Before You Go", "How Beautiful Life Can Be", "Not Nineteen Forever", "Charlemagne"])
board("Songs by Amy Winehouse", "Music", "easy", ["Amy Winehouse", "songs"],
 ["Rehab", "Back to Black", "Valerie", "You Know I'm No Good", "Tears Dry on Their Own", "Love Is a Losing Game", "Stronger Than Me", "In My Bed", "Take the Box", "Body and Soul", "Our Day Will Come", "Me & Mr Jones", "Wake Up Alone", "Just Friends", "Cherry"],
 ["Mercy", "Warwick Avenue", "Chasing Pavements", "Hometown Glory", "Foundations"])
board("Songs by Depeche Mode", "Music", "medium", ["Depeche Mode", "synth-pop", "songs"],
 ["Just Can't Get Enough", "Enjoy the Silence", "Personal Jesus", "People Are People", "Everything Counts", "Master and Servant", "Policy of Truth", "Never Let Me Down Again", "Strangelove", "Walking in My Shoes", "I Feel You", "Precious", "See You", "Shake the Disease", "Barrel of a Gun"],
 ["Blue Monday", "Tainted Love", "Don't You Want Me", "Enola Gay", "Vienna"])
board("Songs by Katy Perry", "Music", "easy", ["Katy Perry", "songs"],
 ["I Kissed a Girl", "Hot n Cold", "Firework", "Roar", "Teenage Dream", "California Gurls", "Last Friday Night (T.G.I.F.)", "Dark Horse", "E.T.", "Part of Me", "Wide Awake", "Unconditionally", "Waking Up in Vegas", "Chained to the Rhythm", "Bon Appétit"],
 ["Since U Been Gone", "TiK ToK", "Domino", "Price Tag", "Born This Way"])
board("Songs by Bruce Springsteen", "Music", "medium", ["Bruce Springsteen", "songs"],
 ["Born in the U.S.A.", "Born to Run", "Dancing in the Dark", "Thunder Road", "The River", "Hungry Heart", "Glory Days", "I'm on Fire", "Streets of Philadelphia", "Badlands", "Atlantic City", "Tougher Than the Rest", "Brilliant Disguise", "Cover Me", "Secret Garden"],
 ["Jack & Diane", "Small Town", "Summer of '69", "Night Moves", "American Girl"])
board("Songs by the Who", "Music", "medium", ["The Who", "1960s", "songs"],
 ["My Generation", "Pinball Wizard", "Baba O'Riley", "Won't Get Fooled Again", "Substitute", "I Can See for Miles", "Who Are You", "Happy Jack", "I'm a Boy", "Pictures of Lily", "Magic Bus", "I Can't Explain", "Behind Blue Eyes", "Squeeze Box", "You Better You Bet"],
 ["All Day and All of the Night", "Waterloo Sunset", "Paint It Black", "(I Can't Get No) Satisfaction", "Whole Lotta Love"])
board("Songs by Radiohead", "Music", "medium", ["Radiohead", "songs"],
 ["Creep", "Karma Police", "No Surprises", "Paranoid Android", "High and Dry", "Fake Plastic Trees", "Street Spirit (Fade Out)", "Just", "There There", "Everything in Its Right Place", "Idioteque", "Pyramid Song", "Lucky", "Nude", "Daydreaming"],
 ["Bitter Sweet Symphony", "The Drugs Don't Work", "Yellow", "Why Does It Always Rain on Me?", "Teardrop"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-39.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
