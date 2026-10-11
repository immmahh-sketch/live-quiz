# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-64.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("Towns in Stirling, Falkirk and Clackmannanshire", "UK geography", "medium", ["Stirling", "Falkirk", "Scotland"],
 ["Stirling", "Falkirk", "Grangemouth", "Alloa", "Callander", "Dunblane", "Bridge of Allan", "Larbert", "Stenhousemuir", "Bo'ness", "Denny", "Polmont", "Tillicoultry", "Dollar", "Killin"],
 ["Kinross", "Linlithgow", "Cumbernauld", "Crieff", "Auchterarder"])
board("Places in the Western Isles, Orkney or Shetland", "UK geography", "hard", ["Scottish islands", "Orkney", "Shetland"],
 ["Stornoway", "Tarbert", "Castlebay", "Balivanich", "Lochmaddy", "Kirkwall", "Stromness", "St Margaret's Hope", "Dounby", "Lerwick", "Scalloway", "Brae", "Sumburgh", "Baltasound", "Leverburgh"],
 ["Portree", "Tobermory", "Thurso", "Oban", "Ullapool"])
board("Towns in the Vale of Glamorgan or Bridgend", "UK geography", "hard", ["South Wales", "Glamorgan", "towns"],
 ["Barry", "Penarth", "Cowbridge", "Llantwit Major", "Dinas Powys", "Rhoose", "Bridgend", "Porthcawl", "Maesteg", "Pencoed", "Ogmore-by-Sea", "St Athan", "Sully", "Pyle", "Kenfig Hill"],
 ["Cardiff", "Pontypridd", "Port Talbot", "Caerphilly", "Neath"])
board("Towns in the South Wales Valleys", "UK geography", "medium", ["South Wales", "Valleys", "towns"],
 ["Pontypridd", "Aberdare", "Mountain Ash", "Treorchy", "Tonypandy", "Porth", "Merthyr Tydfil", "Caerphilly", "Bargoed", "Ystrad Mynach", "Ebbw Vale", "Tredegar", "Abertillery", "Pontypool", "Blaenavon"],
 ["Swansea", "Neath", "Abergavenny", "Brecon", "Barry"])
board("Towns in the East Riding of Yorkshire (not Hull)", "UK geography", "medium", ["East Yorkshire", "Yorkshire", "towns"],
 ["Beverley", "Bridlington", "Goole", "Driffield", "Hornsea", "Withernsea", "Cottingham", "Hessle", "Pocklington", "Howden", "Hedon", "Market Weighton", "Brough", "Flamborough", "Patrington"],
 ["Filey", "Scarborough", "Hull", "Selby", "Malton"])
board("Places in Swansea or Neath Port Talbot", "UK geography", "hard", ["South Wales", "Swansea", "towns"],
 ["Neath", "Port Talbot", "Briton Ferry", "Pontardawe", "Glynneath", "Resolven", "Swansea", "Mumbles", "Gorseinon", "Pontarddulais", "Clydach", "Gowerton", "Morriston", "Sketty", "Baglan"],
 ["Llanelli", "Ammanford", "Bridgend", "Maesteg", "Kidwelly"])
board("Places on the Isle of Man", "UK geography", "medium", ["Isle of Man", "islands"],
 ["Douglas", "Ramsey", "Peel", "Castletown", "Port Erin", "Port St Mary", "Onchan", "Laxey", "Ballasalla", "Kirk Michael", "Union Mills", "Foxdale", "Santon", "Ballaugh", "Sulby"],
 ["Whitehaven", "Heysham", "Portpatrick", "Workington", "Silloth"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-64.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
