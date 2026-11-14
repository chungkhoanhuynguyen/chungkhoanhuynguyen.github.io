// Phòng học trường quý tộc (vẽ vector) – nền cho lớp học Lý thuyết trò chơi.
import React from "react";
import { AbsoluteFill } from "remotion";
const W = 1920, H = 1080, HZ = 640;
const Window: React.FC<{ x: number }> = ({ x }) => {
  const w = 230, top = 120, bot = 560;
  return <g>
    <path d={`M${x - 14},${bot + 14} L${x - 14},${top + 110} A${w / 2 + 14},${w / 2 + 14} 0 0 1 ${x + w + 14},${top + 110} L${x + w + 14},${bot + 14} Z`} fill="#e9dcc0" />
    <path d={`M${x},${bot} L${x},${top + 110} A${w / 2},${w / 2} 0 0 1 ${x + w},${top + 110} L${x + w},${bot} Z`} fill="url(#sky)" />
    {/* cây ngoài cửa */}
    <ellipse cx={x + 60} cy={bot - 40} rx={90} ry={80} fill="#3f7a3a" opacity={0.9} /><ellipse cx={x + 170} cy={bot - 60} rx={80} ry={95} fill="#4f8f45" opacity={0.9} />
    <ellipse cx={x + 115} cy={bot - 120} rx={70} ry={60} fill="#5fa352" opacity={0.85} />
    <path d={`M${x},${bot} L${x},${top + 110} A${w / 2},${w / 2} 0 0 1 ${x + w},${top + 110} L${x + w},${bot} Z`} fill="none" stroke="#8a6a3a" strokeWidth={10} />
    <line x1={x + w / 2} y1={top} x2={x + w / 2} y2={bot} stroke="#8a6a3a" strokeWidth={8} />
    {[220, 330, 440].map((y) => <line key={y} x1={x} y1={top + y - 100} x2={x + w} y2={top + y - 100} stroke="#8a6a3a" strokeWidth={6} />)}
    {/* rèm nhung đỏ + dây vàng */}
    <path d={`M${x - 60},${top - 40} Q${x - 10},${300} ${x - 30},${bot + 60} L${x - 80},${bot + 60} Q${x - 70},${300} ${x - 90},${top - 40} Z`} fill="#7a1424" />
    <path d={`M${x + w + 60},${top - 40} Q${x + w + 10},${300} ${x + w + 30},${bot + 60} L${x + w + 80},${bot + 60} Q${x + w + 70},${300} ${x + w + 90},${top - 40} Z`} fill="#7a1424" />
    <circle cx={x - 40} cy={380} r={9} fill="#e0b54a" /><circle cx={x + w + 40} cy={380} r={9} fill="#e0b54a" />
    <rect x={x - 100} y={top - 55} width={w + 200} height={22} rx={8} fill="#b8862e" />
    <rect x={x - 20} y={bot + 10} width={w + 40} height={18} fill="#d8c8a6" />
  </g>;
};
const Vase: React.FC<{ x: number; y: number; s?: number }> = ({ x, y, s = 1 }) => <g transform={`translate(${x},${y}) scale(${s})`}>
  {/* hoa */}
  {[[-40, -150, "#f2f2f2"], [0, -175, "#f6c6d0"], [40, -150, "#f2f2f2"], [-20, -125, "#e85a7a"], [25, -120, "#f6c6d0"], [-55, -110, "#ffffff"], [55, -105, "#e85a7a"]].map(([dx, dy, c], i) =>
    <g key={i}><line x1={0} y1={-40} x2={dx as number} y2={dy as number} stroke="#3f6a2f" strokeWidth={3} /><circle cx={dx as number} cy={dy as number} r={17} fill={c as string} /><circle cx={dx as number} cy={dy as number} r={6} fill="#f2c94c" /></g>)}
  {[[-60, -80], [60, -85], [-30, -95]].map(([dx, dy], i) => <ellipse key={"l" + i} cx={dx} cy={dy} rx={22} ry={9} fill="#4f8a3a" transform={`rotate(${dx > 0 ? -30 : 30} ${dx} ${dy})`} />)}
  {/* bình sứ xanh trắng */}
  <path d="M-28,-40 Q-30,-20 -48,0 Q-62,40 -36,70 L36,70 Q62,40 48,0 Q30,-20 28,-40 Z" fill="#f4f6fb" stroke="#1f3f8a" strokeWidth={4} />
  <path d="M-46,10 Q0,-5 46,10 M-50,35 Q0,20 50,35" stroke="#1f3f8a" strokeWidth={5} fill="none" />
  <circle cx={0} cy={22} r={10} fill="none" stroke="#2f5fb8" strokeWidth={4} /><path d="M-20,52 Q0,42 20,52" stroke="#2f5fb8" strokeWidth={4} fill="none" />
  <rect x={-30} y={-46} width={60} height={10} rx={4} fill="#1f3f8a" />
</g>;
const Desk: React.FC<{ x: number; y: number; s: number }> = ({ x, y, s }) => <g transform={`translate(${x},${y}) scale(${s})`}>
  <rect x={-150} y={-20} width={300} height={26} rx={6} fill="#6b3a1f" /><rect x={-150} y={-24} width={300} height={8} fill="#8a4f2a" />
  <rect x={-140} y={6} width={18} height={110} fill="#4f2a14" /><rect x={122} y={6} width={18} height={110} fill="#4f2a14" />
  <rect x={-130} y={6} width={260} height={60} fill="#5a3018" opacity={0.85} /><rect x={-60} y={22} width={120} height={8} rx={4} fill="#c9a64a" />
  {/* ghế bọc nhung */}
  <rect x={-55} y={-110} width={110} height={100} rx={18} fill="#5a1220" stroke="#3a2010" strokeWidth={8} /><rect x={-60} y={10} width={120} height={14} fill="#3a2010" />
  {/* sách + bút lông */}
  <rect x={-110} y={-36} width={70} height={14} fill="#1f4f3a" /><rect x={-104} y={-48} width={60} height={12} fill="#8a1f2a" /><line x1={60} y1={-26} x2={110} y2={-70} stroke="#f4f0e6" strokeWidth={5} />
</g>;
export const LopQT: React.FC = () => <AbsoluteFill>
  <svg width={W} height={H} viewBox={`0 0 ${W} ${H}`}>
    <defs>
      <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor="#bfe3ff" /><stop offset="1" stopColor="#eaf6ff" /></linearGradient>
      <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor="#efe2c4" /><stop offset="1" stopColor="#e2cfa6" /></linearGradient>
      <linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor="#7a4a28" /><stop offset="1" stopColor="#4a2a16" /></linearGradient>
      <radialGradient id="glow" cx="0.5" cy="0.15" r="0.8"><stop offset="0" stopColor="#fff3d0" stopOpacity="0.55" /><stop offset="1" stopColor="#fff3d0" stopOpacity="0" /></radialGradient>
      <pattern id="parq" width="80" height="40" patternUnits="userSpaceOnUse"><rect width="80" height="40" fill="url(#floor)" /><path d="M0,40 L40,0 M40,40 L80,0" stroke="#3a2010" strokeWidth={2} opacity={0.5} /></pattern>
    </defs>
    {/* tường + trần trang trí */}
    <rect width={W} height={HZ} fill="url(#wall)" />
    <rect width={W} height={70} fill="#d9c49a" /><rect y={70} width={W} height={16} fill="#b8862e" />
    {Array.from({ length: 24 }, (_, i) => <rect key={i} x={i * 82} y={40} width={50} height={22} rx={4} fill="#c9b07a" />)}
    {/* ốp gỗ chân tường */}
    <rect y={HZ - 170} width={W} height={170} fill="#6b3a1f" /><rect y={HZ - 178} width={W} height={12} fill="#b8862e" />
    {Array.from({ length: 12 }, (_, i) => <rect key={i} x={30 + i * 160} y={HZ - 150} width={130} height={120} rx={6} fill="none" stroke="#8a4f2a" strokeWidth={6} />)}
    {/* cửa sổ vòm */}
    <Window x={110} /><Window x={1580} />
    {/* bảng đen khung mạ vàng */}
    <rect x={430} y={112} width={1060} height={376} rx={10} fill="#c9a64a" /><rect x={446} y={128} width={1028} height={344} fill="#24463a" />
    <rect x={420} y={488} width={1080} height={18} rx={6} fill="#b8862e" />
    <path d="M430,112 l40,-40 h980 l40,40" fill="#d8b85a" />
    <text x={960} y={100} textAnchor="middle" fontFamily="serif" fontSize={34} fontWeight={700} fill="#5a3a12" letterSpacing={6}>SCIENTIA · POTENTIA · VIRTUS</text>
    {/* chân dung + kệ sách */}
    {[[270, 620], [1500, 620]].map(([x]) => null)}
    {/* đèn chùm */}
    <line x1={960} y1={0} x2={960} y2={40} stroke="#b8862e" strokeWidth={4} />
    <rect width={W} height={HZ} fill="url(#glow)" />
    <g transform="translate(960,40)">{[-150, -75, 0, 75, 150].map((dx, i) => <g key={i}><path d={`M0,30 Q${dx / 2},70 ${dx},60`} stroke="#b8862e" strokeWidth={4} fill="none" /><rect x={dx - 6} y={40} width={12} height={22} fill="#f6f0dc" /><ellipse cx={dx} cy={34} rx={7} ry={12} fill="#ffd36b" /><circle cx={dx} cy={34} r={26} fill="#fff1b8" opacity={0.35} /></g>)}
      <circle cx={0} cy={30} r={16} fill="#c9a64a" />{[-120, -60, 0, 60, 120].map((dx, i) => <path key={"c" + i} d={`M${dx},66 l-6,16 l6,10 l6,-10 Z`} fill="#e8f4ff" opacity={0.9} />)}</g>

    {/* sàn gỗ xương cá + thảm */}
    <rect y={HZ} width={W} height={H - HZ} fill="url(#parq)" />
    <path d={`M560,${HZ + 20} L1360,${HZ + 20} L1560,${H} L360,${H} Z`} fill="#7a1424" />
    <path d={`M590,${HZ + 36} L1330,${HZ + 36} L1510,${H - 10} L410,${H - 10} Z`} fill="none" stroke="#e0b54a" strokeWidth={6} />
    <path d={`M640,${HZ + 60} L1280,${HZ + 60} L1440,${H - 40} L480,${H - 40} Z`} fill="none" stroke="#c9a64a" strokeWidth={3} opacity={0.7} />
    {/* bục giảng gỗ gụ */}
    <rect x={200} y={HZ - 40} width={250} height={150} rx={10} fill="#5a2e14" /><rect x={190} y={HZ - 52} width={270} height={20} rx={6} fill="#8a4f2a" /><rect x={260} y={HZ} width={130} height={60} rx={6} fill="none" stroke="#c9a64a" strokeWidth={4} />
    {/* bình hoa sứ xanh trên kệ hai bên */}
    <rect x={1660} y={HZ - 10} width={170} height={110} rx={8} fill="#5a2e14" /><Vase x={1745} y={HZ - 80} s={1.05} />
    <rect x={30} y={HZ + 10} width={140} height={90} rx={8} fill="#5a2e14" /><Vase x={100} y={HZ - 55} s={0.85} />
    <Vase x={325} y={HZ - 125} s={0.55} />
    {/* bàn ghế học trò hai bên tiền cảnh */}
    <Desk x={210} y={H - 120} s={1.3} /><Desk x={1710} y={H - 120} s={1.3} />
  </svg>
</AbsoluteFill>;
