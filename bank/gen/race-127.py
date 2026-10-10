# Bank session 10 Oct 2026: 2 more general races -> bank/race-127.json (money words, kinds of government). 20 rows each, target 10; wrong options are
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


race("what's this money word?", "Everyday life", "medium", ["money", "finance", "words"], [
 ("A long loan for buying a house, secured on the house itself", "Mortgage", ["Annuity", "Bond", "Lease"]),
 ("Spending more than is in your current account, with the bank's agreement", "Overdraft", ["Arrears", "Rebate", "Annuity"]),
 ("Prices rising across the economy, so your money buys less", "Inflation", ["Deflation", "Austerity", "Stagnation"]),
 ("The economy shrinking for two quarters in a row", "Recession", ["Austerity", "Deflation", "Stagflation"]),
 ("A share of a company's profits paid out to its shareholders", "Dividend", ["Royalty", "Rebate", "Commission"]),
 ("Regular money paid to you after you retire", "Pension", ["Allowance", "Bursary", "Stipend"]),
 ("What a bank pays you for saving, or charges you for borrowing", "Interest", ["Commission", "Premium", "Levy"]),
 ("Legally declared unable to pay your debts", "Bankrupt", ["Solvent", "Liquid", "Audited"]),
 ("A bill sent out asking for payment for goods or work", "Invoice", ["Quote", "Estimate", "Ledger"]),
 ("Proof that you've paid, handed over at the till", "Receipt", ["Voucher", "Ledger", "Quote"]),
 ("A plan of how much you'll earn and how much you'll spend", "Budget", ["Ledger", "Audit", "Balance sheet"]),
 ("Money paid up front to secure something, like a rented flat", "Deposit", ["Premium", "Levy", "Rebate"]),
 ("Money handed back when you return something to a shop", "Refund", ["Discount", "Voucher", "Commission"]),
 ("Fixed yearly pay for a job, usually paid in monthly instalments", "Salary", ["Bonus", "Commission", "Allowance"]),
 ("Lets a company take varying amounts from your account when bills are due", "Direct debit", ["Standing order", "Cheque", "Bank transfer"]),
 ("A number lenders check to judge how reliable a borrower you are", "Credit score", ["PIN", "IBAN", "Account number"]),
 ("The form the self-employed fill in each year to tell HMRC what they earned", "Tax return", ["P45", "P60", "Payslip"]),
 ("A long spell of share prices rising", "Bull market", ["Bear market", "Crash", "Correction"]),
 ("The six-digit number that identifies your bank", "Sort code", ["IBAN", "PIN", "Account number"]),
 ("The tax you pay when you buy a house", "Stamp duty", ["Council tax", "Capital gains tax", "Inheritance tax"])])

race("what kind of government is this?", "Politics", "medium", ["government", "politics", "words"], [
 ("Rule by the people, who vote for their leaders", "Democracy", ["Autocracy", "Feudalism", "Despotism"]),
 ("A king or queen is head of state, but an elected parliament makes the laws", "Constitutional monarchy", ["Absolute monarchy", "Regency", "Feudalism"]),
 ("Rule by religious leaders in the name of God", "Theocracy", ["Autocracy", "Timocracy", "Stratocracy"]),
 ("Power held by a small group of people", "Oligarchy", ["Autocracy", "Despotism", "Ochlocracy"]),
 ("Rule by the very rich", "Plutocracy", ["Stratocracy", "Ochlocracy", "Feudalism"]),
 ("One ruler with total power, who has usually seized it", "Dictatorship", ["Regency", "Protectorate", "Triumvirate"]),
 ("No government at all", "Anarchy", ["Ochlocracy", "Feudalism", "Totalitarianism"]),
 ("A state with an elected or appointed head of state instead of a monarch, like France", "Republic", ["Emirate", "Regency", "Protectorate"]),
 ("Power goes to those with the most talent and ability", "Meritocracy", ["Timocracy", "Stratocracy", "Ochlocracy"]),
 ("Rule by the elderly", "Gerontocracy", ["Timocracy", "Stratocracy", "Ochlocracy"]),
 ("Rule by thieves who loot the country's wealth", "Kleptocracy", ["Ochlocracy", "Despotism", "Timocracy"]),
 ("Rule by scientists and technical experts", "Technocracy", ["Stratocracy", "Timocracy", "Ochlocracy"]),
 ("A society where women hold the power", "Matriarchy", ["Regency", "Feudalism", "Despotism"]),
 ("A society where men hold the power", "Patriarchy", ["Regency", "Feudalism", "Ochlocracy"]),
 ("Rule by a privileged noble class", "Aristocracy", ["Ochlocracy", "Stratocracy", "Despotism"]),
 ("Run by officials and layers of red tape", "Bureaucracy", ["Ochlocracy", "Feudalism", "Regency"]),
 ("A group of military officers ruling after a coup", "Junta", ["Triumvirate", "Regency", "Protectorate"]),
 ("States with their own governments joined under a central one, like the USA", "Federation", ["Protectorate", "Regency", "Emirate"]),
 ("A territory ruled from a distant country, like Hong Kong under Britain until 1997", "Colony", ["Emirate", "Regency", "Triumvirate"]),
 ("Two or more parties sharing power, as in Britain from 2010 to 2015", "Coalition", ["Triumvirate", "Regency", "Protectorate"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-127.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
