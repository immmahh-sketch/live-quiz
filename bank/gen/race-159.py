# Bank session 11 Oct 2026: 3 more general races -> bank/race-159.json (auction, clothing and insect words). 20 rows each, target 10; wrong options are
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

race("what's this auction word?", "Everyday life", "medium", ["auctions", "antiques", "words"], [
 ("The auctioneer's little hammer", "Gavel", ["Baton", "Chisel", "Pestle"]),
 ("Each item up for sale, with its own number", "Lot", ["Batch", "Bundle", "Parcel"]),
 ("The lowest price the seller will accept", "Reserve", ["Deposit", "Ransom", "Retainer"]),
 ("The final winning bid", "Hammer price", ["Asking price", "Cost price", "Trade price"]),
 ("The auctioneer's countdown to the sale", "Going, going, gone", ["Ready, steady, go", "Three, two, one", "Once upon a time"]),
 ("The numbered card you hold up to bid", "Paddle", ["Placard", "Banner", "Flag"]),
 ("Someone making an offer", "Bidder", ["Broker", "Agent", "Curator"]),
 ("The person selling", "Vendor", ["Broker", "Agent", "Curator"]),
 ("The recorded history of who has owned an item", "Provenance", ["Inventory", "Insignia", "Ledger"]),
 ("The glow old wood or bronze takes on with age", "Patina", ["Varnish", "Veneer", "Lacquer"]),
 ("The stamp on silver showing where and when it was tested", "Hallmark", ["Watermark", "Postmark", "Trademark"]),
 ("Odds and ends of little value", "Bric-a-brac", ["Heirlooms", "Treasures", "Valuables"]),
 ("The BBC show where experts value the public's treasures", "Antiques Roadshow", ["Flog It!", "Cash in the Attic", "Dickinson's Real Deal"]),
 ("Red and blue teams buy at a fair and sell at auction", "Bargain Hunt", ["Flog It!", "Cash in the Attic", "Antiques Road Trip"]),
 ("The perma-tanned 'cheap as chips' dealer", "David Dickinson", ["Tim Wonnacott", "Paul Martin", "Fiona Bruce"]),
 ("The auction house founded in London in 1744", "Sotheby's", ["Bonhams", "Phillips", "Harrods"]),
 ("The auction house that sold Leonardo's 'Salvator Mundi' for $450 million", "Christie's", ["Bonhams", "Phillips", "Heritage"]),
 ("The extra percentage added on top of the winning bid", "Buyer's premium", ["Stamp duty", "Service charge", "Corkage"]),
 ("Selling junk from the back of your car", "Car boot sale", ["Jumble sale", "Garage sale", "Yard sale"]),
 ("A modern copy made to look old", "Reproduction", ["Restoration", "Renovation", "Rendition"])])

race("what's this clothing word?", "Fashion", "easy", ["clothes", "fashion", "words"], [
 ("A knitted jumper that buttons down the front", "Cardigan", ["Tank top", "Poncho", "Tabard"]),
 ("Trousers with a bib and shoulder straps", "Dungarees", ["Chinos", "Culottes", "Jodhpurs"]),
 ("An all-in-one fleece suit for lounging about", "Onesie", ["Kaftan", "Toga", "Sarong"]),
 ("The tartan skirt worn by Scotsmen", "Kilt", ["Sporran", "Sarong", "Kaftan"]),
 ("A smart jacket with a school badge", "Blazer", ["Anorak", "Cagoule", "Bomber jacket"]),
 ("A coat with a fur-trimmed hood, loved by mods", "Parka", ["Cagoule", "Duffel coat", "Trench coat"]),
 ("The stiff net skirt worn by ballerinas", "Tutu", ["Crinoline", "Bustle", "Basque"]),
 ("A silky scarf tied at the neck instead of a tie", "Cravat", ["Bandana", "Lanyard", "Choker"]),
 ("Leather shoes with decorative punched holes", "Brogues", ["Loafers", "Clogs", "Espadrilles"]),
 ("The cloth cap people link with Yorkshire", "Flat cap", ["Bowler", "Beret", "Fez"]),
 ("A woolly hat covering the whole face except the eyes", "Balaclava", ["Bobble hat", "Beanie", "Deerstalker"]),
 ("A sleeveless jacket worn under a suit jacket", "Waistcoat", ["Gilet", "Bolero", "Tabard"]),
 ("Stretchy, skin-tight trousers", "Leggings", ["Flares", "Chinos", "Cargo trousers"]),
 ("A sleeveless dress worn over a blouse", "Pinafore", ["Kaftan", "Sarong", "Tabard"]),
 ("A sweatshirt with a hood", "Hoodie", ["Gilet", "Poncho", "Tank top"]),
 ("Shoes with very high, thin heels", "Stilettos", ["Wedges", "Platforms", "Kitten heels"]),
 ("The long draped garment worn in India", "Sari", ["Cheongsam", "Dirndl", "Poncho"]),
 ("The wide-sleeved robe from Japan", "Kimono", ["Cheongsam", "Dirndl", "Hanbok"]),
 ("Leather shorts with braces, from Bavaria", "Lederhosen", ["Dirndl", "Jodhpurs", "Culottes"]),
 ("A one-piece outfit covering body, arms and legs", "Jumpsuit", ["Tracksuit", "Twinset", "Trouser suit"])])

race("what's this insect word?", "Animals", "medium", ["insects", "bugs", "words"], [
 ("The feelers on an insect's head", "Antennae", ["Tentacles", "Whiskers", "Pincers"]),
 ("The middle section of an insect's body", "Thorax", ["Pelvis", "Carapace", "Mandible"]),
 ("The rear section of an insect's body", "Abdomen", ["Pelvis", "Carapace", "Mandible"]),
 ("The grub stage that hatches from the egg", "Larva", ["Spawn", "Embryo", "Imago"]),
 ("The resting stage inside a case, before the adult comes out", "Pupa", ["Nymph", "Spawn", "Embryo"]),
 ("A butterfly's pupa case", "Chrysalis", ["Cocoon", "Husk", "Pod"]),
 ("A butterfly's larva", "Caterpillar", ["Tadpole", "Elver", "Fry"]),
 ("A fly's larva", "Maggot", ["Tadpole", "Elver", "Fry"]),
 ("Insect eyes made of thousands of tiny lenses", "Compound eyes", ["Bifocals", "Cat's eyes", "Eyelets"]),
 ("The one bee in the hive that lays the eggs", "Queen", ["Matriarch", "Duchess", "Empress"]),
 ("A male bee whose only job is mating", "Drone", ["Soldier", "Scout", "Hornet"]),
 ("A female bee that collects the nectar", "Worker", ["Soldier", "Hornet", "Wasp"]),
 ("Where honeybees live", "Hive", ["Warren", "Sett", "Eyrie"]),
 ("The hard outer casing an insect has instead of bones", "Exoskeleton", ["Endoskeleton", "Cartilage", "Membrane"]),
 ("A complete change of body, like caterpillar to butterfly", "Metamorphosis", ["Photosynthesis", "Mitosis", "Hibernation"]),
 ("A scientist who studies insects", "Entomologist", ["Etymologist", "Ornithologist", "Herpetologist"]),
 ("A huge flying group of bees or locusts", "Swarm", ["Shoal", "Flock", "Herd"]),
 ("A butterfly's long, coiled drinking tube", "Proboscis", ["Tusk", "Antler", "Beak"]),
 ("How many legs every adult insect has", "Six", ["Eight", "Ten", "Four"]),
 ("Britain's biggest beetle, with huge antler-like jaws", "Stag beetle", ["Dung beetle", "Ladybird", "Cockchafer"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-159.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
