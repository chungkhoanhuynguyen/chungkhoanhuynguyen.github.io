// Cloudflare Worker cho trang chungkhoanhuynguyen.com/hoidapm
// Biến môi trường cần đặt trong Cloudflare (Settings → Variables and Secrets, loại "Secret"):
//   ANTHROPIC_API_KEY : khóa API lấy ở console.anthropic.com
//   MAT_KHAU          : mật khẩu vào trang
// Không ghi khóa hay mật khẩu vào file này.

const MODEL = "claude-sonnet-5-5";
const ALLOWED_ORIGINS = [
  "https://chungkhoanhuynguyen.com",
  "https://www.chungkhoanhuynguyen.com",
  "https://chungkhoanhuynguyen.github.io",
];

const SYSTEM = `Bạn là trợ lý nói chuyện bằng giọng nói của anh Huy (làm trong ngành chứng khoán ở Việt Nam).
Câu trả lời sẽ được ĐỌC TO bằng giọng máy, nên:
- Nói tiếng Việt tự nhiên như người thật đang nói chuyện, xưng "em", gọi "anh".
- Ngắn gọn: thường 2–5 câu. Đi thẳng vào ý chính trước, nếu anh hỏi thêm mới giải thích sâu.
- Tuyệt đối không dùng markdown, gạch đầu dòng, ký hiệu, bảng, emoji hay đường link. Viết số theo cách đọc dễ nghe.
- Nếu cần thông tin mới (giá, tin tức, số liệu hôm nay) thì dùng công cụ tìm kiếm; không bịa số liệu. Không chắc thì nói rõ là không chắc.
- Về đầu tư: đưa thông tin và cách nghĩ để anh tự quyết, không hô mua bán chắc chắn.
- Nếu câu hỏi mơ hồ, hỏi lại một câu ngắn.`;

function cors(origin) {
  const ok = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    "Access-Control-Allow-Origin": ok,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Vary": "Origin",
  };
}

function json(data, status, origin) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", ...cors(origin) },
  });
}

// So sánh chuỗi không lộ thời gian
function sameText(a, b) {
  const x = new TextEncoder().encode(String(a || ""));
  const y = new TextEncoder().encode(String(b || ""));
  let diff = x.length ^ y.length;
  for (let i = 0; i < Math.max(x.length, y.length); i++) diff |= (x[i] || 0) ^ (y[i] || 0);
  return diff === 0;
}

// Chặn đoán mật khẩu: tối đa 8 lần sai / 15 phút / IP (bộ nhớ trong 1 máy chủ, đủ cho dùng cá nhân)
const fails = new Map();
function tooMany(ip) {
  const r = fails.get(ip);
  if (!r) return false;
  if (Date.now() - r.t > 15 * 60 * 1000) { fails.delete(ip); return false; }
  return r.n >= 8;
}
function addFail(ip) {
  const r = fails.get(ip) || { n: 0, t: Date.now() };
  r.n++; fails.set(ip, r);
}

export default {
  async fetch(req, env) {
    const origin = req.headers.get("Origin") || "";
    if (req.method === "OPTIONS") return new Response(null, { headers: cors(origin) });
    if (req.method !== "POST") return json({ loi: "Chỉ nhận POST" }, 405, origin);
    if (origin && !ALLOWED_ORIGINS.includes(origin)) return json({ loi: "Không được phép" }, 403, origin);

    const ip = req.headers.get("CF-Connecting-IP") || "?";
    if (tooMany(ip)) return json({ loi: "Sai mật khẩu quá nhiều lần, thử lại sau 15 phút." }, 429, origin);

    let body;
    try { body = await req.json(); } catch { return json({ loi: "Dữ liệu không hợp lệ" }, 400, origin); }

    if (!env.MAT_KHAU || !sameText(body.matkhau, env.MAT_KHAU)) {
      addFail(ip);
      return json({ loi: "Sai mật khẩu" }, 401, origin);
    }
    fails.delete(ip);

    if (body.kiemtra) return json({ ok: true }, 200, origin);

    // Lịch sử hội thoại: chỉ giữ 12 lượt gần nhất, mỗi lượt tối đa 2000 ký tự
    const msgs = (Array.isArray(body.lichsu) ? body.lichsu : [])
      .filter(m => m && (m.role === "user" || m.role === "assistant") && typeof m.content === "string" && m.content.trim())
      .slice(-12)
      .map(m => ({ role: m.role, content: m.content.slice(0, 2000) }));
    if (!msgs.length || msgs[msgs.length - 1].role !== "user") return json({ loi: "Chưa có câu hỏi" }, 400, origin);
    while (msgs.length && msgs[0].role !== "user") msgs.shift();

    const now = new Date().toLocaleString("vi-VN", { timeZone: "Asia/Ho_Chi_Minh" });
    const r = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "x-api-key": env.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify({
        model: MODEL,
        max_tokens: 700,
        system: SYSTEM + `\nThời điểm hiện tại ở Việt Nam: ${now}.`,
        messages: msgs,
        tools: [{ type: "web_search_20250305", name: "web_search", max_uses: 2 }],
      }),
    });

    const data = await r.json().catch(() => ({}));
    if (!r.ok) {
      const msg = data?.error?.message || `Lỗi API ${r.status}`;
      return json({ loi: msg }, 502, origin);
    }
    const text = (data.content || [])
      .filter(b => b.type === "text")
      .map(b => b.text)
      .join("")
      .replace(/[*#_`>|]/g, "")
      .replace(/https?:\/\/\S+/g, "")
      .trim();
    return json({ traloi: text || "Em chưa có câu trả lời, anh hỏi lại giúp em nhé." }, 200, origin);
  },
};
