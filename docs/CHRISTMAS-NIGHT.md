# Christmas quiz night: preparation plan (asked for 11 Nov 2026)

The host wants a full Christmas-themed hosted quiz night, with as many topics and game types as possible written
in a Christmas theme, plus new twist games in the spirit of Taskmaster, The Traitors, "I Literally Just Told You"
and Box Clever, but different.

## What already exists (do not rewrite it)

The bank already has four complete Christmas topics, each at the full per-type targets:
`christmas`, `christmas-movies`, `christmas-music`, `christmas-tv` (check with `node tools/bank-next.mjs --list | grep christmas`).
Do NOT add a fifth topic: bank-next would ask for ~400 items and most would be duplicates.

## What the first Christmas session does (the next bank session)

1. Do the usual bank-next top-up first if one is pending, then switch to Christmas for the rest of the session.
2. Audit: for each of the four Christmas topics, count the UNUSED, non-rejected, non-flagged items per game type
   (choice, text, tf, order, sort, highlow, smash, tune, rhyme, wipeout, race, pin, match, wheel, club, dingbat,
   conundrum, nearest, reveal, cards). Write the counts into `docs/CHRISTMAS-NIGHT-AUDIT.md`.
3. Fill the gaps with NEW Christmas items in `bank/topics/christmas-night__N.json` files, imported with
   `TOPICS=christmas` (the category name is "Christmas"; the file name only needs to be unique):
   - Any game type with fewer than ~15 unused Christmas items gets topped up to 15+.
   - The item types for the twist games below (festive tasks, wish-list prompts, Grinch/elf content) are extras.
   - Festive Christmas-night flavour: cracker jokes (text: punchline), Christmas dingbats, 9-letter festive
     conundrums, Christmas number ones as `nearest` (year), Wipeout boards (things on a Christmas dinner plate, reindeer,
     Dickens characters, ...), pins (Bethlehem, Rovaniemi, Nuremberg market, Rockefeller Center, Lapland, Bavaria).
   - Rules as ever: genuine difficulty ratings, facts you are sure of, UK spelling, no giveaways, 15%+ "wow".
4. Commit, push, then carry on with the normal loop.
5. Later sessions: assemble the night from the bank (see "Assembling" below) and save it as a draft quiz.

## Assembling the night (about 100 questions, user rule)

Use the one-click builder / Make a Traitors night tool pattern, but with the Christmas topics only:
Welcome slides, music round (tune), pictures (reveal/dingbat), a QI facts round, Wipeout, Pin, Race, Blockbusters
(festive sides, e.g. "Brussels sprouts v Pigs in blankets" or from `BB_TEAM_PAIRS`), Hot Potato as "Pass the Parcel"
(general-knowledge questions, per the game rules), King of the Hill / Chase on general knowledge, then the rules that
always apply: Double Points Answer Smash, then The Final Chase last. Add a break around halfway.

## New twist games proposed (host to choose; none built yet)

See the chat reply of 11 Nov 2026 for the full list. Short names: Secret Santa, Elf on the Shelf, Build Your
Christmas Dinner, Twelve Days of Christmas, Advent Calendar, The Grinch, Don't Say It, Festive Tasks (Taskmaster style),
Wish List (whose is it?), Santa's Tracker (cooperative).
