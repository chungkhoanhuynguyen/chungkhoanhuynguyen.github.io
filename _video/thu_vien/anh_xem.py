# Chạy trong Blender (blender -b -P anh_xem.py -- <thu_muc_goc> <thu_muc_anh>): ảnh xem trước từng mô hình + đếm tam giác, kích thước.
import bpy, sys, os, json, math, mathutils
a = sys.argv[sys.argv.index("--") + 1:]; GOC, ANH = a[0], a[1]; os.makedirs(ANH, exist_ok=True)
sc = bpy.context.scene; sc.render.engine = "BLENDER_WORKBENCH"; sc.display.shading.light = "STUDIO"; sc.display.shading.color_type = "TEXTURE"
sc.display.shading.show_shadows = True; sc.display.shading.show_cavity = True; sc.render.resolution_x = sc.render.resolution_y = 320
sc.render.film_transparent = False; sc.display.shading.background_type = "VIEWPORT"
try: sc.display.shading.background_color = (0.16, 0.08, 0.34)
except Exception: pass
sc.render.image_settings.file_format = "JPEG"; sc.render.image_settings.quality = 80
tep = []
for r, _, fs in os.walk(GOC):
    for f in fs:
        if f.lower().endswith((".glb", ".gltf")): tep.append(os.path.join(r, f))
tep.sort(); cat = []
for i, p in enumerate(tep):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene; sc.render.engine = "BLENDER_WORKBENCH"; sc.display.shading.light = "STUDIO"; sc.display.shading.color_type = "TEXTURE"
    sc.display.shading.show_shadows = True; sc.render.resolution_x = sc.render.resolution_y = 320; sc.render.image_settings.file_format = "JPEG"
    try:
        bpy.ops.import_scene.gltf(filepath=p)
        ms = [o for o in sc.objects if o.type == "MESH"]
        if not ms: continue
        pts = [o.matrix_world @ mathutils.Vector(c) for o in ms for c in o.bound_box]
        mn = mathutils.Vector((min(v.x for v in pts), min(v.y for v in pts), min(v.z for v in pts))); mx = mathutils.Vector((max(v.x for v in pts), max(v.y for v in pts), max(v.z for v in pts)))
        c = (mn + mx) / 2; kt = mx - mn; r0 = max(kt.length / 2, 1e-3)
        cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam); sc.camera = cam; cam.data.lens = 50
        d = r0 / math.tan(cam.data.angle / 2) * 1.15; v = mathutils.Vector((0.9, -1.4, 0.75)).normalized()
        cam.location = c + v * d; cam.rotation_euler = (c - cam.location).to_track_quat("-Z", "Y").to_euler()
        rel = os.path.relpath(p, GOC); ten = rel.replace(os.sep, "__").rsplit(".", 1)[0]
        sc.render.filepath = os.path.join(ANH, ten + ".jpg"); bpy.ops.render.render(write_still=True)
        tri = sum(sum(len(pg.vertices) - 2 for pg in o.data.polygons) for o in ms)
        cat.append(dict(tep=rel, anh=ten + ".jpg", tam_giac=tri, kich_thuoc_m=[round(kt.x, 2), round(kt.y, 2), round(kt.z, 2)], hoat_hinh=len(bpy.data.actions)))
    except Exception as e: print("LOI", p, e)
    if i % 50 == 0: print("anh", i, "/", len(tep), flush=True)
json.dump(cat, open(os.path.join(ANH, "_catalog.json"), "w"), ensure_ascii=False, indent=1); print("XONG", len(cat))
