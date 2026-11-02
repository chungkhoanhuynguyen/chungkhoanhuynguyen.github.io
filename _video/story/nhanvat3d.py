# Ảnh duyệt tạo hình 3D v2: mặt dễ thương hơn (mắt to long lanh, cười, má hồng) + quần áo/đạo cụ.
# blender -b -P nhanvat3d.py -- <out.png>
import bpy, math, sys, os
OUT = sys.argv[sys.argv.index("--") + 1]
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = 48; sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 1350, 1080
sc.view_settings.view_transform = "Standard"; sc.view_settings.look = "None"

def mat(n, rgb, rough=0.55, sheen=0.0, coat=0.0, emit=0.0):
    m = bpy.data.materials.new(n); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1); b.inputs["Roughness"].default_value = rough
    if sheen: b.inputs["Sheen Weight"].default_value = sheen
    if coat: b.inputs["Coat Weight"].default_value = coat
    if emit: b.inputs["Emission Color"].default_value = (*rgb, 1); b.inputs["Emission Strength"].default_value = emit
    return m
def ball(p, r, m, s=(1, 1, 1), parent=None, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_uv_sphere_add(location=p, radius=r, segments=48, ring_count=24, rotation=rot)
    o = bpy.context.object; o.scale = s; o.data.materials.append(m); bpy.ops.object.shade_smooth()
    if parent: o.parent = parent
    return o
def cyl(p, r, d, m, rot=(0, 0, 0), parent=None):
    bpy.ops.mesh.primitive_cylinder_add(location=p, radius=r, depth=d, rotation=rot, vertices=48); o = bpy.context.object
    o.data.materials.append(m); bpy.ops.object.shade_smooth()
    if parent: o.parent = parent
    return o
def box(p, s, m, rot=(0, 0, 0), parent=None, bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(location=p, rotation=rot); o = bpy.context.object; o.scale = tuple(v / 2 for v in s); o.data.materials.append(m)
    if bevel:
        md = o.modifiers.new("b", "BEVEL"); md.width = bevel; md.segments = 4
    if parent: o.parent = parent
    return o
def empty(n, p, parent=None):
    o = bpy.data.objects.new(n, None); bpy.context.collection.objects.link(o); o.location = p
    if parent: o.parent = parent
    return o

INK = mat("muc", (0.02, 0.02, 0.03), 0.15, coat=1.0); WHITE = mat("trang", (1, 1, 1), 0.2, emit=0.6)
PINK = mat("hong", (1.0, 0.42, 0.5), 0.6); MOUTH = mat("mieng", (0.55, 0.12, 0.18), 0.4); TONGUE = mat("luoi", (1.0, 0.45, 0.5), 0.4)

def mat_cuoi(head, y=-0.6):
    # mắt to long lanh: tròng đen lớn + 2 đốm sáng
    for s in (-1, 1):
        ball((s * 0.25, y + 0.02, 0.06), 0.13, INK, (0.9, 0.55, 1.15), head)
        ball((s * 0.25 - s * 0.03, y - 0.06, 0.13), 0.045, WHITE, (1, 0.6, 1), head)
        ball((s * 0.25 + s * 0.04, y - 0.07, 0.0), 0.022, WHITE, (1, 0.6, 1), head)
        ball((s * 0.43, y + 0.08, -0.13), 0.12, PINK, (1.2, 0.35, 0.75), head)
    # miệng cười há (nửa đĩa) + lưỡi
    m = ball((0, y - 0.01, -0.24), 0.11, MOUTH, (1.1, 0.4, 0.6), head)
    ball((0, y - 0.03, -0.29), 0.06, TONGUE, (1.2, 0.4, 0.5), head)

def cun_bo(x):
    F = mat("cho", (1.0, 0.9, 0.72), 0.75, sheen=0.6); E = mat("tai", (0.86, 0.62, 0.38), 0.75, sheen=0.6)
    SHIRT = mat("ao", (0.55, 0.75, 0.98), 0.6); TIE = mat("cavat", (0.85, 0.15, 0.2), 0.4); PHONE = mat("dt", (0.08, 0.08, 0.1), 0.2, coat=1)
    SCR = mat("manhinh", (0.3, 0.7, 1.0), 0.2, emit=2.5)
    root = empty("cun", (x, 0, 0)); root.rotation_euler = (0, 0, 0.25)
    ball((0, 0, 0.62), 0.62, SHIRT, (1.1, 1.0, 0.95), root)                 # thân mặc áo sơ mi
    for s in (-1, 1):
        box((s * 0.12, -0.55, 1.08), (0.22, 0.05, 0.16), mat("co", (0.95, 0.97, 1.0), 0.5), (0.35, 0, s * 0.5), root, 0.03)  # cổ áo
        ball((s * 0.3, -0.1, 0.07), 0.2, F, (1.1, 1.3, 0.6), root)
    box((0, -0.6, 0.85), (0.11, 0.04, 0.36), TIE, (0.18, 0, 0), root, 0.02)   # cà vạt
    ball((-0.68, -0.15, 0.75), 0.2, SHIRT, (1, 1, 1.35), root)
    arm = ball((0.62, -0.35, 0.95), 0.2, SHIRT, (1, 1, 1.35), root, rot=(1.1, 0, -0.3))
    ball((0.55, -0.62, 1.15), 0.14, F, parent=root)                           # bàn tay
    box((0.52, -0.72, 1.32), (0.2, 0.03, 0.36), PHONE, (0.2, 0, -0.15), root, 0.02)   # điện thoại
    box((0.52, -0.74, 1.32), (0.17, 0.01, 0.31), SCR, (0.2, 0, -0.15), root)
    head = empty("cun_dau", (0, 0, 1.62), root)
    ball((0, 0, 0), 0.66, F, (1.12, 1.0, 0.95), head)
    ball((0, -0.52, -0.16), 0.24, mat("mom", (1, 0.96, 0.88), 0.7, sheen=0.5), (1.35, 0.6, 0.8), head)
    ball((0, -0.68, -0.08), 0.075, INK, parent=head)
    for s in (-1, 1): ball((s * 0.74, 0.0, -0.12), 0.22, E, (0.55, 0.5, 1.7), head, rot=(0, s * 0.25, 0))
    mat_cuoi(head)
    return root

def gau_gao(x):
    F = mat("gau", (0.72, 0.47, 0.28), 0.8, sheen=0.7); C = mat("gauk", (0.98, 0.86, 0.68), 0.8, sheen=0.5)
    APRON = mat("tapde", (0.98, 0.55, 0.2), 0.7); BOWL = mat("bat", (0.95, 0.95, 0.92), 0.3, coat=0.5); XOI = mat("xoi", (1.0, 0.85, 0.35), 0.8)
    HAT = mat("non", (0.93, 0.82, 0.55), 0.8)
    root = empty("gau", (x, 0, 0)); root.rotation_euler = (0, 0, -0.25)
    ball((0, 0, 0.64), 0.66, F, (1.12, 1.0, 0.95), root)
    box((0, -0.55, 0.55), (0.75, 0.06, 0.7), APRON, (0.08, 0, 0), root, 0.06)  # tạp dề cam
    ball((0, -0.6, 0.62), 0.11, mat("logo", (1, 1, 1), 0.5), (1, 0.3, 1), root)
    for s in (-1, 1): ball((s * 0.32, -0.1, 0.07), 0.21, F, (1.1, 1.3, 0.6), root)
    ball((0.7, -0.15, 0.75), 0.21, F, (1, 1, 1.35), root)
    ball((-0.6, -0.4, 0.95), 0.21, F, (1, 1, 1.3), root, rot=(1.2, 0, 0.3))
    b = cyl((-0.55, -0.72, 1.12), 0.2, 0.12, BOWL, parent=root)               # bát xôi
    ball((-0.55, -0.72, 1.2), 0.17, XOI, (1, 1, 0.55), root)
    head = empty("gau_dau", (0, 0, 1.66), root)
    ball((0, 0, 0), 0.66, F, (1.12, 1.0, 0.95), head)
    ball((0, -0.52, -0.16), 0.25, C, (1.35, 0.6, 0.8), head)
    ball((0, -0.68, -0.07), 0.08, INK, parent=head)
    for s in (-1, 1):
        ball((s * 0.52, 0.0, 0.5), 0.2, F, (1, 0.6, 1), head); ball((s * 0.52, -0.08, 0.5), 0.11, PINK, (1, 0.4, 1), head)
    cyl((0, 0.05, 0.62), 0.6, 0.05, HAT, parent=head)                          # nón lá
    bpy.ops.mesh.primitive_cone_add(location=(0, 0.05, 0.82), radius1=0.6, depth=0.38, vertices=48); o = bpy.context.object
    o.data.materials.append(HAT); o.parent = head; bpy.ops.object.shade_smooth()
    mat_cuoi(head)
    return root

# phông: tường vàng phố cổ + cửa chớp xanh
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (1.0, 0.95, 0.85, 1); w.node_tree.nodes["Background"].inputs[1].default_value = 0.7
box((0, 0, -0.05), (12, 8, 0.1), mat("via", (0.75, 0.68, 0.6), 0.8))
box((0, 2.2, 3), (12, 0.2, 6), mat("tuongvang", (0.98, 0.8, 0.35), 0.85))
for x in (-2.2, 2.2):
    for s in (-1, 1):
        box((x + s * 0.42, 2.08, 2.6), (0.8, 0.06, 1.9), mat("chop", (0.15, 0.55, 0.4), 0.6), parent=None, bevel=0.02)
cun_bo(-1.05); gau_gao(1.05)
for x, col in ((-3.2, (0.2, 0.5, 0.95)), (3.3, (0.95, 0.25, 0.25))):                 # ghế nhựa trà đá
    box((x, -0.3, 0.45), (0.5, 0.5, 0.08), mat("ghe%d" % int(x), col, 0.4), bevel=0.03)
L = bpy.data.lights.new("k", "AREA"); L.energy = 1200; L.size = 5; o = bpy.data.objects.new("k", L); o.location = (0, -5, 5); o.rotation_euler = (0.75, 0, 0); bpy.context.collection.objects.link(o)
S = bpy.data.lights.new("s", "SUN"); S.energy = 3; S.color = (1, 0.88, 0.7); o2 = bpy.data.objects.new("s", S); o2.rotation_euler = (0.8, 0.4, 0.7); bpy.context.collection.objects.link(o2)
R = bpy.data.lights.new("r", "AREA"); R.energy = 500; R.size = 3; o3 = bpy.data.objects.new("r", R); o3.location = (0, 3, 4); o3.rotation_euler = (-0.8, 0, 0); bpy.context.collection.objects.link(o3)
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); bpy.context.collection.objects.link(cam); sc.camera = cam
cam.data.lens = 40; cam.location = (0, -6.2, 1.9); cam.rotation_euler = (math.radians(86), 0, 0)
sc.render.filepath = OUT; bpy.ops.render.render(write_still=True)
