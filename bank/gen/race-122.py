# Bank session 10 Oct 2026: 2 more general races -> bank/race-122.json (cat breeds, crime and legal words). 20 rows each, target 10; wrong options are
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


race("which cat breed is this?", "Animals", "hard", ["cats", "cat breeds", "pets"], [
 ("Hairless and wrinkly, it needs a jumper in winter", "Sphynx", ["Cornish Rex", "LaPerm", "Toyger"]),
 ("The tailless cat of the Isle of Man", "Manx", ["Korat", "Chartreux", "Somali"]),
 ("A short-haired cat from Thailand with a cream body, dark 'points' and bright blue eyes", "Siamese", ["Korat", "Tonkinese", "Balinese"]),
 ("Long thick coat and a flat, squashed face, like the white cat Blofeld strokes", "Persian", ["Turkish Angora", "Ragamuffin", "Nebelung"]),
 ("The biggest domestic breed, a shaggy cat named after a US state", "Maine Coon", ["Siberian", "Ragamuffin", "Chartreux"]),
 ("Bred from the Asian leopard cat, with a spotted, wild-looking coat", "Bengal", ["Ocicat", "Toyger", "Pixie-bob"]),
 ("Famous for going limp and floppy when you pick it up", "Ragdoll", ["Snowshoe", "Burmilla", "Havana Brown"]),
 ("Silvery-grey coat and green eyes, said to come from the port of Archangel", "Russian Blue", ["Chartreux", "Nebelung", "Korat"]),
 ("Its ears fold forward and down, giving it an owl-like face", "Scottish Fold", ["American Curl", "Selkirk Rex", "Cornish Rex"]),
 ("A golden 'ticked' coat, named after an old name for Ethiopia", "Abyssinian", ["Somali", "Singapura", "Oriental"]),
 ("A sleek sable-brown cat named after an old name for Myanmar", "Burmese", ["Tonkinese", "Havana Brown", "Singapura"]),
 ("A round-faced 'blue' cat said to have inspired the Cheshire Cat", "British Shorthair", ["Chartreux", "Exotic Shorthair", "Korat"]),
 ("A big long-haired Scandinavian climber, the 'skogkatt' of fairy tales", "Norwegian Forest Cat", ["Siberian", "Nebelung", "Turkish Angora"]),
 ("A white cat with a coloured head and tail, famous for loving a swim", "Turkish Van", ["Turkish Angora", "Khao Manee", "Snowshoe"]),
 ("The long-haired 'sacred cat of Burma', with pure white gloves on all four paws", "Birman", ["Balinese", "Snowshoe", "Ragamuffin"]),
 ("Pixie face, huge ears and a short curly coat, first found in Buckfastleigh", "Devon Rex", ["Selkirk Rex", "LaPerm", "Peterbald"]),
 ("The only naturally spotted domestic breed, from the land of the pharaohs", "Egyptian Mau", ["Ocicat", "Toyger", "Pixie-bob"]),
 ("A tall, leggy cross between a house cat and an African serval", "Savannah", ["Chausie", "Ocicat", "Toyger"]),
 ("A Persian with Siamese colouring and blue eyes", "Himalayan", ["Balinese", "Ragamuffin", "Tonkinese"]),
 ("A sleek, jet-black cat with copper eyes, bred to look like a mini panther", "Bombay", ["Havana Brown", "Oriental", "Chartreux"])])

race("name the crime or legal word", "General knowledge", "medium", ["law", "crime", "words"], [
 ("Setting fire to property on purpose", "Arson", ["Affray", "Larceny", "Sedition"]),
 ("Lying in court after swearing to tell the truth", "Perjury", ["Contempt", "Perversion", "Forgery"]),
 ("Damaging someone's good name with spoken words", "Slander", ["Sedition", "Affray", "Battery"]),
 ("Damaging someone's good name in print or writing", "Libel", ["Forgery", "Sedition", "Fraud"]),
 ("Killing someone unlawfully, but without meaning to kill or seriously harm them", "Manslaughter", ["Murder", "Assault", "Infanticide"]),
 ("Marrying someone while still married to someone else", "Bigamy", ["Adultery", "Monogamy", "Trespass"]),
 ("Betraying your own country, for example by helping its enemies in war", "Treason", ["Sedition", "Mutiny", "Sacrilege"]),
 ("Entering a building as a trespasser in order to steal", "Burglary", ["Larceny", "Extortion", "Affray"]),
 ("Stealing from a person using force or the threat of it", "Robbery", ["Larceny", "Fraud", "Forgery"]),
 ("Secretly taking money you were trusted to look after", "Embezzlement", ["Forgery", "Extortion", "Bribery"]),
 ("Demanding money by threatening to reveal someone's secrets", "Blackmail", ["Bribery", "Fraud", "Forgery"]),
 ("Proof that you were somewhere else when the crime happened", "Alibi", ["Caution", "Deposition", "Plea"]),
 ("A written statement sworn to be true, for use as evidence", "Affidavit", ["Codicil", "Injunction", "Indictment"]),
 ("A court order forcing a witness to turn up and give evidence", "Subpoena", ["Injunction", "Codicil", "Caveat"]),
 ("Being let out of custody before trial, sometimes against a sum of money", "Bail", ["Parole", "Probation", "Remand"]),
 ("The jury's decision: guilty or not guilty", "Verdict", ["Sentence", "Plea", "Mistrial"]),
 ("Being formally cleared of a criminal charge", "Acquittal", ["Conviction", "Appeal", "Caution"]),
 ("The person who brings a civil case, now usually called the claimant", "Plaintiff", ["Defendant", "Appellant", "Respondent"]),
 ("The legal process of proving a dead person's will", "Probate", ["Codicil", "Escrow", "Tort"]),
 ("Latin for 'you may have the body', a guard against unlawful detention", "Habeas corpus", ["Sub judice", "Pro bono", "Ultra vires"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-122.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
