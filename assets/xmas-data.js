/* Let's Quiz: CHRISTMAS DAY (November 2026), the shared data. Loaded by the host screen, the phones and the builder.
 * The dinner: nine dishes, each tied to a question category, plus the tomato ketchup that only a 1% question can win.
 * The family: eight characters, each with a quirk that always works and one power to use once.
 * Nothing here runs by itself; assets/xmas.js (host), assets/xmas-phone.js (phones) and assets/night-tools.js (builder) read it. */
(function () {
  const ITEMS = [
    // rar: 1 common (every right answer collects), 2 uncommon (the quickest 60% of right answers), 3 rare (the quickest 35%), 4 the ketchup
    { k: 'turkey', name: 'Turkey', icon: '🦃', cat: 'Christmas', rar: 1, n: 13 },
    { k: 'potatoes', name: 'Roast potatoes', icon: '🥔', cat: 'TV & Film', rar: 1, n: 11 },
    { k: 'pigs', name: 'Pigs in blankets', icon: '🌭', cat: 'Music', rar: 1, n: 11 },
    { k: 'stuffing', name: 'Stuffing', icon: '🍞', cat: 'History', rar: 2, n: 8 },
    { k: 'parsnips', name: 'Carrots & parsnips', icon: '🥕', cat: 'Geography', rar: 2, n: 8 },
    { k: 'sprouts', name: 'Brussels sprouts', icon: '🥦', cat: 'Food & Drink', rar: 2, n: 8 },
    { k: 'gravy', name: 'Gravy', icon: '🥣', cat: 'Celebrities', rar: 3, n: 6 },
    { k: 'cranberry', name: 'Cranberry sauce', icon: '🍒', cat: 'Sport', rar: 3, n: 5 },
    { k: 'yorkie', name: 'Yorkshire pudding', icon: '🥧', cat: 'Science', rar: 3, n: 5 },
    { k: 'ketchup', name: 'Tomato ketchup', icon: '🍅', cat: 'The 1% question', rar: 4, n: 3, ketchup: true },
  ];
  const RARITY = { 1: { label: 'Common', stars: '⭐', share: 1, diff: 'easy' }, 2: { label: 'Uncommon', stars: '⭐⭐', share: 0.6, diff: 'medium' }, 3: { label: 'Rare', stars: '⭐⭐⭐', share: 0.35, diff: 'hard' }, 4: { label: 'The 1% question', stars: '🍅', share: 1, diff: 'hard' } };

  // The family. quirk: always on. power: used once, between questions. need: what the phone must ask for ('item' = a missing common dish, 'target' = a player, 'steal' = a player and an item, none = just press it).
  const CHARS = [
    { k: 'nan', icon: '👵', name: 'Nan', quirk: 'Not on my watch: the first time anyone tries to steal from you or swap with you, it fails.', power: 'Handbag Surprise', how: 'Pull any one missing common dish (turkey, potatoes or pigs in blankets) out of your handbag.', need: 'item' },
    { k: 'grandad', icon: '👴', name: 'Grandad', quirk: 'Wakes up for the good stuff: +300 points every time you collect a rare dish.', power: 'Wake Up!', how: 'On the next dish question your points double, and if you get it right you collect the dish even if you were not quick enough.', need: '' },
    { k: 'teen', icon: '🧒', name: 'The Teenager', quirk: 'Headphones in: the elf cannot touch your plate.', power: 'Hide in Your Room', how: 'Nobody can steal from you or swap with you for the next six dish questions.', need: '' },
    { k: 'dog', icon: '🐕', name: 'The Dog', quirk: 'Under the table: when you steal, nobody is told who did it.', power: 'Snatch the Sausage', how: 'Steal any one dish from anybody, right now.', need: 'steal' },
    { k: 'cousin', icon: '🧠', name: 'Know-It-All Cousin', quirk: 'Well, actually: +100 points whenever you get a dish question wrong.', power: 'Insurance', how: 'On the next dish question, if you get it wrong you still collect the dish.', need: '' },
    { k: 'maureen', icon: '🥂', name: 'Auntie Maureen', quirk: 'Sharp eyes after a sherry: you see the elf three seconds before everyone else.', power: 'Spill the Gravy', how: 'Pick a player: on their next dish question they cannot collect, even if they get it right.', need: 'target' },
    { k: 'keith', icon: '🧔', name: 'Uncle Keith', quirk: 'Dodgy: your steals ignore shields, bedrooms and Nan.', power: 'Dodgy Deal', how: 'Take a random dish from whoever has the fullest plate.', need: '' },
    { k: 'mum', icon: '👩', name: 'Mum', quirk: 'Organised: each missing dish costs you 1,500 at the end, not 2,000.', power: 'Swap Seats', how: 'Swap one random dish with a player you pick: you each give one the other does not have.', need: 'target' },
  ];

  // The day, from stockings to midnight. Shown as a clock on the host screen and on the plate.
  const SCENES = [
    { t: 0, icon: '🧦', name: 'Stockings and pyjamas' }, { t: 0.1, icon: '🎁', name: 'Opening the presents' }, { t: 0.22, icon: '🔔', name: 'Carols and church' },
    { t: 0.34, icon: '🍳', name: 'Cooking the dinner' }, { t: 0.46, icon: '🍽', name: 'The big dinner' }, { t: 0.62, icon: '👑', name: "The King's speech" },
    { t: 0.74, icon: '🎲', name: 'The board-game argument' }, { t: 0.86, icon: '📺', name: 'Leftovers and telly' }, { t: 0.95, icon: '🕛', name: 'Midnight' },
  ];

  // The ketchup questions: logic and lateral thinking, the kind that very few people get. Typed answers; why explains it.
  const KETCHUP_QS = [
    { text: "In 'The Twelve Days of Christmas', how many BIRDS are given altogether over the twelve days? (Count every bird in every verse.)", answers: ['184'], why: 'Partridges 12, turtle doves 22, French hens 30, calling birds 36, geese 42, swans 42: 184.', pct: 4 },
    { text: "In 'The Twelve Days of Christmas', how many gifts of any kind are given altogether over the twelve days?", answers: ['364'], why: 'Day n brings 1 + 2 + … + n gifts. Add the twelve daily totals and you get 364.', pct: 8 },
    { text: 'Look at this sequence: 1, 11, 21, 1211, 111221. What comes next?', answers: ['312211'], why: 'Each term describes the one before it: one 1, one 2 and one 1 make 111221; that is three 1s, two 2s and one 1: 312211.', pct: 2 },
    { text: 'How many squares of any size are there on a standard 8 by 8 chessboard?', answers: ['204'], why: '8² + 7² + 6² + 5² + 4² + 3² + 2² + 1² = 64 + 49 + 36 + 25 + 16 + 9 + 4 + 1 = 204.', pct: 3 },
    { text: 'What is the smallest number that has exactly ten factors?', answers: ['48', 'forty-eight', 'forty eight'], why: '48 = 2⁴ × 3, so it has (4 + 1) × (1 + 1) = 10 factors. Nothing smaller manages it.', pct: 3 },
    { text: 'What three-digit number is exactly eleven times the sum of its digits?', answers: ['198'], why: '1 + 9 + 8 = 18, and 18 × 11 = 198. It is the only one.', pct: 4 },
    { text: 'Which common English word of five letters becomes SHORTER when you add two letters to it?', answers: ['short'], why: 'SHORT plus ER makes SHORTER.', pct: 6 },
    { text: 'A snail climbs a 10 metre Christmas tree. It climbs 3 metres every day and slips back 2 metres every night. On which day does it first reach the top?', answers: ['8', 'day 8', 'day eight', 'eighth', 'the eighth day', '8th', 'the 8th day', 'eight'], why: 'After seven days and nights it is at 7 metres. On day 8 it climbs 3 metres and reaches 10 before it can slip back.', pct: 10 },
    { text: 'If you write out every whole number from 1 to 100, how many times does the digit 1 appear?', answers: ['21', 'twenty-one', 'twenty one'], why: 'Ten times as the last digit (1, 11, … 91), ten times as the first digit of 10 to 19, and once in 100: 21.', pct: 12 },
  ];

  const CFG = { PINCH_EVERY: 5, PINCH_MS: 30000, ELF_SPOT_MS: 14000, ELF_CHOOSE_MS: 25000, MAUREEN_HEAD_START_MS: 3000, MISSING: -2000, FULL: 5000, HIDE_Q: 6, WAKE_RARE: 300, COUSIN_WRONG: 100 };
  const share = (rar) => (RARITY[rar] || RARITY[1]).share;

  window.LQ = window.LQ || {};
  LQ.XMAS = { ITEMS, RARITY, CHARS, SCENES, KETCHUP_QS, CFG, share, item: (k) => ITEMS.find((i) => i.k === k) || null, char: (k) => CHARS.find((c) => c.k === k) || null, dishes: () => ITEMS.filter((i) => !i.ketchup) };
  /** The clock for a share of the night gone (0 to 1): 07:00 to midnight, and the scene it falls in. */
  LQ.XMAS.clock = (p) => {
    p = Math.max(0, Math.min(1, p || 0));
    const mins = Math.round((7 + p * 17) * 60), h = Math.floor(mins / 60) % 24, m = mins % 60;
    let sc = SCENES[0]; for (const s of SCENES) if (p >= s.t) sc = s;
    return { time: String(h).padStart(2, '0') + ':' + String(m).padStart(2, '0'), icon: sc.icon, scene: sc.name };
  };
})();
