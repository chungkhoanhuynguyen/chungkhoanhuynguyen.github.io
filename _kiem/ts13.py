# -*- coding: utf-8 -*-
"""QL1 13/11 – ts13: vòng cuối V2: (1) một nguồn P/B (WiData quý), (2) lọc thanh khoản, (3) xét hằng tuần."""
import subprocess, os, sys
H = os.path.dirname(os.path.abspath(__file__))
COMBO = [("vnd", "0", "0"), ("wi", "0", "0"), ("wi", "0", "5"), ("wi", "0", "20"), ("wi", "1", "0"), ("wi", "1", "5")]
for pbs, wk, liq in COMBO:
    env = dict(os.environ, PBS=pbs, WEEK=wk, LIQ=liq, NR="1000")
    p = subprocess.run([sys.executable, "-u", os.path.join(H, "ts13core.py")], env=env, capture_output=True, text=True)
    for l in p.stdout.splitlines():
        if l.startswith("#") or "PB nguon moi" in l or "LOI" in l: print(l, flush=True)
    if p.returncode: print("LOI CHAY", pbs, wk, liq, p.stderr[-2000:], flush=True)
