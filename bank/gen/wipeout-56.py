# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-56.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

G = "UK geography"
board("Towns in Devon (not Cornwall)", G, "medium", ["Devon", "towns", "England"],
 ["Exeter", "Plymouth", "Torquay", "Paignton", "Barnstaple", "Bideford", "Exmouth", "Sidmouth", "Dartmouth", "Totnes", "Tiverton", "Okehampton", "Salcombe", "Ilfracombe", "Brixham"],
 ["Truro", "Bude", "Newquay", "Penzance", "Launceston"])
board("Towns in Dorset", G, "hard", ["Dorset", "towns", "England"],
 ["Bournemouth", "Poole", "Weymouth", "Dorchester", "Bridport", "Lyme Regis", "Swanage", "Wimborne", "Shaftesbury", "Sherborne", "Blandford Forum", "Christchurch", "Wareham", "Portland", "Verwood"],
 ["Salisbury", "Yeovil", "Lymington", "Exmouth", "Taunton"])
board("Towns in Somerset", G, "hard", ["Somerset", "towns", "England"],
 ["Taunton", "Yeovil", "Bridgwater", "Glastonbury", "Wells", "Frome", "Minehead", "Street", "Shepton Mallet", "Chard", "Burnham-on-Sea", "Wellington", "Crewkerne", "Cheddar", "Weston-super-Mare"],
 ["Bristol", "Salisbury", "Exeter", "Gloucester", "Swindon"])
board("Towns in Lincolnshire", G, "medium", ["Lincolnshire", "towns", "England"],
 ["Lincoln", "Grimsby", "Scunthorpe", "Boston", "Grantham", "Skegness", "Spalding", "Stamford", "Louth", "Gainsborough", "Sleaford", "Cleethorpes", "Mablethorpe", "Horncastle", "Bourne"],
 ["Peterborough", "Newark", "Doncaster", "Hull", "King's Lynn"])
board("Towns in Cheshire", G, "medium", ["Cheshire", "towns", "England"],
 ["Chester", "Crewe", "Macclesfield", "Warrington", "Runcorn", "Widnes", "Northwich", "Nantwich", "Knutsford", "Wilmslow", "Congleton", "Ellesmere Port", "Sandbach", "Middlewich", "Winsford"],
 ["Stockport", "Wrexham", "Stoke-on-Trent", "St Helens", "Bolton"])
board("Towns in Derbyshire", G, "medium", ["Derbyshire", "Peak District", "towns"],
 ["Derby", "Chesterfield", "Buxton", "Matlock", "Bakewell", "Glossop", "Ilkeston", "Ashbourne", "Belper", "Swadlincote", "Long Eaton", "Ripley", "Alfreton", "Heanor", "Castleton"],
 ["Sheffield", "Nottingham", "Leek", "Macclesfield", "Mansfield"])
board("Towns in Hampshire", G, "medium", ["Hampshire", "towns", "England"],
 ["Southampton", "Portsmouth", "Winchester", "Basingstoke", "Andover", "Aldershot", "Fareham", "Gosport", "Petersfield", "Lymington", "Romsey", "Alton", "Eastleigh", "Fleet", "New Milton"],
 ["Salisbury", "Bournemouth", "Chichester", "Guildford", "Newbury"])
board("Towns in Suffolk (not Norfolk)", G, "medium", ["Suffolk", "East Anglia", "towns"],
 ["Ipswich", "Lowestoft", "Bury St Edmunds", "Felixstowe", "Sudbury", "Southwold", "Aldeburgh", "Woodbridge", "Newmarket", "Stowmarket", "Haverhill", "Beccles", "Framlingham", "Lavenham", "Hadleigh"],
 ["Norwich", "Cromer", "Thetford", "Colchester", "Cambridge"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-56.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
