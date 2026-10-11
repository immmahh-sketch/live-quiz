# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-63.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("Towns in the Lothians (East, West or Midlothian, not Edinburgh)", "UK geography", "medium", ["Lothian", "Scotland", "towns"],
 ["Haddington", "Dunbar", "North Berwick", "Musselburgh", "Prestonpans", "Tranent", "Dalkeith", "Penicuik", "Bonnyrigg", "Loanhead", "Livingston", "Bathgate", "Linlithgow", "Broxburn", "Whitburn"],
 ["Peebles", "Galashiels", "Falkirk", "Kirkcaldy", "Grangemouth"])
board("Towns in the Highland council area", "UK geography", "medium", ["Highlands", "Scotland", "towns"],
 ["Inverness", "Fort William", "Aviemore", "Thurso", "Wick", "Nairn", "Dingwall", "Ullapool", "Portree", "Kingussie", "Dornoch", "Tain", "Golspie", "Invergordon", "Alness"],
 ["Oban", "Elgin", "Pitlochry", "Stornoway", "Kirkwall"])
board("Towns and villages in Argyll and Bute", "UK geography", "hard", ["Argyll", "Scotland", "towns"],
 ["Oban", "Campbeltown", "Dunoon", "Helensburgh", "Rothesay", "Inveraray", "Lochgilphead", "Tobermory", "Bowmore", "Port Ellen", "Tighnabruaich", "Cardross", "Kilmartin", "Taynuilt", "Arrochar"],
 ["Fort William", "Largs", "Gourock", "Crianlarich", "Glencoe"])
board("Towns and villages in Moray", "UK geography", "hard", ["Moray", "Speyside", "Scotland"],
 ["Elgin", "Forres", "Buckie", "Lossiemouth", "Keith", "Fochabers", "Rothes", "Dufftown", "Aberlour", "Burghead", "Findhorn", "Cullen", "Portknockie", "Hopeman", "Tomintoul"],
 ["Nairn", "Huntly", "Banff", "Grantown-on-Spey", "Inverness"])
board("Towns in Conwy and Denbighshire", "UK geography", "medium", ["North Wales", "Conwy", "Denbighshire"],
 ["Conwy", "Llandudno", "Colwyn Bay", "Abergele", "Betws-y-Coed", "Llanrwst", "Penmaenmawr", "Rhyl", "Prestatyn", "Denbigh", "Ruthin", "St Asaph", "Llangollen", "Corwen", "Rhuddlan"],
 ["Bangor", "Mold", "Wrexham", "Holywell", "Bala"])
board("Towns and villages in Flintshire and Wrexham", "UK geography", "hard", ["North Wales", "Flintshire", "Wrexham"],
 ["Mold", "Flint", "Holywell", "Buckley", "Connah's Quay", "Shotton", "Queensferry", "Saltney", "Wrexham", "Chirk", "Gresford", "Rhosllanerchrugog", "Ruabon", "Llay", "Overton"],
 ["Chester", "Ellesmere Port", "Oswestry", "Rhyl", "Ruthin"])
board("Towns in Renfrewshire, Inverclyde and the Dunbartonshires", "UK geography", "hard", ["West of Scotland", "Clyde", "towns"],
 ["Greenock", "Gourock", "Port Glasgow", "Paisley", "Renfrew", "Johnstone", "Erskine", "Clydebank", "Dumbarton", "Alexandria", "Bearsden", "Milngavie", "Kirkintilloch", "Bishopbriggs", "Barrhead"],
 ["Largs", "Hamilton", "Cumbernauld", "Helensburgh", "Kilmarnock"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-63.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
