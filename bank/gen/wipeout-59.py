# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-59.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("Towns in Warwickshire", "UK geography", "medium", ["Warwickshire", "towns", "Midlands"],
 ["Warwick", "Leamington Spa", "Stratford-upon-Avon", "Rugby", "Nuneaton", "Bedworth", "Kenilworth", "Atherstone", "Alcester", "Southam", "Shipston-on-Stour", "Coleshill", "Polesworth", "Henley-in-Arden", "Kineton"],
 ["Banbury", "Evesham", "Daventry", "Hinckley", "Tamworth"])
board("Towns and villages in Herefordshire", "UK geography", "hard", ["Herefordshire", "towns", "villages"],
 ["Hereford", "Leominster", "Ross-on-Wye", "Ledbury", "Bromyard", "Kington", "Weobley", "Pembridge", "Eardisland", "Colwall", "Credenhill", "Fownhope", "Wigmore", "Peterchurch", "Madley"],
 ["Hay-on-Wye", "Monmouth", "Ludlow", "Tewkesbury", "Great Malvern"])
board("Towns in Bedfordshire", "UK geography", "medium", ["Bedfordshire", "towns"],
 ["Bedford", "Luton", "Dunstable", "Leighton Buzzard", "Biggleswade", "Sandy", "Flitwick", "Ampthill", "Kempston", "Houghton Regis", "Shefford", "Potton", "Stotfold", "Arlesey", "Woburn"],
 ["Hitchin", "Milton Keynes", "St Neots", "Letchworth", "Rushden"])
board("Towns in the West Midlands county", "UK geography", "medium", ["West Midlands", "Black Country", "towns"],
 ["Birmingham", "Coventry", "Wolverhampton", "Solihull", "Walsall", "West Bromwich", "Dudley", "Sutton Coldfield", "Stourbridge", "Halesowen", "Oldbury", "Smethwick", "Wednesbury", "Bilston", "Willenhall"],
 ["Redditch", "Bromsgrove", "Tamworth", "Lichfield", "Cannock"])
board("Towns on Merseyside", "UK geography", "medium", ["Merseyside", "towns", "Liverpool"],
 ["Liverpool", "Birkenhead", "St Helens", "Southport", "Bootle", "Wallasey", "Crosby", "Kirkby", "Huyton", "Prescot", "Formby", "Maghull", "Newton-le-Willows", "Heswall", "Hoylake"],
 ["Widnes", "Runcorn", "Ormskirk", "Skelmersdale", "Ellesmere Port"])
board("Places on the Isle of Wight", "UK geography", "medium", ["Isle of Wight", "islands", "towns"],
 ["Newport", "Ryde", "Cowes", "East Cowes", "Sandown", "Shanklin", "Ventnor", "Yarmouth", "Freshwater", "Bembridge", "Brading", "Godshill", "Totland", "Seaview", "Niton"],
 ["Lymington", "Southsea", "Hythe", "Lyndhurst", "Christchurch"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-59.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
