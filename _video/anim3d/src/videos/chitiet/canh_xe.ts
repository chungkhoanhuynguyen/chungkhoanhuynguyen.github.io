// Bối cảnh xe (chuẩn chi tiết 20/11): showroom đèn tím xanh, phố ban ngày có speedster mui trần / mô tô sportbike đỗ, tiệm suaxe2 có siêu xe đỗ trước cửa.
// Vị trí xe + chỗ ngồi xuất ra để Demo đặt nhân vật (ride) đúng yên.
import * as THREE from "three";
import { tm, glow, U, setLook } from "./toonmat";
import { sieuXeNem, speedster, sportbike, riderLegs, SPEEDSTER_SEAT, BIKE_SEAT, phys0, envScale } from "./xe_sang";
import { buildStreet } from "../vang/sets";
import { NOINK } from "../pho/ink";
import { mau } from "./xe_mau";

type V3 = [number, number, number];
/** điểm cục bộ của xe → toạ độ thế giới (xe đặt tại pos, xoay ry quanh trục đứng) */
export const toWorld = (pos: V3, ry: number, l: V3): V3 => { const v = new THREE.Vector3(...l).applyAxisAngle(new THREE.Vector3(0, 1, 0), ry); return [pos[0] + v.x, pos[1] + v.y, pos[2] + v.z]; };

// ---------- SHOWROOM ----------
export const SHOW_CAR: { pos: V3; ry: number } = { pos: [0, 0.14, 0], ry: 0.6 };
export function buildShowroom(opt: { mau?: boolean } = {}) {
  setLook("day"); U.uAmbHi.value.set(0.22, 0.2, 0.34); U.uAmbLo.value.set(0.08, 0.08, 0.14); U.uSun.value.set(0.4, 0.4, 0.5);
  const lamps: [V3, V3, number][] = [[[-5, 4.5, 2], [1.4, 0.4, 2.2], 14], [[5, 4.5, -2], [0.3, 0.9, 2.4], 14], [[0, 5.5, 0], [1.0, 1.0, 1.1], 10]];
  lamps.forEach(([p, c, r], i) => { U.uLampP.value[i].set(...p); U.uLampC.value[i].set(...c); U.uLampR.value[i] = r; });
  const g = new THREE.Group(), W = 26, D = 20, H = 6.5;
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(W, D), phys0({ color: "#0d0e13", metalness: 0.2, roughness: 0.22, clearcoat: 1, clearcoatRoughness: 0.08 }, 0.9)); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; g.add(floor);
  const wall = tm("#1b1d2c"); for (const [w, h, x, y, z, ry] of [[W, H, 0, H / 2, -D / 2, 0], [W, H, 0, H / 2, D / 2, Math.PI], [D, H, -W / 2, H / 2, 0, Math.PI / 2], [D, H, W / 2, H / 2, 0, -Math.PI / 2]] as number[][]) { const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.3), wall); m.position.set(x, y, z); m.rotation.y = ry; m.castShadow = true; m.receiveShadow = true; g.add(m); }
  const ceil = new THREE.Mesh(new THREE.BoxGeometry(W, 0.3, D), tm("#111219")); ceil.position.y = H; ceil.castShadow = true; g.add(ceil);
  // dải LED tím / xanh trên trần + chân tường + vách sau dạng sóng
  for (let k = 0; k < 7; k++) { const b = new THREE.Mesh(new THREE.BoxGeometry(W - 2, 0.06, 0.12), glow(...((k % 2 ? [0.5, 1.4, 3.2] : [2.4, 0.6, 3.4]) as [number, number, number]))); b.position.set(0, H - 0.2, -8 + k * 2.6); g.add(b); }
  for (const z of [-D / 2 + 0.2, D / 2 - 0.2]) { const b = new THREE.Mesh(new THREE.BoxGeometry(W - 1, 0.05, 0.05), glow(2.2, 0.6, 3.2)); b.position.set(0, 0.06, z); g.add(b); }
  for (let k = 0; k < 9; k++) { const p = new THREE.Mesh(new THREE.BoxGeometry(1.6, 4.4, 0.12), tm(k % 2 ? "#232641" : "#1d2036")); p.position.set(-8 + k * 2, 2.6, -D / 2 + 0.4 + Math.sin(k) * 0.2); p.rotation.y = (k - 4) * 0.08; g.add(p); const l = new THREE.Mesh(new THREE.BoxGeometry(0.05, 4.2, 0.05), glow(...((k % 2 ? [0.4, 1.2, 3] : [2.2, 0.5, 3.2]) as [number, number, number]))); l.position.set(-8 + k * 2 + 0.82, 2.6, -D / 2 + 0.5 + Math.sin(k) * 0.2); g.add(l); }
  { const c = document.createElement("canvas"); c.width = 1024; c.height = 160; const x = c.getContext("2d")!; x.fillStyle = "#000"; x.fillRect(0, 0, 1024, 160); x.fillStyle = "#e9d8ff"; x.font = "900 96px 'Be Vietnam Pro', 'DejaVu Sans'"; x.textAlign = "center"; x.fillText("TRIỂN LÃM XE", 512, 112);
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; const s = new THREE.Mesh(new THREE.PlaneGeometry(7, 1.1), new THREE.MeshBasicMaterial({ map: t, color: new THREE.Color(1.6, 1.6, 1.6), transparent: true, blending: THREE.AdditiveBlending })); s.position.set(0, 5.4, -D / 2 + 0.6); s.layers.set(NOINK); g.add(s); }
  // bàn xoay + vòng LED + xe
  const tt = new THREE.Mesh(new THREE.CylinderGeometry(3.3, 3.4, 0.14, 64), phys0({ color: "#2a2c34", metalness: 0.8, roughness: 0.3, clearcoat: 1 }, 0.8)); tt.position.y = 0.07; tt.receiveShadow = true; tt.castShadow = true; g.add(tt);
  const ring = new THREE.Mesh(new THREE.TorusGeometry(3.36, 0.03, 8, 96), glow(2.4, 0.7, 3.6)); ring.rotation.x = Math.PI / 2; ring.position.y = 0.13; g.add(ring);
  if (opt.mau) { const a = mau("goblin"); a.position.set(...SHOW_CAR.pos); a.rotation.y = SHOW_CAR.ry; g.add(a); const b = mau("abyss"); b.position.set(-5.2, 0, -2.8); b.rotation.y = 1.0; g.add(b); }
  else { const car = sieuXeNem(); car.position.set(...SHOW_CAR.pos); car.rotation.y = SHOW_CAR.ry; g.add(car); }
  // đèn màu thật (ăn lên sơn bóng): tím trái, xanh phải, đèn trắng rọi từ trên
  const pl1 = new THREE.PointLight("#b45cff", 40, 18, 1.6); pl1.position.set(-5, 4.5, 2); g.add(pl1); const pl2 = new THREE.PointLight("#4aa8ff", 40, 18, 1.6); pl2.position.set(5, 4.5, -2); g.add(pl2);
  const sp = new THREE.SpotLight("#ffffff", 30, 20, 0.5, 0.7, 1.4); sp.position.set(0, 6, 3); sp.target.position.set(0, 0.5, 0); g.add(sp, sp.target);
  envScale(0.22); return { g };
}

// ---------- PHỐ: speedster mui trần + mô tô sportbike (đường ở z = 0, vỉa hè z = ±5.5, cao 0.15) ----------
export const MUI = { pos: [12, 0, 2.9] as V3, ry: -Math.PI / 2 }; // chạy về -x
export const MUI_SEAT = () => toWorld(MUI.pos, MUI.ry, [SPEEDSTER_SEAT.x, SPEEDSTER_SEAT.y + 0.1, SPEEDSTER_SEAT.z]);
export const MOTO = { pos: [-8, 0, 3.2] as V3, ry: Math.PI / 2 }; // đầu xe về +x
export const MOTO_SEAT = () => toWorld(MOTO.pos, MOTO.ry, [0, BIKE_SEAT.y + 0.06, BIKE_SEAT.z - 0.02]);
// mẫu CC BY: mui trần (roadster) + siêu mô tô SPY (nữ ngồi) + mô tô concept (nam ngồi)
export const ROADSTER_SEAT: V3 = [0.36, 0.42, -0.3]; export const SPY_SEAT = { y: 0.86, z: -0.2 }; export const BIKE2 = { pos: [-12.5, 0, 3.2] as V3, ry: Math.PI / 2 };
export const MUI2_SEAT = () => toWorld(MUI.pos, MUI.ry, ROADSTER_SEAT);
export const SPY_SEAT_W = () => toWorld(MOTO.pos, MOTO.ry, [0, SPY_SEAT.y, SPY_SEAT.z]); export const BIKE2_SEAT_W = () => toWorld(BIKE2.pos, BIKE2.ry, [0, SPY_SEAT.y, SPY_SEAT.z]);
export function buildPhoXe(rider: { pants: string; shoe: string } = { pants: "#2b4f8a", shoe: "#3a2a20" }, opt: { mau?: boolean } = {}) {
  setLook("day"); const st = buildStreet(false); const g = new THREE.Group(); g.add(st.g);
  if (opt.mau) { const car = mau("roadster"); car.position.set(...MUI.pos); car.rotation.y = MUI.ry; g.add(car);
    const b1 = mau("spy"); b1.position.set(...MOTO.pos); b1.rotation.y = MOTO.ry; g.add(b1); b1.add(riderLegs(rider.pants, rider.shoe, [0.11, SPY_SEAT.y + 0.04, SPY_SEAT.z], [0.2, 0.84, 0.12], [0.18, 0.33, -0.12]));
    const b2 = mau("bike"); b2.position.set(...BIKE2.pos); b2.rotation.y = BIKE2.ry; g.add(b2); b2.add(riderLegs("#3d3a36", "#2a2a2a", [0.11, SPY_SEAT.y + 0.04, SPY_SEAT.z], [0.2, 0.84, 0.12], [0.18, 0.33, -0.12]));
    envScale(0.85); return { g }; }
  const car = speedster(); car.position.set(...MUI.pos); car.rotation.y = MUI.ry; g.add(car);
  const bike = sportbike(); bike.position.set(...MOTO.pos); bike.rotation.y = MOTO.ry; bike.rotation.z = 0; g.add(bike);
  envScale(0.85);
  bike.add(riderLegs(rider.pants, rider.shoe, [0.11, BIKE_SEAT.y + 0.08, BIKE_SEAT.z - 0.02], [0.2, 0.96, 0.08], [0.18, 0.36, -0.1]));
  return { g };
}
