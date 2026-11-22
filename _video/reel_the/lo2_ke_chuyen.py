"""Lô 2 reel thẻ – bản KỂ CHUYỆN (anh Huy 22/11: bản cũ cụt, không có câu chuyện).
Khuôn: hook → tình huống → cú bất ngờ → lời giải → kỹ thuật 1 cảnh → bỏ ngỏ + góc nhìn → kết hỏi.
Giữ phần hình đã soát số của <mã>.json cũ, bỏ S5A/S5B, viết lại lời đọc + phụ đề + mốc 'at'.
Chạy: python3 lo2_ke_chuyen.py  -> ghi đè <mã>.json và <mã>_kb.json (bản cũ ở git)."""
import json, os, re, copy
HERE = os.path.dirname(os.path.abspath(__file__))

def chunks(sub, MAX=40):
    """Chia phụ đề 1 câu thành dòng <= MAX ký tự (không tính **), ưu tiên ngắt sau dấu phẩy/hai chấm, không cắt giữa **...**."""
    L = lambda x: len(x.replace("**", ""))
    parts = [p.strip() for p in re.split(r"(?<=[,:;])\s+", sub) if p.strip()]
    out = []
    for p in parts:
        cur = ""
        for w in p.split():
            nx = (cur + " " + w).strip()
            if cur and L(nx) > MAX and cur.count("**") % 2 == 0:
                out.append(cur); cur = w
            else: cur = nx
        if cur:
            if out and (L(out[-1] + " " + cur) <= 26 or (L(cur) <= 9 and L(out[-1] + " " + cur) <= 48)) and out[-1].count("**") % 2 == 0: out[-1] += " " + cur
            else: out.append(cur)
    res = []  # dòng quá ngắn ở đầu (vd "**Một**,") thì gộp với dòng sau
    for c in out:
        if res and L(res[-1]) < 9: res[-1] += " " + c
        else: res.append(c)
    return res

# Mỗi cảnh: id, đè (dict ghi đè lên cảnh cũ), câu [(lời đọc, phụ đề)]
L = {}
L["stb"] = [
 ("S1", {}, [("Sacombank giảm bốn nghìn hai trăm chín mươi mốt nhân viên chỉ trong chín tháng.", "Sacombank giảm **4.291** nhân viên chỉ trong **9 tháng**"),
             ("Vậy mà lợi nhuận lại mất hơn một nửa, chuyện gì đã xảy ra?", "Vậy mà lợi nhuận mất **hơn một nửa**, chuyện gì đã xảy ra?")]),
 ("S2", {"chuong": "— CHUYỆN BẮT ĐẦU —", "chot": {"a": "NHÂN SỰ −27%", "b": "CIR CÒN 32,6%", "do": 1, "at": [2, 0.7]}},
  [("Đầu năm, Sacombank có gần mười lăm nghìn chín trăm người.", "Đầu năm, Sacombank có gần **15.900** người"),
   ("Tới cuối tháng chín chỉ còn mười một nghìn năm trăm sáu mươi, cứ bốn người thì gần một người đã rời đi.", "Cuối tháng 9 còn **11.560**, cứ **4 người** thì gần **1 người** rời đi"),
   ("Bộ máy gọn hẳn: chi phí nhân viên giảm hai mươi hai phần trăm, chi phí trên thu nhập từ bốn mươi sáu phẩy một xuống ba mươi hai phẩy sáu phần trăm.", "Bộ máy gọn hẳn: chi phí nhân viên **−22%**, chi phí trên thu nhập từ **46,1%** xuống **32,6%**")]),
 ("S3", {"chuong": "— CÚ BẤT NGỜ —", "chot": {"a": "CẮT CHI PHÍ", "b": "MÀ LÃI VẪN −50,8%", "do": 1, "at": [2, 0.9]},
         "_the_at": [[1, 0.1], [1, 0.7], [2, 0.1], [2, 0.6]]},
  [("Ai cũng nghĩ cắt được chi phí thì lãi phải tăng.", "Ai cũng nghĩ cắt chi phí thì **lãi phải tăng**"),
   ("Nhưng lãi sau thuế chín tháng chỉ còn bốn nghìn hai trăm bảy mươi tám tỷ, giảm năm mươi phẩy tám phần trăm.", "Nhưng lãi sau thuế 9 tháng chỉ còn **4.278 tỷ**, giảm **50,8%**"),
   ("Nợ xấu leo lên bảy phẩy ba ba phần trăm, cổ phiếu cũng lùi chín phần trăm từ đỉnh.", "Nợ xấu leo lên **7,33%**, cổ phiếu lùi **9%** từ đỉnh")]),
 ("S4", {"chuong": "— TIỀN ĐI ĐÂU —",
         "muc": [{"so": "TĂNG 14,1%", "t": "Tổng thu nhập 27.794 tỷ", "at": [1, 0.3], "co": 84},
                 {"so": "DỰ PHÒNG ×6", "t": "Gấp gần 6 lần: 12.848 tỷ", "at": [2, 0.4], "co": 84},
                 {"so": "NỢ XẤU 7,33%", "t": "Đầu năm 6,41%", "at": [3, 0.3], "co": 84, "mau": "#c9533e"}],
         "chot": {"a": "THU NHẬP VẪN TĂNG", "b": "LÃI DÀNH ĐỂ GÁNH NỢ XẤU", "at": [3, 0.85]}},
  [("Vậy tiền đi đâu?", "Vậy **tiền đi đâu?**"),
   ("Thu nhập không hề yếu: tổng thu nhập vẫn tăng mười bốn phẩy một phần trăm.", "Thu nhập không yếu: tổng thu nhập vẫn **+14,1%**"),
   ("Phần lớn được trích ra dự phòng, từ hai nghìn một trăm năm mươi hai lên mười hai nghìn tám trăm bốn mươi tám tỷ, gấp gần sáu lần.", "Phần lớn trích ra **dự phòng**, từ **2.152** lên **12.848 tỷ**, gấp gần **6 lần**"),
   ("Nói dễ hiểu, Sacombank đang dùng lãi để gánh nợ xấu.", "Nói dễ hiểu: Sacombank đang dùng lãi để **gánh nợ xấu**")]),
 ("S5", {"marks": "_keep", "_mark_at": [[0, 0.5], [1, 0.7]], "_vung_at": [[1, 0.15], [1, 0.6]], "_chot_at": [1, 0.92]},
  [("Trên biểu đồ, đường trung bình hai mươi đã cắt xuống đường năm mươi từ ngày tám tháng mười.", "Trên biểu đồ, **MA20 cắt xuống MA50** từ ngày **8/10**"),
   ("Giá đang kẹt giữa vùng cản bảy mươi hai đến bảy mươi ba và hỗ trợ sáu mươi lăm phẩy một đến sáu mươi sáu.", "Giá kẹt giữa cản **72–73** và hỗ trợ **65,1–66**")]),
 ("S5C", {"_muc_at": [[2, 0.0], [3, 0.0], [4, 0.0]], "_chot_at": [4, 0.6], "_muc3": {"t": "Hướng xử lý 32,5% cổ phần", "s": "Ngân hàng Nhà nước khởi động lại"}},
  [("Câu chuyện vẫn còn bỏ ngỏ, vì Ngân hàng Nhà nước vừa khởi động lại việc xử lý ba mươi hai phẩy năm phần trăm cổ phần.", "Chuyện còn bỏ ngỏ: NHNN vừa khởi động lại xử lý **32,5%** cổ phần"),
   ("Góc nhìn của em là chờ ba tín hiệu.", "Góc nhìn của em: chờ **3 tín hiệu**"),
   ("Một, nợ xấu ngừng tăng.", "**Một**, nợ xấu ngừng tăng"),
   ("Hai, giá vượt được vùng cản bảy mươi ba.", "**Hai**, giá vượt cản **73**"),
   ("Ba, có hướng xử lý rõ cho số cổ phần đó.", "**Ba**, có hướng xử lý rõ số cổ phần đó")]),
 ("S6", {"the": [{"nhan": "CẮT 4.291 NGƯỜI", "t": "9 THÁNG LÀ XONG", "co": 58, "at": [0, 0.2]},
                 {"nhan": "GÁNH NỢ XẤU", "t": "CHƯA BIẾT BAO LÂU", "co": 58, "mau": "#c9533e", "at": [1, 0.35]}],
         "hoi": {"t": "Dọn nhà để **bật lên**, hay mới **bắt đầu dọn**?", "at": [2, 0.0]}},
  [("Cắt bốn nghìn người, chín tháng là xong.", "Cắt **4.000** người, 9 tháng là xong"),
   ("Còn gánh nợ xấu thì chưa biết bao lâu.", "Còn gánh **nợ xấu** thì chưa biết bao lâu"),
   ("Anh chị nghĩ Sacombank đang dọn nhà để bật lên, hay mới chỉ bắt đầu dọn?", "Dọn nhà để **bật lên**, hay mới **bắt đầu dọn**?")]),
]

L["ctg"] = [
 ("S1", {}, [("Một lá thư của VietinBank ghi con số ba trăm mười ba nghìn tỷ, cho đúng một dự án.", "Một lá thư của VietinBank ghi **313.000 tỷ**, cho đúng **một dự án**"),
             ("Số tiền đó đã thật sự chảy ra chưa?", "Số tiền đó **đã chảy ra chưa?**")]),
 ("S2", {"chuong": "— LÁ THƯ 313.000 TỶ —", "chot": {"a": "313.000 TỶ", "b": "GẦN 15% TỔNG DƯ NỢ", "do": 1, "at": [1, 0.7]}},
  [("Theo báo cáo Vietcap dẫn trên báo Người Quan Sát, VietinBank có thư cam kết tài trợ có điều kiện ba trăm mười ba nghìn tỷ cho dự án Đại lộ Cảnh quan Sông Hồng.", "VietinBank có thư cam kết tài trợ có điều kiện **313.000 tỷ** cho dự án **Đại lộ Cảnh quan Sông Hồng**"),
   ("Con số này gần bằng mười lăm phần trăm tổng dư nợ hai triệu một trăm bốn mươi nghìn tỷ của cả ngân hàng.", "Gần bằng **15%** tổng dư nợ **2,14 triệu tỷ** của cả ngân hàng")]),
 ("S3", {"chuong": "— ĐỌC KỸ LÁ THƯ —", "chot": {"a": "CHƯA CẤP HẠN MỨC", "b": "CHƯA GIẢI NGÂN, CHƯA DƯ NỢ", "do": 1, "at": [1, 0.9]},
         "_the_at": [[0, 0.3], [2, 0.4], [2, 0.8], [3, 0.4]]},
  [("Nhưng đọc kỹ thì đây mới là thư cam kết.", "Nhưng đọc kỹ, đây mới là **thư cam kết**"),
   ("Chưa cấp hạn mức, chưa giải ngân, chưa phát sinh đồng dư nợ nào.", "Chưa cấp hạn mức, **chưa giải ngân**, chưa có đồng dư nợ nào"),
   ("Trong khi đó, lãi trước thuế chín tháng vẫn tăng ba mươi ba phẩy chín phần trăm, nợ xấu chỉ một phẩy hai phần trăm.", "Lãi trước thuế 9 tháng vẫn **+33,9%**, nợ xấu chỉ **1,2%**"),
   ("Vậy mà cổ phiếu CTG đã lùi mười bốn phần trăm từ đỉnh.", "Vậy mà cổ phiếu CTG đã lùi **14%** từ đỉnh")]),
 ("S4", {"chuong": "— VÌ SAO THỊ TRƯỜNG LO —",
         "muc": [{"so": "BĐS 19,4%", "t": "Khoảng 415.443 tỷ dư nợ", "at": [0, 0.4], "co": 84},
                 {"so": "TÍN DỤNG +7,5%", "t": "9 tháng, đi chậm", "at": [2, 0.4], "co": 72},
                 {"so": "VAY NHÀ −5,5%", "t": "Bán lẻ chỉ +1,4%", "at": [2, 0.8], "co": 77, "mau": "#c9533e"}],
         "chot": {"a": "CAM KẾT CHƯA LÀ DƯ NỢ", "b": "TỶ TRỌNG BĐS LÀ ẨN SỐ", "at": [2, 0.95]}},
  [("Thị trường lo vì bất động sản đã chiếm khoảng bốn trăm mười lăm nghìn tỷ dư nợ, tức mười chín phẩy bốn phần trăm.", "Thị trường lo vì bất động sản đã chiếm khoảng **415.000 tỷ** dư nợ, tức **19,4%**"),
   ("Nếu lá thư biến thành tiền thật, tỷ trọng này có thể phình lên.", "Nếu lá thư thành **tiền thật**, tỷ trọng này có thể phình lên"),
   ("Tuy vậy, chín tháng qua VietinBank đi khá chậm: tín dụng chỉ tăng bảy phẩy năm phần trăm, cho vay mua nhà còn giảm năm phẩy năm phần trăm.", "Nhưng 9 tháng qua VietinBank đi chậm: tín dụng chỉ **+7,5%**, vay mua nhà **−5,5%**")]),
 ("S5", {"_mark_at": [[0, 0.5], [1, 0.7]], "_vung_at": [[1, 0.15], [1, 0.6]], "_chot_at": [1, 0.92]},
  [("Trên biểu đồ, đường trung bình hai mươi vừa cắt lên đường năm mươi ngày chín tháng mười một.", "Trên biểu đồ, **MA20 cắt lên MA50** ngày **9/11**"),
   ("Giá đang nằm giữa vùng cản ba mươi mốt phẩy sáu đến ba mươi hai và hỗ trợ hai mươi tám phẩy chín đến hai mươi chín phẩy tám.", "Giá nằm giữa cản **31,6–32** và hỗ trợ **28,9–29,8**")]),
 ("S5C", {"_muc_at": [[2, 0.0], [3, 0.0], [4, 0.0]], "_chot_at": [4, 0.6]},
  [("Phần còn bỏ ngỏ là lá thư này có trở thành tiền thật hay không, và khi nào.", "Còn bỏ ngỏ: lá thư có thành **tiền thật** không, và **khi nào**"),
   ("Góc nhìn của em là chờ ba tín hiệu.", "Góc nhìn của em: chờ **3 tín hiệu**"),
   ("Một, tỷ trọng bất động sản không tăng thêm.", "**Một**, tỷ trọng bất động sản không tăng"),
   ("Hai, nợ xấu giữ dưới một phẩy tám phần trăm.", "**Hai**, nợ xấu giữ dưới **1,8%**"),
   ("Ba, giá vượt được cản ba mươi hai.", "**Ba**, giá vượt cản **32**")]),
 ("S6", {"hoi": {"t": "Mỏ vàng hay **quả tạ** của VietinBank?", "at": [2, 0.0]}},
  [("Ký một lá thư ba trăm mười ba nghìn tỷ thì nhanh.", "Ký lá thư **313.000 tỷ** thì nhanh"),
   ("Còn giải ngân thì phải đủ điều kiện.", "Còn giải ngân thì phải **đủ điều kiện**"),
   ("Anh chị nghĩ con đường này là mỏ vàng hay quả tạ của VietinBank?", "Con đường này là **mỏ vàng** hay **quả tạ** của VietinBank?")]),
]

L["frt"] = [
 ("S1", {}, [("Trong cùng một nhà, cậu em bán thuốc được định giá gấp mười tám lần ông anh bán điện thoại.", "Cùng một nhà, cậu em **bán thuốc** được định giá gấp **18 lần** ông anh **bán điện thoại**"),
             ("Chuyện gì đang xảy ra ở FPT Retail?", "Chuyện gì đang xảy ra ở **FPT Retail?**")]),
 ("S2", {"chuong": "— HAI ANH EM —", "_mark_at": [[1, 0.5], [2, 0.3]],
         "chot": {"a": "LONG CHÂU", "b": "GẤP 18,3 LẦN FPT SHOP", "do": 1, "at": [2, 0.7]}},
  [("FPT Retail có hai chuỗi: FPT Shop bán điện thoại, máy tính, và Long Châu bán thuốc.", "FPT Retail có 2 chuỗi: **FPT Shop** bán điện thoại, máy tính, và **Long Châu** bán thuốc"),
   ("Báo cáo Vietcap ngày mười bảy tháng mười một ước Long Châu bốn mươi bốn nghìn bốn trăm hai mươi chín tỷ, FPT Shop chỉ hai nghìn bốn trăm hai mươi bảy tỷ.", "Vietcap 17/11 ước Long Châu **44.429 tỷ**, FPT Shop chỉ **2.427 tỷ**"),
   ("Cậu em nặng ký gấp khoảng mười tám phẩy ba lần ông anh.", "Cậu em nặng ký gấp khoảng **18,3 lần** ông anh")]),
 ("S3", {"chuong": "— CÚ BẤT NGỜ —", "chot": {"a": "PHẦN CỦA NHÂN VIÊN", "b": "GẤP 2 LẦN CẢ FPT SHOP", "do": 1, "at": [1, 0.9]},
         "_the_at": [[1, 0.1], [2, 0.3], [2, 0.8], [3, 0.4]]},
  [("Bất ngờ hơn, nhóm nhân viên đang nắm mười một phẩy không ba phần trăm Long Châu.", "Bất ngờ hơn: nhóm nhân viên đang nắm **11,03%** Long Châu"),
   ("Phần này ước khoảng bốn nghìn chín trăm tỷ, gấp hơn hai lần cả chuỗi FPT Shop.", "Ước khoảng **4.901 tỷ**, gấp **hơn 2 lần** cả chuỗi FPT Shop"),
   ("FPT Retail nắm bảy mươi lăm phẩy chín bảy phần trăm, quỹ Creador khoảng mười ba phần trăm.", "FPT Retail nắm **75,97%**, quỹ Creador khoảng **13%**"),
   ("Còn cổ phiếu FRT chỉ lùi ba phần trăm từ đỉnh.", "Cổ phiếu FRT chỉ lùi **3%** từ đỉnh")]),
 ("S4", {"chuong": "— ĐỌC KỸ CON SỐ —", "_muc_at": [[0, 0.3], [1, 0.4], [2, 0.4]], "_chot_at": [2, 0.9],
         "_muc3": {"so": "CÒN KHOẢNG 72%", "t": "Phần của FPT Retail năm 2030", "co": 72}},
  [("Nhưng đây là định giá ước tính của Vietcap, không phải giá giao dịch.", "Nhưng đây là **ước tính** của Vietcap, không phải giá giao dịch"),
   ("Kế hoạch ESOP thêm năm phần trăm vốn, chia năm đợt, mỗi năm một phần trăm.", "ESOP thêm **5% vốn**, chia **5 đợt**, mỗi năm **1%**"),
   ("Tới năm hai nghìn không trăm ba mươi, phần của FPT Retail có thể lùi về khoảng bảy mươi hai phần trăm.", "Tới **2030**, phần của FPT Retail có thể lùi về khoảng **72%**")]),
 ("S5", {"_mark_at": [[0, 0.5], [1, 0.7]], "_vung_at": [[1, 0.15], [1, 0.6]], "_chot_at": [1, 0.92]},
  [("Trên biểu đồ, đường trung bình hai mươi nằm trên đường năm mươi từ ngày mười một tháng tám.", "Trên biểu đồ, **MA20 nằm trên MA50** từ ngày **11/8**"),
   ("Giá đang sát vùng cản một trăm năm mươi hai đến một trăm năm mươi bốn phẩy tám, hỗ trợ một trăm ba mươi tám đến một trăm bốn mươi.", "Giá sát cản **152–154,8**, hỗ trợ **138–140**")]),
 ("S5C", {"_muc_at": [[2, 0.0], [3, 0.0], [4, 0.0]], "_chot_at": [4, 0.6]},
  [("Câu hỏi còn bỏ ngỏ là con số trên giấy có được doanh thu thật kiểm chứng hay không.", "Còn bỏ ngỏ: con số trên giấy có được **doanh thu thật** kiểm chứng không"),
   ("Góc nhìn của em là chờ ba tín hiệu.", "Góc nhìn của em: chờ **3 tín hiệu**"),
   ("Một, doanh thu quý bốn của Long Châu.", "**Một**, doanh thu quý 4 của Long Châu"),
   ("Hai, ESOP đi đúng lộ trình.", "**Hai**, ESOP đúng lộ trình"),
   ("Ba, giá vượt được cản một trăm năm mươi bốn phẩy tám.", "**Ba**, giá vượt cản **154,8**")]),
 ("S6", {"hoi": {"t": "Cầm FRT là cầm **chuỗi điện thoại** hay **nhà thuốc**?", "at": [2, 0.0]}},
  [("Nhà thuốc hơn bốn mươi bốn nghìn tỷ.", "Nhà thuốc hơn **44.000 tỷ**"),
   ("Cửa hàng điện thoại hơn hai nghìn bốn trăm tỷ.", "Cửa hàng điện thoại hơn **2.400 tỷ**"),
   ("Anh chị nghĩ cầm FRT là cầm chuỗi điện thoại, hay cầm nhà thuốc?", "Cầm FRT là cầm **chuỗi điện thoại** hay **nhà thuốc**?")]),
]

L["hvn"] = [
 ("S1", {}, [("Nhà mới sắp khánh thành, vậy mà ba mươi tư hãng bay quốc tế xin hẹn năm sau mới dọn về.", "Nhà mới sắp khánh thành, **34 hãng bay** xin hẹn **năm sau** mới dọn về"),
             ("Chuyện gì đang xảy ra với sân bay Long Thành?", "Chuyện gì đang xảy ra với **Long Thành?**")]),
 ("S2", {"chuong": "— XIN KHẤT —", "chot": {"a": "24 HÃNG: MÙA ĐÔNG 2027", "b": "10 HÃNG: MÙA HÈ 2028+", "do": 1, "at": [2, 0.6]}},
  [("Sân bay Long Thành dự kiến khai thác thương mại từ ngày hai mươi tư tháng mười hai.", "Long Thành dự kiến khai thác thương mại từ **24/12**"),
   ("Nhưng theo Vietnambiz, ba mươi tư hãng quốc tế muốn lùi ngày chuyển khỏi Tân Sơn Nhất.", "Nhưng **34 hãng** quốc tế muốn **lùi ngày chuyển** khỏi Tân Sơn Nhất"),
   ("Hai mươi tư hãng xin từ lịch bay mùa đông năm hai nghìn không trăm hai mươi bảy, mười hãng xin từ mùa hè năm hai nghìn không trăm hai mươi tám hoặc muộn hơn.", "**24 hãng** xin từ mùa đông **2027**, **10 hãng** từ mùa hè **2028** hoặc muộn hơn")]),
 ("S3", {"chuong": "— CÚ BẤT NGỜ —", "chot": {"a": "QUỐC TẾ CHỈ 44/366", "b": "CHUYẾN MỖI TUẦN", "do": 1, "at": [2, 0.9]},
         "_the_at": [[0, 0.2], [2, 0.2], [2, 0.6], [3, 0.4]]},
  [("Lạ ở chỗ, hãng nào cũng khen hạ tầng mới hiện đại.", "Lạ ở chỗ: hãng nào cũng **khen hạ tầng mới**"),
   ("Chỉ là họ cần sáu đến mười hai tháng để chuẩn bị.", "Chỉ là họ cần **6–12 tháng** chuẩn bị"),
   ("Giai đoạn đầu, Long Thành tối đa ba trăm sáu mươi sáu chuyến mỗi tuần, quốc tế chỉ bốn mươi tư chuyến.", "Giai đoạn đầu tối đa **366 chuyến/tuần**, quốc tế chỉ **44**"),
   ("Trong khi đó, cổ phiếu HVN đã lùi mười ba phần trăm từ đỉnh tháng bảy.", "Cổ phiếu HVN đã lùi **13%** từ đỉnh tháng 7")]),
 ("S4", {"chuong": "— VÌ SAO CHƯA VỘI —", "muc": [
            {"so": "ĐỀU ỦNG HỘ", "t": "Hạ tầng hiện đại", "at": [0, 0.3], "co": 84},
            {"so": "CẦN 6–12 THÁNG", "t": "Để lập kế hoạch khai thác", "at": [1, 0.3], "co": 72, "mau": "#c9533e"},
            {"so": "226 CHUYẾN", "t": "Mỗi tuần, tới tháng 3/2027", "at": [2, 0.4], "co": 84}],
         "chot": {"a": "ỦNG HỘ CHUYỂN", "b": "NHƯNG CẦN THÊM THỜI GIAN", "at": [2, 0.9]}},
  [("Đổi sân bay với một hãng bay không đơn giản như dọn nhà.", "Đổi sân bay với hãng bay **không đơn giản** như dọn nhà"),
   ("Phải sắp lại lịch bay, đường bay, nhân sự mặt đất, và bán vé trước nhiều tháng.", "Phải sắp lại **lịch bay**, nhân sự, và **bán vé trước** nhiều tháng"),
   ("Vì vậy tới tháng ba năm sau, Long Thành dự kiến mới đạt khoảng hai trăm hai mươi sáu chuyến mỗi tuần.", "Tới tháng 3/2027, dự kiến mới khoảng **226 chuyến/tuần**")]),
 ("S5", {"_mark_at": [[0, 0.5], [1, 0.7]], "_vung_at": [[1, 0.15], [1, 0.6]], "_chot_at": [1, 0.92]},
  [("Trên biểu đồ, đường trung bình hai mươi vừa cắt lên đường năm mươi ngày mười tháng mười một.", "Trên biểu đồ, **MA20 cắt lên MA50** ngày **10/11**"),
   ("Giá đang thử vùng cản hai mươi ba phẩy một đến hai mươi ba phẩy tư, hỗ trợ quanh hai mươi phẩy hai.", "Giá thử cản **23,1–23,4**, hỗ trợ quanh **20,2**")]),
 ("S5C", {"_muc_at": [[2, 0.0], [3, 0.0], [4, 0.0]], "_chot_at": [4, 0.6]},
  [("Câu hỏi còn bỏ ngỏ là lịch chuyển cuối cùng sẽ được chốt ra sao.", "Còn bỏ ngỏ: **lịch chuyển cuối cùng** được chốt ra sao"),
   ("Góc nhìn của em là chờ ba tín hiệu.", "Góc nhìn của em: chờ **3 tín hiệu**"),
   ("Một, lịch chuyển được chốt chính thức.", "**Một**, lịch chuyển chốt chính thức"),
   ("Hai, giá vượt được cản hai mươi ba phẩy tư.", "**Hai**, giá vượt cản **23,4**"),
   ("Ba, số chuyến tăng dần đúng kế hoạch.", "**Ba**, số chuyến tăng dần đúng kế hoạch")]),
 ("S6", {"the": [{"nhan": "NHÀ MỚI", "t": "XÂY XONG", "co": 70, "at": [0, 0.2]},
                 {"nhan": "KHÁCH", "t": "HẸN NĂM SAU", "co": 64, "mau": "#c9533e", "at": [1, 0.35]}],
         "hoi": {"t": "Bay **Long Thành ngay**, hay cũng xin **khất** như các hãng?", "at": [2, 0.0]}},
  [("Nhà mới xây xong.", "Nhà mới **xây xong**"),
   ("Khách thì hẹn năm sau mới về ở.", "Khách thì **hẹn năm sau** mới về ở"),
   ("Còn anh chị, muốn bay Long Thành ngay, hay cũng xin khất như các hãng?", "Anh chị muốn bay **Long Thành ngay**, hay cũng xin **khất**?")]),
]

L["vhm"] = [
 ("S1", {}, [("Có dự án chung cư ở Hà Nội vừa mất mười bốn phần trăm giá rao chỉ sau một quý.", "Chung cư Hà Nội có nơi mất **14% giá rao** chỉ sau **một quý**"),
             ("Giá đã rẻ hơn, vậy người mua đang ở đâu?", "Giá rẻ hơn, vậy **người mua đang ở đâu?**")]),
 ("S2", {"chuong": "— GIÁ RAO ĐI XUỐNG —", "chot": {"a": "CHUNG CƯ HÀ NỘI −4%", "b": "ĐẤT NỀN −11%", "do": 1, "at": [2, 0.6]}},
  [("Theo số liệu của bất động sản chấm com dẫn trên Vietnambiz, cả mười dự án chung cư nổi bật Hà Nội đều giảm giá rao trong quý ba.", "Theo Batdongsan.com.vn: cả **10 dự án** chung cư nổi bật Hà Nội đều giảm giá rao quý 3"),
   ("The Sapphire ở Vinhomes Smart City và Lumi Hanoi giảm mười bốn phần trăm, Times City mười ba, Ocean Park mười một.", "The Sapphire, Lumi **−14%**, Times City **−13%**, Ocean Park **−11%**"),
   ("Mặt bằng chung cư Hà Nội giảm bốn phần trăm, đất nền giảm mười một phần trăm.", "Chung cư Hà Nội **−4%**, đất nền **−11%**")]),
 ("S3", {"chuong": "— CÚ BẤT NGỜ —", "chot": {"a": "GIÁ RAO GIẢM", "b": "THANH KHOẢN CHƯA VỀ", "do": 1, "at": [2, 0.9]},
         "_the_at": [[0, 0.3], [0, 0.8], [1, 0.4], [2, 0.4]]},
  [("Ai cũng nghĩ giá giảm thì người mua sẽ ùa vào.", "Ai cũng nghĩ giá giảm thì **người mua ùa vào**"),
   ("Nhưng CBRE cho biết giao dịch sơ cấp chín tháng ở Hà Nội và Thành phố Hồ Chí Minh lại giảm khoảng ba mươi phần trăm.", "Nhưng CBRE: giao dịch sơ cấp 9 tháng lại **giảm khoảng 30%**"),
   ("Cổ phiếu VHM cũng đi theo, từ đỉnh bảy mươi tám nghìn về sáu mươi nghìn bốn trăm, mất hai mươi ba phần trăm.", "VHM từ đỉnh **78.000** về **60.400**, mất **23%**")]),
 ("S4", {"chuong": "— NGƯỜI MUA ĐI ĐÂU —", "_muc_at": [[0, 0.4], [1, 0.4], [2, 0.4]], "_chot_at": [2, 0.9]},
  [("Lãi vay vẫn cao, nên giá rao giảm vẫn chưa đủ kéo người mua.", "Lãi vay vẫn cao, giá giảm **chưa đủ kéo** người mua"),
   ("Lượng quan tâm chung cư Hà Nội tháng mười còn giảm chín phần trăm.", "Quan tâm chung cư Hà Nội tháng 10 **−9%**"),
   ("Một bộ phận người mua chọn quay về gửi tiết kiệm, chờ thêm.", "Một bộ phận chọn **gửi tiết kiệm**, chờ thêm")]),
 ("S5", {"_mark_at": [[0, 0.5], [1, 0.75]], "_vung_at": [[1, 0.15], [1, 0.6]], "_chot_at": [1, 0.92]},
  [("Trên biểu đồ, đường trung bình hai mươi đã cắt xuống đường năm mươi từ ngày ba mươi tháng chín.", "Trên biểu đồ, **MA20 cắt xuống MA50** từ **30/9**"),
   ("Giá đang nằm giữa vùng cản sáu mươi ba phẩy chín đến sáu mươi tư phẩy chín và hỗ trợ năm mươi bảy phẩy sáu đến năm mươi tám phẩy chín.", "Giá giữa cản **63,9–64,9** và hỗ trợ **57,6–58,9**")]),
 ("S5C", {"_muc_at": [[2, 0.0], [3, 0.0], [4, 0.0]], "_chot_at": [4, 0.6]},
  [("Câu hỏi còn bỏ ngỏ là quý bốn người mua có quay lại hay không.", "Còn bỏ ngỏ: quý 4 **người mua có quay lại** không"),
   ("Góc nhìn của em là chờ ba tín hiệu.", "Góc nhìn của em: chờ **3 tín hiệu**"),
   ("Một, giao dịch sơ cấp quý bốn cải thiện thật.", "**Một**, sơ cấp quý 4 cải thiện thật"),
   ("Hai, giá rao ngừng giảm.", "**Hai**, giá rao ngừng giảm"),
   ("Ba, giá cổ phiếu vượt được cản sáu mươi tư phẩy chín.", "**Ba**, giá vượt cản **64,9**")]),
 ("S6", {"hoi": {"t": "Chờ **giảm tiếp**, hay đã **đi xem nhà**?", "at": [2, 0.0]}},
  [("Giá rao đã giảm mười bốn phần trăm.", "Giá rao đã giảm **14%**"),
   ("Người mua vẫn chưa vội.", "Người mua **vẫn chưa vội**"),
   ("Anh chị đang chờ giá giảm tiếp, hay đã bắt đầu đi xem nhà?", "Anh chị chờ **giảm tiếp**, hay đã **đi xem nhà**?")]),
]

L["tcb"] = [
 ("S1", {}, [("Chỉ trong bảy ngày, Techcombank vay bảy nghìn năm trăm tỷ, chấp nhận trả lãi gần chín phần trăm một năm.", "Chỉ **7 ngày**, Techcombank vay **7.500 tỷ**, trả lãi gần **9%/năm**"),
             ("Vì sao một ngân hàng lớn lại vội như vậy?", "Vì sao một ngân hàng lớn **lại vội như vậy?**")]),
 ("S2", {"chuong": "— BẢY NGÀY, BA LÔ —", "chot": {"a": "BA LÔ, MỖI LÔ 2.500 TỶ", "b": "KỲ HẠN 36 THÁNG", "do": 1, "at": [2, 0.7]}},
  [("Theo Mekong ASEAN, Techcombank liên tiếp phát hành ba lô trái phiếu riêng lẻ, mỗi lô hai nghìn năm trăm tỷ.", "Techcombank liên tiếp phát hành **3 lô** trái phiếu riêng lẻ, mỗi lô **2.500 tỷ**"),
   ("Lô ngày mười hai tháng mười một lãi chín phần trăm, hai lô ngày mười bảy và mười tám lãi tám phẩy chín phần trăm.", "Lô **12/11** lãi **9%**, hai lô **17/11** và **18/11** lãi **8,9%**"),
   ("Kỳ hạn ba năm, tiền dùng để cho vay.", "Kỳ hạn **3 năm**, tiền dùng để **cho vay**")]),
 ("S3", {"chuong": "— CÚ BẤT NGỜ —", "chot": {"a": "VỐN KỲ HẠN 3 NĂM", "b": "LÃI CỐ ĐỊNH 8,9–9%", "do": 1, "at": [2, 0.9]},
         "_the_at": [[0, 0.3], [1, 0.3], [1, 0.7], [2, 0.4]]},
  [("Nghĩa là ngân hàng đi vay gần chín phần trăm, để cho vay lại.", "Ngân hàng đi vay gần **9%** để **cho vay lại**"),
   ("Lãi suất lô sau thấp hơn lô đầu một chút, từ chín xuống tám phẩy chín.", "Lô sau thấp hơn một chút: **9%** xuống **8,9%**"),
   ("Còn cổ phiếu TCB đã lùi tám phần trăm từ đỉnh ngày hai mươi mốt tháng mười.", "Cổ phiếu TCB lùi **8%** từ đỉnh **21/10**")]),
 ("S4", {"chuong": "— VÌ SAO PHẢI VỘI —", "_muc_at": [[0, 0.4], [1, 0.4], [2, 0.5]], "_chot_at": [2, 0.9]},
  [("Cuộc đua giữ tiền giữa các ngân hàng chưa hạ nhiệt.", "Cuộc đua **giữ tiền** giữa các ngân hàng chưa hạ nhiệt"),
   ("Lãi cho vay bình quân giờ đã vượt mười một phần trăm một năm.", "Lãi cho vay bình quân đã **vượt 11%/năm**"),
   ("Nợ xấu toàn ngành chín tháng ở mức hai phẩy ba phần trăm.", "Nợ xấu toàn ngành 9 tháng **2,3%**")]),
 ("S5", {"_mark_at": [[0, 0.5], [1, 0.7]], "_vung_at": [[1, 0.15], [1, 0.6]], "_chot_at": [1, 0.92]},
  [("Trên biểu đồ, đường trung bình hai mươi vừa cắt xuống đường năm mươi ngày mười chín tháng mười một.", "Trên biểu đồ, **MA20 cắt xuống MA50** ngày **19/11**"),
   ("Giá đang hồi về hai mươi mốt phẩy hai, giữa vùng cản hai mươi mốt phẩy tám đến hai mươi hai phẩy tám và hỗ trợ hai mươi phẩy mười lăm đến hai mươi phẩy sáu.", "Giá hồi về **21,2**, giữa cản **21,8–22,8** và hỗ trợ **20,15–20,6**")]),
 ("S5C", {"_muc_at": [[2, 0.0], [3, 0.0], [4, 0.0]], "_chot_at": [4, 0.6]},
  [("Câu hỏi còn bỏ ngỏ là lãi huy động sẽ còn neo cao bao lâu.", "Còn bỏ ngỏ: lãi huy động **neo cao bao lâu**"),
   ("Góc nhìn của em là chờ ba tín hiệu.", "Góc nhìn của em: chờ **3 tín hiệu**"),
   ("Một, lãi suất huy động hạ nhiệt.", "**Một**, lãi huy động hạ nhiệt"),
   ("Hai, giá vượt được cản hai mươi hai phẩy tám.", "**Hai**, giá vượt cản **22,8**"),
   ("Ba, nợ xấu toàn ngành ngừng tăng.", "**Ba**, nợ xấu ngành ngừng tăng")]),
 ("S6", {"the": [{"nhan": "NGÂN HÀNG", "t": "VAY GẦN 9%", "co": 70, "at": [0, 0.2]},
                 {"nhan": "ANH CHỊ GỬI", "t": "ĐƯỢC BAO NHIÊU?", "co": 58, "mau": "#c9533e", "at": [1, 0.35]}],
         "hoi": {"t": "Anh chị gửi tiết kiệm bao nhiêu %, thấy **9%** có hấp dẫn không?", "at": [2, 0.0]}},
  [("Ngân hàng chịu vay gần chín phần trăm.", "Ngân hàng chịu vay gần **9%**"),
   ("Còn tiền gửi của anh chị thì được bao nhiêu?", "Còn tiền gửi của anh chị **được bao nhiêu?**"),
   ("Anh chị đang gửi tiết kiệm bao nhiêu phần trăm, có thấy chín phần trăm hấp dẫn không?", "Anh chị gửi tiết kiệm bao nhiêu %, thấy **9%** có hấp dẫn không?")]),
]

import sys; sys.path.insert(0, os.path.dirname(HERE))
from phat_am import PHAT_AM, doc  # bảng cách đọc dùng chung (_video/phat_am.py)

def doi_bo_ngo(ma):
    """Chuyển câu 'bỏ ngỏ' (câu đầu S5C) về cuối S4 để cảnh góc nhìn không trống thẻ (soát STB 22/11)."""
    sc = {x[0]: x for x in L[ma]}
    s4, s5c = sc["S4"], sc["S5C"]
    s4[2].append(s5c[2].pop(0))
    s5c[1]["_muc_at"] = [[1, 0.0], [2, 0.0], [3, 0.0]]; s5c[1]["_chot_at"] = [3, 0.6]

def build(ma):
    cfg = json.load(open(os.path.join(HERE, ma + ".json"), encoding="utf-8"))
    old = {s["id"]: s for s in cfg["scenes"]}
    sc_out, kb = [], []
    for sid, ov, sens in L[ma]:
        s = copy.deepcopy(old[sid]); ov = dict(ov)
        for k in ("_the_at", "_muc_at", "_mark_at", "_vung_at", "_chot_at", "_tin_at", "_chart_at", "_muc3"):
            v = ov.pop(k, None)
            if v is None: continue
            if k == "_the_at":
                for x, a in zip(s["the"], v): x["at"] = a
            elif k == "_muc_at":
                for x, a in zip(s["muc"], v): x["at"] = a
            elif k == "_muc3": s["muc"][2].update(v)
            elif k == "_mark_at":
                ms = s["chart"]["marks"] if s["kieu"] == "tin" else s["marks"]
                for x, a in zip(ms, v): x["at"] = a
            elif k == "_vung_at":
                for x, a in zip(s["vung"], v): x["at"] = a
            elif k == "_chot_at": s["chot"]["at"] = v
            elif k == "_tin_at": s["tin"]["at"] = v
            elif k == "_chart_at": s["chart"]["at"] = v
        ov.pop("marks", None); ov.pop("tin", None) if ov.get("tin") == "_at" else None
        s.update(ov)
        if s["kieu"] == "tin" and sid == "S2" and "_mark_at" not in dict(L[ma][1][1]):
            pass
        s["phude"] = [chunks(sub) for _, sub in sens]
        sc_out.append(s)
        kb.append({"id": sid, "say": doc(" ".join(say for say, _ in sens)), "hold": 1.2 if sid == "S6" else 0.3})
    sc_out.append(old["OUT"])
    cfg["scenes"] = sc_out
    cfg["disclaimer"] = ""  # anh Huy 22/11: bỏ chữ "không phải khuyến nghị" trên video
    json.dump(cfg, open(os.path.join(HERE, ma + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump({"key": ma.upper() + "_THE", "title": ma + " the ke chuyen", "scenes": kb},
              open(os.path.join(HERE, ma + "_kb.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    n = sum(len(k["say"]) for k in kb)
    print(ma, "ky tu loi doc:", n)

if __name__ == "__main__":
    for ma in L: doi_bo_ngo(ma); build(ma)
