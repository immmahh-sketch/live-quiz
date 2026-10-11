# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-62.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("Towns and villages in County Armagh", "UK geography", "hard", ["County Armagh", "Northern Ireland", "towns"],
 ["Armagh", "Lurgan", "Portadown", "Craigavon", "Keady", "Markethill", "Richhill", "Tandragee", "Crossmaglen", "Bessbrook", "Forkhill", "Loughgall", "Middletown", "Newtownhamilton", "Poyntzpass"],
 ["Dungannon", "Banbridge", "Monaghan", "Dundalk", "Lisburn"])
board("Towns and villages in County Fermanagh", "UK geography", "hard", ["County Fermanagh", "Northern Ireland", "towns"],
 ["Enniskillen", "Irvinestown", "Lisnaskea", "Belleek", "Kesh", "Derrygonnelly", "Newtownbutler", "Roslea", "Ederney", "Belcoo", "Tempo", "Lisbellaw", "Brookeborough", "Garrison", "Maguiresbridge"],
 ["Omagh", "Fintona", "Clones", "Ballyshannon", "Fivemiletown"])
board("Towns in County Londonderry", "UK geography", "medium", ["County Londonderry", "Northern Ireland", "towns"],
 ["Derry", "Coleraine", "Limavady", "Magherafelt", "Portstewart", "Dungiven", "Maghera", "Castledawson", "Kilrea", "Garvagh", "Draperstown", "Bellaghy", "Eglinton", "Castlerock", "Ballykelly"],
 ["Strabane", "Portrush", "Ballymoney", "Cookstown", "Buncrana"])
board("Towns and villages in Angus (not Dundee)", "UK geography", "hard", ["Angus", "Scotland", "towns"],
 ["Arbroath", "Forfar", "Montrose", "Brechin", "Carnoustie", "Kirriemuir", "Monifieth", "Edzell", "Friockheim", "Letham", "Glamis", "Newtyle", "Auchmithie", "Inverkeilor", "Ferryden"],
 ["Dundee", "Stonehaven", "Blairgowrie", "Laurencekirk", "Perth"])
board("Towns and villages in Ceredigion", "UK geography", "hard", ["Ceredigion", "Wales", "towns"],
 ["Aberystwyth", "Cardigan", "Lampeter", "Aberaeron", "New Quay", "Tregaron", "Llandysul", "Borth", "Aberporth", "Llanon", "Llanbadarn Fawr", "Bow Street", "Penparcau", "Talybont", "Devil's Bridge"],
 ["Machynlleth", "Fishguard", "Newcastle Emlyn", "Carmarthen", "Llandovery"])
board("Places on Anglesey", "UK geography", "medium", ["Anglesey", "Wales", "islands"],
 ["Holyhead", "Llangefni", "Beaumaris", "Menai Bridge", "Amlwch", "Benllech", "Rhosneigr", "Cemaes", "Newborough", "Moelfre", "Valley", "Llanfairpwllgwyngyll", "Pentraeth", "Gaerwen", "Trearddur Bay"],
 ["Bangor", "Caernarfon", "Conwy", "Llandudno", "Pwllheli"])
board("Towns and villages in Monmouthshire", "UK geography", "hard", ["Monmouthshire", "Wales", "towns"],
 ["Monmouth", "Abergavenny", "Chepstow", "Usk", "Caldicot", "Magor", "Raglan", "Tintern", "Portskewett", "Undy", "Llanfoist", "Gilwern", "Rogiet", "Trellech", "Skenfrith"],
 ["Crickhowell", "Newport", "Pontypool", "Ross-on-Wye", "Lydney"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-62.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
