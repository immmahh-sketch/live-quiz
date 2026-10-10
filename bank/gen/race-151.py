# Bank session 10 Oct 2026: 3 more general races -> bank/race-151.json (courtroom words, farm words, army words). 20 rows each, target 10; wrong options are
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

race("what's this courtroom word?", "Law", "medium", ["law", "courts", "words"], [
 ("Presides over the trial in a wig and robe, and passes sentence", "Judge", ["Steward", "Registrar", "Coroner"]),
 ("The twelve members of the public who decide guilty or not guilty", "Jury", ["Panel", "Cabinet", "Council"]),
 ("The jury's decision at the end of the trial", "Verdict", ["Summons", "Warrant", "Affidavit"]),
 ("The person on trial, accused of the crime", "Defendant", ["Juror", "Usher", "Claimant"]),
 ("Where people stand to give their evidence", "Witness box", ["Gallery", "Bench", "Lobby"]),
 ("The promise to tell the truth, the whole truth and nothing but the truth", "Oath", ["Plea", "Writ", "Caution"]),
 ("The lawyer in a wig who argues the case in the Crown Court", "Barrister", ["Notary", "Conveyancer", "Paralegal"]),
 ("The little wooden hammer an American judge bangs", "Gavel", ["Baton", "Sceptre", "Truncheon"]),
 ("The enclosure where the accused sits during a criminal trial", "Dock", ["Bench", "Gallery", "Lobby"]),
 ("Being found not guilty and set free", "Acquittal", ["Conviction", "Remand", "Probation"]),
 ("The crime of lying under oath", "Perjury", ["Libel", "Slander", "Contempt"]),
 ("Paused until a later date", "Adjourned", ["Dismissed", "Overruled", "Sustained"]),
 ("Money paid so the accused can go home until the trial", "Bail", ["Fine", "Costs", "Damages"]),
 ("Proof you were somewhere else when the crime happened", "Alibi", ["Motive", "Hearsay", "Precedent"]),
 ("What TV lawyers shout when the other side asks an unfair question", "Objection", ["Recess", "Hearsay", "Precedent"]),
 ("Asking a higher court to overturn the decision", "Appeal", ["Plea", "Remand", "Caution"]),
 ("London's Central Criminal Court, topped by a golden statue of Justice", "Old Bailey", ["Royal Courts", "Lincoln's Inn", "Middle Temple"]),
 ("A trial stopped part-way and declared invalid, perhaps over a juror's misconduct", "Mistrial", ["Retrial", "Remand", "Recess"]),
 ("An object shown to the court as evidence, labelled with a letter or number", "Exhibit", ["Affidavit", "Summons", "Writ"]),
 ("Slang for a senior barrister, a King's Counsel, after the fabric of their gown", "Silk", ["Bencher", "Gown", "Ermine"])])

race("what's this farm word?", "Animals", "easy", ["farming", "countryside", "words"], [
 ("A young female cow that hasn't had a calf yet", "Heifer", ["Bullock", "Steer", "Ox"]),
 ("Where the pigs live", "Sty", ["Byre", "Kennel", "Stable"]),
 ("Where the hens are shut in at night", "Coop", ["Hutch", "Kennel", "Stall"]),
 ("The big machine that cuts and threshes the wheat in one go", "Combine harvester", ["Baler", "Seed drill", "Muck spreader"]),
 ("A tightly packed block of hay or straw", "Bale", ["Stook", "Rick", "Clamp"]),
 ("Turns over the soil before sowing", "Plough", ["Baler", "Scythe", "Sickle"]),
 ("A male sheep", "Ram", ["Ewe", "Nanny", "Hind"]),
 ("Clipping the wool off the sheep in early summer", "Shearing", ["Dipping", "Docking", "Drenching"]),
 ("The dog breed famous for rounding up sheep", "Border Collie", ["Labrador", "Beagle", "Dachshund"]),
 ("A field left unplanted for a season to rest", "Fallow", ["Headland", "Stubble", "Paddock"]),
 ("The long, straight trench cut by a plough", "Furrow", ["Hedgerow", "Dyke", "Verge"]),
 ("Where the cows are milked", "Milking parlour", ["Granary", "Tack room", "Lambing shed"]),
 ("Pickled grass fed to cattle in winter, stored under black plastic", "Silage", ["Mulch", "Compost", "Bran"]),
 ("A tall tower that stores grain", "Silo", ["Windmill", "Water tower", "Oast house"]),
 ("A female pig", "Sow", ["Ewe", "Doe", "Hen"]),
 ("A baby horse", "Foal", ["Calf", "Kid", "Cub"]),
 ("Steps that let walkers over a fence, but not the sheep", "Stile", ["Lychgate", "Turnstile", "Portcullis"]),
 ("Metal bars across a road that cattle won't walk over", "Cattle grid", ["Cattle crush", "Turnstile", "Speed bump"]),
 ("The upper floor of a barn, where the hay is kept", "Hayloft", ["Cellar", "Pantry", "Scullery"]),
 ("Stands in the field in old clothes to frighten off the birds", "Scarecrow", ["Dummy", "Effigy", "Totem"])])

race("what's this army word?", "History", "medium", ["army", "military", "words"], [
 ("The rank with three stripes on the sleeve", "Sergeant", ["Corporal", "Lance corporal", "Major"]),
 ("The lowest rank of soldier", "Private", ["Colonel", "Captain", "Major"]),
 ("The buildings where soldiers live", "Barracks", ["Armoury", "Arsenal", "Magazine"]),
 ("The blade fixed to the end of a rifle", "Bayonet", ["Cutlass", "Sabre", "Dagger"]),
 ("Patterned clothing that blends into the background", "Camouflage", ["Tunic", "Epaulette", "Puttees"]),
 ("The soldier standing guard at the gate", "Sentry", ["Scout", "Sniper", "Batman"]),
 ("Where soldiers eat together", "Mess", ["Guardroom", "Armoury", "Bunker"]),
 ("A hand raised to the forehead to greet an officer", "Salute", ["Bow", "Wave", "Curtsey"]),
 ("A newly signed-up soldier", "Recruit", ["Veteran", "Reservist", "Mercenary"]),
 ("A permanent army unit with its own badge and history, like the Coldstream Guards", "Regiment", ["Squad", "Section", "Fireteam"]),
 ("A unit of about 30 soldiers led by a lieutenant", "Platoon", ["Battalion", "Division", "Brigade"]),
 ("The bugle call that wakes the soldiers in the morning", "Reveille", ["Last Post", "Tattoo", "Retreat"]),
 ("The letters for a soldier who's gone missing without permission", "AWOL", ["POW", "NCO", "RSM"]),
 ("Soldiers who fight on foot", "Infantry", ["Cavalry", "Artillery", "Signals"]),
 ("A long ditch dug to shelter soldiers on the Western Front", "Trench", ["Moat", "Rampart", "Palisade"]),
 ("The soldier who treats the wounded on the battlefield", "Medic", ["Padre", "Gunner", "Signaller"]),
 ("The officer in charge of supplies and stores", "Quartermaster", ["Adjutant", "Provost", "Chaplain"]),
 ("An army engineer who builds bridges and clears mines", "Sapper", ["Gunner", "Rifleman", "Drummer"]),
 ("The big open square where soldiers drill and march", "Parade ground", ["Firing range", "Assault course", "Helipad"]),
 ("Metal discs worn round a soldier's neck to identify them", "Dog tags", ["Medals", "Insignia", "Epaulettes"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-151.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
