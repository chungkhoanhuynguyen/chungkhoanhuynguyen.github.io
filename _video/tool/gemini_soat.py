# -*- coding: utf-8 -*-
# gemini_soat.py OUTDIR KEY – Gemini (khóa miễn phí, secret GEMINI_API_KEY) xem tấm khung + bìa + Shorts, liệt kê LỖI HÌNH.
# Chỉ là lớp soát sơ bộ chạy miễn phí trên GitHub; KHÔNG thay cổng duyệt của QL1. Kết quả in ra (tu_soat.sh ghi vào KEY_soat.txt).
import base64, json, os, sys, time, urllib.request, urllib.error
O, K = sys.argv[1], sys.argv[2]
anh = [f for f in (f"{K}_khung1.png", f"{K}_khung2.png", f"{K}_bia3.png", f"{K}_shorts.png") if os.path.exists(os.path.join(O, f))]
if not anh:
    print("== GEMINI: không có ảnh để xem"); sys.exit(0)
yeu_cau = ("Bạn là người soát video tài chính tiếng Việt cho kênh YouTube Chứng Khoán Huy Nguyễn. Các ảnh: lưới khung hình video "
           "(mỗi ô cách 20 giây, góc trái có mốc giờ), 3 ảnh bìa A/B/C, khung 3 Shorts. Chỉ liệt kê LỖI NHÌN THẤY ĐƯỢC, mỗi lỗi 1 dòng "
           "'mốc giờ hoặc tên ảnh – lỗi': chữ tràn/bị cắt/đè nhau, chữ sai chính tả tiếng Việt, ô số hoặc thẻ trống, ảnh lạc đề hoặc mờ, "
           "ảnh người thật/người nổi tiếng, logo doanh nghiệp/ngân hàng thật, cờ hoặc địa danh nước ngoài lạc đề, chữ 'MBS' hoặc 'môi giới', "
           "dấu '~' trên màn hình, bìa khó đọc trên điện thoại. Không có lỗi thì ghi đúng 1 dòng: KHÔNG THẤY LỖI HÌNH. "
           "Không chấm điểm, không khen, không bịa lỗi.")
parts = [{"text": yeu_cau}] + [{"inline_data": {"mime_type": "image/png", "data": base64.b64encode(open(os.path.join(O, f), "rb").read()).decode()}} for f in anh]
# QL1 23/11: 2.5-flash/2.0-flash trả 404 (mô hình đổi tên/ngừng) → hỏi danh sách mô hình, lấy bản flash mới nhất còn generateContent.
ds = [os.environ.get("GEMINI_MODEL", ""), "gemini-flash-latest"]  # QL1 24/11: bản này chạy được (NONG2411A); omni/banana/preview 429
try:
    rq0 = urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/models?pageSize=200", headers={"x-goog-api-key": os.environ["GEMINI_API_KEY"]})
    md = json.load(urllib.request.urlopen(rq0, timeout=60)).get("models", [])
    ten = [m["name"].split("/")[-1] for m in md if "generateContent" in m.get("supportedGenerationMethods", [])]
    flash = sorted([t for t in ten if "flash" in t and not any(x in t for x in ("lite","image","tts","live","exp","omni","banana","preview","audio"))], reverse=True)
    ds += flash[:3] + sorted([t for t in ten if "pro" in t and not any(x in t for x in ("tts","image","banana","preview","omni"))], reverse=True)[:1]
except Exception as e:
    print(f"== GEMINI không đọc được danh sách mô hình: {type(e).__name__}: {str(e)[:150]}")
ds += ["gemini-flash-latest", "gemini-2.5-flash"]
# QL1 25/11: 503 (quá tải) / 429 (hết lượt) là lỗi tạm → chờ rồi thử lại; thêm bản flash-lite (hạn mức riêng) làm dự phòng cuối.
try: ds += sorted([t for t in ten if "flash-lite" in t and not any(x in t for x in ("image","tts","live","preview"))], reverse=True)[:2]
except NameError: pass
ds += ["gemini-flash-lite-latest"]
ds = [m for i, m in enumerate(ds) if m and m not in ds[:i]]
def goi(mo_hinh):
    rq = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{mo_hinh}:generateContent",
        data=json.dumps({"contents": [{"parts": parts}], "generationConfig": {"temperature": 0.1}}).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
    return json.load(urllib.request.urlopen(rq, timeout=120))
for vong in range(3):
  for mo_hinh in ds:
    try:
        d = goi(mo_hinh)
        tl = "".join(p.get("text", "") for p in d["candidates"][0]["content"]["parts"]).strip()
        print(f"== GEMINI ({mo_hinh}) xem {', '.join(anh)} – soát sơ bộ, QL1 vẫn duyệt bằng mắt:")
        print(tl[:3000]); sys.exit(0)
    except urllib.error.HTTPError as e:
        print(f"== GEMINI {mo_hinh} vòng {vong+1} lỗi: HTTP {e.code}")
    except Exception as e:
        print(f"== GEMINI {mo_hinh} vòng {vong+1} lỗi: {type(e).__name__}: {str(e)[:150]}")
  if vong < 2: time.sleep(45 * (vong + 1))
print("== GEMINI: hết 3 vòng vẫn lỗi (quá tải phía Google) – QL1 soát bằng mắt như thường")
sys.exit(0)
