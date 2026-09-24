// Let's Quiz! — D-pad navigation for TVs.
//
// A Fire TV remote sends ArrowUp/Down/Left/Right and Enter to the page. This moves a visible
// focus ring between the page's buttons and fields by geometry (nearest thing in the direction
// pressed), clicks the focused thing on Enter, and keeps something focused after every redraw.
// It switches itself on when the page says it is a TV (body.tv), when the URL has ?tv=1, or
// when the TV app's browser identifies itself.
window.DPAD = (() => {
  const params = new URLSearchParams(location.search);
  const isTv = () => document.body.classList.contains('tv') || params.get('tv') === '1' || /LetsQuizTV/.test(navigator.userAgent);
  const SEL = 'button:not([disabled]), a[href], input:not([disabled]):not([type=hidden]), textarea:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])';

  function visible(el) {
    if (el.closest('.hidden, [hidden]')) return false;
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height) return false;
    const st = getComputedStyle(el);
    return st.visibility !== 'hidden' && st.display !== 'none' && r.bottom > 0 && r.right > 0 && r.top < innerHeight && r.left < innerWidth;
  }
  /** The elements the ring can land on. A modal, when open, is the only place to look. */
  function candidates() {
    const modal = document.querySelector('.modal-bg .modal, .modal-bg');
    const root = modal || document;
    return [...root.querySelectorAll(SEL)].filter(visible);
  }
  const mid = (r) => ({ x: r.left + r.width / 2, y: r.top + r.height / 2 });

  /** Picks the best element in a direction: must overlap the axis of travel, nearest first. */
  function pick(from, dir) {
    const fr = from.getBoundingClientRect(), fm = mid(fr);
    let best = null, bestScore = Infinity, fallback = null, fbScore = Infinity;
    for (const el of candidates()) {
      if (el === from) continue;
      const r = el.getBoundingClientRect(), m = mid(r);
      let primary, ortho, aligned;
      if (dir === 'ArrowDown') { primary = r.top - fr.bottom; ortho = Math.abs(m.x - fm.x); aligned = r.right > fr.left && r.left < fr.right; if (m.y <= fm.y) continue; }
      else if (dir === 'ArrowUp') { primary = fr.top - r.bottom; ortho = Math.abs(m.x - fm.x); aligned = r.right > fr.left && r.left < fr.right; if (m.y >= fm.y) continue; }
      else if (dir === 'ArrowRight') { primary = r.left - fr.right; ortho = Math.abs(m.y - fm.y); aligned = r.bottom > fr.top && r.top < fr.bottom; if (m.x <= fm.x) continue; }
      else { primary = fr.left - r.right; ortho = Math.abs(m.y - fm.y); aligned = r.bottom > fr.top && r.top < fr.bottom; if (m.x >= fm.x) continue; }
      primary = Math.max(0, primary);
      const score = primary + ortho * (aligned ? 0.6 : 2.5);
      if (aligned) { if (score < bestScore) { best = el; bestScore = score; } }
      else if (score < fbScore) { fallback = el; fbScore = score; }
    }
    return best || fallback;
  }

  function focus(el) {
    if (!el) return;
    el.focus({ preventScroll: true });
    try { el.scrollIntoView({ block: 'nearest', inline: 'nearest', behavior: 'smooth' }); } catch {}
  }
  /** Focuses the page's natural starting point: [data-autofocus] first, else the primary button, else the first thing. */
  function focusFirst(root = document) {
    const list = candidates();
    const pref = [...root.querySelectorAll('[data-autofocus], .btn-primary')].find((el) => list.includes(el));
    focus(pref || list[0]);
  }
  const inText = (el) => el && (el.tagName === 'TEXTAREA' || (el.tagName === 'INPUT' && !['checkbox', 'radio', 'button', 'range'].includes(el.type)));

  function onKey(e) {
    if (!isTv()) return;
    const a = document.activeElement;
    const arrows = ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'];
    if (arrows.includes(e.key)) {
      // Inside a text box, left and right move the caret until it reaches an edge.
      if (inText(a) && (e.key === 'ArrowLeft' || e.key === 'ArrowRight')) {
        const atStart = a.selectionStart === 0, atEnd = a.selectionEnd === (a.value || '').length;
        if ((e.key === 'ArrowLeft' && !atStart) || (e.key === 'ArrowRight' && !atEnd)) return;
      }
      e.preventDefault(); e.stopImmediatePropagation();
      if (!a || a === document.body || !candidates().includes(a)) return focusFirst();
      focus(pick(a, e.key));
      return;
    }
    if (e.key === 'Enter') {
      if (!a || a === document.body) return; // pages handle Enter themselves when nothing is focused
      if (a.tagName === 'BUTTON' || a.tagName === 'A' || a.hasAttribute('tabindex')) { e.preventDefault(); e.stopImmediatePropagation(); a.click(); }
      else if (a.tagName === 'INPUT' && (a.type === 'checkbox' || a.type === 'radio')) { e.preventDefault(); e.stopImmediatePropagation(); a.click(); }
      else if (inText(a) && a.tagName === 'INPUT') { // Enter in a field: move on to the next thing
        e.preventDefault(); e.stopImmediatePropagation(); const n = pick(a, 'ArrowDown') || pick(a, 'ArrowRight'); if (n) focus(n); else a.blur();
      }
    }
  }
  document.addEventListener('keydown', onKey, true);

  // After a redraw the focused element is usually gone; put the ring back on something.
  let pending = null;
  const mo = new MutationObserver(() => {
    if (!isTv()) return;
    clearTimeout(pending);
    pending = setTimeout(() => { const a = document.activeElement; if (!a || a === document.body || !document.contains(a) || !visible(a)) focusFirst(); }, 60);
  });
  document.addEventListener('DOMContentLoaded', () => {
    if (isTv()) document.body.classList.add('tv');
    mo.observe(document.body, { childList: true, subtree: true });
    if (isTv()) setTimeout(focusFirst, 100);
  });
  return { isTv, focusFirst, focus, candidates };
})();
