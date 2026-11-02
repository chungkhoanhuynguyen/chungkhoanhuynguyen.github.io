# Nhân vật nét vẽ đơn giản (doodle) tự thiết kế cho video kể chuyện – vẽ bằng cairo, không tốn phí.
# Mỗi con vật = đầu to tròn + thân nhỏ + tay ngắn, viền đậm, má hồng. Hoạt ảnh: nhún, chớp mắt, vẫy tay, nghiêng đầu, nói.
import cairo, math

INK = (0.17, 0.2, 0.26)
PINK = (0.98, 0.62, 0.66)
LOAI = {
    # ten: màu lông, màu bụng, kiểu tai, phụ kiện
    "meo":      dict(fur=(1.0, 1.0, 1.0), belly=None, ear="tamgiac", name="Mèo Mun Mập", patch=(0.96, 0.66, 0.3)),
    "cho":      dict(fur=(0.99, 0.93, 0.8), belly=None, ear="cup", name="Cún Bơ"),
    "canhcut":  dict(fur=(0.22, 0.25, 0.33), belly=(1, 1, 1), ear=None, name="Cụt Cánh", beak=True),
    "gau":      dict(fur=(0.82, 0.62, 0.45), belly=(0.98, 0.88, 0.75), ear="tron", name="Gấu Gạo"),
    "meoanh":   dict(fur=(0.66, 0.71, 0.78), belly=(0.86, 0.89, 0.93), ear="tamgiac_nho", name="Anh Lông Ngắn"),
    "meoaicap": dict(fur=(0.95, 0.82, 0.74), belly=None, ear="to", name="Ai Cập", wrinkle=True),
}

def _p(ctx, w, col=INK):
    ctx.set_source_rgb(*col); ctx.set_line_width(w); ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.set_line_join(cairo.LINE_JOIN_ROUND)

def blob(ctx, cx, cy, rx, ry):
    ctx.new_sub_path(); ctx.save(); ctx.translate(cx, cy); ctx.scale(rx, ry); ctx.arc(0, 0, 1, 0, 2 * math.pi); ctx.restore()

def fill_stroke(ctx, fill, lw):
    ctx.set_source_rgb(*fill); ctx.fill_preserve(); _p(ctx, lw); ctx.stroke()

def ve(ctx, loai, x, y, s=1.0, t=0.0, mood="binh", noi=0.0, tay="xuoi", huong=1, nhun=1.0):
    """x,y = điểm chân giữa; s = tỉ lệ (1 = cao ~420px). mood: binh/vui/buon/ngac/nghi. noi: 0..1 độ mở miệng.
    tay: xuoi/vay/chi/om/gio (giơ 2 tay)."""
    L = LOAI[loai]; lw = 9 * s; ctx.new_path()
    bob = math.sin(t * 6.0) * 6 * s * nhun
    blink = (t % 3.3) < 0.12
    tilt = math.sin(t * 1.3) * 0.05 + (0.12 if mood == "nghi" else 0)
    ctx.save(); ctx.translate(x, y + bob)
    # ---- thân ----
    bw, bh = 215 * s, 150 * s
    # chân tròn
    for sd in (-1, 1):
        blob(ctx, sd * bw * 0.2, -6 * s, 34 * s, 20 * s); fill_stroke(ctx, L["fur"], lw)
    blob(ctx, 0, -bh * 0.52, bw * 0.5, bh * 0.56); fill_stroke(ctx, L["fur"], lw)
    if L.get("belly"):
        blob(ctx, 0, -bh * 0.45, bw * 0.32, bh * 0.38); ctx.set_source_rgb(*L["belly"]); ctx.fill()
    # ---- tay ----
    def arm(sd, ang):
        ax, ay = sd * bw * 0.44, -bh * 0.72
        ex, ey = ax + sd * math.sin(ang) * 62 * s, ay + math.cos(ang) * 62 * s
        _p(ctx, lw * 4.2); ctx.move_to(ax, ay); ctx.line_to(ex, ey); ctx.stroke()
        _p(ctx, lw * 4.2 - lw * 1.8, L["fur"]); ctx.move_to(ax, ay); ctx.line_to(ex, ey); ctx.stroke()
    w = math.sin(t * 9) * 0.35
    angs = {"xuoi": (0.15, 0.15), "vay": (0.15, 2.4 + w), "chi": (0.15, 1.75), "om": (0.9, 0.9), "gio": (2.5 + w, 2.5 - w)}[tay]
    arm(-1, angs[0] if huong > 0 else angs[1]); arm(1, angs[1] if huong > 0 else angs[0])
    # ---- đầu ----
    ctx.translate(0, -bh - 78 * s); ctx.rotate(tilt)
    hr, hy = 150 * s, 128 * s
    fur = L["fur"]
    # tai sau đầu
    ear = L.get("ear")
    for sd in (-1, 1):
        if ear in ("tamgiac", "tamgiac_nho", "to"):
            k = {"tamgiac": 1.0, "tamgiac_nho": 0.7, "to": 1.6}[ear]
            ctx.move_to(sd * 50 * s, -hy * 0.75); ctx.line_to(sd * (95 + 20 * k) * s, -hy * (0.95 + 0.55 * k)); ctx.line_to(sd * 118 * s, -hy * 0.35)
            ctx.close_path(); fill_stroke(ctx, fur, lw)
            ctx.move_to(sd * 70 * s, -hy * 0.75); ctx.line_to(sd * (96 + 14 * k) * s, -hy * (0.9 + 0.4 * k)); ctx.line_to(sd * 105 * s, -hy * 0.55)
            ctx.close_path(); ctx.set_source_rgb(*PINK); ctx.fill()
        elif ear == "tron":
            blob(ctx, sd * 98 * s, -hy * 0.82, 38 * s, 38 * s); fill_stroke(ctx, fur, lw)
            blob(ctx, sd * 98 * s, -hy * 0.82, 18 * s, 18 * s); ctx.set_source_rgb(*PINK); ctx.fill()
    blob(ctx, 0, 0, hr, hy); fill_stroke(ctx, fur, lw)
    if L.get("patch"):
        ctx.save(); blob(ctx, 0, 0, hr - lw / 2, hy - lw / 2); ctx.clip()
        blob(ctx, 70 * s, -60 * s, 70 * s, 55 * s); ctx.set_source_rgb(*L["patch"]); ctx.fill(); ctx.restore()
        blob(ctx, 0, 0, hr, hy); _p(ctx, lw); ctx.stroke()
    if L.get("belly") and loai == "canhcut":
        blob(ctx, 0, 18 * s, hr * 0.78, hy * 0.72); ctx.set_source_rgb(1, 1, 1); ctx.fill()
    if ear == "cup":  # tai cụp dài bên ngoài
        for sd in (-1, 1):
            ctx.move_to(sd * 100 * s, -hy * 0.6)
            ctx.curve_to(sd * 175 * s, -hy * 0.4, sd * 170 * s, hy * 0.6, sd * 130 * s, hy * 0.75)
            ctx.curve_to(sd * 110 * s, hy * 0.5, sd * 112 * s, -hy * 0.1, sd * 100 * s, -hy * 0.6)
            fill_stroke(ctx, (0.85, 0.66, 0.45), lw)
    if L.get("wrinkle"):
        _p(ctx, lw * 0.5)
        for i in range(3):
            ctx.move_to(-22 * s, (-80 + i * 14) * s); ctx.curve_to(-8 * s, (-86 + i * 14) * s, 8 * s, (-86 + i * 14) * s, 22 * s, (-80 + i * 14) * s); ctx.stroke()
    # mắt
    ey, ex = -2 * s, 46 * s
    for sd in (-1, 1):
        if blink or mood == "vui":
            _p(ctx, lw * 0.9); ctx.move_to(sd * ex - 14 * s, ey + 4 * s)
            ctx.curve_to(sd * ex - 6 * s, ey - 10 * s, sd * ex + 6 * s, ey - 10 * s, sd * ex + 14 * s, ey + 4 * s); ctx.stroke()
        else:
            r = 13 * s if mood != "ngac" else 16 * s
            blob(ctx, sd * ex, ey, r * 0.8, r * 1.25); ctx.set_source_rgb(*INK); ctx.fill()
            blob(ctx, sd * ex + 3 * s, ey - 6 * s, 3.5 * s, 3.5 * s); ctx.set_source_rgb(1, 1, 1); ctx.fill()
        if mood == "buon":
            _p(ctx, lw * 0.7); ctx.move_to(sd * (ex + 20 * s), ey - 30 * s); ctx.line_to(sd * (ex - 12 * s), ey - 24 * s); ctx.stroke()
    # má
    for sd in (-1, 1):
        blob(ctx, sd * 92 * s, 30 * s, 26 * s, 15 * s); ctx.set_source_rgba(*PINK, 0.9); ctx.fill()
    # mỏ / mũi / miệng
    if L.get("beak"):
        ctx.move_to(-16 * s, 20 * s); ctx.line_to(16 * s, 20 * s); ctx.line_to(0, 38 * s); ctx.close_path(); fill_stroke(ctx, (1, 0.72, 0.25), lw * 0.6)
    elif loai != "meo" or True:
        blob(ctx, 0, 22 * s, 7 * s, 5 * s); ctx.set_source_rgb(*INK); ctx.fill()
    m = max(0.0, min(1.0, noi))
    if m > 0.05:
        blob(ctx, 0, 44 * s, 10 * s, 12 * s * m + 2 * s); ctx.set_source_rgb(0.75, 0.25, 0.3); ctx.fill_preserve(); _p(ctx, lw * 0.6); ctx.stroke()
    elif mood == "buon":
        _p(ctx, lw * 0.6); ctx.move_to(-12 * s, 46 * s); ctx.curve_to(-4 * s, 38 * s, 4 * s, 38 * s, 12 * s, 46 * s); ctx.stroke()
    else:
        _p(ctx, lw * 0.6); ctx.move_to(-14 * s, 34 * s); ctx.curve_to(-7 * s, 44 * s, 0, 40 * s, 0, 34 * s)
        ctx.curve_to(0, 40 * s, 7 * s, 44 * s, 14 * s, 34 * s); ctx.stroke()
    ctx.restore()
