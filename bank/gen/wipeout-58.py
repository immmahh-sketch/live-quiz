# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-58.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

G = "UK geography"
board("Towns in Leicestershire", G, "hard", ["Leicestershire", "towns", "England"],
 ["Leicester", "Loughborough", "Hinckley", "Melton Mowbray", "Market Harborough", "Coalville", "Lutterworth", "Ashby-de-la-Zouch", "Oadby", "Wigston", "Shepshed", "Syston", "Earl Shilton", "Castle Donington", "Birstall"],
 ["Rutland", "Nuneaton", "Kettering", "Grantham", "Burton upon Trent"])
board("Towns in Northamptonshire", G, "hard", ["Northamptonshire", "towns", "England"],
 ["Northampton", "Kettering", "Corby", "Wellingborough", "Daventry", "Rushden", "Brackley", "Towcester", "Oundle", "Desborough", "Rothwell", "Raunds", "Higham Ferrers", "Thrapston", "Burton Latimer"],
 ["Bedford", "Milton Keynes", "Banbury", "Rugby", "Peterborough"])
board("Towns in Worcestershire", G, "hard", ["Worcestershire", "towns", "England"],
 ["Worcester", "Kidderminster", "Redditch", "Bromsgrove", "Malvern", "Evesham", "Droitwich", "Pershore", "Stourport-on-Severn", "Bewdley", "Upton-upon-Severn", "Tenbury Wells", "Broadway", "Hagley", "Wythall"],
 ["Hereford", "Ludlow", "Stratford-upon-Avon", "Cheltenham", "Dudley"])
board("Towns in Berkshire", G, "medium", ["Berkshire", "towns", "England"],
 ["Reading", "Slough", "Windsor", "Maidenhead", "Bracknell", "Newbury", "Wokingham", "Ascot", "Eton", "Hungerford", "Thatcham", "Sandhurst", "Crowthorne", "Twyford", "Lambourn"],
 ["Henley-on-Thames", "Basingstoke", "High Wycombe", "Guildford", "Marlow"])
board("Towns in Buckinghamshire", G, "medium", ["Buckinghamshire", "towns", "England"],
 ["Aylesbury", "High Wycombe", "Milton Keynes", "Marlow", "Amersham", "Beaconsfield", "Chesham", "Buckingham", "Princes Risborough", "Gerrards Cross", "Olney", "Wendover", "Great Missenden", "Newport Pagnell", "Winslow"],
 ["Tring", "Henley-on-Thames", "Maidenhead", "Thame", "Luton"])
board("Towns in Cambridgeshire", G, "medium", ["Cambridgeshire", "towns", "England"],
 ["Cambridge", "Peterborough", "Ely", "Huntingdon", "St Neots", "St Ives", "Wisbech", "March", "Whittlesey", "Chatteris", "Ramsey", "Soham", "Littleport", "Sawston", "Godmanchester"],
 ["Newmarket", "King's Lynn", "Bedford", "Stamford", "Haverhill"])
board("Towns in West Sussex", G, "medium", ["Sussex", "towns", "England"],
 ["Chichester", "Crawley", "Worthing", "Horsham", "Bognor Regis", "Littlehampton", "Haywards Heath", "Burgess Hill", "East Grinstead", "Shoreham-by-Sea", "Arundel", "Midhurst", "Petworth", "Selsey", "Steyning"],
 ["Brighton", "Lewes", "Eastbourne", "Hastings", "Guildford"])
board("Towns in Greater Manchester", G, "medium", ["Greater Manchester", "towns", "England"],
 ["Bolton", "Wigan", "Stockport", "Oldham", "Rochdale", "Bury", "Salford", "Altrincham", "Sale", "Ashton-under-Lyne", "Stalybridge", "Leigh", "Middleton", "Hyde", "Denton"],
 ["Warrington", "St Helens", "Blackburn", "Macclesfield", "Burnley"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-58.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
