# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-57.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

G = "UK geography"
board("Towns in Shropshire", G, "hard", ["Shropshire", "towns", "England"],
 ["Shrewsbury", "Telford", "Oswestry", "Bridgnorth", "Ludlow", "Whitchurch", "Market Drayton", "Newport", "Wellington", "Church Stretton", "Much Wenlock", "Ironbridge", "Shifnal", "Wem", "Bishop's Castle"],
 ["Hereford", "Wrexham", "Stafford", "Kidderminster", "Welshpool"])
board("Towns in Wiltshire", G, "hard", ["Wiltshire", "towns", "England"],
 ["Salisbury", "Swindon", "Chippenham", "Trowbridge", "Devizes", "Marlborough", "Warminster", "Melksham", "Calne", "Corsham", "Bradford-on-Avon", "Malmesbury", "Westbury", "Amesbury", "Royal Wootton Bassett"],
 ["Bath", "Frome", "Newbury", "Cirencester", "Andover"])
board("Towns in Surrey", G, "medium", ["Surrey", "towns", "England"],
 ["Guildford", "Woking", "Epsom", "Farnham", "Godalming", "Reigate", "Redhill", "Dorking", "Leatherhead", "Camberley", "Staines", "Weybridge", "Cobham", "Haslemere", "Esher"],
 ["Crawley", "Horsham", "Croydon", "Reading", "Sevenoaks"])
board("Towns in Gloucestershire", G, "medium", ["Gloucestershire", "Cotswolds", "towns"],
 ["Gloucester", "Cheltenham", "Cirencester", "Stroud", "Tewkesbury", "Stow-on-the-Wold", "Bourton-on-the-Water", "Tetbury", "Moreton-in-Marsh", "Lydney", "Cinderford", "Dursley", "Winchcombe", "Chipping Campden", "Coleford"],
 ["Bath", "Hereford", "Worcester", "Swindon", "Banbury"])
board("Towns in Staffordshire", G, "hard", ["Staffordshire", "towns", "England"],
 ["Stafford", "Stoke-on-Trent", "Lichfield", "Tamworth", "Burton upon Trent", "Cannock", "Leek", "Newcastle-under-Lyme", "Uttoxeter", "Stone", "Rugeley", "Kidsgrove", "Cheadle", "Biddulph", "Penkridge"],
 ["Crewe", "Derby", "Wolverhampton", "Shrewsbury", "Nuneaton"])
board("Towns in Nottinghamshire", G, "medium", ["Nottinghamshire", "towns", "England"],
 ["Nottingham", "Mansfield", "Newark", "Worksop", "Retford", "Southwell", "Beeston", "West Bridgford", "Hucknall", "Arnold", "Kirkby-in-Ashfield", "Sutton-in-Ashfield", "Bingham", "Eastwood", "Ollerton"],
 ["Chesterfield", "Loughborough", "Grantham", "Doncaster", "Derby"])
board("Towns in Oxfordshire", G, "medium", ["Oxfordshire", "towns", "England"],
 ["Oxford", "Banbury", "Bicester", "Witney", "Abingdon", "Didcot", "Henley-on-Thames", "Wantage", "Thame", "Wallingford", "Chipping Norton", "Woodstock", "Carterton", "Kidlington", "Faringdon"],
 ["High Wycombe", "Reading", "Swindon", "Northampton", "Aylesbury"])
board("Towns in Hertfordshire", G, "medium", ["Hertfordshire", "towns", "England"],
 ["St Albans", "Watford", "Hertford", "Stevenage", "Hemel Hempstead", "Hitchin", "Letchworth", "Welwyn Garden City", "Harpenden", "Bishop's Stortford", "Hatfield", "Berkhamsted", "Tring", "Royston", "Ware"],
 ["Luton", "Harlow", "Enfield", "Aylesbury", "Bedford"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-57.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
