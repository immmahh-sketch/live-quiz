# Bank session 9 Oct 2026 (second pass): 21 more Only One prompts appended to bank/unique-prompts.json. Each is a
# closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a day of the week or a month of the year", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]),
 ("Name a primary or secondary colour in painting", ["Red", "Yellow", "Blue", "Green", "Orange", "Purple/Violet"]),
 ("Name an actor who has played James Bond or M in an official Bond film", ["Sean Connery", "George Lazenby", "Roger Moore", "Timothy Dalton", "Pierce Brosnan", "Daniel Craig", "Bernard Lee", "Robert Brown", "Judi Dench", "Ralph Fiennes"]),
 ("Name a Harry Potter book", ["Harry Potter and the Philosopher's Stone/Philosopher's Stone/Sorcerer's Stone", "Harry Potter and the Chamber of Secrets/Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban/Prisoner of Azkaban", "Harry Potter and the Goblet of Fire/Goblet of Fire", "Harry Potter and the Order of the Phoenix/Order of the Phoenix", "Harry Potter and the Half-Blood Prince/Half-Blood Prince", "Harry Potter and the Deathly Hallows/Deathly Hallows"]),
 ("Name one of Peter Jackson's Lord of the Rings or Hobbit films", ["The Fellowship of the Ring/Fellowship of the Ring", "The Two Towers/Two Towers", "The Return of the King/Return of the King", "An Unexpected Journey", "The Desolation of Smaug/Desolation of Smaug", "The Battle of the Five Armies/Battle of the Five Armies"]),
 ("Name a UK coin or Bank of England note in use in 2026", ["1p/One penny/Penny", "2p/Two pence", "5p/Five pence", "10p/Ten pence", "20p/Twenty pence", "50p/Fifty pence", "£1/One pound/Pound coin", "£2/Two pounds", "£5/Five-pound note/Fiver", "£10/Ten-pound note/Tenner", "£20/Twenty-pound note", "£50/Fifty-pound note"]),
 ("Name a vowel, or a letter worth 10 points in English Scrabble", ["A", "E", "I", "O", "U", "Q", "Z"]),
 ("Name a US state whose name is two words", ["New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "South Carolina", "South Dakota", "West Virginia", "Rhode Island"]),
 ("Name a country whose English name ends in -land", ["England", "Scotland", "Ireland", "Northern Ireland", "Finland", "Iceland", "Poland", "Switzerland", "Thailand", "New Zealand", "Swaziland"]),
 ("Name one of the long bones in the human arm or leg", ["Humerus", "Radius", "Ulna", "Femur/Thigh bone", "Tibia/Shin bone/Shinbone", "Fibula"]),
 ("Name an ABO blood group, or one of the four chambers of the heart (say left or right)", ["A", "B", "AB", "O", "Left atrium", "Right atrium", "Left ventricle", "Right ventricle"]),
 ("Name one of Britain's five Classic flat races, or the Grand National", ["2000 Guineas/Two Thousand Guineas", "1000 Guineas/One Thousand Guineas", "The Derby/Derby/Epsom Derby", "The Oaks/Oaks/Epsom Oaks", "St Leger/St. Leger", "Grand National/The Grand National"]),
 ("Name a child or grandchild of King Charles III", ["Prince William/William", "Prince Harry/Harry", "Prince George/George", "Princess Charlotte/Charlotte", "Prince Louis/Louis", "Prince Archie/Archie", "Princess Lilibet/Lilibet/Lili"]),
 ("Name a move in rock, paper, scissors, or a mark in noughts and crosses", ["Rock/Stone", "Paper", "Scissors", "Nought/O/Zero", "Cross/X"]),
 ("Name the colour of a ball used in snooker", ["Red", "Yellow", "Green", "Brown", "Blue", "Pink", "Black", "White/Cue ball"]),
 ("Name a playing position in netball", ["Goal Shooter/GS", "Goal Attack/GA", "Wing Attack/WA", "Centre/C", "Wing Defence/WD", "Goal Defence/GD", "Goal Keeper/Goalkeeper/GK"]),
 ("Name one of the five council areas of Tyne and Wear, or a county that borders it", ["Newcastle upon Tyne/Newcastle", "Gateshead", "North Tyneside", "South Tyneside", "Sunderland", "Northumberland", "County Durham/Durham"]),
 ("Name one of the seven bridges across the Tyne between Newcastle and Gateshead", ["Tyne Bridge", "Swing Bridge", "High Level Bridge", "Gateshead Millennium Bridge/Millennium Bridge/Blinking Eye Bridge", "Queen Elizabeth II Metro Bridge/Queen Elizabeth II Bridge/Metro Bridge", "King Edward VII Bridge/King Edward Bridge", "Redheugh Bridge"]),
 ("Name a country with a Black Sea coastline", ["Turkey/Türkiye", "Bulgaria", "Romania", "Ukraine", "Russia", "Georgia"]),
 ("Name a country the River Danube flows through", ["Germany", "Austria", "Slovakia", "Hungary", "Croatia", "Serbia", "Romania", "Bulgaria", "Moldova", "Ukraine"]),
 ("Name one of the Channel Islands", ["Jersey", "Guernsey", "Alderney", "Sark", "Herm", "Brecqhou", "Jethou", "Lihou"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
