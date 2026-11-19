// Vật liệu toon riêng của bối cảnh suaxe2 : 2 tông nắng (bóng đổ thật) + ambient bán cầu ấm + tối đa 5 đèn ấm mềm.
import * as THREE from "three";
import { LFB } from "../pho/shade";
// ---------------- vật liệu toon riêng của set (2 tông nắng + ánh đèn ấm mềm + ambient bán cầu) ----------------
export const NL = 5; // số đèn ấm tối đa
export const U = {
  uSun: { value: new THREE.Vector3(1.55, 1.12, 0.72) },        // nắng chiều
  uAmbHi: { value: new THREE.Vector3(0.62, 0.55, 0.52) },      // trời / trần hắt xuống
  uAmbLo: { value: new THREE.Vector3(0.36, 0.3, 0.3) },        // sàn hắt lên
  uSat: { value: 1.08 },
  uLampP: { value: Array.from({ length: NL }, () => new THREE.Vector3(0, -99, 0)) },
  uLampC: { value: Array.from({ length: NL }, () => new THREE.Vector3()) },
  uLampR: { value: Array.from({ length: NL }, () => 1) },
};
const DECL = `#include <common>
uniform vec3 uSun; uniform vec3 uAmbHi; uniform vec3 uAmbLo; uniform float uSat;
uniform vec3 uLampP[${NL}]; uniform vec3 uLampC[${NL}]; uniform float uLampR[${NL}];`;
const SHADE = /* glsl */ `
#if NUM_DIR_LIGHTS > 0
{
  vec3 sunV = directionalLights[ 0 ].direction;
  vec3 upV = normalize( ( viewMatrix * vec4( 0.0, 1.0, 0.0, 0.0 ) ).xyz );
  float ndl = max( dot( geometryNormal, sunV ), 0.0 );
  float sunTerm = sunVis * smoothstep( 0.0, 0.22, ndl );
  float up = 0.5 + 0.5 * dot( geometryNormal, upV );
  vec3 alb = max( mix( vec3( dot( diffuseColor.rgb, vec3( 0.2126, 0.7152, 0.0722 ) ) ), diffuseColor.rgb, uSat ), 0.0 );
  vec3 lamp = vec3( 0.0 );
  for ( int i = 0; i < ${NL}; i ++ ) {
    vec3 lp = ( viewMatrix * vec4( uLampP[ i ], 1.0 ) ).xyz; vec3 d = lp - geometryPosition; float dist = length( d );
    float nl = max( dot( geometryNormal, d / dist ), 0.0 ); float att = clamp( 1.0 - dist / uLampR[ i ], 0.0, 1.0 ); att *= att;
    lamp += uLampC[ i ] * smoothstep( 0.0, 0.45, nl ) * att;
  }
  vec3 amb = mix( uAmbLo, uAmbHi, smoothstep( 0.1, 0.9, up ) );
  reflectedLight.directDiffuse = alb * ( amb + uSun * sunTerm * mix( 1.0, ndl, 0.25 ) + lamp );
  reflectedLight.indirectDiffuse = vec3( 0.0 );
}
#endif
`;
const matCache = new Map<string, THREE.MeshLambertMaterial>();
export function tm(color: THREE.ColorRepresentation = "#ffffff", map: THREE.Texture | null = null, o: { alphaTest?: number; side?: THREE.Side; vc?: boolean } = {}) {
  const key = map ? "" : `${new THREE.Color(color).getHexString()}_${o.side ?? 0}`;
  if (key && matCache.has(key)) return matCache.get(key)!;
  const m = new THREE.MeshLambertMaterial({ color, map, alphaTest: o.alphaTest ?? 0, side: o.side ?? THREE.FrontSide, vertexColors: !!o.vc });
  m.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, U);
    sh.fragmentShader = sh.fragmentShader.replace("#include <common>", DECL)
      .replace("#include <lights_fragment_begin>", "float sunVis = 1.0;\n" + LFB)
      .replace("#include <lights_fragment_end>", "#include <lights_fragment_end>\n" + SHADE);
  };
  m.customProgramCacheKey = () => "sx2toon1";
  if (key) matCache.set(key, m);
  return m;
}
export const glow = (r: number, g: number, b: number) => new THREE.MeshBasicMaterial({ color: new THREE.Color(r, g, b) });

