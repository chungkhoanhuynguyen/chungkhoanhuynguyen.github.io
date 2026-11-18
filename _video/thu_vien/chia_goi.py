# Chia thư mục mô hình Poly Haven thành nhiều gói zip dưới 2GB (giới hạn tệp của GitHub release). Chạy trong thư mục W.
import os, subprocess
ds = sorted(os.listdir("polyhaven/models")); nhom, cur, sz = [], [], 0
for d in ds:
    t = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(os.path.join("polyhaven/models", d)) for f in fs)
    if cur and sz + t > 1.6e9: nhom.append(cur); cur, sz = [], 0
    cur.append(d); sz += t
if cur: nhom.append(cur)
for i, g in enumerate(nhom): subprocess.run(["zip", "-qr", f"../polyhaven_models_{i+1}.zip"] + [os.path.join("polyhaven/models", d) for d in g], check=True)
print("so phan", len(nhom))
