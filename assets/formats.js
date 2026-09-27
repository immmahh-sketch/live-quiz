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
  const tv = (games) => ({ title: 'TV & Film', about: ABOUT.tv, categories: TV_FILM, mix: { choice: 6, text: 3, order: 1, tf: 1, ...games } });
  const music = (games) => ({ title: 'Music', about: ABOUT.music, categories: MUSIC, mix: { tune: 5, choice: 4, text: 3, order: 1, tf: 1, ...games } });
  const sport = (games) => ({ title: 'Sport', about: ABOUT.sport, categories: SPORT, mix: { choice: 7, text: 3, order: 1, tf: 1, ...games } });
  const qi = (extra) => ({ title: 'Well I Never Knew That!', about: ABOUT.qi, wowOnly: true, mix: { choice: 7, tf: 3, nearest: 1, ...extra } });
  const game = (title, about, mix) => ({ title, about, mix, general: true });
  const BREAK = { title: 'Half-time', about: 'A 10-minute break with a countdown clock. Get one in!', mix: {}, breakMins: 10 };

  const FORMATS = [
    { id: 'classic', name: 'Friday Classic', blurb: 'Wheel of Fortune and Catchphrase before the break, Wipeout boards in Music and Sport, The Chase to finish.',
      rounds: [
        tv({ race: 1 }),
        music({ wipeout: 1 }),
        game('Wheel of Fortune', 'Phrases, names and titles on the board, letters flipping over one by one.', { wheel: 5 }),
        game('Catchphrase', 'Say what you see! Last one before the break.', { catchphrase: 5 }),
        BREAK,
        sport({ wipeout: 1 }),
        qi(),
        game('Answer Smash', 'A picture and a clue whose answers overlap. Smash them together.', { smash: 5 }),
        game('Rhyme Time', 'Two clues, two rhyming answers. Type both.', { rhyme: 5 }),
        game('Grand Finale: The Chase', 'General knowledge. The leader becomes the Chaser and takes on the rest of the room.', { chase: 1 }),
      ] },
    { id: 'king', name: 'King of the Hill Night', blurb: 'Dingbats and Catchphrase before the break, a head-to-head King of the Hill finale, Highbrow Lowbrow for the brainy ones.',
      rounds: [
        tv({ race: 1 }),
        music({ tune: 6, race: 1 }),
        game('Dingbats', 'Say what you see: phrases hidden in how the words are laid out.', { dingbat: 5 }),
        game('Catchphrase', 'Say what you see! Last one before the break.', { catchphrase: 5 }),
        BREAK,
        sport({ pin: 1, koth: 1 }),
        qi(),
        game('Highbrow Lowbrow', 'A hard, scholarly clue, or tap for the easy pop-culture clue with the same answer for half the points.', { highlow: 5 }),
        game('The 1% Club', 'No knowledge needed, just work it out.', { club: 5 }),
        game('Grand Finale: King of the Hill', 'General knowledge head-to-heads, answered out loud. Stay on the hill to win.', { koth: 1 }),
      ] },
    { id: 'games', name: 'Games Night', blurb: 'Picture Reveal and Draw It, Hot Potato after the break, and Newcastle v Sunderland Blockbusters to finish.',
      rounds: [
        tv({ wipeout: 1 }),
        music({ race: 1 }),
        game('Picture Reveal', 'Famous faces hidden behind tiles that flip over one by one. The sooner you get it, the more you score.', { reveal: 5 }),
        game('Catchphrase', 'Say what you see! Last one before the break.', { catchphrase: 5 }),
        BREAK,
        sport({ potato: 1 }),
        qi(),
        game('Draw It', 'One player draws, everyone else guesses.', { draw: 1 }),
        game('Answer Smash', 'A picture and a clue whose answers overlap. Smash them together.', { smash: 5 }),
        game('Grand Finale: Blockbusters', 'Newcastle v Sunderland across the letter board. General knowledge.', { blockbusters: 1 }),
      ] },
    { id: 'wipeout', name: 'Wipeout & Rhymes', blurb: 'A full Wipeout round, 20 Questions and Rhyme Time, Hot Potato, and The Chase to finish.',
      rounds: [
        tv({ race: 1 }),
        music({ wipeout: 1 }),
        game('20 Questions', 'Everyone hunts the same mystery person or thing with yes/no questions.', { twenty: 2 }),
        game('Catchphrase', 'Say what you see! Last one before the break.', { catchphrase: 5 }),
        BREAK,
        sport({ potato: 1 }),
        qi(),
        game('Wipeout', 'Pick the right answers off the board. One wrong pick and you are out.', { wipeout: 3 }),
        game('Rhyme Time', 'Two clues, two rhyming answers. Type both.', { rhyme: 5 }),
        game('Grand Finale: The Chase', 'General knowledge. The leader becomes the Chaser and takes on the rest of the room.', { chase: 1 }),
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
