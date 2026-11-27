# F1 (27/11 Phòng Web) – Cổng kiểm tra mỗi lần đẩy mã: mở 10 trang mẫu ở 390px và 1440px qua máy chủ tĩnh tại chỗ,
# bắt lỗi JavaScript, lỗi CSP (chặn AdSense/GA/PostHog), tràn ngang ngoài khung cuộn, và khối quan trọng biến mất
# (bảng thế giới #thegioi, bảng giá #banggia, ô gửi mã #soima, thẻ Soi 3 dòng, khối Công cụ liên quan trang video).
# Có lỗi -> in danh sách và thoát mã 1 (Actions báo đỏ, GitHub gửi thư cho chủ kho). Chạy: python3 _kiem/cong_kiem.py
import os, sys, glob, threading, http.server, socketserver, functools
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def first(pat):
    L = sorted(glob.glob(os.path.join(ROOT, pat))); L = [x for x in L if not x.endswith("index.html")]
    return "/" + os.path.relpath(L[-1], ROOT) if L else None
PAGES = {  # trang: các khối bắt buộc (bộ chọn CSS)
    "/index.html": ["#thegioi", "#banggia", "#soima", "#bctc"],
    "/soi-ma-mien-phi.html": ["#soima"],
    "/ma/HPG.html": ["table.mt"],
    "/ma/index.html": [],
    "/f0/index.html": [],
    "/hoc/index.html": [".grid"],
    "/the-gioi-hang-hoa.html": [],
    "/dinh-gia-co-phieu.html": [],
    "/ket-qua-kinh-doanh-quy.html": [],
    "/mo-tai-khoan-chung-khoan.html": [],
}
h = first("hoc/*.html")
if h: PAGES[h] = ["section.cc form[action='/soi-ma-mien-phi.html']", ".vid iframe"]
f = first("f0/*.html")
if f: PAGES[f] = []
OV = """()=>{const W=document.documentElement.clientWidth;if(document.documentElement.scrollWidth<=W+2)return [];let bad=[];
for(const e of document.querySelectorAll('body *')){const r=e.getBoundingClientRect();if(r.width>0&&r.right>W+2){let p=e.parentElement,ok=false;
while(p){if(/(auto|scroll|hidden)/.test(getComputedStyle(p).overflowX)){ok=true;break}p=p.parentElement}
if(!ok){bad.push(e.tagName+'.'+String(e.className).slice(0,30)+':'+Math.round(r.right));if(bad.length>2)break}}}return bad}"""

class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), functools.partial(Q, directory=ROOT)); srv.daemon_threads = True
port = srv.server_address[1]; threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{port}"
loi = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for w in (390, 1440):
        ctx = b.new_context(viewport={"width": w, "height": 900}, is_mobile=(w < 500), has_touch=(w < 500))
        # chỉ tải tệp của web; chặn mạng ngoài để kết quả ổn định (lỗi CSP vẫn bắt được vì trình duyệt chặn trước khi gửi)
        ctx.route("**/*", lambda r: r.continue_() if r.request.url.startswith(BASE) else r.abort())
        for u, need in PAGES.items():
            if not os.path.exists(os.path.join(ROOT, u.lstrip("/"))): loi.append(f"{w}px {u}: KHÔNG CÒN TRANG"); continue
            pg = ctx.new_page(); errs = []
            pg.on("pageerror", lambda e: errs.append("JS: " + str(e)[:120]))
            pg.on("console", lambda m: errs.append("CSP: " + m.text[:140]) if m.type == "error" and "Content Security Policy" in m.text else None)
            try:
                pg.goto(BASE + u, wait_until="load", timeout=30000); pg.wait_for_timeout(1500)
                for e in errs: loi.append(f"{w}px {u}: {e}")
                for s in need:
                    if pg.locator(s).count() == 0: loi.append(f"{w}px {u}: mất khối {s}")
                for x in pg.evaluate(OV): loi.append(f"{w}px {u}: tràn ngang {x}")
            except Exception as ex:
                loi.append(f"{w}px {u}: không mở được ({str(ex)[:80]})")
            pg.close()
        ctx.close()
    b.close()
srv.shutdown()
print(f"Cổng kiểm F1: {len(PAGES)} trang × 2 khổ, {len(loi)} lỗi")
for x in loi: print(" -", x)
sys.exit(1 if loi else 0)
