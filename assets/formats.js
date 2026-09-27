// One-click quiz formats. Modelled on the host's own Kahoot nights (docs/kahoot-analysis.html): a warm TV & Film opener,
// the long Music round, a light picture/letters breather, Catchphrase into the break, Sport straight after it, the
// "well I never knew that" round, a silly wordplay run-in and a game-show finale. The weekly rounds stay; the
// game shows rotate, so one week leans on Wipeout, the next on King of the Hill, the next on Hot Potato.
window.LQ_FORMATS = (() => {
  const TV_FILM = ['Film', 'Television', 'British films', 'Action and blockbusters', 'Horror films', 'Romantic comedies', 'Film quotes',
    'The Oscars and award winners', 'Animated films', 'Disney films', 'James Bond', 'Star Wars', 'Harry Potter', 'The Marvel universe',
    'DC, Batman and Superman', 'The Lord of the Rings and fantasy', 'British sitcoms', 'Soaps', 'Crime dramas', 'American TV', 'Reality TV',
    'Quiz and game shows', "Children's TV", 'Doctor Who', 'Friends', 'The Office and workplace comedies'];
  const MUSIC = ['Music', 'Pop music', 'Rock music', 'UK number ones', 'One-hit wonders', 'Boy bands and girl groups', 'The Beatles', 'Eurovision'];
  const SPORT = ['Sport', 'Football', 'The football World Cup', 'The Olympics', 'Cricket', 'Rugby', 'Tennis and golf', 'Boxing and combat sports',
    'Horse racing and darts', 'Motorsport', 'Newcastle v Sunderland'];
  const ABOUT = {
    tv: 'Films, telly, soaps and sitcoms: behind-the-scenes stories, famous relatives, real names, quotes and the detail behind the famous scene. Opens warm and nostalgic.',
    music: 'Songs, singers and bands: covers and who did it first, real names, famous relatives, chart records, release years, band line-ups and lyrics. Not musicals.',
    sport: 'Football first (Newcastle banter welcome), then darts, snooker, boxing, rugby, cricket, tennis, the Olympics and the odd oddity. Records, firsts and daft moments.',
    qi: '"Well I never knew that!" Surprising, counter-intuitive and funny true facts from every subject, where the obvious answer is often the wrong one.',
  };
  const tv = (games) => ({ title: 'TV & Film', about: ABOUT.tv, categories: TV_FILM, mix: { choice: 5, text: 4, order: 1, tf: 1, ...games } });
  const music = (games) => ({ title: 'Music', about: ABOUT.music, categories: MUSIC, mix: { tune: 5, choice: 3, text: 4, order: 1, tf: 1, ...games } });
  const sport = (games) => ({ title: 'Sport', about: ABOUT.sport, categories: SPORT, mix: { choice: 7, text: 3, order: 1, tf: 1, ...games } });
  const qi = (extra) => ({ title: 'Well I Never Knew That!', about: ABOUT.qi, wowOnly: true, mix: { choice: 7, tf: 3, nearest: 1, ...extra } });
  const game = (title, about, mix) => ({ title, about, mix, general: true });
  const dbl = (title, about, mix) => ({ ...game('Double Points: ' + title, about + ' Every score in this round counts twice!', mix), double: true });
  const BREAK = { title: 'Half-time', about: 'A 10-minute break with a countdown clock. Get one in!', mix: {}, breakMins: 10 };
  // Every night: The Chase just before the break, a Double Points round, then The Final Chase to finish.
  const CHASE = game('The Chase', 'Last game before the break! General knowledge: the leader becomes the Chaser and takes on the rest of the room.', { chase: 1 });
  const FINAL = game('The Final Chase', 'The last game of the night. General knowledge: whoever is leading now is the Chaser.', { chase: 1 });
  const catchphrase = game('Catchphrase', 'Say what you see!', { catchphrase: 5 });

  const FORMATS = [
    { id: 'classic', name: 'Friday Classic', blurb: 'Wheel of Fortune and Catchphrase, The Chase before the break, Wipeout boards in Music and Sport, Double Points Highbrow Lowbrow, and The Final Chase.',
      rounds: [
        tv({ race: 1 }),
        music({ wipeout: 1 }),
        game('Wheel of Fortune', 'Phrases, names and titles on the board, letters flipping over one by one.', { wheel: 5 }),
        catchphrase, CHASE, BREAK,
        sport({ wipeout: 1 }),
        qi(),
        game('Answer Smash', 'A picture and a clue whose answers overlap. Smash them together.', { smash: 5 }),
        game('Rhyme Time', 'Two clues, two rhyming answers. Type both.', { rhyme: 5 }),
        dbl('Highbrow Lowbrow', 'A hard, scholarly clue, or tap for the easy pop-culture clue with the same answer for half the points.', { highlow: 5 }),
        FINAL,
      ] },
    { id: 'king', name: 'King of the Hill Night', blurb: 'Dingbats and Catchphrase, The Chase before the break, The 1% Club and Highbrow Lowbrow, Double Points King of the Hill, and The Final Chase.',
      rounds: [
        tv({ race: 1 }),
        music({ tune: 6, race: 1 }),
        game('Dingbats', 'Say what you see: phrases hidden in how the words are laid out.', { dingbat: 5 }),
        catchphrase, CHASE, BREAK,
        sport({ pin: 1 }),
        qi(),
        game('Highbrow Lowbrow', 'A hard, scholarly clue, or tap for the easy pop-culture clue with the same answer for half the points.', { highlow: 5 }),
        game('The 1% Club', 'No knowledge needed, just work it out.', { club: 5 }),
        dbl('King of the Hill', 'General knowledge head-to-heads, answered out loud. Stay on the hill to win.', { koth: 1 }),
        FINAL,
      ] },
    { id: 'games', name: 'Games Night', blurb: 'Picture Reveal and Catchphrase, The Chase before the break, Hot Potato, Draw It and Only One, Double Points Blockbusters, and The Final Chase.',
      rounds: [
        tv({ wipeout: 1 }),
        music({ race: 1 }),
        game('Picture Reveal', 'Famous faces hidden behind tiles that flip over one by one. The sooner you get it, the more you score.', { reveal: 5 }),
        catchphrase, CHASE, BREAK,
        sport({ potato: 1 }),
        qi(),
        game('Draw It', 'One player draws, everyone else guesses.', { draw: 1 }),
        game('Answer Smash', 'A picture and a clue whose answers overlap. Smash them together.', { smash: 5 }),
        game('Only One', 'Be the only one to say it: match anyone and you are out. Last one standing wins.', { unique: 1 }),
        dbl('Blockbusters', 'Newcastle v Sunderland across the letter board. General knowledge.', { blockbusters: 1 }),
        FINAL,
      ] },
    { id: 'wipeout', name: 'Wipeout & Rhymes', blurb: '20 Questions, Only One and Catchphrase, The Chase before the break, Hot Potato and Rhyme Time, Double Points Wipeout, and The Final Chase.',
      rounds: [
        tv({ race: 1 }),
        music({ wipeout: 1 }),
        game('20 Questions', 'Everyone hunts the same mystery person or thing with yes/no questions.', { twenty: 2 }),
        game('Only One', 'Be the only one to say it: match anyone and you are out. Last one standing wins.', { unique: 1 }),
        catchphrase, CHASE, BREAK,
        sport({ potato: 1 }),
        qi(),
        game('Rhyme Time', 'Two clues, two rhyming answers. Type both.', { rhyme: 5 }),
        dbl('Wipeout', 'Pick the right answers off the board. One wrong pick and you are out.', { wipeout: 3 }),
        FINAL,
      ] },
  ];
  /** This week's format: they take turns week by week, so no two weeks running feel the same. */
  function thisWeek(date = new Date()) {
    const d = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
    const week = Math.floor((d - Date.UTC(2026, 0, 5)) / (7 * 86400000));
    return FORMATS[((week % FORMATS.length) + FORMATS.length) % FORMATS.length];
  }
  return { FORMATS, thisWeek, TV_FILM, MUSIC, SPORT };
})();
