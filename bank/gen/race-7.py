# Bank session 10 Oct 2026: 4 more general races -> bank/race-7.json. 20 rows each, target 10; wrong options are
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

race("what's the Italian word?", "Words and language", "medium", ["Italian", "languages"], [
 ("Love", "Amore", ["Amaro", "Ambra", "Armadio"]), ("Goodbye", "Arrivederci", ["Avanti", "Allora", "Andiamo"]),
 ("Good morning", "Buongiorno", ["Buonasera", "Buonanotte", "Benvenuto"]), ("Please", "Per favore", ["Per sempre", "Perché", "Permesso"]),
 ("Church", "Chiesa", ["Chiave", "Chiusa", "Cassa"]), ("Square (in a town)", "Piazza", ["Pizza", "Pazzo", "Pezzo"]),
 ("Street", "Strada", ["Stanza", "Stella", "Strega"]), ("Ice cream", "Gelato", ["Gelo", "Gilet", "Gettone"]),
 ("Cheese", "Formaggio", ["Formica", "Fortuna", "Foraggio"]), ("Boy", "Ragazzo", ["Ragno", "Regalo", "Razzo"]),
 ("Girl", "Ragazza", ["Regina", "Ragione", "Rana"]), ("Beautiful", "Bello", ["Bollo", "Bagno", "Bianco"]),
 ("Bridge", "Ponte", ["Porta", "Punto", "Pane"]), ("Window", "Finestra", ["Fiera", "Fontana", "Festa"]),
 ("Dog", "Cane", ["Carne", "Cena", "Casa"]), ("Cat", "Gatto", ["Gallo", "Gamba", "Guanto"]),
 ("Sea", "Mare", ["Mano", "Male", "Madre"]), ("Mountain", "Montagna", ["Montone", "Moneta", "Mostra"]),
 ("Island", "Isola", ["Isolato", "Inverno", "Insegna"]), ("Tomorrow", "Domani", ["Domenica", "Dopo", "Donna"])])

race("which sport has this role or position?", "Sport", "medium", ["positions", "sports"], [
 ("Wicketkeeper", "Cricket", ["Rounders", "Hockey", "Lacrosse"]), ("Quarterback", "American football", ["Rugby league", "Australian rules", "Gaelic football"]),
 ("Pitcher", "Baseball", ["Rounders", "Lacrosse", "Hurling"]), ("Goal attack", "Netball", ["Handball", "Korfball", "Lacrosse"]),
 ("Setter", "Volleyball", ["Badminton", "Squash", "Handball"]), ("Fly-half", "Rugby union", ["Gaelic football", "Australian rules", "Hurling"]),
 ("Point guard", "Basketball", ["Handball", "Korfball", "Lacrosse"]), ("Cox", "Rowing", ["Canoeing", "Kayaking", "Dragon boat racing"]),
 ("Skip", "Curling", ["Snooker", "Darts", "Bobsleigh"]), ("Jockey", "Horse racing", ["Show jumping", "Polo", "Dressage"]),
 ("Caddie", "Golf", ["Tennis", "Snooker", "Croquet"]), ("Netminder", "Ice hockey", ["Handball", "Hockey", "Korfball"]),
 ("Picador", "Bullfighting", ["Rodeo", "Fencing", "Polo"]), ("Seeker", "Quidditch", ["Lacrosse", "Polo", "Hurling"]),
 ("Domestique", "Cycling", ["Athletics", "Triathlon", "Motor racing"]), ("Cutman", "Boxing", ["Wrestling", "Judo", "Fencing"]),
 ("Jammer", "Roller derby", ["Speed skating", "Figure skating", "Skateboarding"]), ("Hole set", "Water polo", ["Swimming", "Diving", "Canoe polo"]),
 ("Co-driver", "Rallying", ["Speedway", "Motocross", "Karting"]), ("Helm", "Sailing", ["Canoeing", "Surfing", "Windsurfing"])])

race("what's this wedding anniversary called?", "Weddings", "medium", ["anniversaries", "weddings"], [
 ("1st", "Paper", ["Wool", "Glass", "Velvet"]), ("2nd", "Cotton", ["Wool", "Velvet", "Glass"]), ("3rd", "Leather", ["Copper", "Wool", "Oak"]),
 ("5th", "Wood", ["Iron", "Copper", "Glass"]), ("8th", "Bronze", ["Brass", "Copper", "Pewter"]), ("9th", "Pottery", ["Glass", "Wool", "Brass"]),
 ("10th", "Tin", ["Iron", "Copper", "Pewter"]), ("11th", "Steel", ["Iron", "Brass", "Copper"]), ("12th", "Silk", ["Velvet", "Wool", "Satin"]),
 ("13th", "Lace", ["Velvet", "Satin", "Wool"]), ("15th", "Crystal", ["Glass", "Amber", "Opal"]), ("20th", "China", ["Glass", "Opal", "Amber"]),
 ("25th", "Silver", ["Pewter", "Brass", "Copper"]), ("30th", "Pearl", ["Opal", "Amber", "Jade"]), ("35th", "Coral", ["Opal", "Topaz", "Amber"]),
 ("40th", "Ruby", ["Garnet", "Topaz", "Opal"]), ("45th", "Sapphire", ["Topaz", "Jade", "Opal"]), ("50th", "Gold", ["Brass", "Amber", "Topaz"]),
 ("55th", "Emerald", ["Jade", "Topaz", "Opal"]), ("60th", "Diamond", ["Opal", "Topaz", "Jade"])])

race("what is this chemical formula?", "Science and nature", "hard", ["chemistry", "formulas"], [
 ("H₂O", "Water", ["Hydrogen", "Helium", "Ethane"]), ("CO₂", "Carbon dioxide", ["Nitrogen dioxide", "Sulphur dioxide", "Chlorine"]),
 ("NaCl", "Salt", ["Bleach", "Chlorine", "Washing soda"]), ("O₃", "Ozone", ["Nitrogen", "Helium", "Chlorine"]),
 ("CH₄", "Methane", ["Ethane", "Propane", "Butane"]), ("NH₃", "Ammonia", ["Nitric acid", "Nitrogen", "Ethane"]),
 ("H₂O₂", "Hydrogen peroxide", ["Bleach", "Vinegar", "Nitric acid"]), ("C₆H₁₂O₆", "Glucose", ["Starch", "Cellulose", "Lactose"]),
 ("CaCO₃", "Chalk", ["Quicklime", "Epsom salts", "Magnesia"]), ("HCl", "Hydrochloric acid", ["Nitric acid", "Vinegar", "Chlorine"]),
 ("H₂SO₄", "Sulphuric acid", ["Nitric acid", "Sulphur dioxide", "Vinegar"]), ("NaHCO₃", "Bicarbonate of soda", ["Washing soda", "Epsom salts", "Potash"]),
 ("C₂H₅OH", "Alcohol (ethanol)", ["Vinegar", "Ethylene", "Propane"]), ("CO", "Carbon monoxide", ["Nitrogen dioxide", "Sulphur dioxide", "Helium"]),
 ("N₂O", "Laughing gas", ["Nitrogen dioxide", "Nitric acid", "Sulphur dioxide"]), ("SiO₂", "Sand (silica)", ["Lime", "Quicklime", "Magnesia"]),
 ("Fe₂O₃", "Rust", ["Iron sulphide", "Magnetite", "Quicklime"]), ("C₁₂H₂₂O₁₁", "Sugar (sucrose)", ["Starch", "Cellulose", "Vinegar"]),
 ("O₂", "Oxygen", ["Nitrogen", "Hydrogen", "Helium"]), ("NaOH", "Caustic soda", ["Washing soda", "Bleach", "Potash"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
