# Bank session 10 Oct 2026: 3 more general races -> bank/race-141.json (geography words, maths words, election words). 20 rows each, target 10; wrong options are
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

race("what's this geography word?", "World geography", "medium", ["geography", "landforms", "words"], [
 ("Fan-shaped land where a river splits into channels near the sea, like the Nile's", "Delta", ["Levee", "Floodplain", "Spit"]),
 ("A long, deep sea inlet carved out by a glacier, common in Norway", "Fjord", ["Strait", "Bay", "Cove"]),
 ("A slow-moving river of ice", "Glacier", ["Moraine", "Cirque", "Scree"]),
 ("Where a river widens as it meets the sea and the tide comes in", "Estuary", ["Levee", "Floodplain", "Confluence"]),
 ("A narrow strip of land joining two larger areas, like Panama", "Isthmus", ["Spit", "Headland", "Strait"]),
 ("Land almost surrounded by water, like Cornwall", "Peninsula", ["Spit", "Stack", "Arch"]),
 ("A big group of islands", "Archipelago", ["Stack", "Sound", "Strait"]),
 ("A ring-shaped coral island around a lagoon", "Atoll", ["Stack", "Spit", "Headland"]),
 ("A shallow stretch of water cut off from the sea by a reef or sandbar", "Lagoon", ["Oasis", "Wadi", "Cove"]),
 ("A smaller river that flows into a bigger one", "Tributary", ["Confluence", "Levee", "Distributary"]),
 ("A curved lake left behind when a river cuts off one of its loops", "Oxbow lake", ["Tarn", "Reservoir", "Loch"]),
 ("A big looping bend in a river", "Meander", ["Levee", "Confluence", "Rapids"]),
 ("A large area of high, flat land", "Plateau", ["Escarpment", "Floodplain", "Drumlin"]),
 ("A deep, steep-sided valley cut by a river, like the Grand one in Arizona", "Canyon", ["Moraine", "Drumlin", "Esker"]),
 ("A cold, treeless plain where the ground stays frozen", "Tundra", ["Taiga", "Steppe", "Pampas"]),
 ("Hot tropical grassland with scattered trees, home to lions and zebras", "Savanna", ["Taiga", "Wadi", "Moorland"]),
 ("The imaginary line round the middle of the Earth", "Equator", ["Prime meridian", "International Date Line", "Arctic Circle"]),
 ("The seasonal wind that brings heavy summer rain to South Asia", "Monsoon", ["Sirocco", "Mistral", "Chinook"]),
 ("Where a river begins", "Source", ["Mouth", "Confluence", "Levee"]),
 ("A mountain that can erupt with lava", "Volcano", ["Geyser", "Fumarole", "Drumlin"])])

race("what's this maths word?", "Maths and numbers", "easy", ["maths", "words", "school"], [
 ("The longest side of a right-angled triangle", "Hypotenuse", ["Tangent", "Vertex", "Gradient"]),
 ("The distance from the centre of a circle to its edge", "Radius", ["Arc", "Tangent", "Segment"]),
 ("A straight line across a circle through its centre", "Diameter", ["Tangent", "Arc", "Sector"]),
 ("The distance all the way round a circle", "Circumference", ["Arc", "Sector", "Tangent"]),
 ("The distance all the way round the edge of a shape", "Perimeter", ["Vertex", "Axis", "Gradient"]),
 ("The amount of flat space a shape covers", "Area", ["Vertex", "Axis", "Ratio"]),
 ("How much space a solid takes up", "Volume", ["Vertex", "Ratio", "Gradient"]),
 ("A whole number, with no fractions or decimals", "Integer", ["Surd", "Vector", "Coefficient"]),
 ("The top number of a fraction", "Numerator", ["Quotient", "Coefficient", "Index"]),
 ("The bottom number of a fraction", "Denominator", ["Quotient", "Coefficient", "Index"]),
 ("An amount out of 100", "Percentage", ["Ratio", "Quotient", "Index"]),
 ("Add them all up and divide by how many there are", "Mean", ["Quartile", "Frequency", "Variance"]),
 ("The middle value once they're put in order", "Median", ["Quartile", "Frequency", "Variance"]),
 ("The value that turns up most often", "Mode", ["Quartile", "Frequency", "Variance"]),
 ("The biggest value take away the smallest", "Range", ["Quartile", "Variance", "Frequency"]),
 ("A number that divides exactly into another", "Factor", ["Remainder", "Quotient", "Exponent"]),
 ("Any number in another number's times table", "Multiple", ["Remainder", "Quotient", "Exponent"]),
 ("The number that, multiplied by itself, gives this one", "Square root", ["Logarithm", "Exponent", "Coefficient"]),
 ("A number that only divides by 1 and itself", "Prime number", ["Surd", "Vector", "Coefficient"]),
 ("About 3.14: a circle's circumference divided by its diameter", "Pi", ["Phi", "Euler's number", "Sigma"])])

race("what's this election word?", "Politics", "medium", ["elections", "politics", "words"], [
 ("The paper you mark with an X", "Ballot", ["Hansard", "Mandate", "Caucus"]),
 ("The area an MP represents", "Constituency", ["Caucus", "Lobby", "Primary"]),
 ("A party's list of promises before an election", "Manifesto", ["Hansard", "Filibuster", "Mandate"]),
 ("A meeting where the candidates debate in front of voters", "Hustings", ["Caucus", "Primary", "Division bell"]),
 ("Often a school or village hall, where you go to vote", "Polling station", ["Lobby", "Division bell", "Electoral college"]),
 ("The 10pm forecast based on asking people as they leave", "Exit poll", ["Caucus", "Primary", "Purdah"]),
 ("A huge victory, like Labour's in 1997", "Landslide", ["Filibuster", "Gerrymander", "Purdah"]),
 ("No party has an overall majority", "Hung parliament", ["Prorogation", "Dissolution", "Filibuster"]),
 ("The percentage shift of votes from one party to another", "Swing", ["Whip", "Mandate", "Pairing"]),
 ("Held when an MP dies or resigns between general elections", "By-election", ["Primary", "Caucus", "Prorogation"]),
 ("A public vote on a single question, like Brexit", "Referendum", ["Primary", "Caucus", "Filibuster"]),
 ("The share of people who actually voted", "Turnout", ["Mandate", "Whip", "Pairing"]),
 ("Counting the votes again when the result is very close", "Recount", ["Filibuster", "Prorogation", "Pairing"]),
 ("Knocking on doors to ask for people's votes", "Canvassing", ["Lobbying", "Filibuster", "Pairing"]),
 ("Backing a party you don't love to keep another one out", "Tactical voting", ["Gerrymander", "Filibuster", "Pairing"]),
 ("A constituency one party almost always wins", "Safe seat", ["Backbench", "Front bench", "Shadow cabinet"]),
 ("A seat that could easily change hands", "Marginal", ["Backbench", "Front bench", "Shadow cabinet"]),
 ("Voting by post instead of in person", "Postal vote", ["Proxy vote", "Division", "Pairing"]),
 ("What happens to a candidate's £500 if they get under 5% of the vote", "Lost deposit", ["Purdah", "Whip", "Mandate"]),
 ("The official who reads out the results at the count", "Returning officer", ["Speaker", "Chief whip", "Black Rod"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-141.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
