# Bank session 11 Oct 2026: 3 more general races -> bank/race-158.json (orchestra, barbecue and birdwatching words). 20 rows each, target 10; wrong options are
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

race("what's this orchestra word?", "Music", "medium", ["orchestras", "classical music", "words"], [
 ("Waves a baton at the front", "Conductor", ["Soloist", "Répétiteur", "Prompter"]),
 ("The first violinist, who leads the tuning", "Leader", ["Soloist", "Répétiteur", "Prompter"]),
 ("The little stick the conductor holds", "Baton", ["Wand", "Cane", "Twig"]),
 ("Strung with horsehair and drawn across the strings", "Bow", ["Pick", "Plectrum", "Mallet"]),
 ("The raised platform the conductor stands on", "Podium", ["Pulpit", "Lectern", "Plinth"]),
 ("The full written music, with every part on the page", "Score", ["Libretto", "Synopsis", "Programme"]),
 ("What everyone does when the oboe plays an A", "Tune up", ["Bow out", "Sign off", "Wind down"]),
 ("The section with violins, violas, cellos and basses", "Strings", ["Keys", "Choir", "Continuo"]),
 ("The section with trumpets, trombones, horns and a tuba", "Brass", ["Keys", "Rhythm section", "Continuo"]),
 ("The section with flutes, oboes, clarinets and bassoons", "Woodwind", ["Keys", "Choir", "Rhythm section"]),
 ("The section with timpani, cymbals and drums", "Percussion", ["Choir", "Rhythm section", "Continuo"]),
 ("The big copper kettle drums", "Timpani", ["Bongos", "Tom-toms", "Snare drums"]),
 ("The biggest string instrument, played standing up", "Double bass", ["Cello", "Viola", "Harp"]),
 ("A piece for one soloist with the orchestra", "Concerto", ["Sonata", "Overture", "Requiem"]),
 ("A big piece for full orchestra, usually in four movements", "Symphony", ["Sonata", "Overture", "Requiem"]),
 ("One separate section of a symphony", "Movement", ["Act", "Verse", "Chapter"]),
 ("Everyone playing together, in Italian", "Tutti", ["Solo", "Staccato", "Legato"]),
 ("Plucking the strings instead of bowing", "Pizzicato", ["Vibrato", "Glissando", "Tremolo"]),
 ("The BBC's summer concert season at the Royal Albert Hall", "Proms", ["Glyndebourne", "Aldeburgh", "Edinburgh Fringe"]),
 ("Practice before the concert", "Rehearsal", ["Recital", "Matinée", "Premiere"])])

race("what's this barbecue word?", "Food and drink", "easy", ["barbecues", "summer", "words"], [
 ("The black lumps you burn on the grill", "Charcoal", ["Pumice", "Flint", "Slate"]),
 ("White cubes that help get it going", "Firelighters", ["Sugar cubes", "Stock cubes", "Ice cubes"]),
 ("For turning the sausages", "Tongs", ["Pliers", "Tweezers", "Pincers"]),
 ("The metal stick you thread meat and veg onto", "Skewer", ["Spindle", "Knitting needle", "Spike"]),
 ("A minced beef patty in a bun", "Burger", ["Panini", "Wrap", "Toastie"]),
 ("A sausage in a long bun", "Hot dog", ["Panini", "Wrap", "Sub"]),
 ("Soak the meat in this beforehand for flavour", "Marinade", ["Gravy", "Custard", "Batter"]),
 ("The red sauce squirted on everything", "Ketchup", ["Brown sauce", "Mint sauce", "Tartare sauce"]),
 ("The yellow sauce for hot dogs", "Mustard", ["Mayonnaise", "Salad cream", "Relish"]),
 ("Buttery yellow veg eaten with your hands", "Corn on the cob", ["Baby corn", "Sweet potato", "Courgette"]),
 ("The fuel tank for a gas barbecue", "Gas bottle", ["Hot-water bottle", "Milk bottle", "Message in a bottle"]),
 ("Steak cooked briefly, still red inside", "Rare", ["Medium", "Charred", "Crispy"]),
 ("Cooked right through, with no pink", "Well done", ["Medium", "Blue", "Pink"]),
 ("Shredded cabbage and carrot in mayo", "Coleslaw", ["Sauerkraut", "Piccalilli", "Chutney"]),
 ("The squeaky Cypriot cheese that grills without melting", "Halloumi", ["Feta", "Mozzarella", "Brie"]),
 ("Shish ___: chunks of meat on a stick", "Kebab", ["Korma", "Kedgeree", "Kipper"]),
 ("A canopy to keep the rain off", "Gazebo", ["Pergola", "Trellis", "Conservatory"]),
 ("The metal rack the food sits on", "Grill", ["Colander", "Sieve", "Whisk"]),
 ("Moulded blocks of charcoal", "Briquettes", ["Croquettes", "Baguettes", "Banquettes"]),
 ("A foil tray you light once and throw away", "Disposable barbecue", ["Chiminea", "Fire pit", "Smoker"])])

race("what's this birdwatching word?", "Animals", "medium", ["birds", "birdwatching", "words"], [
 ("The pair of lenses round your neck", "Binoculars", ["Monocle", "Periscope", "Spectacles"]),
 ("A wooden shelter where you watch birds unseen", "Hide", ["Den", "Lair", "Burrow"]),
 ("A keen birder who rushes off to see rare birds", "Twitcher", ["Tweeter", "Flapper", "Chirper"]),
 ("The bird charity, by its initials", "RSPB", ["RSPCA", "RNLI", "NSPCC"]),
 ("A bird's feathers, all together", "Plumage", ["Fleece", "Pelt", "Mane"]),
 ("Flying south for the winter", "Migration", ["Hibernation", "Aestivation", "Incubation"]),
 ("Shedding old feathers and growing new ones", "Moult", ["Brood", "Fledge", "Perch"]),
 ("Cleaning and tidying the feathers with the beak", "Preen", ["Brood", "Perch", "Hatch"]),
 ("A young bird that's just learned to fly", "Fledgling", ["Hatchling", "Gosling", "Cygnet"]),
 ("A swirling cloud of thousands of starlings", "Murmuration", ["Parliament", "Gaggle", "Charm"]),
 ("Birdsong at first light", "Dawn chorus", ["Evensong", "Lullaby", "Reveille"]),
 ("The RSPB's January count of the birds in back gardens", "Big Garden Birdwatch", ["Countryfile Count", "Bird Race", "Garden Census"]),
 ("The BBC show that watches nests live, with Chris Packham", "Springwatch", ["Countryfile", "Planet Earth", "Blue Planet"]),
 ("A wooden box with a hole, put up for blue tits", "Nest box", ["Dovecote", "Bird bath", "Feeder"]),
 ("A raised platform where you put out food", "Bird table", ["Bird bath", "Dovecote", "Perch"]),
 ("Another word for a bird of prey", "Raptor", ["Wader", "Passerine", "Finch"]),
 ("The crow family, including magpies and jays", "Corvid", ["Finch", "Warbler", "Wader"]),
 ("Fitting a tiny numbered band to a bird's leg", "Ringing", ["Branding", "Tattooing", "Clipping"]),
 ("A short sound a bird makes, rather than its song", "Call", ["Verse", "Chorus", "Refrain"]),
 ("The sound a little bird makes, and the old name for a post on X", "Tweet", ["Toot", "Honk", "Bleat"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-158.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
