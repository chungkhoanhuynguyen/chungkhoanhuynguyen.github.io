import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
F = lambda w, s: ImageFont.truetype("/tmp/cw/_video/engine/fonts/BeVietnamPro-%s.ttf" % w, s)
def bia(img, lines, badge, out):
    W, H = 1280, 720; im = Image.new("RGB", (W, H), (24, 12, 40)); d = ImageDraw.Draw(im)
    for y in range(H): a=y/H; d.line([(0,y),(W,y)], fill=(int(24+34*a),int(12+12*a),int(40+48*a)))
    ph = Image.open(img).convert("RGB"); r = max(760/ph.width, H/ph.height); ph = ph.resize((int(ph.width*r)+1, int(ph.height*r)+1))
    ph = ph.crop(((ph.width-760)//2, (ph.height-H)//2, (ph.width-760)//2+760, (ph.height-H)//2+H))
    m = Image.new("L", (760, H)); md = ImageDraw.Draw(m)
    for x in range(760): md.line([(x,0),(x,H)], fill=min(235, int(235*x/300)))
    im.paste(ph, (W-760, 0), m)
    pt = Image.open("/tmp/cw/_video/engine/chu_kenh.png").convert("RGBA"); h = 500; pt = pt.resize((int(pt.width*h/pt.height), h), Image.LANCZOS)
    px = W - pt.width - 10
    gl = Image.new("L", (W, H)); ImageDraw.Draw(gl).ellipse([px+20, H-h-10, px+pt.width, H+160], fill=170)
    im.paste(Image.new("RGB", (W, H), (20, 10, 34)), (0, 0), gl.filter(ImageFilter.GaussianBlur(50)))
    im.paste(pt, (px, H-h), pt); d = ImageDraw.Draw(im)
    d.text((48, 26), "HUY NGUYỄN", font=F("Black", 28), fill=(255,255,255)); d.text((48+F("Black",28).getlength("HUY NGUYỄN")+10, 33), "CHỨNG KHOÁN", font=F("Bold", 20), fill=(255,204,0))
    y = 105
    for i, s in enumerate(lines):
        sz = 112
        while F("Black", sz).getlength(s) > 820: sz -= 4
        d.text((48, y), s, font=F("Black", sz), fill=(255,255,255) if i%2==0 else (255,204,0), stroke_width=6, stroke_fill=(10,5,20)); y += sz + 20
    f = F("Black", 50); w = f.getlength(badge)
    d.rounded_rectangle([48, y+10, 48+w+44, y+88], 14, fill=(226,46,46)); d.text((70, y+18), badge, font=f, fill=(255,255,255))
    d.text((48, H-52), "chungkhoanhuynguyen", font=F("Bold", 24), fill=(255,255,255)); d.text((48+F("Bold",24).getlength("chungkhoanhuynguyen"), H-52), ".com", font=F("Bold", 24), fill=(255,204,0))
    im.save(out)
if __name__ == "__main__":
    bia(sys.argv[1], sys.argv[3].split("|"), sys.argv[4], sys.argv[2])
