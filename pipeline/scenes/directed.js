// directed.js - hand-directed shots. Each shot in story/shots.json with params.tpl === 'dir' carries params.dir,
// a storyboard written by reading the script (not keyword matching):
//   set:    room | bathroom | kitchen | office | hallway | night | city | highway | map | face | end
//   cam:    { z: [from, to], x: [from, to], y: [from, to] }   (lerped over the shot)
//   actors: [{ id, outfit?, x: [[p, xFrac], ...], s, facing, pose: [[p, name], ...], expr: [[p, name], ...],
//              hold: { k, from?, to? }, talk: [p0, p1], rot, alpha: [[p, a], ...], lie }]
//   items:  [{ k, x, ...options }]   world objects drawn on the floor line (door, bed, sink, desk, bagel ...)
//   text:   [{ s, x, y, at, size, color }]
// Times are fractions of the shot (0..1) so the board survives small changes in voice timing.
import { E, V, S, mood, layer, backdrop, ease, prog, clamp, lerp, seg, circle, ring, rr, poly, glow, alpha, shade, mix, text, linGrad, radGrad, rng, FONTS } from '/engine/core.js';
import { drawFigure, POSES, posesAt, breathe, walkPose, bigFace, blendPose } from '/engine/rig2d.js';
import * as FX from '/engine/fx2d.js';
import { drawSet } from './sets.js';
import { drawProp } from './props.js';

const GY = () => E.H * 0.8;
export const OUTFITS = {
  rio: { top: 'hoodie', color: '#2d7fe0', head: 'curly', headColor: '#0e0b12' },
  rioSuit: { top: 'suit', color: '#2a3a5a', head: 'curly', headColor: '#0e0b12' },
  guard: { top: 'jersey', color: '#2a2a3a', head: 'cap', headColor: '#1a1a22' },
  rioPj: { top: 'tshirt', color: '#7a8ad8', head: 'curly', headColor: '#0e0b12' },
  max: { top: 'tshirt', color: '#e0532f', head: 'cap', headColor: '#7a2a18' },
  linda: { top: 'dress', color: '#c86a9a', head: 'bun', headColor: '#3a2a2a' },
  boss: { top: 'suit', color: '#2a2a3a', head: 'none' },
  elder: { top: 'suit', color: '#6a5a4a', head: 'fedora', headColor: '#4a3a2a', face: 'glasses' },
  victor: { top: 'suit', color: '#1e2230', head: 'none', face: 'sunglasses' },
  nurse: { top: 'tshirt', color: '#5ac0b0', head: 'bun', headColor: '#2a1a1a' },
  doctor: { top: 'labcoat', face: 'glasses', head: 'none' },
  oldman: { top: 'suit', color: '#7a6a5a', head: 'none', face: 'glasses' },
  oldwoman: { top: 'dress', color: '#9a7ab0', head: 'bun', headColor: '#d8d8d8', face: 'glasses' },
  zoe: { top: 'tshirt', color: '#5ac0b0', head: 'ponytail', headColor: '#3a1a12' },
  zoeRich: { top: 'suit', color: '#c8a040', head: 'ponytail', headColor: '#3a1a12', face: 'sunglasses' },
  grandma: { top: 'dress', color: '#c87a5a', head: 'bun', headColor: '#e0e0e0', face: 'glasses' },
  leo: { top: 'jersey', color: '#3aa876', head: 'beanie', headColor: '#1a5a3a' },
  mia: { top: 'dress', color: '#e06aa0', head: 'ponytail', headColor: '#3a1a12' },
  sam: { top: 'tshirt', color: '#f2c21a', head: 'cap', headColor: '#7a5a10' },
  dad: { top: 'trench', color: '#6a4a3a', head: 'none', face: 'glasses' },
  crane: { top: 'suit', color: '#5a5a66', head: 'none' },
  lily: { top: 'dress', color: '#e0443a', head: 'ponytail', headColor: '#1a0e0a', kid: true },
  boy: { top: 'tshirt', color: '#f2c21a', head: 'cap', headColor: '#2a5aa0', kid: true },
  kid: { top: 'tshirt', color: '#3aa876', head: 'cap', headColor: '#1a5a3a', kid: true },
  mom2: { top: 'dress', color: '#3a8ad0', head: 'bun', headColor: '#2a1a1a' },
  producer: { top: 'suit', color: '#8a2a4a', head: 'bun', headColor: '#2a1a1a' },
  pilot: { top: 'jersey', color: '#2a3a6a', head: 'cap', headColor: '#1a1a2a' },
  frank: { top: 'trench', color: '#7a6a4a', head: 'fedora', headColor: '#4a3a2a', face: 'glasses' },
  victoria: { top: 'suit', color: '#e8e4ec', head: 'bun', headColor: '#e8d070' },
  investor: { top: 'suit', color: '#2a4a3a', head: 'none' },
  crowd1: { top: 'tshirt', color: '#9a5ad6', head: 'beanie', headColor: '#4a2a6a' },
  crowd2: { top: 'jersey', color: '#d98a3a', head: 'cap', headColor: '#6a3a10' },
};
// Scale: Rio is 1.75 m = 234 pose units, so 1 m = 134 units (= 214 px at s = 1.6). All items below follow that.
export const PX_PER_M = 214;
const EXTRA_POSES = {
  brush: (p) => ({ ...POSES.stand, eF: [28, -150], hF: [27 + 3 * Math.sin(p * 70), -193] }),   // brush head at the mouth
  sip: () => ({ ...POSES.stand, head: [2, -207], eF: [30, -156], hF: [25, -192] }),            // cup rim at the lips
  pour: () => ({ ...POSES.stand, eF: [24, -142], hF: [30, -172], eB: [32, -140], hB: [62, -153] }), // carafe in front hand, mug in back hand right under the spout
  holdCup: () => ({ ...POSES.relaxed, eF: [18, -134], hF: [32, -146] }),
  knob: () => ({ ...POSES.stand, eF: [18, -134], hF: [32, -146], eB: [30, -150], hB: [58, -134] }),  // back hand on the knob (1 m), front hand keeps the cup
  chest: () => ({ ...POSES.sad, eF: [22, -140], hF: [10, -156], eB: [16, -138], hB: [8, -150] }),
  push: () => ({ ...POSES.reach, eF: [30, -160], hF: [58, -170], eB: [28, -150], hB: [56, -158] }),
  cpr: (p) => { const b = 6 * Math.max(0, Math.sin(p * 120)); return { ...POSES.kneel, head: [34, -132 + b], sh: [26, -100 + b], eF: [36, -62 + b * 0.6], hF: [44, -24], eB: [33, -62 + b * 0.6], hB: [42, -24] }; },   // straight arms, hands on the chest of someone lying on the floor
  phoneEar: () => ({ ...POSES.stand, eF: [24, -160], hF: [18, -196] }),
  flySup: () => ({ ...POSES.dive }),
  flyUp: () => ({ ...POSES.stand, eF: [20, -200], hF: [24, -240], eB: [-14, -200], hB: [-18, -238], kF: [8, -52], fF: [6, -4], kB: [-4, -48], fB: [-10, -6] }),
  carry: () => ({ ...POSES.holdFront, eF: [26, -140], hF: [42, -124], eB: [22, -142], hB: [38, -126] }),
  hug: () => ({ ...POSES.stand, eF: [30, -150], hF: [42, -160], eB: [26, -150], hB: [40, -162] }),
  sitTable: () => ({ ...POSES.sit, eF: [24, -120], hF: [44, -118], eB: [18, -120], hB: [38, -116] }),
  eat: (p) => ({ ...POSES.sit, eF: [24, -128], hF: [18 + 4 * Math.sin(p * 40), -172 + 6 * Math.sin(p * 40)] }),
  type: (p) => ({ ...POSES.sit, eF: [26, -118], hF: [46, -122 + 3 * Math.sin(p * 90)], eB: [20, -118], hB: [40, -120 - 3 * Math.sin(p * 90)] }),
  sitPhone: () => ({ ...POSES.sit, eF: [22, -140], hF: [16, -176] }),
  present: () => ({ ...POSES.explain }),
  bow: () => ({ ...POSES.stand, head: [20, -190], sh: [12, -164] }),
  kick2: () => ({ ...POSES.kick }),
  drop: () => ({ ...POSES.shrug, eF: [26, -150], hF: [44, -136], eB: [-20, -150], hB: [-36, -170] }),
};
const poseOf = (name, p) => EXTRA_POSES[name] ? EXTRA_POSES[name](p) : (POSES[name] || POSES.relaxed);

// keyframe helpers ---------------------------------------------------------
function track(keys, p, def) {
  if (keys == null) return def;
  if (!Array.isArray(keys)) return keys;
  if (!Array.isArray(keys[0])) return keys;
  if (p <= keys[0][0]) return keys[0][1];
  for (let i = 1; i < keys.length; i++) {
    const [p1, v1] = keys[i], [p0, v0] = keys[i - 1];
    if (p < p1) { const k = ease.inOut(prog(p, p0, p1)); return typeof v0 === 'number' ? lerp(v0, v1, k) : (k > 0.5 ? v1 : v0); }
  }
  return keys[keys.length - 1][1];
}
const stepVal = (keys, p, def) => { if (!keys) return def; let v = keys[0][1]; for (const [k, x] of keys) if (p >= k) v = x; return v; };
const range = (a, p) => Array.isArray(a) ? lerp(a[0], a[1], ease.inOut(p)) : (a ?? 0);
const pk = (pairs, p) => stepVal(pairs, p, null);

// world objects, real sizes at PX_PER_M (door 2.03 x 0.9 m, bed 2.05 m, desk 0.75 m, counter 0.9 m ...)
const M_ = (m) => m * 214;
function pinkDoor(g, x, y, o, p, t) {
  const w = M_(0.9), h = M_(2.03), open = track(o.open, p, 0), a = track(o.a, p, 1), L = x - w / 2;
  g.save(); g.globalAlpha *= a;
  seg(g, [[L - 12, y], [L - 34, y]], 8, '#c24a86'); seg(g, [[L + w + 12, y], [L + w + 34, y]], 8, '#c24a86');   // little feet: it stands on its own
  if (open > 0) {
    g.save(); g.beginPath(); g.rect(L, y - h, w, h); g.clip();
    const inside = o.inside || 'office';
    if (inside === 'office') { g.fillStyle = linGrad(g, 0, y - h, 0, y, ['#a8c8f0', '#e8f0ff']); g.fillRect(L, y - h, w, h); FX.skyline(g, { x: L, y: y - h * 0.38, w, minH: 40, maxH: h * 0.4, color: '#5a7ab0', windowColor: '#ffe8a0', seed: 3 }); g.fillStyle = '#c8b090'; g.fillRect(L, y - M_(0.75), w, 8); g.fillStyle = '#3a4a6a'; g.fillRect(L, y - M_(0.72), w, M_(0.72)); }
    else if (inside === 'mountain' || inside === 'snow') { g.fillStyle = linGrad(g, 0, y - h, 0, y, ['#7ab0e8', '#e8f2ff']); g.fillRect(L, y - h, w, h); poly(g, [[L - 40, y], [L + w * 0.45, y - h * 0.75], [L + w + 40, y]], '#f4f8ff'); poly(g, [[L + w * 0.3, y - h * 0.5], [L + w * 0.45, y - h * 0.75], [L + w * 0.62, y - h * 0.45]], '#ffffff'); if (inside === 'snow') FX.snow(g, t, { count: 40 }); }
    else if (inside === 'tokyo') { g.fillStyle = '#0a0c1e'; g.fillRect(L, y - h, w, h); FX.skyline(g, { x: L, y: y - 40, w, minH: 80, maxH: h * 0.7, color: '#1a1a34', windowColor: '#ff6a9a', seed: 6 }); }
    else if (inside === 'water') { g.fillStyle = linGrad(g, 0, y - h, 0, y, ['#2a7ac0', '#0a2a5a']); g.fillRect(L, y - h, w, h); for (let k = 0; k < 8; k++) circle(g, L + w * ((k * 37) % 100) / 100, y - ((t * 120 + k * 60) % h), 6, 'rgba(255,255,255,.5)'); }
    else if (inside === 'hospital') { g.fillStyle = linGrad(g, 0, y - h, 0, y, ['#e8f4f8', '#c8dce4']); g.fillRect(L, y - h, w, h); g.fillStyle = '#e04a3a'; g.fillRect(x - 12, y - h * 0.8, 24, 70); g.fillRect(x - 35, y - h * 0.8 + 23, 70, 24); }
    else if (inside === 'roof') { g.fillStyle = linGrad(g, 0, y - h, 0, y, ['#1a2030', '#3a4a5a']); g.fillRect(L, y - h, w, h); FX.rain(g, t, { count: 50, a: 0.7 }); }
    else if (inside === 'sunset') { g.fillStyle = linGrad(g, 0, y - h, 0, y, ['#f2a04a', '#e04a6a', '#3a2a5a']); g.fillRect(L, y - h, w, h); FX.sun(g, x, y - h * 0.3, 40, '#fff0c0', '#ffb070', 3); }
    else if (inside === 'market') { g.fillStyle = linGrad(g, 0, y - h, 0, y, ['#8ac8f0', '#f2e0b0']); g.fillRect(L, y - h, w, h); for (let k = 0; k < 6; k++) circle(g, L + 30 + k * 26, y - 90 - (k % 2) * 14, 12, '#e0443a'); }
    else if (inside === 'apartment') { g.fillStyle = linGrad(g, 0, y - h, 0, y, ['#e8c8a0', '#b88a60']); g.fillRect(L, y - h, w, h); }
    else { g.fillStyle = '#fff6e0'; g.fillRect(L, y - h, w, h); }
    g.restore(); glow(g, x, y - h / 2, h * 0.8, '#fff0d0', 0.3 * open);
  }
  g.lineWidth = 12; g.strokeStyle = '#c24a86'; g.strokeRect(L, y - h, w, h);
  // panel: hinge on the RIGHT, knob on the LEFT (1.0 m high) so a person coming from the left can open it
  const pw = w * (1 - open * 0.9), px = L + w - pw;
  rr(g, px + 6, y - h + 6, Math.max(4, pw - 12), h - 12, 8); g.fillStyle = '#ff7ab8'; g.fill();
  if (pw > 60) { g.strokeStyle = '#e0609e'; g.lineWidth = 4; g.strokeRect(px + 26, y - h + 34, pw - 52, h * 0.36); g.strokeRect(px + 26, y - h * 0.52, pw - 52, h * 0.4); circle(g, px + 22, y - M_(1.0), 8, '#ffd24a'); }
  if (o.label) { const lw = M_(0.62); rr(g, x - lw / 2, y - h - 46, lw, 34, 5); g.fillStyle = '#f2efe8'; g.fill(); text(g, o.label, x, y - h - 29, { size: 19, color: '#2a2230', font: FONTS.ui, weight: 900 }); }
  if (o.sparkle) for (let k = 0; k < 8; k++) { const r2 = rng(k + 7), a2 = (t * 0.8 + r2()) % 1; FX.sparkle(g, L + w * (r2() * 1.6 - 0.3), y - h * r2(), 10 + 10 * Math.sin(a2 * Math.PI), '#fff', a * Math.sin(a2 * Math.PI)); }
  g.restore();
}
function doorKnobX(x) { return x - M_(0.9) / 2 + 22; }   // used when blocking the actor next to the knob
function alarm(g, x, y, o, p, t) {     // nightstand 0.45 x 0.55 m, clock 0.24 m wide
  const ringOn = p >= (o.ring?.[0] ?? 0) && p <= (o.ring?.[1] ?? 1), sh = ringOn ? Math.sin(t * 60) * 2.5 : 0;
  const nw = M_(0.45), nh = M_(0.55); g.fillStyle = '#6a4a3a'; g.fillRect(x - nw / 2, y - nh, nw, nh); g.fillStyle = '#4a3428'; g.fillRect(x - nw / 2 - 4, y - nh - 8, nw + 8, 8);
  const cw = M_(0.24), ch = M_(0.13); g.save(); g.translate(x + sh, y - nh - 8 - ch / 2);
  rr(g, -cw / 2, -ch / 2, cw, ch, 8); g.fillStyle = '#e04a3a'; g.fill(); rr(g, -cw / 2 + 6, -ch / 2 + 5, cw - 12, ch - 10, 4); g.fillStyle = '#1a1622'; g.fill();
  text(g, o.time || '7:00', 0, 1, { size: 21, color: '#ff6a5a', font: FONTS.ui, weight: 900, glow: 8, glowColor: 'rgba(255,90,70,.8)' });
  for (const s of [-1, 1]) circle(g, s * cw * 0.35, -ch / 2 - 4, 6, '#f2c21a');
  g.restore();
  if (ringOn) for (let k = 0; k < 3; k++) { const q = (t * 2 + k / 3) % 1, r = 40 + q * 60; g.strokeStyle = alpha('#ffd24a', 1 - q); g.lineWidth = 4; g.beginPath(); g.arc(x, y - nh - 8 - ch / 2, r, -2.6, -0.5); g.stroke(); }
}
// bed: 2.05 m long, mattress top 0.5 m. x = centre. Pillow at the LEFT end.
function bed(g, x, y) { const w = M_(2.05), L = x - w / 2; g.fillStyle = '#2a2238'; g.fillRect(L, y - M_(0.33), w, M_(0.33)); g.fillRect(L - 10, y - M_(0.85), 20, M_(0.85)); g.fillRect(L + w - 10, y - M_(0.6), 20, M_(0.6)); rr(g, L + 8, y - M_(0.5), w - 16, M_(0.18), 12); g.fillStyle = '#5a62b0'; g.fill(); rr(g, L + 18, y - M_(0.6), M_(0.5), M_(0.12), 12); g.fillStyle = '#e8e4f4'; g.fill(); }
function blanket(g, x, y) { const w = M_(2.05), L = x - w / 2; rr(g, L + M_(0.62), y - M_(0.6), w - M_(0.62) - 4, M_(0.16), 18); g.fillStyle = '#7a84d8'; g.fill(); }
// bathroom sink: vanity top 0.85 m, mirror 0.6 x 0.8 m hung 1.25-2.05 m
function sink(g, x, y) {
  const vw = M_(0.7); rr(g, x - M_(0.3), y - M_(2.05), M_(0.6), M_(0.8), 10); g.fillStyle = '#bfe0f0'; g.fill(); g.strokeStyle = '#e8f4fa'; g.lineWidth = 8; g.stroke();
  poly(g, [[x - M_(0.22), y - M_(1.98)], [x - M_(0.12), y - M_(1.98)], [x - M_(0.24), y - M_(1.35)], [x - M_(0.27), y - M_(1.35)]], 'rgba(255,255,255,.35)');
  g.fillStyle = '#d8dce6'; g.fillRect(x - vw / 2, y - M_(0.82), vw, M_(0.82)); rr(g, x - vw / 2 - 6, y - M_(0.87), vw + 12, M_(0.07), 6); g.fillStyle = '#f2f4f8'; g.fill();
  seg(g, [[x + M_(0.12), y - M_(0.87)], [x + M_(0.12), y - M_(1.0)], [x + M_(0.02), y - M_(1.0)]], 7, '#a8b0c0');
  for (const dx of [-0.17, 0.17]) { g.strokeStyle = '#b8bcc8'; g.lineWidth = 3; g.strokeRect(x + M_(dx) - M_(0.14), y - M_(0.75), M_(0.28), M_(0.62)); }
}
function counter(g, x, y) { FX.counter(g, { x: x - M_(2.1), y, w: M_(4.2), h: M_(0.9), color: '#7a5030', top: '#e8dcc8', doors: 7 }); }
// office desk 1.6 x 0.75 m with a 0.55 m monitor
function desk(g, x, y) {
  const w = M_(1.6); rr(g, x - w / 2, y - M_(0.75), w, 14, 5); g.fillStyle = '#c8b090'; g.fill(); seg(g, [[x - w / 2 + 16, y - M_(0.73)], [x - w / 2 + 16, y]], 8, '#3a3a46'); seg(g, [[x + w / 2 - 16, y - M_(0.73)], [x + w / 2 - 16, y]], 8, '#3a3a46');
  const mw = M_(0.55), mh = M_(0.33); FX.screen(g, { x: x - mw / 2, y: y - M_(0.75) - mh - M_(0.14), w: mw, h: mh, glowC: '#7fd0ff', a: 0.12 }, (g, X, Y, w2) => { for (let i = 0; i < 3; i++) { g.fillStyle = '#7fd0d6'; g.fillRect(X + 10, Y + 12 + i * 18, 40 + (i * 37) % 50, 6); } });
  seg(g, [[x, y - M_(0.75) - M_(0.14)], [x, y - M_(0.75)]], 8, '#2a2a36');
}
function sign(g, x, y, o) { rr(g, x - 90, y - 40, 180, 50, 8); g.fillStyle = o.bg || '#f2efe8'; g.fill(); text(g, o.s, x, y - 14, { size: o.size || 26, color: o.color || '#2a2230', font: FONTS.ui, weight: 900 }); }
// generic illustrated prop placed in the world at real size: { k:'prop', p:'cat', x, up: metres above floor, size: metres }
function propItem(g, x, y, o, p, t) { const a = track(o.a, p, 1); if (a <= 0) return; const X = x + track(o.dx, p, 0) * E.W, up = track(o.upk, p, o.up || 0), r = track(o.rot, p, 0); g.save(); g.translate(X, y - M_(up) - M_(o.size || 0.5) / 2); g.rotate(r); drawProp(g, o.p, 0, 0, M_(o.size || 0.5) / 2, t, { start: 0, disc: !!o.disc, bob: !!o.bob, a }); g.restore(); }
function house(g, x, y, o, p, t) {   // two-storey house 8 m wide, 6 m tall, porch on the left, flat roof part
  const w = M_(8), h = M_(5.2), L = x - w / 2;
  g.fillStyle = o.color || '#e8d8b8'; g.fillRect(L, y - h, w, h); poly(g, [[L - 20, y - h], [x + w * 0.1, y - h - M_(1.6)], [L + w * 0.7, y - h]], '#8a3a2a');
  g.fillStyle = '#6a5a4a'; g.fillRect(L + w * 0.7, y - h - 10, w * 0.3 + 10, 14);   // flat roof above the kitchen
  for (const [wx, wy] of [[0.15, 0.25], [0.45, 0.25], [0.8, 0.25], [0.45, 0.62], [0.8, 0.62]]) { g.fillStyle = o.night ? '#ffd88a' : '#9ac8e8'; g.fillRect(L + w * wx - 50, y - h + h * wy, 100, 110); g.strokeStyle = '#4a3a2a'; g.lineWidth = 6; g.strokeRect(L + w * wx - 50, y - h + h * wy, 100, 110); }
  g.fillStyle = '#5a3a2a'; g.fillRect(L + w * 0.12, y - M_(2.1), M_(0.95), M_(2.1));
  g.fillStyle = '#8a6a4a'; g.fillRect(L - M_(1.4), y - M_(2.6), M_(1.4) + w * 0.3, 14); for (const px of [L - M_(1.3), L - M_(0.2)]) seg(g, [[px, y - M_(2.6)], [px, y]], 10, '#8a6a4a');
  if (o.chime !== false) chime(g, L - M_(0.7), y - M_(2.6) + 14, o, p, t);
}
function chime(g, x, y, o, p, t) {   // six old spoons on fishing line, 40 cm
  seg(g, [[x - 26, y + 6], [x + 26, y + 6]], 4, '#a07a4a'); seg(g, [[x, y], [x, y + 6]], 2, '#ccc');
  for (let k = 0; k < 6; k++) { const sx = x - 22 + k * 9, sw = Math.sin(t * 3 + k) * 0.25 * (o.wind ?? 1); g.save(); g.translate(sx, y + 6); g.rotate(sw); seg(g, [[0, 0], [0, 40 + (k % 3) * 8]], 1.2, '#dcdcdc'); g.fillStyle = '#c8ccd4'; g.beginPath(); g.ellipse(0, 46 + (k % 3) * 8, 4, 8, 0, 0, 7); g.fill(); seg(g, [[0, 54 + (k % 3) * 8], [0, 70 + (k % 3) * 8]], 2.5, '#c8ccd4'); g.restore(); }
}
function water(g, x, y, o, p, t) {   // flood water rising to `level` metres (keyframable)
  const lv = M_(track(o.level, p, 0.3)); g.fillStyle = 'rgba(70,110,140,.78)'; g.fillRect(-E.W, y - lv, E.W * 3, lv + E.H);
  g.strokeStyle = 'rgba(200,230,255,.6)'; g.lineWidth = 4; g.beginPath(); for (let X = -E.W; X < E.W * 2; X += 20) { const yy = y - lv + Math.sin(X * 0.02 + t * 3) * 6; X === -E.W ? g.moveTo(X, yy) : g.lineTo(X, yy); } g.stroke();
}
function car(g, x, y, o, p, t) {   // side view sedan 4.5 m; o.color, o.front (draw only the lower body so seated actors show in windows)
  const w = M_(4.5), L = x - w / 2, c = o.color || '#e0443a', shake = o.drive ? Math.sin(t * 20) * 1.5 : 0;
  g.save(); g.translate(0, shake);
  if (o.part !== 'front') { poly(g, [[L + w * 0.22, y - M_(0.95)], [L + w * 0.32, y - M_(1.42)], [L + w * 0.72, y - M_(1.42)], [L + w * 0.84, y - M_(0.95)]], alpha('#bfe6ff', 0.55)); g.strokeStyle = c; g.lineWidth = 12; g.stroke(); }
  rr(g, L, y - M_(1.0), w, M_(0.62), 26); g.fillStyle = c; g.fill(); g.fillStyle = '#fff6c0'; g.fillRect(L + w - 24, y - M_(0.85), 18, 18);
  for (const wx of [0.2, 0.8]) { const rot = o.drive ? t * 12 : 0; circle(g, L + w * wx, y - M_(0.34), M_(0.34), '#1a1a22'); circle(g, L + w * wx, y - M_(0.34), M_(0.16), '#9aa0ae'); seg(g, [[L + w * wx, y - M_(0.34)], [L + w * wx + Math.cos(rot) * M_(0.15), y - M_(0.34) + Math.sin(rot) * M_(0.15)]], 4, '#555'); }
  g.restore();
}
function booth(g, x, y, o, p, t) {   // red phone booth 1.0 x 2.4 m; o.part = 'back' | 'front'
  const w = M_(1.0), h = M_(2.4), L = x - w / 2;
  if (o.part !== 'front') { g.fillStyle = '#b02a2a'; g.fillRect(L, y - h, w, h); g.fillStyle = 'rgba(200,230,255,.25)'; g.fillRect(L + 14, y - h + 60, w - 28, h - 120); rr(g, L + w - 60, y - M_(1.45), 34, 60, 6); g.fillStyle = '#2a2a30'; g.fill(); if (o.ring && p >= o.ring[0] && p <= o.ring[1]) for (let k = 0; k < 2; k++) { g.strokeStyle = alpha('#ffd24a', 0.8); g.lineWidth = 4; g.beginPath(); g.arc(L + w - 43, y - M_(1.45), 40 + k * 22 + Math.sin(t * 30) * 4, -2.4, -0.7); g.stroke(); } }
  else { g.strokeStyle = '#d0302a'; g.lineWidth = 16; g.strokeRect(L, y - h, w, h); for (let k = 1; k < 5; k++) seg(g, [[L, y - h + k * h / 5], [L + w, y - h + k * h / 5]], 6, '#d0302a'); seg(g, [[x, y - h], [x, y]], 6, '#d0302a'); rr(g, L - 10, y - h - 40, w + 20, 46, 8); g.fillStyle = '#b02a2a'; g.fill(); text(g, 'TELEPHONE', x, y - h - 17, { size: 22, color: '#fff', font: FONTS.ui, weight: 900 }); }
}
function table(g, x, y, o) {   // 1.8 m table, 0.75 m high; o.cloth draws the white magic tablecloth
  const w = M_(o.w || 1.8), L = x - w / 2, top = y - M_(0.75);
  for (const lx of [L + 20, L + w - 20]) seg(g, [[lx, top], [lx, y]], 10, '#5a3a2a');
  if (o.cloth) { poly(g, [[L - 14, top], [L + w + 14, top], [L + w + 26, top + M_(0.35)], [L - 26, top + M_(0.35)]], '#f6f4ee'); for (let k = 0; k < 8; k++) seg(g, [[L + k * w / 7, top + M_(0.33)], [L + k * w / 7 - 4, top + M_(0.36)]], 3, '#dcd8ce'); }
  else { g.fillStyle = '#8a5a3a'; g.fillRect(L, top, w, 14); }
}
// simple real-size foods on a plate (plate 28 cm). kinds: lasagna pancakes taco sushi steak pasta soup mac cocoa spaghetti pho curry cake pizza pepper milk
function food(g, k, x, y) {
  const m = M_;
  if (k === 'lasagna') { for (let i = 0; i < 4; i++) { g.fillStyle = i % 2 ? '#e0443a' : '#f2c060'; g.fillRect(x - m(0.1), y - m(0.02) * (i + 1), m(0.2), m(0.02)); } }
  else if (k === 'pancakes') { for (let i = 0; i < 4; i++) { g.fillStyle = '#d8a050'; g.beginPath(); g.ellipse(x, y - 4 - i * 7, m(0.1), 5, 0, 0, 7); g.fill(); g.strokeStyle = '#5a3010'; g.lineWidth = 2.5; g.stroke(); } circle(g, x, y - 34, 5, '#f2e070'); }
  else if (k === 'taco') { g.fillStyle = '#e8b040'; g.beginPath(); g.arc(x, y - 4, m(0.08), Math.PI, 0); g.fill(); for (const [dx, c] of [[-8, '#3aa876'], [0, '#e0443a'], [8, '#f2e070']]) circle(g, x + dx, y - m(0.07), 6, c); }
  else if (k === 'sushi') { for (const dx of [-24, 0, 24]) { rr(g, x + dx - 10, y - 14, 20, 12, 4); g.fillStyle = '#f4f4f4'; g.fill(); rr(g, x + dx - 11, y - 20, 22, 7, 3); g.fillStyle = '#f08a5a'; g.fill(); } }
  else if (k === 'steak') { g.fillStyle = '#8a3a2a'; g.beginPath(); g.ellipse(x, y - 8, m(0.09), 10, 0, 0, 7); g.fill(); for (let i = -2; i <= 2; i++) seg(g, [[x + i * 10 - 6, y - 14], [x + i * 10 + 6, y - 2]], 2, '#3a1a10'); }
  else if (k === 'pasta' || k === 'spaghetti') { g.fillStyle = '#f2d080'; g.beginPath(); g.ellipse(x, y - 10, m(0.09), 14, 0, Math.PI, 0); g.fill(); if (k === 'spaghetti') for (const dx of [-10, 6, 16]) circle(g, x + dx, y - 16, 6, '#8a3a2a'); else circle(g, x, y - 20, 5, '#2a2a2a'); }
  else if (k === 'soup' || k === 'pho' || k === 'curry' || k === 'mac') { const c = { soup: '#f2b040', pho: '#e8c890', curry: '#d88a20', mac: '#f2c030' }[k]; g.fillStyle = '#f4f0e8'; g.beginPath(); g.arc(x, y - 14, m(0.08), 0, Math.PI); g.fill(); g.fillStyle = c; g.beginPath(); g.ellipse(x, y - 14, m(0.08), 6, 0, 0, 7); g.fill(); if (k === 'pho') seg(g, [[x - 20, y - 40], [x + 6, y - 14]], 3, '#8a5a3a'); }
  else if (k === 'cocoa' || k === 'milk') { rr(g, x - 11, y - 26, 22, 26, 4); g.fillStyle = '#f2efe8'; g.fill(); g.fillStyle = k === 'milk' ? '#ffffff' : '#6a3a20'; g.fillRect(x - 9, y - 22, 18, 6); }
  else drawProp(g, k, x, y - m(0.1), m(0.1), 0, { disc: false, bob: false });
  for (let i = 0; i < 3; i++) { g.strokeStyle = 'rgba(255,255,255,.35)'; g.lineWidth = 3; g.beginPath(); g.moveTo(x - 10 + i * 10, y - 40); g.quadraticCurveTo(x + i * 10, y - 56, x - 10 + i * 10, y - 70); g.stroke(); }
}
function dish(g, x, y, o, p, t) {  // a dish appearing on the table top in a puff at time `at`
  const at = o.at ?? 0, a = clamp((p - at) * 12); if (a <= 0) return; const top = y - M_(0.75);
  if (p - at < 0.12) for (let k = 0; k < 6; k++) FX.sparkle(g, x + Math.cos(k) * 50 * (1 + (p - at) * 8), top - 40 - Math.sin(k) * 30, 14, '#fff', 1 - (p - at) * 8);
  g.save(); g.globalAlpha *= a; g.fillStyle = '#eeeae2'; g.beginPath(); g.ellipse(x, top - 6, M_(0.14), 9, 0, 0, 7); g.fill();
  food(g, o.food || 'pizza', x, top - 8); g.restore();
}
function kite(g, x, y, o, p, t) {   // red kite with a rainbow tail; string goes to (o.hx, o.hy) in screen fractions
  const ky = y - M_(o.up || 6) + Math.sin(t * 1.3) * 20, kx = x + Math.sin(t * 0.9) * 30;
  if (o.hx != null) seg(g, [[kx, ky + 40], [o.hx * E.W, o.hy * E.H]], 1.5, 'rgba(255,255,255,.7)');
  poly(g, [[kx, ky - 50], [kx + 36, ky], [kx, ky + 40], [kx - 36, ky]], '#e0443a'); seg(g, [[kx, ky - 50], [kx, ky + 40]], 2, '#7a1a1a'); seg(g, [[kx - 36, ky], [kx + 36, ky]], 2, '#7a1a1a');
  ['#e0443a', '#f2c21a', '#3aa876', '#3a8ad0', '#9a5ad6'].forEach((c, k) => { const tx = kx - (o.dir || 1) * (20 + k * 26), ty = ky + 40 + k * 14 + Math.sin(t * 4 + k) * 10; poly(g, [[tx - 8, ty], [tx, ty - 8], [tx + 8, ty], [tx, ty + 8]], c); });
}
function float(g, x, y, o, p, t) { const b = Math.sin(t * 2) * 6; g.save(); g.translate(x, y + b); g.fillStyle = '#f2f0f8'; g.beginPath(); g.ellipse(0, 0, M_(0.7), M_(0.16), 0, 0, 7); g.fill(); circle(g, M_(0.55), -M_(0.32), M_(0.14), '#f2f0f8'); seg(g, [[M_(0.5), -M_(0.1)], [M_(0.55), -M_(0.3)]], M_(0.12), '#f2f0f8'); poly(g, [[M_(0.6), -M_(0.44)], [M_(0.66), -M_(0.68)], [M_(0.68), -M_(0.42)]], '#f2c21a'); for (let k = 0; k < 4; k++) circle(g, M_(0.42) - k * 14, -M_(0.36) + k * 6, 8, ['#e06aa0', '#9a5ad6', '#3a8ad0', '#3aa876'][k]); g.restore(); }
function sea(g, x, y, o, p, t) {   // dark sea surface covering the lower screen at `level` px above floor line
  const top = y - (o.level ?? 80); g.fillStyle = linGrad(g, 0, top, 0, E.H, [o.night ? '#1a2a4a' : '#2a6aa0', o.night ? '#05101e' : '#0a3a60']); g.fillRect(-E.W, top, E.W * 3, E.H * 2);
  for (let k = 0; k < 4; k++) { g.strokeStyle = alpha('#cfe8ff', 0.35 - k * 0.07); g.lineWidth = 3; g.beginPath(); for (let X = -E.W; X < E.W * 2; X += 24) { const yy = top + 10 + k * 40 + Math.sin(X * 0.015 + t * 2 + k) * 6; X === -E.W ? g.moveTo(X, yy) : g.lineTo(X, yy); } g.stroke(); }
  if (o.rip) for (let k = 0; k < 4; k++) { const q = (t * 0.6 + k / 4) % 1, ax = o.rip * E.W, ay = top + 260 - q * 220; seg(g, [[ax, ay + 40], [ax, ay], [ax - 14, ay + 16]], 5, alpha('#ff8a6a', 1 - q)); seg(g, [[ax, ay], [ax + 14, ay + 16]], 5, alpha('#ff8a6a', 1 - q)); }
}
function robot(g, x, y, o, p, t) {  // Mini: a 25 cm blue robot (our own design: round head, antenna, one bell)
  const s = M_(o.size || 0.3) / 100, hop = o.hop ? Math.abs(Math.sin(t * 8)) * 12 : 0, wave = o.wave ? Math.sin(t * 10) * 0.6 : 0;
  g.save(); g.translate(x, y - M_(o.up || 0) - hop); g.scale(s, s);
  rr(g, -26, -60, 52, 50, 14); g.fillStyle = '#3a8ae0'; g.fill(); seg(g, [[-12, -10], [-14, 0]], 10, '#2a5aa0'); seg(g, [[12, -10], [14, 0]], 10, '#2a5aa0');
  g.save(); g.translate(26, -48); g.rotate(-0.4 + wave); seg(g, [[0, 0], [16, -18]], 8, '#3a8ae0'); g.restore(); seg(g, [[-26, -48], [-40, -30]], 8, '#3a8ae0');
  circle(g, 0, -86, 34, '#3a8ae0'); circle(g, 0, -80, 26, '#f4f4f8'); circle(g, -10, -88, 7, '#1a1a22'); circle(g, 10, -88, 7, '#1a1a22'); g.strokeStyle = '#1a1a22'; g.lineWidth = 3; g.beginPath(); g.arc(0, -76, 8, 0.3, Math.PI - 0.3); g.stroke();
  seg(g, [[0, -120], [0, -136]], 3, '#555'); circle(g, 0, -140, 6, o.alert ? (Math.sin(t * 20) > 0 ? '#ff3a3a' : '#7a1a1a') : '#ffd24a'); circle(g, 0, -56, 6, '#f2c21a');
  g.restore();
  if (o.say) { const bx = x + 30, by = y - M_(o.up || 0) - hop - M_(0.35) - 70, w = Math.max(160, o.say.length * 17 + 30); rr(g, bx, by, w, 54, 12); g.fillStyle = '#fff'; g.fill(); poly(g, [[bx + 14, by + 54], [bx + 34, by + 54], [bx + 6, by + 78]], '#fff'); text(g, o.say, bx + w / 2, by + 28, { size: 26, color: '#1a1a22', font: FONTS.ui, weight: 900 }); }
}
function glassWall(g, x, y) { g.fillStyle = 'rgba(180,220,255,.18)'; g.fillRect(x - 6, y - M_(2.8), 12, M_(2.8)); seg(g, [[x, y - M_(2.8)], [x, y]], 3, 'rgba(220,240,255,.6)'); }
function stage(g, x, y, o, p, t) { const w = M_(o.w || 8); g.fillStyle = '#2a1a3a'; g.fillRect(x - w / 2, y - M_(0.9), w, M_(0.9)); g.fillStyle = '#4a2a5a'; g.fillRect(x - w / 2, y - M_(0.9) - 10, w, 12); FX.lightCone(g, x, y - M_(6), { angle: Math.PI / 2, spread: 0.18, len: M_(6), color: '#fff3d0', a: 0.18 }); }
function fridge(g, x, y) { rr(g, x - M_(0.35), y - M_(1.8), M_(0.7), M_(1.8), 10); g.fillStyle = '#e8ecf0'; g.fill(); seg(g, [[x - M_(0.3), y - M_(1.15)], [x + M_(0.3), y - M_(1.15)]], 3, '#b8bcc8'); seg(g, [[x + M_(0.22), y - M_(1.5)], [x + M_(0.22), y - M_(1.3)]], 6, '#9aa0ae'); }
function paper(g, x, y, o) { const up = M_(o.up || 1.4); rr(g, x - 50, y - up - 70, 100, 70, 4); g.fillStyle = '#f2ecd8'; g.fill(); if (o.s) text(g, o.s, x, y - up - 35, { size: 16, color: '#3a2a1a', font: FONTS.ui, weight: 900 }); }
function jet(g, x, y, o, p, t) { const a = track(o.a, p, 1); if (a <= 0) return; g.save(); g.globalAlpha *= a; for (let k = 0; k < 30; k++) { const q = (t * 3 + k / 30) % 1; circle(g, x - q * M_(1.2) * (o.dir || 1), y - M_(o.up || 1.5) + Math.sin(k * 7) * 10 + q * q * 40, 10 - q * 6, 'rgba(120,190,255,.8)'); } g.restore(); }
function puddle(g, x, y) { g.fillStyle = 'rgba(120,180,230,.55)'; g.beginPath(); g.ellipse(x, y + 4, M_(0.7), 14, 0, 0, 7); g.fill(); }
function stall(g, x, y) { const w = M_(2.4); g.fillStyle = '#8a5a3a'; g.fillRect(x - w / 2, y - M_(0.9), w, M_(0.9)); for (let k = 0; k < 6; k++) poly(g, [[x - w / 2 + k * w / 6, y - M_(2.4)], [x - w / 2 + (k + 1) * w / 6, y - M_(2.4)], [x - w / 2 + (k + 0.5) * w / 6, y - M_(2.1)]], k % 2 ? '#f2efe8' : '#3aa876'); g.fillStyle = '#3aa876'; g.fillRect(x - w / 2, y - M_(2.6), w, M_(0.2)); seg(g, [[x - w / 2 + 8, y - M_(2.4)], [x - w / 2 + 8, y - M_(0.9)]], 6, '#5a3a2a'); seg(g, [[x + w / 2 - 8, y - M_(2.4)], [x + w / 2 - 8, y - M_(0.9)]], 6, '#5a3a2a'); for (let k = 0; k < 16; k++) circle(g, x - w / 2 + 30 + (k % 8) * (w - 60) / 7, y - M_(0.95) - Math.floor(k / 8) * 22, 11, k % 3 ? '#e0443a' : '#f2a03a'); }
function shopFront(g, x, y, o) { const w = M_(4); g.fillStyle = o.color || '#3a2a3a'; g.fillRect(x - w / 2, y - M_(3.4), w, M_(3.4)); g.fillStyle = o.lit ? '#ffd88a' : '#1a1622'; g.fillRect(x - w / 2 + 30, y - M_(2.6), w - 60, M_(1.6)); rr(g, x - w * 0.35, y - M_(3.3), w * 0.7, M_(0.5), 8); g.fillStyle = '#e04a3a'; g.fill(); text(g, o.s || 'RAMEN', x, y - M_(3.05), { size: 40, color: '#fff', font: FONTS.ui, weight: 900 }); if (o.closed) { rr(g, x - 80, y - M_(1.9), 160, 50, 6); g.fillStyle = '#f2efe8'; g.fill(); text(g, 'CLOSED', x, y - M_(1.9) + 25, { size: 26, color: '#c0302a', font: FONTS.ui, weight: 900 }); } }
function stairs(g, x, y) { for (let k = 0; k < 8; k++) { g.fillStyle = k % 2 ? '#8a6a5a' : '#7a5a4a'; g.fillRect(x + k * M_(0.28), y - (k + 1) * M_(0.18), M_(2.4) - k * M_(0.28), M_(0.18)); } seg(g, [[x, y - M_(0.9)], [x + 8 * M_(0.28), y - M_(0.9) - 8 * M_(0.18)]], 6, '#3a2a2a'); }
function ship(g, x, y, o, p, t) { const w = M_(o.len || 20) * (o.sc || 0.25), b = Math.sin(t) * 4; g.save(); g.translate(x, y + b); poly(g, [[-w / 2, -w * 0.08], [w / 2, -w * 0.08], [w * 0.42, w * 0.06], [-w * 0.45, w * 0.06]], '#3a4a6a'); for (let k = 0; k < 7; k++) { g.fillStyle = ['#e0443a', '#3aa876', '#f2c21a', '#3a8ad0'][k % 4]; g.fillRect(-w * 0.4 + k * w * 0.1, -w * 0.18, w * 0.09, w * 0.1); } g.fillStyle = '#f2efe8'; g.fillRect(w * 0.3, -w * 0.28, w * 0.12, w * 0.2); g.restore(); }
function cards(g, x, y) { for (let k = 0; k < 5; k++) { g.save(); g.translate(x - 60 + k * 30, y - M_(0.78)); g.rotate((k - 2) * 0.15); rr(g, -14, -22, 28, 40, 4); g.fillStyle = '#f4f4f8'; g.fill(); circle(g, 0, -2, 6, k % 2 ? '#e0443a' : '#1a1a22'); g.restore(); } }
function fence(g, x, y, o, p, t) {   // garden fence 1 m high with a gate that can swing (o.open keyframes)
  for (let X = x - M_(3); X < x + M_(3); X += 34) if (Math.abs(X - x) > M_(0.5)) { g.fillStyle = '#f2ece0'; g.fillRect(X, y - M_(1.0), 18, M_(1.0)); poly(g, [[X, y - M_(1.0)], [X + 9, y - M_(1.08)], [X + 18, y - M_(1.0)]], '#f2ece0'); }
  seg(g, [[x - M_(3), y - M_(0.7)], [x + M_(3), y - M_(0.7)]], 6, '#e0d8c8'); const op = track(o.open, p, 0); g.save(); g.translate(x - M_(0.5), 0); g.scale(1 - op * 0.8, 1); for (let k = 0; k < 5; k++) { g.fillStyle = '#d8ccb8'; g.fillRect(k * M_(0.2) + 4, y - M_(1.0), 16, M_(1.0)); } seg(g, [[0, y - M_(0.7)], [M_(1.0), y - M_(0.7)]], 6, '#c8bca8'); g.restore();
  for (let k = 0; k < 5; k++) { const tx = x + M_(1.2) + k * 60; seg(g, [[tx, y], [tx, y - 60]], 3, '#3a7a3a'); circle(g, tx, y - 66, 10, '#e0443a'); }
}
function bankDesk(g, x, y) { FX.counter(g, { x: x - M_(1.2), y, w: M_(2.4), h: M_(1.1), color: '#4a5a6a', top: '#c8d0d8', doors: 3 }); rr(g, x - 90, y - M_(2.6), 180, 50, 8); g.fillStyle = '#2a4a7a'; g.fill(); text(g, 'BANK', x, y - M_(2.6) + 25, { size: 30, color: '#fff', font: FONTS.ui, weight: 900 }); }
const ITEMS = { fence, bank: bankDesk, jet, puddle, stall, shop: shopFront, stairs, ship, cards, door: pinkDoor, alarm, bed, blanket, sink, counter, desk, sign, prop: propItem, house, chime, water, car, booth, table, dish, kite, float, sea, robot, glass: glassWall, stage, fridge, paper };

// held objects, drawn in pose units (1 m = 134) right at the hand --------------------
function heldItem(g, k, h, p, o = {}) {
  const [x, y] = h; g.save(); g.translate(x, y);
  if (k === 'toothbrush') {      // 19 cm, bristles pointing back at the mouth
    seg(g, [[2, 2], [-12, -5]], 2.4, '#3aa8f0'); rr(g, -16, -8, 6, 4, 1.5); g.fillStyle = '#f4f4f4'; g.fill();
    for (let i = 0; i < 4; i++) circle(g, -15 + Math.sin(p * 50 + i * 2) * 4, -9 - i * 2.5, 1.6 + (i % 2) * 0.8, 'rgba(255,255,255,.9)');
  } else if (k === 'cup' || k === 'mug') {   // 8 x 9.5 cm
    const tilt = o.tilt || 0; g.rotate(tilt);
    rr(g, -6, -13, 11, 13, 2); g.fillStyle = '#f2efe8'; g.fill(); ring(g, 6.5, -7, 3, 1.6, '#f2efe8');
    const f = o.fill ?? 0.8; if (f > 0) { g.fillStyle = '#5a3420'; g.fillRect(-5, -1 - 11 * f, 9, 11 * f); }
  } else if (k === 'carafe') {   // 15 x 20 cm, tilted so the spout points down-forward
    g.rotate(0.9); rr(g, -4, -26, 18, 24, 4); g.fillStyle = '#2a2a36'; g.fill(); rr(g, -2, -14, 14, 11, 3); g.fillStyle = '#5a3420'; g.fill(); poly(g, [[14, -26], [20, -28], [14, -21]], '#2a2a36');
  } else if (k === 'bagel') { circle(g, 6, -4, 7, '#d8a060'); circle(g, 6, -4, 2.4, 'rgba(20,14,20,.9)'); }
  else if (k === 'tomato') { circle(g, 6, -6, 6, '#e0443a'); seg(g, [[6, -12], [8, -15]], 1.5, '#3aa876'); circle(g, 14, -2, 5.5, '#e0443a'); }
  else if (k === 'chime') { seg(g, [[-10, 0], [10, 0]], 2, '#a07a4a'); for (let i = 0; i < 6; i++) { const sw = Math.sin(p * 30 + i) * 0.3; g.save(); g.translate(-9 + i * 3.6, 0); g.rotate(sw); seg(g, [[0, 0], [0, 14 + (i % 3) * 3]], 0.6, '#ddd'); g.fillStyle = '#c8ccd4'; g.beginPath(); g.ellipse(0, 17 + (i % 3) * 3, 1.6, 3, 0, 0, 7); g.fill(); g.restore(); } }
  else if (k === 'hammer') { seg(g, [[0, 0], [10, -22]], 2.4, '#8a5a3a'); rr(g, 4, -28, 14, 7, 1.5); g.fillStyle = '#6a6a72'; g.fill(); }
  else if (k === 'note') { rr(g, 0, -12, 12, 12, 1); g.fillStyle = '#f2e04a'; g.fill(); }
  else if (k === 'towel') { rr(g, -4, -20, 20, 30, 3); g.fillStyle = '#e8d8c0'; g.fill(); }
  else if (k === 'fork') { seg(g, [[0, 0], [8, -16]], 1.6, '#c8ccd4'); }
  else if (k === 'shovel') { seg(g, [[0, 20], [0, -30]], 2.4, '#8a5a3a'); rr(g, -6, 20, 12, 14, 2); g.fillStyle = '#6a6a72'; g.fill(); }
  else if (k === 'pepper') { g.fillStyle = '#e0302a'; g.beginPath(); g.ellipse(6, -4, 6, 3, 0.3, 0, 7); g.fill(); }
  else if (k === 'suitcase') { rr(g, -6, 2, 26, 30, 3); g.fillStyle = '#3a4a6a'; g.fill(); seg(g, [[2, 2], [2, -2], [12, -2], [12, 2]], 1.6, '#2a2a30'); }
  else if (k === 'phone') { rr(g, 0, -12, 7, 13, 1.5); g.fillStyle = '#22222e'; g.fill(); g.fillStyle = '#6fc3ff'; g.fillRect(1, -11, 5, 10); }
  g.restore();
}
function drawHeld(g, a, pz, p) {
  g.save(); g.translate(a.X, a.Y); g.scale(a.facing * a.s, a.s);
  const hd = a.hold, on = hd && p >= (hd.from ?? 0) && p <= (hd.to ?? 1);
  if (on) {
    if (hd.k === 'pour') {   // carafe in the front hand, mug in the back hand, stream between them
      const fill = clamp(prog(p, hd.fill?.[0] ?? 0.15, hd.fill?.[1] ?? 0.85));
      heldItem(g, 'mug', [pz.hB[0] + 2, pz.hB[1] + 4], p, { fill });
      heldItem(g, 'carafe', pz.hF, p);
      const sx = pz.hF[0] + 34, sy = pz.hF[1] - 2;          // spout tip after the 0.9 rad tilt
      if (fill < 1) seg(g, [[sx, sy], [sx, pz.hB[1] - 9]], 1.8, '#6a3a20');
    } else if (hd.k === 'cup' && hd.sip) heldItem(g, 'cup', [pz.hF[0] - 6, pz.hF[1] + 2], p, { tilt: -0.55 });
    else heldItem(g, hd.k, pz.hF, p);
  }
  g.restore();
}
// dropped objects fall from the hand to the floor with gravity and a small bounce
function dropFall(g, a, pz, p, info) {
  const hd = a.hold; if (!hd || hd.drop == null || p < hd.drop) return;
  const t = (p - hd.drop) * info.dur, x0 = a.X + (pz.hF[0] + 6) * a.facing * a.s, y0 = a.Y + (pz.hF[1] - 4) * a.s;
  const g0 = 9.8 * PX_PER_M, fallT = Math.sqrt(2 * (a.Y - 12 - y0) / g0);
  let y, rot = t * 9 * a.facing; const x = x0 + a.facing * 60 * Math.min(t, fallT + 0.6);
  if (t < fallT) y = y0 + 0.5 * g0 * t * t; else { const tb = t - fallT, v = g0 * fallT * 0.3; y = a.Y - 12 - Math.max(0, v * tb - 0.5 * g0 * tb * tb); }
  g.save(); g.translate(x, y); g.rotate(rot); circle(g, 0, 0, 7 * a.s, '#d8a060'); circle(g, 0, 0, 2.4 * a.s, 'rgba(20,14,20,.9)'); g.restore();
}

// scenery --------------------------------------------------------------------
function room(g, cam, M, wall, wall2, o = {}) {
  layer(g, cam, 0.4, (g) => {
    g.fillStyle = linGrad(g, 0, -E.H, 0, GY(), [wall2, wall]); g.fillRect(-E.W, -E.H, E.W * 3, GY() + E.H);
    if (o.tiles) for (let y = GY() - 520; y < GY() - 120; y += 46) for (let x = -E.W; x < E.W * 2; x += 46) { g.strokeStyle = 'rgba(255,255,255,.18)'; g.lineWidth = 2; g.strokeRect(x, y, 46, 46); }
    if (o.window) FX.windowFrame(g, { x: o.window, y: GY() - 640, w: 340, h: 280, cols: 2, frame: shade(wall, -0.5), bar: 10 }, (g, x, y, w, h) => { g.fillStyle = linGrad(g, 0, y, 0, y + h, mood(o.sky || 'dusk').sky); g.fillRect(x, y, w, h); if (o.night) FX.moon(g, x + w * 0.7, y + 70, 26); else FX.sun(g, x + w * 0.75, y + 80, 30, '#fff6e0', '#ffd59a', 3); });
    if (o.frames) for (let k = 0; k < 3; k++) { rr(g, o.frames + k * 120, GY() - 560 + (k % 2) * 26, 92, 74, 6); g.fillStyle = shade(wall, -0.45); g.fill(); rr(g, o.frames + k * 120 + 8, GY() - 552 + (k % 2) * 26, 76, 58, 4); g.fillStyle = ['#e08a5a', '#7ab0e0', '#9ad07a'][k]; g.fill(); }
  });
  layer(g, cam, 0.95, (g) => { g.fillStyle = linGrad(g, 0, GY(), 0, GY() + 400, [shade(M.floor || '#6a4a3a', 0.05), shade(M.dark || '#2a1a1a', -0.2)]); g.fillRect(-E.W, GY(), E.W * 3, E.H * 2); FX.floorLines(g, GY(), GY() + 600, 'rgba(0,0,0,.2)', 0.07); });
}
function mapCard(g, p, t, o) {
  backdrop(g, ['#0e2a4a', '#1a4a6a', '#2a6a8a']);
  g.save(); g.globalAlpha = 0.35; for (let x = 0; x < E.W; x += 80) seg(g, [[x, 0], [x, E.H]], 1, '#9ad0f0'); for (let y = 0; y < E.H; y += 80) seg(g, [[0, y], [E.W, y]], 1, '#9ad0f0'); g.restore();
  // stylised land mass
  g.fillStyle = '#3a8a5a'; g.beginPath(); g.moveTo(420, 260); g.bezierCurveTo(800, 180, 1300, 200, 1560, 300); g.bezierCurveTo(1620, 520, 1500, 700, 1330, 760); g.bezierCurveTo(1300, 900, 1270, 960, 1230, 940); g.bezierCurveTo(1200, 860, 1150, 800, 1000, 800); g.bezierCurveTo(800, 820, 600, 760, 480, 640); g.bezierCurveTo(380, 520, 360, 360, 420, 260); g.fill();
  const A = [1250, 900], B = [1130, 380], k = ease.inOut(prog(p, 0.15, 0.75));
  g.setLineDash([18, 14]); seg(g, [A, [lerp(A[0], B[0], k), lerp(A[1], B[1], k)]], 6, '#ffd24a'); g.setLineDash([]);
  const pin = (x, y, label, a, col) => { if (a <= 0) return; g.save(); g.globalAlpha *= a; circle(g, x, y - 34, 22, col); circle(g, x, y - 34, 8, '#fff'); poly(g, [[x - 18, y - 24], [x + 18, y - 24], [x, y]], col); text(g, label, x + 120, y - 34, { size: 46, color: '#fff', font: FONTS.ui, weight: 900, stroke: 6, strokeColor: 'rgba(0,0,0,.5)' }); g.restore(); };
  pin(A[0], A[1], 'MIAMI', ease.out(prog(p, 0.0, 0.15)), '#ff5a6a');
  pin(B[0], B[1], 'CHICAGO', ease.out(prog(p, 0.7, 0.85)), '#5ab0ff');
  // tiny pink door hopping along the route
  const dx = lerp(A[0], B[0], k), dy = lerp(A[1], B[1], k);
  rr(g, dx - 16, dy - 64, 32, 56, 4); g.fillStyle = '#ff7ab8'; g.fill();
}

function town(g, t, cam, d) {   // small-town street: day (default) / dusk / night
  const m = d.smood || 'day', M = mood(m), Y = GY();
  layer(g, cam, 0.1, (g) => { backdrop(g, m === 'night' ? ['#0b1028', '#1d2550', '#3a3570'] : m === 'dusk' ? ['#3d3360', '#e8956b', '#f7cf98'] : ['#6aa8e8', '#a8d0f0', '#e8f2fa']); if (m === 'night') { FX.stars(g, 0, { count: 80, area: [-E.W, -E.H, E.W * 3, Y] }); FX.moon(g, E.W * 0.8, Y - 700, 40); } else FX.sun(g, E.W * 0.8, Y - 680, 56, '#fffbe8', '#fff3dc', 3); });
  layer(g, cam, 0.3, (g) => { FX.hills(g, { y: Y - 120, amp: 90, color: m === 'night' ? '#1a2a3a' : '#7ab07a', seed: 3 }); for (let k = -6; k < 16; k++) FX.tree(g, k * 260 + 60, Y - 60, 1.2, m === 'night' ? '#0e1a14' : '#3a7a4a'); });
  layer(g, cam, 0.92, (g) => { g.fillStyle = m === 'night' ? '#1a1c28' : '#6a6a72'; g.fillRect(-E.W, Y, E.W * 3, E.H * 2); g.fillStyle = m === 'night' ? '#2a2a32' : '#9a9aa2'; g.fillRect(-E.W, Y, E.W * 3, 26); for (let x = -E.W; x < E.W * 2; x += 220) { g.fillStyle = 'rgba(242,230,200,.45)'; g.fillRect(x, Y + 150, 110, 8); } });
  return { GY: Y, M };
}
function roofSet(g, t, cam, d) {   // night, rain, on top of a flat roof, flood water all around
  const Y = GY();
  layer(g, cam, 0.1, (g) => { backdrop(g, ['#0a0e1a', '#1a2234', '#2a3446']); });
  layer(g, cam, 0.35, (g) => { for (let k = -4; k < 12; k++) { const x = k * 300, h = 140 + (k * 37) % 120; g.fillStyle = '#141a26'; g.fillRect(x, Y - 120 - h, 180, h); poly(g, [[x - 20, Y - 120 - h], [x + 90, Y - 190 - h], [x + 200, Y - 120 - h]], '#141a26'); } g.fillStyle = 'rgba(40,70,100,.9)'; g.fillRect(-E.W, Y - 130, E.W * 3, 200); });
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, Y, 0, Y + 300, ['#4a4a52', '#2a2a30']); g.fillRect(-E.W, Y, E.W * 3, E.H * 2); for (let y = Y + 30; y < E.H + 200; y += 34) seg(g, [[-E.W, y], [E.W * 2, y]], 2, 'rgba(0,0,0,.35)'); g.fillStyle = 'rgba(160,190,220,.25)'; g.fillRect(-E.W, Y, E.W * 3, 6); });
  return { GY: Y, M: mood('storm') };
}

// main ------------------------------------------------------------------------
export function directed(g, t, info) {
  const d = info.dir || {}, p = info.p, cam = { z: range(d.cam?.z ?? 1, p), x: range(d.cam?.x ?? 0, p), y: range(d.cam?.y ?? 0, p) };
  const M = mood(d.mood || 'interiorWarm'), Y = GY();
  // keep flying actors in frame: follow the highest one unless the board fixes the camera height
  if (d.follow !== false && !(d.cam && d.cam.y != null)) { let mu = 0; for (const a of (d.actors || [])) mu = Math.max(mu, track(a.up, p, 0)); if (mu > 1.3) { cam.y = -M_(mu - 0.9) * 0.6; cam.z = Math.min(cam.z, 0.8); } }
  if (d.set === 'map') { mapCard(g, p, t, d); return; }
  if (d.set === 'face') {
    const st = drawSet(d.bg || 'home', g, t * 0.3, { z: 1.5, x: 0, y: -E.H * 0.1 });
    g.fillStyle = 'rgba(16,10,20,.45)'; g.fillRect(0, 0, E.W, E.H);
    bigFace(g, E.W * 0.42, E.H * 0.58, 290, { outfit: OUTFITS[d.who || 'rio'], expr: pk(d.expr, p) || 'smile', blink: (t % 2.7) > 2.6, rimColor: '#ffc68a', look: [0.3, -0.1] });
    if (d.name) { const a = ease.outBack(prog(p, 0.2, 0.45)); g.save(); g.translate(E.W * 0.74, E.H * 0.42); g.scale(a, a); rr(g, -190, -70, 380, 140, 24); g.fillStyle = '#f2c21a'; g.fill(); text(g, d.name, 0, 4, { size: 96, color: '#1a1222', font: FONTS.title, weight: 700 }); g.restore(); }
    return;
  }
  if (d.set === 'room') room(g, cam, M, d.wall || '#c8a888', d.wall2 || '#8a6a5a', d.room || {});
  else if (d.set === 'night') { room(g, cam, mood('night'), '#2a2c50', '#141830', { window: E.W * 0.62, night: true, sky: 'night', ...(d.room || {}) }); }
  else if (d.set === 'bathroom') room(g, cam, M, '#9ac8d8', '#5a8aa0', { tiles: true });
  else if (d.set === 'town') town(g, t, cam, d);
  else if (d.set === 'roof') roofSet(g, t, cam, d);
  else drawSet(d.set || 'home', g, t, cam, { mood: d.smood });
  // items behind actors
  layer(g, cam, 1, (g) => {
    for (const it of (d.items || [])) if (!it.front) ITEMS[it.k]?.(g, it.x * E.W, it.y ? it.y * E.H : Y, it, p, t);
    for (const a of (d.actors || [])) {
      const of = OUTFITS[a.who || a.id] || a.outfit || OUTFITS.rio, s = a.s || 1.6;
      // position = storyboard keys + optional walk-in / walk-out + pacing (small walks back and forth)
      const xAt = (pp) => {
        let x = track(a.x, pp, 0.5);
        if (a.enter) { const u = a.enterUntil ?? 0.22; if (pp < u) { const from = a.enter === 'left' ? -0.08 : 1.08; x = lerp(from, track(a.x, u, 0.5), ease.inOut(pp / u)); } }
        if (a.exit) { const u0 = a.exitFrom ?? 0.8; if (pp > u0) { const to = a.exit === 'left' ? -0.08 : 1.08; x = lerp(track(a.x, u0, 0.5), to, ease.inOut((pp - u0) / (1 - u0))); } }
        if (a.pace) { const T = a.paceT || 4.2, u = (((pp * info.dur + (a.seed || 0) * 1.3) % T) + T) % T / T; const k = u < 0.28 ? ease.inOut(u / 0.28) : u < 0.5 ? 1 : u < 0.78 ? 1 - ease.inOut((u - 0.5) / 0.28) : 0; x += a.pace * k; }
        return x;
      };
      const xf = xAt(p), xPrev = xAt(Math.max(0, p - 0.008)), moving = Math.abs(xf - xPrev) > 0.0003;
      const facing = moving && !a.lockFacing ? Math.sign(xf - xPrev) : a.facing != null ? (Array.isArray(a.facing) ? stepVal(a.facing, p, 1) : a.facing) : 1;
      const up = track(a.up, p, 0), fly = up > 0.05 || a.fly;
      const X = xf * E.W, Yy = Y + (a.dy || 0) + track(a.yk, p, 0) * E.H - M_(up) + (fly ? Math.sin(t * 2.4 + (a.seed || 0)) * 6 : 0);
      const bounce = (!moving && !fly && /^(cheer|jump)$/.test(stepVal(a.pose, p, ''))) ? Math.abs(Math.sin(t * 6 + (a.seed || 0))) * 16 : 0;
      let pz = moving ? walkPose(info.globalT * 9, {}) : poseOf(stepVal(a.pose, p, 'relaxed'), p);
      if (moving && a.hold && a.hold.k !== 'pour') { const hc = EXTRA_POSES.holdCup(), dx = pz.sh[0] - hc.sh[0], dy = pz.sh[1] - hc.sh[1]; pz = { ...pz, eF: [hc.eF[0] + dx, hc.eF[1] + dy], hF: [hc.hF[0] + dx, hc.hF[1] + dy] }; }
      // talking people gesture: cycle through natural talk poses while their line plays
      const pn0 = stepVal(a.pose, p, 'relaxed'), talkNow = a.talk && p >= a.talk[0] && p <= a.talk[1];
      if (!moving && talkNow && ['talk', 'explain', 'relaxed', 'point', 'shrug', 'stand', 'crossArms'].includes(pn0)) { const G = ['talk', 'explain', 'talk', 'point', 'shrug'], q = info.globalT * 0.8 + (a.seed || 0), i = Math.floor(q) % G.length, f = q - Math.floor(q); pz = blendPose(G[i], G[(i + 1) % G.length], clamp((f - 0.75) * 4)); }
      if (!moving) pz = breathe(pz, t);
      const al = track(a.alpha, p, 1);
      if (al <= 0) continue;
      const expr = stepVal(a.expr, p, 'neutral');
      const talking = a.talk && p >= a.talk[0] && p <= a.talk[1];
      if (a.shadowAt != null && fly) { g.fillStyle = 'rgba(0,0,0,.18)'; g.beginPath(); g.ellipse(X, Y, 30 * s, 5 * s, 0, 0, 7); g.fill(); }
      if (a.trail) FX.speedLines(g, t, { cx: X, cy: Yy - 120, count: 14, a: 0.12, inner: 120 });
      const pn = stepVal(a.pose, p, 'relaxed');
      if (!moving && !fly && a.chair !== false && a.clip == null && /^(sit|sitTable|eat|type|sitPhone|sitBack)$/.test(pn)) FX.chair(g, X - facing * 6 * s, Y, s * 0.62, '#3a2a2a');   // something to sit on
      if (a.clip != null) { g.save(); g.beginPath(); g.rect(-E.W, -E.H * 2, E.W * 3, Y - M_(a.clip) + E.H * 2); g.clip(); }   // e.g. seated in a car: hide legs below the door line
      drawFigure(g, { x: X, y: Yy - bounce, s, facing, outfit: of, pose: pz, expr, rot: track(a.rot, p, 0) || 0, shadow: !fly, alpha: al, talk: talking ? 0.5 + 0.5 * Math.sin(t * 22) : 0, look: [facing * 0.6, 0], rim: { color: M.rim || '#ffc68a', dir: [0, -1], w: 4 } });
      if (a.clip != null) g.restore();
      const A = { X, Y: Yy, s, facing, hold: a.hold };
      if (!(a.hold?.drop != null && p >= a.hold.drop)) drawHeld(g, A, pz, p); else dropFall(g, A, pz, p, info);
      if (a.hat === 'copter') { const hx = X + pz.head[0] * facing * s, hy = Yy + (pz.head[1] - 30) * s; seg(g, [[hx, hy + 8 * s], [hx, hy]], 3 * s, '#c8a010'); const k = Math.cos(t * 40); seg(g, [[hx - 34 * s * k, hy], [hx + 34 * s * k, hy]], 5 * s, '#f2c21a'); circle(g, hx, hy, 4 * s, '#c8a010'); }
      if (a.zzz) for (let k = 0; k < 3; k++) { const q = (t * 0.6 + k / 3) % 1; text(g, 'z', X + 60 + q * 60, Yy - 260 - q * 120, { size: 30 + k * 10, color: alpha('#e8ecff', 1 - q), font: FONTS.title, weight: 700 }); }
    }
    for (const it of (d.items || [])) if (it.front) ITEMS[it.k]?.(g, it.x * E.W, it.y ? it.y * E.H : Y, it, p, t);
    for (const it of (d.extra || [])) ITEMS[it.k]?.(g, it.x * E.W, it.y ? it.y * E.H : Y, it, p, t);
  });
  for (const tx of (d.text || [])) { const a = ease.outBack(prog(p, tx.at ?? 0.1, (tx.at ?? 0.1) + 0.15)); if (a <= 0) continue; g.save(); g.translate(tx.x * E.W, tx.y * E.H); g.scale(a, a); text(g, tx.s, 0, 0, { size: tx.size || 70, color: tx.color || S().ui.gold, font: FONTS.title, weight: 700, stroke: 10, strokeColor: 'rgba(0,0,0,.55)' }); g.restore(); }
  for (const pr of (d.props || [])) drawProp(g, pr.k, pr.x * E.W, pr.y * E.H, pr.r || 70, t, { start: (pr.at || 0) * info.dur, disc: pr.disc ?? false });
  const fx = [].concat(d.fx || []);
  if (fx.includes('rain')) FX.rain(g, t, { count: 260, a: 0.5 });
  if (fx.includes('snow')) FX.snow(g, t, { count: 220 });
  if (fx.includes('greensky')) { g.fillStyle = 'rgba(60,200,90,.38)'; g.fillRect(0, 0, E.W, E.H * 0.55); }
  if (fx.includes('drought')) { g.fillStyle = 'rgba(170,110,40,.35)'; g.fillRect(0, 0, E.W, E.H); }
  if (fx.includes('night')) { g.fillStyle = 'rgba(10,14,40,.38)'; g.fillRect(0, 0, E.W, E.H); }
  if (fx.includes('dark')) { g.fillStyle = 'rgba(0,0,0,.32)'; g.fillRect(0, 0, E.W, E.H); }
  if (fx.includes('flash')) { const a = clamp(1 - p * 6); g.fillStyle = `rgba(255,255,255,${a})`; g.fillRect(0, 0, E.W, E.H); }
  if (fx.includes('speed')) FX.speedLines(g, t, { count: 30, a: 0.12, inner: 420 });
  if (fx.includes('shake')) { /* handled by cam */ }
  if (d.inset) {   // phone call / video call bubble: the other person's face in a circle, top corner
    const ins = d.inset, a = ease.outBack(prog(p, ins.at ?? 0.05, (ins.at ?? 0.05) + 0.12)); if (a > 0) {
      const cx = E.W * (ins.x ?? 0.8), cy = E.H * (ins.y ?? 0.27), r = 150; g.save(); g.translate(cx, cy); g.scale(a, a);
      circle(g, 0, 0, r + 10, '#f2efe8'); g.save(); g.beginPath(); g.arc(0, 0, r, 0, 7); g.clip(); g.fillStyle = linGrad(g, 0, -r, 0, r, ins.bg || ['#6a5a8a', '#2a2238']); g.fillRect(-r, -r, 2 * r, 2 * r);
      if (ins.rain) FX.rain(g, t, { count: 60, a: 0.6 });
      bigFace(g, 0, 30, 92, { outfit: OUTFITS[ins.who] || OUTFITS.rio, expr: stepVal(ins.expr, p, 'neutral'), talk: ins.talk ? 0.5 + 0.5 * Math.sin(t * 22) : 0, blink: (t % 3) > 2.9, look: [-0.4, 0] }); g.restore();
      if (ins.label) text(g, ins.label, 0, r + 44, { size: 34, color: '#fff', font: FONTS.ui, weight: 900, stroke: 6, strokeColor: 'rgba(0,0,0,.6)' });
      if (ins.icon) drawProp(g, ins.icon, -r * 0.75, -r * 0.75, 34, t, { disc: true });
      g.restore(); }
  }
  if (d.thought) { const th = d.thought, a = ease.outBack(prog(p, th.at ?? 0.1, (th.at ?? 0.1) + 0.12)); if (a > 0) { const cx = E.W * (th.x ?? 0.3), cy = E.H * (th.y ?? 0.25); g.save(); g.translate(cx, cy); g.scale(a, a); for (const [dx, dy, r] of [[-130, 120, 14], [-100, 90, 22]]) circle(g, dx, dy, r, '#f4efe6'); g.fillStyle = '#f4efe6'; g.beginPath(); g.ellipse(0, 0, 220, 130, 0, 0, 7); g.fill(); if (th.s) text(g, th.s, 0, 70, { size: 34, color: '#2a2230', font: FONTS.ui, weight: 900 }); (th.props || []).forEach((k, i, arr) => drawProp(g, k, (i - (arr.length - 1) / 2) * 140, 0, 54, t, { disc: false })); if (th.cross) { seg(g, [[-160, -90], [160, 90]], 14, '#e0443a'); } g.restore(); } }
  if (d.card) {   // fact card: a big number / short label over a dimmed frame, used for real figures in the narration
    const c = d.card, a = ease.outBack(prog(p, c.at ?? 0.15, (c.at ?? 0.15) + 0.15)); if (a > 0) { g.save(); g.translate(E.W * (c.x ?? 0.5), E.H * (c.y ?? 0.22)); g.scale(a, a); const w = c.w || 560; rr(g, -w / 2, -90, w, 180, 26); g.fillStyle = 'rgba(16,12,24,.82)'; g.fill(); g.strokeStyle = S().ui.gold; g.lineWidth = 4; g.stroke(); text(g, c.big, 0, -18, { size: c.size || 88, color: S().ui.gold, font: FONTS.ui, weight: 900 }); if (c.small) text(g, c.small, 0, 52, { size: 32, color: '#f2ecdf', font: FONTS.ui, weight: 800 }); g.restore(); } }
}
