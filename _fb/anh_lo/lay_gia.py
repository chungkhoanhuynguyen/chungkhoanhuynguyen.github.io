"""Lấy OHLCV ngày từ DỮ LIỆU WEB (data/c/<MÃ>.bin + data/c/recent.bin) – 0 token, ko gọi WiData.
Dùng: python3 _fb/anh_lo/lay_gia.py FPT 120  -> in JSON [{time,open,high,low,close,volume}] (giá nghìn đồng)
Gốc *.bin: giá/100 = nghìn đồng (5710 = 57,10). recent.bin: giá đồng (5450 = 5,45 nghìn?) -> tự nhận đơn vị theo phiên trùng."""
import sys, json, os, datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
import hncodec
def lay(ma, n=120):
    j = hncodec.load("data/c/%s.bin" % ma) or {}
    rows = {}
    if j:
        d = datetime.date.fromisoformat(j["d0"]); 
        for i, g in enumerate(j["g"]):
            d += datetime.timedelta(days=g)
            rows[d.isoformat()] = [j["o"][i], j["h"][i], j["l"][i], j["c"][i], j["v"][i]]
    rec = ((hncodec.load("data/c/recent.bin", {}) or {}).get("b", {}) or {}).get(ma) or []
    # quy đổi đơn vị recent về đơn vị gốc nhờ 1 phiên trùng
    k = 1.0
    for r in rec:
        if r[0] in rows and r[4]:
            k = rows[r[0]][3] / r[4]; break
    for r in rec:
        rows[r[0]] = [round(r[1]*k), round(r[2]*k), round(r[3]*k), round(r[4]*k), r[5]]
    out = [dict(time=d, open=v[0]/100, high=v[1]/100, low=v[2]/100, close=v[3]/100, volume=v[4]) for d, v in sorted(rows.items())]
    return out[-n:]
if __name__ == "__main__":
    print(json.dumps(lay(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 120)))
