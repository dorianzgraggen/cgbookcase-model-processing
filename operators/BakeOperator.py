from genericpath import getmtime
import bpy, os, math
from .. import util;

class OP_BAKE(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "cgb_model.bake"
    bl_label = "Bake"

    def execute(self, context):

        options = context.scene.bakePropertyGroupInstance

        # save selected as obj
        bpy.ops.export_scene.obj(
            filepath = bpy.path.abspath("//_cgbMeshProcessing/" + "bake_target" + ".obj"),
            use_selection = True
        )

        print("exported")

        replace(options)

        print("baking")
        o = os.system(util.get_addon_prefs().filepath + " " + util.get_xnormal_config())
        print("finished baking")
        print(o)


        return {'FINISHED'}


def replace(options):
    fin = open(util.addon_file_to_abs_path("xnormal.xml"), "rt")
    fout = open(util.addon_file_to_abs_path("xnormal_temp.xml"), "wt")

    for line in fin:
        line = line.replace("__TARGET_MESH_PATH", "X:\\cgbookcase\\models\\addon\\blend-test\\_cgbMeshProcessing\\bake_target.obj")
        line = line.replace("__WIDTH", options.resolution_x)
        line = line.replace("__HEIGHT", options.resolution_y)
        line = line.replace("__ANTIALIAS", options.antialias)
        line = line.replace("__EDGE_PADDING", "16")
        line = line.replace("__MAP_FILE", "X:\\cgbookcase\\models\\addon\\blend-test\\_cgbMeshProcessing\\maps\\bake__.tif")
        line = line.replace("__SOURCE_MESH_PATH", "X:\\cgbookcase\\models\\addon\\blend-test\\_cgbMeshProcessing\\original.obj")
        line = line.replace("__BASE_TEXTURE_PATH", "X:\\cgbookcase\\models\\addon\\blend-test\\_cgbMeshProcessing\\original_color.png")

        line = line.replace("__GEN_THICKNESS", bool_to_string(options.map_thickness))
        line = line.replace("__GEN_CAVITY", bool_to_string(options.map_cavity))
        line = line.replace("__GEN_NORMALS", bool_to_string(options.map_normal))
        line = line.replace("__GEN_AO", bool_to_string(options.map_ao))
        line = line.replace("__GEN_HEIGHT", bool_to_string(options.map_height))
        line = line.replace("__GEN_CONVEXITY", bool_to_string(options.map_convexity))
        line = line.replace("__GEN_BASECOLOR", bool_to_string(options.map_color))

        fout.write(line)

    fin.close()
    fout.close()
    
def bool_to_string(b):
    return str(b).lower()