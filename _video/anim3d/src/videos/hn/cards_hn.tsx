// Thẻ tin tức / giấy tờ CỠ LỚN cho phim #3 (anh Huy 14/11: "tin tức hình ảnh giấy tờ hiện rõ hơn trên màn hình, đừng qua loa").
// Nguyên tắc: 1 tin = 1 màn hình; tiêu đề ≥ 64px; câu quan trọng tô vàng chạy dần; giữ đủ lâu để đọc; luôn có tên báo + ngày.
import React from "react";
import { AbsoluteFill, Img, staticFile } from "remotion";
import { F, sm } from "../vang/cards";

const pop = (x: number) => { x = Math.max(0, Math.min(1, x)); return 1 - Math.pow(1 - x, 3); };

/** Bài báo chiếm trọn màn hình: tên báo + chuyên mục + ngày, tiêu đề to, ảnh lớn, đoạn trích tô vàng dần. */
export const Article: React.FC<{ t: number; src: string; srcCol?: string; cat: string; date: string; head: string; img?: string; credit?: string; quote: string; hiAt?: number; tail?: string; dark?: boolean }> =
  ({ t, src, srcCol = "#b3131f", cat, date, head, img, credit, quote, hiAt = 1.6, tail, dark }) => {
  const a = pop(t / 0.5), z = 1 + 0.035 * Math.min(1, t / 8), hi = Math.max(0, Math.min(1, (t - hiAt) / 1.6));
  const bg = dark ? "#121420" : "#f6f3ec", fg = dark ? "#f2f2f2" : "#16171c", mute = dark ? "#9aa0b4" : "#6b6b72";
  return <AbsoluteFill style={{ background: "#0b0d16", fontFamily: F }}>
    <div style={{ position: "absolute", left: 90, top: 50, right: 90, bottom: 170, background: bg, borderRadius: 18, overflow: "hidden", boxShadow: "0 30px 80px rgba(0,0,0,.6)", transform: `translateY(${(1 - a) * 60}px) scale(${0.96 + 0.04 * a})`, opacity: a }}>
      <div style={{ height: 86, background: srcCol, display: "flex", alignItems: "center", padding: "0 40px", gap: 26 }}>
        <div style={{ fontSize: 46, fontWeight: 900, color: "#fff", letterSpacing: 1 }}>{src}</div>
        <div style={{ fontSize: 28, fontWeight: 700, color: "rgba(255,255,255,.85)", borderLeft: "2px solid rgba(255,255,255,.5)", paddingLeft: 22 }}>{cat}</div>
        <div style={{ marginLeft: "auto", fontSize: 28, fontWeight: 700, color: "#fff" }}>{date}</div>
      </div>
      <div style={{ display: "flex", height: "calc(100% - 86px)" }}>
        <div style={{ flex: img ? "0 0 54%" : "1 1 auto", padding: img ? "40px 46px" : "60px 80px", display: "flex", flexDirection: "column", gap: img ? 28 : 44, justifyContent: img ? "flex-start" : "center" }}>
          <div style={{ fontSize: img ? 62 : 92, lineHeight: 1.12, fontWeight: 900, color: fg }}>{head}</div>
          <div style={{ fontSize: img ? 40 : 56, lineHeight: 1.45, fontWeight: 700, color: fg }}>
            <span style={{ backgroundImage: "linear-gradient(#ffe14d,#ffe14d)", backgroundRepeat: "no-repeat", backgroundSize: `${hi * 100}% 100%`, padding: "2px 4px", boxDecorationBreak: "clone", WebkitBoxDecorationBreak: "clone", color: hi > 0.05 ? "#111" : fg } as React.CSSProperties}>{quote}</span>
          </div>
          {tail ? <div style={{ fontSize: img ? 30 : 34, color: mute, fontWeight: 600 }}>{tail}</div> : null}
        </div>
        {img ? <div style={{ flex: "1 1 auto", position: "relative", overflow: "hidden" }}>
          <Img src={staticFile(img)} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${z})` }} />
          {credit ? <div style={{ position: "absolute", right: 12, bottom: 10, fontSize: 18, color: "#fff", background: "rgba(0,0,0,.55)", padding: "3px 10px", borderRadius: 6 }}>{credit}</div> : null}
        </div> : null}
      </div>
    </div>
  </AbsoluteFill>;
};

/** Cảnh báo khẩn trên điện thoại (to, đỏ, rung). */
export const AlertCard: React.FC<{ t: number; title: string; body: string; time: string; fake?: number }> = ({ t, title, body, time, fake }) => {
  const a = pop(t / 0.25), sh = t < 2 ? Math.sin(t * 60) * 6 * (1 - t / 2) : 0, fk = fake !== undefined ? sm((t - fake) / 0.5) : 0;
  return <AbsoluteFill style={{ background: `radial-gradient(circle at 50% 40%, rgba(200,20,30,${0.55 + 0.25 * Math.abs(Math.sin(t * 5))}), #120206 70%)`, fontFamily: F, justifyContent: "center", alignItems: "center" }}>
    <div style={{ width: 620, height: 940, borderRadius: 70, background: "#0c0d12", border: "10px solid #2a2c34", transform: `translateX(${sh}px) scale(${0.9 + 0.1 * a})`, position: "relative", overflow: "hidden" }}>
      <div style={{ textAlign: "center", color: "#fff", fontSize: 92, fontWeight: 300, marginTop: 70 }}>{time}</div>
      <div style={{ margin: "40px 28px", background: "#f2f2f4", borderRadius: 34, padding: "30px 30px" }}>
        <div style={{ fontSize: 30, fontWeight: 900, color: "#d0101e" }}>⚠ CẢNH BÁO KHẨN CẤP</div>
        <div style={{ fontSize: 52, fontWeight: 900, color: "#111", marginTop: 14, lineHeight: 1.1 }}>{title}</div>
        <div style={{ fontSize: 34, fontWeight: 600, color: "#222", marginTop: 16, lineHeight: 1.35 }}>{body}</div>
      </div>
      {fake !== undefined && fk > 0 ? <div style={{ margin: "0 28px", background: "#fff7d6", borderRadius: 30, padding: "24px 28px", opacity: fk, transform: `translateY(${(1 - fk) * 40}px)` }}>
        <div style={{ fontSize: 28, fontWeight: 900, color: "#1d6b3a" }}>Tin nhắn nhà mạng · 23:20</div>
        <div style={{ fontSize: 36, fontWeight: 800, color: "#111", marginTop: 8 }}>Cảnh báo vừa rồi là GIẢ, do kẻ xấu phát tán. Không làm theo.</div>
      </div> : null}
    </div>
  </AbsoluteFill>;
};

type Row = { sym: string; ref: number; px: number; vol?: string; at: number };
/** Bảng giá chứng khoán như thật (số thật phiên 13/11/2026). */
export const BoardCard: React.FC<{ t: number; title: string; time: string; rows: Row[]; idx?: { name: string; v: string; ch: string; col: string }; note?: string; noteAt?: number }> = ({ t, title, time, rows, idx, note, noteAt = 3 }) => {
  const col = (r: Row) => (r.px > r.ref ? "#2fd36b" : r.px < r.ref ? "#ff4d5e" : "#ffd23f");
  const fmt = (x: number) => (x / 1000).toFixed(2).replace(".", ",");
  return <AbsoluteFill style={{ background: "#05070d", fontFamily: F, padding: "60px 110px" }}>
    <div style={{ display: "flex", alignItems: "center", color: "#cfd6ea", fontSize: 34, fontWeight: 800, opacity: sm(t / 0.3) }}>
      <div>{title}</div><div style={{ marginLeft: "auto", color: "#ffd23f" }}>{time}</div>
      {idx ? <div style={{ marginLeft: 40, color: idx.col }}>{idx.name} {idx.v} ({idx.ch})</div> : null}
    </div>
    <div style={{ marginTop: 30, border: "2px solid #1d2233", borderRadius: 14, overflow: "hidden" }}>
      <div style={{ display: "grid", gridTemplateColumns: "1.2fr 1fr 1.3fr 1fr 1.3fr", background: "#121726", color: "#8a93ad", fontSize: 30, fontWeight: 800, padding: "18px 30px" }}>
        <div>MÃ</div><div>THAM CHIẾU</div><div>GIÁ KHỚP</div><div>+/-</div><div>KHỐI LƯỢNG</div></div>
      {rows.map((r, i) => { const a = sm((t - r.at) / 0.35), c = col(r), ch = ((r.px - r.ref) / r.ref) * 100, flash = t - r.at < 0.6 && t > r.at;
        return <div key={i} style={{ display: "grid", gridTemplateColumns: "1.2fr 1fr 1.3fr 1fr 1.3fr", padding: "22px 30px", fontSize: 50, fontWeight: 900, borderTop: "2px solid #151a28", opacity: a, background: flash ? "rgba(255,77,94,.18)" : "transparent" }}>
          <div style={{ color: c }}>{r.sym}</div><div style={{ color: "#ffd23f" }}>{fmt(r.ref)}</div><div style={{ color: c }}>{fmt(r.px)}</div>
          <div style={{ color: c }}>{ch > 0 ? "+" : ""}{ch.toFixed(1).replace(".", ",")}%</div><div style={{ color: "#cfd6ea", fontSize: 40 }}>{r.vol ?? ""}</div></div>; })}
    </div>
    {note ? <div style={{ marginTop: 34, fontSize: 40, fontWeight: 800, color: "#fff", opacity: sm((t - noteAt) / 0.4) }}>{note}</div> : null}
    <div style={{ position: "absolute", left: 110, bottom: 160, fontSize: 24, color: "#6b7390" }}>Giá đơn vị nghìn đồng – số liệu thật phiên 13/11/2026 (WiData). Minh hoạ câu chuyện, không phải khuyến nghị.</div>
  </AbsoluteFill>;
};

/** Bảng giá vàng tiệm (mua vào / bán ra) + chênh lệch. */
export const GoldBoard: React.FC<{ t: number; rows: { name: string; buy: string; sell: string; at: number }[]; spreadAt?: number; spread?: string; shop?: string; date?: string; dream?: boolean }> = ({ t, rows, spreadAt = 3, spread, shop = "BẢO TÍN MINH ANH", date = "", dream }) => (
  <AbsoluteFill style={{ background: dream ? "radial-gradient(circle,#3a0a0a,#0a0202)" : "linear-gradient(#5a0a0f,#2a0306)", fontFamily: F, justifyContent: "center", alignItems: "center" }}>
    <div style={{ width: 1400, border: "6px solid #e8b94a", borderRadius: 24, background: "#140204", padding: "36px 50px", boxShadow: "0 0 80px rgba(232,185,74,.35)", opacity: sm(t / 0.3) }}>
      <div style={{ display: "flex", alignItems: "center", color: "#ffd86b", fontSize: 54, fontWeight: 900 }}><div>{shop}</div><div style={{ marginLeft: "auto", fontSize: 32, color: "#f4e6c4" }}>{date}</div></div>
      <div style={{ display: "grid", gridTemplateColumns: "1.6fr 1fr 1fr", marginTop: 24, fontSize: 34, color: "#e8b94a", fontWeight: 800 }}><div>LOẠI VÀNG (triệu đồng/lượng)</div><div>MUA VÀO</div><div>BÁN RA</div></div>
      {rows.map((r, i) => <div key={i} style={{ display: "grid", gridTemplateColumns: "1.6fr 1fr 1fr", marginTop: 16, fontSize: 64, fontWeight: 900, color: "#fff", opacity: sm((t - r.at) / 0.25), fontVariantNumeric: "tabular-nums" }}>
        <div style={{ fontSize: 46 }}>{r.name}</div><div style={{ color: "#5be38a" }}>{r.buy}</div><div style={{ color: "#ff6b6b" }}>{r.sell}</div></div>)}
      {spread ? <div style={{ marginTop: 30, fontSize: 48, fontWeight: 900, color: "#111", background: "#ffe14d", display: "inline-block", padding: "10px 26px", borderRadius: 12, opacity: sm((t - spreadAt) / 0.35) }}>{spread}</div> : null}
    </div>
  </AbsoluteFill>
);

/** Đồng hồ Tận thế: kim tiến về 12 giờ, chữ "85 GIÂY". */
export const DoomClock: React.FC<{ t: number }> = ({ t }) => {
  const ang = -90 + 360 * (1 - 85 / 3600) * Math.min(1, 0.985 + 0.015 * sm(t / 2)), s = sm(t / 0.5);
  return <AbsoluteFill style={{ background: "radial-gradient(circle,#1a1d2b,#05060a)", fontFamily: F, justifyContent: "center", alignItems: "center" }}>
    <div style={{ display: "flex", alignItems: "center", gap: 90, opacity: s }}>
      <svg width="560" height="560" viewBox="-110 -110 220 220">
        <path d="M0 -100 A100 100 0 0 1 100 0 L0 0Z" fill="none" stroke="#e8e8e8" strokeWidth="3" />
        {Array.from({ length: 12 }, (_, i) => <line key={i} x1="0" y1="-92" x2="0" y2="-80" stroke="#fff" strokeWidth="4" transform={`rotate(${i * 30})`} />)}
        <line x1="0" y1="0" x2="0" y2="-88" stroke="#ff3b3b" strokeWidth="6" strokeLinecap="round" transform={`rotate(${ang + 90})`} />
        <circle r="7" fill="#ff3b3b" />
      </svg>
      <div style={{ color: "#fff" }}>
        <div style={{ fontSize: 46, fontWeight: 800, color: "#c9cee0" }}>ĐỒNG HỒ TẬN THẾ – 27/01/2026</div>
        <div style={{ fontSize: 190, fontWeight: 900, color: "#ff4d5e", lineHeight: 1 }}>85 GIÂY</div>
        <div style={{ fontSize: 56, fontWeight: 900 }}>trước nửa đêm – gần nhất lịch sử</div>
        <div style={{ fontSize: 28, color: "#8a93ad", marginTop: 20 }}>Nguồn: Bulletin of the Atomic Scientists</div>
      </div>
    </div>
  </AbsoluteFill>;
};

/** Ba lần thế giới hoảng loạn: giảm rồi hồi (minh hoạ xu hướng, có ghi chú). */
export const HistoryCard: React.FC<{ t: number; items: { yr: string; name: string; note: string; at: number }[] }> = ({ t, items }) => (
  <AbsoluteFill style={{ background: "#0b0e1a", fontFamily: F, padding: "70px 100px" }}>
    <div style={{ fontSize: 62, fontWeight: 900, color: "#fff", opacity: sm(t / 0.4) }}>Mỗi lần thế giới hoảng loạn, chứng khoán đã đi thế nào?</div>
    <div style={{ display: "flex", gap: 40, marginTop: 50 }}>
      {items.map((it, i) => { const a = sm((t - it.at) / 0.5), p = Math.max(0, Math.min(1, (t - it.at) / 2.2));
        const pts = [[0, 40], [60, 52], [110, 120], [160, 100], [220, 70], [300, 30]].map(([x, y]) => [x, y] as [number, number]);
        const n = Math.max(2, Math.ceil(p * pts.length)); const d = pts.slice(0, n).map((q, k) => (k ? "L" : "M") + q[0] + " " + q[1]).join(" ");
        return <div key={i} style={{ flex: 1, background: "#141a2c", borderRadius: 22, padding: "30px 30px", opacity: a, transform: `translateY(${(1 - a) * 40}px)` }}>
          <div style={{ fontSize: 80, fontWeight: 900, color: "#ffd23f" }}>{it.yr}</div>
          <div style={{ fontSize: 40, fontWeight: 900, color: "#fff", marginTop: 6, minHeight: 100 }}>{it.name}</div>
          <svg width="300" height="150" style={{ marginTop: 10 }}><path d={d} fill="none" stroke={p > 0.6 ? "#2fd36b" : "#ff4d5e"} strokeWidth="8" strokeLinecap="round" strokeLinejoin="round" /></svg>
          <div style={{ fontSize: 32, fontWeight: 700, color: "#cfd6ea", marginTop: 10 }}>{it.note}</div>
        </div>; })}
    </div>
    <div style={{ position: "absolute", left: 100, bottom: 160, fontSize: 26, color: "#6b7390" }}>Đường vẽ minh hoạ xu hướng chung, không phải biểu đồ giá chính xác.</div>
  </AbsoluteFill>
);
