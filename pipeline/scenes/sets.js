// sets.js — reusable locations for the Rio Animation auto-templates. Each set(g, t, cam, o) draws the background
// layers and returns { GY, CX, M }. Characters are drawn by the caller at depth 1.
import { E, V, mood, layer, backdrop, rr, seg, circle, ring, poly, linGrad, radGrad, glow, alpha, shade, mix, rng, text, FONTS } from '/engine/core.js';
import * as FX from '/engine/fx2d.js';

const ground = () => E.H * V(0.8, 0.7);

function floor(g, cam, M, GY, lines = true, poolC = null) {
  layer(g, cam, 0.92, (g) => {
    g.fillStyle = linGrad(g, 0, GY, 0, GY + 600, [shade(M.floor, 0.05), shade(M.dark, -0.2)]); g.fillRect(-E.W, GY, E.W * 3, E.H * 2);
    if (lines) FX.floorLines(g, GY, GY + 700, 'rgba(0,0,0,.22)', 0.07);
    if (poolC) FX.pool(g, E.W / 2, GY + 16, V(520, 420), 70, poolC, 0.22);
  });
}

export function street(g, t, cam, o = {}) {
  const M = mood(o.mood || 'night'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.1, (g) => { backdrop(g, M.sky); FX.stars(g, 0, { count: 90, area: [-E.W, -E.H, E.W * 3, GY], color: '#dfe6ff' }); FX.moon(g, CX + V(600, 280), GY - V(700, 1150), 46); });
  layer(g, cam, 0.3, (g) => FX.skyline(g, { x: -E.W, y: GY - V(140, 260), w: E.W * 3, minH: 120, maxH: V(520, 820), color: mix(M.sky[0], '#000', 0.35), windowColor: alpha(M.practical, 0.7), lit: 0.25, seed: 11 }));
  layer(g, cam, 0.6, (g) => {
    FX.skyline(g, { x: -E.W, y: GY, w: E.W * 3, minH: 200, maxH: V(460, 760), minW: 120, maxW: 260, color: shade(M.wall, -0.45), windowColor: alpha(M.practical, 0.9), lit: 0.35, seed: 4 });
    for (const x of [-700, -100, 500, 1100, 1700, 2300]) FX.lampPost(g, x, GY, V(360, 420), { light: M.practical });
  });
  layer(g, cam, 0.92, (g) => {
    g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, [shade(M.road, 0.1), shade(M.dark, -0.3)]); g.fillRect(-E.W, GY, E.W * 3, E.H * 2);
    for (let x = -E.W; x < E.W * 2; x += 220) { g.fillStyle = alpha('#f2e6c8', 0.35); g.fillRect(x, GY + V(150, 260), 110, 8); }
    for (const x of [-700, -100, 500, 1100, 1700]) FX.pool(g, x + 34, GY + 20, 220, 36, M.practical, 0.2);
  });
  return { GY, CX, M, fx: (g, t) => FX.dust(g, t, { count: 30, color: '#c9d4ff', a: 0.25 }) };
}

export function home(g, t, cam, o = {}) {
  const M = mood(o.mood || 'interiorWarm'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.35, (g) => {
    g.fillStyle = linGrad(g, 0, -E.H, 0, GY, [M.dark, M.wall]); g.fillRect(-E.W, -E.H, E.W * 3, GY + E.H);
    for (let x = -E.W; x < E.W * 2; x += 90) { g.fillStyle = alpha(shade(M.wall, 0.15), 0.25); g.fillRect(x, -E.H, 3, GY + E.H); }
    const wx = CX + V(180, -230), wy = GY - V(600, 900), ww = V(440, 460), wh = V(340, 420);
    FX.windowFrame(g, { x: wx, y: wy, w: ww, h: wh, cols: 2, frame: shade(M.wall, -0.55), bar: 10 }, (g, x, y, w, h) => {
      g.fillStyle = linGrad(g, 0, y, 0, y + h, mood('dusk').sky); g.fillRect(x, y, w, h);
      FX.skyline(g, { x, y: y + h, w, maxH: h * 0.5, color: alpha('#2a2036', 0.9), windowColor: alpha(M.practical, 0.8), seed: 9 });
    });
    // picture frames + shelf
    const fx0 = CX - V(640, 380), fy0 = GY - V(560, 1000);
    for (let k = 0; k < 3; k++) { rr(g, fx0 + k * 130, fy0 + (k % 2) * 30, 100, 80, 6); g.fillStyle = shade(M.wall, -0.5); g.fill(); rr(g, fx0 + k * 130 + 8, fy0 + 8 + (k % 2) * 30, 84, 64, 4); g.fillStyle = ['#c98a6a', '#6a8ac9', '#8ac96a'][k]; g.fill(); }
    // lamp
    const lx = CX - V(520, 330); seg(g, [[lx, GY - 40], [lx, GY - 330]], 6, shade(M.wall, -0.6)); poly(g, [[lx - 60, GY - 330], [lx + 60, GY - 330], [lx + 38, GY - 400], [lx - 38, GY - 400]], '#f2d9a8');
    glow(g, lx, GY - 340, 260, M.practical, 0.45);
  });
  layer(g, cam, 0.75, (g) => {   // sofa
    const sx = CX + V(380, 250), sw = V(520, 380);
    rr(g, sx - sw / 2, GY - 190, sw, 120, 26); g.fillStyle = shade('#6a4a6a', -0.2); g.fill();
    rr(g, sx - sw / 2 - 20, GY - 110, sw + 40, 70, 22); g.fillStyle = '#6a4a6a'; g.fill();
    seg(g, [[sx - sw / 2, GY - 40], [sx - sw / 2, GY]], 10, '#1a1218'); seg(g, [[sx + sw / 2, GY - 40], [sx + sw / 2, GY]], 10, '#1a1218');
  });
  floor(g, cam, M, GY, true, M.key);
  return { GY, CX, M, fx: (g, t) => FX.dust(g, t, { count: 40, color: '#ffe2bd', a: 0.3 }) };
}

export function hospital(g, t, cam, o = {}) {
  const M = mood(o.mood || 'interiorCool'), GY = ground(), CX = E.W / 2;
  const wall = mix(M.wall, '#9fb4c8', 0.35);
  layer(g, cam, 0.35, (g) => {
    g.fillStyle = linGrad(g, 0, -E.H, 0, GY, [shade(wall, -0.4), wall]); g.fillRect(-E.W, -E.H, E.W * 3, GY + E.H);
    g.fillStyle = shade(wall, -0.25); g.fillRect(-E.W, GY - 150, E.W * 3, 14);
    for (const x of [-600, 0, 600, 1200, 1800]) { rr(g, x, -E.H * 0.2 + V(0, 300), 320, 26, 10); g.fillStyle = '#e8f6ff'; g.fill(); glow(g, x + 160, V(-200, 120), 360, '#cfefff', 0.25); }
    // red cross sign
    const cx = CX - V(620, 340), cy = GY - V(560, 1000); rr(g, cx - 60, cy - 60, 120, 120, 14); g.fillStyle = '#f4f7fa'; g.fill(); g.fillStyle = '#e0443a'; g.fillRect(cx - 14, cy - 44, 28, 88); g.fillRect(cx - 44, cy - 14, 88, 28);
    // heart monitor
    FX.screen(g, { x: CX + V(420, 160), y: GY - V(520, 820), w: 200, h: 130, glowC: '#5fd39a', a: 0.25 }, (g, x, y, w, h) => {
      g.strokeStyle = '#5fd39a'; g.lineWidth = 3; g.beginPath();
      for (let i = 0; i <= 40; i++) { const u = (i / 40 + t * 0.5) % 1, beat = Math.abs(u - 0.5) < 0.03 ? -40 * Math.sin((u - 0.47) * 52) : 0; const px = x + 8 + i * (w - 16) / 40; i ? g.lineTo(px, y + h / 2 + beat) : g.moveTo(px, y + h / 2 + beat); }
      g.stroke();
    });
  });
  layer(g, cam, 0.75, (g) => FX.bed(g, { x: CX + V(160, -120), y: GY, w: V(460, 380), color: '#a8c8e8', frame: '#3a4a5a', pillow: '#f2f6fa' }));
  floor(g, cam, M, GY, true, '#cfefff');
  return { GY, CX, M };
}

export function stadium(g, t, cam, o = {}) {
  const M = mood(o.mood || 'night'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.1, (g) => { backdrop(g, M.sky); FX.stars(g, 0, { count: 60, area: [-E.W, -E.H, E.W * 3, GY * 0.6] }); });
  layer(g, cam, 0.3, (g) => {
    for (const x of [CX - V(700, 380), CX + V(700, 380)]) { seg(g, [[x, GY - V(260, 400)], [x, GY - V(760, 1300)]], 10, '#1a1a28'); rr(g, x - 70, GY - V(820, 1360), 140, 70, 8); g.fillStyle = '#f6f8ff'; g.fill(); glow(g, x, GY - V(785, 1325), 420, '#eaf2ff', 0.55); FX.lightCone(g, x, GY - V(760, 1300), { angle: Math.PI / 2 + (x < CX ? -0.35 : 0.35), spread: 0.45, len: 1400, color: '#eaf2ff', a: 0.08 }); }
  });
  layer(g, cam, 0.5, (g) => {
    g.fillStyle = shade(M.wall, -0.5); g.fillRect(-E.W, GY - V(420, 640), E.W * 3, V(420, 640));
    FX.crowd(g, t, { y: GY - V(400, 610), x: -E.W, w: E.W * 3, rows: V(13, 20), rowH: 28, colors: ['#3a3358', '#5a3a4a', '#2a4a6a', '#6a5a3a', '#4a2a3a'], flags: 0.03, cheer: 0.6, size: 1.1 });
    g.fillStyle = '#1a1424'; g.fillRect(-E.W, GY - 40, E.W * 3, 40);
  });
  layer(g, cam, 0.92, (g) => {
    g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, ['#3f7a4a', '#1d3a26']); g.fillRect(-E.W, GY, E.W * 3, E.H * 2);
    for (let x = -E.W; x < E.W * 2; x += 180) { g.fillStyle = 'rgba(255,255,255,.04)'; g.fillRect(x, GY, 90, E.H); }
    FX.pool(g, CX, GY + 30, 600, 80, '#eaf2ff', 0.18);
  });
  return { GY, CX, M };
}

export function park(g, t, cam, o = {}) {
  const M = mood(o.mood || 'day'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.08, (g) => { backdrop(g, M.sky); FX.sun(g, CX - V(560, 260), GY - V(640, 1100), 60, '#fffbe8', M.key, 4); FX.clouds(g, { y: GY - V(680, 1200), h: 220, color: '#ffffff', a: 0.35, seed: 5 }); });
  layer(g, cam, 0.25, (g) => FX.hills(g, { y: GY - V(140, 260), amp: 160, color: mix(M.grass, M.sky[0], 0.55), seed: 3 }));
  layer(g, cam, 0.5, (g) => { FX.hills(g, { y: GY - 30, amp: 90, color: shade(M.grass, -0.15), seed: 7 }); for (const [x, s] of [[-300, 1.3], [180, 1.6], [CX + V(560, 300), 1.9], [1500, 1.4], [2100, 1.7]]) FX.tree(g, x, GY - 20, s, shade(M.grass, -0.55)); });
  layer(g, cam, 0.92, (g) => {
    g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, [M.grass, shade(M.grass, -0.5)]); g.fillRect(-E.W, GY, E.W * 3, E.H * 2);
    g.fillStyle = alpha('#d8c49a', 0.55); g.beginPath(); g.moveTo(-E.W, GY + V(120, 200)); g.quadraticCurveTo(CX, GY + V(40, 80), E.W * 2, GY + V(160, 260)); g.lineTo(E.W * 2, GY + V(200, 320)); g.quadraticCurveTo(CX, GY + V(90, 150), -E.W, GY + V(170, 280)); g.fill();
  });
  return { GY, CX, M, fx: (g, t) => FX.dust(g, t, { count: 24, color: '#fffbe0', a: 0.35 }) };
}

export function classroom(g, t, cam, o = {}) {
  const M = mood(o.mood || 'interiorWarm'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.35, (g) => {
    g.fillStyle = linGrad(g, 0, -E.H, 0, GY, [M.dark, mix(M.wall, '#6a7a5a', 0.3)]); g.fillRect(-E.W, -E.H, E.W * 3, GY + E.H);
    const bw = V(900, 760), bh = V(380, 420), bx = CX - bw / 2, by = GY - V(640, 1050);
    rr(g, bx - 14, by - 14, bw + 28, bh + 28, 10); g.fillStyle = '#5a4030'; g.fill(); g.fillStyle = '#1f3a2e'; g.fillRect(bx, by, bw, bh);
    g.strokeStyle = alpha('#f2f2e8', 0.6); g.lineWidth = 4; g.beginPath(); g.moveTo(bx + 60, by + 90); g.lineTo(bx + 300, by + 90); g.moveTo(bx + 60, by + 150); g.lineTo(bx + 420, by + 150); g.stroke();
    ring(g, bx + bw - 180, by + bh / 2, 80, 4, alpha('#f2f2e8', 0.55)); seg(g, [[bx + bw - 260, by + bh / 2], [bx + bw - 100, by + bh / 2]], 3, alpha('#f2f2e8', 0.4));
    FX.clock(g, CX + V(640, 360), GY - V(700, 1150), 40, 10 * 3600 + t * 2);
    for (const x of [-500, CX - V(820, 470), CX + V(820, 470), 2400]) { FX.windowFrame(g, { x: x - 90, y: GY - V(560, 760), w: 180, h: V(300, 360), cols: 1, frame: shade(M.wall, -0.5), bar: 8 }, (g, x, y, w, h) => { g.fillStyle = linGrad(g, 0, y, 0, y + h, mood('day').sky); g.fillRect(x, y, w, h); }); }
  });
  layer(g, cam, 0.8, (g) => { for (const x of [CX - V(560, 320), CX + V(560, 320)]) { rr(g, x - 120, GY - 110, 240, 18, 6); g.fillStyle = '#7a5a40'; g.fill(); seg(g, [[x - 100, GY - 100], [x - 100, GY]], 8, '#3a2a20'); seg(g, [[x + 100, GY - 100], [x + 100, GY]], 8, '#3a2a20'); } });
  floor(g, cam, M, GY, true, M.key);
  return { GY, CX, M, fx: (g, t) => FX.dust(g, t, { count: 30, color: '#ffe8c8', a: 0.3 }) };
}

export function cafe(g, t, cam, o = {}) {
  const M = mood(o.mood || 'golden'), GY = ground(), CX = E.W / 2;
  const wall = shade(M.wall, -0.3), wallDark = shade(M.wall, -0.6);
  layer(g, cam, 0.12, (g) => { backdrop(g, M.sky); FX.sun(g, CX + V(620, 300), GY - V(560, 1000), 64, '#fff3dc', M.key, 5); FX.skyline(g, { x: -E.W, y: GY - V(420, 700), w: E.W * 3, minH: 80, maxH: V(260, 420), color: mix(M.sky[1], wallDark, 0.75), windowColor: alpha(M.practical, 0.5), lit: 0.15, seed: 8 }); });
  layer(g, cam, 0.55, (g) => {
    const top = GY - V(560, 860), left = CX - 1500, w = 3000;
    g.fillStyle = linGrad(g, 0, top, 0, GY, [shade(wall, 0.06), wall, wallDark]); g.fillRect(left, top, w, GY - top + 4);
    const ay = GY - V(430, 560), ah = 58;
    for (const i of [-3, -2, -1, 1, 2, 3]) { const ww = 210, wh = V(250, 300), wx = CX + i * 300 - ww / 2 + (i > 0 ? 30 : -30), wy = ay + 46;
      FX.windowFrame(g, { x: wx, y: wy, w: ww, h: wh, cols: 2, rows: 1, frame: wallDark, bar: 9 }, (g, x, y, w, h) => { g.fillStyle = linGrad(g, 0, y, 0, y + h, [M.practical, shade(M.practical, -0.45), shade(M.practical, -0.7)]); g.fillRect(x, y, w, h); circle(g, x + w * 0.5, y + 34, 9, '#fff3d6'); glow(g, x + w * 0.5, y + 34, 70, '#fff3d6', 0.5); });
      glow(g, wx + ww / 2, wy + wh / 2, 230, M.practical, 0.1); }
    FX.door(g, { x: CX - 70, y: GY, w: 140, h: V(330, 380), color: wallDark, open: 0.3, light: M.practical });
    for (let x = left, k = 0; x < left + w; x += 56, k++) { g.fillStyle = k % 2 ? '#c9b8a4' : '#2f6a8f'; g.fillRect(x, ay - ah, 56, ah); g.beginPath(); g.arc(x + 28, ay, 28, 0, Math.PI); g.fill(); }
  });
  layer(g, cam, 0.9, (g) => { g.fillStyle = linGrad(g, 0, GY, 0, GY + 400, [shade(M.floor, -0.1), shade(M.dark, -0.2)]); g.fillRect(-E.W, GY, E.W * 3, E.H * 2); FX.floorLines(g, GY, GY + 600, 'rgba(0,0,0,.25)', 0.08); FX.pool(g, CX, GY + 20, 260, 34, M.practical, 0.25); });
  return { GY, CX, M, fx: (g, t) => FX.dust(g, t, { count: 36, color: '#ffe2bd', a: 0.35 }) };
}

export function lab(g, t, cam, o = {}) {
  const M = mood(o.mood || 'interiorCool'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.35, (g) => {
    g.fillStyle = linGrad(g, 0, -E.H, 0, GY, [M.dark, M.wall]); g.fillRect(-E.W, -E.H, E.W * 3, GY + E.H);
    for (let k = -2; k <= 2; k++) FX.screen(g, { x: CX + k * V(330, 250) - 110, y: GY - V(600, 1000) + (k % 2) * 40, w: 220, h: 140, glowC: '#7fd0d6', a: 0.18 }, (g, x, y, w, h) => {
      g.strokeStyle = '#7fd0d6'; g.lineWidth = 2; g.beginPath(); for (let i = 0; i < 24; i++) g.lineTo(x + 8 + i * (w - 16) / 23, y + h / 2 - Math.sin(i * 0.8 + t * 2 + k) * 24); g.stroke(); });
  });
  layer(g, cam, 0.7, (g) => FX.counter(g, { x: CX - V(700, 520), y: GY - 30, w: V(1400, 1040), h: 120, color: shade(M.wall, -0.45), top: shade(M.wall, -0.2), doors: 10 }));
  floor(g, cam, M, GY, true, '#7fd0d6');
  return { GY, CX, M };
}


// ---------------- extra locations (bo 2) ----------------
export function sky(g, t, cam, o = {}) {
  const M = mood('day'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.05, (g) => { backdrop(g, ['#4a8ad8', '#8fc0ec', '#d8ecf8']); FX.sun(g, CX + V(600, 300), V(160, 260), 70, '#fffbe8', '#fff3dc', 4); });
  for (const [d, y, a, sp] of [[0.2, 0.25, 0.5, 30], [0.45, 0.55, 0.7, 80], [0.8, 0.85, 0.9, 200]]) layer(g, cam, d, (g) => {
    for (let k = 0; k < 7; k++) { const x = ((k * 520 - t * sp) % 3600 + 3600) % 3600 - 900, yy = E.H * y + Math.sin(k * 2.1) * 90; cloudPuff(g, x, yy, 1 + 0.4 * Math.sin(k * 3), a); } });
  layer(g, cam, 0.3, (g) => FX.hills(g, { y: E.H * V(1.05, 0.95), amp: 60, color: alpha('#5a8a6a', 0.6), seed: 2 }));
  return { GY, CX, M, air: true, fx: (g, t) => FX.speedLines(g, t, { count: 24, a: 0.08, inner: 500 }) };
}
function cloudPuff(g, x, y, s, a) { g.save(); g.globalAlpha *= a; g.fillStyle = '#ffffff'; for (const [dx, dy, r] of [[-70, 10, 55], [-20, -25, 70], [45, -5, 60], [95, 15, 45], [10, 25, 60]]) { g.beginPath(); g.arc(x + dx * s, y + dy * s, r * s, 0, 7); g.fill(); } g.restore(); }

export function ocean(g, t, cam, o = {}) {
  const M = mood('day'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.08, (g) => { backdrop(g, ['#5aa0e0', '#a8d4f2', '#f2e8d0']); FX.sun(g, CX - V(500, 240), GY - V(600, 1000), 60, '#fffbe8', '#fff3dc', 4); FX.clouds(g, { y: GY - V(650, 1100), h: 200, color: '#fff', a: 0.4, seed: 3 }); });
  layer(g, cam, 0.4, (g) => { g.fillStyle = linGrad(g, 0, GY - V(260, 400), 0, GY + 600, ['#3a8ad0', '#1a5aa0', '#0a3060']); g.fillRect(-E.W, GY - V(260, 400), E.W * 3, E.H * 2); });
  layer(g, cam, 0.7, (g) => { for (let row = 0; row < 6; row++) { const y = GY - V(220, 360) + row * V(70, 90); g.strokeStyle = alpha('#cfefff', 0.35 - row * 0.03); g.lineWidth = 4; g.beginPath(); for (let x = -E.W; x <= E.W * 2; x += 30) g.lineTo(x, y + Math.sin(x * 0.01 - t * 2 + row) * 10); g.stroke(); } });
  return { GY, CX, M, water: true, fx: (g, t) => { for (let k = 0; k < 8; k++) { const x = (k * 300 + t * 40) % E.W; circle(g, x, GY + 40 + Math.sin(t * 3 + k) * 10, 3, alpha('#fff', 0.5)); } } };
}
export function beach(g, t, cam, o = {}) {
  const M = mood('golden'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.08, (g) => { backdrop(g, M.sky); FX.sun(g, CX + V(400, 200), GY - V(420, 800), 90, '#fff3dc', M.key, 5); });
  layer(g, cam, 0.35, (g) => { g.fillStyle = linGrad(g, 0, GY - V(240, 380), 0, GY, ['#3a6aa0', '#5a9ad0']); g.fillRect(-E.W, GY - V(240, 380), E.W * 3, V(240, 380)); for (let row = 0; row < 4; row++) { g.strokeStyle = alpha('#ffe8c0', 0.5); g.lineWidth = 3; g.beginPath(); for (let x = -E.W; x <= E.W * 2; x += 30) g.lineTo(x, GY - 200 + row * 50 + Math.sin(x * 0.012 + t * 2 + row) * 8); g.stroke(); } });
  layer(g, cam, 0.6, (g) => { for (const x of [CX - V(700, 380), CX + V(760, 400)]) { seg(g, [[x, GY], [x + 30, GY - 300], [x + 70, GY - 520]], 22, '#6a4a2a'); for (let k = 0; k < 6; k++) { const a = k / 6 * Math.PI * 2 + Math.sin(t) * 0.05; g.fillStyle = '#2a6a3a'; g.beginPath(); g.ellipse(x + 70 + Math.cos(a) * 80, GY - 520 + Math.sin(a) * 30 + 20, 110, 24, a, 0, 7); g.fill(); } } });
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, ['#f2d8a0', '#c8a870']); g.fillRect(-E.W, GY, E.W * 3, E.H * 2); });
  return { GY, CX, M };
}
export function space(g, t, cam, o = {}) {
  const M = mood('void'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.02, (g) => { backdrop(g, ['#05060f', '#0e1030', '#1a1040']); FX.stars(g, t, { count: 260, area: [-E.W, -E.H, E.W * 3, E.H * 3], color: '#e8ecff' }); glow(g, CX - 600, 200, 700, '#7a4ad0', 0.25); glow(g, CX + 700, 700, 600, '#3a6ad0', 0.2); });
  layer(g, cam, 0.15, (g) => { const px = CX + V(560, 250), py = V(260, 420); circle(g, px, py, V(150, 120), '#e0a050'); g.save(); g.translate(px, py); g.rotate(-0.3); g.strokeStyle = '#f2d9a8'; g.lineWidth = 14; g.beginPath(); g.ellipse(0, 0, V(260, 210), 50, 0, 0.1, Math.PI - 0.1); g.stroke(); g.restore(); });
  layer(g, cam, 0.5, (g) => { const ey = GY + V(380, 600); g.fillStyle = radGrad(g, CX, ey + 1400, 1300, 1500, ['#3a8ad0', '#1a4a90', alpha('#6ab0ff', 0)]); g.beginPath(); g.arc(CX, ey + 1400, 1500, 0, 7); g.fill(); circle(g, CX, ey + 1400, 1400, '#2a6ab0'); for (const [x, w] of [[-300, 260], [200, 340], [600, 200]]) { g.fillStyle = '#4a9a5a'; g.beginPath(); g.ellipse(CX + x, ey + 60, w, 50, 0, 0, 7); g.fill(); } });
  return { GY, CX, M, air: true };
}
export function mountain(g, t, cam, o = {}) {
  const M = mood(o.mood || 'golden'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.08, (g) => { backdrop(g, M.sky); FX.sun(g, CX - V(500, 200), GY - V(560, 900), 70, '#fff3dc', M.key, 4); FX.clouds(g, { y: GY - V(600, 1000), h: 160, color: '#fff', a: 0.25, seed: 9 }); });
  layer(g, cam, 0.25, (g) => { for (const [x, h, c] of [[-400, 620, '#8a6a8a'], [300, 760, '#7a5a7a'], [1100, 680, '#8a6a8a'], [1900, 720, '#7a5a7a']]) { poly(g, [[x - 520, GY], [x, GY - V(h, h * 1.2)], [x + 520, GY]], c); poly(g, [[x - 110, GY - V(h, h * 1.2) + 130], [x, GY - V(h, h * 1.2)], [x + 110, GY - V(h, h * 1.2) + 130], [x + 30, GY - V(h, h * 1.2) + 100]], '#f6f2f8'); } });
  layer(g, cam, 0.55, (g) => { for (const [x, h] of [[-200, 380], [700, 460], [1500, 400]]) poly(g, [[x - 420, GY], [x - 60, GY - h], [x + 80, GY - h + 30], [x + 420, GY]], '#b0603a'); for (let x = -800; x < 2800; x += 140) FX.pine(g, x, GY + 10, 0.6 + 0.3 * Math.sin(x), '#2a3a2a'); });
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, ['#a0603a', '#5a3020']); g.fillRect(-E.W, GY, E.W * 3, E.H * 2); });
  return { GY, CX, M, fx: (g, t) => FX.dust(g, t, { count: 20, color: '#ffe0b0', a: 0.3 }) };
}
export function forest(g, t, cam, o = {}) {
  const M = mood(o.mood || 'day'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.08, (g) => { backdrop(g, ['#6a9ac0', '#b8d8c0', '#e8ecc8']); });
  layer(g, cam, 0.3, (g) => { for (let x = -900; x < 2900; x += 110) FX.pine(g, x, GY - 60, 1.4 + 0.4 * Math.sin(x * 3), '#4a7a5a'); });
  layer(g, cam, 0.55, (g) => { for (let x = -900; x < 2900; x += 260) FX.tree(g, x, GY - 10, 2.0 + 0.5 * Math.sin(x), '#2a5a3a'); FX.godRays(g, CX, -200, { count: 10, angle: Math.PI / 2, spread: 0.8, len: 1600, a: 0.05, t }); });
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, ['#5a8a3a', '#2a4a1a']); g.fillRect(-E.W, GY, E.W * 3, E.H * 2); for (let x = -E.W; x < E.W * 2; x += 40) seg(g, [[x, GY + 6], [x + 6, GY - 14]], 4, '#4a7a2a'); });
  return { GY, CX, M, fx: (g, t) => { for (let k = 0; k < 14; k++) { const x = (k * 151 + t * 30) % E.W, y = (k * 97 + t * 50) % E.H; g.fillStyle = alpha('#e0a040', 0.6); g.beginPath(); g.ellipse(x, y, 8, 4, t + k, 0, 7); g.fill(); } } };
}
export function kitchen(g, t, cam, o = {}) {
  const M = mood('interiorWarm'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.35, (g) => {
    g.fillStyle = linGrad(g, 0, -E.H, 0, GY, ['#5a4a3a', '#c8b090']); g.fillRect(-E.W, -E.H, E.W * 3, GY + E.H);
    for (let y = GY - 420; y < GY - 140; y += 40) for (let x = -E.W + ((y / 40) % 2) * 20; x < E.W * 2; x += 40) { g.strokeStyle = 'rgba(255,255,255,.12)'; g.lineWidth = 2; g.strokeRect(x, y, 40, 40); }
    for (let k = -2; k <= 2; k++) { rr(g, CX + k * 300 - 120, GY - V(760, 1100), 240, 220, 10); g.fillStyle = '#8a5a3a'; g.fill(); circle(g, CX + k * 300 + 90, GY - V(650, 990), 8, '#e8d0a0'); }
    rr(g, CX + V(620, 300), GY - 620, 260, 620, 14); g.fillStyle = '#e8ecf0'; g.fill(); seg(g, [[CX + V(620, 300) + 30, GY - 500], [CX + V(620, 300) + 30, GY - 380]], 10, '#9aa0ae');
    FX.windowFrame(g, { x: CX - V(160, 140), y: GY - V(520, 760), w: 320, h: 220, cols: 2, frame: '#f2ece0', bar: 10 }, (g, x, y, w, h) => { g.fillStyle = linGrad(g, 0, y, 0, y + h, mood('day').sky); g.fillRect(x, y, w, h); });
  });
  layer(g, cam, 0.8, (g) => { FX.counter(g, { x: -E.W, y: GY, w: E.W * 3, h: 140, color: '#7a5030', top: '#e8dcc8', doors: 14 }); for (let k = 0; k < 3; k++) { const p = (t * 0.5 + k / 3) % 1; circle(g, CX - V(500, 300) + Math.sin(t * 2 + k) * 10, GY - 180 - p * 160, 18 + p * 20, alpha('#ffffff', 0.25 * (1 - p))); } rr(g, CX - V(560, 340), GY - 175, 120, 40, 10); g.fillStyle = '#2a2a36'; g.fill(); });
  floor(g, cam, M, GY, true, M.key);
  return { GY, CX, M };
}
export function office(g, t, cam, o = {}) {
  const M = mood('interiorCool'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.12, (g) => { backdrop(g, ['#1a2a5a', '#5a7ab0', '#a8c0e0']); FX.skyline(g, { x: -E.W, y: GY - 120, w: E.W * 3, minH: 200, maxH: V(700, 1000), color: '#2a3a6a', windowColor: alpha('#ffe8a0', 0.8), lit: 0.4, seed: 14 }); });
  layer(g, cam, 0.4, (g) => { g.fillStyle = alpha('#0a1020', 0.25); for (let x = -E.W; x < E.W * 2; x += 360) g.fillRect(x, -E.H, 26, E.H * 3); g.fillStyle = '#20263a'; g.fillRect(-E.W, -E.H, E.W * 3, V(120, 300)); });
  layer(g, cam, 0.8, (g) => { for (const x of [CX - V(600, 340), CX + V(600, 340)]) { rr(g, x - 200, GY - 150, 400, 24, 6); g.fillStyle = '#c8b090'; g.fill(); seg(g, [[x - 180, GY - 130], [x - 180, GY]], 8, '#3a3a46'); seg(g, [[x + 180, GY - 130], [x + 180, GY]], 8, '#3a3a46'); FX.screen(g, { x: x - 90, y: GY - 300, w: 180, h: 120, glowC: '#7fd0ff', a: 0.25 }, (g, X, Y, w, h) => { for (let i = 0; i < 4; i++) { g.fillStyle = alpha('#7fd0ff', 0.8); g.fillRect(X + 12, Y + 16 + i * 24, (w - 24) * ((Math.sin(t + i * 2 + x) + 1.4) / 2.4), 10); } }); } });
  floor(g, cam, M, GY, true, '#cbd6ff');
  return { GY, CX, M };
}
export function studio(g, t, cam, o = {}) {
  const M = mood('night'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.15, (g) => { backdrop(g, ['#10081a', '#2a1040', '#401a50']); for (let k = -3; k <= 3; k++) FX.lightCone(g, CX + k * 300, -100, { angle: Math.PI / 2 + Math.sin(t * 0.8 + k) * 0.35, spread: 0.22, len: 1400, color: ['#ff5a8a', '#5ab0ff', '#ffd25a'][(k + 3) % 3], a: 0.12 }); });
  layer(g, cam, 0.4, (g) => { FX.screen(g, { x: CX - V(420, 300), y: GY - V(720, 1100), w: V(840, 600), h: V(380, 340), glowC: '#5ab0ff', a: 0.3 }, (g, x, y, w, h) => { g.fillStyle = linGrad(g, x, y, x + w, y + h, ['#3a1a8a', '#d04a8a']); g.fillRect(x, y, w, h); text(g, 'LIVE', x + 70, y + 40, { size: 34, color: '#fff', font: FONTS.ui, weight: 900 }); circle(g, x + 26, y + 40, 10, Math.sin(t * 6) > 0 ? '#ff3b3b' : '#6a1a1a'); text(g, 'RIO ANIMATION', x + w / 2, y + h / 2, { size: 54, color: '#fff', font: FONTS.title, weight: 700, alpha: 0.8 }); }); });
  layer(g, cam, 0.6, (g) => { FX.crowd(g, t, { y: GY + V(40, 80), x: -E.W, w: E.W * 3, rows: 3, rowH: 30, colors: ['#3a3358', '#5a3a4a', '#2a4a6a'], cheer: 0.8, size: 1.2 }); });
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, GY, 0, GY + 400, ['#2a1a3a', '#0a0610']); g.fillRect(-E.W, GY, E.W * 3, E.H * 2); FX.pool(g, CX, GY + 20, 500, 70, '#ffe0f0', 0.3); });
  return { GY, CX, M, fx: (g, t) => FX.dust(g, t, { count: 40, color: '#ffd0f0', a: 0.35 }) };
}
export function bedroom(g, t, cam, o = {}) {
  const M = mood('night'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.35, (g) => { g.fillStyle = linGrad(g, 0, -E.H, 0, GY, ['#141830', '#2a2c50']); g.fillRect(-E.W, -E.H, E.W * 3, GY + E.H);
    FX.windowFrame(g, { x: CX + V(200, -200), y: GY - V(640, 980), w: 360, h: 300, cols: 2, frame: '#0a0c1a', bar: 10 }, (g, x, y, w, h) => { g.fillStyle = linGrad(g, 0, y, 0, y + h, mood('night').sky); g.fillRect(x, y, w, h); FX.moon(g, x + w * 0.7, y + 80, 34); FX.stars(g, 0, { count: 20, area: [x, y, w, h] }); });
    FX.lightCone(g, CX + V(380, 0), GY - V(640, 980), { angle: Math.PI / 2 + 0.4, spread: 0.3, len: 900, color: '#bcd0ff', a: 0.1 });
    for (let k = 0; k < 5; k++) { const x = CX - V(700, 400) + k * 70; poly(g, [[x, GY - 600 - (k % 2) * 30], [x + 14, GY - 570 - (k % 2) * 30], [x, GY - 540 - (k % 2) * 30], [x - 14, GY - 570 - (k % 2) * 30]], alpha('#fff6a0', 0.5 + 0.4 * Math.sin(t * 2 + k))); } });
  layer(g, cam, 0.75, (g) => FX.bed(g, { x: CX - V(150, 220), y: GY, w: V(500, 420), color: '#4a4a9a', frame: '#1a1a2e', pillow: '#d8d8f4' }));
  floor(g, cam, M, GY, true, '#bcd0ff');
  return { GY, CX, M };
}
export function rooftop(g, t, cam, o = {}) {
  const M = mood('dusk'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.06, (g) => { backdrop(g, M.sky); FX.sun(g, CX - V(400, 200), GY - V(360, 700), 80, '#fff3dc', M.key, 5); });
  layer(g, cam, 0.25, (g) => FX.skyline(g, { x: -E.W, y: GY + 120, w: E.W * 3, minH: 200, maxH: V(700, 1000), color: '#3a2a4a', windowColor: alpha(M.practical, 0.8), lit: 0.3, seed: 31 }));
  layer(g, cam, 0.6, (g) => { rr(g, CX + V(500, 260), GY - 280, 200, 220, 10); g.fillStyle = '#5a4a5a'; g.fill(); for (let k = 0; k < 4; k++) seg(g, [[CX + V(520, 280) + k * 45, GY - 280], [CX + V(520, 280) + k * 45, GY - 380]], 6, '#3a2a3a'); seg(g, [[-E.W, GY - 90], [E.W * 2, GY - 90]], 6, '#2a1a2a'); for (let x = -E.W; x < E.W * 2; x += 80) seg(g, [[x, GY - 90], [x, GY]], 5, '#2a1a2a'); });
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, ['#4a3a4a', '#1a101a']); g.fillRect(-E.W, GY, E.W * 3, E.H * 2); });
  return { GY, CX, M, fx: (g, t) => FX.dust(g, t, { count: 24, color: '#ffd0a0', a: 0.3 }) };
}
export function museum(g, t, cam, o = {}) {
  const M = mood('interiorWarm'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.35, (g) => { g.fillStyle = linGrad(g, 0, -E.H, 0, GY, ['#2a2030', '#6a5a5a']); g.fillRect(-E.W, -E.H, E.W * 3, GY + E.H);
    for (let k = -3; k <= 3; k++) { const x = CX + k * 420; rr(g, x - 50, GY - V(720, 1100), 100, V(720, 1100), 8); g.fillStyle = '#d8ccb8'; g.fill(); if (k % 2) { rr(g, x + 110, GY - V(560, 900), 190, 150, 6); g.fillStyle = '#b8902a'; g.fill(); rr(g, x + 122, GY - V(548, 888), 166, 126, 4); g.fillStyle = ['#4a6a9a', '#9a4a5a', '#5a8a4a'][(k + 3) % 3]; g.fill(); } }
    for (const x of [CX - V(600, 340), CX + V(600, 340)]) FX.lightCone(g, x, -50, { angle: Math.PI / 2, spread: 0.25, len: 1200, color: '#fff0d0', a: 0.12 }); });
  layer(g, cam, 0.75, (g) => { rr(g, CX - 110, GY - 220, 220, 220, 6); g.fillStyle = '#e8e0d0'; g.fill(); rr(g, CX - 90, GY - 420, 180, 200, 8); g.fillStyle = alpha('#dff4ff', 0.25); g.fill(); g.strokeStyle = alpha('#fff', 0.6); g.lineWidth = 3; g.stroke(); const s = 34; poly(g, [[CX - s, GY - 320], [CX - s * 0.6, GY - 345], [CX + s * 0.6, GY - 345], [CX + s, GY - 320], [CX, GY - 270]], '#9fe8ff'); glow(g, CX, GY - 320, 120, '#bff0ff', 0.4 + 0.2 * Math.sin(t * 3)); });
  floor(g, cam, M, GY, true, '#fff0d0');
  return { GY, CX, M };
}
export function snowy(g, t, cam, o = {}) {
  const M = mood('day'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.08, (g) => backdrop(g, ['#8a9ab8', '#c8d4e4', '#eef2f8']));
  layer(g, cam, 0.3, (g) => { FX.hills(g, { y: GY - V(160, 260), amp: 180, color: '#dfe8f4', seed: 4 }); for (let x = -900; x < 2900; x += 180) FX.pine(g, x, GY - 80, 1.1, '#3a5a5a'); });
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, ['#f6f8fc', '#c8d4e4']); g.fillRect(-E.W, GY, E.W * 3, E.H * 2); });
  return { GY, CX, M, fx: (g, t) => FX.snow(g, t, { count: 160 }) };
}
export function desert(g, t, cam, o = {}) {
  const M = mood('golden'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.06, (g) => { backdrop(g, ['#f0a060', '#f8d090', '#fff0c8']); FX.sun(g, CX + V(500, 200), GY - V(560, 900), 100, '#fffbe8', '#ffe0a0', 5); });
  layer(g, cam, 0.3, (g) => { FX.hills(g, { y: GY - V(120, 200), amp: 120, color: '#e0a060', seed: 6 }); for (const x of [CX - V(700, 360), CX + V(300, 200)]) { rr(g, x - 20, GY - 260, 40, 260, 20); g.fillStyle = '#4a8a4a'; g.fill(); rr(g, x - 80, GY - 180, 30, 100, 15); g.fill(); rr(g, x + 50, GY - 210, 30, 110, 15); g.fill(); } });
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, ['#f0c070', '#c08040']); g.fillRect(-E.W, GY, E.W * 3, E.H * 2); });
  return { GY, CX, M, fx: (g, t) => FX.dust(g, t, { count: 30, color: '#fff0c0', a: 0.4 }) };
}
export function gym(g, t, cam, o = {}) {
  const M = mood('interiorCool'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.35, (g) => { g.fillStyle = linGrad(g, 0, -E.H, 0, GY, ['#1a1a2a', '#3a3a50']); g.fillRect(-E.W, -E.H, E.W * 3, GY + E.H); text(g, 'NO PAIN NO GAIN', CX, GY - V(620, 980), { size: 60, color: alpha('#ffd25a', 0.5), font: FONTS.ui, weight: 900, spacing: 8 }); for (let x = -E.W; x < E.W * 2; x += 300) { rr(g, x, GY - V(520, 860), 200, 300, 6); g.fillStyle = alpha('#bfe6ff', 0.15); g.fill(); } });
  layer(g, cam, 0.75, (g) => { for (const x of [CX - V(620, 360), CX + V(620, 360)]) { seg(g, [[x - 140, GY - 160], [x + 140, GY - 160]], 12, '#9aa0ae'); for (const s of [-1, 1]) { rr(g, x + s * 140 - 18, GY - 220, 36, 120, 8); g.fillStyle = '#2a2a36'; g.fill(); } seg(g, [[x - 100, GY - 160], [x - 100, GY]], 10, '#3a3a46'); seg(g, [[x + 100, GY - 160], [x + 100, GY]], 10, '#3a3a46'); } });
  floor(g, cam, M, GY, true, '#cbd6ff');
  return { GY, CX, M };
}
export function store(g, t, cam, o = {}) {
  const M = mood('interiorWarm'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.35, (g) => { g.fillStyle = linGrad(g, 0, -E.H, 0, GY, ['#e8e0d0', '#c8c0b0']); g.fillRect(-E.W, -E.H, E.W * 3, GY + E.H); for (let x = -E.W; x < E.W * 2; x += 420) { for (let r = 0; r < 4; r++) { g.fillStyle = '#7a6a5a'; g.fillRect(x, GY - 120 - r * 140, 360, 12); for (let k = 0; k < 8; k++) { rr(g, x + 10 + k * 44, GY - 120 - r * 140 - 70, 36, 70, 4); g.fillStyle = ['#e0443a', '#f2c21a', '#3a8ae0', '#5ab04a', '#e06aa0'][(k + r + x / 420) % 5 | 0]; g.fill(); } } } });
  floor(g, cam, M, GY, true, M.key);
  return { GY, CX, M };
}
export function poolside(g, t, cam, o = {}) {
  const M = mood('day'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.08, (g) => { backdrop(g, ['#5aa0e0', '#a8d4f2', '#e8f4fa']); FX.sun(g, CX + V(600, 300), GY - V(620, 1000), 60, '#fffbe8', '#fff3dc', 4); });
  layer(g, cam, 0.4, (g) => { g.fillStyle = '#e8e0d0'; g.fillRect(-E.W, GY - V(220, 300), E.W * 3, V(220, 300)); for (let x = -E.W; x < E.W * 2; x += 60) seg(g, [[x, GY - V(220, 300)], [x, GY]], 2, 'rgba(0,0,0,.08)'); });
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, ['#5ad0e8', '#1a8ab0']); g.fillRect(-E.W, GY, E.W * 3, E.H * 2); for (let k = 0; k < 30; k++) { const x = (k * 137) % (E.W * 2) - E.W / 2, y = GY + 30 + (k * 53) % 300; g.strokeStyle = alpha('#ffffff', 0.35); g.lineWidth = 3; g.beginPath(); g.ellipse(x + Math.sin(t + k) * 20, y, 50, 10, 0, 0, Math.PI); g.stroke(); } });
  return { GY, CX, M, water: true };
}
export function lake(g, t, cam, o = {}) {
  const M = mood('golden'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.06, (g) => { backdrop(g, M.sky); FX.sun(g, CX, GY - V(300, 600), 90, '#fff3dc', M.key, 5); });
  layer(g, cam, 0.3, (g) => { FX.hills(g, { y: GY - V(140, 240), amp: 140, color: '#5a4a6a', seed: 12 }); for (let x = -900; x < 2900; x += 120) FX.pine(g, x, GY - 100, 0.9, '#2a2a3a'); });
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, GY - 100, 0, GY + 500, ['#e8a070', '#5a4a7a', '#2a2a4a']); g.fillRect(-E.W, GY - 100, E.W * 3, E.H * 2); for (let k = 0; k < 12; k++) { const y = GY - 80 + k * 30; seg(g, [[CX - 200 + Math.sin(t * 2 + k) * 40, y], [CX + 200 + Math.sin(t * 2 + k) * 40, y]], 4, alpha('#fff3dc', 0.4 - k * 0.03)); } rr(g, CX + V(300, 100), GY - 40, 700, 40, 6); g.fillStyle = '#6a4a2a'; g.fill(); });
  return { GY, CX, M, water: true };
}
export function library(g, t, cam, o = {}) {
  const M = mood('interiorWarm'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.35, (g) => { g.fillStyle = linGrad(g, 0, -E.H, 0, GY, ['#2a1a1a', '#5a3a2a']); g.fillRect(-E.W, -E.H, E.W * 3, GY + E.H); for (let r = 0; r < 7; r++) { g.fillStyle = '#3a2418'; g.fillRect(-E.W, GY - 60 - r * 130, E.W * 3, 14); for (let x = -E.W; x < E.W * 2; x += 34) { const h = 80 + ((x * 7 + r * 13) % 30); g.fillStyle = ['#8a3a2a', '#2a4a6a', '#4a6a3a', '#8a6a2a', '#5a3a6a'][(x / 34 + r) % 5 | 0]; g.fillRect(x, GY - 60 - r * 130 - h, 28, h); } } });
  layer(g, cam, 0.8, (g) => { rr(g, CX - 300, GY - 140, 600, 24, 6); g.fillStyle = '#7a5030'; g.fill(); const lx = CX + 200; seg(g, [[lx, GY - 140], [lx, GY - 260], [lx - 40, GY - 300]], 6, '#2a6a3a'); glow(g, lx - 40, GY - 290, 240, '#ffe0a0', 0.5); });
  floor(g, cam, M, GY, true, M.key);
  return { GY, CX, M };
}
export function highway(g, t, cam, o = {}) {
  const M = mood('dusk'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.06, (g) => { backdrop(g, M.sky); FX.sun(g, CX + V(300, 100), GY - V(300, 600), 80, '#fff3dc', M.key, 5); });
  layer(g, cam, 0.3, (g) => FX.hills(g, { y: GY - V(80, 160), amp: 100, color: '#4a3a5a', seed: 5 }));
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, ['#4a4458', '#1a1622']); g.fillRect(-E.W, GY, E.W * 3, E.H * 2); const off = (t * 900) % 300; for (let x = -E.W - off; x < E.W * 2; x += 300) { g.fillStyle = '#f2e6c8'; g.fillRect(x, GY + V(150, 240), 150, 10); } for (let x = -E.W + ((t * 200) % 200); x < E.W * 2; x += 200) seg(g, [[x, GY], [x, GY - 60]], 6, '#9aa0ae'); seg(g, [[-E.W, GY - 50], [E.W * 2, GY - 50]], 6, '#9aa0ae'); });
  return { GY, CX, M, fx: (g, t) => FX.speedLines(g, t, { count: 20, a: 0.06, inner: 600 }) };
}
export function canyon(g, t, cam, o = {}) {
  const M = mood('golden'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.05, (g) => { backdrop(g, ['#4a7ac8', '#e8a878', '#ffd8a8']); FX.sun(g, CX - V(520, 220), GY - V(560, 980), 70, '#fff3dc', '#ffcf8f', 4); FX.clouds(g, { y: GY - V(700, 1150), h: 140, color: '#fff', a: 0.25, seed: 13 }); });
  const mesa = (x, w, h, col, seed) => { const r = rng(seed), top = GY - h; const pts = [[x - w / 2 - 40, GY + 20]]; let yy = top; for (let i = 0; i <= 8; i++) { yy = top + (r() - 0.5) * 30; pts.push([x - w / 2 + i * w / 8 + (i === 0 ? 30 : 0) - (i === 8 ? 30 : 0), yy]); } pts.push([x + w / 2 + 40, GY + 20]); poly(g, pts, col); for (let k = 1; k < 7; k++) { g.fillStyle = alpha(k % 2 ? '#7a3018' : '#f0b080', 0.18); g.fillRect(x - w / 2, top + k * h / 7, w, h / 14); } };
  layer(g, cam, 0.2, (g) => { for (const [x, w, h, s] of [[-500, 700, 420, 1], [500, 520, 520, 2], [1500, 760, 460, 3], [2400, 600, 500, 4]]) mesa(x, w, V(h, h * 1.3), '#c88a68', s); });
  layer(g, cam, 0.45, (g) => { for (const [x, w, h, s] of [[-200, 560, 300, 5], [CX + V(640, 360), 500, 360, 6], [1900, 640, 320, 7]]) mesa(x, w, V(h, h * 1.3), '#b0582e', s); g.fillStyle = linGrad(g, 0, GY - 40, 0, GY + 40, ['#5ab0d8', '#2a6a98']); g.fillRect(-E.W, GY - 30, E.W * 3, 60); for (let k = 0; k < 10; k++) { const x = ((k * 260 + t * 60) % 2800) - 600; seg(g, [[x, GY - 6], [x + 70, GY - 6]], 3, alpha('#e8f8ff', 0.6)); } });
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, ['#d07a40', '#6a3018']); g.beginPath(); g.moveTo(-E.W, GY + 10); for (let x = -E.W; x <= E.W * 2; x += 80) g.lineTo(x, GY + 10 + Math.sin(x * 0.03) * 8); g.lineTo(E.W * 2, E.H * 2); g.lineTo(-E.W, E.H * 2); g.fill(); for (const [x, s] of [[CX - V(760, 400), 1], [CX + V(820, 420), 1.3]]) { poly(g, [[x - 60 * s, GY + 14], [x - 20 * s, GY - 50 * s], [x + 50 * s, GY - 30 * s], [x + 70 * s, GY + 14]], '#8a4a28'); } });
  return { GY, CX, M, fx: (g, t) => FX.dust(g, t, { count: 24, color: '#ffe0b0', a: 0.35 }) };
}
export function city(g, t, cam, o = {}) {
  const M = mood('day'), GY = ground(), CX = E.W / 2;
  layer(g, cam, 0.06, (g) => { backdrop(g, M.sky); FX.clouds(g, { y: GY - V(700, 1150), h: 200, color: '#fff', a: 0.35, seed: 6 }); });
  layer(g, cam, 0.3, (g) => FX.skyline(g, { x: -E.W, y: GY - 40, w: E.W * 3, minH: 200, maxH: V(700, 1100), color: '#7a88a8', windowColor: alpha('#dff0ff', 0.8), lit: 0.5, seed: 19 }));
  layer(g, cam, 0.6, (g) => { FX.skyline(g, { x: -E.W, y: GY, w: E.W * 3, minH: 200, maxH: V(450, 700), minW: 140, maxW: 280, color: '#4a5878', windowColor: alpha('#fff2c0', 0.9), lit: 0.4, seed: 23 }); for (let k = 0; k < 4; k++) { const x = ((t * 160 + k * 700) % 3600) - 900; rr(g, x, GY - 70, 180, 60, 16); g.fillStyle = ['#e0443a', '#f2c21a', '#3a8ae0', '#5ab04a'][k]; g.fill(); circle(g, x + 40, GY - 8, 18, '#1a1a22'); circle(g, x + 140, GY - 8, 18, '#1a1a22'); } });
  layer(g, cam, 0.92, (g) => { g.fillStyle = linGrad(g, 0, GY, 0, GY + 500, ['#8a8a96', '#4a4a56']); g.fillRect(-E.W, GY, E.W * 3, E.H * 2); for (let x = -E.W; x < E.W * 2; x += 120) { g.fillStyle = alpha('#fff', 0.5); g.fillRect(x, GY + V(160, 260), 70, 30); } });
  return { GY, CX, M };
}

export const SETS = { street, home, hospital, stadium, park, classroom, cafe, lab, sky, ocean, beach, space, mountain, forest, kitchen, office, studio, bedroom, rooftop, museum, snowy, desert, gym, store, poolside, lake, library, highway, canyon, city };
export function drawSet(name, g, t, cam) { return (SETS[name] || street)(g, t, cam); }
