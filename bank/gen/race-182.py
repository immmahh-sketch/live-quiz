# Bank session 11 Oct 2026: 3 more general races -> bank/race-182.json (dog, sweet shop and gig words). 20 rows each, target 10; wrong options are
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

race("what's this dog word?", "Animals", "easy", ["dogs", "pets", "words"], [
 ("A young dog", "Puppy", ["Cub", "Kit", "Foal"]),
 ("A dog's shelter in the garden", "Kennel", ["Hutch", "Coop", "Stable"]),
 ("A dog of mixed breed", "Mongrel", ["Thoroughbred", "Pedigree", "Champion"]),
 ("Worn over the snout to stop biting", "Muzzle", ["Bridle", "Halter", "Blinkers"]),
 ("The band round a dog's neck with its name tag", "Collar", ["Bridle", "Halter", "Girth"]),
 ("The strap you walk a dog on", "Lead", ["Rein", "Tether", "Bridle"]),
 ("The famous dog show held every March in Birmingham", "Crufts", ["Badminton", "Burghley", "Chelsea"]),
 ("The charity behind 'A dog is for life, not just for Christmas'", "Dogs Trust", ["RSPCA", "PDSA", "Blue Cross"]),
 ("A dog trained to lead a blind person", "Guide dog", ["Sheepdog", "Bloodhound", "Watchdog"]),
 ("A dog trained to fetch birds that have been shot", "Gun dog", ["Toy dog", "Guard dog", "Herding dog"]),
 ("A small pampered pet that sits on your knee", "Lapdog", ["Watchdog", "Underdog", "Sea dog"]),
 ("A police dog that finds drugs or explosives", "Sniffer dog", ["Guard dog", "Herding dog", "Show dog"]),
 ("The long, mournful cry of a wolf or husky", "Howl", ["Whimper", "Snarl", "Growl"]),
 ("The breed that pulls sleds across the snow", "Husky", ["Boxer", "Pug", "Shih Tzu"]),
 ("The spotted breed that once ran beside fire engines", "Dalmatian", ["Pointer", "Weimaraner", "Setter"]),
 ("The fastest breed, raced round a track", "Greyhound", ["Bulldog", "Basset Hound", "Pekingese"]),
 ("The breed the late Queen famously loved", "Corgi", ["Dachshund", "Pug", "Beagle"]),
 ("Teaching a puppy to go to the toilet outside", "House-training", ["Socialising", "Obedience", "Teething"]),
 ("Brushing and trimming a dog's coat", "Grooming", ["Worming", "Neutering", "Microchipping"]),
 ("The command to walk close by your side", "Heel", ["Stay", "Fetch", "Beg"])])

race("what's this sweet shop word?", "Food and drink", "easy", ["sweets", "nostalgia", "words"], [
 ("A huge hard sweet that changes colour as you suck it", "Gobstopper", ["Barley sugar", "Butterscotch", "Mint imperial"]),
 ("Choosing your own sweets from the tubs", "Pick 'n' mix", ["Lucky dip", "Assortment", "Selection box"]),
 ("The old weight sweets were sold in from the jar: four ounces", "Quarter", ["Pound", "Stone", "Gill"]),
 ("Fizzy powder you dip a lolly into", "Sherbet", ["Icing sugar", "Popping candy", "Bicarbonate"]),
 ("Black and chewy, made from a root, and found in Allsorts", "Liquorice", ["Aniseed", "Treacle", "Molasses"]),
 ("A striped boiled mint, and Scrooge's favourite word", "Humbug", ["Mint imperial", "Polo", "Murray Mint"]),
 ("A soft sugary block made with butter and milk", "Fudge", ["Nougat", "Marzipan", "Halva"]),
 ("The seaside stick with the resort's name running through it", "Rock", ["Candy cane", "Barley sugar", "Stick toffee"]),
 ("Spun sugar on a stick at the fair", "Candyfloss", ["Marshmallow", "Meringue", "Nougat"]),
 ("Little jelly people, the Fourth Doctor's favourite", "Jelly Babies", ["Jelly Tots", "Wine Gums", "Fruit Pastilles"]),
 ("Rice-paper discs filled with sherbet", "Flying saucers", ["Parma Violets", "Refreshers", "Fruit Salads"]),
 ("Fizzy tablets printed with messages like 'Be Mine'", "Love Hearts", ["Parma Violets", "Refreshers", "Polos"]),
 ("A hard sweet on a stick", "Lollipop", ["Sugar mouse", "Barley sugar", "Ice lolly"]),
 ("An apple dipped in hard caramel for Bonfire Night", "Toffee apple", ["Glacé cherry", "Candied peel", "Crystallised ginger"]),
 ("Tiny pastel cubes and jellies", "Dolly Mixtures", ["Jelly Tots", "Allsorts", "Midget Gems"]),
 ("Fizzy gummy sweets shaped like little bottles of pop", "Cola bottles", ["Fried eggs", "Shrimps", "Jelly beans"]),
 ("The tall glass container on the sweet-shop shelf", "Sweet jar", ["Kilner jar", "Bell jar", "Tea caddy"]),
 ("Pink and yellow boiled sweets with a nail-varnish smell", "Pear drops", ["Cola cubes", "Aniseed balls", "Clove rock"]),
 ("Red and yellow boiled sweets named after a pudding", "Rhubarb and custard", ["Jam roly-poly", "Spotted dick", "Bread and butter"]),
 ("Chewy toffee balls dusted in icing sugar", "Bonbons", ["Truffles", "Macarons", "Marshmallows"])])

race("what's this gig word?", "Music", "medium", ["gigs", "live music", "words"], [
 ("The crew member who lugs and sets up the band's gear", "Roadie", ["Bouncer", "Usher", "Steward"]),
 ("Extra songs after the band leaves and comes back on", "Encore", ["Reprise", "Medley", "Interval"]),
 ("The list of songs the band will play tonight", "Setlist", ["Tracklist", "Playlist", "Chart"]),
 ("The band's list of backstage demands", "Rider", ["Contract", "Manifest", "Itinerary"]),
 ("The act that plays before the headliner", "Support act", ["Tribute act", "Session band", "House band"]),
 ("Leaping off the stage into the crowd", "Stage dive", ["Belly flop", "Swan dive", "Moonwalk"]),
 ("Being passed over the audience's heads", "Crowd surfing", ["Conga", "Pogoing", "Slow dance"]),
 ("The area at the front where fans slam into each other", "Mosh pit", ["Orchestra pit", "Front row", "Dance floor"]),
 ("Testing the levels before the doors open", "Soundcheck", ["Curtain call", "Photocall", "Roll call"]),
 ("Speakers pointing at the band so they can hear themselves", "Monitors", ["Subwoofers", "Tweeters", "Mixers"]),
 ("The box that makes an electric guitar loud", "Amp", ["Mixer", "Pickup", "Capo"]),
 ("The floor switch a guitarist stamps on to change the sound", "Effects pedal", ["Capo", "Whammy bar", "Tuning peg"]),
 ("The little piece used to strum a guitar", "Plectrum", ["Bow", "Mallet", "Slide"]),
 ("Someone outside selling tickets at a huge mark-up", "Tout", ["Busker", "Pedlar", "Hawker"]),
 ("A superfan who follows the band everywhere", "Groupie", ["Session musician", "Tour manager", "A&R man"]),
 ("The person who books the venue and sells the gig", "Promoter", ["Producer", "Engineer", "Publicist"]),
 ("The act at the top of the bill", "Headliner", ["Opener", "Warm-up", "Compère"]),
 ("A run of gigs in different cities", "Tour", ["Residency", "Session", "Showcase"]),
 ("An acoustic set with no electric instruments", "Unplugged", ["Unmixed", "Unreleased", "Untitled"]),
 ("The squeal when a mic picks up its own speaker", "Feedback", ["Reverb", "Distortion", "Echo"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-182.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
