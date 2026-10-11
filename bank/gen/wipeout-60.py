# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-60.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("Towns in Fife", "UK geography", "medium", ["Fife", "Scotland", "towns"],
 ["Dunfermline", "Kirkcaldy", "Glenrothes", "St Andrews", "Cupar", "Leven", "Methil", "Burntisland", "Kinghorn", "Rosyth", "Inverkeithing", "Cowdenbeath", "Lochgelly", "Anstruther", "Crail"],
 ["Dundee", "Perth", "Kinross", "Falkirk", "Alloa"])
board("Towns in Ayrshire", "UK geography", "medium", ["Ayrshire", "Scotland", "towns"],
 ["Ayr", "Kilmarnock", "Irvine", "Troon", "Prestwick", "Largs", "Saltcoats", "Ardrossan", "Girvan", "Cumnock", "Maybole", "Stevenston", "Kilwinning", "Dalry", "Stewarton"],
 ["Paisley", "Greenock", "Stranraer", "Hamilton", "Gourock"])
board("Towns in Aberdeenshire (not the city of Aberdeen)", "UK geography", "hard", ["Aberdeenshire", "Scotland", "towns"],
 ["Peterhead", "Fraserburgh", "Inverurie", "Stonehaven", "Ellon", "Banff", "Huntly", "Turriff", "Westhill", "Portlethen", "Banchory", "Ballater", "Macduff", "Oldmeldrum", "Laurencekirk"],
 ["Elgin", "Forres", "Montrose", "Arbroath", "Buckie"])
board("Towns and villages in Pembrokeshire", "UK geography", "hard", ["Pembrokeshire", "Wales", "towns"],
 ["Haverfordwest", "Pembroke", "Pembroke Dock", "Milford Haven", "Tenby", "Fishguard", "St Davids", "Narberth", "Saundersfoot", "Neyland", "Goodwick", "Solva", "Manorbier", "Amroth", "Little Haven"],
 ["Cardigan", "Carmarthen", "Aberaeron", "Laugharne", "Llanelli"])
board("Towns in Gwynedd", "UK geography", "medium", ["Gwynedd", "Wales", "towns"],
 ["Caernarfon", "Bangor", "Pwllheli", "Porthmadog", "Dolgellau", "Bala", "Barmouth", "Criccieth", "Blaenau Ffestiniog", "Harlech", "Tywyn", "Bethesda", "Llanberis", "Abersoch", "Nefyn"],
 ["Llandudno", "Conwy", "Holyhead", "Beaumaris", "Betws-y-Coed"])
board("Towns in County Antrim (leave out Belfast)", "UK geography", "medium", ["County Antrim", "Northern Ireland", "towns"],
 ["Ballymena", "Antrim", "Larne", "Carrickfergus", "Ballymoney", "Ballycastle", "Newtownabbey", "Portrush", "Bushmills", "Ballyclare", "Randalstown", "Cushendall", "Crumlin", "Glenarm", "Whitehead"],
 ["Coleraine", "Portstewart", "Bangor", "Cookstown", "Newry"])
board("Towns in County Down", "UK geography", "medium", ["County Down", "Northern Ireland", "towns"],
 ["Bangor", "Newtownards", "Downpatrick", "Newcastle", "Holywood", "Comber", "Banbridge", "Ballynahinch", "Dundrum", "Kilkeel", "Warrenpoint", "Donaghadee", "Portaferry", "Dromore", "Saintfield"],
 ["Larne", "Armagh", "Lurgan", "Portadown", "Carrickfergus"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-60.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
