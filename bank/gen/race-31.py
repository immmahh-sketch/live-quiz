# Bank session 10 Oct 2026: 4 more general races -> bank/race-31.json. 20 rows each, target 10; wrong options are
# the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("which club did this legend spend most of his career at?", "Football", "medium", ["football", "legends", "clubs"], [
 ("Paolo Maldini", "AC Milan", ["Lazio", "Napoli", "Fiorentina"]), ("Francesco Totti", "Roma", ["Lazio", "Napoli", "Fiorentina"]),
 ("Ryan Giggs", "Manchester United", ["Manchester City", "Everton", "Aston Villa"]), ("Steven Gerrard", "Liverpool", ["Everton", "Aston Villa", "Manchester City"]),
 ("Carles Puyol", "Barcelona", ["Valencia", "Sevilla", "Atlético Madrid"]), ("Matt Le Tissier", "Southampton", ["Portsmouth", "Ipswich Town", "Norwich City"]),
 ("Tony Adams", "Arsenal", ["Everton", "Aston Villa", "Ipswich Town"]), ("Alan Shearer", "Newcastle United", ["Blackburn Rovers", "Sunderland", "Middlesbrough"]),
 ("John Terry", "Chelsea", ["Fulham", "Aston Villa", "Everton"]), ("Ledley King", "Tottenham Hotspur", ["Fulham", "Charlton Athletic", "Crystal Palace"]),
 ("Iker Casillas", "Real Madrid", ["Atlético Madrid", "Valencia", "Sevilla"]), ("Thomas Müller", "Bayern Munich", ["Schalke", "Bayer Leverkusen", "Hamburg"]),
 ("Javier Zanetti", "Inter Milan", ["Lazio", "Napoli", "Fiorentina"]), ("Marco Reus", "Borussia Dortmund", ["Schalke", "Bayer Leverkusen", "Hamburg"]),
 ("Jamie Vardy", "Leicester City", ["Nottingham Forest", "Derby County", "Sheffield United"]), ("Mark Noble", "West Ham United", ["Fulham", "Charlton Athletic", "Crystal Palace"]),
 ("Billy Bremner", "Leeds United", ["Sheffield Wednesday", "Huddersfield Town", "Bradford City"]), ("Gianluigi Buffon", "Juventus", ["Lazio", "Torino", "Fiorentina"]),
 ("Billy McNeill", "Celtic", ["Aberdeen", "Hearts", "Hibernian"]), ("Eusébio", "Benfica", ["Porto", "Sporting Lisbon", "Braga"])])

race("which language gave English this word?", "Words and language", "hard", ["words", "etymology", "languages"], [
 ("Kindergarten", "German", ["Danish", "Polish", "Hungarian"]), ("Bungalow", "Hindi", ["Tamil", "Malay", "Korean"]),
 ("Tsunami", "Japanese", ["Korean", "Mandarin", "Malay"]), ("Robot", "Czech", ["Polish", "Russian", "Hungarian"]),
 ("Algebra", "Arabic", ["Greek", "Latin", "Hebrew"]), ("Yacht", "Dutch", ["Danish", "Portuguese", "Polish"]),
 ("Ski", "Norwegian", ["Danish", "Polish", "Russian"]), ("Kayak", "Inuit", ["Maori", "Korean", "Sami"]),
 ("Boomerang", "an Aboriginal Australian language", ["Maori", "Samoan", "Malay"]), ("Tomato", "Nahuatl (Aztec)", ["Quechua", "Portuguese", "Latin"]),
 ("Mosquito", "Spanish", ["Latin", "Greek", "Hebrew"]), ("Piano", "Italian", ["Latin", "Greek", "Portuguese"]),
 ("Ballet", "French", ["Latin", "Greek", "Portuguese"]), ("Safari", "Swahili", ["Zulu", "Malay", "Hebrew"]),
 ("Sauna", "Finnish", ["Hungarian", "Russian", "Icelandic"]), ("Slogan", "Scottish Gaelic", ["Welsh", "Icelandic", "Latin"]),
 ("Smorgasbord", "Swedish", ["Danish", "Icelandic", "Polish"]), ("Taboo", "Tongan", ["Malay", "Korean", "Zulu"]),
 ("Ukulele", "Hawaiian", ["Malay", "Maori", "Samoan"]), ("Bazaar", "Persian", ["Hebrew", "Greek", "Latin"])])

race("which war was this battle part of?", "History", "hard", ["battles", "wars"], [
 ("Hastings", "The Norman Conquest", ["The Crusades", "The Anarchy", "The Barons' War"]), ("Agincourt", "The Hundred Years' War", ["The Seven Years' War", "The Thirty Years' War", "The Crusades"]),
 ("Bosworth", "The Wars of the Roses", ["The Anarchy", "The Barons' War", "The Seven Years' War"]), ("Naseby", "The English Civil War", ["The Thirty Years' War", "The Seven Years' War", "The Glorious Revolution"]),
 ("Culloden", "The Jacobite rising", ["The Seven Years' War", "The Thirty Years' War", "The Glorious Revolution"]), ("Waterloo", "The Napoleonic Wars", ["The Peninsular War", "The Franco-Prussian War", "The Seven Years' War"]),
 ("Gettysburg", "The American Civil War", ["The War of 1812", "The Mexican–American War", "The Spanish–American War"]), ("Bunker Hill", "The American War of Independence", ["The War of 1812", "The Seven Years' War", "The Mexican–American War"]),
 ("Balaclava", "The Crimean War", ["The Franco-Prussian War", "The Russo-Japanese War", "The Opium Wars"]), ("Rorke's Drift", "The Anglo-Zulu War", ["The Opium Wars", "The Mahdist War", "The Indian Mutiny"]),
 ("The Siege of Mafeking", "The Boer War", ["The Mahdist War", "The Indian Mutiny", "The Russo-Japanese War"]), ("The Somme", "The First World War", ["The Franco-Prussian War", "The Spanish Civil War", "The Russo-Japanese War"]),
 ("Stalingrad", "The Second World War", ["The Spanish Civil War", "The Russo-Japanese War", "The Winter War"]), ("Inchon", "The Korean War", ["The Russo-Japanese War", "The Winter War", "The Iraq War"]),
 ("The Tet Offensive", "The Vietnam War", ["The Iraq War", "The Afghan War", "The Russo-Japanese War"]), ("Goose Green", "The Falklands War", ["The Iraq War", "The Afghan War", "The Suez Crisis"]),
 ("Bannockburn", "The Scottish Wars of Independence", ["The Crusades", "The Anarchy", "The Barons' War"]), ("Thermopylae", "The Greco-Persian Wars", ["The Peloponnesian War", "The Punic Wars", "The Trojan War"]),
 ("The Alamo", "The Texas Revolution", ["The Mexican–American War", "The War of 1812", "The Spanish–American War"]), ("Operation Desert Storm", "The Gulf War", ["The Iraq War", "The Afghan War", "The Suez Crisis"])])

race("who was on the English or British throne when this happened?", "History", "hard", ["monarchs", "kings and queens"], [
 ("The Domesday Book is compiled", "William I", ["William II", "Henry I", "Stephen"]), ("Thomas Becket is murdered", "Henry II", ["Stephen", "Richard I", "Henry I"]),
 ("Magna Carta is sealed", "John", ["Richard I", "Henry III", "Edward I"]), ("The Black Death reaches England", "Edward III", ["Edward I", "Edward II", "Henry IV"]),
 ("The Peasants' Revolt", "Richard II", ["Edward II", "Henry IV", "Henry VI"]), ("The Battle of Agincourt", "Henry V", ["Henry IV", "Henry VI", "Edward IV"]),
 ("Columbus reaches the Americas", "Henry VII", ["Richard III", "Edward IV", "Henry VIII"]), ("The first Book of Common Prayer", "Edward VI", ["Henry VIII", "Mary I", "Richard III"]),
 ("The Spanish Armada", "Elizabeth I", ["Mary I", "Henry VIII", "Charles I"]), ("The Gunpowder Plot", "James I", ["Charles I", "Mary I", "James II"]),
 ("The Great Fire of London", "Charles II", ["Charles I", "James II", "George I"]), ("The Battle of the Boyne", "William III", ["Charles I", "George I", "Mary I"]),
 ("The Act of Union with Scotland", "Anne", ["George I", "Mary II", "James II"]), ("The Battle of Culloden", "George II", ["George I", "George IV", "James II"]),
 ("The Battle of Trafalgar", "George III", ["George IV", "George I", "Edward VII"]), ("The Great Reform Act", "William IV", ["George IV", "Edward VII", "George I"]),
 ("The Great Exhibition", "Victoria", ["Edward VII", "George IV", "Edward VIII"]), ("The Titanic sinks", "George V", ["Edward VII", "Edward VIII", "George IV"]),
 ("The Battle of Britain", "George VI", ["Edward VIII", "Edward VII", "Charles III"]), ("The first Moon landing", "Elizabeth II", ["Charles III", "Edward VIII", "Edward VII"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-31.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
