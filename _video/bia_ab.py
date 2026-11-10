# -*- coding: utf-8 -*-
"""QL1 11/11 – Ảnh bìa thử nghiệm A/B/C cho tính năng "Thử nghiệm và so sánh" của YouTube Studio.
Mỗi tập khai trong META: bia_hook (A), bia_hook_b, bia_hook_c (+ badge_b, badge_c tuỳ chọn).
Chạy: HN_PX=... python3 bia_ab.py <lô> KEY  -> out/KEY_bia.png, out/KEY_bia_b.png, out/KEY_bia_c.png
Nguyên tắc chữ bìa (học từ kênh tài chính lên view nhanh 11/2026): 2 dòng ≤ 14 ký tự, có 1 con số, 1 nghịch lý hoặc câu hỏi; không lặp nguyên văn tiêu đề.
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "engine"))
import bia, anh

if __name__ == "__main__":
    lo, key = sys.argv[1], sys.argv[2]
    g = {"__name__": "kb"}; exec(open(os.path.join(HERE, "queue", lo, "video_dai.py"), encoding="utf-8").read(), g)
    raw = g["S"][key]; M = (g.get("META") or {}).get(key, {})
    sc = dict(raw[0])
    if isinstance(sc.get("cap"), str): sc["cap"] = tuple(sc["cap"].split("\n"))
    kho = anh.Kho("/tmp/anh_bia"); ph = None
    for s in raw[:4]:
        try: ph = kho.cho(dict(s), M.get("title", ""))
        except Exception: ph = None
        if ph is not None: break
    od = os.path.join(HERE, "out"); os.makedirs(od, exist_ok=True)
    for sfx, hk, bd in (("", "bia_hook", "badge"), ("_b", "bia_hook_b", "badge_b"), ("_c", "bia_hook_c", "badge_c")):
        if not M.get(hk): continue
        mt = dict(title=M.get("title", ""), bia=M[hk], badge=M.get(bd) or M.get("badge", ""))
        bia.make(sc, mt, ph, os.path.join(od, key + "_bia" + sfx + ".png")); print("bia" + sfx, key, M[hk], flush=True)
