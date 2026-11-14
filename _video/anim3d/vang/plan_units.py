# Chia video thành từng "đơn vị cảnh" (mỗi cảnh quay/thẻ một đơn vị, liền khung từ 0 đến hết) và tính mã băm nội dung.
# Cảnh nào mã băm không đổi thì lấy bản đã dựng trong kho (release <tag>-cache), chỉ dựng lại cảnh đổi.
# Dùng: python plan_units.py <src_dir_anim3d> <comp> <cache_names.txt|-> <N_may> <out_plan.json>
import json, re, sys, os, hashlib, math
A, comp, have_f, N, OUT = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), sys.argv[5]
D = comp.lower(); V = os.path.join(A, "src", "videos", D); FPS = 30; TAIL = 4.0
tim = json.load(open(os.path.join(V, "timing.json"))); S = {s["id"]: s for s in tim["scenes"]}
src = open(os.path.join(V, comp + ".tsx")).read(); i0, i1 = src.index("const PLAN"), src.index("function teaStall"); plan = src[i0:i1]
fr = lambda x: int(math.floor(x * FPS + 0.5))
# mã chung: mọi mã nguồn ngoài phần PLAN + công cụ dựng; sửa phần chung thì dựng lại tất cả (chắc ăn)
h = hashlib.sha1()
for root, _, fs in sorted(os.walk(os.path.join(A, "src"))):
    for f in sorted(fs):
        p = os.path.join(root, f)
        if p.endswith("timing.json"): continue
        b = open(p, "rb").read()
        if p.endswith(os.path.join(D, comp + ".tsx")): b = (src[:i0] + src[i1:]).encode()
        h.update(p[len(A):].encode()); h.update(b)
for f in ["render_units.mjs", "package.json"]: h.update(open(os.path.join(A, f), "rb").read())
COMMON = h.hexdigest()
segs = []
for m in re.finditer(r'\{ id: "(S\d+)", shots: \[(.*?)\] \},?\n', plan, re.S):
    sid, body = m.group(1), m.group(2)
    shots = [(int(x.group(1)), x.start()) for x in re.finditer(r'^\s*\[(\d+), \(\) => (?:D3|CD)', body, re.M)]
    for k, (j, st) in enumerate(shots):
        txt = body[st: shots[k + 1][1] if k + 1 < len(shots) else len(body)].strip()
        a = S[sid]["a"] if k == 0 else S[sid]["sens"][j]["a"] - 0.12
        b = S[sid]["sens"][shots[k + 1][0]]["a"] - 0.12 if k + 1 < len(shots) else S[sid]["b"]
        segs.append({"id": f"{sid}.{j}", "sid": sid, "k": k, "first": k == 0, "txt": txt, "d3": "D3(" in txt, "a": a, "b": b})
TOTAL_F = math.ceil((tim["total"] + TAIL) * FPS)
units = []
for i, s in enumerate(segs):
    f0 = 0 if i == 0 else fr(s["a"]); f1 = (fr(segs[i + 1]["a"]) if i + 1 < len(segs) else fr(tim["total"])) - 1
    ref = s["a"]; sc = S[s["sid"]]
    if "fa" in sc:  # mốc khung nguyên (giọng đọc đã khớp lưới khung) -> mã băm ổn định khi cảnh trước dài/ngắn đi
        rel = [[z["text"], z["fa"] - f0, z["ns"]] for z in sc["sens"]]; sab = [sc["fa"] - f0, sc["fb"] - f0]
    else: rel = [[z["text"], round(z["a"] - ref, 3), round(z["b"] - ref, 3)] for z in sc["sens"]]; sab = [round(sc["a"] - ref, 3), round(sc["b"] - ref, 3)]
    key = hashlib.sha1(json.dumps([COMMON, comp, s["txt"], s["first"], s["k"], f1 - f0, fr(s["b"]) - fr(s["a"]), sab, rel], ensure_ascii=False).encode()).hexdigest()[:20]
    units.append({"id": s["id"], "f0": f0, "f1": f1, "w": (f1 - f0 + 1) * (1.0 if s["d3"] else 0.08), "key": key})
f0 = fr(tim["total"]); units.append({"id": "END", "f0": f0, "f1": TOTAL_F - 1, "w": (TOTAL_F - f0) * 0.08, "key": hashlib.sha1((COMMON + comp + "END" + str(TOTAL_F - f0)).encode()).hexdigest()[:20]})
for u in units: u["name"] = f"{comp}_{u['key']}.mp4"
have = set(open(have_f).read().split()) if have_f != "-" and os.path.exists(have_f) else set()
todo = [u for u in units if u["name"] not in have]
# chia việc cho tối đa N máy theo độ nặng (tham lam: việc nặng trước, vào máy nhẹ nhất)
n = max(1, min(N, len(todo))); bins = [[0.0, []] for _ in range(n)]
for u in sorted(todo, key=lambda u: -u["w"]): b = min(bins, key=lambda b: b[0]); b[0] += u["w"]; b[1].append(u["name"])
json.dump({"comp": comp, "total_f": TOTAL_F, "units": units, "groups": [b[1] for b in bins]}, open(OUT, "w"), ensure_ascii=False)
print(f"{len(units)} canh, can dung lai {len(todo)} ({sum(u['f1'] - u['f0'] + 1 for u in todo)} khung), co san {len(units) - len(todo)}; {n} may")
print("GROUPS=" + json.dumps(list(range(len(bins)))))
