"""Trộn giọng + nhạc nền lo-fi nhẹ (nhạc lùi sau giọng, sidechain), loudnorm I=-13. python3 mix.py voice.wav timing.json mix.wav"""
import sys, os, subprocess, json
ENG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"); sys.path.insert(0, ENG)
import music, nhac20
v, tj, out = sys.argv[1:4]; total = json.load(open(tj))["total"] + 1.0
x = nhac20.tao(3, total + 2)[:int(music.SR * total)]; music.write("/tmp/bgm_the.wav", x)
fc = ("[1:a]volume=-20dB,afade=t=in:st=0:d=4,aresample=44100[m];[0:a]highpass=f=75,aresample=44100,asplit=2[v][sc];"
      "[m][sc]sidechaincompress=threshold=0.05:ratio=5:attack=100:release=700[md];[v][md]amix=inputs=2:duration=longest:normalize=0,"
      "loudnorm=I=-13:TP=-1.5:LRA=7[a]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", v, "-i", "/tmp/bgm_the.wav", "-filter_complex", fc, "-map", "[a]", "-ar", "44100", out], check=True)
