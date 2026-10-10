# Bank session 10 Oct 2026 (seventh pass): more Picture Reveal faces -> bank/reveal-people-8.json
# (Wikipedia title, accepted answers, difficulty). Nobody already in the live bank; mostly people whose Wikipedia lead
# photo is a portrait. Stock with PEOPLE=bank/reveal-people-8.json node tools/reveal-stock.mjs, then contact-sheet them.
import json, os
P = [
 # TV and comedy
 ("Alex Horne", ["Alex Horne", "Horne"], "medium"), ("Sue Perkins", ["Sue Perkins", "Perkins"], "medium"), ("Mel Giedroyc", ["Mel Giedroyc", "Giedroyc"], "medium"),
 ("Richard Ayoade", ["Richard Ayoade", "Ayoade"], "medium"), ("David Mitchell (comedian)", ["David Mitchell"], "medium"), ("Robert Webb", ["Robert Webb"], "medium"),
 ("Paul Whitehouse", ["Paul Whitehouse", "Whitehouse"], "medium"), ("Harry Enfield", ["Harry Enfield", "Enfield"], "medium"), ("Catherine Tate", ["Catherine Tate", "Tate"], "medium"),
 ("Michelle Dockery", ["Michelle Dockery", "Dockery"], "medium"), ("Lily James", ["Lily James"], "medium"), ("Jenna Coleman", ["Jenna Coleman", "Coleman"], "medium"),
 ("Ncuti Gatwa", ["Ncuti Gatwa", "Gatwa"], "medium"), ("Christopher Eccleston", ["Christopher Eccleston", "Eccleston"], "medium"), ("Tom Baker", ["Tom Baker"], "medium"),
 ("Freema Agyeman", ["Freema Agyeman", "Agyeman"], "hard"),
 # music
 ("James Bay (singer)", ["James Bay"], "hard"), ("Mabel (singer)", ["Mabel", "Mabel McVey"], "hard"), ("Liam Payne", ["Liam Payne", "Payne"], "medium"),
 ("Louis Tomlinson", ["Louis Tomlinson", "Tomlinson"], "medium"), ("Jason Orange", ["Jason Orange"], "hard"), ("Brett Anderson", ["Brett Anderson"], "hard"),
 ("Thom Yorke", ["Thom Yorke", "Yorke"], "medium"), ("Alex Turner (musician)", ["Alex Turner"], "medium"), ("Brandon Flowers", ["Brandon Flowers", "Flowers"], "medium"),
 ("Doja Cat", ["Doja Cat"], "medium"), ("The Weeknd", ["The Weeknd", "Weeknd", "Abel Tesfaye"], "medium"), ("Post Malone", ["Post Malone"], "medium"),
 # sport
 ("James Anderson (cricketer)", ["James Anderson", "Jimmy Anderson"], "medium"), ("Alastair Cook", ["Alastair Cook", "Alastair Cook", "Cook"], "medium"),
 ("Martin Johnson (rugby union)", ["Martin Johnson"], "medium"), ("Owen Farrell", ["Owen Farrell", "Farrell"], "medium"),
 ("George Russell (racing driver)", ["George Russell"], "medium"), ("Daniel Ricciardo", ["Daniel Ricciardo", "Ricciardo"], "medium"),
 ("Luke Humphries", ["Luke Humphries", "Humphries"], "medium"), ("Oleksandr Usyk", ["Oleksandr Usyk", "Usyk"], "medium"), ("Nicola Adams", ["Nicola Adams"], "medium"),
 ("Laura Kenny", ["Laura Kenny", "Laura Trott"], "medium"), ("Geraint Thomas", ["Geraint Thomas"], "medium"), ("Ellie Simmonds", ["Ellie Simmonds", "Simmonds"], "medium"),
 ("Jonnie Peacock", ["Jonnie Peacock", "Peacock"], "medium"), ("Sarah Storey", ["Sarah Storey", "Dame Sarah Storey"], "hard"),
 ("Alexander Isak", ["Alexander Isak", "Isak"], "easy"), ("Anthony Gordon", ["Anthony Gordon"], "easy"), ("Nick Pope", ["Nick Pope", "Pope"], "medium"),
 ("Joelinton", ["Joelinton"], "easy"), ("Sandro Tonali", ["Sandro Tonali", "Tonali"], "medium"), ("Raheem Sterling", ["Raheem Sterling", "Sterling"], "medium"),
 ("Kyle Walker", ["Kyle Walker"], "medium"), ("John Stones", ["John Stones", "Stones"], "medium"),
]
# After stocking: Mel Giedroyc was already in the bank (skipped), and these were retired from the contact sheet
# (stage, action or crowd shots where the face is small, dark or hidden).
ALREADY = {"Mel Giedroyc"}
RETIRED = {"Alex Turner (musician)", "Anthony Gordon", "Brandon Flowers", "Brett Anderson", "James Bay (singer)", "Jonnie Peacock",
           "Nick Pope", "Post Malone", "The Weeknd", "Thom Yorke"}
P = [p for p in P if p[0] not in ALREADY | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
