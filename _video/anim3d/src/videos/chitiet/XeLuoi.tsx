// Tờ lưới xe: mỗi khung = 1 xe, 3 góc (ngang, 3/4 trước, 3/4 sau) trên nền sáng trung tính, cùng viền mực + tone map như sân khấu.
import React, { useMemo } from "react";
import * as THREE from "three";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { ThreeCanvas } from "@remotion/three";
import { useThree } from "@react-three/fiber";
import { EffectComposer } from "@react-three/postprocessing";
import { BlendFunction, BloomEffect, ToneMappingEffect, ToneMappingMode } from "postprocessing";
import { InkPass, NOINK } from "../pho/ink";
import { XE_DS } from "./xe";
import { MAU_DS } from "./xe_mau";
const BO = { xe: XE_DS, mau: MAU_DS };
import { setLook } from "./toonmat";
import { envScale } from "./xe_sang";

const View: React.FC<{ i: number; ang: number; bo: "xe" | "mau" }> = ({ i, ang, bo }) => {
  const { camera, scene } = useThree(); const X = BO[bo][i];
  const W = useMemo(() => {
    setLook("day"); const root = new THREE.Group();
    const sun = new THREE.DirectionalLight("#ffffff", 2.4); sun.position.set(6, 10, 7); sun.castShadow = true; sun.shadow.mapSize.set(2048, 2048); const sc = sun.shadow.camera as THREE.OrthographicCamera; sc.left = sc.bottom = -6; sc.right = sc.top = 6; sun.shadow.bias = -0.0004; sun.shadow.normalBias = 0.02; sun.shadow.radius = 6;
    root.add(sun, sun.target, new THREE.HemisphereLight("#f4f6ff", "#bdb6a8", 1.1));
    const fl = new THREE.Mesh(new THREE.CircleGeometry(40, 64), new THREE.MeshStandardMaterial({ color: "#d9d6cf", roughness: 0.75 })); fl.rotation.x = -Math.PI / 2; fl.receiveShadow = true; root.add(fl);
    const bg = new THREE.Mesh(new THREE.SphereGeometry(60, 32, 16), new THREE.ShaderMaterial({ side: THREE.BackSide, depthWrite: false, vertexShader: "varying vec3 p; void main(){ p = normalize(position); gl_Position = projectionMatrix*modelViewMatrix*vec4(position,1.0);}", fragmentShader: "varying vec3 p; void main(){ float t = smoothstep(-0.05, 0.5, p.y); gl_FragColor = vec4(mix(vec3(0.86,0.85,0.82), vec3(0.95,0.95,0.94), t), 1.0); }" }));
    bg.layers.set(NOINK); root.add(bg); const car = X.make(); root.add(car); envScale(0.8); return { root };
  }, [i, bo]);
  const fx = useMemo(() => ({ ink: new InkPass(scene, camera as THREE.PerspectiveCamera), bloom: new BloomEffect({ blendFunction: BlendFunction.ADD, intensity: 0.6, luminanceThreshold: 1.0, luminanceSmoothing: 0.2, mipmapBlur: true }), tone: new ToneMappingEffect({ mode: ToneMappingMode.NEUTRAL }) }), [camera, scene]);
  const cam = camera as THREE.PerspectiveCamera, D = Math.max(X.L * 1.35, 2.6) + 0.6, a = [Math.PI / 2, Math.PI * 0.22, Math.PI * 0.78][ang], h = Math.max(1.0, X.H * 0.9);
  cam.position.set(Math.sin(a) * D, h + (ang ? 0.5 : 0.1), Math.cos(a) * D); cam.lookAt(0, X.H * 0.42, 0); cam.fov = 30; cam.aspect = 16 / 9; cam.near = 0.05; cam.far = 200; cam.updateProjectionMatrix();
  return <><primitive object={W.root} dispose={null} /><EffectComposer multisampling={0}><primitive object={fx.ink} dispose={null} /><primitive object={fx.bloom} dispose={null} /><primitive object={fx.tone} dispose={null} /></EffectComposer></>;
};
export const XE_N = XE_DS.length;
export const MAU_N = MAU_DS.length;
export const XeLuoi: React.FC<{ bo?: "xe" | "mau" }> = ({ bo = "xe" }) => { const f = useCurrentFrame(), L = BO[bo], i = Math.min(L.length - 1, f); const X = L[i];
  return <AbsoluteFill style={{ background: "#eeeae2", fontFamily: "DejaVu Sans, Arial" }}>
    <div style={{ display: "flex", gap: 6, padding: 6 }}>{[0, 1, 2].map((ang) => <div key={ang} style={{ width: 632, height: 356, position: "relative", overflow: "hidden" }}>
      <div style={{ position: "absolute", left: 0, top: 0, width: 1280, height: 720, transform: "scale(0.49375)", transformOrigin: "0 0" }}>
        <ThreeCanvas width={1280} height={720} shadows="soft" gl={{ antialias: false, stencil: false }} camera={{ fov: 30, near: 0.05, far: 200 }}><View i={i} ang={ang} bo={bo} /></ThreeCanvas></div></div>)}</div>
    <div style={{ fontSize: 26, fontWeight: 800, color: "#222", padding: "0 14px" }}>{X.ten} <span style={{ fontWeight: 500, color: "#666", fontSize: 20 }}>· ngang · 3/4 trước · 3/4 sau</span></div>
  </AbsoluteFill>; };
