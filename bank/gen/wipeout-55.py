# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-55.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

G = "UK geography"
board("Towns in Lancashire (not Yorkshire)", G, "medium", ["Lancashire", "towns", "England"],
 ["Blackpool", "Preston", "Lancaster", "Burnley", "Blackburn", "Accrington", "Morecambe", "Fleetwood", "Chorley", "Clitheroe", "Lytham St Annes", "Ormskirk", "Colne", "Nelson", "Darwen"],
 ["Halifax", "Huddersfield", "Skipton", "Harrogate", "Keighley"])
board("Towns in Cumbria", G, "medium", ["Cumbria", "Lake District", "towns"],
 ["Carlisle", "Kendal", "Keswick", "Penrith", "Workington", "Whitehaven", "Barrow-in-Furness", "Windermere", "Ambleside", "Cockermouth", "Ulverston", "Maryport", "Appleby", "Grasmere", "Sedbergh"],
 ["Hexham", "Alnwick", "Darlington", "Lancaster", "Richmond"])
board("Towns in Kent (not Sussex or Essex)", G, "medium", ["Kent", "towns", "England"],
 ["Canterbury", "Dover", "Folkestone", "Maidstone", "Margate", "Ramsgate", "Ashford", "Tunbridge Wells", "Sevenoaks", "Whitstable", "Faversham", "Deal", "Sandwich", "Gravesend", "Chatham"],
 ["Hastings", "Rye", "Brighton", "Chelmsford", "Southend-on-Sea"])
board("Towns in Norfolk (not Suffolk)", G, "hard", ["Norfolk", "East Anglia", "towns"],
 ["Norwich", "King's Lynn", "Great Yarmouth", "Cromer", "Sheringham", "Thetford", "Dereham", "Swaffham", "Hunstanton", "Wells-next-the-Sea", "Diss", "Wymondham", "Fakenham", "Aylsham", "Holt"],
 ["Ipswich", "Lowestoft", "Southwold", "Aldeburgh", "Bury St Edmunds"])
board("Towns in Essex", G, "medium", ["Essex", "towns", "England"],
 ["Chelmsford", "Colchester", "Southend-on-Sea", "Basildon", "Harlow", "Brentwood", "Clacton-on-Sea", "Saffron Walden", "Braintree", "Maldon", "Billericay", "Epping", "Harwich", "Witham", "Frinton-on-Sea"],
 ["Watford", "St Albans", "Luton", "Ipswich", "Cambridge"])
board("Rivers in Scotland (not England)", G, "medium", ["Scotland", "rivers"],
 ["Tay", "Spey", "Clyde", "Forth", "Tweed", "Dee", "Don", "Ness", "Nith", "Annan", "Deveron", "Findhorn", "Lochy", "Awe", "Leven"],
 ["Wear", "Tees", "Severn", "Trent", "Mersey"])
board("Places on Teesside (not Wearside or Tyneside)", "North East England", "medium", ["Teesside", "North East", "towns"],
 ["Middlesbrough", "Stockton-on-Tees", "Redcar", "Billingham", "Thornaby", "Guisborough", "Marske", "Saltburn", "Yarm", "Eston", "Ingleby Barwick", "Norton", "Ormesby", "Nunthorpe", "Coulby Newham"],
 ["Sunderland", "Washington", "Gateshead", "Jarrow", "South Shields"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-55.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
