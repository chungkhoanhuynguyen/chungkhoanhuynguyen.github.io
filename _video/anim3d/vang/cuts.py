# Tính mốc cắt cảnh (giây) từ kế hoạch Vang.tsx + timing.json -> cuts.json (để đặt tiếng vút ở mỗi lần chuyển cảnh)
import json, re, sys
tim = json.load(open(sys.argv[1])); S = {s["id"]: s for s in tim["scenes"]}
src = open(sys.argv[2]).read(); plan = src[src.index("const PLAN"):src.index("function teaStall")]
cuts = []
for m in re.finditer(r'\{ id: "(S\d+)", shots: \[(.*?)\] \},?\n', plan, re.S):
    sid, body = m.group(1), m.group(2); js = [int(x) for x in re.findall(r'\[(\d+), \(\) => (?:D3|CD)', body)]
    for k, j in enumerate(js): cuts.append(S[sid]["a"] if k == 0 else S[sid]["sens"][j]["a"] - 0.12)
json.dump([round(c, 3) for c in cuts[1:]], open(sys.argv[3], "w")); print(len(cuts), "canh")

# chia khung hình cho N máy dựng theo "độ nặng": cảnh 3D nặng gấp ~12 lần cảnh thẻ 2D
if len(sys.argv) > 5:
    N = int(sys.argv[5]); fps = 30; total = int(-(-(tim["total"] + 4.0) * fps // 1))
    w = [0.08] * total
    for m in re.finditer(r'\{ id: "(S\d+)", shots: \[(.*?)\] \},?\n', plan, re.S):
        sid, body = m.group(1), m.group(2); js = re.findall(r'\[(\d+), \(\) => (D3|CD)', body)
        for k, (j, kind) in enumerate(js):
            j = int(j); a = S[sid]["a"] if k == 0 else S[sid]["sens"][j]["a"] - 0.12
            b = S[sid]["sens"][int(js[k + 1][0])]["a"] - 0.12 if k + 1 < len(js) else S[sid]["b"]
            if kind == "D3":
                for f in range(round(a * fps), min(total, round(b * fps))): w[f] = 1.0
    tot = sum(w); out = []; acc = 0; start = 0
    for f in range(total):
        acc += w[f]
        if acc >= tot / N * (len(out) + 1) and len(out) < N - 1: out.append([start, f]); start = f + 1
    out.append([start, total - 1])
    json.dump(out, open(sys.argv[4], "w")); print("chia", len(out), "phan, tong", total, "khung")
