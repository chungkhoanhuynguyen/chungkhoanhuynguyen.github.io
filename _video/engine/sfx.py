import numpy as np, wave, subprocess
SR = 44100
def coin(f1=2093, f2=2637, dur=0.45, amp=0.5):
    t = np.arange(int(SR*dur))/SR; n1 = int(SR*0.07)
    s = np.zeros_like(t)
    a = np.sin(2*np.pi*f1*t[:n1])*np.exp(-t[:n1]*30); s[:n1] += a
    t2 = t[n1:]-t[n1]
    s[n1:] += (np.sin(2*np.pi*f2*t2) + 0.4*np.sin(2*np.pi*f2*2*t2))*np.exp(-t2*7)
    return s*amp
def tick(dur=0.03, amp=0.25):
    t = np.arange(int(SR*dur))/SR
    return np.sin(2*np.pi*3200*t)*np.exp(-t*160)*amp
def track(total, events):
    out = np.zeros(int(SR*total)+SR)
    for st, kind in events:
        s = coin() if kind == "coin" else tick()
        i = int(st*SR); out[i:i+len(s)] += s[:len(out)-i]
    return out
def write(path, x):
    x = np.clip(x, -1, 1); 
    with wave.open(path, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x*32767).astype(np.int16).tobytes())
def money_events(b, scenes):
    ev = []
    for i, sc in enumerate(scenes):
        if not sc.get("ting"): continue
        s0 = b[i] + sc.get("t0", 0); d = sc.get("dur", 0.9)
        # ticks speeding up during count, then coins "tinh tinh"
        k = 0.0
        while k < d - 0.05:
            ev.append((s0 + k, "tick")); k += 0.09 if k < d*0.7 else 0.13
        ev += [(s0 + d, "coin"), (s0 + d + 0.18, "coin")]
    return ev
def mix(video, b, scenes, out, sfx_db=-4):
    dur = b[-1]; tr = track(dur, money_events(b, scenes)); write("/tmp/sfx.wav", tr)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", "/tmp/sfx.wav", "-filter_complex",
                    "[1:a]volume=%ddB,aresample=44100[s];[0:a][s]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]" % sfx_db,
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", out])
