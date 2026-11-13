// Một "sân khấu" 3D: dựng đúng một bối cảnh + các nhân vật cần dùng, chạy danh sách cảnh quay (camera, nhân vật, màn hình) theo khung hình.
import React, { useEffect, useMemo } from "react";
import * as THREE from "three";
import { useCurrentFrame } from "remotion";
import { ThreeCanvas } from "@remotion/three";
import { useThree } from "@react-three/fiber";
import { EffectComposer } from "@react-three/postprocessing";
import { BlendFunction, BloomEffect, ToneMappingEffect, ToneMappingMode } from "postprocessing";
import { InkPass, noInkFallback, NOINK } from "../pho/ink";
import { GradeEffect } from "../pho/grade";
import { Actor, Pose, DO, NGAN, VEST, CLERK, ME2, crowd } from "./cast2";
import { buildRoom, buildStreet, buildShop, buildHue, buildBenThanh, buildHoGuom, buildVilla, rainStreaks, RX, SX, IX, HX, BX, GX, VX, Screen } from "./sets";
import { applyLight, GR, LK, L } from "./look";
import { F } from "./cards";
import { buildExtras } from "./extras";

export type V = [number, number, number];
export type SetKey = "room" | "street" | "streetday" | "shop" | "hue" | "bt" | "lake" | "villa";
export const OFF: Record<SetKey, number> = { room: RX, street: SX, streetday: SX, shop: IX, hue: HX, bt: BX, lake: GX, villa: VX };
export type Cast = { a: string; p: V; to?: V; pose: (t: number, d: number) => Pose };
export type Shot3D = { set: SetKey; light: LK; from: [V, V, number]; to: [V, V, number]; cast: Cast[]; rain?: boolean; shake?: number; chat?: "calm" | "fast" | "off" | "boom"; game?: boolean; board?: "buy" | "sell"; ease?: "sm" | "lin" | "out"; walkers?: boolean; jam?: boolean };
export type Run = { a: number; b: number; s: Shot3D }; // frames, relative to the Stage sequence

const sm = (t: number) => { t = Math.max(0, Math.min(1, t)); return t * t * t * (t * (t * 6 - 15) + 10); };
const outE = (t: number) => 1 - (1 - Math.max(0, Math.min(1, t))) ** 3;
const lerpV = (a: V, b: V, t: number) => new THREE.Vector3(a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t);

const NAMES = ["minh_anh92", "Hùng Xe Ôm", "bé Na", "TuấnGaming", "chị Hoa", "LongVũ", "Phúc 2k", "ThảoMy", "Quang Trần", "Đạt Lửa", "Hải Béo", "Yến Nhi"];
const CALM = ["anh ơi bắn đi", "kkk", "đỉnh quá anh", "lương 7 triệu =))", "hello anh Tân", "anh ăn tối chưa", "GG", "bo hết đạn rồi"];
const FAST = ["ANH ƠI SAO IM THẾ", "???", "anh ơi", "lag à", "anh Tân ơi", "alo alo", "sao đứng hình vậy", "anh ổn không"];
const BOOM = ["ĐỈNH QUÁ ANH ƠI", "mai em mua có kịp không anh??", "anh chỉ em mua với", "giàu rồi bỏ live à", "vàng lên tiếp không anh", "🔥🔥🔥", "em đi xếp hàng luôn", "lương 7 triệu mà lãi chục triệu =))"];
function drawChat(s: Screen, t: number, mode: "calm" | "fast" | "off" | "boom") {
  const g = s.g, W = s.c.width, H = s.c.height; g.fillStyle = mode === "off" ? "#050507" : "#12131c"; g.fillRect(0, 0, W, H); if (mode === "off") { s.t.needsUpdate = true; return; }
  g.fillStyle = "#e62117"; g.fillRect(0, 0, W, 34); g.fillStyle = "#fff"; g.font = `800 20px ${F}`; g.fillText("TRÒ CHUYỆN TRỰC TIẾP", 12, 24);
  const rate = mode === "calm" ? 1.4 : mode === "fast" ? 7 : 9, n = Math.floor(t * rate), L = mode === "calm" ? CALM : mode === "fast" ? FAST : BOOM, lh = 30;
  for (let i = 0; i < 9; i++) { const k = n - i; if (k < 0) break; const y = H - 18 - i * lh; const nm = NAMES[(k * 7) % NAMES.length], tx = L[(k * 5 + 3) % L.length];
    g.font = `700 19px ${F}`; g.fillStyle = ["#7fc8ff", "#ffcf5a", "#9dff9a", "#ff9ad5"][k % 4]; g.fillText(nm, 10, y); const w = g.measureText(nm + " ").width; g.font = `600 19px ${F}`; g.fillStyle = "#f1f1f5"; g.fillText(tx, 10 + w, y, W - w - 16); }
  s.t.needsUpdate = true;
}
function drawGame(s: Screen, t: number, on: boolean) {
  const g = s.g, W = s.c.width, H = s.c.height;
  if (!on) { g.fillStyle = "#050507"; g.fillRect(0, 0, W, H); s.t.needsUpdate = true; return; }
  const sky = g.createLinearGradient(0, 0, 0, H); sky.addColorStop(0, "#ff8a3d"); sky.addColorStop(1, "#ffd27a"); g.fillStyle = sky; g.fillRect(0, 0, W, H);
  g.fillStyle = "#2f7a4a"; g.beginPath(); g.moveTo(0, H * 0.7); for (let x = 0; x <= W; x += 20) g.lineTo(x, H * 0.62 + Math.sin(x * 0.02 + t * 0.3) * 14); g.lineTo(W, H); g.lineTo(0, H); g.fill();
  for (let i = 0; i < 6; i++) { const x = ((i * 97 + t * 40) % (W + 60)) - 30; g.fillStyle = "#1e4f33"; g.beginPath(); g.moveTo(x, H * 0.66); g.lineTo(x + 20, H * 0.5); g.lineTo(x + 40, H * 0.66); g.fill(); }
  g.fillStyle = "#222"; g.fillRect(W / 2 - 14, H * 0.6, 28, 46); g.fillStyle = "#f3cfa8"; g.beginPath(); g.arc(W / 2, H * 0.58, 13, 0, 7); g.fill();
  g.strokeStyle = "rgba(255,255,255,.9)"; g.lineWidth = 3; g.beginPath(); g.arc(W / 2, H / 2 - 20, 16, 0, 7); g.moveTo(W / 2 - 26, H / 2 - 20); g.lineTo(W / 2 + 26, H / 2 - 20); g.stroke();
  g.fillStyle = "rgba(0,0,0,.55)"; g.fillRect(W - 210, 12, 196, 40); g.fillStyle = "#fff"; g.font = `800 22px ${F}`; g.fillText(`CÒN ${Math.max(2, 23 - Math.floor(t / 4))} NGƯỜI`, W - 198, 40);
  g.fillStyle = "#ff3b30"; g.font = `900 26px ${F}`; g.fillText("LỬA CHÙA", 14, 38);
  s.t.needsUpdate = true;
}
function drawBoard(s: Screen, mode: "buy" | "sell") {
  const g = s.g, W = s.c.width, H = s.c.height; g.fillStyle = "#07090f"; g.fillRect(0, 0, W, H); g.strokeStyle = "#f5c518"; g.lineWidth = 6; g.strokeRect(6, 6, W - 12, H - 12);
  g.fillStyle = "#f5c518"; g.font = `900 44px ${F}`; g.textAlign = "center"; g.fillText(mode === "buy" ? "BẢNG GIÁ 26/02/2026" : "BẢNG GIÁ 13/11/2026", W / 2, 62);
  g.font = `700 30px ${F}`; g.fillStyle = "#9fb0c8"; g.fillText("nghìn đồng/lượng", W / 2, 100);
  g.textAlign = "left"; g.font = `800 40px ${F}`; g.fillStyle = "#fff"; g.fillText("NHẪN TRÒN 9999", 40, 180);
  g.font = `700 30px ${F}`; g.fillStyle = "#9fb0c8"; g.fillText("MUA VÀO", 40, 250); g.fillText("BÁN RA", 480, 250);
  g.font = `900 64px ${F}`; g.fillStyle = mode === "sell" ? "#ff4d5e" : "#e9eef5"; g.fillText(mode === "buy" ? "180.800" : "133.800", 40, 325);
  g.fillStyle = mode === "buy" ? "#2bd17e" : "#e9eef5"; g.fillText(mode === "buy" ? "184.000" : "137.800", 480, 325);
  s.t.needsUpdate = true;
}

const Inner: React.FC<{ set: SetKey; runs: Run[] }> = ({ set, runs }) => {
  const f = useCurrentFrame(), { camera, scene } = useThree();
  const W = useMemo(() => {
    const root = new THREE.Group();
    const sun = new THREE.DirectionalLight("#ffffff", 2.8); sun.castShadow = true; sun.shadow.mapSize.set(2048, 2048);
    const scm = sun.shadow.camera as THREE.OrthographicCamera; scm.left = -26; scm.right = 26; scm.top = 26; scm.bottom = -26; scm.near = 1; scm.far = 200; sun.shadow.bias = -0.0004; sun.shadow.normalBias = 0.02;
    root.add(sun, sun.target, new THREE.HemisphereLight("#dcecff", "#b49a78", 0.4));
    const skyMat = new THREE.ShaderMaterial({ side: THREE.BackSide, depthWrite: false, uniforms: { top: { value: new THREE.Color() }, hor: { value: new THREE.Color() } },
      vertexShader: "varying vec3 p; void main(){ p = normalize(position); gl_Position = projectionMatrix*modelViewMatrix*vec4(position,1.0);}",
      fragmentShader: "uniform vec3 top; uniform vec3 hor; varying vec3 p; void main(){ float t = smoothstep(-0.05, 0.6, p.y); gl_FragColor = vec4(mix(hor, top, t), 1.0); }" });
    const sky = new THREE.Mesh(new THREE.SphereGeometry(380, 32, 16), skyMat); sky.layers.set(NOINK); root.add(sky);
    let room: ReturnType<typeof buildRoom> | null = null, shop: ReturnType<typeof buildShop> | null = null, bike: THREE.Group | null = null;
    if (set === "room") { room = buildRoom(); root.add(room.g); }
    else if (set === "street" || set === "streetday") { const st = buildStreet(set === "street"); root.add(st.g); bike = st.bikeDo; }
    else if (set === "shop") { shop = buildShop(); root.add(shop.g); }
    else if (set === "hue") root.add(buildHue().g);
    else if (set === "bt") root.add(buildBenThanh().g);
    else if (set === "villa") { const v = buildVilla(); root.add(v.g); bike = v.hero; }
    else root.add(buildHoGuom().g);
    const rain = rainStreaks(); root.add(rain.m);
    const keys = new Set<string>(); runs.forEach((r) => r.s.cast.forEach((c) => keys.add(c.a)));
    const actors: Record<string, Actor> = {};
    keys.delete("bike"); keys.delete("boat");
    for (const k of keys) {
      const o = k === "tan" ? DO : k === "ngan" ? NGAN : k === "vest" ? VEST : k === "clerk" ? CLERK : k === "me" ? ME2 : crowd(parseInt(k.slice(1)) || 0);
      const h = k === "tan" ? 1.7 : k === "ngan" ? 1.58 : k === "vest" ? 1.76 : k === "me" ? 1.48 : 1.55 + ((parseInt(k.slice(1)) || 0) % 5) * 0.05;
      const a = new Actor(o, h, k === "tan" ? 3 : k === "ngan" ? 9 : 5 + (parseInt(k.slice(1)) || 0) * 3); actors[k] = a; root.add(a.root); a.root.visible = false;
    }
    const extras = buildExtras(set, root);
    noInkFallback(root);
    return { extras, root, sun, skyMat, sky, room, shop, rain, actors, bike, bike0: bike ? bike.position.clone() : null };
  }, [set]);
  const fx = useMemo(() => ({
    ink: new InkPass(scene, camera as THREE.PerspectiveCamera),
    bloom: new BloomEffect({ blendFunction: BlendFunction.ADD, intensity: 0.7, luminanceThreshold: 1.0, luminanceSmoothing: 0.2, mipmapBlur: true, levels: 5, radius: 0.65 }),
    tone: new ToneMappingEffect({ mode: ToneMappingMode.NEUTRAL }),
    grade: new GradeEffect(GR.day, 1),
  }), [camera, scene]);
  useEffect(() => () => { const k = fx.ink as unknown as { dispose?: () => void }; if (typeof k.dispose === "function") k.dispose(); }, [fx]);
  const run = runs.find((r) => f >= r.a && f < r.b) ?? runs[runs.length - 1];
  const s = run.s, X = OFF[set], d = (run.b - run.a) / 30, t = (f - run.a) / 30, u = s.ease === "lin" ? Math.min(1, t / d) : s.ease === "out" ? outE(t / d) : sm(t / d);
  const cam = camera as THREE.PerspectiveCamera;
  const pos = lerpV(s.from[0], s.to[0], u).add(new THREE.Vector3(X, 0, 0)), look = lerpV(s.from[1], s.to[1], u).add(new THREE.Vector3(X, 0, 0));
  if (s.shake) { const k = s.shake; pos.x += Math.sin(f * 0.13) * 0.02 * k + Math.sin(f * 0.31) * 0.01 * k; pos.y += Math.sin(f * 0.17 + 1) * 0.015 * k; look.x += Math.sin(f * 0.09 + 2) * 0.02 * k; }
  let fov = s.from[2] + (s.to[2] - s.from[2]) * u; fov *= 1 + 0.05 * (1 - sm((f - run.a) / 10));
  cam.position.copy(pos); cam.lookAt(look); cam.fov = fov; cam.aspect = 16 / 9; cam.near = 0.05; cam.far = 800; cam.updateProjectionMatrix();
  W.sky.position.copy(pos);
  applyLight(s.light, W.sun, pos, W.skyMat);
  const tag = fx.grade as unknown as { _k?: string }; if (tag._k !== s.light) { fx.grade.set(GR[s.light]); tag._k = s.light; }
  W.rain.update(f / 30, pos, !!s.rain);
  if (W.room) { drawChat(W.room.chat, t, s.chat ?? "calm"); drawGame(W.room.game, f / 30, s.game ?? true); }
  if (W.shop) drawBoard(W.shop.board, s.board ?? "buy");
  const tint = new THREE.Color(L[s.light].tint);
  W.extras(f / 30, cam, tint, !!s.jam);
  for (const a of Object.values(W.actors)) a.root.visible = false;
  if (W.bike && W.bike0) W.bike.position.copy(W.bike0);
  for (const c of s.cast) { if ((c.a === "bike" || c.a === "boat") && W.bike) { const p = c.to ? lerpV(c.p, c.to, Math.min(1, t / d)) : new THREE.Vector3(...c.p); W.bike.position.set(p.x, p.y, p.z); continue; }
    const a = W.actors[c.a]; if (!a) continue; a.root.visible = true; const p = c.to ? lerpV(c.p, c.to, Math.min(1, t / d)) : new THREE.Vector3(...c.p); a.root.position.set(p.x + X, p.y, p.z); a.pose(c.pose(t, d), cam, tint); }
  return (
    <>
      <primitive object={W.root} dispose={null} />
      <EffectComposer multisampling={0}>
        <primitive object={fx.ink} dispose={null} />
        <primitive object={fx.bloom} dispose={null} />
        <primitive object={fx.tone} dispose={null} />
        <primitive object={fx.grade} dispose={null} />
      </EffectComposer>
    </>
  );
};

export const Stage: React.FC<{ set: SetKey; runs: Run[] }> = ({ set, runs }) => (
  <div style={{ position: "absolute", left: 0, top: 0, width: 1280, height: 720, transform: "scale(1.5)", transformOrigin: "0 0" }}>
    <ThreeCanvas width={1280} height={720} shadows gl={{ antialias: false, stencil: false }} camera={{ fov: 40, near: 0.05, far: 800 }}>
      <Inner set={set} runs={runs} />
    </ThreeCanvas>
  </div>
);
