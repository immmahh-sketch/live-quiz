# Bank session 9 Oct 2026 (third pass): more Picture Reveal faces -> bank/reveal-people-4.json
# (Wikipedia title, accepted answers, difficulty). Nobody already in the live bank; mostly people whose Wikipedia lead
# photo is a portrait. Stock with PEOPLE=bank/reveal-people-4.json node tools/reveal-stock.mjs, then contact-sheet them.
import json, os
P = [
 # film and TV drama
 ("Julie Andrews", ["Julie Andrews"], "medium"), ("Kenneth Branagh", ["Kenneth Branagh", "Branagh"], "medium"), ("Jim Broadbent", ["Jim Broadbent", "Broadbent"], "hard"),
 ("Timothy Spall", ["Timothy Spall", "Spall"], "hard"), ("Brenda Blethyn", ["Brenda Blethyn", "Blethyn"], "medium"), ("Jodie Whittaker", ["Jodie Whittaker", "Whittaker"], "medium"),
 ("Peter Capaldi", ["Peter Capaldi", "Capaldi"], "medium"), ("Matt Smith (actor)", ["Matt Smith"], "medium"), ("Karen Gillan", ["Karen Gillan", "Gillan"], "hard"),
 ("Billie Piper", ["Billie Piper", "Piper"], "medium"), ("David Suchet", ["David Suchet", "Suchet"], "medium"), ("Nicholas Lyndhurst", ["Nicholas Lyndhurst", "Lyndhurst"], "medium"),
 ("Goldie Hawn", ["Goldie Hawn", "Hawn"], "medium"), ("Kurt Russell", ["Kurt Russell"], "hard"), ("Sharon Stone", ["Sharon Stone"], "medium"),
 ("Demi Moore", ["Demi Moore"], "medium"), ("Michelle Pfeiffer", ["Michelle Pfeiffer", "Pfeiffer"], "medium"), ("Uma Thurman", ["Uma Thurman", "Thurman"], "medium"),
 ("Winona Ryder", ["Winona Ryder", "Ryder"], "hard"), ("Ben Affleck", ["Ben Affleck", "Affleck"], "medium"), ("Patrick Swayze", ["Patrick Swayze", "Swayze"], "medium"),
 ("Michael Douglas", ["Michael Douglas"], "medium"), ("Catherine Zeta-Jones", ["Catherine Zeta-Jones", "Catherine Zeta Jones", "Zeta-Jones"], "medium"), ("Rami Malek", ["Rami Malek", "Malek"], "hard"),
 ("Zac Efron", ["Zac Efron", "Efron"], "medium"), ("Channing Tatum", ["Channing Tatum", "Tatum"], "medium"), ("Austin Butler", ["Austin Butler"], "hard"),
 ("Millie Bobby Brown", ["Millie Bobby Brown"], "medium"), ("Jenna Ortega", ["Jenna Ortega", "Ortega"], "medium"), ("Steve Buscemi", ["Steve Buscemi", "Buscemi"], "hard"),
 # British TV, food and comedy
 ("Fern Britton", ["Fern Britton", "Britton"], "medium"), ("Richard Madeley", ["Richard Madeley", "Madeley"], "medium"), ("Judy Finnigan", ["Judy Finnigan", "Finnigan"], "hard"),
 ("Dale Winton", ["Dale Winton", "Winton"], "medium"), ("Les Dennis", ["Les Dennis"], "medium"), ("Bob Monkhouse", ["Bob Monkhouse", "Monkhouse"], "medium"),
 ("Brian Cox (physicist)", ["Brian Cox", "Professor Brian Cox"], "medium"), ("Jeremy Kyle", ["Jeremy Kyle", "Kyle"], "medium"), ("John Torode", ["John Torode", "Torode"], "hard"),
 ("Keith Floyd", ["Keith Floyd", "Floyd"], "hard"), ("Kevin McCloud", ["Kevin McCloud", "McCloud"], "medium"), ("Sarah Beeny", ["Sarah Beeny", "Beeny"], "medium"),
 ("Jack Dee", ["Jack Dee"], "medium"), ("Paul Merton", ["Paul Merton", "Merton"], "medium"), ("Ian Hislop", ["Ian Hislop", "Hislop"], "medium"),
 ("Frank Skinner", ["Frank Skinner", "Skinner"], "medium"), ("Victoria Wood", ["Victoria Wood"], "medium"), ("Steve Coogan", ["Steve Coogan", "Coogan", "Alan Partridge"], "medium"),
 ("Johnny Vegas", ["Johnny Vegas"], "medium"), ("Les Dawson", ["Les Dawson", "Dawson"], "medium"), ("Tommy Cooper", ["Tommy Cooper", "Cooper"], "easy"),
 ("Ken Dodd", ["Ken Dodd", "Doddy"], "medium"), ("Kenneth Williams", ["Kenneth Williams"], "hard"), ("Norman Wisdom", ["Norman Wisdom", "Wisdom"], "hard"),
 # music
 ("Billy Joel", ["Billy Joel", "Joel"], "medium"), ("Paul Simon", ["Paul Simon"], "hard"), ("Cyndi Lauper", ["Cyndi Lauper", "Lauper"], "medium"),
 ("Dusty Springfield", ["Dusty Springfield", "Springfield"], "hard"), ("Petula Clark", ["Petula Clark"], "hard"), ("Engelbert Humperdinck", ["Engelbert Humperdinck", "Engelbert"], "medium"),
 ("Roger Daltrey", ["Roger Daltrey", "Daltrey"], "hard"), ("Bryan Ferry", ["Bryan Ferry", "Ferry"], "medium"), ("Bob Geldof", ["Bob Geldof", "Geldof"], "easy"),
 ("Midge Ure", ["Midge Ure", "Ure"], "hard"), ("Mark Ronson", ["Mark Ronson", "Ronson"], "hard"), ("Gloria Gaynor", ["Gloria Gaynor", "Gaynor"], "medium"),
 # sport
 ("Bobby Charlton", ["Bobby Charlton", "Sir Bobby Charlton"], "medium"), ("Bobby Moore", ["Bobby Moore"], "medium"), ("Geoff Hurst", ["Geoff Hurst", "Hurst"], "medium"),
 ("Gordon Banks", ["Gordon Banks", "Banks"], "hard"), ("Martina Navratilova", ["Martina Navratilova", "Navratilova"], "medium"), ("Andre Agassi", ["Andre Agassi", "Agassi"], "medium"),
 ("Björn Borg", ["Björn Borg", "Bjorn Borg", "Borg"], "medium"), ("Lester Piggott", ["Lester Piggott", "Piggott"], "hard"), ("Barry McGuigan", ["Barry McGuigan", "McGuigan"], "hard"),
 # politics and public life
 ("Harold Wilson", ["Harold Wilson"], "medium"), ("Edward Heath", ["Edward Heath", "Ted Heath", "Heath"], "medium"), ("Neil Kinnock", ["Neil Kinnock", "Kinnock"], "medium"),
 ("Paddy Ashdown", ["Paddy Ashdown", "Ashdown"], "hard"), ("Nick Clegg", ["Nick Clegg", "Clegg"], "medium"), ("Ed Miliband", ["Ed Miliband", "Miliband"], "medium"),
 ("Jacob Rees-Mogg", ["Jacob Rees-Mogg", "Rees-Mogg"], "easy"), ("Michael Gove", ["Michael Gove", "Gove"], "medium"), ("John Prescott", ["John Prescott", "Prescott"], "medium"),
 ("Mo Mowlam", ["Mo Mowlam", "Mowlam"], "hard"), ("Michelle Obama", ["Michelle Obama"], "easy"), ("Hillary Clinton", ["Hillary Clinton", "Hillary"], "easy"),
 ("George W. Bush", ["George W. Bush", "George Bush", "Bush"], "easy"), ("Jimmy Carter", ["Jimmy Carter", "Carter"], "hard"), ("Kamala Harris", ["Kamala Harris", "Harris"], "medium"),
 ("Justin Trudeau", ["Justin Trudeau", "Trudeau"], "medium"), ("Jacinda Ardern", ["Jacinda Ardern", "Ardern"], "medium"),
]
# No usable Wikipedia photo: Nicholas Lyndhurst, Judy Finnigan, Dale Winton, Bob Monkhouse, Keith Floyd, Sarah Beeny, Les Dawson,
# Tommy Cooper. Stocked, then retired after the contact sheet (not a face, distant stage/event shot, or face too small):
RETIRED = {"Engelbert Humperdinck", "Kenneth Williams", "Björn Borg", "Bryan Ferry", "Geoff Hurst", "Jeremy Kyle", "Les Dennis",
           "Mark Ronson", "Midge Ure", "Norman Wisdom", "Paul Merton", "Paul Simon", "Steve Coogan", "Victoria Wood", "Edward Heath",
           "John Torode", "Jack Dee", "Roger Daltrey"}
NO_PHOTO = {"Nicholas Lyndhurst", "Judy Finnigan", "Dale Winton", "Bob Monkhouse", "Keith Floyd", "Sarah Beeny", "Les Dawson", "Tommy Cooper"}
P = [p for p in P if p[0] not in RETIRED | NO_PHOTO]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": a, "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
