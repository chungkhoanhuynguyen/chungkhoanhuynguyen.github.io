import json, time, datetime, urllib.request, os, zlib, base64
U = sorted(set("ACB BCM BID BMP BSR BVH BWE CII CMG CTD CTG CTR CTS DBC DCM DGC DGW DHC DIG DPM DXG DXS EIB EVF FPT FRT FTS GAS GEX GMD GVR HAG HCM HDB HDC HDG HHV HPG HSG HT1 IMP KBC KDC KDH KOS LPB MBB MSB MSN MWG NAB NKG NLG NT2 NVL OCB PAN PC1 PDR PHR PLX PNJ POW PTB PVD PVT REE SAB SBT SCS SHB SIP SJS SSB SSI STB SZC TCB TCH TPB VCB VCG VCI VDS VGC VHC VHM VIB VIC VIX VJC VND VNM VPB VPI VRE VSC VTP HAH ANV DPG ELC MSR ACV VGI QNS OIL VEA FOX PVS SHS CEO IDC L14 TNG HUT VCS PVC DTD".split()))
UA = {"User-Agent": "Mozilla/5.0"}
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r: return json.load(r)
def bars(sym, days=400):
    to = int(time.time()); fr = to - days*86400
    try:
        j = get(f"https://dchart-api.vndirect.com.vn/dchart/history?resolution=D&symbol={sym}&from={fr}&to={to}")
        if j.get("c"): return j["t"], j["c"], j.get("v") or [0]*len(j["c"])
    except Exception as e: print(sym, "vnd", e)
    try:
        j = get(f"https://apipubaws.tcbs.com.vn/stock-insight/v2/stock/bars-long-term?ticker={sym}&type=stock&resolution=D&from={fr}&to={to}")
        d = j.get("data") or []
        if d: return [x["tradingDate"] for x in d], [x["close"]/1000 for x in d], [x.get("volume", 0) for x in d]
    except Exception as e: print(sym, "tcbs", e)
    return None
def _q(c, n): return c[-1]/c[-n-1]-1 if len(c) > n else None
_B = (
    "c-nPSL9Wv<5Z&h#qq4F4)7DNPA`#&T>{vw+N?W(FlGyonTFNmHCt!<U!3v4L?7v8F!q`cRzTihnG9JH~dGkCr`lE#$iZa+~0~Vx$"
    "_gMh=tkJ!$j3t)(wcLTy1G*8{3PsihFDbkM9<vNKS`AVighvh`Y(hA?c)vbYZNzY84;|SQvYa3B1FoKQ^-QJqf-E8y0;6;lu{mdq"
    "t++@5Uchj9_yv!jFArbTe%06V{7nJb%kx(l&OcNQ>&x$-Y7c5(pTDasaAa)a5KMw^iZ73l!H0W-%#xUflgXpxul+i`+0m<L%+X*J"
    "TfUr|81B%B<|dg8Vp6Ax`&zHeJFNtW)(R|2Zy>DeQ1161n6FVwEYejc6lZ~jvvQ)3N3*Q@UZ^eE%FRG*Zc*7*Tag=mKriBXiDZ%X"
    "mQTLXxpJw>1*cBS5n<v9VdBxroin*Qlbh2Q|L4IDu23FbvCp>VtPplaceQ*<td=)cjsVWawC|^6bT)bO3=7*=rpb#j;^Z3hb98cZ"
    "g!vPel_eeJ8)PSzwiTi$Y#GzQ%W1V4NFzSwZPl%}6_^Z6F>7WhxxzzmbM0`{-v){LxWqyoI$^3ojC($$pOw?0aYT7KX*wtJj?<Mw"
    "2Cckz*UET$K8uU>dKEKl6~o`=z*!j#x_5U2iHR-2Fl_$`zr{qb$Q=5X4#SYhve!MqZ5sRm@^2JX"
)
exec(zlib.decompress(base64.b85decode(_B)).decode())
os.makedirs("data", exist_ok=True)
now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
json.dump(dict(updated=now.strftime("%H:%M %d/%m/%Y"), universe=n, top=top), open("data/rs.json", "w"), ensure_ascii=False)
print("ok", n)
