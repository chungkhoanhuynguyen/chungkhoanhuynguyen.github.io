// Bảng ánh sáng + màu trời cho từng cảnh (đêm phố mưa, phòng livestream đèn RGB, rạng sáng Huế, sáng Sài Gòn, đêm Hồ Gươm).
import * as THREE from "three";
import { TONE } from "../pho/shade";
import { GradeParams } from "../pho/grade";
type C3 = [number, number, number];
export type LK = "day" | "morning" | "golden" | "night" | "room" | "roomdim" | "dawn" | "lake";
export const L: Record<LK, { lit: C3; shade: C3; lift: C3; lambert: number; sideK: number; term: number; sat: number; sun: [number, number, number]; sky: [string, string]; tint: string }> = {
  day: { lit: [1.58, 1.5, 1.33], shade: [0.3, 0.29, 0.36], lift: [0.05, 0.06, 0.11], lambert: 0.35, sideK: 0.84, term: 0.2, sat: 1.08, sun: [22, 55, -40], sky: ["#3e7fd2", "#bcd6ef"], tint: "#ffffff" },
  morning: { lit: [1.6, 1.38, 1.05], shade: [0.28, 0.27, 0.4], lift: [0.05, 0.05, 0.12], lambert: 0.35, sideK: 0.84, term: 0.18, sat: 1.1, sun: [-40, 30, -35], sky: ["#5a8fd6", "#f6d7a8"], tint: "#fff4e6" },
  golden: { lit: [1.5, 0.75, 0.32], shade: [0.15, 0.15, 0.3], lift: [0.04, 0.06, 0.17], lambert: 0.35, sideK: 0.82, term: 0.07, sat: 1.0, sun: [-45, 16, -40], sky: ["#6a4f8c", "#ffcf8f"], tint: "#ffd9b8" },
  night: { lit: [1.15, 0.86, 0.55], shade: [0.1, 0.12, 0.27], lift: [0.02, 0.03, 0.1], lambert: 0.45, sideK: 0.8, term: 0.25, sat: 0.95, sun: [6, 40, -14], sky: ["#070b1c", "#22305a"], tint: "#d9c8e6" },
  lake: { lit: [1.25, 0.92, 0.62], shade: [0.12, 0.13, 0.3], lift: [0.02, 0.03, 0.1], lambert: 0.45, sideK: 0.8, term: 0.25, sat: 1.05, sun: [-18, 35, 20], sky: ["#0b1030", "#3a3f78"], tint: "#f0dcd8" },
  room: { lit: [1.3, 1.05, 1.32], shade: [0.22, 0.19, 0.4], lift: [0.04, 0.03, 0.12], lambert: 0.4, sideK: 0.82, term: 0.22, sat: 1.05, sun: [3, 10, 12], sky: ["#0a0d22", "#1b2350"], tint: "#f1e2ff" },
  roomdim: { lit: [0.78, 0.74, 1.05], shade: [0.1, 0.1, 0.24], lift: [0.02, 0.02, 0.09], lambert: 0.45, sideK: 0.8, term: 0.25, sat: 0.85, sun: [-12, 9, 6], sky: ["#05070f", "#121831"], tint: "#b9bfe0" },
  dawn: { lit: [1.25, 1.08, 1.12], shade: [0.2, 0.23, 0.42], lift: [0.04, 0.05, 0.14], lambert: 0.35, sideK: 0.84, term: 0.2, sat: 0.95, sun: [-50, 14, -30], sky: ["#3c4f8c", "#f2b9a0"], tint: "#f3e4ea" },
};
export const GR: Record<LK, GradeParams> = {
  day: { ky: [0, 0.1, 0.28, 0.6, 0.835, 0.945, 1], sat: [1.0, 1.05, 1.0], tintS: [0.01, 0.002], tintM: [0, 0], tintH: [0.006, 0], vig: [0.12, 0.45] },
  morning: { ky: [0, 0.1, 0.28, 0.6, 0.84, 0.95, 1], sat: [1.0, 1.08, 1.05], tintS: [0.012, 0.0], tintM: [-0.004, 0.006], tintH: [-0.01, 0.008], vig: [0.14, 0.45] },
  golden: { ky: [0, 0.09, 0.245, 0.54, 0.8, 0.93, 1], sat: [1.0, 1.12, 1.15], tintS: [0.02, 0.002], tintM: [0, 0], tintH: [-0.012, 0.006], vig: [0.2, 0.4] },
  night: { ky: [0, 0.075, 0.22, 0.52, 0.8, 0.94, 1], sat: [0.9, 1.05, 1.1], tintS: [0.035, -0.006], tintM: [0.012, 0.0], tintH: [-0.01, 0.01], vig: [0.32, 0.36] },
  lake: { ky: [0, 0.08, 0.235, 0.54, 0.81, 0.94, 1], sat: [0.95, 1.1, 1.15], tintS: [0.03, 0.0], tintM: [0.006, 0.004], tintH: [-0.012, 0.012], vig: [0.3, 0.36] },
  room: { ky: [0, 0.085, 0.25, 0.56, 0.82, 0.94, 1], sat: [1.0, 1.1, 1.1], tintS: [0.03, 0.01], tintM: [0.01, 0.01], tintH: [0, 0], vig: [0.26, 0.4] },
  roomdim: { ky: [0, 0.06, 0.19, 0.46, 0.74, 0.9, 1], sat: [0.8, 0.85, 0.9], tintS: [0.04, -0.004], tintM: [0.02, -0.004], tintH: [0.01, 0], vig: [0.4, 0.32] },
  dawn: { ky: [0, 0.1, 0.27, 0.58, 0.83, 0.945, 1], sat: [0.95, 1.0, 1.05], tintS: [0.03, 0.0], tintM: [0.006, 0.004], tintH: [-0.006, 0.01], vig: [0.2, 0.42] },
};
export function applyLight(k: LK, sun: THREE.DirectionalLight, cam: THREE.Vector3, sky: THREE.ShaderMaterial) {
  const P = L[k];
  TONE.uLitCol.value.set(...P.lit); TONE.uShadeCol.value.set(...P.shade); TONE.uShadeLift.value.set(...P.lift);
  TONE.uLambert.value = P.lambert; TONE.uSideK.value = P.sideK; TONE.uTerm.value = P.term; TONE.uSat.value = P.sat;
  sun.position.set(cam.x + P.sun[0], cam.y + P.sun[1], cam.z + P.sun[2]); sun.target.position.set(cam.x, 0, cam.z); sun.intensity = 2.8;
  (sky.uniforms.top.value as THREE.Color).set(P.sky[0]); (sky.uniforms.hor.value as THREE.Color).set(P.sky[1]);
}
