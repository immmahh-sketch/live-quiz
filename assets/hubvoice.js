/* Hands-free for the "Choose your quiz" pages: the phone reads the screen out and listens for what to do. Needs boxes-voice.js (bvSay, bvListen, BVP, BV) and hubkit.js.
 * One call, HV.screen({ prompt, items, hint }), per screen:
 *   - prompt: what to say first (read out in a natural British woman's voice);
 *   - items: what can be said. Each is { words: ['next', 'carry on'], fn } (any of those phrases, heard whole), or { test(alts) -> truthy, fn } for answers like "B";
 *   - buttons on the page with data-say="start|begin" are added automatically, so every button on screen can be said;
 *   - then: instead of listening, run this straight after the prompt has been read (a screen with nothing to ask);
 *   - always understood: "repeat" / "say that again" reads the prompt again.
 * A new screen cancels the one before. Nothing is spoken on the TV (the remote is used there) or when hands-free is off. */
window.HV = (() => {
  let tok = 0;
  const norm = (s) => (typeof BVP !== 'undefined' ? BVP.norm(s) : String(s || '').toLowerCase().replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim());
  const on = () => typeof BV !== 'undefined' && BV.on && !(window.HUB && HUB.mode.tv) && (BV_TTS || BV_SR);
  /** how a letter sounds when spoken to a phone */
  const SOUNDS = { a: ['a', 'ay', 'eh', 'hey'], b: ['b', 'be', 'bee', 'bea'], c: ['c', 'see', 'sea', 'si', 'cee'], d: ['d', 'dee'], e: ['e', 'ee'], f: ['f', 'eff', 'ef'], g: ['g', 'gee', 'jee'], h: ['h', 'aitch', 'age'], i: ['i', 'eye', 'aye'], j: ['j', 'jay'], k: ['k', 'kay'], l: ['l', 'el', 'ell'], m: ['m', 'em'], n: ['n', 'en'], o: ['o', 'oh'], p: ['p', 'pee'], q: ['q', 'queue', 'cue'] };
  const LETTERS = 'abcdefghijklmnopq';
  /** "B", "option b", "letter bee", "the second one" -> 0-based index below n, or -1 */
  function letterIndex(text, n) {
    const w = norm(text).split(' ').filter(Boolean); if (!w.length) return -1;
    const ORD = { first: 0, second: 1, third: 2, fourth: 3, fifth: 4, sixth: 5, seventh: 6, eighth: 7 };
    const lead = new Set(['option', 'answer', 'letter', 'number', 'choose', 'pick', 'select', 'is', 'its', 'it', 'the']);
    const core = w.filter((x) => !lead.has(x));
    if (core.length === 1 || (w.length <= 3 && core.length <= 2)) for (const x of core) for (let i = 0; i < Math.min(n, LETTERS.length); i++) if (SOUNDS[LETTERS[i]].includes(x)) return i;
    for (const x of w) if (x in ORD && ORD[x] < n) return ORD[x];
    return -1;
  }
  /** does what was heard say one of these phrases (whole words, in order)? */
  function hears(alts, words) {
    for (const a of alts) { const h = ' ' + norm(a) + ' '; for (const p of words) { const q = norm(p); if (q && h.includes(' ' + q + ' ')) return true; } }
    return false;
  }
  /** the page's own buttons that can be said: data-say="start|begin" */
  function domItems(root = document) {
    return [...root.querySelectorAll('[data-say]')].filter((el) => !el.disabled && el.getClientRects().length && !el.closest('[hidden]'))
      .map((el) => ({ words: el.dataset.say.split('|').map((x) => x.trim()).filter(Boolean), fn: () => el.click(), el }));
  }
  async function screen({ prompt = '', items = [], hint = '', dom = true, listenMs = 11000, then = null } = {}) {
    if (!on()) return null;
    const my = ++tok; try { bvAbort(); } catch {}
    const all = () => [...items, ...(dom ? domItems() : [])];
    let say = prompt, miss = 0;
    for (let round = 0; round < 6 && my === tok; round++) {
      if (say) { await bvSay(say); if (my !== tok) return null; }
      if (then) { tok++; try { await then(); } catch (e) { console.error(e); } return null; } // nothing to ask: read it, then carry on by itself
      const alts = await bvListen(listenMs); if (my !== tok) return null;
      if (!alts.length) { say = (miss++ ? '' : 'I did not hear anything. ') + (hint || bvText(prompt)); if (miss > 3) break; continue; }
      if (hears(alts, ['repeat', 'say that again', 'say again', 'pardon', 'what was that', 'read it again', 'read that again'])) { say = prompt; continue; }
      let hit = null;
      for (const it of all()) { const ok = it.test ? it.test(alts) : hears(alts, it.words || []); if (ok !== false && ok !== null && ok !== undefined && ok !== -1) { hit = { it, ok }; break; } }
      if (hit) { tok++; try { await hit.it.fn(hit.ok); } catch (e) { console.error(e); } return hit.it; }
      say = 'Sorry, I did not get that. ' + (hint || 'Say repeat to hear the choices again.'); if (++miss > 3) break;
    }
    if (my === tok) { try { bvStatus('Tap 🎙 to try again'); } catch {} }
    return null;
  }
  const stop = () => { tok++; try { bvAbort(); } catch {} };
  /** the hands-free switch, bottom of the screen (not on the TV). rerun() starts the current screen's voice again. */
  function button(rerun) {
    if (!window.HUB || HUB.mode.tv || typeof BV_TTS === 'undefined' || !(BV_TTS || BV_SR) || document.getElementById('hvbtn')) return;
    const wrap = document.createElement('div'); wrap.id = 'hvbtn'; wrap.style.cssText = 'position:fixed;left:0;right:0;bottom:calc(8px + env(safe-area-inset-bottom,0px));z-index:40;display:flex;flex-direction:column;align-items:center;gap:4px;pointer-events:none';
    wrap.innerHTML = '<div id="bvstat" style="max-width:92%;font-size:.8rem;color:#fff;background:rgba(20,16,50,.82);border-radius:10px;padding:3px 10px;display:none"></div><button type="button" id="hvtog" class="btn" style="pointer-events:auto;border-radius:999px;padding:7px 14px;font-weight:800;font-size:.85rem"></button>';
    document.body.appendChild(wrap);
    const tog = wrap.querySelector('#hvtog'), stat = wrap.querySelector('#bvstat');
    new MutationObserver(() => { stat.style.display = stat.textContent ? 'block' : 'none'; }).observe(stat, { childList: true, characterData: true, subtree: true });
    const paint = () => { tog.textContent = BV.on ? '🎙️ Hands-free: ON (tap to turn off)' : '🎙️ Hands-free'; tog.style.background = BV.on ? '#2e9d57' : 'rgba(255,255,255,.16)'; };
    tog.onclick = () => {
      BV.on = !BV.on; try { localStorage.setItem('lq_handsfree', BV.on ? '1' : '0'); } catch {} paint(); stop(); bvMedia(BV.on);
      if (BV.on) { try { if (BV_TTS) { speechSynthesis.cancel(); speechSynthesis.speak(new SpeechSynthesisUtterance('')); } } catch {} rerun && rerun(); }
    };
    paint(); if (BV.on) bvMedia(true);
  }
  return { on, screen, stop, button, letterIndex, hears, norm, LETTERS };
})();
