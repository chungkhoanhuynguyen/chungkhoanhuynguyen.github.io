# tao_sfx.py – sinh bộ tiếng động miễn phí bằng code (QL1 28/11), dùng dsp.py + sfx_gen.py chép từ
# mromidev/claude-animated-shorts (MIT, xem LICENSE_claude-animated-shorts). Chạy: python3 tao_sfx.py → *.wav 48kHz 16-bit.
import numpy as np, sfx_gen as G
from dsp import rng, write_wav, fades, st
def chuan(x, db=-3.0):
    x = np.asarray(x, float); p = np.abs(x).max() or 1; return x / p * 10 ** (db / 20)
def ghep(parts, gap):
    out = np.zeros(int(48000 * (gap * len(parts) + 0.5)))
    for k, p in enumerate(parts):
        i = int(48000 * gap * k); out[i:i + len(p)] += p[:len(out) - i]
    return out
B = {
 'vut_nhanh': lambda: G.whoosh(0.35, rng(1), peak=0.25),
 'vut_cham': lambda: G.whoosh(0.8, rng(2), peak=0.45, f_lo=250, f_hi=1600, tail=0.35),
 'xu_leng_keng': lambda: ghep([G.clink(rng(10 + k), bright=1.2) for k in range(5)], 0.07),
 'xu_roi_1': lambda: G.clink(rng(3), dur=0.25),
 'vo_tay': lambda: G.applause(2.5, rng(4), people=36),
 'dam_dong_xi_xao': lambda: G.babble(3.0, rng(5), 1.0, 1.0),
 'dam_dong_ui': lambda: G.whoa(rng(6)),
 'oi': lambda: G.oof(rng(7)),
 'gay_vo': lambda: G.wood_crack(rng(8)),
 'dut_gay_kim_loai': lambda: G.bolt_snap(rng(9)),
}
for k, f in B.items():
    try:
        x = f(); x = x[0] if isinstance(x, tuple) else x
        write_wav(f"{k}.wav", fades(chuan(x)), bits=16); print("OK", k, f"{(x.shape[-1]) / 48000:.2f}s")
    except Exception as e:
        print("LOI", k, e)
