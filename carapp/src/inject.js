// The two scripts the app puts into the game page (react-native-webview injects them). Plain CommonJS so the tests can load them in Node.
//
// speech: runs in EVERY frame before the page's own scripts. A web view has no speech recognition of its own, so this gives the page a
// SpeechRecognition that asks the app to listen (expo-speech-recognition). The page's boxes-voice.js uses it as it would use Safari's.
// bridge: runs once in the main frame after the page has loaded. It reads what the player's phone view knows (the "play" frame inside
// warmup.html), tells the app a small summary for the car screen, and lets the app send taps back (window.lqAct = a tap on the phone).
const speech = String.raw`
(function () {
  var T;
  try { T = window.top; T.__lqSR = T.__lqSR || { n: 0, inst: {} }; } catch (e) { return; }
  var post = function (m) { try { m.t = 'speech'; (window.ReactNativeWebView || T.ReactNativeWebView).postMessage(JSON.stringify(m)); } catch (e) {} };
  function SR() { this.id = ++T.__lqSR.n; this.lang = 'en-GB'; this.continuous = false; this.interimResults = false; this.maxAlternatives = 1; T.__lqSR.inst[this.id] = this; }
  SR.prototype.start = function () { post({ op: 'start', id: this.id, lang: this.lang }); };
  SR.prototype.stop = function () { post({ op: 'stop', id: this.id }); };
  SR.prototype.abort = function () { post({ op: 'abort', id: this.id }); };
  window.SpeechRecognition = SR;
  window.webkitSpeechRecognition = SR;
  T.__lqSRDone = function (id, alts) {
    var r = T.__lqSR.inst[id]; if (!r) return; delete T.__lqSR.inst[id];
    try { if (alts && alts.length && r.onresult) r.onresult({ results: [alts.map(function (t) { return { transcript: t }; })] }); } catch (e) {}
    try { if (r.onend) r.onend(); } catch (e) {}
  };
  try { localStorage.setItem('lq_handsfree', '1'); } catch (e) {}
})();
true;
`;

const bridge = String.raw`
(function () {
  if (window.__lqBridge) return; window.__lqBridge = true;
  var last = '';
  var frame = function () { var f = document.getElementById('playFrame'); return f && f.contentWindow; };
  window.lqAct = function (k, v, extra) { var w = frame(); if (w && typeof w.bxSend === 'function') w.bxSend(k, v, extra || {}); };
  window.lqCompact = function () {
    var w = frame(); if (!w) return null;
    var P = null; try { P = w.eval('typeof P === "undefined" ? null : P'); } catch (e) {} // P is a top-level const in the game page, so it is not a window property
    if (!P || !P.state) return null;
    var s = P.state, g = s.bx, out = { phase: s.phase || '' };
    if (s.phase === 'final' && g) {
      out.final = g.teams.map(function (t) { return { n: t.name, e: t.emoji || '', v: Math.max(0, t.pot) - (t.loan || 0) }; }).sort(function (a, b) { return b.v - a.v; });
      return out;
    }
    if (!g || s.phase !== 'question') { out.note = s.phase === 'lobby' ? 'Waiting for the other player…' : ''; return out; }
    var me = w.bxMe(s), c = g.cur, T = function (i) { return g.teams[i] || { name: '', emoji: '', pot: 0 }; };
    out.me = me.t ? me.t.name : '';
    out.pot = me.t ? me.t.pot : 0;
    out.step = g.step;
    out.cats = g.cats.map(function (x) { return { n: x.n, e: x.e || '' }; });
    out.cols = g.cols; out.board = g.board.slice();
    out.teams = g.teams.map(function (t) { return { name: t.name, emoji: t.emoji || '', pot: t.pot }; });
    var needs = 'wait', note = '';
    if (g.step === 'seg' && g.solo) needs = g.part === 1 ? 'go' : 'next';
    else if (g.step === 'pick') { if (g.pickTeam === me.ti) needs = 'pick'; else note = T(g.pickTeam).name + ' is choosing a box'; }
    else if (g.step === 'stake') { if (g.turn === me.ti) { needs = 'stake'; out.stakes = (me.t && me.t.stakes) || []; } else note = T(g.turn).name + ' is deciding how much to gamble'; }
    else if (g.step === 'ask' && c) { if (c.by === me.ti && !c.locked && c.mode !== 'host') needs = 'answer'; else note = T(c.by).name + ' is answering'; }
    else if (g.step === 'result') needs = 'next';
    else if (g.step === 'open') note = 'Opening box ' + (c ? c.num : '') + '…';
    else if (g.step === 'locked') note = 'Locked in…';
    out.needs = needs; out.note = note;
    if (c) {
      out.cur = { num: c.num, cat: g.cats[c.cat] ? g.cats[c.cat].n : '', stake: c.stake || 0, by: T(c.by).name, canPass: !!c.canPass, tune: !!(c.q && c.q.m && c.q.m.k === 'tune') };
      if (g.step === 'ask' || g.step === 'locked' || g.step === 'result') { out.cur.text = c.q.t; out.cur.opts = c.q.opts || null; }
      if (g.step === 'result' && c.res) out.cur.res = { ok: c.res.ok === null || c.res.ok === undefined ? null : !!c.res.ok, passed: !!c.res.passed, right: c.res.right || '', delta: c.res.delta || 0, who: T(c.res.team).name };
    }
    return out;
  };
  var tick = function () {
    var out; try { out = window.lqCompact(); } catch (e) { out = null; }
    var j = JSON.stringify(out || { phase: '' });
    if (j === last) return; last = j;
    try { window.ReactNativeWebView.postMessage(JSON.stringify({ t: 'state', s: j })); } catch (e) {}
  };
  setInterval(tick, 350); tick();
})();
true;
`;

module.exports = { speech, bridge };
