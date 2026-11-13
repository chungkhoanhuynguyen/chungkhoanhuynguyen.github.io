// Demo "Vì sao thật tệ khi là F0" – Vietnamese street in the toon-3D style. 16:9, 30 fps, 636 frames (21.2 s).
import React, { useEffect, useMemo } from "react";
import * as THREE from "three";
import { AbsoluteFill, useCurrentFrame, staticFile, Audio, getInputProps } from "remotion";
import { ThreeCanvas } from "@remotion/three";
import { useThree } from "@react-three/fiber";
import { EffectComposer } from "@react-three/postprocessing";
import { BlendFunction, BloomEffect, ToneMappingEffect, ToneMappingMode } from "postprocessing";
import { World } from "./world";
import { InkPass, noInkFallback } from "./ink";
import { LensBlur } from "./lensblur";
import { GradeEffect, GRADES, gradeFor } from "./grade";
import { drawChart } from "./paint";
import { Pose } from "./cast";

export const PHO_FRAMES = 636;
type V = [number, number, number];
type Shot = { a: number; b: number; light: "day" | "golden"; from: [V, V, number]; to: [V, V, number]; cInf: number; focus?: V | "phone" };
const T0: V = [0, 0.15, 5.0];
const SHOTS: Shot[] = [
  { a: 0, b: 40, light: "day", from: [[-26, 15, -1], [0, 3, 3], 50], to: [[-12, 8, 0], [0, 2, 4.5], 46], cInf: 0 },
  { a: 40, b: 110, light: "day", from: [[0.9, 1.2, 1.3], [0, 1.75, 5], 44], to: [[0.6, 1.2, 1.9], [0, 1.7, 5], 40], cInf: 10, focus: [0, 1.4, 5] },
  { a: 110, b: 211, light: "day", from: [[0.2, 1.55, 2.6], [0, 1.3, 5], 40], to: [[0.2, 1.55, 2.7], [0, 1.3, 5], 37], cInf: 14, focus: "phone" },
  { a: 211, b: 281, light: "day", from: [[-1.8, 1.1, 0.9], [-0.4, 1.8, 5], 46], to: [[-1.2, 1.15, 1.6], [-0.4, 1.75, 5], 41], cInf: 9, focus: [0, 1.4, 5] },
  { a: 281, b: 318, light: "golden", from: [[18, 6, 0.5], [0, 2.5, 3], 48], to: [[14, 4.5, 0.2], [0, 2, 3.5], 44], cInf: 0 },
  { a: 318, b: 367, light: "day", from: [[-3.0, 1.15, 1.0], [-3.2, 1.6, 5], 46], to: [[-2.9, 1.15, 1.6], [-3.2, 1.55, 5], 41], cInf: 9, focus: [-3.2, 1, 5] },
  { a: 367, b: 403, light: "day", from: [[0.6, 1.15, 1.4], [0.5, 1.6, 5], 44], to: [[0.6, 1.15, 1.9], [0.5, 1.55, 5], 40], cInf: 10, focus: [0.5, 1.3, 5] },
  { a: 403, b: 466, light: "day", from: [[-0.6, 0.9, 3.0], [0.0, 1.0, 5.5], 40], to: [[-0.5, 0.9, 3.4], [0.0, 1.0, 5.5], 35], cInf: 11, focus: [0.6, 0.85, 5.3] },
  { a: 466, b: 608, light: "day", from: [[2.6, 2.0, 4.9], [2.6, 2.05, 7], 40], to: [[0.4, 1.5, 2.0], [1.7, 1.4, 6.0], 50], cInf: 7, focus: [2.6, 2.05, 6.9] },
  { a: 608, b: 636, light: "day", from: [[-0.4, 1.05, 3.6], [0.0, 1.05, 5.5], 32], to: [[-0.4, 1.05, 3.8], [0.0, 1.05, 5.5], 28], cInf: 12, focus: [0.6, 1.4, 5.3] },
];
const KICK = 608;
const sm = (t: number) => { t = Math.max(0, Math.min(1, t)); return t * t * t * (t * (t * 6 - 15) + 10); };
const shotAt = (f: number) => SHOTS.find((s) => f >= s.a && f < s.b) ?? SHOTS[SHOTS.length - 1];
const lerpV = (a: V, b: V, t: number) => new THREE.Vector3(a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t);

const fbScreen = (g: CanvasRenderingContext2D, f: number) => {
  const W = 360, H = 720; g.fillStyle = "#f0f2f5"; g.fillRect(0, 0, W, H);
  g.fillStyle = "#1877f2"; g.fillRect(0, 0, W, 64); g.fillStyle = "#fff"; g.font = "800 30px 'DejaVu Sans', Arial"; g.textAlign = "left"; g.fillText("Trang cá nhân", 16, 44);
  // cover = green board
  g.save(); g.translate(0, 64); drawChart(g, W, 200, -1, "VN-INDEX 1.528"); g.restore();
  // avatar circle with green arrow
  g.save(); g.beginPath(); g.arc(90, 270, 62, 0, 7); g.fillStyle = "#fff"; g.fill(); g.beginPath(); g.arc(90, 270, 56, 0, 7); g.clip(); g.fillStyle = "#0e1726"; g.fillRect(20, 200, 140, 140);
  g.strokeStyle = "#2bd17e"; g.lineWidth = 10; g.beginPath(); g.moveTo(50, 300); g.lineTo(80, 275); g.lineTo(100, 285); g.lineTo(132, 240); g.stroke(); g.restore();
  g.fillStyle = "#111"; g.font = "800 26px 'DejaVu Sans', Arial"; g.fillText("Tuấn Nguyễn", 162, 296);
  g.fillStyle = "#555"; g.font = "500 16px 'DejaVu Sans', Arial"; g.fillText("vừa đổi ảnh đại diện", 162, 322);
  const k = Math.max(0, Math.min(1, (f - 150) / 40)), txt = "Nghỉ việc thôi, đi làm chi nữa 🚀".slice(0, Math.round(32 * k));
  g.fillStyle = "#fff"; g.fillRect(14, 370, W - 28, 150); g.fillStyle = "#111"; g.font = "700 26px 'DejaVu Sans', Arial";
  const words = txt.split(" "); let line = "", y = 412; for (const w of words) { if (g.measureText(line + w).width > W - 60) { g.fillText(line, 30, y); line = ""; y += 38; } line += w + " "; } g.fillText(line, 30, y);
  g.fillStyle = "#65676b"; g.font = "600 22px 'DejaVu Sans', Arial"; g.fillText("👍 ❤️ 128   ·   47 bình luận", 30, 500);
};

const Inner: React.FC = () => {
  const f = useCurrentFrame();
  const { camera, scene } = useThree();
  const world = useMemo(() => new World(), []);
  const fx = useMemo(() => ({
    ink: new InkPass(scene, camera as THREE.PerspectiveCamera),
    lens: new LensBlur({ maxCoC: 24, nearScale: 1.2 }),
    bloom: new BloomEffect({ blendFunction: BlendFunction.ADD, intensity: 0.5, luminanceThreshold: 1.0, luminanceSmoothing: 0.2, mipmapBlur: true, levels: 5, radius: 0.6 }),
    tone: new ToneMappingEffect({ mode: ToneMappingMode.NEUTRAL }),
    grade: new GradeEffect(GRADES.day, 1),
  }), [camera, scene]);
  useEffect(() => () => fx.ink.dispose(), [fx]);
  const cam = camera as THREE.PerspectiveCamera;
  const s = shotAt(f), k = f - s.a, t = sm(k / Math.max(1, s.b - s.a));
  const pos = lerpV(s.from[0], s.to[0], t), look = lerpV(s.from[1], s.to[1], t);
  let fov = s.from[2] + (s.to[2] - s.from[2]) * t;
  const burst = 1 - sm(k / 10); fov *= 1 + 0.06 * burst; // ease-out arrival on every cut
  cam.position.copy(pos); cam.lookAt(look);
  if (f >= KICK && f < KICK + 8) { const a = 0.05 * (1 - (f - KICK) / 8) * (f % 2 ? 1 : -1); cam.rotateZ(a); cam.position.y += a * 0.6; fov *= 0.97; }
  cam.fov = fov; cam.aspect = 16 / 9; cam.near = 0.05; cam.updateProjectionMatrix();
  world.setLight(s.light, pos);
  gradeFor(fx.grade, s.light);
  // actors per shot
  const W = world, show = (a: typeof W.tuan, p: V, pose: Pose) => { a.root.visible = true; a.root.position.set(...p); a.pose(pose, cam, tint); };
  const tint = new THREE.Color(s.light === "day" ? (f >= 281 ? "#f4ecf2" : "#ffffff") : "#ffd9b8");
  for (const a of [W.tuan, W.me, W.khach, W.chi]) a.root.visible = false;
  const blink = f % 71 < 4;
  W.bikeT.visible = f < 318 || (f >= 318 && f < 367);
  if (f < 281) {
    show(W.tuan, T0, { expr: f < 211 ? "grin" : "laugh", blink, wave: f >= 211 ? 0.55 + 0.35 * Math.sin(f * 0.35) : undefined });
    if (f >= 211) show(W.chi, [-2.4, 0.15, 5.6], { expr: "nervous", blink: f % 53 < 4 });
  } else if (f < 318) {
    show(W.tuan, [-2.2, 0.15, 4.9], { expr: "neutral", blink });
  } else if (f < 367) {
    show(W.tuan, [-2.1, 0.15, 4.85], { expr: "pained", blink, headTilt: -0.1 });
    show(W.khach, [-4.4, 0.15, 5.0], { expr: "smile", blink: f % 61 < 4 });
  } else if (f < 403) {
    show(W.tuan, [0, 0.15, 4.9], { expr: "nervous", blink, headTilt: 0.08 });
    show(W.me, [1.1, 0.15, 5.1], { expr: "stern", blink: f % 47 < 4 });
  } else if (f < 608) {
    show(W.tuan, [0.0, 0.15, 5.5], { expr: f < 466 ? "dazed" : "nervous", blink, mode: "sit" });
  } else {
    show(W.tuan, [0.0, 0.15, 5.5], { expr: "shock", mode: "sit" });
  }
  // TV board: crash progresses through shot 8
  drawChart(W.tv.g, 640, 400, f < 466 ? 0 : (f - 480) / 120, "VN-INDEX");
  W.tv.t.needsUpdate = true;
  // phone insert
  const ph = W.phone.mesh; ph.visible = s.focus === "phone";
  if (ph.visible) {
    const fwd = new THREE.Vector3(); cam.getWorldDirection(fwd);
    ph.position.copy(cam.position).addScaledVector(fwd, 1.35).add(new THREE.Vector3(0.22, -0.04, 0));
    ph.lookAt(cam.position); ph.rotateZ(-0.06 + 0.01 * Math.sin(f * 0.08));
    fbScreen(W.phone.g, f); W.phone.t.needsUpdate = true;
  }
  noInkFallback(world.root);
  const fwd = new THREE.Vector3(); cam.getWorldDirection(fwd);
  const fp = s.focus === "phone" ? ph.position.clone() : s.focus ? new THREE.Vector3(...s.focus) : look;
  fx.lens.focus = Math.max(0.3, fp.clone().sub(cam.position).dot(fwd));
  fx.lens.cInf = s.cInf;
  return (
    <>
      <primitive object={world.root} dispose={null} />
      <EffectComposer multisampling={2}>
        <primitive object={fx.ink} dispose={null} />
        <primitive object={fx.lens.pre} dispose={null} />
        <primitive object={fx.lens.main} dispose={null} />
        <primitive object={fx.bloom} dispose={null} />
        <primitive object={fx.tone} dispose={null} />
        <primitive object={fx.grade} dispose={null} />
      </EffectComposer>
    </>
  );
};

export const PhoDemo: React.FC = () => {
  const f = useCurrentFrame();
  const audio = (getInputProps() as { audio?: boolean }).audio;
  const flash = f >= 281 && f < 287 ? [0.9, 0.7, 0.5, 0.3, 0.15, 0.05][f - 281] : 0;
  const big = f >= KICK ? Math.min(1, (f - KICK) / 4) : 0;
  return (
    <AbsoluteFill style={{ background: "#bcd6ef" }}>
      <ThreeCanvas width={1920} height={1080} shadows gl={{ antialias: false, stencil: false, toneMappingExposure: 1.0 }} camera={{ fov: 40, near: 0.05, far: 900 }}>
        <Inner />
      </ThreeCanvas>
      {flash > 0 && <AbsoluteFill style={{ background: "#000", opacity: flash }} />}
      {big > 0 && (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "flex-start", paddingLeft: 140 }}>
          <div style={{ fontFamily: "DejaVu Sans, Arial", fontWeight: 900, fontSize: 260 * (1.3 - 0.3 * big), color: "#ff3b4e", WebkitTextStroke: "10px #1a0b10", transform: `rotate(-6deg)`, opacity: big }}>-40%</div>
        </AbsoluteFill>
      )}
      {f >= 281 && f < 318 && (
        <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: 90 }}>
          <div style={{ fontFamily: "DejaVu Sans, Arial", fontWeight: 900, fontSize: 84, color: "#fff", WebkitTextStroke: "6px #1a1a2a", opacity: Math.min(1, (f - 281) / 6) }}>MỘT NĂM SAU…</div>
        </AbsoluteFill>
      )}
      {audio ? <Audio src={staticFile("pho/voice.mp3")} /> : null}
    </AbsoluteFill>
  );
};
