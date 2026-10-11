# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-61.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("Towns in the Scottish Borders", "UK geography", "medium", ["Scottish Borders", "Scotland", "towns"],
 ["Hawick", "Galashiels", "Peebles", "Kelso", "Jedburgh", "Selkirk", "Melrose", "Duns", "Eyemouth", "Innerleithen", "Coldstream", "Lauder", "St Boswells", "Earlston", "Newcastleton"],
 ["Berwick-upon-Tweed", "Dunbar", "Moffat", "Biggar", "Penicuik"])
board("Towns in Dumfries and Galloway", "UK geography", "medium", ["Dumfries and Galloway", "Scotland", "towns"],
 ["Dumfries", "Stranraer", "Annan", "Castle Douglas", "Kirkcudbright", "Newton Stewart", "Lockerbie", "Moffat", "Dalbeattie", "Gretna", "Langholm", "Sanquhar", "Wigtown", "Thornhill", "Gatehouse of Fleet"],
 ["Girvan", "Carlisle", "Hawick", "Cumnock", "Longtown"])
board("Towns in Lanarkshire (North or South)", "UK geography", "medium", ["Lanarkshire", "Scotland", "towns"],
 ["Hamilton", "Motherwell", "Wishaw", "East Kilbride", "Airdrie", "Coatbridge", "Cumbernauld", "Lanark", "Carluke", "Bellshill", "Uddingston", "Larkhall", "Strathaven", "Biggar", "Blantyre"],
 ["Paisley", "Falkirk", "Livingston", "Kilmarnock", "Kirkintilloch"])
board("Towns and villages in Perth and Kinross", "UK geography", "hard", ["Perth and Kinross", "Perthshire", "Scotland"],
 ["Perth", "Pitlochry", "Crieff", "Auchterarder", "Blairgowrie", "Kinross", "Aberfeldy", "Dunkeld", "Coupar Angus", "Alyth", "Comrie", "Milnathort", "Bridge of Earn", "Scone", "Blair Atholl"],
 ["Callander", "Killin", "Forfar", "Dollar", "Dunblane"])
board("Towns in Carmarthenshire", "UK geography", "hard", ["Carmarthenshire", "Wales", "towns"],
 ["Carmarthen", "Llanelli", "Ammanford", "Burry Port", "Kidwelly", "Laugharne", "Llandeilo", "Llandovery", "Newcastle Emlyn", "St Clears", "Whitland", "Pembrey", "Ferryside", "Llangennech", "Cross Hands"],
 ["Tenby", "Swansea", "Cardigan", "Neath", "Lampeter"])
board("Towns in Powys", "UK geography", "medium", ["Powys", "Wales", "towns"],
 ["Brecon", "Builth Wells", "Llandrindod Wells", "Newtown", "Welshpool", "Machynlleth", "Llanidloes", "Knighton", "Presteigne", "Rhayader", "Hay-on-Wye", "Crickhowell", "Ystradgynlais", "Talgarth", "Llanwrtyd Wells"],
 ["Abergavenny", "Ludlow", "Oswestry", "Aberystwyth", "Merthyr Tydfil"])
board("Towns and villages in County Tyrone", "UK geography", "hard", ["County Tyrone", "Northern Ireland", "towns"],
 ["Omagh", "Dungannon", "Cookstown", "Strabane", "Coalisland", "Castlederg", "Fintona", "Newtownstewart", "Augher", "Clogher", "Fivemiletown", "Moy", "Pomeroy", "Sixmilecross", "Ballygawley"],
 ["Enniskillen", "Magherafelt", "Armagh", "Lifford", "Limavady"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-61.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
