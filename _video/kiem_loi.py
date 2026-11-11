# Tự kiểm văn phong lời thoại trước khi dựng (anh Huy 6/11: "viết lời thoại hơi kém, tự cải thiện, đừng để tôi sửa nhiều").
# Trả về danh sách lỗi; xưởng ghi vào KEY_qc.txt, NV3 không đăng nếu còn dòng "LỖI".
import re
CAM = [(r"\btôi\b|(?<!\d )(?<!người )\bbạn\b(?!\s*(bè|nào|học|đồng hành|đời|thân|[A-Z]{2,})\b)", "gọi 'bạn'/xưng 'tôi' – phải xưng em, gọi anh chị"),
       (r"không phải (là )?khuyến nghị|chia sẻ kiến thức", "câu miễn trừ – anh Huy đã bỏ"),
       (r"em là Huy|môi giới chứng khoán\.", "tự giới thiệu 'em là môi giới' – không cần"),
       (r"bình luận giúp em|để lại (giúp em )?một chữ", "câu cuối phải là câu hỏi mở thuần, không xin bình luận"),
       (r"\b(OK|ok|wow|(?<!nhập )(?<!xuất )siêu|cực kỳ khủng|bùng nổ|x\d+ tài khoản)\b", "từ giật gân/thiếu chuẩn mực")]
CHU_NGU = r"\b(em|anh chị|ngân hàng|nhà nước|NHNN|thị trường|cổ phiếu|doanh nghiệp|công ty|giá|lãi suất|đây|điều|số tiền|khoản|kỳ hạn|tin|mốc|hợp đồng|hai bên|nhà đầu tư|dòng tiền|lợi nhuận|vốn|họ|nó|các|mỗi|như vậy|vì vậy|tuy nhiên|theo|nếu|khi|trong|sau|từ|với|hạn mức|quy mô|chênh|đợt|cơ chế|hoán đổi|[A-Z]{3}\b)"
def kiem(canh, cau_hoi=None, tin_nong=True):
    loi = []
    for i, c in enumerate(canh):
        t = c.get("loi", "")
        for pat, ly in CAM:
            if "miễn trừ" in ly and not tin_nong: continue
            if re.search(pat, t, re.I if "bạn" not in pat else 0): loi.append("LỖI cảnh %d: %s" % (i + 1, ly))
        for s in re.split(r"(?<=[.!?])\s+", t.strip()):
            w = s.split()
            if 0 < len(w) < 6 and not re.search(CHU_NGU, s, re.I): loi.append(("LỖI" if tin_nong else "CẢNH BÁO") + " cảnh %d: câu cụt thiếu chủ ngữ – \"%s\"" % (i + 1, s))
            if len(w) > 38: loi.append("CẢNH BÁO cảnh %d: câu quá dài (%d từ) – tách đôi" % (i + 1, len(w)))
        if re.search(r"\b(\w+) \1\b", t, re.I): loi.append("CẢNH BÁO cảnh %d: lặp từ liền nhau" % (i + 1))
    if tin_nong and canh:
        t0 = canh[0].get("loi", "")
        if len(t0.split()) < 15 or not re.search(r"\bvừa\b|\bhôm nay\b|\bsáng nay\b|\bchiều nay\b|\btối qua\b|\bphiên\b", t0, re.I):
            loi.append("LỖI cảnh 1: chưa nói rõ TIN GÌ (ai – vừa làm gì – bao nhiêu – khi nào)")
    if cau_hoi is not None:
        q = cau_hoi.get("loi", "")
        if not q.strip().endswith("?"): loi.append("LỖI câu kết: phải là câu hỏi mở, kết bằng dấu ?")
        if not re.search(r"anh chị", q, re.I): loi.append("CẢNH BÁO câu kết: nên hỏi thẳng 'anh chị'")
    return loi
