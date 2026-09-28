// Face framing for the cameras on the quiz screen.
//
// Every camera from the quiz call (assets/quizcam.js) plays into a hidden <video> here. Face detection (MediaPipe's
// BlazeFace, run in the browser) looks at each one a few times a second, and each picture on screen is painted onto a
// <canvas> cropped around that face: head and shoulders in the corner tile, a close-up in the round player bubbles.
// The crop eases towards the face, so it follows people as they move without jumping. Two or more people on one
// camera are framed together: the crop takes in every face (a face far smaller than the biggest, like a photo on the
// wall or someone passing in the background, is left out). With no face in view, or if the detector cannot load,
// the crop settles on the middle of the picture.
window.FaceCam = (() => {
  'use strict';
  const VISION = 'https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.14';
  const MODEL = 'https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite';
  const DETECT_MS = 120;      // one detection this often, taking turns between the cameras in use
  const FORGET_MS = 2500;     // no face for this long: back to the middle
  const EASE = 0.12;          // how far the crop moves towards the face each frame

  const tracks = new Map();   // key -> { video, stream, target, cur, seen, used }
  let detector = null, loading = null, failed = false, box = null, turn = 0, timer = null;

  async function load() {
    if (detector || failed) return detector;
    if (!loading) loading = (async () => {
      try {
        const v = await import(VISION + '/vision_bundle.mjs');
        const files = await v.FilesetResolver.forVisionTasks(VISION + '/wasm');
        const make = (delegate) => v.FaceDetector.createFromOptions(files, { baseOptions: { modelAssetPath: MODEL, delegate }, runningMode: 'IMAGE', minDetectionConfidence: 0.45 });
        try { detector = await make('GPU'); } catch { detector = await make('CPU'); }
      } catch (e) { console.warn('Face framing unavailable, using a centre crop:', e && e.message); failed = true; }
      return detector;
    })();
    return loading;
  }

  function holder() {
    if (box) return box;
    // In view but invisible: Chrome stops decoding muted videos it thinks nobody can see.
    box = document.createElement('div');
    box.style.cssText = 'position:fixed;left:0;bottom:0;width:4px;height:4px;overflow:hidden;opacity:.01;pointer-events:none;z-index:-1';
    document.body.appendChild(box);
    return box;
  }
  // What the crop follows: the box round every face (centre, width and height, as fractions of the picture) and
  // the size of one face (fh), which sets the headroom around them.
  const MIDDLE = () => ({ cx: 0.5, cy: 0.45, w: 0.2, h: 0.42, fh: 0.42 });

  /** Keeps camera `key` playing (or stops it when `stream` has no picture). */
  function setStream(key, stream) {
    let t = tracks.get(key);
    const live = !!stream && stream.getVideoTracks().some((x) => x.readyState === 'live');
    if (!live) { if (t) { t.video.srcObject = null; t.video.remove(); tracks.delete(key); } return; }
    if (!t) {
      const video = document.createElement('video');
      video.muted = true; video.playsInline = true; video.setAttribute('playsinline', '');
      holder().appendChild(video);
      t = { video, stream: null, target: MIDDLE(), cur: MIDDLE(), seen: 0, used: 0 };
      tracks.set(key, t);
    }
    if (t.stream !== stream) { t.stream = stream; t.video.srcObject = stream; t.video.play().catch(() => {}); }
    if (!timer) { timer = setInterval(detectOne, DETECT_MS); load(); }
  }
  function drop(key) { setStream(key, null); if (!tracks.size) { clearInterval(timer); timer = null; } }

  /** One detection, on the next camera that is on screen. */
  async function detectOne() {
    const now = Date.now();
    const live = [...tracks.entries()].filter(([, t]) => now - t.used < 1500 && t.video.readyState >= 2 && t.video.videoWidth);
    for (const [, t] of tracks) if (t.seen && now - t.seen > FORGET_MS) { t.target = MIDDLE(); t.seen = 0; }
    if (!live.length || !detector) return;
    const [, t] = live[turn++ % live.length];
    let res; try { res = detector.detect(t.video); } catch { return; }
    const vw = t.video.videoWidth, vh = t.video.videoHeight;
    const boxes = (res?.detections || []).map((d) => d.boundingBox).filter(Boolean).sort((a, b) => b.height - a.height);
    if (!boxes.length) return;
    // everyone in the room, but not the faces far smaller than the biggest (photos on the wall, people way behind)
    const faces = boxes.filter((b) => b.height >= boxes[0].height * 0.45).slice(0, 6);
    const x0 = Math.min(...faces.map((b) => b.originX)), x1 = Math.max(...faces.map((b) => b.originX + b.width));
    const y0 = Math.min(...faces.map((b) => b.originY)), y1 = Math.max(...faces.map((b) => b.originY + b.height));
    const fh = faces.reduce((a, b) => a + Math.max(b.height, b.width * 0.9), 0) / faces.length;
    t.target = { cx: (x0 + x1) / 2 / vw, cy: (y0 + y1) / 2 / vh, w: (x1 - x0) / vw, h: (y1 - y0) / vh, fh: fh / vh, n: faces.length };
    t.seen = now;
  }

  /** Once a frame, before painting: every crop moves a little towards its face. */
  function tick() {
    for (const t of tracks.values()) {
      const c = t.cur, g = t.target;
      for (const k of ['cx', 'cy', 'w', 'h', 'fh']) c[k] += (g[k] - c[k]) * EASE;
    }
  }

  /** Paints camera `key` onto `canvas`, cropped around the face. `zoom` is how many face-heights tall the picture is
   *  (3.2 is head and shoulders, 1.9 a close-up). Returns false if there is no picture yet. */
  function paint(canvas, key, zoom = 3) {
    const t = tracks.get(key); if (!t) return false;
    t.used = Date.now();
    const v = t.video, vw = v.videoWidth, vh = v.videoHeight;
    if (!vw || !vh || v.readyState < 2) return false;
    const dpr = Math.min(2, window.devicePixelRatio || 1);
    const cw = Math.max(2, Math.round(canvas.clientWidth * dpr)), ch = Math.max(2, Math.round(canvas.clientHeight * dpr));
    if (canvas.width !== cw) canvas.width = cw;
    if (canvas.height !== ch) canvas.height = ch;
    const aspect = cw / ch, f = t.cur;
    // The box round the faces plus headroom: for one face, a picture `zoom` faces tall with the face a touch above
    // the middle; for a group, the same margins round all of them, so nobody is cut off.
    const pad = f.fh * vh * (zoom - 1) / 2;
    const top = (f.cy - f.h / 2) * vh - pad * 0.92, bottom = (f.cy + f.h / 2) * vh + pad * 1.08;
    const needW = f.w * vw + pad * 2.8; // room for the outer shoulders either side
    let h = Math.min(vh, Math.max(vh * 0.22, bottom - top, needW / aspect)), w = h * aspect;
    if (w > vw) { w = vw; h = w / aspect; }
    const x = Math.min(vw - w, Math.max(0, f.cx * vw - w / 2));
    const y = Math.min(vh - h, Math.max(0, (top + bottom) / 2 - h / 2));
    canvas.getContext('2d').drawImage(v, x, y, w, h, 0, 0, cw, ch);
    return true;
  }

  /** For diagnosing: what the crop is following on camera `key`. */
  const debug = (key) => { const t = tracks.get(key); return t ? { target: t.target, cur: t.cur, seen: t.seen } : null; };

  return { setStream, drop, tick, paint, debug, has: (key) => tracks.has(key), get tracking() { return !!detector; } };
})();
