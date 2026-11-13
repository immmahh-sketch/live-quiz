/* Let's Quiz: CHRISTMAS DAY (November 2026), the shared data. Loaded by the host screen, the phones and the builder.
 * The dinner: nine items, each tied to a question category, plus the tomato ketchup that only a 1% question can win.
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
  // Hand-drawn item pictures (the emoji set has no roast potatoes, gravy or Yorkshire pudding). `icon` stays as the emoji for plain text; ico(i) gives the picture for screens.
  const SVGS = {
    turkey: `<svg class="xmsvg" viewBox="0 0 64 64" aria-hidden="true" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.6"><ellipse cx="32" cy="54" rx="27" ry="5" fill="#d3ccbc" stroke="none"/><ellipse cx="32" cy="53" rx="23" ry="3.6" fill="#e8e2d4" stroke="none"/>
<g stroke="#7a3f12">
<path d="M9 40 L4 49" stroke="#fff4dc" stroke-width="5.5"/><circle cx="3.5" cy="50" r="3" fill="#fff4dc" stroke="#8a6f3f"/><circle cx="6.5" cy="52" r="3" fill="#fff4dc" stroke="#8a6f3f"/>
<ellipse cx="15" cy="37" rx="10" ry="7" transform="rotate(35 15 37)" fill="#c9792a"/>
<path d="M55 40 L60 49" stroke="#fff4dc" stroke-width="5.5"/><circle cx="60.5" cy="50" r="3" fill="#fff4dc" stroke="#8a6f3f"/><circle cx="57.5" cy="52" r="3" fill="#fff4dc" stroke="#8a6f3f"/>
<ellipse cx="49" cy="37" rx="10" ry="7" transform="rotate(-35 49 37)" fill="#c9792a"/>
<path d="M10 40 Q9 22 32 20 Q55 22 54 40 Q52 52 32 52 Q12 52 10 40Z" fill="#c9792a"/>
<path d="M17 30 Q32 18 47 30" fill="none" stroke="#fbd58a" stroke-width="3"/>
<path d="M20 44 Q32 50 44 44" fill="none" stroke="#7a3f12"/>
<ellipse cx="26" cy="31" rx="5" ry="2.5" fill="#fbd58a" stroke="none" opacity=".75"/>
</g></svg>`,
    potatoes: `<svg class="xmsvg" viewBox="0 0 64 64" aria-hidden="true" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.6"><ellipse cx="32" cy="54" rx="27" ry="5" fill="#d3ccbc" stroke="none"/><ellipse cx="32" cy="53" rx="23" ry="3.6" fill="#e8e2d4" stroke="none"/><g><path d="M33 28 L38 22 L44 19 L49 21 L53 24 L58 28 L57 34 L53 37 L54 42 L48 44 L42 42 L37 41 L38 35Z" fill="#e3a13e" stroke="#8f4a14" stroke-width="4.5"/><path d="M33 28 L38 22 L44 19 L49 21 L53 24 L58 28 L57 34 L53 37 L54 42 L48 44 L42 42 L37 41 L38 35Z" fill="#e3a13e" stroke="none"/><path d="M5 37 L8 29 L13 27 L14 22 L21 21 L25 25 L31 23 L35 29 L32 35 L35 41 L29 46 L22 45 L17 49 L11 46 L8 42Z" fill="#e8a840" stroke="#8f4a14" stroke-width="4.5"/><path d="M5 37 L8 29 L13 27 L14 22 L21 21 L25 25 L31 23 L35 29 L32 35 L35 41 L29 46 L22 45 L17 49 L11 46 L8 42Z" fill="#e8a840" stroke="none"/><path d="M25 49 L30 43 L36 41 L42 42 L48 44 L53 47 L48 52 L40 54 L31 54Z" fill="#dc9733" stroke="#8f4a14" stroke-width="4.5"/><path d="M25 49 L30 43 L36 41 L42 42 L48 44 L53 47 L48 52 L40 54 L31 54Z" fill="#dc9733" stroke="none"/></g>
<g fill="#f6d27a" stroke="none"><path d="M10 31 L15 29 L18 33 L13 36Z"/><path d="M22 27 L28 27 L29 32 L24 33Z"/><path d="M40 24 L47 23 L49 28 L43 29Z"/><path d="M50 31 L55 31 L54 35 L50 35Z"/><path d="M31 46 L38 45 L40 49 L33 50Z"/><path d="M14 40 L19 39 L20 43 L15 44Z"/></g>
<g fill="#7a3a0e" stroke="none"><path d="M17 24 l3 1 l-1 3z"/><path d="M33 38 l3 -1 l0 3z"/><path d="M44 36 l3 1 l-2 3z"/><path d="M26 41 l3 1 l-2 2z"/><path d="M9 38 l3 0 l-1 3z"/><path d="M51 26 l3 1 l-2 2z"/><path d="M38 50 l3 0 l-2 2z"/></g>
<g fill="#fff" stroke="none" opacity=".85"><circle cx="12" cy="31" r="1"/><circle cx="25" cy="28" r="1"/><circle cx="43" cy="25" r="1"/><circle cx="34" cy="47" r="1"/><circle cx="52" cy="32" r="1"/></g>
<g stroke="#3f6b2a" fill="none" stroke-width="1.8"><path d="M26 18 L36 8"/><path d="M28 16 l-5 -1 M31 13 l-5 -1 M33 11 l4 4 M30 14 l4 4"/></g></svg>`,
    pigs: `<svg class="xmsvg" viewBox="0 0 64 64" aria-hidden="true" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.6"><ellipse cx="32" cy="54" rx="27" ry="5" fill="#d3ccbc" stroke="none"/><ellipse cx="32" cy="53" rx="23" ry="3.6" fill="#e8e2d4" stroke="none"/><rect x="6" y="14" width="52" height="15" rx="7.5" fill="#c1623f" stroke="#6f2e1b"/><rect x="10" y="16.5" width="44" height="3.5" rx="1.7" fill="#d98a6a" stroke="none" opacity=".7"/><path d="M15 12.5 h6 l-3 18 h-6z" fill="#f2aa9a" stroke="#c4604b"/><path d="M16.2 15 l3 0 M15 21 l3 0" stroke="#d9594a" stroke-width="1.5"/><path d="M25 12.5 h6 l-3 18 h-6z" fill="#f2aa9a" stroke="#c4604b"/><path d="M26.2 15 l3 0 M25 21 l3 0" stroke="#d9594a" stroke-width="1.5"/><path d="M35 12.5 h6 l-3 18 h-6z" fill="#f2aa9a" stroke="#c4604b"/><path d="M36.2 15 l3 0 M35 21 l3 0" stroke="#d9594a" stroke-width="1.5"/><path d="M45 12.5 h6 l-3 18 h-6z" fill="#f2aa9a" stroke="#c4604b"/><path d="M46.2 15 l3 0 M45 21 l3 0" stroke="#d9594a" stroke-width="1.5"/><rect x="6" y="33" width="52" height="15" rx="7.5" fill="#c1623f" stroke="#6f2e1b"/><rect x="10" y="35.5" width="44" height="3.5" rx="1.7" fill="#d98a6a" stroke="none" opacity=".7"/><path d="M15 31.5 h6 l-3 18 h-6z" fill="#f2aa9a" stroke="#c4604b"/><path d="M16.2 34 l3 0 M15 40 l3 0" stroke="#d9594a" stroke-width="1.5"/><path d="M25 31.5 h6 l-3 18 h-6z" fill="#f2aa9a" stroke="#c4604b"/><path d="M26.2 34 l3 0 M25 40 l3 0" stroke="#d9594a" stroke-width="1.5"/><path d="M35 31.5 h6 l-3 18 h-6z" fill="#f2aa9a" stroke="#c4604b"/><path d="M36.2 34 l3 0 M35 40 l3 0" stroke="#d9594a" stroke-width="1.5"/><path d="M45 31.5 h6 l-3 18 h-6z" fill="#f2aa9a" stroke="#c4604b"/><path d="M46.2 34 l3 0 M45 40 l3 0" stroke="#d9594a" stroke-width="1.5"/></svg>`,
    stuffing: `<svg class="xmsvg" viewBox="0 0 64 64" aria-hidden="true" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.6"><ellipse cx="32" cy="54" rx="27" ry="5" fill="#d3ccbc" stroke="none"/><ellipse cx="32" cy="53" rx="23" ry="3.6" fill="#e8e2d4" stroke="none"/>
<g fill="#6b9a3f" stroke="#3f6b2a"><path d="M8 48 Q10 38 22 38 Q22 48 8 48Z"/><path d="M10 47 Q16 43 21 39" fill="none"/><path d="M56 48 Q54 38 42 38 Q42 48 56 48Z"/><path d="M54 47 Q48 43 43 39" fill="none"/></g>
<g stroke="#6a3a14"><circle cx="20" cy="44" r="11" fill="#c3894a"/><circle cx="15.1" cy="40.1" r="1.5" fill="#8a4f1f" stroke="none"/><circle cx="21.1" cy="37.4" r="1.3" fill="#e1b46d" stroke="none"/><circle cx="25.5" cy="42.9" r="1.6" fill="#8a4f1f" stroke="none"/><circle cx="18.9" cy="45.6" r="1.4" fill="#e1b46d" stroke="none"/><circle cx="14.5" cy="47.9" r="1.3" fill="#6b9a3f" stroke="none"/><circle cx="23.3" cy="49.5" r="1.4" fill="#6b9a3f" stroke="none"/><circle cx="20.6" cy="41.8" r="1.1" fill="#4f7d2e" stroke="none"/><circle cx="44" cy="44" r="11" fill="#c3894a"/><circle cx="39.0" cy="40.1" r="1.5" fill="#8a4f1f" stroke="none"/><circle cx="45.1" cy="37.4" r="1.3" fill="#e1b46d" stroke="none"/><circle cx="49.5" cy="42.9" r="1.6" fill="#8a4f1f" stroke="none"/><circle cx="42.9" cy="45.6" r="1.4" fill="#e1b46d" stroke="none"/><circle cx="38.5" cy="47.9" r="1.3" fill="#6b9a3f" stroke="none"/><circle cx="47.3" cy="49.5" r="1.4" fill="#6b9a3f" stroke="none"/><circle cx="44.5" cy="41.8" r="1.1" fill="#4f7d2e" stroke="none"/><circle cx="32" cy="30" r="12" fill="#c3894a"/><circle cx="26.6" cy="25.8" r="1.7" fill="#8a4f1f" stroke="none"/><circle cx="33.2" cy="22.8" r="1.4" fill="#e1b46d" stroke="none"/><circle cx="38.0" cy="28.8" r="1.8" fill="#8a4f1f" stroke="none"/><circle cx="30.8" cy="31.8" r="1.6" fill="#e1b46d" stroke="none"/><circle cx="26.0" cy="34.2" r="1.4" fill="#6b9a3f" stroke="none"/><circle cx="35.6" cy="36.0" r="1.6" fill="#6b9a3f" stroke="none"/><circle cx="32.6" cy="27.6" r="1.2" fill="#4f7d2e" stroke="none"/></g></svg>`,
    parsnips: `<svg class="xmsvg" viewBox="0 0 64 64" aria-hidden="true" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.6">
<g stroke="#a88b4a"><path d="M13 8 L24 4 Q26 6 55 52 Q56 58 49 55 Q36 44 13 8Z" fill="#f3e6b8"/><path d="M22 20 q5 1 8 -2 M30 31 q4 1 7 -2 M37 42 q3 1 6 -2" fill="none"/></g>
<g stroke="#a5521a"><path d="M40 8 L56 20 Q22 52 10 58 Q4 58 6 52 Q12 40 40 8Z" fill="#f08a2c"/><path d="M30 24 l6 4 M22 33 l5 4 M15 43 l4 3" fill="none"/><path d="M42 12 l5 4" fill="none" stroke="#fbb465" stroke-width="2.2"/></g>
<g fill="#5a9440" stroke="#3a6a28"><path d="M40 8 Q37 0 30 1 Q31 8 40 8Z"/><path d="M40 8 Q46 0 53 3 Q49 10 40 8Z"/><path d="M56 20 Q63 22 62 30 Q54 28 56 20Z"/><path d="M18 6 Q16 -1 9 1 Q10 7 18 6Z"/></g></svg>`,
    sprouts: `<svg class="xmsvg" viewBox="0 0 64 64" aria-hidden="true" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.6"><ellipse cx="32" cy="54" rx="27" ry="5" fill="#d3ccbc" stroke="none"/><ellipse cx="32" cy="53" rx="23" ry="3.6" fill="#e8e2d4" stroke="none"/><circle cx="20" cy="38" r="15" fill="#6fa83f" stroke="#3a6a28"/><path d="M8.0 35.0 Q18.5 45.5 30.5 29.8" fill="none" stroke="#3a6a28"/><path d="M18.5 23.0 Q11.0 39.5 18.5 53.0" fill="none" stroke="#3a6a28"/><path d="M24.5 24.5 Q33.5 38.0 26.0 50.8" fill="none" stroke="#3a6a28"/><ellipse cx="14.8" cy="30.5" rx="3.8" ry="2.1" fill="#a8d878" stroke="none"/><circle cx="44" cy="34" r="14" fill="#82bb4a" stroke="#3a6a28"/><path d="M32.8 31.2 Q42.6 41.0 53.8 26.3" fill="none" stroke="#3a6a28"/><path d="M42.6 20.0 Q35.6 35.4 42.6 48.0" fill="none" stroke="#3a6a28"/><path d="M48.2 21.4 Q56.6 34.0 49.6 45.9" fill="none" stroke="#3a6a28"/><ellipse cx="39.1" cy="27.0" rx="3.5" ry="2.0" fill="#b6e085" stroke="none"/><circle cx="33" cy="46" r="9" fill="#5f9a35" stroke="#3a6a28"/><path d="M25.8 44.2 Q32.1 50.5 39.3 41.0" fill="none" stroke="#3a6a28"/><path d="M32.1 37.0 Q27.6 46.9 32.1 55.0" fill="none" stroke="#3a6a28"/><path d="M35.7 37.9 Q41.1 46.0 36.6 53.6" fill="none" stroke="#3a6a28"/><ellipse cx="29.9" cy="41.5" rx="2.2" ry="1.3" fill="#9ccb6a" stroke="none"/></svg>`,
    gravy: `<svg class="xmsvg" viewBox="0 0 64 64" aria-hidden="true" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.6"><ellipse cx="32" cy="54" rx="27" ry="5" fill="#d3ccbc" stroke="none"/><ellipse cx="32" cy="53" rx="23" ry="3.6" fill="#e8e2d4" stroke="none"/>
<g stroke="#7d7d7d"><path d="M6 25 L0 14 Q11 17 17 25Z" fill="#fff"/>
<path d="M6 25 H53 Q50 42 30 45 Q10 42 6 25Z" fill="#fff"/>
<path d="M52 28 Q61 28 60 36 Q58 41 50 39" fill="none" stroke-width="2.6"/>
<rect x="26" y="45" width="8" height="5" fill="#fff"/>
<ellipse cx="30" cy="51" rx="13" ry="2.6" fill="#fff"/></g>
<ellipse cx="29.5" cy="25" rx="23" ry="3.4" fill="#6a3918" stroke="#43230c"/>
<path d="M3 17 Q1.5 24 3 29" fill="none" stroke="#6a3918" stroke-width="3"/>
<circle cx="3" cy="33" r="1.8" fill="#6a3918" stroke="none"/>
<ellipse cx="22" cy="24" rx="6" ry="1.1" fill="#a3622d" stroke="none"/>
<path d="M11 31 Q17 40 28 41" fill="none" stroke="#e4e0d8" stroke-width="2"/></svg>`,
    cranberry: `<svg class="xmsvg" viewBox="0 0 64 64" aria-hidden="true" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.6"><ellipse cx="32" cy="54" rx="27" ry="5" fill="#d3ccbc" stroke="none"/><ellipse cx="32" cy="53" rx="23" ry="3.6" fill="#e8e2d4" stroke="none"/>
<path d="M8 28 H56 Q55 47 32 50 Q9 47 8 28Z" fill="#b3202e" stroke="#6e1219"/>
<ellipse cx="32" cy="28" rx="24" ry="6" fill="#d02c3d" stroke="#6e1219"/>
<g fill="#c4262e" stroke="#6e1219"><circle cx="22" cy="23" r="5"/><circle cx="33" cy="20" r="5"/><circle cx="43" cy="24" r="5"/><circle cx="31" cy="27" r="4.4"/></g>
<g fill="#f7b5bb" stroke="none"><circle cx="20.5" cy="21.5" r="1.4"/><circle cx="31.5" cy="18.5" r="1.4"/><circle cx="41.5" cy="22.5" r="1.4"/></g>
<path d="M13 35 Q14 42 20 45" fill="none" stroke="#f3a2aa" stroke-width="2.6"/>
<path d="M24 52 H40" stroke="#8a857a" stroke-width="2.4"/></svg>`,
    yorkie: `<svg class="xmsvg" viewBox="0 0 64 64" aria-hidden="true" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.6"><ellipse cx="32" cy="54" rx="27" ry="5" fill="#d3ccbc" stroke="none"/><ellipse cx="32" cy="53" rx="23" ry="3.6" fill="#e8e2d4" stroke="none"/>
<path d="M10 30 Q8 46 32 50 Q56 46 54 30Z" fill="#d9a043" stroke="#8a4b1f"/>
<circle cx="54.0" cy="30.0" r="5.2" fill="#e8b155" stroke="#8a4b1f"/><circle cx="50.8" cy="34.7" r="5.2" fill="#e8b155" stroke="#8a4b1f"/><circle cx="42.0" cy="38.0" r="5.2" fill="#e8b155" stroke="#8a4b1f"/><circle cx="30.3" cy="39.0" r="5.2" fill="#e8b155" stroke="#8a4b1f"/><circle cx="19.1" cy="37.3" r="5.2" fill="#e8b155" stroke="#8a4b1f"/><circle cx="11.7" cy="33.4" r="5.2" fill="#e8b155" stroke="#8a4b1f"/><circle cx="10.3" cy="28.6" r="5.2" fill="#e8b155" stroke="#8a4b1f"/><circle cx="15.3" cy="24.1" r="5.2" fill="#e8b155" stroke="#8a4b1f"/><circle cx="25.2" cy="21.4" r="5.2" fill="#e8b155" stroke="#8a4b1f"/><circle cx="37.2" cy="21.3" r="5.2" fill="#e8b155" stroke="#8a4b1f"/><circle cx="47.6" cy="23.7" r="5.2" fill="#e8b155" stroke="#8a4b1f"/><circle cx="53.4" cy="27.9" r="5.2" fill="#e8b155" stroke="#8a4b1f"/>
<ellipse cx="32" cy="30" rx="18" ry="6.8" fill="#e8b155" stroke="#8a4b1f"/>
<ellipse cx="32" cy="31" rx="14" ry="5" fill="#b0661a" stroke="#7a3f12"/>
<ellipse cx="32" cy="32" rx="9" ry="2.8" fill="#6a3918" stroke="none"/>
<path d="M16 42 Q22 47 30 48" fill="none" stroke="#f8d796" stroke-width="2.4"/></svg>`,
    ketchup: `<svg class="xmsvg" viewBox="0 0 64 64" aria-hidden="true" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.6">
<path d="M26 12 H38 L35 2 H29Z" fill="#fff" stroke="#8a857a"/>
<rect x="26" y="12" width="12" height="9" fill="#c4262e" stroke="#7a1219"/>
<path d="M26 21 Q12 24 12 38 V54 Q12 60 18 60 H46 Q52 60 52 54 V38 Q52 24 38 21Z" fill="#c4262e" stroke="#7a1219"/>
<path d="M17 36 Q17 28 24 26" fill="none" stroke="#ee7b80" stroke-width="2.6"/>
<rect x="18" y="38" width="28" height="16" rx="3" fill="#fff6e0" stroke="#7a1219"/>
<circle cx="32" cy="46.5" r="5" fill="#d83a3a" stroke="#7a1219"/><path d="M29.5 42.5 l2.5 2 l2.5 -2" fill="none" stroke="#3a6a28" stroke-width="1.8"/></svg>`,
  };
  ITEMS.forEach((i) => { i.svg = SVGS[i.k] || ''; });
  const ico = (i) => (i && i.svg ? `<span class="xmico">${i.svg}</span>` : (i ? i.icon : ''));
  const RARITY = { 1: { label: 'Common', stars: '⭐', share: 1, diff: 'easy' }, 2: { label: 'Uncommon', stars: '⭐⭐', share: 0.6, diff: 'medium' }, 3: { label: 'Rare', stars: '⭐⭐⭐', share: 0.35, diff: 'hard' }, 4: { label: 'The 1% question', stars: '🍅', share: 1, diff: 'hard' } };

  // The family. quirk: always on. power: used once, between questions. need: what the phone must ask for ('item' = a missing common item, 'target' = a player, 'steal' = a player and an item, none = just press it).
  const CHARS = [
    { k: 'nan', icon: '👵', name: 'Nan', quirk: 'Not on my watch: the first time anyone tries to steal from you or swap with you, it fails.', power: 'Handbag Surprise', how: 'Pull any one missing common item (turkey, potatoes or pigs in blankets) out of your handbag.', need: 'item' },
    { k: 'grandad', icon: '👴', name: 'Grandad', quirk: 'Wakes up for the good stuff: +300 points every time you collect a rare item.', power: 'Wake Up!', how: 'On the next item question your points double, and if you get it right you collect the item even if you were not quick enough.', need: '' },
    { k: 'teen', icon: '🧒', name: 'The Teenager', quirk: 'Headphones in: the elf cannot touch your dish.', power: 'Hide in Your Room', how: 'Nobody can steal from you or swap with you for the next six item questions.', need: '' },
    { k: 'dog', icon: '🐕', name: 'The Dog', quirk: 'Under the table: when you steal, nobody is told who did it.', power: 'Snatch the Sausage', how: 'Steal any one item from anybody, right now.', need: 'steal' },
    { k: 'cousin', icon: '🧠', name: 'Know-It-All Cousin', quirk: 'Well, actually: +100 points whenever you get an item question wrong.', power: 'Insurance', how: 'On the next item question, if you get it wrong you still collect the item.', need: '' },
    { k: 'maureen', icon: '🥂', name: 'Auntie Maureen', quirk: 'Sharp eyes after a sherry: the first time the elf comes, you see him three seconds before everyone else.', power: 'Spill the Gravy', how: 'Pick a player: on their next item question they cannot collect, even if they get it right.', need: 'target' },
    { k: 'keith', icon: '🧔', name: 'Uncle Keith', quirk: 'Dodgy: your steals ignore shields, bedrooms and Nan.', power: 'Dodgy Deal', how: 'Take a random item from whoever has the fullest dish.', need: '' },
    { k: 'mum', icon: '👩', name: 'Mum', quirk: 'Organised: each missing item costs you 1,500 at the end, not 2,000.', power: 'Swap Seats', how: 'Swap one random item with a player you pick: you each give one the other does not have.', need: 'target' },
  ];

  // The day, from stockings to midnight. Shown as a clock on the host screen and on the dish.
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

  const CFG = { PINCH_EVERY: 5, DARK_QS: 4, PICK_MS: 20000, PINCH_MS: 30000, ELF_SPOT_MS: 14000, ELF_CHOOSE_MS: 25000, MAUREEN_HEAD_START_MS: 3000, MISSING: -2000, FULL: 5000, HIDE_Q: 6, WAKE_RARE: 300, COUSIN_WRONG: 100 };
  const share = (rar) => (RARITY[rar] || RARITY[1]).share;

  window.LQ = window.LQ || {};
  LQ.XMAS = { ico, ITEMS, RARITY, CHARS, SCENES, KETCHUP_QS, CFG, share, item: (k) => ITEMS.find((i) => i.k === k) || null, char: (k) => CHARS.find((c) => c.k === k) || null, dishes: () => ITEMS.filter((i) => !i.ketchup) };
  /** The clock for a share of the night gone (0 to 1): 07:00 to midnight, and the scene it falls in. */
  LQ.XMAS.clock = (p) => {
    p = Math.max(0, Math.min(1, p || 0));
    const mins = Math.round((7 + p * 17) * 60), h = Math.floor(mins / 60) % 24, m = mins % 60;
    let sc = SCENES[0]; for (const s of SCENES) if (p >= s.t) sc = s;
    return { time: String(h).padStart(2, '0') + ':' + String(m).padStart(2, '0'), icon: sc.icon, scene: sc.name };
  };
})();
