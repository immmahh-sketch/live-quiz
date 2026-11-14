// What the car screen shows, worked out from the game's state. Pure functions: no CarPlay, no React, so they can be tested alone.
export type Cat = { n: string; e: string };
export type Res = { ok: boolean | null; passed: boolean; right: string; delta: number; who: string };
export type Cur = { num: number; cat: string; stake: number; by: string; canPass: boolean; tune: boolean; text?: string; opts?: string[] | null; res?: Res };
export type GameState = {
  phase: string; note?: string; me?: string; pot?: number; step?: string; needs?: 'go' | 'pick' | 'stake' | 'answer' | 'next' | 'wait';
  cats?: Cat[]; cols?: number; board?: string[]; teams?: { name: string; emoji: string; pot: number }[]; stakes?: number[]; cur?: Cur;
  final?: { n: string; e: string; v: number }[];
};
/** A tap on a car row: either send something to the game, or change what the car screen is showing. */
export type Act = { send: [string, unknown, Record<string, unknown>?] } | { row: number | null };
export type Row = { text: string; detail?: string; act?: Act };

const fmt = (n: number) => Math.round(n).toLocaleString('en-GB');
const LETTERS = 'ABCD';

/** The rows of the car list. `openRow` is the category whose boxes are showing while picking a box (null: the categories). */
export function buildRows(s: GameState | null, openRow: number | null): { title: string; rows: Row[] } {
  if (!s || !s.phase) return { title: 'Box Clever', rows: [{ text: 'Open Box Clever on your iPhone', detail: 'Enter your name there once, and the game appears here.' }] };
  if (s.phase === 'final' && s.final) {
    return { title: 'Game over', rows: s.final.map((f, i) => ({ text: `${i === 0 ? '🏆 ' : ''}${f.e} ${f.n}`.trim(), detail: `${fmt(f.v)} points` })) };
  }
  if (s.phase !== 'question' || !s.needs) return { title: 'Box Clever', rows: [{ text: s.note || 'Waiting for the game…' }] };
  const head = s.me ? `${s.me}: ${fmt(s.pot ?? 0)} points` : 'Box Clever';
  const c = s.cur;
  switch (s.needs) {
    case 'go':
      return { title: head, rows: [{ text: "Let's go ▶", detail: `${(s.board || []).length} boxes. Everyone starts on ${fmt(s.pot ?? 0)}.`, act: { send: ['next', 1] } }] };
    case 'pick': {
      const cats = s.cats || [], cols = s.cols || 6, board = s.board || [];
      if (openRow === null) {
        return { title: `${head} · pick a box`, rows: cats.map((cat, r) => {
          const left = board.slice(r * cols, (r + 1) * cols).filter((x) => x === 'open').length;
          return { text: `${cat.e} ${cat.n}`.trim(), detail: left ? `${left} left · boxes ${r * cols + 1}–${(r + 1) * cols}` : 'all gone', act: left ? { row: r } as Act : undefined };
        }) };
      }
      const rows: Row[] = [{ text: '◀ Back', act: { row: null } }];
      for (let k = 0; k < cols; k++) { const n = openRow * cols + k + 1; if (board[n - 1] === 'open') rows.push({ text: `Box ${n}`, detail: cats[openRow]?.n, act: { send: ['pick', n, { go: true }] } }); }
      return { title: `${head} · ${cats[openRow]?.n || ''}`, rows };
    }
    case 'stake': {
      const st = s.stakes || [], pot = s.pot ?? 0;
      return { title: `${head} · box ${c?.num ?? ''}`, rows: st.map((amt, i) => ({ text: i === st.length - 1 ? `ALL IN ${fmt(amt)}` : `Gamble ${fmt(amt)}`, detail: i === 0 ? `${c?.cat ?? ''} · you have ${fmt(pot)}` : undefined, act: { send: ['stake', amt, { go: true }] } as Act })) };
    }
    case 'answer': {
      const rows: Row[] = [{ text: c?.text || 'Question', detail: `Box ${c?.num ?? ''} · ${c?.cat ?? ''} · stake ${fmt(c?.stake ?? 0)}` }];
      if (c?.opts) c.opts.forEach((o, i) => rows.push({ text: `${LETTERS[i]}  ${o}`, act: { send: ['ans', i, { go: true }] } }));
      else rows.push({ text: '🎙 Say your answer', detail: 'Hands-free is listening' });
      if (c?.canPass) rows.push({ text: 'Pass', detail: 'Lose half your stake', act: { send: ['pass', 1, { go: true }] } });
      return { title: head, rows };
    }
    case 'next': {
      const r = c?.res;
      const verdict = !r ? 'Next' : r.passed ? '🏳️ Passed' : r.ok ? '✅ Correct!' : `❌ Wrong · ${r.right}`;
      return { title: head, rows: [{ text: verdict, detail: r ? `${r.who} ${r.delta >= 0 ? '+' : '−'}${fmt(Math.abs(r.delta))}` : undefined }, { text: 'Next ▶', act: { send: ['next', 1] } }] };
    }
    default:
      return { title: head, rows: [{ text: s.note || 'Waiting…' }] };
  }
}
