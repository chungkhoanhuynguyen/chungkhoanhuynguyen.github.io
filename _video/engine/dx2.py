# Khuôn video v2 – motion graphics tự vẽ (bố cục: logo · nhãn vàng · khung hình động · 2 dòng chữ lớn)
import subprocess, re, math, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H, FPS = 1080, 1920, 24
import os
SP = os.path.dirname(os.path.abspath(__file__)) + "/"
FD = SP + "fonts/BeVietnamPro-"
_FC = {}
def F(w, s):
    k = (w, int(s))
    if k not in _FC: _FC[k] = ImageFont.truetype(FD + w + ".ttf", int(s))
    return _FC[k]
GOLD = (214, 170, 88); CREAM = (242, 234, 216); RED = (222, 64, 60); GREEN = (56, 190, 122)
BG0 = (13, 16, 23); PANEL = (19, 24, 34); BORDER = (46, 55, 72); GRID = (31, 37, 50); DIM = (128, 136, 152); INK = (24, 28, 38)
ease = lambda t: 1 - (1 - max(0., min(1., t))) ** 3
clamp = lambda t: max(0., min(1., t))
PX = json.load(open(os.environ.get("HN_PX", SP + "px.json")))

def series(sym, n):
    d = PX[sym][::-1][-n - 60:]
    return d
def make_bg():
    g = Image.new("RGB", (W, H), BG0); d = ImageDraw.Draw(g)
    for r, c in ((1000, (18, 22, 31)), (700, (22, 27, 38)), (380, (26, 32, 45))):
        d.ellipse([W/2-r, H*0.42-r, W/2+r, H*0.42+r], fill=c)
    g = g.filter(ImageFilter.GaussianBlur(160)); d = ImageDraw.Draw(g)
    for r in range(260, 1300, 170): d.ellipse([W/2-r, H*0.42-r, W/2+r, H*0.42+r], outline=(24, 29, 40), width=2)
    # vignette
    v = Image.new("L", (W, H), 0); vd = ImageDraw.Draw(v); vd.ellipse([-300, -200, W+300, H+200], fill=255)
    v = v.filter(ImageFilter.GaussianBlur(220)); g = Image.composite(g, Image.new("RGB", (W, H), (6, 8, 12)), v)
    return g
BG = make_bg()

def fit(d, s, w, mw, st):
    while d.textlength(s, font=F(w, st)) > mw and st > 18: st -= 2
    return F(w, st)
def ct(d, y, s, f, c, cx=W/2): d.text((cx - d.textlength(s, font=f)/2, y), s, font=f, fill=c)
def mix(c, a, base=BG0): return tuple(int(b + (x-b)*a) for b, x in zip(base, c))
def spaced(d, cx, y, s, f, c, sp=4):
    tw = sum(d.textlength(ch, font=f) for ch in s) + sp*(len(s)-1); x = cx - tw/2
    for ch in s: d.text((x, y), ch, font=f, fill=c); x += d.textlength(ch, font=f) + sp
    return tw

# ---------- avatar / header ----------
_AV = {}
def avatar(size):
    if size not in _AV:
        a = Image.open(SP+"fa/avatar.png").convert("RGB"); s = min(a.size)
        a = a.crop(((a.width-s)//2, 0, (a.width-s)//2+s, s)).resize((size, size), Image.LANCZOS)
        m = Image.new("L", (size, size), 0); ImageDraw.Draw(m).ellipse([0, 0, size-1, size-1], fill=255)
        _AV[size] = (a, m)
    return _AV[size]
WHITE_L = (255, 255, 255); LILAC = (205, 191, 224); LGOLD = (242, 207, 116)
def brand(im, d, cx, y, s=1.0, a=1.0, bg=BG0):
    # Logo đúng nhận diện web (img/og.png): HUY NGUYỄN trắng đậm + CHỨNG KHOÁN tím nhạt giãn chữ + gạch vàng #f2cf74 – canh giữa
    if a <= 0: return
    f1 = F("Black", 50*s); f2 = F("SemiBold", 21*s)
    t1 = "HUY NGUYỄN"; w1 = d.textlength(t1, font=f1)
    d.text((cx - w1/2, y), t1, font=f1, fill=mix(WHITE_L, a, bg))
    spaced(d, cx, y + 66*s, "CHỨNG KHOÁN", f2, mix(LILAC, a, bg), int(6*s))
    bw = 70*s; by = y + 104*s
    d.rounded_rectangle([cx - bw/2, by, cx + bw/2, by + 5*s], int(2*s), fill=mix(LGOLD, a, bg))
def header(im, d, a=1.0):
    brand(im, d, W/2, 128, 1.0, a)

def label(d, s, a, y=372):
    if a <= 0: return
    f = F("Bold", 36); c = mix(GOLD, a)
    tw = spaced(d, W/2, y, s, f, c, 3)
    L = 60*ease(a)
    d.line([W/2-tw/2-26-L, y+24, W/2-tw/2-26, y+24], fill=c, width=3)
    d.line([W/2+tw/2+26, y+24, W/2+tw/2+26+L, y+24], fill=c, width=3)

BX = (66, 470, 1014, 1150)  # panel box
def panel(d, a=1.0, box=BX):
    if a <= 0: return
    d.rounded_rectangle(box, 24, fill=mix(PANEL, a), outline=mix(BORDER, a), width=2)

def caption(d, lines, t, y=1250, cols=None, size=86):
    cols = cols or [CREAM, GOLD, RED]
    for i, l in enumerate(lines):
        if not l: continue
        a = ease((t - 0.25 - i*0.18) / 0.45)
        if a <= 0: continue
        f = fit(d, l, "Black", W-100, size); c = cols[i] if i < len(cols) else CREAM
        ct(d, y + (1-a)*28, l, f, mix(c, a)); y += int(f.size*1.2)

def footer(d): ct(d, H-120, "chungkhoanhuynguyen.com", F("SemiBold", 28), (92, 100, 116))

# ---------- stamp ----------
_ST = {}
def stamp(im, text, cy, a, scale=1.0):
    if a <= 0: return
    if text not in _ST:
        lines = text.split("\n"); f = F("Black", 96 if len(lines) == 1 else 84)
        tw = max(ImageDraw.Draw(Image.new("L", (1, 1))).textlength(l, font=f) for l in lines)
        Wd = int(tw + 120); Hd = int(len(lines)*f.size*1.12 + 90)
        s = Image.new("RGBA", (Wd, Hd), (0, 0, 0, 0)); sd = ImageDraw.Draw(s)
        sd.rounded_rectangle([8, 8, Wd-8, Hd-8], 16, outline=RED+(255,), width=10)
        sd.rounded_rectangle([22, 22, Wd-22, Hd-22], 10, outline=RED+(150,), width=3)
        yy = (Hd - len(lines)*f.size*1.12)/2 - 6
        for l in lines:
            sd.text(((Wd-sd.textlength(l, font=f))/2, yy), l, font=f, fill=RED+(255,)); yy += f.size*1.12
        # grunge
        import random; rnd = random.Random(len(text))
        for _ in range(260):
            x, y = rnd.randint(0, Wd), rnd.randint(0, Hd); sd.ellipse([x, y, x+rnd.randint(2, 6), y+rnd.randint(2, 5)], fill=(0, 0, 0, 0))
        _ST[text] = s.rotate(-7, expand=True, resample=Image.BICUBIC)
    s = _ST[text]; k = ease(a*2.4); sc = (1.8 - 0.8*k)*scale
    ss = s.resize((max(1, int(s.width*sc)), max(1, int(s.height*sc))))
    al = ss.split()[3].point(lambda v: int(v*min(1, k*1.4)*0.95))
    im.paste(ss, (int(W/2-ss.width/2), int(cy-ss.height/2)), al)

# ---------- panel contents ----------
def candles(im, d, sc, t, box=BX):
    sym = sc["sym"]; n = sc.get("n", 70); data = PX[sym][::-1]
    end = len(data) - sc.get("end_off", 0); seg = data[end-n:end]
    x0, y0, x1, y1 = box[0]+28, box[1]+40, box[2]-110, box[3]-40
    vh = (y1-y0)*0.2; py1 = y1 - vh - 14
    lo = min(r["l"] for r in seg); hi = max(r["h"] for r in seg)
    for z in sc.get("zones", []): lo = min(lo, z[0]); hi = max(hi, z[1])
    for hl in sc.get("hlines", []): lo = min(lo, hl[0]); hi = max(hi, hl[0])
    pad = (hi-lo)*0.08; lo -= pad; hi += pad
    Y = lambda p: py1 - (p-lo)/(hi-lo)*(py1-y0)
    cw = (x1-x0)/n; X = lambda i: x0 + cw*(i+0.5)
    # grid + axis
    step = nice_step(hi-lo)
    g = math.ceil(lo/step)*step
    fa = F("SemiBold", 24)
    while g < hi:
        yy = Y(g); d.line([x0, yy, x1, yy], fill=GRID, width=1)
        d.text((x1+14, yy-14), fmtp(g), font=fa, fill=DIM); g += step
    reveal = sc.get("reveal", 1.6)
    k = n if reveal <= 0 else int(n*ease(t/reveal)) if t < reveal else n
    # zones
    for z in sc.get("zones", []):
        za = ease((t - z[3] if len(z) > 3 else t - 1.0)/0.6)
        if za > 0:
            ov = Image.new("RGBA", im.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
            od.rectangle([x0, Y(z[1]), x1, Y(z[0])], fill=RED+(int(60*za),))
            od.line([x0, Y(z[1]), x1, Y(z[1])], fill=RED+(int(200*za),), width=2)
            od.line([x0, Y(z[0]), x1, Y(z[0])], fill=RED+(int(200*za),), width=2)
            im.paste(ov, (0, 0), ov); d = ImageDraw.Draw(im)
            f = F("ExtraBold", 30); d.text((x0+16, Y(z[1])+10), z[2], font=f, fill=mix((255, 140, 130), za, PANEL))
    vmax = max(r["v"] for r in seg)
    for i in range(k):
        r = seg[i]; up = r["c"] >= r["o"]; col = GREEN if up else RED
        if r["c"] == r["o"]: col = (220, 190, 80)
        xc = X(i); bw = max(2, cw*0.62)
        d.line([xc, Y(r["h"]), xc, Y(r["l"])], fill=col, width=2)
        yt, yb = Y(max(r["o"], r["c"])), Y(min(r["o"], r["c"]))
        if yb - yt < 2: yb = yt + 2
        d.rectangle([xc-bw/2, yt, xc+bw/2, yb], fill=col)
        vb = r["v"]/vmax*vh
        d.rectangle([xc-bw/2, y1-vb, xc+bw/2, y1], fill=mix(col, 0.45, PANEL))
    # MAs
    closes = [r["c"] for r in data]
    for (m, colr) in sc.get("mas", []):
        pts = []
        for i in range(k):
            gi = end-n+i
            if gi-m+1 < 0: continue
            pts.append((X(i), Y(sum(closes[gi-m+1:gi+1])/m)))
        if len(pts) > 1: d.line(pts, fill=colr, width=4, joint="curve")
        if pts and k == n:
            d.text((pts[-1][0]-150, pts[-1][1]-44), "MA%d" % m, font=F("ExtraBold", 26), fill=colr)
    # hlines
    for hl in sc.get("hlines", []):
        ha = ease((t - (hl[3] if len(hl) > 3 else 1.2))/0.5)
        if ha <= 0: continue
        yy = Y(hl[0]); c = hl[2]
        xe = x0 + (x1-x0)*ha
        for xx in range(int(x0), int(xe), 22): d.line([xx, yy, min(xx+12, xe), yy], fill=c, width=3)
        f = F("ExtraBold", 26); tw = d.textlength(hl[1], font=f)
        d.rounded_rectangle([x1-tw-24, yy-42, x1-4, yy-8], 8, fill=mix(c, ha, PANEL))
        d.text((x1-tw-14, yy-41), hl[1], font=f, fill=INK)
    # last price tag
    if k == n:
        lr = seg[-1]; yy = Y(lr["c"]); col = GREEN if lr["c"] >= seg[-2]["c"] else RED
        f = F("ExtraBold", 26); s = fmtp(lr["c"])
        d.rounded_rectangle([x1+6, yy-18, x1+96, yy+18], 6, fill=col); d.text((x1+12, yy-16), s, font=f, fill=(255, 255, 255))
    # circles
    for cc in sc.get("circles", []):
        ca = ease((t - cc[3])/0.4) if len(cc) > 3 else ease((t-reveal)/0.4)
        if ca <= 0: continue
        i = cc[0] if cc[0] >= 0 else n + cc[0]; yy = Y(cc[1]); rr = 30*(1.6-0.6*ca)
        d.ellipse([X(i)-rr, yy-rr, X(i)+rr, yy+rr], outline=mix(RED, ca, PANEL), width=5)
        if cc[2]:
            f = F("ExtraBold", 30); tw = d.textlength(cc[2], font=f)
            tx = min(max(X(i)-tw/2, x0), x1-tw); ty = yy-rr-48 if cc[1] > (lo+hi)/2 else yy+rr+10
            d.rounded_rectangle([tx-10, ty-4, tx+tw+10, ty+38], 8, fill=mix((40, 20, 22), ca, PANEL))
            d.text((tx, ty), cc[2], font=f, fill=mix((255, 120, 110), ca, PANEL))
    # title tag
    f = F("Bold", 24); d.text((box[0]+28, box[1]+12), sc.get("tag", sym + " · NẾN NGÀY"), font=f, fill=DIM)
    return d

def nice_step(r):
    for s in (0.5, 1, 2, 2.5, 5, 10, 20, 25, 50, 100, 200, 250, 500):
        if r/s <= 6: return s
    return 1000
def fmtp(p):
    s = ("%.2f" % p).rstrip("0").rstrip(".")
    if p >= 1000: s = "{:,.0f}".format(p).replace(",", ".")
    return s.replace(".", ",") if p < 1000 else s

def levels(im, d, sc, t, box=BX):
    x0, y0, x1, y1 = box[0]+40, box[1]+50, box[2]-40, box[3]-50
    lv = sc["levels"]; ps = [l[0] for l in lv]; lo, hi = min(ps), max(ps); pad = (hi-lo)*0.18; lo -= pad; hi += pad
    Y = lambda p: y1 - (p-lo)/(hi-lo)*(y1-y0)
    ax = x0 + 150
    d.rectangle([x0, y0, ax, y1], fill=(16, 20, 29))
    step = nice_step(hi-lo); g = math.ceil(lo/step)*step; fa = F("SemiBold", 26)
    while g < hi:
        d.text((x0+18, Y(g)-15), fmtp(g), font=fa, fill=DIM); d.line([ax, Y(g), x1, Y(g)], fill=GRID); g += step
    for i, (p, lab, col) in enumerate(lv):
        a = ease((t - 0.3 - i*0.35)/0.5)
        if a <= 0: continue
        yy = Y(p); xe = ax + (x1-ax)*a
        d.line([ax, yy, xe, yy], fill=col, width=4)
        f = F("ExtraBold", 30); s = fmtp(p) + ("  " + lab if lab else "")
        tw = d.textlength(s, font=f)
        lx = ax+18 if i % 2 == 0 else x1-tw-30
        d.rounded_rectangle([lx, yy-48, lx+20+tw, yy-8], 8, fill=mix(col, a, PANEL)); d.text((lx+10, yy-47), s, font=f, fill=INK)
    if sc.get("pct"):
        a = ease((t - 0.3 - len(lv)*0.35)/0.6)
        if a > 0:
            p0, p1 = sc["pct_from"], sc["pct_to"]; v = (p1/p0-1)*100*a
            s = ("%+.1f%%" % v).replace(".", ","); f = F("Black", 120)
            col = RED if v < 0 else GREEN
            d.text((x1 - d.textlength(s, font=f) - 10, (Y(p0)+Y(p1))/2 - 70), s, font=f, fill=mix(col, a, PANEL))
            # arrow
            ya, yb = Y(p0), Y(p0) + (Y(p1)-Y(p0))*a; xa = ax + 120
            d.line([xa, ya, xa, yb], fill=col, width=6)
            dirn = 1 if yb > ya else -1
            d.polygon([(xa-16, yb-dirn*18), (xa+16, yb-dirn*18), (xa, yb+dirn*4)], fill=col)

def volume(im, d, sc, t, box=BX):
    data = PX[sc["sym"]][::-1][-sc.get("n", 30):]
    x0, y0, x1, y1 = box[0]+40, box[1]+120, box[2]-40, box[3]-60
    vmax = max(r["v"] for r in data); n = len(data); cw = (x1-x0)/n
    avg = sum(r["v"] for r in data[-21:-1])/20
    for i, r in enumerate(data):
        a = ease((t - i*0.025)/0.4)
        if a <= 0: continue
        last = i == n-1
        hgt = r["v"]/vmax*(y1-y0)*(ease((t-1.2)/0.7) if last else a)
        col = GOLD if last else (70, 80, 100)
        d.rectangle([x0+i*cw+3, y1-hgt, x0+(i+1)*cw-3, y1], fill=col)
    ya = y1 - avg/vmax*(y1-y0); aa = ease((t-0.9)/0.4)
    if aa > 0:
        for xx in range(int(x0), int(x1), 20): d.line([xx, ya, xx+10, ya], fill=mix(CREAM, aa*0.7, PANEL), width=2)
        d.text((x0, ya-40), "TB 20 PHIÊN: %.1f TR" % (avg/1e6), font=F("Bold", 26), fill=mix(CREAM, aa*0.8, PANEL))
    la = ease((t-1.8)/0.4)
    if la > 0:
        s = sc.get("big", "x%.1f" % (data[-1]["v"]/avg)).replace(".", ",")
        f = F("Black", 96); d.text((x1 - d.textlength(s, font=f) - 70, box[1]+40), s, font=f, fill=mix(GOLD, la, PANEL))
    d.text((box[0]+28, box[1]+14), sc["sym"] + " · KHỐI LƯỢNG 30 PHIÊN", font=F("Bold", 24), fill=DIM)

def cards(im, d, sc, t, box=BX):
    cs = sc["cards"]; gap = 34 if len(cs) <= 4 else 18; hh = min(168, (box[3]-box[1]-40 - gap*(len(cs)-1))/len(cs)); k_ = hh/168; tot = len(cs)*hh + (len(cs)-1)*gap
    y = (box[1]+box[3])/2 - tot/2
    for i, cd in enumerate(cs):
        big, small, num = cd[:3]; ncol = cd[3] if len(cd) > 3 else ((28, 140, 78) if num.startswith("+") else RED)
        a = ease((t - 0.2 - i*0.45)/0.5)
        if a > 0:
            x0 = 110 - (1-a)*200; x1 = x0 + 860
            ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(ov); al = int(255*a)
            od.rounded_rectangle([x0, y, x1, y+hh], 12, fill=CREAM+(al,))
            fl = fit(od, big, "Black", 250, 84*k_); od.text((x0+36, y+hh/2-fl.size*0.62), big, font=fl, fill=INK+(al,))
            od.line([x0+310, y+30, x0+310, y+hh-30], fill=(196, 184, 160, al), width=3)
            od.text((x0+344, y+26*k_), small, font=fit(od, small, "ExtraBold", 480, 30*max(k_,0.8)), fill=(150, 60, 56, al))
            fn = fit(od, num, "Black", 480, 76*k_)
            if num: od.text((x0+340, y+66*k_), num, font=fn, fill=ncol+(al,))
            im.paste(ov, (0, 0), ov)
        y += hh + gap
    return ImageDraw.Draw(im)

def checklist(im, d, sc, t, box=BX):
    items = sc["items"]; y = box[1] + 90; f = F("Bold", 46)
    if sc.get("title"):
        d.text((box[0]+50, box[1]+40), sc["title"], font=F("ExtraBold", 32), fill=GOLD); y += 60
    for i, it in enumerate(items):
        a = ease((t - 0.3 - i*sc.get("gap", 1.1))/0.4)
        if a <= 0: continue
        bx = box[0]+50; d.rounded_rectangle([bx, y, bx+52, y+52], 8, outline=mix(GOLD, a, PANEL), width=4)
        ck = ease((t - 0.7 - i*sc.get("gap", 1.1))/0.35)
        if ck > 0:
            pts = [(bx+11, y+27), (bx+23, y+40), (bx+44, y+12)]
            d.line(pts[:2] if ck < 0.5 else pts, fill=GOLD, width=7, joint="curve")
        d.text((bx+80, y+2), it, font=fit(d, it, "Bold", box[2]-bx-120, 46), fill=mix(CREAM if ck > 0 else (190, 190, 200), a, PANEL))
        y += 130

def person(d, x, y, s, col):
    d.ellipse([x-s*0.32, y, x+s*0.32, y+s*0.64], fill=col)
    d.rounded_rectangle([x-s*0.5, y+s*0.72, x+s*0.5, y+s*1.6], int(s*0.3), fill=col)

def crowd(im, d, sc, t, box=BX):
    n = sc.get("n", 5); s = 70; gx = (box[2]-box[0]-200)/(n)
    base = box[3] - 200
    # stack of shares (left)
    sa = ease(t/0.5)
    sx0, sy1 = box[0]+70, box[3]-80
    for j in range(6):
        d.rounded_rectangle([sx0, sy1-30*(j+1), sx0+190, sy1-30*j-4], 4, fill=mix((230, 220, 196) if j == 5 else (200, 190, 168), sa, PANEL))
    d.text((sx0+30, sy1-30*6-60), sc.get("stack", "CỔ PHIẾU"), font=F("ExtraBold", 30), fill=mix(CREAM, sa, PANEL))
    for i in range(n):
        a = ease((t - 0.3 - i*0.15)/0.4)
        if a <= 0: continue
        x = box[0]+330 + i*(box[2]-box[0]-380)/(n-1) if n > 1 else W/2
        person(d, x, base - (1-a)*30, s, mix((120, 130, 150), a, PANEL))
        ta = ease((t - 1.2 - i*0.25)/0.35)
        if ta > 0 and sc.get("tags"):
            tg = sc["tags"][i % len(sc["tags"])]; f = F("ExtraBold", 24); tw = d.textlength(tg, font=f)
            d.rounded_rectangle([x-tw/2-10, base-56, x+tw/2+10, base-20], 6, fill=mix(CREAM, ta, PANEL))
            d.text((x-tw/2, base-55), tg, font=f, fill=INK)
    if sc.get("arrow"):
        aa = ease((t-2.0)/0.6)
        if aa > 0:
            # down arrow over crowd = sell pressure
            x = box[2]-120; ya = box[1]+90; yb = ya + 200*aa
            d.line([x, ya, x, yb], fill=RED, width=10); d.polygon([(x-26, yb-6), (x+26, yb-6), (x, yb+30)], fill=RED)
            d.text((x-150, ya-6), sc["arrow"], font=F("ExtraBold", 30), fill=RED)

def zigzag(im, d, sc, t, box=BX):
    pts = sc.get("pts", [(0, 0.1), (0.18, 0.45), (0.27, 0.32), (0.45, 0.62), (0.54, 0.5), (0.72, 0.8), (0.8, 0.7), (1.0, 0.95)])
    x0, y0, x1, y1 = box[0]+60, box[1]+80, box[2]-60, box[3]-60
    P = [(x0 + (x1-x0)*a, y0 + (y1-y0)*b) for a, b in pts]
    prog = ease(t/2.4)*(len(P)-1)
    drawn = [P[0]]
    for i in range(1, len(P)):
        if prog >= i: drawn.append(P[i])
        else:
            f = prog-(i-1)
            if f > 0: drawn.append((P[i-1][0]+(P[i][0]-P[i-1][0])*f, P[i-1][1]+(P[i][1]-P[i-1][1])*f))
            break
    for i in range(1, len(drawn)):
        up = drawn[i][1] < drawn[i-1][1]
        d.line([drawn[i-1], drawn[i]], fill=GREEN if up else CREAM, width=6)
    f = F("Bold", 30)
    for i in range(1, len(P)):
        if P[i][1] < P[i-1][1] and prog >= i:
            s = sc.get("note", "đáy rồi?"); d.text((P[i][0]-60, P[i][1]-52), s, font=f, fill=GREEN)

def follow(im, d, sc, t, box=BX):
    cy = (box[1]+box[3])/2; k = clamp((t-1.0)/0.3)
    bx0, bx1 = 220, 720; by0, by1 = cy-60, cy+60
    if k < 1:
        d.rounded_rectangle([bx0, by0, bx1, by1], 60, outline=GOLD, width=4, fill=PANEL)
        ct(d, by0+24, "+  FOLLOW", F("ExtraBold", 54), GOLD, (bx0+bx1)/2)
    else:
        d.rounded_rectangle([bx0, by0, bx1, by1], 60, fill=GOLD)
        ct(d, by0+24, "✓  FOLLOW", F("ExtraBold", 54), INK, (bx0+bx1)/2)
    # bookmark
    x0, x1 = 770, 870; kb = clamp((t-1.6)/0.3)
    d.rounded_rectangle([x0, by0, x1, by1], 18, outline=GOLD, width=4, fill=GOLD if kb >= 1 else PANEL)
    pts = [(x0+32, by0+28), (x1-32, by0+28), (x1-32, by1-26), ((x0+x1)/2, by1-48), (x0+32, by1-26)]
    d.polygon(pts, outline=INK if kb >= 1 else GOLD, fill=INK if kb >= 1 else None, width=4)
    # tap cursor
    if t < 1.3:
        tx = bx1 - 80 + (1-ease(t/1.0))*120; ty = cy + 40 + (1-ease(t/1.0))*120
        d.ellipse([tx-22, ty-22, tx+22, ty+22], fill=(240, 240, 240))

def bignum(im, d, sc, t, box=BX):
    v = sc["value"]; a = ease(max(0, t - sc.get("t0", 0))/sc.get("dur", 0.9)); cur = sc.get("v0", 0) + (v - sc.get("v0", 0))*a
    s = sc.get("fmt", "{:+,.0f}").format(cur).translate(str.maketrans({",": ".", ".": ","})) + sc.get("unit", "")
    col = sc.get("col") or (RED if v < 0 else GREEN)
    f = fit(d, s, "Black", box[2]-box[0]-80, 200); ct(d, (box[1]+box[3])/2 - f.size*0.75, s, f, col)
    if sc.get("top"): ct(d, (box[1]+box[3])/2 - f.size*0.75 - 90, sc["top"], F("ExtraBold", 44), CREAM)
    if sc.get("sub"): ct(d, (box[1]+box[3])/2 + f.size*0.45, sc["sub"], F("Bold", 36), DIM)

def bars(im, d, sc, t, box=BX):
    # biểu đồ thanh ngang: sc["bars"] = [(nhãn, giá trị, màu, chữ hiển thị), ...]
    bs = sc["bars"]; n = len(bs); x0, y0, x1, y1 = box[0]+36, box[1]+60, box[2]-36, box[3]-30
    vmax = max(b[1] for b in bs); rh = (y1-y0)/n; lw = 210
    if sc.get("tag"): d.text((box[0]+28, box[1]+14), sc["tag"], font=F("Bold", 24), fill=DIM)
    for i, b in enumerate(bs):
        lab, v, col = b[0], b[1], b[2]; txt = b[3] if len(b) > 3 else fmtp(v)
        a = ease((t - 0.2 - i*0.18)/0.6)
        if a <= 0: continue
        yc = y0 + rh*(i+0.5); bh = min(46, rh*0.62)
        f = fit(d, lab, "ExtraBold", lw-16, 34); d.text((x0, yc - f.size*0.62), lab, font=f, fill=mix(CREAM, a, PANEL))
        w = (x1 - x0 - lw - 150)*(v/vmax)*a
        d.rounded_rectangle([x0+lw, yc-bh/2, x0+lw+max(6, w), yc+bh/2], 8, fill=mix(col, a, PANEL))
        fv = F("Black", 34); d.text((x0+lw+w+14, yc - 22), txt, font=fv, fill=mix(col, a, PANEL))
    return d

_IM = {}
def image(im, d, sc, t, box=BX):
    # ảnh thật (bài đăng, danh mục) đặt vừa khung, phóng nhẹ + mờ dần vào; sc["img"], tùy chọn sc["blur"]=[(x0,y0,x1,y1) tỉ lệ 0-1]
    p = sc["img"]
    if p not in _IM:
        from PIL import ImageFilter as IF
        a = Image.open(SP + p).convert("RGB")
        for (bx0, by0, bx1, by1) in sc.get("blur", []):
            W0, H0 = a.size; r = (int(bx0*W0), int(by0*H0), int(bx1*W0), int(by1*H0))
            a.paste(a.crop(r).filter(IF.GaussianBlur(18)), r[:2])
        _IM[p] = a
    a = _IM[p]; bw, bh = box[2]-box[0]-24, box[3]-box[1]-24
    k = ease(t/0.6); z = 1.0 + 0.04*min(1, t/6)
    s = min(bw/a.width, bh/a.height)*z; w, h = int(a.width*s), int(a.height*s)
    b = a.resize((w, h))
    cx, cy = (box[0]+box[2])//2, (box[1]+box[3])//2
    x0, y0 = cx-w//2, cy-h//2
    # cắt theo khung
    cl = (max(0, box[0]+12-x0), max(0, box[1]+12-y0), min(w, box[2]-12-x0), min(h, box[3]-12-y0))
    b = b.crop(cl); m = Image.new("L", b.size, int(255*k))
    im.paste(b, (x0+cl[0], y0+cl[1]), m)
    return ImageDraw.Draw(im)

KINDS = dict(image=image, bars=bars, candles=candles, levels=levels, volume=volume, cards=cards, checklist=checklist, crowd=crowd, zigzag=zigzag, follow=follow, bignum=bignum)

def endcard(im, d, t):
    a = ease(t/0.5)
    label(d, "CHỨNG KHOÁN HUY NGUYỄN", a, y=330)
    k = ease((t-0.2)/0.6)
    if k > 0:
        d.rounded_rectangle([190, 520, 890, 900], 40, fill=mix((22, 28, 40), k), outline=mix(LGOLD, k), width=3)
        brand(im, d, W/2, 588, 2.0, k, (22, 28, 40))
    k2 = ease((t-0.6)/0.5)
    if k2 > 0:
        by = 990; filled = t > 1.6
        if filled: d.rounded_rectangle([300, by, 780, by+110], 55, fill=GOLD); ct(d, by+24, "✓  FOLLOW", F("ExtraBold", 56), INK)
        else: d.rounded_rectangle([300, by, 780, by+110], 55, outline=mix(GOLD, k2), width=4); ct(d, by+24, "+  FOLLOW", F("ExtraBold", 56), mix(GOLD, k2))
        f = F("Medium", 26); c = mix((140, 146, 162), k2)
        ct(d, by+150, "Thị trường thay đổi từng ngày. Xem thêm các video trên kênh.", f, c)
        ct(d, by+186, "Nội dung chỉ chia sẻ quan điểm cá nhân, không phải khuyến nghị mua bán.", f, c)
        pass
    k3 = ease((t-1.0)/0.5)
    if k3 > 0:
        ct(d, 1400+(1-k3)*30, "FOLLOW ĐỂ NHẬN", F("Black", 92), mix(CREAM, k3))
        ct(d, 1510+(1-k3)*30, "GÓC NHÌN SỚM", F("Black", 92), mix(GOLD, k3))

def draw(sc, t, z=0.0):
    im = BG.copy(); d = ImageDraw.Draw(im); k = sc["k"]
    if k == "end":
        endcard(im, d, t); return im
    header(im, d, 1.0)
    if k == "text":
        if sc.get("label"): label(d, sc["label"], ease(t/0.4))
        caption(d, sc["cap"], t + (5 if sc.get("instant") else 0), y=sc.get("y", 860), cols=sc.get("cols"), size=sc.get("size", 104))
        if sc.get("stamp"):
            stamp(im, sc["stamp"], sc.get("stamp_y", 1250), (t - sc.get("stamp_t", 0.3))); d = ImageDraw.Draw(im)
        footer(d); return im
    label(d, sc["label"], ease(t/0.4))
    panel(d, 1.0)
    if k in KINDS:
        r = KINDS[k](im, d, sc, t)
        if isinstance(r, ImageDraw.ImageDraw): d = r
        d = ImageDraw.Draw(im)
    if sc.get("stamp"):
        stamp(im, sc["stamp"], (BX[1]+BX[3])/2, (t - sc.get("stamp_t", 0.6))); d = ImageDraw.Draw(im)
    caption(d, sc["cap"], t, cols=sc.get("cols"))
    footer(d)
    return im

def silences(A):
    log = subprocess.run(["ffmpeg", "-hide_banner", "-i", A, "-af", "silencedetect=noise=-32dB:d=0.18", "-f", "null", "-"], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]; en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", log); dur = int(m.group(2))*60+float(m.group(3))
    return [((a+b)/2, b-a) for a, b in zip(st, en) if a > 0.3], dur

def bounds(scenes, A):
    pauses, dur = silences(A)
    sents = []  # (text, scene_index)
    for si, sc in enumerate(scenes):
        for x in re.split(r"(?<=[.?!:])\s+", sc["say"].strip()):
            if x: sents.append((x, si))
    cost = lambda x: len(x) + 6*x.count(",")
    tot = sum(cost(x) for x, _ in sents); ps = 0.5; rate = tot/(dur - ps*len(sents))
    tg = []; acc = 0
    for x, _ in sents[:-1]: acc += cost(x)/rate + ps; tg.append(acc - ps/2)
    P = [p for p in pauses if p[0] < dur-0.5]; n, m = len(tg), len(P)
    if m < n:
        sb = tg
    else:
        INF = 1e18; best = [[INF]*(m+1) for _ in range(n+1)]; ch = [[0]*(m+1) for _ in range(n+1)]
        for j in range(m+1): best[0][j] = 0
        for i in range(1, n+1):
            for j in range(i, m+1):
                cu = best[i-1][j-1] + (P[j-1][0]-tg[i-1])**2 - 2.5*min(P[j-1][1], 0.9)
                cs = best[i][j-1]
                if cu < cs: best[i][j] = cu; ch[i][j] = 1
                else: best[i][j] = cs
        sb = []; i, j = n, m
        while i > 0:
            if ch[i][j] == 1: sb.append(P[j-1][0]); i -= 1; j -= 1
            else: j -= 1
        sb = sb[::-1]
    b = [0.0]
    for k in range(len(sents)-1):
        if sents[k][1] != sents[k+1][1]: b.append(sb[k])
    b.append(dur)
    return b, dur

def build(key, scenes, A, out, preview=None):
    b, dur = bounds(scenes, A)
    tmp = "/tmp/dx2_%s.mp4" % key
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "19", "-preset", "veryfast", tmp], stdin=subprocess.PIPE)
    fr = 0
    for i, sc in enumerate(scenes):
        n = int(round(b[i+1]*FPS)) - fr
        for j in range(n):
            im = draw(sc, j/FPS, j/max(1, n))
            p.stdin.write(im.tobytes())
        fr += n
    p.stdin.close(); p.wait()
    af = ("highpass=f=120,acompressor=threshold=-26dB:ratio=4:attack=3:release=60:makeup=6,"
          "loudnorm=I=-11:TP=-1:LRA=5,volume=6dB,alimiter=limit=0.95:attack=1:release=40:level=false")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-i", A, "-af", af, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-shortest", out])
    vd = subprocess.run(["ffmpeg", "-hide_banner", "-i", out, "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
    print(key, "dur %.1f" % dur, [round(x, 1) for x in b], re.search(r"mean_volume: ([-\d.]+)", vd).group(1))
    return b

def build_scenes(key, scenes, wav_dir, out, gap=0.28, tail=1.2, tempo=1.12):
    import os, wave
    tmpd = "/tmp/dx2_%s_parts" % key; os.makedirs(tmpd, exist_ok=True)
    parts = []; b = [0.0]
    for i in range(len(scenes)):
        src = os.path.join(wav_dir, "%02d.wav" % i); dst = os.path.join(tmpd, "%02d.wav" % i)
        # trim lead/trail silence, pad gap at end, unify format
        pad = gap + (tail if i == len(scenes)-1 else 0)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-af",
                        "silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.08,areverse,atempo=%.3f,apad=pad_dur=%.2f" % (tempo, pad),
                        "-ar", "44100", "-ac", "1", dst])
        with wave.open(dst) as w: dd = w.getnframes()/w.getframerate()
        b.append(b[-1] + dd); parts.append(dst)
    lst = os.path.join(tmpd, "list.txt"); open(lst, "w").write("".join("file '%s'\n" % p for p in parts))
    A = os.path.join(tmpd, "full.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", A])
    tmp = "/tmp/dx2_%s.mp4" % key
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "19", "-preset", "veryfast", tmp], stdin=subprocess.PIPE)
    fr = 0
    for i, sc in enumerate(scenes):
        n = int(round(b[i+1]*FPS)) - fr
        for j in range(n): p.stdin.write(draw(sc, j/FPS, j/max(1, n)).tobytes())
        fr += n
    p.stdin.close(); p.wait()
    af = ("highpass=f=120,acompressor=threshold=-26dB:ratio=4:attack=3:release=60:makeup=6,"
          "loudnorm=I=-11:TP=-1:LRA=5,volume=6dB,alimiter=limit=0.95:attack=1:release=40:level=false")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-i", A, "-af", af, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-shortest", out])
    vd = subprocess.run(["ffmpeg", "-hide_banner", "-i", out, "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
    print(key, "dur %.1f" % b[-1], [round(x, 1) for x in b], re.search(r"mean_volume: ([-\d.]+)", vd).group(1))
    return b
