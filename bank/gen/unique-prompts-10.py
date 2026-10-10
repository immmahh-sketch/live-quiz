# Bank session 10 Oct 2026: 20 more Only One prompts appended to bank/unique-prompts.json. Each is a closed list with
# every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a country that shares a land border with Thailand or Vietnam", ["Myanmar/Burma", "Laos", "Cambodia", "Malaysia", "China"]),
 ("Name a country that shares a land border with Kenya or Ethiopia", ["Ethiopia", "Kenya", "Somalia", "South Sudan", "Uganda", "Tanzania", "Eritrea", "Djibouti", "Sudan"]),
 ("Name a country that shares a land border with Mexico or Colombia", ["United States/USA", "Guatemala", "Belize", "Panama", "Venezuela", "Brazil", "Peru", "Ecuador"]),
 ("Name a country that shares a land border with Egypt or Libya", ["Libya", "Egypt", "Sudan", "Israel", "Palestine/Gaza", "Tunisia", "Algeria", "Niger", "Chad"]),
 ("Name a Shakespeare play set mainly in Italy or ancient Rome", ["Romeo and Juliet", "The Merchant of Venice", "Othello", "The Two Gentlemen of Verona", "The Taming of the Shrew", "Much Ado About Nothing", "Julius Caesar", "Coriolanus", "Titus Andronicus"]),
 ("Name a member of Led Zeppelin, Pink Floyd or Genesis", ["Robert Plant", "Jimmy Page", "John Paul Jones", "John Bonham", "Syd Barrett", "Roger Waters", "David Gilmour", "Richard Wright/Rick Wright", "Nick Mason", "Peter Gabriel", "Phil Collins", "Tony Banks", "Mike Rutherford", "Steve Hackett", "Anthony Phillips", "Ray Wilson"]),
 ("Name one of the 'Big Four' accountancy firms or the 'Big Four' UK supermarkets", ["Deloitte", "PwC/PricewaterhouseCoopers", "EY/Ernst & Young", "KPMG", "Tesco", "Sainsbury's", "Asda", "Morrisons"]),
 ("Name a UK Chancellor of the Exchequer from 1997 to 2025", ["Gordon Brown", "Alistair Darling", "George Osborne", "Philip Hammond", "Sajid Javid", "Rishi Sunak", "Nadhim Zahawi", "Kwasi Kwarteng", "Jeremy Hunt", "Rachel Reeves"]),
 ("Name a UK Home Secretary from 2010 to the end of 2025", ["Theresa May", "Amber Rudd", "Sajid Javid", "Priti Patel", "Suella Braverman", "Grant Shapps", "James Cleverly", "Yvette Cooper", "Shabana Mahmood"]),
 ("Name a winner of BBC Sports Personality of the Year from 2000 to 2024", ["Steve Redgrave", "David Beckham", "Paula Radcliffe", "Jonny Wilkinson", "Kelly Holmes", "Andrew Flintoff/Freddie Flintoff", "Zara Phillips/Zara Tindall", "Joe Calzaghe", "Chris Hoy", "Ryan Giggs", "Tony McCoy/AP McCoy", "Mark Cavendish", "Bradley Wiggins", "Andy Murray", "Lewis Hamilton", "Mo Farah", "Geraint Thomas", "Ben Stokes", "Emma Raducanu", "Beth Mead", "Mary Earps", "Luke Littler"]),
 ("Name a country that has won the Women's World Cup or the Women's Euros, up to 2025", ["United States/USA", "Norway", "Germany", "Japan", "Spain", "Sweden", "Netherlands/The Netherlands", "England"]),
 ("Name a US state with a coast on the Gulf of Mexico or one of the Great Lakes", ["Texas", "Louisiana", "Mississippi", "Alabama", "Florida", "Minnesota", "Wisconsin", "Illinois", "Indiana", "Michigan", "Ohio", "Pennsylvania", "New York"]),
 ("Name a leader who sat at the Yalta or Potsdam conference in 1945", ["Winston Churchill/Churchill", "Franklin D. Roosevelt/Roosevelt/FDR", "Joseph Stalin/Stalin", "Harry Truman/Truman", "Clement Attlee/Attlee"]),
 ("Name a country that has hosted the Commonwealth Games", ["Canada", "England", "Australia", "New Zealand", "Wales", "Jamaica", "Scotland", "Malaysia", "India"]),
 ("Name a country that has hosted or co-hosted the men's Rugby World Cup", ["New Zealand", "Australia", "England", "Wales", "Scotland", "Ireland", "France", "South Africa", "Japan"]),
 ("Name one of The Golden Girls or the four friends in Sex and the City", ["Dorothy", "Rose", "Blanche", "Sophia", "Carrie", "Samantha", "Charlotte", "Miranda"]),
 ("Name an independent country with exactly five letters in its usual English name", ["Benin", "Chile", "China", "Congo", "Egypt", "Gabon", "Ghana", "Haiti", "India", "Italy", "Japan", "Kenya", "Libya", "Malta", "Nauru", "Nepal", "Niger", "Palau", "Qatar", "Samoa", "Spain", "Sudan", "Syria", "Tonga", "Yemen"]),
 ("Name an independent country with exactly four letters in its usual English name", ["Chad", "Cuba", "Fiji", "Iran", "Iraq", "Laos", "Mali", "Oman", "Peru", "Togo"]),
 ("Name a Formula One team that won the constructors' title from 2000 to 2025", ["Ferrari", "Renault", "McLaren", "Brawn/Brawn GP", "Red Bull", "Mercedes"]),
 ("Name a UK city that has been a European Capital of Culture or UK City of Culture", ["Glasgow", "Liverpool", "Derry/Londonderry/Derry~Londonderry", "Hull/Kingston upon Hull", "Coventry", "Bradford"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
