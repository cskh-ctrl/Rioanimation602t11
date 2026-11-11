// auto.js — registers every shot in story/shots.json with an automatic template chosen by pipeline/build.py.
// Templates: act, focus, props, think, duo, face, number, science, compare, question, title, end (hero = act).
import { radGrad, E, V, S, registerShot, mood, layer, blurLayer, veil, backdrop, ease, prog, clamp, lerp, key, talkAmount, seg, circle, ring, rr, poly, glow, alpha, shade, mix, text, measure, FONTS, rng } from '/engine/core.js';
import { drawFigure, POSES, posesAt, breathe, walkPose, bigFace } from '/engine/rig2d.js';
import * as FX from '/engine/fx2d.js';
import * as UI from '/engine/ui2d.js';
import { drawSet, SETS } from './sets.js';
import { drawProp, hasProp, sparkle as spk } from './props.js';
import { directed } from './directed.js';

export const RIO = { top: 'hoodie', color: '#2d7fe0', head: 'curly', headColor: '#0e0b12' };
const PALETTE = ['#e0532f', '#f2c21a', '#3aa876', '#9a5ad6', '#e06aa0', '#d98a3a'];
function outfitFor(name, role, k) {
  const color = PALETTE[k % PALETTE.length];
  if (role === 'doctor') return { top: 'labcoat', face: 'glasses', head: 'none' };
  if (role === 'kid') return { top: 'tshirt', color, head: k % 2 ? 'ponytail' : 'cap', headColor: shade(color, -0.3), kid: true };
  if (role === 'elder') return { top: 'suit', color: '#6a5a4a', head: 'fedora', headColor: '#4a3a2a', face: 'glasses' };
  if (role === 'boss') return { top: 'suit', color: '#2a2a3a', head: k % 2 ? 'bun' : 'none' };
  return { top: ['tshirt', 'jersey', 'tracksuit', 'dress'][k % 4], color, head: ['cap', 'ponytail', 'beanie', 'bun'][k % 4], headColor: shade(color, -0.35) };
}
let CASTMAP = null;
function castOf(name) {
  if (!CASTMAP) { CASTMAP = {}; (E.cfg.cast || []).forEach((c, k) => { CASTMAP[c.name] = outfitFor(c.name, c.role, k); }); }
  return CASTMAP[name] || outfitFor(name || 'x', 'friend', 1);
}
const allCast = () => [RIO, ...(E.cfg.cast || []).map(c => castOf(c.name))].slice(0, 5);

// deterministic per-shot camera
function camFor(info, kind = 'mid') {
  const r = rng(info.seed || 1), m = Math.floor(r() * 7), p = ease.inOut(info.p), d = V(1, 0.8);
  const base = kind === 'wide' ? 1.0 : kind === 'close' ? 1.38 : 1.14;
  const cam = [
    { z: base + 0.12 * p, x: 0, y: 0 },                                  // slow push in
    { z: base + 0.04, x: lerp(-90, 90, p) * d, y: 0 },                   // pan right
    { z: base + 0.16 - 0.14 * p, x: 0, y: -14 * p },                     // pull out
    { z: base + 0.05 * p, x: lerp(70, -70, p) * d, y: 0 },              // pan left
    { z: base + 0.08, x: 0, y: lerp(-50, 30, p), r: 0 },                 // tilt down
    { z: base + 0.1 * p, x: lerp(-40, 40, p) * d, y: 0, r: -0.035 },     // dutch angle drift
    { z: base + 0.02 + 0.2 * ease.out(prog(info.p, 0, 0.25)), x: 0, y: 0 }, // quick punch in
  ][m];
  if (kind === 'close') cam.y = (cam.y || 0) - E.H * V(0.16, 0.12);
  return cam;
}
function rimOf(M) { return { color: M.rim, dir: [0, -1], w: 4 }; }
function rioPose(info, t) {
  const p = info.pose;
  if (p === 'run' || p === 'walk') return null;
  const target = POSES[p] || [POSES.relaxed, POSES.talk, POSES.explain, POSES.crossArms, POSES.think][(info.seed || 0) % 5];
  return breathe(posesAt(t, [[0, POSES.relaxed], [0.25, target]]), t);
}
function wrap(g, str, size, maxW, font = FONTS.title, weight = 700) {
  const words = str.split(/\s+/), lines = []; let cur = '';
  for (const w of words) { const nx = cur ? cur + ' ' + w : w; if (measure(g, nx, size, font, weight) > maxW && cur) { lines.push(cur); cur = w; } else cur = nx; }
  if (cur) lines.push(cur); return lines;
}
function blockText(g, str, cx, cy, o = {}) {
  const { size = V(68, 76), maxW = E.W * 0.82, color = S().ui.cream, font = FONTS.title, weight = 700, a = 1, maxLines = 3, italic = false } = o;
  let sz = size, lines = wrap(g, str, sz, maxW, font, weight);
  while (lines.length > maxLines && sz > 30) { sz *= 0.88; lines = wrap(g, str, sz, maxW, font, weight); }
  const lh = sz * 1.18, y0 = cy - (lines.length - 1) * lh / 2;
  lines.forEach((ln, i) => text(g, ln, cx, y0 + i * lh, { size: sz, color, font, weight, alpha: a, italic, stroke: sz * 0.12, strokeColor: 'rgba(0,0,0,.55)', glow: 16, glowColor: 'rgba(0,0,0,.6)' }));
}
const showText = () => !E.cfg.captions;   // long videos: short on-screen text; shorts already have captions

// ---------- templates ----------
function duo(g, t, info) {
  const cam = camFor(info, 'mid');
  const st = drawSet(info.loc, g, t, cam); const { GY, M } = st;
  const s = V(1.6, 1.75), gap = V(230, 200), fr = castOf(info.friend);
  const friendTalks = info.speaker === 'friend';
  const tk = talkAmount(info.globalT);
  layer(g, cam, 1, (g) => {
    drawFigure(g, { x: E.W / 2 - gap, y: GY, s, facing: 1, outfit: RIO, pose: breathe(friendTalks ? POSES.relaxed : posesAt(t, [[0, POSES.relaxed], [0.3, POSES.talk]]), t), expr: friendTalks ? (info.expr === 'neutral' ? 'surprised' : 'smile') : info.expr, rim: rimOf(M), look: [1, 0] });
    drawFigure(g, { x: E.W / 2 + gap, y: GY, s, facing: -1, outfit: fr, pose: breathe(friendTalks ? posesAt(t, [[0, POSES.relaxed], [0.25, [POSES.talk, POSES.explain, POSES.point, POSES.shrug][info.seed % 4]]]) : POSES.crossArms, t, 1, 2), expr: friendTalks ? info.expr : 'neutral', talk: friendTalks ? tk : 0, rim: rimOf(M), look: [-1, 0] });
  });
  st.fx?.(g, t);
  if (friendTalks && info.friend && showText()) text(g, info.friend.toUpperCase(), E.W / 2 + gap, GY - 300 * s * 0.85, { size: V(30, 40), color: S().ui.gold, font: FONTS.ui, weight: 900, alpha: ease.out(prog(t, 0.1, 0.4)) * 0.85 });
}

function face(g, t, info) {
  const M = mood('dusk');
  blurLayer(g, 14, (g) => drawSet(info.loc, g, t * 0.3, { z: 1.5, x: (info.seed % 2 ? 1 : -1) * 120, y: -E.H * 0.1 }));
  veil(g, '#100a14', 0.3);
  const friend = info.speaker === 'friend' && info.friend;
  const r = V(280, 300) * (1 + 0.04 * t / Math.max(1, info.dur));
  const cx = E.W / 2 + V(friend ? 140 : -140, 0), cy = E.H * V(0.6, 0.5);
  bigFace(g, cx, cy, r, { outfit: friend ? castOf(info.friend) : RIO, expr: info.expr === 'neutral' ? ['surprised', 'smirk', 'determined', 'thinking'][info.seed % 4] : info.expr, talk: friend ? talkAmount(info.globalT) : 0, blink: (t % 2.7) > 2.6, rimColor: M.rim, rimSide: friend ? 1 : -1, look: [friend ? -0.4 : 0.4, -0.1] });
  if (info.expr === 'shocked' || info.expr === 'scared') FX.rings(g, cx, cy, t, { count: 3, r0: r * 1.1, r1: r * 1.7, color: '#fff3e0', a: 0.3 });
  if (showText() && info.text && info.text.split(' ').length <= 7) blockText(g, info.text.toUpperCase(), E.W / 2, E.H * 0.16, { size: 64, a: ease.out(prog(t, 0.05, 0.35)) });
}

function parseNum(s) { const v = parseFloat(String(s).replace(/,/g, '')); return isNaN(v) ? null : v; }
function number(g, t, info) {
  blurLayer(g, 12, (g) => drawSet(info.loc, g, t * 0.3, { z: 1.3, x: 0, y: 0 }));
  veil(g, '#08060e', 0.55);
  const ui = S().ui, v = parseNum(info.num), p = ease.out(prog(t, 0.1, Math.min(1.4, info.dur * 0.5)));
  let str = info.num;
  if (v != null) { const dec = (String(info.num).split('.')[1] || '').length; const cur = v * p; str = dec ? cur.toFixed(dec) : Math.round(cur).toLocaleString('en-US'); }
  const unit = info.unit === '%' ? '%' : '';
  const sc = 1 + 0.06 * ease.outBack(prog(t, 0, 0.4));
  g.save(); g.translate(E.W / 2, E.H * V(0.42, 0.4)); g.scale(sc, sc);
  const size = Math.min(V(240, 230), (E.W * 0.85) / Math.max(1, measure(g, str + unit, 100) / 100));
  text(g, str + unit, 0, 0, { size, color: ui.gold, font: FONTS.ui, weight: 900, glow: 40, glowColor: alpha(ui.gold, 0.6) });
  if (info.unit && info.unit !== '%') text(g, info.unit, 0, size * 0.75, { size: V(64, 70), color: ui.cream, font: FONTS.ui, weight: 900, spacing: 4, alpha: ease.out(prog(t, 0.5, 0.9)) });
  g.restore();
  FX.rings(g, E.W / 2, E.H * V(0.42, 0.4), t, { count: 3, r0: 200, r1: 700, speed: 0.5, color: ui.gold, a: 0.12 });
  const M = mood('dusk');
  drawFigure(g, { x: E.W * V(0.15, 0.8), y: E.H * V(0.95, 0.72), s: V(1.2, 1.3), facing: 1, outfit: RIO, pose: breathe(POSES.pointUp, t), expr: 'awe', rim: rimOf(M), look: [0.6, -1] });
}

function icon(g, kind, x, y, r, t, col) {
  g.save(); g.strokeStyle = col; g.lineWidth = r * 0.06; g.lineCap = 'round'; g.lineJoin = 'round';
  const L = (pts) => { g.beginPath(); pts.forEach(([a, b], i) => i ? g.lineTo(x + a * r, y + b * r) : g.moveTo(x + a * r, y + b * r)); g.stroke(); };
  if (kind === 'eye') { g.beginPath(); g.moveTo(x - r, y); g.quadraticCurveTo(x, y - r * 0.9, x + r, y); g.quadraticCurveTo(x, y + r * 0.9, x - r, y); g.stroke(); ring(g, x, y, r * 0.36, r * 0.06, col); circle(g, x, y, r * 0.16, col); }
  else if (kind === 'brain') { for (const [dx, dy, rr2] of [[-0.35, -0.2, 0.45], [0.3, -0.25, 0.5], [-0.1, 0.25, 0.45], [0.4, 0.2, 0.38]]) { g.beginPath(); g.arc(x + dx * r, y + dy * r, rr2 * r, 0, 7); g.stroke(); } L([[0, -0.7], [0, 0.65]]); }
  else if (kind === 'heart') { const b = 1 + 0.08 * Math.max(0, Math.sin(t * 7)); g.beginPath(); g.moveTo(x, y + 0.75 * r * b); g.bezierCurveTo(x - 1.2 * r * b, y - 0.1 * r, x - 0.6 * r * b, y - 1.0 * r * b, x, y - 0.4 * r); g.bezierCurveTo(x + 0.6 * r * b, y - 1.0 * r * b, x + 1.2 * r * b, y - 0.1 * r, x, y + 0.75 * r * b); g.stroke(); L([[-1.4, 0.1], [-0.5, 0.1], [-0.3, -0.3], [-0.1, 0.4], [0.1, 0.1], [1.4, 0.1]]); }
  else if (kind === 'ear') { g.beginPath(); g.arc(x, y - 0.1 * r, 0.6 * r, Math.PI * 0.9, Math.PI * 2.3); g.quadraticCurveTo(x + 0.2 * r, y + 0.8 * r, x - 0.2 * r, y + 0.8 * r); g.stroke(); for (let k = 1; k <= 3; k++) { g.beginPath(); g.arc(x + 0.5 * r, y, r * (0.4 + k * 0.3), -0.5, 0.5); g.stroke(); } }
  else if (kind === 'lungs') { for (const s of [-1, 1]) { g.beginPath(); g.ellipse(x + s * 0.42 * r, y + 0.1 * r, 0.32 * r, 0.62 * r * (1 + 0.05 * Math.sin(t * 2)), s * 0.15, 0, 7); g.stroke(); } L([[0, -0.9], [0, -0.3], [-0.3, -0.1]]); L([[0, -0.3], [0.3, -0.1]]); }
  else if (kind === 'cell') { ring(g, x, y, r * 0.8, r * 0.06, col); circle(g, x + 0.15 * r, y - 0.1 * r, r * 0.25, alpha(col, 0.5)); for (let k = 0; k < 6; k++) circle(g, x + Math.cos(k + t) * r * 0.5, y + Math.sin(k * 1.7 + t) * r * 0.45, r * 0.06, col); }
  else if (kind === 'bone') { L([[-0.6, 0.6], [0.6, -0.6]]); for (const [a, b] of [[-0.7, 0.5], [-0.5, 0.7], [0.7, -0.5], [0.5, -0.7]]) ring(g, x + a * r, y + b * r, r * 0.16, r * 0.06, col); }
  else if (kind === 'bolt') L([[0.1, -1], [-0.4, 0.1], [0.05, 0.1], [-0.1, 1], [0.45, -0.15], [0, -0.15], [0.1, -1]]);
  else if (kind === 'moon') { g.beginPath(); g.arc(x, y, r * 0.8, 0.6, Math.PI * 2 - 0.6 + 0.6); g.stroke(); circle(g, x + r * 0.35, y - r * 0.25, r * 0.6, S().ui.bpBg); text(g, 'z', x + r * 0.8, y - r * 0.8, { size: r * 0.5, color: col }); }
  else if (kind === 'clock') { ring(g, x, y, r * 0.85, r * 0.06, col); for (let k = 0; k < 12; k++) { const a = k / 12 * Math.PI * 2; seg(g, [[x + Math.cos(a) * r * 0.7, y + Math.sin(a) * r * 0.7], [x + Math.cos(a) * r * 0.8, y + Math.sin(a) * r * 0.8]], r * 0.04, col); } seg(g, [[x, y], [x + Math.cos(t * 3 - 1.57) * r * 0.65, y + Math.sin(t * 3 - 1.57) * r * 0.65]], r * 0.05, col); seg(g, [[x, y], [x + Math.cos(t * 0.3) * r * 0.4, y + Math.sin(t * 0.3) * r * 0.4]], r * 0.07, col); }
  else if (kind === 'therm') { rr(g, x - 0.15 * r, y - 0.9 * r, 0.3 * r, 1.4 * r, 0.15 * r); g.stroke(); circle(g, x, y + 0.65 * r, 0.3 * r, col); seg(g, [[x, y + 0.5 * r], [x, y - (0.2 + 0.4 * Math.sin(t)) * r]], r * 0.12, col); }
  else { ring(g, x, y, r * 0.15, r * 0.08, col); for (let k = 0; k < 3; k++) { g.save(); g.translate(x, y); g.rotate(k * Math.PI / 3 + t * 0.6); g.beginPath(); g.ellipse(0, 0, r, r * 0.35, 0, 0, 7); g.stroke(); g.restore(); } }
  g.restore();
}
function science(g, t, info) {
  UI.blueprint(g); const ui = S().ui, col = UI.bpStroke();
  const cam = { z: 1 + 0.05 * ease.inOut(info.p) };
  layer(g, cam, 1, (g) => {
    const ix = E.W * V(0.36, 0.5), iy = E.H * V(0.48, 0.3), r = V(230, 250) * ease.outBack(prog(t, 0, 0.5));
    glow(g, ix, iy, r * 2.2, col, 0.15);
    icon(g, info.icon, ix, iy, r, t, col);
    ring(g, ix, iy, r * 1.35, 2, alpha(col, 0.35));
    const lx = E.W * V(0.66, 0.5), ly = E.H * V(0.42, 0.5);
    const room = E.vertical ? E.W - 120 : E.W - (ix + r * 1.4) - 80, fsz = Math.min(V(96, 96), V(96, 96) * room / Math.max(1, measure(g, info.sci || '', V(96, 96), FONTS.ui, 900) + 12 * (info.sci || '').length)); const lxx = E.vertical ? lx : Math.max(lx, ix + r * 1.4 + 40 + room / 2 - 40);
    text(g, info.sci || '', lxx, ly, { size: fsz, color: ui.gold, font: FONTS.ui, weight: 900, spacing: 6, glow: 24, glowColor: alpha(ui.gold, 0.5), alpha: ease.out(prog(t, 0.3, 0.7)) });
    UI.callout(g, t, { at: [ix + r * 0.6, iy - r * 0.6], to: [lxx - V(160, 0), ly - V(60, 120)], str: '', start: 0.4 });
    UI.lineFigure(g, { x: E.W * V(0.66, 0.82), y: E.H * V(0.82, 0.72), s: V(1.1, 0.9), pose: [POSES.think, POSES.point, POSES.explain][info.seed % 3], color: alpha('#e8f0ff', 0.9) });
    if (info.numAny) text(g, info.numAny[0] + (info.numAny[1] === '%' ? '%' : ' ' + (info.numAny[1] || '')), lx, ly + V(110, 110), { size: V(56, 60), color: ui.cream, font: FONTS.ui, weight: 900, alpha: ease.out(prog(t, 0.6, 1.0)) });
  });
}

function compare(g, t, info) {
  UI.blueprint(g); const ui = S().ui, col = UI.bpStroke();
  const x0 = V(560, 140), x1 = E.W - V(220, 120), rows = [E.H * V(0.38, 0.4), E.H * V(0.64, 0.6)];
  const row = (y, label, val, frac, c, pose, k) => {
    if (!E.vertical) UI.lineFigure(g, { x: 300, y: y + 110, s: 1.0, pose, color: alpha(c, 0.9) });
    text(g, label, x0, y - 62, { size: V(42, 46), color: c, font: FONTS.ui, weight: 900, align: 'left', spacing: 2 });
    rr(g, x0, y - 26, x1 - x0, 52, 26); g.fillStyle = alpha(c, 0.12); g.fill();
    const w = Math.max(52, (x1 - x0) * frac); rr(g, x0, y - 26, w, 52, 26); g.fillStyle = c; g.fill(); glow(g, x0 + w, y, 60, c, 0.5);
    if (val) text(g, val, Math.min(x0 + w + 24, x1 - 200), y + 66, { size: V(48, 52), color: c, font: FONTS.ui, weight: 900, align: 'left', alpha: clamp(frac * 4) });
  };
  row(rows[0], 'AVERAGE PERSON', info.avg || '', 0.3 * ease.inOut(prog(t, 0.2, 1.2)), col, POSES.stand);
  row(rows[1], 'YOU (RIO)', info.you || '', 0.95 * ease.out(prog(t, 0.8, 1.8)), ui.gold, POSES.cheer);
}

function question(g, t, info) {
  blurLayer(g, 12, (g) => drawSet(info.loc, g, t * 0.3, { z: 1.25, x: -60, y: 0 }));
  veil(g, '#0a0812', 0.45);
  const M = mood('dusk');
  drawRio(g, info, { x: E.W * V(0.82, 0.5), y: E.H * V(0.95, 0.74), s: V(1.4, 1.9), facing: -1, outfit: RIO, pose: breathe(POSES.think, t), expr: 'thinking', rim: rimOf(M), t });
  const qp = (info.props || []).filter(p => hasProp(p.k))[0]; if (qp && E.cfg.captions) drawProp(g, qp.k, E.W * V(0.3, 0.72), E.H * V(0.4, 0.45), V(110, 110), t, { start: 0.3 });
  if (!E.cfg.captions) blockText(g, info.text, E.W * V(0.44, 0.5), E.H * V(0.45, 0.32), { size: V(76, 80), maxW: E.W * V(0.7, 0.85), font: FONTS.serif, weight: 900, italic: true, color: S().ui.cream, a: ease.out(prog(t, 0.05, 0.4)) });
  else { text(g, '?', E.W / 2, E.H * 0.26, { size: 360, color: S().ui.gold, font: FONTS.serif, weight: 900, italic: true, glow: 40, glowColor: alpha(S().ui.gold, 0.5), alpha: ease.out(prog(t, 0, 0.3)) }); }
}

function title(g, t, info) {
  const M = mood('dusk'), cam = { z: 1.06 - 0.06 * ease.inOut(info.p), y: -14 * t };
  layer(g, cam, 0.2, (g) => { backdrop(g, M.sky); FX.sun(g, E.W / 2, E.H * V(0.62, 0.55), V(90, 110), '#fff3dc', M.key, 5); FX.godRays(g, E.W / 2, E.H * V(0.62, 0.55), { count: 14, angle: -Math.PI / 2, spread: Math.PI * 1.6, len: 1800, a: 0.06, t }); });
  layer(g, cam, 0.5, (g) => FX.skyline(g, { x: -200, y: E.H * V(0.74, 0.66), w: E.W + 400, maxH: V(300, 500), color: '#2a1f36', windowColor: alpha(M.practical, 0.8), seed: 21 }));
  layer(g, cam, 0.8, (g) => { g.fillStyle = '#16111e'; g.fillRect(-E.W, E.H * V(0.74, 0.66), E.W * 3, E.H); });
  drawFigure(g, { x: E.W / 2, y: E.H * V(0.74, 0.66), s: V(1.0, 1.4), facing: 1, outfit: RIO, pose: breathe(POSES.pointUp, t), expr: 'awe', rim: rimOf(M) });
  FX.dust(g, t, { count: 30, color: '#ffd9b0', a: 0.4 });
  const tt = (info.title || '').replace(/\?$/, '');
  const m = tt.match(/^(What If)\s+(.*)$/i);
  const rest = m ? m[2] : tt;
  const words = rest.split(' '); const half = Math.ceil(words.length / 2);
  const lines = (E.vertical || rest.length > 22) ? [m ? 'WHAT IF' : '', words.slice(0, half).join(' ').toUpperCase(), words.slice(half).join(' ').toUpperCase() + '?'].filter(Boolean) : [m ? 'WHAT IF' : '', rest.toUpperCase() + '?'].filter(Boolean);
  UI.titleCard(g, t, { lines, dur: info.dur + 0.6, y: E.H * V(0.32, 0.3) });
}

function end(g, t, info) {
  UI.endScreen(g, t, { question: E.vertical ? 'Follow for more!' : 'What would YOU do?', cast: allCast() });
  text(g, 'RIO ANIMATION', E.W / 2, E.H * V(0.5, 0.42), { size: V(72, 80), color: S().ui.gold, font: FONTS.title, weight: 700, spacing: 4, glow: 24, glowColor: 'rgba(255,140,60,.7)', alpha: ease.out(prog(t, 0.3, 0.8)) });
  text(g, 'Subscribe for more fascinating videos', E.W / 2, E.H * V(0.58, 0.48), { size: V(40, 44), color: S().ui.cream, font: FONTS.ui, weight: 800, alpha: ease.out(prog(t, 0.5, 1.0)) });
}


// =====================================================================================
// Bo 2 upgrade: illustrated action shots. Rio acts out the verb of the sentence, the
// nouns of the sentence pop in as animated props exactly when they are spoken, and the
// video's superpower is visible on Rio whenever it is in use.
// =====================================================================================
const sinT = Math.sin, cosT = Math.cos;
function propStart(info, pr) { const s = pr.at - (info.t0 || 0); return s < 0 ? -2 : s; }
const HOLD = { eat: ['burger', 'pizza', 'apple', 'cake'], drink: ['coffee', 'water', 'bottle', 'glass'], phone: ['phone'], read: ['book', 'newspaper', 'letter'], write: ['contract', 'pencil', 'letter'], type: ['laptop'], lift: ['dumbbell', 'gift', 'bag', 'money'], throw: ['ball', 'soccer'], sing: ['mic'] };
const DEF_HOLD = { eat: 'burger', drink: 'coffee', phone: 'phone', read: 'book', write: 'contract', type: 'laptop', lift: 'dumbbell', throw: 'ball', sing: 'mic' };

function powerMods(info, o) {
  const pw = info.powerOn ? info.power : null;
  if (pw === 'invisible') o.alpha = 0.18 + 0.12 * Math.abs(sinT(info.globalT * 3));
  if (pw === 'shrink') o.s *= 0.38;
  if (pw === 'giant') o.s *= 1.9;
  if (pw === 'reflex' || pw === 'future') o.trail = { count: 4, dx: pw === 'future' ? 70 : -60, a: 0.3 };
  if (pw === 'face') { const cols = ['#e0443a', '#f2c21a', '#5ab04a', '#9a5ad6']; o.outfit = { ...o.outfit, head: ['curly', 'cap', 'ponytail', 'beanie'][Math.floor(info.globalT * 1.5) % 4], headColor: cols[Math.floor(info.globalT * 1.5) % 4] }; }
  return o;
}
function powerFx(g, info, x, y, s, t, under) {
  const pw = info.powerOn ? info.power : null; if (!pw) return;
  const hy = y - 208 * s, cy = y - 140 * s, gt = info.globalT;
  if (under) {
    if (pw === 'glow') { glow(g, x, cy, 420 * s, '#9ff0ff', 0.55 + 0.2 * sinT(t * 4)); glow(g, x, cy, 200 * s, '#ffffff', 0.4); }
    if (pw === 'armor') glow(g, x, cy, 260 * s, '#c8d8ff', 0.3);
    if (pw === 'teleport') FX.rings(g, x, y - 100 * s, t, { count: 4, r0: 40 * s, r1: 260 * s, color: '#b8a0ff', a: 0.5, w: 4 });
    if (pw === 'water') { for (let k = 0; k < 3; k++) { const ph = (t * 0.8 + k / 3) % 1; g.save(); g.globalAlpha *= 1 - ph; g.strokeStyle = '#bfefff'; g.lineWidth = 4; g.beginPath(); g.ellipse(x, y + 4, 60 * s + ph * 200 * s, 10 * s + ph * 30 * s, 0, 0, Math.PI * 2); g.stroke(); g.restore(); } }
    if (pw === 'swap') FX.rings(g, x, cy, t, { count: 3, r0: 60 * s, r1: 300 * s, color: '#ff9af0', a: 0.4, w: 5 });
    if (pw === 'fly' || pw === 'jumpbig') { for (let k = 0; k < 6; k++) { const ph = (t * 1.5 + k / 6) % 1; seg(g, [[x - 120 * s + k * 45 * s, y + 20 + ph * 140], [x - 120 * s + k * 45 * s, y + 60 + ph * 140]], 4, alpha('#ffffff', 0.5 * (1 - ph))); } }
    if (pw === 'invisible') { g.save(); g.globalAlpha *= 0.6; for (let k = 0; k < 10; k++) { const a = k / 10 * Math.PI * 2 + t; circle(g, x + cosT(a) * 70 * s, cy + sinT(a * 1.3) * 120 * s, 4, '#e8f4ff'); } g.restore(); }
    return;
  }
  if (pw === 'xray') { g.save(); g.globalCompositeOperation = 'lighter'; const dir = info._facing || 1; const L = 520 * s; g.fillStyle = radGrad(g, x + 14 * s * dir, hy, 0, L, [alpha('#9ff0ff', 0.5), alpha('#9ff0ff', 0)]); g.beginPath(); g.moveTo(x + 14 * s * dir, hy); g.lineTo(x + dir * L, hy - 140 * s); g.lineTo(x + dir * L, hy + 140 * s); g.closePath(); g.fill(); for (let k = 0; k < 5; k++) { const u = ((t * 0.8 + k / 5) % 1); seg(g, [[x + dir * L * u, hy - 140 * s * u], [x + dir * L * u, hy + 140 * s * u]], 2, alpha('#d0ffff', 0.6 * (1 - u))); } g.restore(); }
  if (pw === 'electric') { for (const hx of [-1, 1]) { if ((t * 8 + hx) % 1 < 0.6) FX.lightning(g, { x1: x + hx * 40 * s, y1: y - 100 * s, x2: x + hx * (170 + 60 * sinT(t * 9)) * s, y2: y - (60 + 80 * cosT(t * 7)) * s, color: '#bff4ff', w: 4, jag: 30, branches: 1, seed: Math.floor(t * 12) + hx + 5 }); } glow(g, x, y - 100 * s, 200 * s, '#9fe8ff', 0.35); }
  if (pw === 'space') { ring(g, x + 3 * s, hy, 44 * s, 4, alpha('#dff4ff', 0.9)); circle(g, x + 3 * s, hy, 44 * s, alpha('#bfe6ff', 0.18)); }
  if (pw === 'language') { const W = ['Hola!', 'Bonjour!', 'Ciao!', 'Hallo!', 'Ola!', 'Salut!', 'Merhaba!', 'Jambo!']; const k = Math.floor(gt * 1.2) % W.length; UI.bubble(g, x + 150 * s, hy - 90 * s, { w: 220 * s, h: 80 * s, str: W[k] }); }
  if (pw === 'lie') { const lie = sinT(gt * 0.7) > 0; ring(g, x + 3 * s, hy, 52 * s + 6 * sinT(t * 6), 6, alpha(lie ? '#ff4a4a' : '#5fe08a', 0.8)); glow(g, x, hy, 140 * s, lie ? '#ff4a4a' : '#5fe08a', 0.35); }
  if (pw === 'animal') { for (let k = 0; k < 3; k++) drawProp(g, ['bird', 'dog', 'cat'][k], x + (k - 1) * 170 * s, hy - 150 * s - (k % 2) * 40 * s, 40 * s, t, { disc: false }); }
  if (pw === 'voice' || pw === 'pitch' || pw === 'sing') { for (let k = 0; k < 4; k++) { const ph = (t * 0.7 + k / 4) % 1; g.save(); g.globalAlpha *= 1 - ph; g.strokeStyle = '#ffd25a'; g.lineWidth = 5; g.beginPath(); g.arc(x + 20 * s, hy + 10 * s, (40 + ph * 160) * s, -0.6, 0.6); g.stroke(); g.restore(); } drawProp(g, 'note', x + 150 * s, hy - 40 * s, 50 * s, t, { disc: false }); }
  if (pw === 'armor') { const sh = ((t * 0.7) % 1.6) - 0.3; g.save(); g.globalCompositeOperation = 'lighter'; seg(g, [[x - 40 * s + sh * 80 * s, y - 220 * s], [x - 10 * s + sh * 80 * s, y - 20 * s]], 10 * s, alpha('#ffffff', 0.35)); g.restore(); if ((t * 2) % 1 < 0.12) spk(g, x + 30 * s, y - 150 * s, 30 * s); }
  if (pw === 'internet') { for (let k = 0; k < 12; k++) { const ph = (t * 0.9 + k / 12) % 1; const a = k * 0.9; text(g, k % 2 ? '1' : '0', x + cosT(a) * (260 - ph * 230) * s, hy + sinT(a) * (200 - ph * 180) * s, { size: 30 * s, color: '#7fffd0', font: FONTS.ui, weight: 900, alpha: ph }); } drawProp(g, 'wifi', x, hy - 120 * s, 36 * s, t, { disc: false }); }
  if (pw === 'believe') { for (let k = 0; k < 5; k++) { const a = (t * 1.5 + k * 0.37) % 1; spk(g, x + sinT(k * 2.4) * 140 * s, hy - 60 * s + cosT(k * 1.7) * 90 * s, 22 * s * sinT(a * Math.PI)); } }
  if (pw === 'aim') { const tx = x + (info._facing || 1) * 420 * s, ty = hy; ring(g, tx, ty, 50, 4, alpha('#ff5a5a', 0.9)); seg(g, [[tx - 70, ty], [tx + 70, ty]], 3, alpha('#ff5a5a', 0.9)); seg(g, [[tx, ty - 70], [tx, ty + 70]], 3, alpha('#ff5a5a', 0.9)); }
  if (pw === 'digest') { glow(g, x, y - 120 * s, 70 * s, '#ffd25a', 0.6 + 0.3 * sinT(t * 5)); }
  if (pw === 'laugh') { for (let k = 0; k < 3; k++) { const ph = (t * 0.8 + k / 3) % 1; text(g, 'HA', x + (k - 1) * 110 * s, hy - 70 * s - ph * 120 * s, { size: 44 * s, color: '#ffd25a', font: FONTS.title, weight: 700, alpha: 1 - ph, stroke: 6, strokeColor: 'rgba(0,0,0,.6)' }); } }
  if (pw === 'gecko') { for (const k of [-1, 1]) spk(g, x + k * 45 * s, y - 110 * s, 12 * s * (1 + sinT(t * 6 + k))); }
  if (pw === 'teleport' && (t % 2) < 0.2) glow(g, x, y - 110 * s, 300 * s, '#ffffff', 0.7);
}
function drawRio(g, info, o) {
  o = powerMods(info, { outfit: RIO, ...o });
  info._facing = o.facing ?? 1;
  const pw = info.powerOn ? info.power : null;
  powerFx(g, info, o.x, o.y, o.s, o.t ?? 0, true);
  if (pw === 'stretch') { g.save(); g.translate(o.x, o.y); g.scale(1, 1.15 + 0.25 * Math.abs(sinT((o.t ?? 0) * 2))); g.translate(-o.x, -o.y); drawFigure(g, o); g.restore(); }
  else drawFigure(g, o);
  if (pw === 'arms') drawFigure(g, { ...o, pose: { ...o.pose, eF: [o.pose.eF[0] - 4, o.pose.eF[1] + 30], hF: [o.pose.hF[0] + 10, o.pose.hF[1] + 50], eB: [o.pose.eB[0] + 4, o.pose.eB[1] + 30], hB: [o.pose.hB[0] - 10, o.pose.hB[1] + 50] }, shadow: false, trail: null });
  if (pw === 'double') drawFigure(g, { ...o, x: o.x + (o.facing ?? 1) * -150 * o.s, facing: -(o.facing ?? 1), shadow: true, trail: null, expr: 'smirk' });
  powerFx(g, info, o.x, o.y, o.s, o.t ?? 0, false);
}

// Rio's motion for each action: returns figure params for local time t
function actionFigure(info, t, GY, M, st) {
  const dur = Math.max(0.5, info.dur), p = clamp(t / dur), s0 = V(1.55, 1.9), dir = (info.seed % 2) ? 1 : -1;
  const cx = E.W / 2 + V(dir * 250, 0), act = info.act || (info.pose === 'run' || info.pose === 'walk' ? info.pose : null);
  const base = { x: cx, y: GY, s: s0, facing: -dir, expr: info.expr, rim: rimOf(M), blink: (t % 3.1) > 3.0, t };
  const talkish = [POSES.talk, POSES.explain, POSES.point, POSES.shrug, POSES.crossArms, POSES.think];
  const gest = (k = 0) => breathe(posesAt(t, [[0, POSES.relaxed], [0.25, talkish[(info.seed + k) % talkish.length]], [Math.max(0.6, dur * 0.55), talkish[(info.seed + k + 2) % talkish.length]]]), t);
  if (st.air && act !== 'fly') {   // in the sky / in space nobody stands: float and keep gesturing
    const y = E.H * V(0.62, 0.58) + sinT(t * 2) * 18;
    return { ...base, y, pose: gest(), shadow: false, rot: sinT(t * 1.3) * 0.05, expr: info.expr, _wind: true };
  }
  switch (act) {
    case 'fly': { const air = st.air; const x = E.W / 2 + lerp(-1, 1, p) * V(520, 260) * -dir; const y = air ? E.H * V(0.5, 0.48) + sinT(t * 2.2) * 24 : GY - ease.out(p) * V(300, 520) + sinT(t * 2.2) * 14;
      return { ...base, x, y, pose: POSES.dive, rot: -dir * 0.0 + (air ? -0.15 : -0.05), facing: -dir, expr: info.expr === 'neutral' ? 'joy' : info.expr, trail: { count: 3, dx: dir * 60, a: 0.2 }, shadow: false, _fly: true }; }
    case 'run': { const x = E.W / 2 + lerp(-1, 1, p) * V(420, 220) * -dir; return { ...base, x, pose: walkPose(t * 9, { run: true }), trail: { count: 3, dx: dir * 50 }, _dust: true }; }
    case 'walk': { const x = E.W / 2 + lerp(-1, 1, p) * V(260, 140) * -dir; return { ...base, x, pose: walkPose(t * 5, {}) }; }
    case 'drive': return { ...base, x: E.W / 2, pose: POSES.sit, _car: true };
    case 'jump': { const ph = (t % 1.6) / 1.6, h = 4 * ph * (1 - ph); return { ...base, y: GY - h * V(260, 380), pose: h > 0.1 ? POSES.jump : POSES.crouch, expr: 'joy', shadow: true }; }
    case 'fall': return { ...base, y: GY - (1 - ease.in(clamp(p * 1.4))) * V(160, 260), pose: POSES.fall, rot: -dir * 0.6 * ease.out(p), expr: 'scared' };
    case 'climb': { const ph = sinT(t * 5); return { ...base, y: GY - p * V(260, 420), pose: ph > 0 ? POSES.reach : POSES.pointUp, facing: 1, _wall: true, shadow: false }; }
    case 'swim': return { ...base, x: E.W / 2 + lerp(-1, 1, p) * V(300, 160) * -dir, y: GY - 40 + sinT(t * 3) * 10, pose: POSES.dive, rot: 0.05 * sinT(t * 3), shadow: false, _swim: true };
    case 'eat': case 'drink': return { ...base, pose: breathe(posesAt(t, [[0, POSES.holdFront], [0.6, POSES.phone], [1.0, POSES.holdFront], [1.6, POSES.phone]]), t), expr: 'happy', _hold: true };
    case 'phone': return { ...base, pose: breathe(POSES.phone, t), prop: undefined, _hold: true };
    case 'read': case 'write': case 'type': return { ...base, pose: breathe(act === 'type' ? POSES.holdFront : POSES.holdFront, t), _hold: true };
    case 'lift': return { ...base, pose: breathe(posesAt(t, [[0, POSES.crouch], [0.5, POSES.cheer]]), t), expr: 'determined', _hold: true, _above: true };
    case 'throw': return { ...base, pose: posesAt(t, [[0, POSES.ready], [0.45, POSES.point]]), expr: 'determined', _throw: true };
    case 'sleep': return { ...base, pose: POSES.lie, expr: 'neutral', blink: true, _sleep: true };
    case 'laugh': return { ...base, y: GY - Math.abs(sinT(t * 9)) * 10, pose: breathe(POSES.cheer, t), expr: 'joy', _ha: true };
    case 'cry': return { ...base, pose: breathe(POSES.sad, t), expr: 'cry', _tears: true };
    case 'hug': return { ...base, x: E.W / 2 - V(70, 60), facing: 1, pose: POSES.reach, expr: 'joy', _hug: true };
    case 'sing': return { ...base, pose: breathe(POSES.talk, t), expr: 'happy', _notes: true, _hold: true };
    case 'shout': return { ...base, pose: breathe(POSES.cheer, t), expr: 'angry', _shout: true };
    case 'dance': { const k = Math.floor(t * 3) % 3; return { ...base, y: GY - Math.abs(sinT(t * 6)) * 14, pose: [POSES.cheer, POSES.wave, POSES.jump][k], expr: 'joy' }; }
    case 'look': return { ...base, pose: breathe(POSES.point, t), expr: info.expr === 'neutral' ? 'surprised' : info.expr, _look: true };
    case 'listen': return { ...base, pose: breathe(POSES.think, t), expr: 'thinking', _listen: true };
    case 'think': return { ...base, pose: breathe(POSES.think, t), expr: 'thinking', _thought: true };
    case 'sit': return { ...base, pose: breathe(POSES.sit, t), _chair: true };
    case 'wave': return { ...base, pose: posesAt(t, [[0, POSES.wave], [0.3, POSES.relaxed], [0.6, POSES.wave], [0.9, POSES.relaxed]]), expr: 'happy' };
    case 'cheer': return { ...base, y: GY - Math.abs(sinT(t * 7)) * 18, pose: breathe(POSES.cheer, t), expr: 'joy', _confetti: true };
    case 'talk': return { ...base, pose: gest(), talk: talkAmount(info.globalT) * 0.3, _bubble: true };
    default: {
      if (info.pose === 'phone') return { ...base, pose: breathe(POSES.phone, t), _hold: true };
      if (info.pose === 'handsOnHead' || info.pose === 'facepalm' || info.pose === 'shrug' || info.pose === 'sad') return { ...base, pose: breathe(POSES[info.pose], t) };
      // idle: walk in for a few frames on some shots, otherwise gestures
      if (info.seed % 5 === 0 && dur > 2) { const wp = clamp(t / 1.2); return wp < 1 ? { ...base, x: cx + (1 - ease.out(wp)) * V(300, 160) * dir, pose: walkPose(t * 5, {}) } : { ...base, pose: gest(1) }; }
      return { ...base, pose: gest() };
    }
  }
}

function act(g, t, info) {
  const kind = info.power === 'giant' && info.powerOn ? 'wide' : ['wide', 'mid', 'mid', 'close'][info.seed % 4];
  let cam = camFor(info, kind);
  const GROUNDED = ['hug', 'eat', 'drink', 'sleep', 'sit', 'walk', 'run', 'drive', 'type', 'read', 'write', 'lift', 'dance', 'cry', 'climb', 'swim'];
  let loc = (info.act === 'fly' && !['sky', 'space', 'canyon', 'mountain', 'city', 'ocean'].includes(info.loc)) ? 'sky' : info.loc;
  if (['sky', 'space'].includes(loc) && GROUNDED.includes(info.act)) loc = info.loc2 && !['sky', 'space'].includes(info.loc2) ? info.loc2 : 'park';
  if (info.act === 'swim' && !['ocean', 'poolside', 'lake', 'beach'].includes(loc)) loc = 'poolside';
  const st = drawSet(loc, g, t, cam); const { GY, M } = st;
  const f = actionFigure(info, t, GY, M, st);
  const props = (info.props || []).filter(p => hasProp(p.k));
  const holdKey = f._hold ? ((props.find(p => (HOLD[info.act] || []).includes(p.k)) || {}).k || DEF_HOLD[info.act] || (props[0] || {}).k) : null;
  const free = props.filter(p => p.k !== holdKey);
  const friendIn = (E.cfg.cast || []).length && (f._hug || info.seed % 3 === 0) && !['fly', 'swim', 'climb'].includes(info.act);
  layer(g, cam, 1, (g) => {
    if (f._wall) { rr(g, f.x - V(240, 220), -E.H, V(260, 240), E.H * 3, 0); g.fillStyle = alpha(shade(M.wall, -0.2), 0.95); g.fill(); for (let y = -E.H; y < E.H * 2; y += 60) seg(g, [[f.x - V(240, 220), y], [f.x + V(20, 20), y]], 2, alpha('#000', 0.2)); }
    if (f._chair) FX.chair(g, f.x - 18 * f.s, GY, f.s, '#24181e');
    if (f._swim) { g.fillStyle = alpha('#2a8ad0', 0.35); g.fillRect(-E.W, GY - 70, E.W * 3, E.H); }
    if (friendIn) { const fr = castOf(info.friend); const fx = f._hug ? f.x + V(120, 110) : E.W / 2 - (f.x - E.W / 2) * 1.15; drawFigure(g, { x: fx, y: GY, s: f.s * 0.95, facing: fx > f.x ? -1 : 1, outfit: fr, pose: f._hug ? POSES.reach : breathe(posesAt(t, [[0, POSES.relaxed], [0.4, [POSES.handsOnHead, POSES.cheer, POSES.point, POSES.crossArms][info.seed % 4]]]), t, 1, 2), expr: f._hug ? 'joy' : ['surprised', 'smile', 'shocked', 'neutral'][info.seed % 4], rim: rimOf(M), look: [fx > f.x ? -1 : 1, 0] }); }
    if (f._car) { drawFigure(g, { ...f, y: GY - V(60, 80) }); g.save(); g.translate(E.W / 2, GY - V(60, 70)); drawProp(g, 'car', 0, 0, V(230, 260), t, { disc: false, bob: false }); g.restore(); }
    else drawRio(g, info, f);
    if (f._wind) for (let k = 0; k < 7; k++) { const ph = (t * 1.2 + k / 7) % 1; seg(g, [[f.x - 140 + k * 40, f.y + 30 + ph * 200], [f.x - 140 + k * 40, f.y + 70 + ph * 200]], 3, alpha('#ffffff', 0.45 * (1 - ph))); }
    if (f._dust) for (let k = 0; k < 4; k++) { const ph = (t * 2 + k / 4) % 1; circle(g, f.x + (f.facing > 0 ? -1 : 1) * (40 + ph * 120), GY - 10 - ph * 30, 10 + ph * 16, alpha('#d8c8b0', 0.4 * (1 - ph))); }
    if (holdKey) { const hx = f.x + (f.facing ?? 1) * 52 * f.s, hy = f._above ? f.y - 300 * f.s : f.y - (info.act === 'phone' || info.pose === 'phone' ? 175 : 125) * f.s; drawProp(g, holdKey, hx, hy, (info.act === 'type' ? 60 : info.act === 'phone' ? 34 : 44) * f.s, t, { disc: false, bob: false }); }
    if (f._throw && props[0]) { const ph = clamp((t - 0.45) / 1.2); if (ph > 0) drawProp(g, props[0].k, f.x + (f.facing ?? 1) * ph * V(700, 400), f.y - 200 * f.s - 4 * ph * (1 - ph) * 300, 40 * f.s, t, { disc: false }); }
    if (f._tears) for (let k = 0; k < 2; k++) { const ph = (t * 1.2 + k * 0.5) % 1; circle(g, f.x + (k ? 14 : -6) * f.s * (f.facing ?? 1), f.y - 200 * f.s + ph * 90 * f.s, 5 * f.s, alpha('#8fd0ff', 1 - ph)); }
    if (f._sleep) for (let k = 0; k < 3; k++) { const ph = (t * 0.5 + k / 3) % 1; text(g, 'z', f.x + 60 * f.s + ph * 60, f.y - 60 * f.s - ph * 160, { size: (26 + k * 10) * f.s, color: '#dfe8ff', font: FONTS.title, alpha: sinT(ph * Math.PI) }); }
    if (f._ha) for (let k = 0; k < 3; k++) { const ph = (t * 0.9 + k / 3) % 1; text(g, k % 2 ? 'HA!' : 'HA', f.x + (k - 1) * 90 * f.s, f.y - 260 * f.s - ph * 120, { size: 40 * f.s, color: '#ffd25a', font: FONTS.title, alpha: 1 - ph, stroke: 6, strokeColor: 'rgba(0,0,0,.6)' }); }
    if (f._shout) { for (let k = 0; k < 5; k++) { const a = -0.6 + k * 0.3; seg(g, [[f.x + (f.facing ?? 1) * (60 + 20 * sinT(t * 20)) * f.s * cosT(a), f.y - 200 * f.s + 60 * f.s * sinT(a)], [f.x + (f.facing ?? 1) * 120 * f.s * cosT(a), f.y - 200 * f.s + 110 * f.s * sinT(a)]], 5, '#fff3c8'); } }
    if (f._notes) drawProp(g, 'note', f.x + (f.facing ?? 1) * 140 * f.s, f.y - 280 * f.s, 50 * f.s, t, { disc: false });
    if (f._listen) for (let k = 0; k < 3; k++) { const ph = (t * 0.8 + k / 3) % 1; g.save(); g.globalAlpha *= 1 - ph; g.strokeStyle = '#ffd25a'; g.lineWidth = 4; g.beginPath(); g.arc(f.x, f.y - 200 * f.s, (50 + ph * 120) * f.s, -0.5 + (f.facing > 0 ? 0 : Math.PI), 0.5 + (f.facing > 0 ? 0 : Math.PI)); g.stroke(); g.restore(); }
    if (f._confetti) for (let k = 0; k < 24; k++) { const r = rng(k + 3), x = r() * E.W, y = ((r() * E.H + t * (120 + r() * 100)) % (E.H + 100)) - 100; g.save(); g.translate(x, y); g.rotate(t * 4 + k); g.fillStyle = ['#e0443a', '#f2c21a', '#3a8ae0', '#5ab04a', '#e06aa0'][k % 5]; g.fillRect(-6, -3, 12, 6); g.restore(); }
    if (f._hug) drawProp(g, 'heart', f.x + V(60, 55), f.y - 300 * f.s, 34 * f.s, t, { disc: false });
  });
  st.fx?.(g, t);
  // props from the sentence: big card for the first, small bubbles for the rest
  const side = f.x > E.W / 2 ? -1 : 1;
  if (f._thought || f._bubble) { const pk = (free[0] || props[0] || {}).k; const bx = f.x + side * V(260, 150), by = f.y - V(560, 700) * f.s / V(1.55, 1.9);
    const a = ease.out(prog(t, 0.1, 0.4)); g.save(); g.globalAlpha *= a;
    if (f._thought) { for (let k = 0; k < 3; k++) circle(g, f.x + side * (40 + k * 45) * f.s, f.y - (250 + k * 45) * f.s, (8 + k * 6) * f.s, '#f4efe6'); }
    rr(g, bx - V(170, 160), by - V(130, 130), V(340, 320), V(260, 260), V(120, 120)); g.fillStyle = '#f4efe6'; g.fill(); g.restore();
    if (pk) drawProp(g, pk, bx, by, V(85, 85), t, { disc: false, start: 0.15 }); else { for (let i = -1; i <= 1; i++) circle(g, bx + i * 50, by, 14 * a, S().ink); }
  } else {
    free.forEach((pr, k) => {
      const st0 = propStart(info, pr);
      const big = k === 0, px = E.W / 2 + side * V(big ? 520 : 300 + k * 120, big ? 230 : 280 - k * 140), py = big ? GY - V(380, 620) : V(250, 420) + (k - 1) * V(40, 90);
      if (E.vertical && big) drawProp(g, pr.k, E.W / 2 + side * 210, E.H * 0.3, 120, t, { start: st0 });
      else drawProp(g, pr.k, px, py, big ? V(120, 120) : V(70, 80), t, { start: st0 });
    });
  }
  if (info.numAny && !E.cfg.captions) UI.readout(g, { value: info.numAny[0], x: E.W / 2, y: V(150, 300), align: 'center', size: V(64, 72), a: ease.out(prog(t, 0.2, 0.6)) });
}

// single prop, big and centred over a blurred version of the location
function focus(g, t, info) {
  const props = (info.props || []).filter(p => hasProp(p.k)); const pr = props[(info.seed >> 1) % Math.max(1, props.length)] || props[0];
  blurLayer(g, 14, (g) => drawSet(info.loc, g, t * 0.3, { z: 1.4, x: (info.seed % 2 ? 1 : -1) * 140, y: -E.H * 0.06 }));
  veil(g, '#0a0812', 0.35);
  const M = mood('dusk');
  if (!pr) { face(g, t, info); return; }
  const cx = E.W / 2 + V(info.seed % 2 ? 260 : -260, 0), cy = E.H * V(0.46, 0.38);
  FX.rings(g, cx, cy, t, { count: 3, r0: 180, r1: 420, color: '#fff3e0', a: 0.12 });
  drawProp(g, pr.k, cx, cy, V(210, 230), t, { start: 0, label: E.vertical ? null : pr.w, discColor: '#fff3dc' });
  drawRio(g, info, { x: E.W / 2 + V(info.seed % 2 ? -420 : 420, info.seed % 2 ? -220 : 220), y: E.H * V(0.98, 0.8), s: V(1.5, 1.9), facing: info.seed % 2 ? 1 : -1, pose: breathe(posesAt(t, [[0, POSES.relaxed], [0.3, [POSES.point, POSES.handsOnHead, POSES.think, POSES.explain][info.seed % 4]]]), t), expr: info.expr === 'neutral' ? 'surprised' : info.expr, rim: rimOf(M), look: [info.seed % 2 ? 1 : -1, -0.4], t });
}

// 2-3 props in a row, each popping in on its word, with labels
function propsShot(g, t, info) {
  const props = (info.props || []).filter(p => hasProp(p.k));
  blurLayer(g, 16, (g) => drawSet(info.loc, g, t * 0.3, { z: 1.3, x: 0, y: 0 }));
  veil(g, '#08060e', 0.5);
  const n = props.length || 1;
  props.forEach((pr, k) => {
    const st0 = Math.max(0, propStart(info, pr)) || k * 0.35;
    const x = E.vertical ? E.W / 2 + (k % 2 ? 180 : -180) * (n > 1 ? 1 : 0) : E.W * (k + 1) / (n + 1);
    const y = E.vertical ? E.H * (0.22 + k * 0.2) : E.H * 0.46 + (k % 2 ? 40 : -40);
    drawProp(g, pr.k, x, y, V(150, 140), t, { start: st0, label: E.vertical ? null : pr.w, discColor: ['#fff3dc', '#dff4ff', '#ffe0f0'][k % 3] });
    if (k > 0 && !E.vertical) text(g, '+', E.W * (k + 0.5) / (n + 1), E.H * 0.46, { size: 80, color: alpha('#fff', 0.5), font: FONTS.title, alpha: clamp((t - st0) * 3) });
  });
  const M = mood('dusk');
  drawFigure(g, { x: E.W * V(0.1, 0.82), y: E.H * V(0.98, 0.92), s: V(1.1, 1.2), facing: 1, outfit: RIO, pose: breathe(POSES.pointUp, t), expr: 'awe', rim: rimOf(M), look: [0.6, -1] });
}

function think(g, t, info) { act(g, t, { ...info, act: 'think' }); }
function hero(g, t, info) { act(g, t, info); }

// duo: two characters talk; the first prop of the line floats between them
function duo2(g, t, info) {
  if (SETS[info.loc] && ['sky', 'space'].includes(info.loc)) { act(g, t, { ...info, act: 'talk' }); return; }
  duo(g, t, info);
  const props = (info.props || []).filter(p => hasProp(p.k));
  if (props[0]) drawProp(g, props[0].k, E.W / 2, E.H * V(0.3, 0.32), V(90, 100), t, { start: Math.max(0, propStart(info, props[0])) });
  if (info.powerOn && info.power) { const s = V(1.6, 1.75), x = E.W / 2 - V(230, 200), y = E.H * V(0.8, 0.7); powerFx(g, info, x, y, s, t, false); }
}

const T = { dir: directed, hero, act, focus, props: propsShot, think, duo: duo2, face, number, science, compare, question, title, end };
for (const sh of E.shots) {
  registerShot(sh.id, { draw(g, t, info) {
    (T[info.tpl] || act)(g, t, info);
    if (info.hook && info.shot.id === 's001' && info.title) {   // Shorts: title band over the hook
      const a = clamp(Math.min(t / 0.3, (info.dur - t) / 0.4));
      g.save(); g.globalAlpha *= a; g.fillStyle = 'rgba(8,6,14,.55)'; rr(g, 60, 190, E.W - 120, 330, 30); g.fill(); g.restore();
      blockText(g, info.title.toUpperCase(), E.W / 2, 355, { size: 84, maxW: E.W - 180, color: S().ui.gold, a, maxLines: 3 });
    }
  } });
}
