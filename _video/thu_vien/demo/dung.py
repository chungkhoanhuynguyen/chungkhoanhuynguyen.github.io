# blender -b -P dung.py -- <W thư mục tài nguyên> <OUT> : dựng 10 ảnh demo từ canh.py (Cycles CPU).
import bpy, sys, os, glob, math, mathutils
a = sys.argv[sys.argv.index("--") + 1:]; W, OUT = a[0], a[1]; os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from canh import C
CHI = os.environ.get("CHI", "")
def xoa():
    bpy.ops.wm.read_factory_settings(use_empty=True)
def tex_mat(ten, rep):
    d = os.path.join(W, "polyhaven/textures", ten); fs = sorted(glob.glob(d + "/**/*.*", recursive=True))
    pick = lambda *ks: next((f for f in fs if any(k in os.path.basename(f).lower() for k in ks) and f.lower().endswith(('.jpg', '.png', '.exr'))), None)
    m = bpy.data.materials.new(ten); m.use_nodes = True; nt = m.node_tree; b = nt.nodes["Principled BSDF"]
    tc = nt.nodes.new("ShaderNodeTexCoord"); mp = nt.nodes.new("ShaderNodeMapping"); mp.inputs["Scale"].default_value = (rep, rep, rep)
    nt.links.new(tc.outputs["UV"], mp.inputs["Vector"])
    def img(f, col=True):
        n = nt.nodes.new("ShaderNodeTexImage"); n.image = bpy.data.images.load(f)
        if not col: n.image.colorspace_settings.name = "Non-Color"
        nt.links.new(mp.outputs["Vector"], n.inputs["Vector"]); return n
    f = pick("diff", "col", "albedo")
    if f: nt.links.new(img(f).outputs["Color"], b.inputs["Base Color"])
    f = pick("rough")
    if f: nt.links.new(img(f, False).outputs["Color"], b.inputs["Roughness"])
    else:
        f = pick("_arm")
        if f:
            sp = nt.nodes.new("ShaderNodeSeparateColor"); nt.links.new(img(f, False).outputs["Color"], sp.inputs["Color"]); nt.links.new(sp.outputs["Green"], b.inputs["Roughness"])
    f = pick("nor_gl", "normal")
    if f:
        nm = nt.nodes.new("ShaderNodeNormalMap"); nt.links.new(img(f, False).outputs["Color"], nm.inputs["Color"]); nt.links.new(nm.outputs["Normal"], b.inputs["Normal"])
    if not fs: print("LOI thieu vat lieu", ten)
    return m
def mat_phang(ten, kt, loc, rot, mat, rep):
    bpy.ops.mesh.primitive_plane_add(size=1, location=loc, rotation=rot); o = bpy.context.object; o.name = ten
    o.scale = (kt[0], kt[1], 1); bpy.ops.object.transform_apply(scale=True)
    bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.uv.cube_project(cube_size=1.0); bpy.ops.object.mode_set(mode='OBJECT')
    o.data.materials.append(mat); return o
def nhap(ten):
    f = os.path.join(W, "polyhaven/models", ten, ten + ".gltf")
    if not os.path.exists(f):
        g = glob.glob(os.path.join(W, "polyhaven/models", ten, "*.gltf")) + glob.glob(os.path.join(W, "polyhaven/models", ten, "*.glb"))
        if not g: print("LOI thieu mo hinh", ten); return None
        f = g[0]
    truoc = set(bpy.data.objects); bpy.ops.import_scene.gltf(filepath=f); moi = [o for o in bpy.data.objects if o not in truoc]
    goc = bpy.data.objects.new(ten, None); bpy.context.scene.collection.objects.link(goc)
    for o in moi:
        if o.parent is None: o.parent = goc
    return goc
def bbox(goc):
    pts = []
    for o in goc.children_recursive:
        if o.type == 'MESH': pts += [o.matrix_world @ mathutils.Vector(c) for c in o.bound_box]
    if not pts: return (0, 0, 0), (0, 0, 0)
    return tuple(min(p[i] for p in pts) for i in range(3)), tuple(max(p[i] for p in pts) for i in range(3))
def dat(v, ban):
    if isinstance(v, (tuple, list)):
        v = dict(m=v[0], x=v[1], y=v[2], r=v[3], z=(v[4] if len(v) > 4 else None))
    g = nhap(v['m'])
    if g is None: return
    s = v.get('s', 1); g.scale = (s, s, s); g.rotation_euler[2] = math.radians(v.get('r', 0)); bpy.context.view_layer.update()
    x, y = v['x'], v['y']; z0 = 0
    if v.get('tren') and v['tren'] in ban:
        lo, hi = ban[v['tren']]; x += (lo[0] + hi[0]) / 2; y += (lo[1] + hi[1]) / 2; z0 = hi[2]
    lo, hi = bbox(g); cx, cy = (lo[0] + hi[0]) / 2, (lo[1] + hi[1]) / 2
    g.location = (x - cx, y - cy, 0); bpy.context.view_layer.update()
    lo, hi = bbox(g)
    if v.get('z') is not None:   # z = độ cao mép TRÊN (đèn trần, tranh treo dùng tâm)
        z = v['z']; g.location[2] += (z - hi[2]) if z >= 2.5 else (z - (lo[2] + hi[2]) / 2)
    else: g.location[2] += z0 - lo[2]
    bpy.context.view_layer.update(); ban[v.get('k', v['m'])] = bbox(g)
for c in C:
    if CHI and CHI not in c['ten']: continue
    xoa(); sc = bpy.context.scene
    sc.render.engine = 'CYCLES'; sc.cycles.samples = int(os.environ.get("MAU", "128")); sc.cycles.use_denoising = True
    sc.render.resolution_x, sc.render.resolution_y = 1600, 900; sc.view_settings.view_transform = 'AgX' if 'AgX' in [i.identifier for i in sc.view_settings.bl_rna.properties['view_transform'].enum_items] else 'Filmic'
    wd = bpy.data.worlds.new("w"); sc.world = wd; wd.use_nodes = True; nt = wd.node_tree
    hs = glob.glob(os.path.join(W, "polyhaven/hdris", c['hdri'] + "*.hdr")) + glob.glob(os.path.join(W, "polyhaven/hdris", c['hdri'] + "*.exr"))
    if hs:
        e = nt.nodes.new("ShaderNodeTexEnvironment"); e.image = bpy.data.images.load(hs[0]); nt.links.new(e.outputs["Color"], nt.nodes["Background"].inputs["Color"])
    else: print("LOI thieu hdri", c['hdri'])
    nt.nodes["Background"].inputs["Strength"].default_value = c.get('sang', 1)
    Wd, D, H = c['W'], c['D'], c['H']
    mat_phang("san", (Wd, D), (0, 0, 0), (0, 0, 0), tex_mat(c['san'], max(Wd, D) / 2), 1)
    if c.get('tuong'):
        mt = tex_mat(c['tuong'], max(Wd, H) / 2)
        mat_phang("t_sau", (Wd, H), (0, D / 2, H / 2), (math.pi / 2, 0, 0), mt, 1)
        mat_phang("t_trai", (D, H), (-Wd / 2, 0, H / 2), (math.pi / 2, 0, math.pi / 2), mt, 1)
        mat_phang("t_phai", (D, H), (Wd / 2, 0, H / 2), (math.pi / 2, 0, -math.pi / 2), mt, 1)
        mat_phang("tran", (Wd, D), (0, 0, H), (math.pi, 0, 0), mt, 1)
    for (x, y, z, wt, col) in c.get('den', []):
        l = bpy.data.lights.new("d", 'POINT'); l.energy = wt; l.color = col; l.shadow_soft_size = 0.4
        o = bpy.data.objects.new("d", l); sc.collection.objects.link(o); o.location = (x, y, z)
    ban = {}
    for v in c['vat']:
        try: dat(v, ban)
        except Exception as ex: print("LOI dat", v, ex)
    (cp, tg, fl) = c['cam']; cd = bpy.data.cameras.new("cam"); cd.lens = fl
    co = bpy.data.objects.new("cam", cd); sc.collection.objects.link(co); co.location = cp
    d = mathutils.Vector(tg) - mathutils.Vector(cp); co.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler(); sc.camera = co
    sc.render.filepath = os.path.join(OUT, c['ten'] + ".png"); bpy.ops.render.render(write_still=True); print("anh", c['ten'], flush=True)
print("XONG")
