# Thử A/B giọng: A = VieNeu Huy70_HaiDang30 (đang dùng) · B = OmniVoice nhân bản từ mẫu giọng thật 14s.
import base64, json, os, subprocess, sys, time, traceback, numpy as np, soundfile as sf
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")); sys.path.insert(0, ROOT); import hncodec
OUT = "ab_out"; os.makedirs(OUT, exist_ok=True)
CAU = [
    "Chào anh chị, hôm nay thị trường giằng co khá mạnh, dòng tiền vẫn đang đứng ngoài quan sát.",
    "Lương ba mươi triệu một tháng, vậy mà mới đến ngày mùng năm, tài khoản chỉ còn ba trăm mười hai nghìn đồng.",
    "Thị trường chưa đẹp thì mình giữ tiền, kiên nhẫn chờ điểm mua an toàn, anh chị đừng sốt ruột nhé.",
]
ref = hncodec.load(os.path.join(ROOT, "_video/engine/ref_mau.bin"))
open("ref.ogg", "wb").write(base64.b64decode(ref["ogg_b64"]))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "ref.ogg", "-ac", "1", "-ar", "24000", "ref.wav"], check=True)
def norm(i, o):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", i, "-af", "loudnorm=I=-16:TP=-1.5", "-ar", "24000", "-ac", "1", o], check=True)
mode = sys.argv[1]
if mode == "A":
    from vieneu import Vieneu
    v = json.loads(os.environ["HN_VOICE_JSON"])
    V = {"speaker_emb": np.asarray(v["speaker_emb"], np.float32), "codes": np.asarray(v["codes"], dtype=v.get("codes_dtype", "int64"))}
    tts = Vieneu()
    for i, c in enumerate(CAU, 1):
        a = np.asarray(tts.infer(c, voice=V, temperature=0.7), np.float32).reshape(-1)
        tts.save(a, "t.wav")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "t.wav", "-af", "atempo=0.95", "t2.wav"], check=True)
        norm("t2.wav", f"{OUT}/A_vieneu_{i}.wav"); print("A", i, flush=True)
else:
    from faster_whisper import WhisperModel
    seg, _ = WhisperModel("medium", device="cpu", compute_type="int8").transcribe("ref.wav", language="vi", beam_size=5)
    rt = " ".join(s.text.strip() for s in seg).strip(); print("REF_TEXT:", rt, flush=True)
    open(f"{OUT}/ref_text.txt", "w").write(rt)
    import torch
    from omnivoice import OmniVoice
    for mid in ["termanteus/omnivoice-vietnamese", "k2-fsa/OmniVoice"]:
        try:
            t0 = time.time(); tts = OmniVoice.from_pretrained(mid, device_map="cpu", dtype=torch.float32)
            tag = "vn" if "viet" in mid else "goc"
            for i, c in enumerate(CAU, 1):
                r = tts.generate(text=c, language="vietnamese", ref_audio="ref.wav", ref_text=rt)
                a = r[0] if isinstance(r, (list, tuple)) else r
                a = a.detach().cpu().numpy() if hasattr(a, "detach") else np.asarray(a)
                sf.write("t.wav", a.reshape(-1).astype(np.float32), 24000)
                norm("t.wav", f"{OUT}/B_omni_{tag}_{i}.wav"); print("B", tag, i, "%.0fs" % (time.time() - t0), flush=True)
            del tts
        except Exception:
            traceback.print_exc()
