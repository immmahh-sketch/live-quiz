/* Let's Quiz! — shared config and helpers used by the builder, host screen and player app. */
// GitHub Pages lets browsers keep a page for up to 10 minutes, so after an update people can be served the old one.
// On opening, ask for the page afresh; if a newer one is live, reload once to pick it up.
(async () => {
  try {
    const r = await fetch(location.pathname, { method: 'HEAD', cache: 'no-store' });
    const live = r.headers.get('last-modified');
    if (!live || new Date(live) - new Date(document.lastModified) < 2000 || sessionStorage.getItem('lq_reloaded_for') === live) return;
    sessionStorage.setItem('lq_reloaded_for', live);
    location.reload();
  } catch {}
})();
window.LQ = (() => {
  const SUPABASE_URL = 'https://safcrtrfdzsnftghibot.supabase.co';
  const SUPABASE_KEY = 'sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU';
  const API = SUPABASE_URL + '/functions/v1/quiz-api';
  const PW_KEY = 'lq_host_pw';

  // ---------------------------------------------------------------- basics
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const uid = (p = 'x') => p + '_' + Math.random().toString(36).slice(2, 10);
  const clamp = (n, a, b) => Math.min(b, Math.max(a, n));
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  function shuffle(arr) { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  function store(key, val) { try { if (val === undefined) return JSON.parse(localStorage.getItem(key)); localStorage.setItem(key, JSON.stringify(val)); } catch { return null; } }
  function unstore(key) { try { localStorage.removeItem(key); } catch {} }

  // ---------------------------------------------------------------- API
  function hostPassword() { try { return localStorage.getItem(PW_KEY) || ''; } catch { return ''; } }
  function setHostPassword(pw) { try { pw ? localStorage.setItem(PW_KEY, pw) : localStorage.removeItem(PW_KEY); } catch {} }
  async function api(action, payload = {}, opts = {}) {
    const ctrl = new AbortController();
    const t = setTimeout(() => ctrl.abort(), opts.timeout || 60000);
    let r, data;
    try {
      r = await fetch(API, {
        method: 'POST', signal: ctrl.signal,
        headers: { 'content-type': 'application/json', apikey: SUPABASE_KEY, Authorization: 'Bearer ' + SUPABASE_KEY },
        body: JSON.stringify({ action, password: opts.password ?? hostPassword(), ...payload }),
      });
      data = await r.json().catch(() => ({ error: 'The server sent back something unexpected.' }));
    } catch (e) {
      throw new Error(e.name === 'AbortError' ? 'That took too long and was cancelled.' : 'Could not reach the server. Check your connection.');
    } finally { clearTimeout(t); }
    if (!r.ok || data.error) {
      const msg = data.error || (r.status === 504 || r.status === 546 ? 'The server took too long on that. Try again, or ask for fewer at once.' : 'Request failed (' + r.status + ')');
      const err = new Error(msg); err.status = r.status; throw err;
    }
    if (action === 'generate' && data && typeof data === 'object') Object.defineProperty(data, '__req', { value: payload, enumerable: false }); // for the build log
    return data;
  }
  function client() {
    return supabase.createClient(SUPABASE_URL, SUPABASE_KEY, { realtime: { params: { eventsPerSecond: 30 } } });
  }

  // ---------------------------------------------------------------- question types
  const TYPES = {
    choice: { label: 'Multiple choice', icon: '◆', blurb: 'One right answer and up to three wrong ones.' },
    text:   { label: 'Type the answer', icon: '✎', blurb: 'Players type it in. Spelling and wording are judged by AI.' },
    order:  { label: 'Put in order',    icon: '↕', blurb: 'Players arrange the items into the right order.' },
    pin:    { label: 'Drop the pin',    icon: '📍', blurb: 'Players tap a spot on a picture. Closest scores most.' },
    match:  { label: 'Match up',        icon: '⇄', blurb: 'Pair each word with its picture or partner.' },
    tf:     { label: 'True or false',   icon: '✓✗', blurb: 'A statement. Players say true or false.' },
    sort:   { label: 'Categorise',      icon: '🗂', blurb: 'Players drop each answer into the right category.' },
    wipeout:{ label: 'Wipeout',         icon: '💥', blurb: 'Answers scattered on screen, some wrong. Players take turns picking a right one. Pick a wrong one and you are wiped out.' },
    race:   { label: 'The Race',        icon: '🏁', blurb: 'A bank of quick questions on the phones. First to ten right wins the prize. Their emoji races across the screen.' },
    smash:  { label: 'Answer Smash',    icon: '🔀', blurb: 'A picture and a clue whose answers overlap. Players type the two smashed together.' },
    wheel:  { label: 'Wheel of Fortune', icon: '🎡', blurb: 'A hidden phrase on the board. Letters flip over one by one; the sooner you solve it, the more you score.' },
    highlow:{ label: 'Highbrow Lowbrow', icon: '🎓', blurb: 'A hard, scholarly clue on the screen. Stuck? Tap your phone for the easy, pop-culture clue with the same answer, for half the points.' },
    rhyme:  { label: 'Rhyme Time',      icon: '🎤', blurb: 'Two clues whose answers rhyme. Players type both answers in one go.' },
    club:   { label: 'The 1% Club',    icon: '🧠', blurb: 'Logic, wordplay and lateral thinking. No knowledge needed, just work it out. The fewer people who get it, the more it pays.' },
    dingbat:{ label: 'Dingbats',        icon: '🔤', blurb: 'Say what you see: a well-known phrase hidden in how the words are laid out.' },
    catchphrase: { label: 'Catchphrase', icon: '🗯️', blurb: 'A clip from the show plays on the screen. Players type the well-known phrase it shows.' },
    tune:   { label: 'Name That Tune',  icon: '🎵', blurb: 'A clip plays on the screen. Name the song, the artist, the film it is from, the year, or the next line.' },
    potato: { label: 'Hot Potato',      icon: '💣', blurb: 'A lit bomb passes round the room. Whoever holds it answers on their phone; get it right and pass it on. Holding it when it blows costs you points.' },
    koth:   { label: 'King of the Hill', icon: '👑', blurb: 'Fastest finger picks two players for a head-to-head buzzer battle, answered out loud. Right keeps you on the hill. First to the target wins the prize.' },
    chase:  { label: 'The Chase',       icon: '🏃', blurb: 'The leader becomes the Chaser and takes on everyone else as one team, who start a few steps ahead. First right answer on each question moves that side a step. Get home before you are caught.' },
    blockbusters: { label: 'Blockbusters', icon: '⬢', blurb: 'Two teams battle across a board of letter hexagons. First to type the answer claims the hex; the first team to join two opposite sides of the board wins.' },
    nearest:{ label: 'Nearest Wins',    icon: '🎯', blurb: 'A number question. Everyone guesses, the guesses go up on a number line, then the answer drops in. The closer you are, the more you score.' },
    draw:   { label: 'Draw It',         icon: '🎨', blurb: 'One player draws a secret word on their phone and it appears live on the screen. Everyone else races to guess it. Quick guessers score, and so does the artist.' },
    twenty: { label: '20 Questions',    icon: '🕵️', blurb: 'Everyone has the same mystery person or thing to find. Players tap yes/no questions on their phones and guess whenever they like. The first three to crack it score; running out of questions or time costs points.' },
  };
  // ---------------------------------------------------------------- 20 Questions
  // One tree of yes/no questions that works for any answer. The openers say what kind of thing it is; a yes to
  // one opens that kind's questions, and a question with `needs` only appears once all of those were answered yes.
  // Each 20 Questions item stores what it is (q.what: which opener is yes) and a yes/no for each question in that branch.
  const TWENTY_KINDS = [
    { id: 'person', text: 'Is it a person?' }, { id: 'character', text: 'Is it a fictional character?' },
    { id: 'animal', text: 'Is it an animal?' }, { id: 'place', text: 'Is it a place?' },
    { id: 'food', text: 'Is it a food or drink?' }, { id: 'object', text: 'Is it an object?' },
    { id: 'title', text: 'Is it a film, TV show, book or song?' }, { id: 'brand', text: 'Is it a brand or company?' },
  ];
  // Each kind's questions, in sections the phone shows as headings. A question can be gated:
  //   needs: every id answered Yes · any: at least one answered Yes · not: hidden once any is answered Yes
  //   notNo: hidden once any is answered No · pair: hidden once its partner has been asked at all
  //   group: once one question in the group is answered Yes, the rest of the group go (a singer is not also asked "a politician?")
  const TWENTY_QS = [];
  function tq(cat, sec, o, rows) {
    for (const [id, text, x = {}] of rows) TWENTY_QS.push({ cat, sec, id, text, needs: [...(o.needs || []), ...(x.needs || [])], any: x.any || o.any || [], not: [...(o.not || []), ...(x.not || [])], notNo: x.notNo || [], pair: x.pair || null, group: 'group' in x ? x.group : (o.group || null) });
  }
  const P_ROLES = ['p_music', 'p_actor', 'p_sport', 'p_tv', 'p_comedy', 'p_politics', 'p_royal', 'p_writer', 'p_science', 'p_business', 'p_hero'];
  // ---- a real person ----
  tq('person', 'About them', {}, [
    ['p_man', 'Is it a man?', { pair: 'p_woman' }], ['p_woman', 'Is it a woman?', { pair: 'p_man' }],
    ['p_alive', 'Are they alive?'], ['p_over50', 'Are they over 50? (Or were they, when they died?)', { notNo: [] }], ['p_over70', 'Are they over 70?', { needs: ['p_over50'] }],
    ['p_under30', 'Are they under 30?', { needs: ['p_alive'], not: ['p_over50'], notNo: [] }], ['p_history', 'Did they live before 1900?', { notNo: [], not: ['p_alive'] }],
    ['p_british', 'Are they British?', { group: 'nat' }], ['p_american', 'Are they American?', { group: 'nat' }], ['p_irish', 'Are they Irish?', { group: 'nat' }],
    ['p_knighted', 'Have they been knighted or made a dame?', { not: ['p_royal'] }],
  ]);
  tq('person', 'Where are they from?', { needs: ['p_british'] }, [
    ['p_english', 'Are they English?', { group: 'home' }], ['p_scottish', 'Are they Scottish?', { group: 'home' }], ['p_welsh', 'Are they Welsh?', { group: 'home' }],
    ['p_northeast', 'Are they from the North East?', { not: ['p_scottish', 'p_welsh'] }],
    ['p_north', 'Are they from the north of England?', { not: ['p_scottish', 'p_welsh', 'p_northeast'] }],
    ['p_london', 'Are they from London?', { not: ['p_scottish', 'p_welsh', 'p_northeast', 'p_north'] }],
  ]);
  tq('person', 'What are they known for?', { group: 'role' }, [
    ['p_music', 'Are they a singer or musician?'], ['p_actor', 'Are they an actor?'], ['p_sport', 'Are they a sports star?'],
    ['p_tv', 'Are they a TV presenter or personality?'], ['p_comedy', 'Are they a comedian?'], ['p_politics', 'Are they a politician or leader?'],
    ['p_royal', 'Are they royal?'], ['p_writer', 'Are they a writer?'], ['p_science', 'Are they a scientist or inventor?'],
    ['p_business', 'Are they a business person?'], ['p_hero', 'Are they famous for bravery or a daring feat?'],
  ]);
  tq('person', 'When did they become famous?', { any: P_ROLES }, [
    ['p_b1970', 'Were they famous before 1970?', { notNo: ['p_b1980', 'p_b1990', 'p_b2000', 'p_b2010'] }],
    ['p_b1980', 'Were they famous before 1980?', { not: ['p_b1970'], notNo: ['p_b1990', 'p_b2000', 'p_b2010'] }],
    ['p_b1990', 'Were they famous before 1990?', { not: ['p_b1970', 'p_b1980'], notNo: ['p_b2000', 'p_b2010'] }],
    ['p_b2000', 'Were they famous before 2000?', { not: ['p_b1970', 'p_b1980', 'p_b1990'], notNo: ['p_b2010'] }],
    ['p_b2010', 'Were they famous before 2010?', { not: ['p_b1970', 'p_b1980', 'p_b1990', 'p_b2000'] }],
  ]);
  tq('person', 'Their music', { needs: ['p_music'] }, [
    ['p_band', 'Have they been in a band or group?'], ['p_boyband', 'Were they in a boy band or girl group?', { needs: ['p_band'] }],
    ['p_frontman', 'Were they the main singer of their band?', { needs: ['p_band'] }], ['p_solo', 'Have they had hits as a solo artist?'],
    ['p_number1', 'Have they had a UK number one?'], ['p_christmas1', 'Have they had a Christmas number one?', { needs: ['p_number1'] }],
    ['p_songwriter', 'Do they write their own songs?'], ['p_instrument', 'Do they play guitar or piano on stage?'],
    ['p_pop', 'Are they mainly a pop act?', { group: 'genre' }], ['p_rock', 'Are they mainly rock or indie?', { group: 'genre' }],
    ['p_rap', 'Are they a rapper or grime artist?', { group: 'genre' }], ['p_soul', 'Are they mainly soul, R&B or Motown?', { group: 'genre' }],
    ['p_dance', 'Are they mainly dance or electronic?', { group: 'genre' }], ['p_talent', 'Did they find fame on a TV talent show?'],
    ['p_judge', 'Have they been a judge on a TV talent show?'], ['p_acted', 'Have they also acted in films or TV dramas?'],
    ['p_brit', 'Have they won a Brit Award?'], ['p_grammy', 'Have they won a Grammy?'], ['p_glasto', 'Have they headlined Glastonbury?'],
    ['p_active', 'Are they still performing?', { needs: ['p_alive'] }],
  ]);
  tq('person', 'Their music', { needs: ['p_music'] }, [
    ['p_bondtheme', 'Have they sung a James Bond theme?'], ['p_eurovision', 'Have they sung at Eurovision?'],
    ['p_xfactorwin', 'Did they win The X Factor?', { needs: ['p_talent'] }],
  ]);
  tq('person', 'Which group?', { needs: ['p_boyband'], group: 'bb' }, [
    ['p_takethat', 'Were they in Take That?', { not: ['p_woman'] }], ['p_westlife', 'Were they in Westlife?', { not: ['p_woman'] }],
    ['p_boyzone', 'Were they in Boyzone?', { not: ['p_woman'] }], ['p_1d', 'Were they in One Direction?', { not: ['p_woman'] }],
    ['p_busted', 'Were they in Busted or McFly?', { not: ['p_woman'] }], ['p_spice', 'Were they in the Spice Girls?', { not: ['p_man'] }],
    ['p_girlsaloud', 'Were they in Girls Aloud?', { not: ['p_man'] }], ['p_littlemix', 'Were they in Little Mix?', { not: ['p_man'] }],
    ['p_sugababes', 'Were they in the Sugababes?', { not: ['p_man'] }], ['p_steps', 'Were they in Steps?'],
  ]);
  tq('person', 'Which band?', { needs: ['p_band'], not: ['p_boyband'], group: 'bandname' }, [
    ['p_beatles', 'Were they in the Beatles?'], ['p_stones', 'Were they in the Rolling Stones?'], ['p_queenband', 'Were they in Queen?'],
    ['p_oasis', 'Were they in Oasis?'], ['p_police', 'Were they in the Police?'], ['p_coldplay', 'Were they in Coldplay?'], ['p_u2', 'Were they in U2?'],
    ['p_abba', 'Were they in ABBA?'], ['p_arctic', 'Were they in Arctic Monkeys?'], ['p_direstraits', 'Were they in Dire Straits?'],
  ]);
  tq('person', 'Their acting', { needs: ['p_actor'] }, [
    ['p_hollywood', 'Have they starred in Hollywood films?'], ['p_oscar', 'Have they won an Oscar?'], ['p_soap', 'Have they been in a soap?'],
    ['p_sitcom', 'Have they starred in a sitcom?'], ['p_funny', 'Are they best known for comedy roles?'], ['p_action', 'Are they known for action films?'],
    ['p_bond', 'Have they been in a James Bond film?'], ['p_superhero', 'Have they played a superhero?'], ['p_potter', 'Have they been in a Harry Potter film?'],
    ['p_whoactor', 'Have they been in Doctor Who?'], ['p_voice', 'Have they voiced an animated character?'], ['p_sang', 'Have they sung in a musical film or show?'],
    ['p_period', 'Are they known for costume or period dramas?'], ['p_stage', 'Are they known for theatre and Shakespeare?'],
  ]);
  tq('person', 'Which roles?', { needs: ['p_actor'] }, [
    ['p_corrie', 'Have they been in Coronation Street?', { needs: ['p_soap'], group: 'soapname' }], ['p_eastenders', 'Have they been in EastEnders?', { needs: ['p_soap'], group: 'soapname' }],
    ['p_emmerdale', 'Have they been in Emmerdale?', { needs: ['p_soap'], group: 'soapname' }], ['p_hollyoaks', 'Have they been in Hollyoaks?', { needs: ['p_soap'], group: 'soapname' }],
    ['p_marvel', 'Have they been in a Marvel film?', { needs: ['p_hollywood'] }], ['p_starwars', 'Have they been in a Star Wars film?', { needs: ['p_hollywood'] }],
  ]);
  tq('person', 'Their sport', { needs: ['p_sport'] }, [
    ['p_football', 'Are they a footballer?', { group: 'sport' }], ['p_cricket', 'Are they a cricketer?', { group: 'sport' }], ['p_tennis', 'Do they play tennis?', { group: 'sport' }],
    ['p_rugby', 'Do they play rugby?', { group: 'sport' }], ['p_athletics', 'Are they an athlete (running, jumping or throwing)?', { group: 'sport' }],
    ['p_boxing', 'Are they a boxer or fighter?', { group: 'sport' }], ['p_motor', 'Are they a racing driver?', { group: 'sport' }], ['p_golf', 'Are they a golfer?', { group: 'sport' }],
    ['p_cycling', 'Are they a cyclist?', { group: 'sport' }], ['p_swim', 'Are they a swimmer or diver?', { group: 'sport' }], ['p_cue', 'Do they play darts or snooker?', { group: 'sport' }],
    ['p_country', 'Have they represented their country?'], ['p_captain', 'Have they captained their country?', { needs: ['p_country'] }],
    ['p_olympic', 'Have they won an Olympic medal?'], ['p_world', 'Have they been world champion or won a World Cup?'],
    ['p_spoty', 'Have they won BBC Sports Personality of the Year?'], ['p_retired', 'Have they retired from playing?'],
    ['p_pundit', 'Are they a TV pundit or commentator?'], ['p_manager', 'Have they been a manager or coach?'],
    ['p_toon', 'Have they played for Newcastle?', { needs: ['p_football'] }], ['p_mackem', 'Have they played for Sunderland?', { needs: ['p_football'] }],
    ['p_prem', 'Have they played in the Premier League?', { needs: ['p_football'] }], ['p_manutd', 'Have they played for Manchester United?', { needs: ['p_football'] }],
    ['p_liverpool', 'Have they played for Liverpool?', { needs: ['p_football'] }], ['p_striker', 'Are they a striker?', { needs: ['p_football'], group: 'pos' }],
    ['p_keeper', 'Are they a goalkeeper?', { needs: ['p_football'], group: 'pos' }],
  ]);
  tq('person', 'Which clubs?', { needs: ['p_football'] }, [
    ['p_arsenal', 'Have they played for Arsenal?'], ['p_chelsea', 'Have they played for Chelsea?'], ['p_mancity', 'Have they played for Manchester City?'],
    ['p_spurs', 'Have they played for Spurs?'], ['p_everton', 'Have they played for Everton?'], ['p_boro', 'Have they played for Middlesbrough?'],
    ['p_leeds', 'Have they played for Leeds?'], ['p_abroad', 'Have they played for a club abroad?'], ['p_ballon', "Have they won the Ballon d'Or?"],
  ]);
  tq('person', 'Their TV work', { needs: ['p_tv'] }, [
    ['p_reality', 'Did they find fame on reality TV?'], ['p_gameshow', 'Have they hosted a quiz or game show?'], ['p_chat', 'Have they hosted a chat show?'],
    ['p_saturday', 'Have they fronted Saturday-night TV?'], ['p_cook', 'Are they a TV cook or chef?'], ['p_nature', 'Do they present nature or travel shows?'],
    ['p_news', 'Are they a newsreader or journalist?'], ['p_duo', 'Are they half of a presenting double act?'], ['p_strictly', 'Have they been a contestant on Strictly?'],
    ['p_jungle', "Have they been a contestant on I'm a Celebrity?"], ['p_daytime', 'Have they presented breakfast or daytime TV?'], ['p_kidstv', "Did they start on children's TV?"],
  ]);
  tq('person', 'Which shows?', { needs: ['p_tv'] }, [
    ['p_takeaway', 'Have they presented Saturday Night Takeaway?'], ['p_imceleb', "Have they presented I'm a Celebrity?"],
    ['p_bgt', "Have they hosted or judged Britain's Got Talent?"], ['p_bakeoff', 'Have they presented or judged Bake Off?'],
    ['p_topgear', 'Have they presented Top Gear?'], ['p_bluepeter', 'Have they presented Blue Peter?'], ['p_thismorning', 'Have they presented This Morning?'],
  ]);
  tq('person', 'Their comedy', { needs: ['p_comedy'] }, [
    ['p_standup', 'Are they a stand-up comic?'], ['p_panel', 'Are they a regular on TV panel shows?'], ['p_csitcom', 'Have they starred in a sitcom?'],
    ['p_double', 'Are they part of a double act?'], ['p_characters', 'Are they known for playing comic characters?'], ['p_silent', 'Are they known for visual or silent comedy?'],
    ['p_cfilm', 'Have they starred in films?'],
  ]);
  tq('person', 'Which shows?', { needs: ['p_comedy'] }, [
    ['p_blackadder', 'Were they in Blackadder?'], ['p_python', 'Were they in Monty Python?'],
  ]);
  tq('person', 'Their politics', { needs: ['p_politics'] }, [
    ['p_pm', 'Have they been Prime Minister?'], ['p_president', 'Have they been a president?'], ['p_mp', 'Have they been a UK MP?'],
    ['p_labour', 'Are they Labour?', { group: 'party' }], ['p_tory', 'Are they Conservative?', { group: 'party' }], ['p_inoffice', 'Are they in office now?'],
    ['p_wartime', 'Did they lead a country in a war?'], ['p_resigned', 'Did they resign or get forced out?'],
  ]);
  tq('person', 'Their royal life', { needs: ['p_royal'] }, [
    ['p_monarch', 'Have they been king or queen?'], ['p_heir', 'Are they in line to the throne?'], ['p_marriedin', 'Did they marry into the royal family?'],
    ['p_tudor', 'Were they a Tudor?'], ['p_divorced', 'Have they been divorced?'],
  ]);
  tq('person', 'Their writing', { needs: ['p_writer'] }, [
    ['p_kidsbooks', "Do they write children's books?"], ['p_crime', 'Do they write crime or thrillers?'], ['p_poet', 'Are they a poet?'], ['p_plays', 'Did they write plays?'],
    ['p_fantasy', 'Do they write fantasy or science fiction?'], ['p_filmed', 'Have their books been made into films?'], ['p_bookseries', 'Did they write a famous series of books?'],
    ['p_school', 'Are their books studied at school?'],
  ]);
  tq('person', 'Their work', { needs: ['p_science'] }, [
    ['p_invented', 'Did they invent something we still use?'], ['p_theory', 'Are they famous for a theory or law?'], ['p_space', 'Are they linked to space or the stars?'],
    ['p_medicine', 'Are they linked to medicine?'], ['p_nobel', 'Did they win a Nobel Prize?'], ['p_tvsci', 'Do they present science on TV?'],
  ]);
  tq('person', 'Their business', { needs: ['p_business'] }, [
    ['p_billion', 'Are they a billionaire?'], ['p_techco', 'Did they found a tech company?'], ['p_shopco', 'Did they found a shop or high-street brand?'],
    ['p_den', "Have they been on Dragons' Den or The Apprentice?"], ['p_rocket', 'Have they run a space company?'],
  ]);
  tq('person', 'Their feat', { needs: ['p_hero'] }, [
    ['p_sea', 'Did their feat happen at sea?'], ['p_war', 'Are they linked to a war?'], ['p_rescue', 'Did they save lives?'],
    ['p_explore', 'Were they an explorer or adventurer?'], ['p_astro', 'Have they been into space?'], ['p_nurse', 'Were they a nurse or doctor?'],
  ]);
  // ---- a fictional character ----
  tq('character', 'About them', {}, [
    ['c_human', 'Are they human?'], ['c_animal', 'Are they an animal?', { not: ['c_human'] }],
    ['c_male', 'Are they male?', { pair: 'c_female' }], ['c_female', 'Are they female?', { pair: 'c_male' }],
    ['c_hero', 'Are they a goodie?', { pair: 'c_villain' }], ['c_villain', 'Are they a baddie?', { pair: 'c_hero' }],
    ['c_kids', 'Are they mainly for children?'], ['c_animated', 'Are they animated, a cartoon or a puppet?'], ['c_powers', 'Do they have special powers or magic?'],
    ['c_british', 'Are they British?', { group: 'cnat' }], ['c_american', 'Are they American?', { group: 'cnat' }],
    ['c_old', 'Did they first appear before 1980?'], ['c_hat', 'Do they usually wear a hat?'], ['c_royal', 'Are they a king, queen, prince or princess?'],
    ['c_christmas', 'Are they linked to Christmas?'], ['c_school', 'Do they go to school?'], ['c_detective', 'Are they a detective or spy?'],
  ]);
  tq('character', 'Where do they appear?', {}, [
    ['c_film', 'Are they best known from films?', { group: 'med' }], ['c_tv', 'Are they best known from TV?', { group: 'med' }],
    ['c_book', 'Did they start in a book?', { group: 'med' }], ['c_game', 'Are they from a video game?', { group: 'med' }], ['c_comic', 'Did they start in comics?', { group: 'med' }],
    ['c_franchise', 'Have they been in more than three films?', { needs: ['c_film'] }], ['c_starwars', 'Are they from Star Wars?', { needs: ['c_film'] }],
    ['c_potter', 'Are they from Harry Potter?', { any: ['c_film', 'c_book'] }], ['c_soapc', 'Are they from a soap?', { needs: ['c_tv'] }],
    ['c_sitcomc', 'Are they from a sitcom?', { needs: ['c_tv'] }], ['c_classic', 'Are they from a book over 100 years old?', { needs: ['c_book'] }],
    ['c_bookseries', 'Are they in a series of books?', { needs: ['c_book'] }],
  ]);
  tq('character', 'What sort of animal?', { needs: ['c_animal'] }, [
    ['c_bear', 'Are they a bear?', { group: 'sp' }], ['c_dog', 'Are they a dog?', { group: 'sp' }], ['c_cat', 'Are they a cat?', { group: 'sp' }],
    ['c_mouse', 'Are they a mouse or rat?', { group: 'sp' }], ['c_pig', 'Are they a pig?', { group: 'sp' }], ['c_bird', 'Are they a bird?', { group: 'sp' }],
    ['c_rabbit', 'Are they a rabbit?', { group: 'sp' }], ['c_lion', 'Are they a lion?', { group: 'sp' }],
    ['c_talks', 'Can they talk?'], ['c_clothes', 'Do they wear clothes?'],
  ]);
  tq('character', 'Cartoons', { needs: ['c_animated'] }, [
    ['c_disney', 'Are they a Disney character?', { group: 'studio' }], ['c_pixar', 'Are they from Pixar?', { group: 'studio' }],
    ['c_simpsons', 'Are they from The Simpsons?', { group: 'studio' }], ['c_stopmotion', 'Are they stop-motion or a puppet?'],
  ]);
  tq('character', 'Their powers', { needs: ['c_powers'] }, [
    ['c_super', 'Are they a superhero?'], ['c_marvel', 'Are they from Marvel?', { needs: ['c_super'] }], ['c_mask', 'Do they wear a mask?'],
    ['c_fly', 'Can they fly?'], ['c_wizard', 'Do they cast spells?'], ['c_alien', 'Are they from another planet?'],
  ]);
  // ---- an animal ----
  tq('character', 'Which story?', {}, [
    ['c_toystory', 'Are they from Toy Story?', { needs: ['c_pixar'] }], ['c_lionking', 'Are they from The Lion King?', { needs: ['c_disney'], group: 'dfilm' }],
    ['c_frozen', 'Are they from Frozen?', { needs: ['c_disney'], group: 'dfilm' }], ['c_muppet', 'Are they a Muppet?', { needs: ['c_animated'] }],
    ['c_wallace', 'Are they from Wallace and Gromit?', { needs: ['c_stopmotion'] }], ['c_dc', 'Are they from DC Comics?', { needs: ['c_super'], not: ['c_marvel'] }],
  ]);
  tq('animal', 'What sort of animal?', { group: 'class' }, [
    ['a_mammal', 'Is it a mammal?'], ['a_bird', 'Is it a bird?'], ['a_reptile', 'Is it a reptile?'], ['a_fish', 'Is it a fish?'],
    ['a_insect', 'Is it an insect, spider or bug?'], ['a_amphibian', 'Is it a frog, toad or newt?'],
  ]);
  tq('animal', 'About it', {}, [
    ['a_pet', 'Is it a common pet?'], ['a_farm', 'Is it a farm animal?'], ['a_wildbritain', 'Is it found wild in Britain?'], ['a_zoo', 'Would you see it at a zoo?'],
    ['a_bigger', 'Is it bigger than a person?', { pair: 'a_small' }], ['a_small', 'Is it smaller than a cat?', { pair: 'a_bigger' }],
    ['a_fourlegs', 'Does it have four legs?'], ['a_fly', 'Can it fly?'], ['a_water', 'Does it live in or around water?'], ['a_sea', 'Does it live in the sea?', { needs: ['a_water'] }],
    ['a_meat', 'Does it eat meat?'], ['a_plants', 'Does it eat plants?'], ['a_danger', 'Can it be dangerous to people?'], ['a_venom', 'Is it venomous or poisonous?'],
    ['a_stripes', 'Does it have stripes or spots?'], ['a_blackwhite', 'Is it black and white?'], ['a_horns', 'Does it have horns, antlers or tusks?'], ['a_tail', 'Does it have a long tail?'],
    ['a_herd', 'Does it live in a herd, pack or colony?'], ['a_eggs', 'Does it lay eggs?'], ['a_nocturnal', 'Is it mostly active at night?'], ['a_hibernate', 'Does it hibernate?'],
    ['a_fast', 'Is it famous for being fast?'], ['a_endangered', 'Is it endangered?'], ['a_eat', 'Do people in Britain eat it?'],
  ]);
  tq('animal', 'Where does it live?', {}, [
    ['a_africa', 'Is it found in Africa?'], ['a_asia', 'Is it found in Asia?'], ['a_australia', 'Is it found in Australia?'], ['a_americas', 'Is it found in the Americas?'],
  ]);
  tq('animal', 'Which mammal?', { needs: ['a_mammal'], group: 'fam' }, [
    ['a_catfam', 'Is it in the cat family?'], ['a_dogfam', 'Is it in the dog family?'], ['a_hooves', 'Does it have hooves?'], ['a_ape', 'Is it a monkey or ape?'],
    ['a_rodent', 'Is it a rodent?'], ['a_marsupial', 'Is it a marsupial?'], ['a_whale', 'Is it a whale, dolphin or seal?'], ['a_bear', 'Is it a bear?'],
  ]);
  tq('animal', 'Which bird?', { needs: ['a_bird'] }, [
    ['a_flightless', "Is it a bird that can't fly?"], ['a_prey', 'Is it a bird of prey?'], ['a_garden', 'Would you see it in a British garden?'],
    ['a_swims', 'Does it swim?'], ['a_talkbird', 'Can it copy speech?'], ['a_colourful', 'Is it brightly coloured?'],
  ]);
  tq('animal', 'Which creepy-crawly?', { needs: ['a_insect'] }, [['a_sting', 'Can it sting?'], ['a_eightlegs', 'Does it have eight legs?']]);
  tq('animal', 'Which reptile?', { needs: ['a_reptile'] }, [['a_snake', 'Is it a snake?'], ['a_shell', 'Does it have a shell?']]);
  // ---- a place ----
  tq('place', 'Where is it?', {}, [
    ['pl_uk', 'Is it in the UK?'],
    ['pl_europe', 'Is it in Europe?', { group: 'cont', not: ['pl_uk'] }], ['pl_americas', 'Is it in the Americas?', { group: 'cont', not: ['pl_uk'] }],
    ['pl_asia', 'Is it in Asia?', { group: 'cont', not: ['pl_uk'] }], ['pl_africa', 'Is it in Africa?', { group: 'cont', not: ['pl_uk'] }],
    ['pl_oceania', 'Is it in Australia or the Pacific?', { group: 'cont', not: ['pl_uk'] }],
    ['pl_england', 'Is it in England?', { needs: ['pl_uk'], group: 'part' }], ['pl_scotland', 'Is it in Scotland?', { needs: ['pl_uk'], group: 'part' }],
    ['pl_wales', 'Is it in Wales?', { needs: ['pl_uk'], group: 'part' }], ['pl_ni', 'Is it in Northern Ireland?', { needs: ['pl_uk'], group: 'part' }],
    ['pl_northeast', 'Is it in the North East?', { needs: ['pl_uk'], not: ['pl_scotland', 'pl_wales', 'pl_ni'] }],
    ['pl_north', 'Is it in the north of England?', { needs: ['pl_uk'], not: ['pl_scotland', 'pl_wales', 'pl_ni', 'pl_northeast'] }],
    ['pl_london', 'Is it in London?', { needs: ['pl_uk'], not: ['pl_scotland', 'pl_wales', 'pl_ni', 'pl_northeast', 'pl_north'] }],
  ]);
  tq('place', 'Which country or area?', {}, [
    ['pl_france', 'Is it in France?', { needs: ['pl_europe'], group: 'ctry' }], ['pl_italy', 'Is it in Italy?', { needs: ['pl_europe'], group: 'ctry' }],
    ['pl_spain', 'Is it in Spain?', { needs: ['pl_europe'], group: 'ctry' }], ['pl_germany', 'Is it in Germany?', { needs: ['pl_europe'], group: 'ctry' }],
    ['pl_usa', 'Is it in the USA?', { needs: ['pl_americas'] }], ['pl_canada', 'Is it in Canada?', { needs: ['pl_americas'] }],
    ['pl_nyc', 'Is it in New York?', { needs: ['pl_usa'] }],
    ['pl_tyneside', 'Is it on Tyneside?', { needs: ['pl_northeast'] }], ['pl_sunderland', 'Is it in Sunderland?', { needs: ['pl_northeast'], not: ['pl_tyneside'] }],
    ['pl_northumberland', 'Is it in Northumberland?', { needs: ['pl_northeast'], not: ['pl_tyneside', 'pl_sunderland'] }],
    ['pl_durham', 'Is it in County Durham?', { needs: ['pl_northeast'], not: ['pl_tyneside', 'pl_sunderland', 'pl_northumberland'] }],
  ]);
  tq('place', 'What is it?', {}, [
    ['pl_country', 'Is it a country?', { group: 'ptype' }], ['pl_city', 'Is it a city or town?', { group: 'ptype' }], ['pl_region', 'Is it a region, county or state?', { group: 'ptype' }],
    ['pl_building', 'Is it a building or landmark?', { group: 'ptype' }], ['pl_natural', 'Is it a natural feature?', { group: 'ptype' }], ['pl_island', 'Is it an island?'],
    ['pl_capital', 'Is it a capital city?', { needs: ['pl_city'] }], ['pl_bigpop', 'Do more than a million people live there?', { any: ['pl_city', 'pl_country', 'pl_region'] }],
    ['pl_english', 'Do they speak English there?', { any: ['pl_city', 'pl_country', 'pl_region'], not: ['pl_uk'] }],
    ['pl_olympics', 'Has it hosted the Olympics?', { any: ['pl_city', 'pl_country'] }], ['pl_club', 'Is it home to a famous football club?', { needs: ['pl_city'] }],
    ['pl_religious', 'Is it a church, cathedral or temple?', { needs: ['pl_building'], group: 'bld' }], ['pl_castle', 'Is it a castle or palace?', { needs: ['pl_building'], group: 'bld' }],
    ['pl_stadium', 'Is it a stadium?', { needs: ['pl_building'], group: 'bld' }], ['pl_bridge', 'Is it a bridge?', { needs: ['pl_building'], group: 'bld' }],
    ['pl_statue', 'Is it a statue or sculpture?', { needs: ['pl_building'], group: 'bld' }], ['pl_tall', 'Is it taller than 100 metres?', { needs: ['pl_building'] }],
    ['pl_old', 'Is it over 500 years old?', { needs: ['pl_building'] }],
    ['pl_mountain', 'Is it a mountain or hill?', { needs: ['pl_natural'], group: 'nat' }], ['pl_waterfeat', 'Is it a river, lake, waterfall or sea?', { needs: ['pl_natural'], group: 'nat' }],
    ['pl_beach', 'Is it a beach or stretch of coast?', { needs: ['pl_natural'], group: 'nat' }], ['pl_forest', 'Is it a forest, park or moor?', { needs: ['pl_natural'], group: 'nat' }],
  ]);
  tq('place', 'About it', {}, [
    ['pl_sea', 'Is it by the sea?'], ['pl_river', 'Is it on a river?'], ['pl_hot', 'Is it usually hot there?'], ['pl_snow', 'Does it often get snow?'],
    ['pl_tourist', 'Is it a big tourist attraction?'], ['pl_heritage', 'Is it (or is it home to) a World Heritage Site?'],
  ]);
  // ---- food or drink ----
  tq('food', 'Food or drink?', {}, [['f_drink', 'Is it a drink?']]);
  tq('food', 'The drink', { needs: ['f_drink'] }, [
    ['f_alcohol', 'Does it contain alcohol?'], ['f_beer', 'Is it a beer, lager or cider?', { needs: ['f_alcohol'], group: 'alc' }],
    ['f_spirit', 'Is it a spirit?', { needs: ['f_alcohol'], group: 'alc' }], ['f_wine', 'Is it wine or champagne?', { needs: ['f_alcohol'], group: 'alc' }],
    ['f_cocktail', 'Is it a cocktail?', { needs: ['f_alcohol'], group: 'alc' }], ['f_fizzy', 'Is it fizzy?'], ['f_hotdrink', 'Is it drunk hot?'],
    ['f_milk', 'Is it made with milk?'], ['f_juice', 'Is it a fruit juice?'], ['f_caffeine', 'Does it contain caffeine?'],
  ]);
  tq('food', 'The food', { not: ['f_drink'] }, [
    ['f_sweet', 'Is it sweet?'], ['f_hot', 'Is it usually served hot?'], ['f_fruitveg', 'Is it a fruit or vegetable?'], ['f_fruit', 'Is it a fruit?', { needs: ['f_fruitveg'] }],
    ['f_tropical', 'Does it grow in hot countries?', { needs: ['f_fruitveg'] }], ['f_raw', 'Is it usually eaten raw?'],
    ['f_meat', 'Does it contain meat or fish?'], ['f_fish', 'Does it contain fish or seafood?', { needs: ['f_meat'] }], ['f_pork', 'Does it contain pork?', { needs: ['f_meat'] }],
    ['f_beef', 'Does it contain beef?', { needs: ['f_meat'] }], ['f_chicken', 'Does it contain chicken?', { needs: ['f_meat'] }], ['f_egg', 'Does it contain egg?'],
    ['f_dairy', 'Does it contain dairy?'], ['f_cheese', 'Does it contain cheese?', { needs: ['f_dairy'] }], ['f_chocolate', 'Does it contain chocolate?', { needs: ['f_sweet'] }],
    ['f_cake', 'Is it a cake, biscuit or pudding?', { needs: ['f_sweet'] }], ['f_pastry', 'Is it made with pastry?'], ['f_bread', 'Is it bread or served in bread?'],
    ['f_potato', 'Is it made from potato?'], ['f_rice', 'Does it contain rice or pasta?'], ['f_fried', 'Is it fried?'], ['f_hands', 'Do you eat it with your hands?'],
    ['f_takeaway', 'Is it a takeaway favourite?'], ['f_breakfast', 'Is it eaten at breakfast?'], ['f_snack', 'Is it a snack?'], ['f_round', 'Is it round?'],
  ]);
  tq('food', 'About it', {}, [
    ['f_brand', 'Is it a brand name?'], ['f_christmas', 'Is it linked to Christmas?'], ['f_orange', 'Is it orange?'],
    ['f_british', 'Is it a British classic?', { group: 'origin' }], ['f_scot', 'Is it Scottish?', { needs: ['f_british'] }], ['f_northeast', 'Is it from the North East?', { needs: ['f_british'] }],
    ['f_italian', 'Is it Italian?', { group: 'origin' }], ['f_indian', 'Is it Indian?', { group: 'origin' }], ['f_chinese', 'Is it Chinese?', { group: 'origin' }],
    ['f_japanese', 'Is it Japanese?', { group: 'origin' }], ['f_american', 'Is it American?', { group: 'origin' }], ['f_mexican', 'Is it Mexican?', { group: 'origin' }],
    ['f_french', 'Is it French?', { group: 'origin' }],
  ]);
  // ---- an object ----
  tq('object', 'What is it for?', { group: 'use' }, [
    ['o_vehicle', 'Is it a vehicle?'], ['o_wear', 'Do you wear it?'], ['o_toy', 'Is it a toy or game?'], ['o_tool', 'Is it a tool?'], ['o_sport', 'Is it used in sport?'],
    ['o_music', 'Is it a musical instrument?'], ['o_eat', 'Is it used for eating or drinking?'], ['o_cook', 'Is it used for cooking?'], ['o_clean', 'Is it used for cleaning?'],
    ['o_write', 'Is it used for writing or drawing?'], ['o_furniture', 'Is it furniture?'], ['o_comm', 'Is it used to communicate?'], ['o_money', 'Is it to do with money?'],
    ['o_time', 'Does it tell the time?'],
  ]);
  tq('object', 'Where would you find it?', {}, [
    ['o_home', 'Would you find it in most homes?'],
    ['o_kitchen', 'Is it kept in the kitchen?', { needs: ['o_home'], group: 'room' }], ['o_bathroom', 'Is it kept in the bathroom?', { needs: ['o_home'], group: 'room' }],
    ['o_bedroom', 'Is it kept in the bedroom?', { needs: ['o_home'], group: 'room' }], ['o_living', 'Is it kept in the living room?', { needs: ['o_home'], group: 'room' }],
    ['o_garden', 'Is it used in the garden?'], ['o_office', 'Is it used at school or work?'],
  ]);
  tq('object', 'About it', {}, [
    ['o_electric', 'Does it use electricity or batteries?'], ['o_screen', 'Does it have a screen?', { needs: ['o_electric'] }], ['o_plug', 'Does it plug into the wall?', { needs: ['o_electric'] }],
    ['o_internet', 'Does it connect to the internet?', { needs: ['o_electric'] }],
    ['o_pocket', 'Can it fit in your pocket?', { pair: 'o_heavy' }], ['o_heavy', 'Is it heavier than a person?', { pair: 'o_pocket' }], ['o_hold', 'Do you hold it in your hand to use it?'],
    ['o_metal', 'Is it mostly metal?', { group: 'mat' }], ['o_wood', 'Is it mostly wood?', { group: 'mat' }], ['o_plastic', 'Is it mostly plastic?', { group: 'mat' }],
    ['o_glass', 'Is it mostly glass?', { group: 'mat' }], ['o_paper', 'Is it mostly paper or card?', { group: 'mat' }], ['o_fabric', 'Is it mostly fabric?', { group: 'mat' }],
    ['o_old', 'Was it around before 1900?'], ['o_new', 'Was it invented after 1990?', { not: ['o_old'] }], ['o_sharp', 'Is it sharp?'], ['o_wheels', 'Does it have wheels?'],
    ['o_moving', 'Does it have moving parts?'], ['o_light', 'Does it give off light?'], ['o_sound', 'Does it make a sound or music?'], ['o_round', 'Is it round?'],
  ]);
  tq('object', 'More about it', {}, [
    ['o_engine', 'Does it have an engine?', { needs: ['o_vehicle'] }], ['o_flies', 'Does it fly?', { needs: ['o_vehicle'] }], ['o_boat', 'Does it go on water?', { needs: ['o_vehicle'] }],
    ['o_public', 'Is it public transport?', { needs: ['o_vehicle'] }], ['o_rails', 'Does it run on rails?', { needs: ['o_vehicle'] }],
    ['o_feet', 'Do you wear it on your feet?', { needs: ['o_wear'] }], ['o_head', 'Do you wear it on your head?', { needs: ['o_wear'] }],
    ['o_jewel', 'Is it jewellery?', { needs: ['o_wear'] }], ['o_warm', 'Is it worn to keep warm?', { needs: ['o_wear'] }],
    ['o_ball', 'Is it a ball?', { needs: ['o_sport'] }], ['o_hit', 'Do you hit something with it?', { needs: ['o_sport'] }],
    ['o_strings', 'Does it have strings?', { needs: ['o_music'] }], ['o_blow', 'Do you blow into it?', { needs: ['o_music'] }], ['o_keys', 'Does it have keys?', { needs: ['o_music'] }],
  ]);
  // ---- a film, TV show, book or song ----
  tq('title', 'What is it?', { group: 'med' }, [['t_film', 'Is it a film?'], ['t_tv', 'Is it a TV show?'], ['t_book', 'Is it a book?'], ['t_song', 'Is it a song?'], ['t_game', 'Is it a video game?']]);
  tq('title', 'When did it come out?', { group: 'era' }, [
    ['t_e_old', 'Did it come out before 1970?'], ['t_e_70', 'Did it come out in the 1970s?'], ['t_e_80', 'Did it come out in the 1980s?'],
    ['t_e_90', 'Did it come out in the 1990s?'], ['t_e_00', 'Did it come out in the 2000s?'], ['t_e_10', 'Did it come out in 2010 or later?'],
  ]);
  tq('title', 'About it', {}, [
    ['t_british', 'Is it British?', { group: 'orig' }], ['t_american', 'Is it American?', { group: 'orig' }], ['t_kids', 'Is it mainly for children?'],
    ['t_comedy', 'Is it a comedy?'], ['t_animated', 'Is it animated?'], ['t_series', 'Is it part of a series or franchise?'], ['t_scary', 'Is it scary?'],
    ['t_love', 'Is it a love story?'], ['t_christmas', 'Is it linked to Christmas?'], ['t_real', 'Is it based on a true story?'], ['t_scifi', 'Is it science fiction or fantasy?'],
    ['t_crime', 'Is it about crime or detectives?'], ['t_war', 'Is it about a war?'], ['t_sport', 'Is it about sport?'], ['t_animal', 'Is an animal a main character?'],
    ['t_northeast', 'Is it set in the North East?'], ['t_london', 'Is it set in London?'], ['t_named', "Is its title a character's name?"],
    ['t_bookfirst', 'Was it a book first?', { not: ['t_book', 't_song'] }],
  ]);
  tq('title', 'More about it', {}, [
    ['t_disney', 'Is it a Disney film?', { needs: ['t_film'] }], ['t_pixar', 'Is it a Pixar film?', { needs: ['t_film'] }], ['t_bestpic', 'Did it win the Best Picture Oscar?', { needs: ['t_film'] }],
    ['t_bond', 'Is it a James Bond film?', { needs: ['t_film'] }], ['t_superhero', 'Is it a superhero film?', { needs: ['t_film'] }], ['t_sequel', 'Is it a sequel?', { needs: ['t_film'] }],
    ['t_musical', 'Is it a musical?', { needs: ['t_film'] }],
    ['t_sitcom', 'Is it a sitcom?', { needs: ['t_tv'], group: 'genre' }], ['t_soap', 'Is it a soap?', { needs: ['t_tv'], group: 'genre' }], ['t_quiz', 'Is it a quiz or game show?', { needs: ['t_tv'], group: 'genre' }],
    ['t_reality', 'Is it reality TV?', { needs: ['t_tv'], group: 'genre' }], ['t_drama', 'Is it a drama?', { needs: ['t_tv'], group: 'genre' }],
    ['t_bbc', 'Is it on the BBC?', { needs: ['t_tv'], group: 'chan' }], ['t_itv', 'Is it on ITV?', { needs: ['t_tv'], group: 'chan' }], ['t_netflix', 'Is it on Netflix?', { needs: ['t_tv'], group: 'chan' }],
    ['t_running', 'Is it still being made?', { needs: ['t_tv'] }], ['t_long', 'Has it run for over 20 years?', { needs: ['t_tv'] }],
    ['t_number1', 'Was it a UK number one?', { needs: ['t_song'] }], ['t_xmas1', 'Was it a Christmas number one?', { needs: ['t_number1'] }],
    ['t_band', 'Is it by a band or group?', { needs: ['t_song'] }], ['t_male', 'Is it sung by a man?', { needs: ['t_song'] }], ['t_slow', 'Is it a slow song?', { needs: ['t_song'] }],
    ['t_dance', 'Is it a party or dance song?', { needs: ['t_song'] }], ['t_filmsong', 'Is it from a film?', { needs: ['t_song'] }], ['t_cover', 'Is it a cover version?', { needs: ['t_song'] }],
    ['t_novel', 'Is it a novel?', { needs: ['t_book'] }], ['t_picture', 'Is it a picture book?', { needs: ['t_book'] }], ['t_classic', 'Is it over 100 years old?', { needs: ['t_book'] }],
  ]);
  // ---- a brand or company ----
  tq('title', 'Which one?', {}, [
    ['t_oasis', 'Is it by Oasis?', { needs: ['t_song'], group: 'act' }], ['t_queen', 'Is it by Queen?', { needs: ['t_song'], group: 'act' }],
    ['t_beatles', 'Is it by the Beatles?', { needs: ['t_song'], group: 'act' }], ['t_wham', 'Is it by Wham! or George Michael?', { needs: ['t_song'], group: 'act' }],
    ['t_abba', 'Is it by ABBA?', { needs: ['t_song'], group: 'act' }],
    ['t_starwars', 'Is it a Star Wars film?', { needs: ['t_film'] }], ['t_hpfilm', 'Is it a Harry Potter film?', { needs: ['t_film'] }],
  ]);
  tq('brand', 'What does it do?', {}, [
    ['b_food', 'Does it sell food or drink?'], ['b_shop', 'Is it a shop or supermarket?'], ['b_tech', 'Is it a tech company?'], ['b_cars', 'Does it make cars?'],
    ['b_clothes', 'Does it sell clothes or shoes?'], ['b_sport', 'Is it a sports brand?'], ['b_bank', 'Is it a bank?'], ['b_airline', 'Is it an airline?'], ['b_online', 'Is it mainly online?'],
  ]);
  tq('brand', 'Where is it from?', { group: 'orig' }, [
    ['b_uk', 'Is it British?'], ['b_american', 'Is it American?'], ['b_german', 'Is it German?'], ['b_japanese', 'Is it Japanese?'], ['b_french', 'Is it French?'],
    ['b_northeast', 'Was it founded in the North East?', { needs: ['b_uk'], group: null }],
  ]);
  tq('brand', 'About it', {}, [
    ['b_old', 'Was it founded before 1950?'], ['b_logo', 'Is its logo an animal or a person?'], ['b_red', 'Is its logo mainly red?'], ['b_letters', 'Is its name letters or initials?'],
    ['b_person', 'Is it named after a person?'], ['b_highstreet', 'Is it on most high streets?'], ['b_luxury', 'Is it a luxury brand?'],
  ]);
  tq('brand', 'More about it', {}, [
    ['b_supermarket', 'Is it a supermarket?', { needs: ['b_shop'] }], ['b_fastfood', 'Is it a fast-food chain?', { needs: ['b_food'] }], ['b_coffee', 'Does it sell coffee?', { needs: ['b_food'] }],
    ['b_drinks', 'Does it mainly make drinks?', { needs: ['b_food'] }], ['b_sweets', 'Does it make sweets, chocolate or crisps?', { needs: ['b_food'] }],
    ['b_phone', 'Does it make phones or computers?', { needs: ['b_tech'] }], ['b_social', 'Is it a social media app?', { needs: ['b_tech'] }],
    ['b_search', 'Is it a search engine?', { needs: ['b_tech'] }], ['b_stream', 'Is it a streaming service?', { needs: ['b_tech'] }], ['b_games', 'Does it make games or consoles?', { needs: ['b_tech'] }],
    ['b_sportscar', 'Does it make luxury or sports cars?', { needs: ['b_cars'] }], ['b_ukfactory', 'Does it build cars in Britain?', { needs: ['b_cars'] }],
  ]);
  const twentyQ = (id) => TWENTY_KINDS.find((k) => k.id === id) || TWENTY_QS.find((x) => x.id === id) || null;
  /** The questions in one kind's branch, openers excluded. */
  const twentyBranch = (kind) => TWENTY_QS.filter((x) => x.cat === kind);
  /** The true answer to a question about this item: the openers from its kind, the rest from its facts. */
  function twentyYes(q, id) { return TWENTY_KINDS.some((k) => k.id === id) ? q.what === id : !!(q.facts || {})[id]; }
  /** Which questions a player can ask next, given what they've asked ([{id, yes}]): the openers until one is yes, then
   *  that kind's questions that the answers so far make worth asking (see the gates on TWENTY_QS). Never one already asked. */
  function twentyOpen(asked) {
    const done = new Set(asked.map((a) => a.id)), yes = new Set(asked.filter((a) => a.yes).map((a) => a.id)), no = new Set(asked.filter((a) => !a.yes).map((a) => a.id));
    const kind = TWENTY_KINDS.find((k) => yes.has(k.id));
    if (!kind) return TWENTY_KINDS.filter((k) => !done.has(k.id));
    const branch = twentyBranch(kind.id), closed = new Set(branch.filter((x) => x.group && yes.has(x.id)).map((x) => x.group));
    return branch.filter((x) => !done.has(x.id) && x.needs.every((n) => yes.has(n)) && (!x.any.length || x.any.some((n) => yes.has(n)))
      && !x.not.some((n) => yes.has(n)) && !x.notNo.some((n) => no.has(n)) && !(x.pair && done.has(x.pair)) && !(x.group && closed.has(x.group)));
  }
  /** The games that run on a bank of quick questions, like The Race. */
  const BANK_GAMES = ['race', 'potato', 'koth', 'blockbusters', 'chase'];
  /** Not a question: a title, a few lines and an optional picture or video on the screen and the phones. No clock, no points. */
  const SLIDE = { label: 'Slide', icon: '🪧', blurb: 'Not a question: a welcome, the rules, a break or a message, on the screen and the phones. No points.' };
  /** Label and icon for any item in a quiz, slides included. */
  function typeInfo(t, q) { return TYPES[t] || (t === 'slide' ? (q?.break ? BREAK : SLIDE) : { icon: '❓', label: String(t || ''), blurb: '' }); }
  /** A slide's text as HTML: lines starting "-", "•" or "1." become a list, the rest paragraphs. */
  function slideHtml(body) {
    let html = '', list = [];
    const flush = () => { if (list.length) { html += `<ul>${list.map((l) => `<li>${esc(l)}</li>`).join('')}</ul>`; list = []; } };
    for (const raw of String(body || '').split(/\r?\n/)) {
      const l = raw.trim(); if (!l) { flush(); continue; }
      const m = l.match(/^(?:[-•*]|\d+[.)])\s+(.*)$/);
      if (m) list.push(m[1]); else { flush(); html += `<p>${esc(l)}</p>`; }
    }
    flush(); return html;
  }
  /** A break slide: a slide with a countdown clock. */
  const BREAK = { label: 'Break', icon: '☕', blurb: 'A big countdown clock on the screen and the phones, for half-time or a bar run. Add or take off minutes while it runs.' };
  function breakMs(q) { return clamp(Math.round(+q?.breakMins || 10), 1, 120) * 60000; }
  /** 9:05, or 1:02:05 for an hour or more. */
  function clockText(ms) { const t = Math.max(0, Math.ceil(ms / 1000)), h = Math.floor(t / 3600), m = Math.floor((t % 3600) / 60), s = t % 60; return h ? `${h}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}` : `${m}:${String(s).padStart(2, '0')}`; }
  /** The countdown ring: minute ticks round the edge, an arc that drains, the time in the middle. Ids get a prefix so screen and phone can differ. */
  function breakClockHtml(p = 'brk') {
    return `<div class="brkclock" id="${p}Clock"><svg viewBox="0 0 200 200" aria-hidden="true"><circle class="ticks" cx="100" cy="100" r="95" pathLength="120"/><circle class="trk" cx="100" cy="100" r="82"/><circle class="arc" id="${p}Arc" cx="100" cy="100" r="82" pathLength="1000" transform="rotate(-90 100 100)"/></svg><div class="brktime"><span id="${p}Time">0:00</span><small id="${p}Note">left of the break</small></div></div>`;
  }
  /** Moves a clock drawn by breakClockHtml on to `rem` of `total` ms. */
  function setBreakClock(p, rem, total) {
    const c = document.getElementById(p + 'Clock'); if (!c) return;
    const f = total > 0 ? clamp(rem / total, 0, 1) : 0;
    document.getElementById(p + 'Arc').style.strokeDashoffset = String(1000 * (1 - f));
    document.getElementById(p + 'Time').textContent = rem > 0 ? clockText(rem) : '0:00';
    document.getElementById(p + 'Note').textContent = rem > 0 ? 'left of the break' : "time's up!";
    c.classList.toggle('warn', rem > 0 && rem <= 120000); c.classList.toggle('end', rem > 0 && rem <= 30000); c.classList.toggle('over', rem <= 0);
  }
  // ---- Wheel of Fortune board: the show's four rows of 12/14/14/12 tiles ----
  const WHEEL_ROWS = [12, 14, 14, 12];
  /** Lays the phrase's words onto the board, centred, never splitting a word. Returns rows of tiles or null if it will not fit. */
  function wheelLayout(phrase) {
    const words = String(phrase || '').toUpperCase().replace(/\s+/g, ' ').trim().split(' ').filter(Boolean);
    if (!words.length) return null;
    // Greedy fill of the middle rows first (they are longest), then the outer ones, keeping word order top to bottom.
    const tryFit = (rowsOrder) => {
      const lines = WHEEL_ROWS.map(() => []); let wi = 0;
      for (const r of rowsOrder) { let len = 0; while (wi < words.length) { const w = words[wi]; const need = (len ? 1 : 0) + w.length; if (len + need > WHEEL_ROWS[r]) break; lines[r].push(w); len += need; wi++; } }
      return wi === words.length ? lines : null;
    };
    const total = words.join(' ').length;
    let lines = null;
    if (total <= 14) lines = tryFit([1]) || tryFit([1, 2]);
    if (!lines) lines = tryFit([1, 2]) || tryFit([0, 1, 2]) || tryFit([1, 2, 3]) || tryFit([0, 1, 2, 3]);
    if (!lines) return null;
    return lines.map((ws, r) => {
      const text = ws.join(' '), width = WHEEL_ROWS[r], pad = Math.floor((width - text.length) / 2);
      const tiles = [];
      for (let i = 0; i < width; i++) { const ch = text[i - pad]; tiles.push(!ch ? { t: 'off' } : ch === ' ' ? { t: 'gap' } : /[A-Z]/.test(ch) ? { t: 'L', ch } : { t: 'sym', ch }); }
      return tiles;
    });
  }
  /** The board as HTML. `revealed` is a string of letters already turned; `all` shows everything. */
  function wheelBoardHtml(layout, revealed = '', all = false) {
    if (!layout) return '';
    const rev = new Set(String(revealed).toUpperCase());
    return `<div class="wof">${layout.map((row) => `<div class="wof-row">${row.map((t) => t.t === 'off' ? '<span class="wt off"></span>' : t.t === 'gap' ? '<span class="wt gap"></span>' : t.t === 'sym' ? `<span class="wt on">${esc(t.ch)}</span>` : (all || rev.has(t.ch)) ? `<span class="wt on lit">${t.ch}</span>` : '<span class="wt on"></span>').join('')}</div>`).join('')}</div>`;
  }
  /** Answer Smash: the longest run of letters that ends the first answer and starts the second. */
  function smashOf(a, b) {
    const letters = (s) => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]/g, '');
    const la = letters(a), lb = letters(b);
    let n = 0;
    for (let k = Math.min(la.length - 1, lb.length - 1); k >= 1; k--) if (la.slice(-k) === lb.slice(0, k)) { n = k; break; }
    if (!n) return { smash: '', overlap: 0 };
    // Drop the first n letters of b (keeping its spacing after them) and glue.
    let seen = 0, i = 0; const bs = String(b);
    while (i < bs.length && seen < n) { if (/[a-z0-9]/i.test(bs[i].normalize('NFD')[0])) seen++; i++; }
    return { smash: String(a).trimEnd() + bs.slice(i), overlap: n };
  }
  const EMOJIS = ['🦊', '🐸', '🐼', '🦁', '🐙', '🦄', '🐢', '🐝', '🦖', '🐧', '🐨', '🦉', '🐬', '🦋', '🍕', '🚀', '🎸', '🏆', '👾', '🧙',
    '🐶', '🐱', '🐯', '🐮', '🐷', '🐵', '🦒', '🦓', '🐘', '🦈', '🐳', '🦀', '🐞', '🦜', '🌵', '🌈', '⚡', '🍔', '🎮', '👑'];
  /** What a player needs to know before a run of questions of a new type: shown on the title card, on the screen and the phones. */
  const HOWTO = {
    choice: 'Four answers on your phone. Tap the right one. The faster you are, the more you score.',
    text: 'Type your answer on your phone. Close spellings count.',
    order: 'Put the items on your phone into the right order, then lock it in.',
    pin: 'Work out the answer, then drop your pin on it. The closer you are, the more you score.',
    match: 'Tap an item, then tap its partner, until everything is paired up.',
    tf: 'True or false? Tap your answer. Quick!',
    sort: 'Put each answer into the right category.',
    wipeout: 'A board full of answers, and some of them are wrong. You get a good look first, then take turns to pick a right one. Pick a wrong one and you are wiped out.',
    race: 'Quick-fire questions on your phone. First to the target wins the bonus. Watch your emoji race across the screen.',
    smash: 'Name the picture, answer the clue, then smash the two together where they overlap: Brad Pitt + Pittsburgh = Brad Pittsburgh.',
    wheel: 'A hidden phrase. Letters turn over one at a time. Solve it on your phone: the sooner you do, the more you score.',
    highlow: 'A hard clue on the screen. Stuck? Tap your phone for the easy clue, for half the points.',
    rhyme: 'Two clues whose answers rhyme. Type both answers.',
    club: 'No knowledge needed, just logic. The fewer people who get it, the more it is worth.',
    dingbat: 'Say what you see: a well-known phrase hidden in how the words are laid out.',
    catchphrase: 'Watch the clip and say what you see: type the well-known saying it shows.',
    tune: 'Listen to the clip and answer on your phone.',
    potato: 'The bomb is lit and nobody knows how long the fuse is. If it lands on you, answer the question on your phone. Get it right and you choose who gets it next. Holding it when it goes bang costs you points.',
    koth: 'Fastest finger first picks two players to go head to head. Buzz on your phone, then say your answer out loud. Get it right and you stay on the hill and win a hill point: every one is worth points. First to the target wins the bonus too, but there are only so many head-to-heads.',
    chase: 'Whoever is in the lead is the Chaser. Everyone else plays as one team with a head start. The first right answer on each question moves that side one step: the team towards home, the Chaser towards the team. Get home before you are caught!',
    blockbusters: 'Pick a side, quick: each side holds half the players, so once one is full you join the other. Your side chooses a letter, and the answer starts with it. First to type the right answer wins the hexagon for their side. Join any two opposite sides of the board, left to right or top to bottom, to win.',
    nearest: 'Type your best guess at the number. The closer you are, the more you score, and the closest of all gets a bonus.',
    twenty: 'Everyone has the same mystery person or thing. Tap a question and your phone says yes or no; new questions open up as you go. Guess whenever you like in the box, but a wrong guess uses up a question. You have 20 questions and a three-minute clock. First to crack it scores most, then second and third; still stuck at the end and it costs you.',
    draw: 'When it is your turn, pick a word and draw it on your phone: no letters or numbers! Everyone else types guesses as fast as they can. Quick guessers score most, and the artist scores for every right guess.',
  };
  /** The build log: every writer call for a quiz, with what was asked and what came back, kept in its settings. */
  function genLog(settings, how, res, extra = {}) {
    if (!settings || !res) return;
    const q = res.__req || {};
    const got = (res.questions || []).map((x) => ({ type: x.type, text: String(x.text || x.phrase || x.place || x.track || '').slice(0, 140), bank: !!x.fromBank }));
    pushLog(settings, { at: new Date().toISOString(), how, round: extra.round || q.title || '', topic: String(q.topic || ''), brief: String(q.brief || '').slice(0, 600), types: q.types || [], asked: q.count || 0, difficulty: q.difficulty || '', fromBank: res.fromBank || 0, written: Math.max(0, got.length - (res.fromBank || 0)), keywords: res.bankInfo?.keywords || null, matching: res.bankInfo?.matching ?? null, got, warnings: (res.warnings || []).slice(0, 4) });
  }
  function genPlan(settings, how, rounds) {
    pushLog(settings, { at: new Date().toISOString(), how, plan: (rounds || []).map((r) => ({ title: r.title || '', brief: String(r.brief || '').slice(0, 600), mix: r.mix || {} })) });
  }
  function pushLog(settings, entry) {
    if (!settings) return;
    settings.buildLog = Array.isArray(settings.buildLog) ? settings.buildLog : [];
    settings.buildLog.push(entry);
    if (settings.buildLog.length > 150) settings.buildLog.splice(0, settings.buildLog.length - 150);
  }
  const COLORS = [
    { name: 'red',    hex: '#e21b3c', shape: '▲' },
    { name: 'blue',   hex: '#1368ce', shape: '◆' },
    { name: 'yellow', hex: '#d89e00', shape: '●' },
    { name: 'green',  hex: '#26890c', shape: '■' },
  ];
  const DEFAULT_TIMES = { nearest: 25, draw: 60, catchphrase: 50, choice: 20, text: 30, order: 45, pin: 25, match: 45, tf: 15, sort: 45, wipeout: 5, race: 120, smash: 30, wheel: 60, highlow: 40, rhyme: 30, club: 30, dingbat: 45, tune: 30, potato: 90, koth: 15, blockbusters: 20, chase: 15, twenty: 180 };
  const DEFAULT_SETTINGS = { maxPoints: 1000, minPoints: 500, defaultTime: 30, showAnswersOnPhones: true, timeByType: { ...DEFAULT_TIMES } };

  /** The time limit a question of this type gets by default in this quiz. */
  function timeFor(type, settings = DEFAULT_SETTINGS) {
    const t = +(settings.timeByType || {})[type];
    return clamp(t || +settings.defaultTime || DEFAULT_TIMES[type] || 30, 5, 180);
  }

  /** Fills in what an older or partial quiz is missing: settings defaults, rounds, and a round on every question. */
  function normalizeQuiz(q) {
    const settings = { ...DEFAULT_SETTINGS, ...(q.settings || {}), timeByType: { ...DEFAULT_TIMES, ...((q.settings || {}).timeByType || {}) } };
    const questions = Array.isArray(q.questions) ? q.questions : [];
    let rounds = Array.isArray(q.rounds) ? q.rounds : Array.isArray(settings.rounds) ? settings.rounds : [];
    rounds = rounds.filter((r) => r && r.id).map((r) => {
      // The mix is how many of each type the round should have; types and count follow from it.
      let mix = r.mix && typeof r.mix === 'object' ? Object.fromEntries(Object.entries(r.mix).filter(([k, v]) => TYPES[k] && +v > 0).map(([k, v]) => [k, Math.min(40, Math.round(+v))])) : null;
      if (!mix) { const types = Array.isArray(r.types) ? r.types.filter((t) => TYPES[t]) : []; const total = +r.count || 0; mix = {}; if (types.length && total) { const each = Math.floor(total / types.length); types.forEach((t, i) => { mix[t] = each + (i < total - each * types.length ? 1 : 0); }); } }
      const types = Object.keys(mix), count = Object.values(mix).reduce((a, b) => a + b, 0);
      return { id: r.id, title: r.title || '', intro: r.intro || '', brief: r.brief || '', mix, types, count, practice: !!r.practice };
    });
    if (!rounds.length) rounds = [{ id: uid('r'), title: 'Round 1', intro: '', brief: '', mix: {}, count: 0, types: [] }];
    const ids = new Set(rounds.map((r) => r.id));
    for (const qu of questions) if (!ids.has(qu.round)) qu.round = rounds[rounds.length - 1].id;
    // Races saved under the old scoring (5000 to the winner, nothing per right answer) move to today's: 100 per right answer, 500/200/100, −200 for last.
    for (const qu of questions) if (qu.type === 'race' && qu.perCorrect === undefined) Object.assign(qu, { perCorrect: 100, prize: 500, prize2: 200, prize3: 100, forfeit: 200 });
    for (const qu of questions) if (qu.type === 'race' && qu.maxWrong === undefined) qu.maxWrong = 10;
    for (const qu of questions) if (NEW_GAME_DEFAULTS[qu.type]) for (const [k, v] of Object.entries(NEW_GAME_DEFAULTS[qu.type]())) if (qu[k] === undefined) qu[k] = v;
    delete settings.rounds;
    const quiz = { id: q.id || null, title: q.title || 'Untitled quiz', settings, rounds, questions };
    orderQuestions(quiz);
    return quiz;
  }
  /** A practice question scores nothing: ticked on its own, or its whole round is a practice round. */
  function isPractice(quiz, q) { return !!(q && (q.practice || (quiz?.rounds || []).find((r) => r.id === q.round)?.practice)); }
  /** Keeps the flat question list in play order: round by round. */
  function orderQuestions(quiz) {
    quiz.questions = quiz.rounds.flatMap((r) => quiz.questions.filter((q) => q.round === r.id));
    return quiz;
  }
  /** What gets sent to the server: rounds ride inside settings so the table needs no new column. */
  function quizForSave(quiz) {
    return { id: quiz.id, title: quiz.title, settings: { ...quiz.settings, rounds: quiz.rounds }, questions: quiz.questions };
  }

  function newQuestion(type = 'choice', settings = DEFAULT_SETTINGS) {
    if (type === 'slide') return { id: uid('q'), type: 'slide', text: '', body: '', time: 20, media: { kind: 'none' } };
    if (type === 'catchphrase') { const c = newQuestion('text', settings); c.kind = 'catchphrase'; c.text = 'Catchphrase: say what you see'; c.media = { kind: 'youtube', url: '', videoId: '', start: 0 }; c.time = timeFor('catchphrase', settings); return c; }
    const q = { id: uid('q'), type, text: '', time: timeFor(type, settings), media: { kind: 'none' }, partial: false };
    if (type === 'choice') { q.options = [0, 1, 2, 3].map(() => ({ id: uid('o'), text: '' })); q.correct = q.options[0].id; }
    if (type === 'text') { q.answers = ['']; q.ai = true; }
    if (type === 'order') { q.items = [0, 1, 2, 3].map(() => ({ id: uid('i'), text: '' })); q.hint = ''; }
    if (type === 'pin') { q.media = { kind: 'image', url: '' }; q.mode = 'point'; q.pin = { x: 0.5, y: 0.5 }; q.radiusFull = 0.04; q.radiusZero = 0.2; }
    if (type === 'smash') { q.media = { kind: 'image', url: '' }; q.pictureAnswer = ''; q.clueAnswer = ''; q.smash = ''; q.ai = true; }
    if (type === 'wheel') { q.phrase = ''; q.category = 'Phrase'; q.revealEvery = 4; q.startLetters = ''; q.ai = true; }
    if (type === 'highlow') { q.lowText = ''; q.answers = ['']; q.highPoints = 1000; q.lowPoints = 500; q.ai = true; }
    if (type === 'club') { q.answers = ['']; q.pct = 50; q.ai = true; }
    if (type === 'dingbat') { q.answers = ['']; q.elements = [{ t: '', x: 50, y: 50, s: 4 }]; q.ai = true; }
    if (type === 'tune') { q.ask = 'song'; q.track = ''; q.artist = ''; q.year = ''; q.film = ''; q.cue = ''; q.answers = ['']; q.tolerance = 1; q.media = { kind: 'audio', url: '', start: 0, length: 15 }; q.ai = true; }
    if (type === 'rhyme') { q.text2 = ''; q.answer1 = ''; q.answer2 = ''; q.ai = true; }
    if (type === 'match') { q.pairs = [0, 1, 2, 3].map(() => ({ id: uid('p'), left: '', right: { kind: 'text', value: '' } })); }
    if (type === 'tf') { q.answer = true; }
    if (type === 'nearest') { q.answer = ''; q.unit = ''; q.spread = null; }
    if (type === 'draw') { q.text = 'Draw It'; q.turns = 3; q.words = []; q.guessPoints = 500; q.drawerPoints = 100; }
    if (type === 'twenty') { q.text = '20 Questions: who or what am I?'; q.answers = ['']; q.what = ''; q.facts = {}; q.maxQ = 20; q.prize = 1000; q.prize2 = 500; q.prize3 = 100; q.penalty = 200; }
    if (type === 'sort') { q.categories = [0, 1].map(() => ({ id: uid('c'), name: '' })); q.items = [0, 1, 2, 3].map(() => ({ id: uid('i'), text: '', category: q.categories[0].id })); }
    if (type === 'wipeout') { q.right = Array.from({ length: 8 }, () => ({ id: uid('w'), text: '' })); q.wrong = Array.from({ length: 3 }, () => ({ id: uid('w'), text: '' })); q.pickPoints = 200; q.penalty = 500; q.study = 20; }
    if (type === 'race') { q.target = 10; q.maxWrong = 10; q.perCorrect = 100; q.prize = 500; q.prize2 = 200; q.prize3 = 100; q.forfeit = 200; q.bank = Array.from({ length: 20 }, () => newBankItem()); }
    if (NEW_GAME_DEFAULTS[type]) Object.assign(q, NEW_GAME_DEFAULTS[type](), { bank: Array.from({ length: type === 'potato' ? 20 : 30 }, () => newBankItem()) });
    return q;
  }
  /** Settings for the three newer bank games: filled in on new questions, and on older saves that lack them. */
  const NEW_GAME_DEFAULTS = {
    potato: () => ({ fuseMin: 40, fuseMax: 90, perCorrect: 50, penalty: 300 }),
    koth: () => ({ target: 3, prize: 1000, answerSecs: 3, perPoint: 100, maxRounds: 12 }),
    chase: () => ({ headStart: 2, target: 5, teamPrize: 1000, chaserPrize: 200 }),
    blockbusters: () => ({ teams: [{ name: 'Newcastle', color: '#f2f2f2' }, { name: 'Sunderland', color: '#e21b3c' }], hexPoints: 50, prize: 500 }),
  };
  /** The bank rows a game can use: a question and its right answer, plus (except in Blockbusters) at least one wrong one. */
  function goodRows(q) { return (q.bank || []).filter((b) => b.text?.trim() && b.options?.[0]?.trim() && (q.type === 'blockbusters' || b.options.filter((o) => o.trim()).length >= 2)); }
  function newBankItem() { return { id: uid('b'), text: '', options: ['', '', '', ''] }; }
  /** The id a right answer maps to, for the types that have one. */
  function correctId(q) { return q.type === 'tf' ? String(q.answer) : q.correct; }

  /** Something wrong with the question that would stop it being played. */
  function validate(q) {
    const problems = [];
    if (q.type === 'slide') {
      if (!(q.text || '').trim() && !(q.body || '').trim() && !q.break) problems.push('Needs a title or some text.');
      if (q.break && !(+q.breakMins >= 1 && +q.breakMins <= 120)) problems.push('A break lasts between 1 and 120 minutes.');
      if (q.media && q.media.kind === 'youtube' && !q.media.videoId) problems.push('The YouTube link is not valid.');
      return problems;
    }
    if (q.type === 'wheel') {
      if (!(q.phrase || '').trim()) problems.push('Needs the phrase.');
      else if (!wheelLayout(q.phrase)) problems.push('The phrase does not fit the board (four rows of 12, 14, 14 and 12 letters; a word cannot be split).');
      if (!(q.category || '').trim()) problems.push('Needs a category, like Phrase, Person or Place.');
      return problems;
    }
    if (q.type !== 'tune' && (!q.text || !q.text.trim())) problems.push('Needs question text.');
    if (q.type === 'choice') {
      const filled = (q.options || []).filter((o) => o.text.trim());
      if (filled.length < 2) problems.push('Needs at least two answers.');
      if (!(q.options || []).some((o) => o.id === q.correct && o.text.trim())) problems.push('Mark which answer is right.');
    }
    if (q.type === 'text' && !(q.answers || []).some((a) => a.trim())) problems.push('Needs an accepted answer.');
    if (q.type === 'nearest') {
      if (!Number.isFinite(parseNum(q.answer))) problems.push('Needs the answer as a number.');
      if (q.spread != null && q.spread !== '' && !(parseNum(q.spread) > 0)) problems.push('"Points run out at" must be a number above nought, or blank for automatic.');
    }
    if (q.type === 'draw') {
      const turns = +q.turns || 0, words = drawWords(q);
      if (turns < 1 || turns > 12) problems.push('Between 1 and 12 drawings.');
      if ((q.words || []).some((w) => String(w).trim()) && words.length < turns * 2) problems.push(`Needs at least ${turns * 2} words (two to choose from for each drawing), or leave the list empty to use the built-in words.`);
    }
    if (q.type === 'order' && (q.items || []).filter((i) => i.text.trim()).length < 2) problems.push('Needs at least two items.');
    if (q.type === 'pin') {
      if (!q.media || q.media.kind !== 'image' || !q.media.url) problems.push('Needs a picture to drop the pin on.');
      if (q.mode === 'area') { if (!q.target || !(q.target.w > 0.01) || !(q.target.h > 0.01)) problems.push('Draw a box around the right thing, or pick the right tile.'); }
      else if (!q.pin) problems.push('Set where the pin goes.');
    }
    if (q.type === 'club') {
      if (!(q.answers || []).some((a) => a.trim())) problems.push('Needs the answer.');
      if (!(q.pct >= 1 && q.pct <= 99)) problems.push('Pick how many people get it (1–99%).');
    }
    if (q.type === 'tune') {
      if (!(q.media?.kind === 'audio' && q.media.url)) problems.push('Needs a clip: search for the song.');
      if (!(q.answers || []).some((a) => String(a).trim())) problems.push('Needs the answer.');
      if (q.ask === 'year' && !/^\d{4}$/.test(String(q.answers?.[0] || '').trim())) problems.push('The year needs four digits.');
    }
    if (q.type === 'dingbat') {
      if (!(q.answers || []).some((a) => a.trim())) problems.push('Needs the phrase it stands for.');
      if (!(q.elements || []).some((e) => (e.t || '').trim()) && !(q.media?.kind === 'image' && q.media.url)) problems.push('Lay out the dingbat (or upload a picture of one).');
    }
    if (q.type === 'twenty') {
      if (!(q.answers || []).some((a) => String(a).trim())) problems.push('Needs the answer: who or what it is.');
      if (!TWENTY_KINDS.some((k) => k.id === q.what)) problems.push('Say what kind of thing it is (a person, an animal, a place…).');
    }
    if (q.type === 'highlow') {
      if (!(q.lowText || '').trim()) problems.push('Needs the lowbrow clue.');
      if (!(q.answers || []).some((a) => a.trim())) problems.push('Needs the answer.');
    }
    if (q.type === 'rhyme') {
      if (!(q.text2 || '').trim()) problems.push('Needs the second clue.');
      if (!(q.answer1 || '').trim() || !(q.answer2 || '').trim()) problems.push('Needs both answers.');
    }
    if (q.type === 'smash') {
      if (!q.media || !q.media.url) problems.push('Needs the picture.');
      if (!q.pictureAnswer?.trim()) problems.push('What is the picture of?');
      if (!q.clueAnswer?.trim()) problems.push('Needs the clue\'s answer.');
      if (!(q.smash || '').trim()) problems.push('The two answers don\'t overlap — change one, or type the smash yourself.');
    }
    if (q.type === 'match') {
      const ok = (q.pairs || []).filter((p) => p.left.trim() && p.right && p.right.value);
      if (ok.length < 2) problems.push('Needs at least two complete pairs.');
    }
    if (q.type === 'sort') {
      const cats = (q.categories || []).filter((c) => c.name.trim());
      if (cats.length < 2) problems.push('Needs at least two named categories.');
      const items = (q.items || []).filter((i) => i.text.trim());
      if (items.length < 2) problems.push('Needs at least two answers to sort.');
      if (items.some((i) => !cats.some((c) => c.id === i.category))) problems.push('Every answer needs a category.');
    }
    if (q.type === 'wipeout') {
      const r = (q.right || []).filter((i) => i.text.trim()).length, w = (q.wrong || []).filter((i) => i.text.trim()).length;
      if (r < 3) problems.push('Needs at least three right answers.');
      if (w < 1) problems.push('Needs at least one wrong answer.');
      if (r + w > 35) problems.push('Thirty-five answers on the board at most.');
    }
    if (q.type === 'race') {
      const good = (q.bank || []).filter((b) => b.text.trim() && b.options[0].trim() && b.options.filter((o) => o.trim()).length >= 2);
      const target = +q.target || 10, lives = q.maxWrong ?? 10;
      if (good.length < target + lives) problems.push(`Needs ${target + lives} complete questions in the bank (it has ${good.length}), so a player can get ${lives} wrong and still finish.`);
    }
    if (q.type === 'potato') {
      const n = goodRows(q).length;
      if (n < 10) problems.push(`Needs at least 10 complete questions in the bank (it has ${n}). They are reused if the bomb goes round a lot.`);
      if (!(+q.fuseMin >= 10) || !(+q.fuseMax >= +q.fuseMin) || +q.fuseMax > 600) problems.push('The fuse needs a shortest time of at least 10 seconds, and a longest time no shorter than that (600 at most).');
    }
    if (q.type === 'koth') {
      const n = goodRows(q).length;
      if (n < 12) problems.push(`Needs at least 12 complete questions in the bank (it has ${n}); a game to ${q.target || 3} can easily use 20 or more.`);
      if (!(+q.target >= 1 && +q.target <= 10)) problems.push('Points to win must be between 1 and 10.');
    }
    if (q.type === 'chase') {
      const n = goodRows(q).length;
      if (n < 15) problems.push(`Needs at least 15 complete questions in the bank (it has ${n}); a close chase can use 20 or more.`);
      if (!(+q.target >= 1 && +q.target <= 15) || !(+q.headStart >= 0 && +q.headStart <= 10)) problems.push('Steps home must be 1 to 15, and the head start 0 to 10.');
    }
    if (q.type === 'blockbusters') {
      const n = goodRows(q).length;
      if (n < BB_COLS * BB_ROWS) problems.push(`Needs at least ${BB_COLS * BB_ROWS} complete questions, one for each hexagon (it has ${n}). A few spares cover the ones nobody gets.`);
      if ((q.teams || []).length !== 2 || !q.teams.every((t) => (t.name || '').trim())) problems.push('Both teams need a name.');
    }
    if (q.media && q.media.kind === 'youtube' && !q.media.videoId) problems.push('The YouTube link is not valid.');
    return problems;
  }

  // ---- Blockbusters board: five columns of four hexagons, every other column dropped half a hex, as on the show.
  // Unlike the show (a pair going across against one player going down), either side wins by joining EITHER pair of
  // opposite sides: left to right or top to bottom. The first side to link wins, so there is only ever one winner. ----
  const BB_COLS = 5, BB_ROWS = 4;
  /** The hexagons touching hexagon i (i = row * BB_COLS + column). */
  function bbNeighbours(i) {
    const c = i % BB_COLS, r = Math.floor(i / BB_COLS), odd = c % 2 === 1;
    const cand = [[c, r - 1], [c, r + 1], [c - 1, odd ? r : r - 1], [c - 1, odd ? r + 1 : r], [c + 1, odd ? r : r - 1], [c + 1, odd ? r + 1 : r]];
    return cand.filter(([x, y]) => x >= 0 && x < BB_COLS && y >= 0 && y < BB_ROWS).map(([x, y]) => y * BB_COLS + x);
  }
  /** A team's linked path as hexagon indices, or null: left edge to right edge, or top edge to bottom edge. */
  function bbPath(owner, team) { return bbLink(owner, team, true) || bbLink(owner, team, false); }
  /** One direction: across (left to right) or down (top to bottom). */
  function bbLink(owner, team, across) {
    const n = BB_COLS * BB_ROWS, prev = {};
    const start = [...Array(n).keys()].filter((i) => owner[i] === team && (across ? i % BB_COLS === 0 : i < BB_COLS));
    const seen = new Set(start), queue = start.slice();
    while (queue.length) {
      const i = queue.shift();
      if (across ? i % BB_COLS === BB_COLS - 1 : i >= n - BB_COLS) { const path = [i]; let p = i; while (prev[p] !== undefined) { p = prev[p]; path.push(p); } return path; }
      for (const j of bbNeighbours(i)) if (owner[j] === team && !seen.has(j)) { seen.add(j); prev[j] = i; queue.push(j); }
    }
    return null;
  }
  /** Dark or light writing, whichever reads on a team's colour. */
  function inkOn(hex) { const h = String(hex || '').replace('#', ''); if (h.length < 6) return '#fff'; const [r, g, b] = [0, 2, 4].map((k) => parseInt(h.slice(k, k + 2), 16)); return (r * 299 + g * 587 + b * 114) / 1000 > 150 ? '#1b1640' : '#fff'; }
  /** The board as HTML. hexes: [{ letter, owner (-1 open, 0 or 1) }]; opts: { teams, hot (index), win (indices), pick (open ones tappable), cls }. */
  function bbBoardHtml(hexes, opts = {}) {
    const teams = opts.teams || [], win = new Set(opts.win || []);
    const col = (t) => teams[t]?.color || (t === 0 ? '#f2f2f2' : '#e21b3c');
    // Hexagon width w (share of the board): columns overlap by a quarter, so C columns span w × (0.75C + 0.25).
    const w = 1 / (0.75 * BB_COLS + 0.25), rows = BB_ROWS + 0.5, ar = 1 / (rows * w * Math.sqrt(3) / 2);
    const cells = hexes.map((h, i) => {
      const c = i % BB_COLS, r = Math.floor(i / BB_COLS);
      const style = `left:${(c * 0.75 * w * 100).toFixed(3)}%;top:${(((r + (c % 2) / 2) / rows) * 100).toFixed(3)}%;${h.owner >= 0 ? `--hx:${col(h.owner)};color:${inkOn(col(h.owner))}` : ''}`;
      const tag = opts.pick && h.owner < 0 ? 'button' : 'div';
      return `<${tag} class="bbhex ${h.owner >= 0 ? 'owned' : ''} ${opts.hot === i ? 'hot' : ''} ${win.has(i) ? 'win' : ''}" style="${style}" ${tag === 'button' ? `data-hex="${i}"` : ''}><span>${esc(h.letter || '')}</span></${tag}>`;
    }).join('');
    return `<div class="bbframe ${opts.cls || ''}" style="--t0:${col(0)};--t1:${col(1)};--hw:${(w * 100).toFixed(3)}%;--hh:${(100 / rows).toFixed(3)}%;--ar:${ar.toFixed(4)}"><div class="bbboard">${cells}</div></div>`;
  }

  function youtubeId(url) {
    const m = String(url || '').match(/(?:youtu\.be\/|v=|\/shorts\/|\/embed\/|\/live\/)([A-Za-z0-9_-]{11})/);
    return m ? m[1] : (/^[A-Za-z0-9_-]{11}$/.test(String(url || '').trim()) ? url.trim() : '');
  }

  // ---------------------------------------------------------------- scoring
  function speedPoints(elapsedMs, timeMs, settings = DEFAULT_SETTINGS) {
    const max = +settings.maxPoints || 1000, min = Math.min(+settings.minPoints || 0, max);
    const f = clamp(elapsedMs / Math.max(1, timeMs), 0, 1);
    return Math.round(max - (max - min) * f);
  }
  function normText(s) {
    return String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '')
      .replace(/&/g, ' and ').replace(/[^a-z0-9]+/g, ' ').trim().replace(/^(the|a|an) /, '');
  }
  function levenshtein(a, b) {
    if (a === b) return 0; if (!a.length) return b.length; if (!b.length) return a.length;
    let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
    for (let i = 1; i <= a.length; i++) {
      const cur = [i];
      for (let j = 1; j <= b.length; j++) cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      prev = cur;
    }
    return prev[b.length];
  }
  function similarity(a, b) { return 1 - levenshtein(a, b) / Math.max(a.length, b.length, 1); }
  /** 'right' | 'wrong' | 'unsure' — unsure goes to the AI. */
  function textMatch(answer, accepted) {
    const n = normText(answer);
    if (!n) return 'wrong';
    for (const acc of accepted || []) {
      const m = normText(acc);
      if (!m) continue;
      if (n === m) return 'right';
      if (m.length >= 4 && similarity(n, m) >= 0.85) return 'right';
      if (/^\d+$/.test(m) && n.replace(/\s/g, '') === m) return 'right';
    }
    return 'unsure';
  }

  // ---------------------------------------------------------------- game code + join URL
  const CODE_CHARS = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  function newCode() { let c = ''; for (let i = 0; i < 6; i++) c += CODE_CHARS[Math.floor(Math.random() * CODE_CHARS.length)]; return c; }
  function playUrl(code) {
    const u = new URL('play.html', location.href);
    u.search = '?g=' + encodeURIComponent(code);
    return u.toString();
  }
  function shortPlayUrl() { return new URL('play', location.href).toString().replace(/^https?:\/\//, ''); }

  // ---------------------------------------------------------------- images
  /** Shrinks a picked image file in the browser before upload. Returns {data (base64), contentType}. */
  function resizeImage(file, maxSide = 1600) {
    return new Promise((resolve, reject) => {
      const img = new Image();
      const url = URL.createObjectURL(file);
      img.onload = () => {
        const scale = Math.min(1, maxSide / Math.max(img.width, img.height));
        const c = document.createElement('canvas');
        c.width = Math.round(img.width * scale); c.height = Math.round(img.height * scale);
        c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
        const png = file.type === 'image/png' && file.size < 1500000;
        const dataUrl = c.toDataURL(png ? 'image/png' : 'image/jpeg', 0.86);
        URL.revokeObjectURL(url);
        resolve({ data: dataUrl.split(',')[1], contentType: png ? 'image/png' : 'image/jpeg', width: c.width, height: c.height });
      };
      img.onerror = () => { URL.revokeObjectURL(url); reject(new Error('That file is not a picture we can read.')); };
      img.src = url;
    });
  }

  // ---------------------------------------------------------------- collages (Drop the pin on one of several pictures)
  /** Tiles pictures into one image in the browser. Returns the upload payload and each tile's rectangle as fractions. */
  async function composeCollage(tiles) {
    const imgs = await Promise.all(tiles.map((t) => new Promise((res, rej) => { const im = new Image(); im.crossOrigin = 'anonymous'; im.onload = () => res(im); im.onerror = () => rej(new Error(`Could not load ${t.title || 'a picture'}.`)); im.src = t.url; })));
    const n = tiles.length, cols = n <= 4 ? 2 : 3, rows = Math.ceil(n / cols), cw = 560, chh = 420, gap = 14;
    const c = document.createElement('canvas'); c.width = cols * cw + gap * (cols + 1); c.height = rows * chh + gap * (rows + 1);
    const ctx = c.getContext('2d'); ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, c.width, c.height);
    const rects = imgs.map((im, i) => {
      const x = gap + (i % cols) * (cw + gap), y = gap + Math.floor(i / cols) * (chh + gap);
      const s = Math.max(cw / im.width, chh / im.height), sw = cw / s, sh = chh / s; // cover
      ctx.save(); ctx.beginPath(); ctx.rect(x, y, cw, chh); ctx.clip();
      ctx.drawImage(im, (im.width - sw) / 2, (im.height - sh) / 2, sw, sh, x, y, cw, chh); ctx.restore();
      ctx.strokeStyle = '#d6d6e4'; ctx.lineWidth = 3; ctx.strokeRect(x + 1.5, y + 1.5, cw - 3, chh - 3);
      return { x: x / c.width, y: y / c.height, w: cw / c.width, h: chh / c.height };
    });
    return { data: c.toDataURL('image/jpeg', 0.86).split(',')[1], contentType: 'image/jpeg', rects };
  }
  /** Composes and uploads a collage for a question whose tiles are known, and points the target at the answer. */
  async function buildCollageFor(q) {
    const tiles = (q.collage || []).filter((t) => t.url);
    if (tiles.length < 2) throw new Error('A collage needs at least two pictures.');
    const out = await composeCollage(tiles);
    const up = await api('upload', { data: out.data, contentType: out.contentType }, { timeout: 90000 });
    q.media = { kind: 'image', url: up.url, credit: tiles.map((t) => t.credit).filter(Boolean).join('; ') || undefined };
    q.collage = tiles.map((t, i) => ({ ...t, rect: out.rects[i] }));
    q.mode = 'area';
    const ai = Number.isInteger(q.answerIndex) && q.answerIndex < tiles.length ? q.answerIndex : 0;
    q.answerIndex = ai; q.target = { ...out.rects[ai] };
  }

  // ---------------------------------------------------------------- The 1% Club + Dingbats
  /** Flat points for a 1% Club question: the rarer the right answer, the more it pays (90% → 200, 50% → 600, 10% → 1000). */
  function clubPoints(pct) { return clamp(Math.round(1100 - 10 * (+pct || 50)), 200, 1000); }
  const CLUB_PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1];
  /** Draws a dingbat: text elements placed by percentage on a white board. Sizes 1–6; rot in degrees; flip h/v; style strike/underline/box/outline. */
  function dingbatHtml(elements, cls = '') {
    const els = (elements || []).filter((e) => (e.t || '').trim());
    return `<div class="dingbat ${cls}">${els.map((e) => {
      const sz = clamp(+e.s || 3, 1, 6);
      const tf = ['translate(-50%,-50%)', e.rot ? `rotate(${clamp(+e.rot, -180, 180)}deg)` : '', e.flip === 'h' ? 'scaleX(-1)' : e.flip === 'v' ? 'scaleY(-1)' : ''].filter(Boolean).join(' ');
      const color = /^#[0-9a-f]{3,8}$/i.test(e.color || '') ? `color:${e.color};` : '';
      return `<span class="db-el ${['strike', 'underline', 'box', 'outline'].includes(e.style) ? e.style : ''}" style="left:${clamp(+e.x || 50, 0, 100)}%;top:${clamp(+e.y || 50, 0, 100)}%;font-size:${sz}em;transform:${tf};${color}">${esc(e.t)}</span>`;
    }).join('')}</div>`;
  }

  // ---------------------------------------------------------------- AI usage and a rough cost
  // List prices in US dollars per million tokens (in, out); cache reads cost a tenth of input, cache writes a quarter more.
  // Edit here if the prices change. Web searches are priced per thousand.
  const AI_PRICES = { 'claude-opus-5': [15, 75], 'claude-sonnet-5': [3, 15], 'claude-haiku-4-5-20251001': [1, 5] };
  const SEARCH_PRICE = 10;
  const AI_NAMES = { 'claude-opus-5': 'Opus', 'claude-sonnet-5': 'Sonnet', 'claude-haiku-4-5-20251001': 'Haiku' };
  /** Adds one call's usage (as the server reports it) to a quiz's running total. */
  function addUsage(settings, u) {
    if (!settings || !u || !u.model) return;
    const all = settings.aiUsage = settings.aiUsage || {};
    const m = all[u.model] = all[u.model] || { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, searches: 0, calls: 0 };
    for (const k of ['input', 'output', 'cacheRead', 'cacheWrite', 'searches']) m[k] += +u[k] || 0;
    m.calls += 1;
  }
  function usageCost(all) {
    let usd = 0;
    for (const [model, m] of Object.entries(all || {})) { const [pi, po] = AI_PRICES[model] || [15, 75]; usd += (m.input * pi + m.cacheRead * pi * 0.1 + m.cacheWrite * pi * 1.25 + m.output * po) / 1e6 + (m.searches || 0) * SEARCH_PRICE / 1000; }
    return usd;
  }
  /** One line per model, plus the estimate. */
  function usageSummary(all) {
    const rows = Object.entries(all || {}).map(([model, m]) => `${AI_NAMES[model] || model}: ${m.calls} call${m.calls === 1 ? '' : 's'}, ${Math.round((m.input + m.cacheRead + m.cacheWrite) / 1000)}k in (${Math.round(m.cacheRead / 1000)}k cached), ${Math.round(m.output / 1000)}k out${m.searches ? `, ${m.searches} searches` : ''}`);
    return rows.length ? { rows, usd: usageCost(all) } : null;
  }

  // ---------------------------------------------------------------- Name That Tune
  const TUNE_ASKS = { song: { label: 'Name the song', prompt: '🎵 Name that tune' }, artist: { label: 'Name the artist', prompt: '🎤 Who is this?' }, film: { label: 'Which film is it from?', prompt: '🎬 Which film is this music from?' }, year: { label: 'What year?', prompt: '📅 What year was this released?' }, lyric: { label: 'Next line of the lyric', prompt: '🎶 The clip stops — what is the next line?' } };
  /** What the screen and phones ask for a tune question: the host's own wording, or the ask's default. */
  function tunePrompt(q) { if ((q.text || '').trim()) return q.text.trim(); if (q.ask === 'lyric' && (q.cue || '').trim()) return `🎶 What line comes after: “${q.cue.trim()}”?`; return (TUNE_ASKS[q.ask] || TUNE_ASKS.song).prompt; }
  /** A track title without the "(feat. …)", "- Remastered" and "[Single Version]" clutter: what a player would actually say. */
  function cleanTitle(t) { return String(t || '').replace(/\s*[\(\[][^)\]]*(feat\.|featuring|remaster|remastered|version|edit|mix|mono|stereo|live|radio)[^)\]]*[\)\]]/gi, '').replace(/\s+-\s+(remaster(ed)?|single version|radio edit|\d{4} remaster).*$/i, '').trim(); }
  /** Bigger Apple artwork from the 100px thumbnail the search returns. */
  function bigArt(url) { return String(url || '').replace(/\/\d+x\d+bb\./, '/600x600bb.'); }

  // ---------------------------------------------------------------- Nearest Wins
  /** A number typed by a person: "1,250", "£3.5m", "12 000", "-4" all read as numbers. */
  function parseNum(v) {
    if (typeof v === 'number') return v;
    const raw = String(v ?? '').trim().toLowerCase(), money = /[£$€]/.test(raw);
    const s = raw.replace(/[£$€,]/g, '').replace(/(\d)\s+(?=\d)/g, '$1');
    const m = s.match(/(-?\d*\.?\d+)(?![\d.])\s*(?:(thousand|million|billion|bn|k|m)(?![a-z]))?/); if (!m) return NaN;
    const mult = { thousand: 1e3, k: 1e3, million: 1e6, billion: 1e9, bn: 1e9, m: money ? 1e6 : 1 }[m[2]] || 1; // 100m is metres, £100m is money
    return parseFloat(m[1]) * mult;
  }

  /** How far off a guess can be before it scores nothing: set on the question, or worked out from the answer (a year: 25; otherwise half the answer). */
  function nearestSpread(q) {
    const set = parseNum(q.spread); if (set > 0) return set;
    const a = parseNum(q.answer); if (!Number.isFinite(a)) return 1;
    if (Number.isInteger(a) && a >= 1000 && a <= 2100) return 25;
    return Math.max(Math.abs(a) * 0.5, 1);
  }
  /** A number for the screen: thousands separated, no stray decimals. */
  function fmtNum(n) { if (!Number.isFinite(n)) return '?'; const r = Math.abs(n) >= 100 ? Math.round(n) : Math.round(n * 100) / 100; return Number.isInteger(r) && r >= 1000 && r <= 2100 ? String(r) : r.toLocaleString('en-GB'); } // years without a comma

  // ---------------------------------------------------------------- Draw It
  /** Words anyone can have a go at drawing, used when a Draw It question has no list of its own. */
  const DRAW_WORDS = ['Banana', 'Umbrella', 'Snowman', 'Rocket', 'Pizza', 'Guitar', 'Bicycle', 'Castle', 'Spider', 'Rainbow', 'Toothbrush', 'Lighthouse', 'Volcano', 'Octopus', 'Ladder', 'Kite', 'Anchor', 'Cactus', 'Penguin', 'Helicopter',
    'Sandcastle', 'Mermaid', 'Dragon', 'Crown', 'Teapot', 'Scissors', 'Glasses', 'Wheelbarrow', 'Tent', 'Candle', 'Hot dog', 'Ice cream', 'Snail', 'Tortoise', 'Giraffe', 'Elephant', 'Kangaroo', 'Hedgehog', 'Jellyfish', 'Shark',
    'Bridge', 'Windmill', 'Igloo', 'Pyramid', 'Treasure chest', 'Pirate', 'Ghost', 'Robot', 'Alien', 'Wizard', 'Skateboard', 'Trampoline', 'Swing', 'Rollercoaster', 'Ferris wheel', 'Hot air balloon', 'Submarine', 'Tractor', 'Double-decker bus', 'Train',
    'Football', 'Goalkeeper', 'Trophy', 'Medal', 'Boxing glove', 'Fishing rod', 'Golf', 'Darts', 'Snooker', 'Tennis racket', 'Bowling', 'Surfboard', 'Scarecrow', 'Chimney', 'Doorbell', 'Toaster', 'Kettle', 'Washing machine', 'Fridge', 'Sofa',
    'Lamp', 'Clock', 'Alarm clock', 'Mobile phone', 'Television', 'Headphones', 'Camera', 'Microphone', 'Drum', 'Trumpet', 'Piano', 'Violin', 'Paintbrush', 'Pencil', 'Envelope', 'Stamp', 'Map', 'Compass', 'Magnet', 'Battery',
    'Light bulb', 'Key', 'Padlock', 'Sword', 'Shield', 'Bow and arrow', 'Cowboy', 'Horse', 'Unicorn', 'Chicken', 'Egg', 'Frying pan', 'Sausage', 'Chips', 'Cheese', 'Sandwich', 'Birthday cake', 'Cupcake', 'Doughnut', 'Popcorn',
    'Carrot', 'Pineapple', 'Strawberry', 'Mushroom', 'Tree', 'Palm tree', 'Flower', 'Sunflower', 'Leaf', 'Snowflake', 'Lightning', 'Tornado', 'Moon', 'Star', 'Sun', 'Cloud', 'Island', 'Mountain', 'Waterfall', 'Beach',
    'Fireworks', 'Christmas tree', 'Pumpkin', 'Easter egg', 'Santa', 'Present', 'Balloon', 'Bubble', 'Spaceship', 'Astronaut', 'Dinosaur', 'Skeleton', 'Zombie', 'Vampire', 'Superhero', 'King', 'Queen', 'Angel', 'Clown', 'Chef',
    'Angel of the North', 'Tyne Bridge', 'Stottie', 'Pint of beer', 'Fish and chips', 'Seagull', 'Magpie', 'Black cat', 'Football shirt', 'Referee', 'Bus stop', 'Traffic lights', 'Roundabout', 'Car park', 'Shopping trolley', 'Tattoo', 'Beard', 'Moustache', 'Handbag'];
  /** The words a Draw It question plays with: its own list, or the built-in one. No repeats. */
  function drawWords(q) {
    const own = (q?.words || []).map((w) => String(w).trim()).filter(Boolean);
    return [...new Set(own.length ? own : DRAW_WORDS)];
  }
  /** The word as the guessers see it: a line per letter, spaces and hyphens kept, some letters shown. */
  function drawHint(word, shown = []) { return [...String(word)].map((ch, i) => /[a-z0-9]/i.test(ch) ? (shown.includes(i) ? ch.toUpperCase() : '_') : ch === ' ' ? '\u2003' : ch).join(' '); }

  function fmtTime(ms) { const s = Math.max(0, Math.ceil(ms / 1000)); return s + 's'; }
  function ordinal(n) { const s = ['th', 'st', 'nd', 'rd'], v = n % 100; return n + (s[(v - 20) % 10] || s[v] || s[0]); }

  return { SUPABASE_URL, SUPABASE_KEY, $, $$, esc, uid, clamp, sleep, shuffle, store, unstore, hostPassword, setHostPassword, api, client,
    TYPES, BANK_GAMES, NEW_GAME_DEFAULTS, TWENTY_KINDS, TWENTY_QS, twentyQ, twentyBranch, twentyYes, twentyOpen, parseNum, nearestSpread, fmtNum, DRAW_WORDS, drawWords, drawHint, goodRows, BB_COLS, BB_ROWS, bbNeighbours, bbPath, bbBoardHtml, inkOn, SLIDE, BREAK, isPractice, typeInfo, slideHtml, breakMs, clockText, breakClockHtml, setBreakClock, EMOJIS, HOWTO, genLog, genPlan, pushLog, COLORS, DEFAULT_SETTINGS, DEFAULT_TIMES, timeFor, normalizeQuiz, orderQuestions, quizForSave, newQuestion, newBankItem, correctId, validate, smashOf, wheelLayout, wheelBoardHtml, WHEEL_ROWS, youtubeId, speedPoints, normText, similarity, textMatch,
    newCode, playUrl, shortPlayUrl, resizeImage, fmtTime, ordinal, composeCollage, buildCollageFor, clubPoints, CLUB_PCTS, dingbatHtml, addUsage, usageCost, usageSummary, AI_PRICES, TUNE_ASKS, tunePrompt, bigArt, cleanTitle };
})();
