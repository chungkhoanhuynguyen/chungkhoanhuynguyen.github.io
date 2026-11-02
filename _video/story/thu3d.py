# Clip thử 3D (Blender miễn phí, chạy trên xưởng GitHub): cùng cảnh "Mới ngày 26 mà ví đã rỗng"
# blender -b -P thu3d.py -- <out_dir> [sec] [w] [h] [spp]
import bpy, math, sys, os
a = sys.argv[sys.argv.index("--") + 1:]
OUT = a[0]; SEC = float(a[1]) if len(a) > 1 else 10; W = int(a[2]) if len(a) > 2 else 720; H = int(a[3]) if len(a) > 3 else 1280
SPP = int(a[4]) if len(a) > 4 else 16; FPS = 24
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = SPP; sc.cycles.use_denoising = True
sc.cycles.max_bounces = 4
sc.render.resolution_x, sc.render.resolution_y = W, H; sc.render.fps = FPS
sc.frame_start, sc.frame_end = 1, int(SEC * FPS)
sc.render.image_settings.file_format = "PNG"; sc.render.filepath = os.path.join(OUT, "f_")
try: sc.view_settings.view_transform = "AgX"
except Exception: sc.view_settings.view_transform = "Filmic"

def mat(n, rgb, rough=0.55, emit=0.0, sss=0.0):
    m = bpy.data.materials.new(n); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1); b.inputs["Roughness"].default_value = rough
    if emit: b.inputs["Emission Color"].default_value = (*rgb, 1); b.inputs["Emission Strength"].default_value = emit
    return m
def ball(loc, r, m, sx=1, sy=1, sz=1, parent=None, seg=32):
    bpy.ops.mesh.primitive_uv_sphere_add(location=loc, radius=r, segments=seg, ring_count=seg // 2)
    o = bpy.context.object; o.scale = (sx, sy, sz); o.data.materials.append(m); bpy.ops.object.shade_smooth()
    if parent: o.parent = parent
    return o
def box(loc, size, m):
    bpy.ops.mesh.primitive_cube_add(location=loc); o = bpy.context.object; o.scale = tuple(v / 2 for v in size)
    o.data.materials.append(m); return o
def text(s, loc, size, m, rot=(math.pi / 2, 0, 0)):
    bpy.ops.object.text_add(location=loc, rotation=rot); o = bpy.context.object; o.data.body = s; o.data.size = size
    o.data.align_x = "CENTER"; o.data.extrude = 0.01
    f = "/tmp/cw/_video/engine/fonts/BeVietnamPro-Black.ttf"
    for p in (f, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine", "fonts", "BeVietnamPro-Black.ttf")):
        if os.path.exists(p): o.data.font = bpy.data.fonts.load(p); break
    o.data.materials.append(m); return o

INK = mat("muc", (0.03, 0.03, 0.04), 0.3); WHITE = mat("trang", (1, 1, 1), 0.25); PINK = mat("hong", (1.0, 0.45, 0.5), 0.6)
def thu(kind, x, rotz):
    fur = {"gau": (0.62, 0.38, 0.2), "cho": (0.98, 0.86, 0.62)}[kind]
    F = mat(kind, fur, 0.7); C = mat(kind + "k", (1.0, 0.92, 0.8), 0.7)
    root = bpy.data.objects.new(kind, None); bpy.context.collection.objects.link(root); root.location = (x, 0, 0); root.rotation_euler = (0, 0, rotz)
    ball((0, 0, 0.62), 0.62, F, 1.08, 1.0, 0.95, root)              # thân mũm mĩm
    ball((0, -0.42, 0.55), 0.42, C, 1.0, 0.45, 0.9, root)           # bụng
    for s in (-1, 1): ball((s * 0.3, -0.1, 0.08), 0.2, F, 1.1, 1.3, 0.6, root)   # chân
    arms = [ball((s * 0.66, -0.1, 0.78), 0.2, F, 1, 1, 1.35, root) for s in (-1, 1)]
    head = bpy.data.objects.new(kind + "_dau", None); bpy.context.collection.objects.link(head); head.parent = root; head.location = (0, 0, 1.5)
    ball((0, 0, 0), 0.62, F, 1.12, 1.0, 0.95, head)
    ball((0, -0.5, -0.12), 0.24, C, 1.3, 0.6, 0.85, head)
    ball((0, -0.64, -0.05), 0.07, INK, parent=head)
    eyes = []
    for s in (-1, 1):
        e = ball((s * 0.24, -0.55, 0.08), 0.075, INK, 0.85, 0.6, 1.2, head); eyes.append(e)
        ball((s * 0.21, -0.6, 0.12), 0.022, WHITE, parent=head)
        ball((s * 0.4, -0.5, -0.08), 0.1, PINK, 1.2, 0.4, 0.7, head)
        if kind == "gau":
            ball((s * 0.5, 0.0, 0.48), 0.2, F, 1, 0.6, 1, head); ball((s * 0.5, -0.08, 0.48), 0.11, PINK, 1, 0.4, 1, head)
        else:
            ball((s * 0.72, 0.0, -0.1), 0.2, mat("tai", (0.82, 0.6, 0.38), 0.7), 0.6, 0.5, 1.6, head)
    mouth = ball((0, -0.62, -0.2), 0.06, mat("mieng", (0.6, 0.15, 0.2), 0.5), 1.2, 0.4, 0.2, head)
    return root, head, arms, eyes, mouth

def anim(root, head, arms, eyes, mouth, talk, walk=None, point=None):
    N = sc.frame_end
    for f in range(1, N + 1):
        t = f / FPS
        root.location.z = abs(math.sin(t * 5)) * 0.05 if walk and walk[0] <= t <= walk[1] else math.sin(t * 2.5) * 0.015
        if walk:
            k = min(1, max(0, (t - walk[0]) / (walk[1] - walk[0]))); root.location.x = walk[2] + (walk[3] - walk[2]) * k
            root.keyframe_insert("location", frame=f)
        else: root.keyframe_insert("location", frame=f)
        head.rotation_euler = (math.sin(t * 1.7) * 0.05, 0, math.sin(t * 1.1) * 0.12); head.keyframe_insert("rotation_euler", frame=f)
        on = talk[0] <= t <= talk[1]
        mouth.scale = (1.2, 0.4, 0.2 + (abs(math.sin(t * 11)) * 1.6 if on else 0)); mouth.keyframe_insert("scale", frame=f)
        bl = (t % 3.1) < 0.12
        for e in eyes: e.scale = (0.85, 0.6, 0.15 if bl else 1.2); e.keyframe_insert("scale", frame=f)
        if point and t > point:
            arms[0].rotation_euler = (-1.3 + math.sin(t * 4) * 0.1, 0, 0)
        else:
            arms[0].rotation_euler = (math.sin(t * 2) * 0.1, 0, 0)
        arms[0].keyframe_insert("rotation_euler", frame=f)

# phòng
world = bpy.data.worlds.new("w"); sc.world = world; world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (1.0, 0.93, 0.82, 1); world.node_tree.nodes["Background"].inputs[1].default_value = 0.6
box((0, 0, -0.05), (14, 10, 0.1), mat("san", (0.85, 0.66, 0.45), 0.6))
box((0, 3, 3), (14, 0.2, 6.5), mat("tuong", (1.0, 0.92, 0.8), 0.9))
box((-2.2, 2.85, 3.6), (1.8, 0.1, 2.0), mat("kinh", (0.7, 0.85, 1.0), 0.1, emit=1.5))
cal = box((1.6, 2.85, 3.7), (1.4, 0.08, 1.7), WHITE); box((1.6, 2.8, 4.38), (1.4, 0.06, 0.4), mat("xanh", (0.15, 0.3, 0.6), 0.5))
text("THÁNG 11", (1.6, 2.75, 4.3), 0.2, WHITE); text("26", (1.6, 2.75, 3.25), 0.85, INK)
d = thu("cho", -1.0, 0.25); g = thu("gau", 4.5, -0.25)
anim(*d, talk=(0.5, 4.5)); anim(*g, talk=(5.2, 9.5), walk=(3.8, 5.0, 4.5, 1.1), point=5.5)
# ánh sáng + máy quay
L = bpy.data.lights.new("k", "AREA"); L.energy = 900; L.size = 6; o = bpy.data.objects.new("k", L); o.location = (0, -4, 6); o.rotation_euler = (0.6, 0, 0); bpy.context.collection.objects.link(o)
S = bpy.data.lights.new("s", "SUN"); S.energy = 2.5; S.color = (1, 0.9, 0.75); o2 = bpy.data.objects.new("s", S); o2.rotation_euler = (0.9, 0.3, 0.6); bpy.context.collection.objects.link(o2)
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); bpy.context.collection.objects.link(cam); sc.camera = cam
cam.data.lens = 30; cam.rotation_euler = (math.radians(82), 0, 0)
for f, x in ((1, -0.6), (sc.frame_end, 0.4)):
    cam.location = (x, -7.4, 2.3); cam.keyframe_insert("location", frame=f)
os.makedirs(OUT, exist_ok=True)
import time; t0 = time.time()
bpy.ops.render.render(animation=True)
open(os.path.join(OUT, "thoi_gian.txt"), "w").write("3D: %d khung %dx%d spp=%d, %.0f giây dựng (%.2f s/khung)\n" % (sc.frame_end, W, H, SPP, time.time() - t0, (time.time() - t0) / sc.frame_end))
