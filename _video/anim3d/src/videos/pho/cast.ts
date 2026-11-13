// Flat 2D cartoon cast as camera-facing cards (drawn with toon.ts Pen), Vietnamese everyday people.
import * as THREE from "three";
import { Pen, bodyFront, Outfit, Expr } from "./toon";
import { NOINK } from "./ink";

export const TUAN: Outfit = { jacket: "#f5f5f2", pants: "#2f3546", boots: "#3a2a22", hat: "hair", hair: "#1c1719", belt: null, buttons: "#c9ced6" };
export const ME: Outfit = { jacket: "#8a5a3a", pants: "#26262b", boots: "#5a3b2a", hat: "hair", hair: "#b9b6b2", belt: null, buttons: "#d8c7a8", build: "stout", skin: "#f0c9a2" };
export const KHACH: Outfit = { jacket: "#3a78c2", pants: "#4a4a42", boots: "#2a2a2a", hat: "cap", cap: "#2f8a52", belt: null, buttons: "#dfe6ee", skin: "#d9a77e" };
export const CHI: Outfit = { jacket: "#e86a92", pants: "#e86a92", boots: "#f3e8dc", hat: "hair", hair: "#2a1d1b", belt: null, buttons: "#ffffff", skin: "#ffdcc0" };

export type Pose = { expr: Expr; wave?: number; blink?: boolean; mode?: "stand" | "sit" | "stroll"; phase?: number; tilt?: number; headTilt?: number };

export class Actor {
  root = new THREE.Group();
  card: THREE.Mesh;
  shadow: THREE.Mesh;
  private c: HTMLCanvasElement;
  private g: CanvasRenderingContext2D;
  private t: THREE.CanvasTexture;
  private key = "";
  constructor(public o: Outfit, public h = 1.72, public seed = 3) {
    this.c = document.createElement("canvas"); this.c.width = 600; this.c.height = 1000;
    this.g = this.c.getContext("2d")!;
    this.t = new THREE.CanvasTexture(this.c); this.t.colorSpace = THREE.SRGBColorSpace;
    const H = h / 0.95, W = H * 0.6; // soles at y=975 of 1000
    const geo = new THREE.PlaneGeometry(W, H); geo.translate(0, H / 2 - H * 0.025, 0);
    this.card = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ map: this.t, alphaTest: 0.45, transparent: false, side: THREE.DoubleSide }));
    this.card.layers.set(NOINK);
    this.shadow = new THREE.Mesh(new THREE.CircleGeometry(0.42, 24), new THREE.MeshBasicMaterial({ color: "#1d1a2a", transparent: true, opacity: 0.35, depthWrite: false }));
    this.shadow.rotation.x = -Math.PI / 2; this.shadow.scale.set(1, 0.45, 1); this.shadow.position.y = 0.02; this.shadow.layers.set(NOINK);
    this.root.add(this.card, this.shadow);
  }
  pose(p: Pose, cam: THREE.Camera, tint: THREE.Color) {
    const k = JSON.stringify(p);
    if (k !== this.key) {
      this.key = k; const g = this.g; g.setTransform(1, 0, 0, 1, 0, 0); g.clearRect(0, 0, 600, 1000);
      bodyFront(new Pen(g), this.o, { expr: p.blink && p.expr !== "shock" ? p.expr : p.expr, blink: p.blink ? 1 : 0, mode: p.mode ?? "stand", seed: this.seed, wave: p.wave, phase: p.phase ?? 0, tilt: p.tilt ?? 0, headTilt: p.headTilt ?? 0 });
      this.t.needsUpdate = true;
    }
    (this.card.material as THREE.MeshBasicMaterial).color.copy(tint);
    const wp = this.root.getWorldPosition(new THREE.Vector3());
    this.card.rotation.y = Math.atan2(cam.position.x - wp.x, cam.position.z - wp.z) - this.root.rotation.y;
  }
}
