# Bank session 11 Oct 2026: 3 more general races -> bank/race-192.json (house buying, electrician and job hunting words). 20 rows each, target 10; wrong options are
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

race("what's this house buying word?", "Lifestyle", "medium", ["property", "house buying", "words"], [
 ("The big loan you take out to buy a home", "Mortgage", ["Overdraft", "Pension", "Annuity"]),
 ("The chunk of the price you put down yourself", "Deposit", ["Dividend", "Rebate", "Refund"]),
 ("The tax you pay when you buy", "Stamp duty", ["Council tax", "Road tax", "Poll tax"]),
 ("The inspection for damp, cracks and rot", "Survey", ["Census", "Audit", "Poll"]),
 ("The legal work of transferring ownership", "Conveyancing", ["Conveyor belt", "Convening", "Canvassing"]),
 ("Another buyer outbidding you after your offer was accepted", "Gazumping", ["Gazundering", "Gatecrashing", "Jumping the gun"]),
 ("The line of buyers and sellers all waiting on each other", "Chain", ["Queue", "Loop", "Rope"]),
 ("What first-time buyers try to get a foot on", "Property ladder", ["Stepladder", "Snakes and ladders", "Rope ladder"]),
 ("The moment the deal becomes legally binding", "Exchange of contracts", ["Shaking hands", "Signing off", "Handover"]),
 ("Moving day, when the money changes hands and you get the keys", "Completion", ["Conclusion", "Competition", "Compilation"]),
 ("Owning the building and the land outright, for ever", "Freehold", ["Stronghold", "Foothold", "Household"]),
 ("Owning it only for a fixed number of years", "Leasehold", ["Rent-to-buy", "Timeshare", "Tenancy"]),
 ("Owing more than the house is worth", "Negative equity", ["Negative feedback", "Overdrawn", "Bankruptcy"]),
 ("The price the seller hopes to get", "Asking price", ["Ticket price", "Reserve price", "Cover price"]),
 ("A house joined to one neighbour", "Semi-detached", ["Detached", "Maisonette", "Cottage"]),
 ("A house in a row, joined on both sides", "Terraced", ["Detached", "Maisonette", "Cottage"]),
 ("A home with no upstairs", "Bungalow", ["Penthouse", "Townhouse", "Duplex"]),
 ("Someone buying their very first home", "First-time buyer", ["Early adopter", "Window shopper", "Landlord"]),
 ("The UK's biggest property-search website", "Rightmove", ["Trustpilot", "Moneysupermarket", "Autotrader"]),
 ("Sells houses for a commission", "Estate agent", ["Travel agent", "Secret agent", "Double agent"])])

race("what's this electrician's word?", "Science", "medium", ["electricity", "trades", "words"], [
 ("Slang for an electrician", "Sparky", ["Chippy", "Brickie", "Postie"]),
 ("Blows to protect a circuit", "Fuse", ["Valve", "Filter", "Washer"]),
 ("The box of switches that trip when something goes wrong", "Fuse box", ["Junction box", "Meter box", "Letterbox"]),
 ("The green-and-yellow wire", "Earth", ["Return", "Signal", "Feed"]),
 ("The brown wire", "Live", ["Return", "Signal", "Spare"]),
 ("The blue wire", "Neutral", ["Signal", "Feed", "Spare"]),
 ("The unit of electrical 'push'", "Volt", ["Joule", "Newton", "Pascal"]),
 ("The unit of current", "Amp", ["Hertz", "Kelvin", "Lumen"]),
 ("The unit of power printed on light bulbs", "Watt", ["Joule", "Kelvin", "Lumen"]),
 ("The unit of resistance", "Ohm", ["Hertz", "Newton", "Pascal"]),
 ("Current taking a path it shouldn't, with sparks", "Short circuit", ["Long haul", "Circuit training", "Shortcut"]),
 ("The safety switch that cuts the power if you touch a live wire", "RCD", ["MOT", "LED", "DVD"]),
 ("Checking that portable appliances are safe", "PAT testing", ["MOT test", "Smear test", "Driving test"]),
 ("The plastic coating round copper wire", "Insulation", ["Isolation", "Inflation", "Installation"]),
 ("A lead with several sockets on the end", "Extension lead", ["Dog lead", "Pencil lead", "Lead singer"]),
 ("Turns the lights brighter or lower", "Dimmer switch", ["Toggle switch", "Bait and switch", "Nintendo Switch"]),
 ("The meter that measures volts, amps and ohms", "Multimeter", ["Speedometer", "Thermometer", "Pedometer"]),
 ("The tube that cables run through", "Conduit", ["Culvert", "Conductor", "Chimney"]),
 ("The British plug", "Three-pin plug", ["Two-pin plug", "Spark plug", "Bath plug"]),
 ("Where you plug in on the wall", "Socket", ["Sprocket", "Pocket", "Rocket"])])

race("what's this job hunting word?", "Lifestyle", "easy", ["jobs", "work", "words"], [
 ("Your two-page summary of jobs and skills", "CV", ["ID", "PIN", "VAT"]),
 ("The letter sent with it saying why you want the job", "Cover letter", ["Love letter", "Chain letter", "Newsletter"]),
 ("A former boss vouching for you", "Reference", ["Preference", "Inference", "Conference"]),
 ("A job waiting to be filled", "Vacancy", ["Vacation", "Vagrancy", "Vacuum"]),
 ("The few picked out for interview", "Shortlist", ["Shortcut", "Shortbread", "Short straw"]),
 ("A recruiter who poaches people for top jobs", "Headhunter", ["Bounty hunter", "Treasure hunter", "Ghost hunter"]),
 ("The government office that helps people find work", "Jobcentre", ["Garden centre", "Leisure centre", "Call centre"]),
 ("The social network for professionals", "LinkedIn", ["Facebook", "Instagram", "Snapchat"]),
 ("The trial period at the start of a new job", "Probation", ["Probate", "Proclamation", "Prohibition"]),
 ("The time you must work after handing in your notice letter", "Notice period", ["Grace period", "Cooling-off period", "Free period"]),
 ("The monthly breakdown of pay and deductions", "Payslip", ["Receipt", "Invoice", "Bank statement"]),
 ("Fixed yearly pay", "Salary", ["Pension", "Bonus", "Commission"]),
 ("A contract with no guaranteed hours", "Zero-hours", ["Part-time", "Full-time", "Flexitime"]),
 ("Self-employed, working for different clients", "Freelance", ["Free rein", "Free kick", "Freeloader"]),
 ("Losing your job because the role is cut", "Redundancy", ["Retirement", "Dismissal", "Sabbatical"]),
 ("Choosing to leave your job", "Resignation", ["Retirement", "Sabbatical", "Reservation"]),
 ("Earning while you learn a trade", "Apprenticeship", ["Fellowship", "Partnership", "Membership"]),
 ("A short work placement, often unpaid", "Internship", ["Fellowship", "Citizenship", "Friendship"]),
 ("Moving up to a better job in the same firm", "Promotion", ["Demotion", "Commotion", "Locomotion"]),
 ("The meeting where they quiz you about the job", "Interview", ["Overview", "Preview", "Review"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-192.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
