from genericpath import getmtime
import bpy, os, math
from .. import util;

class OP_BAKE(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "cgb_model.bake"
    bl_label = "Bake"

    def execute(self, context):

        # save selected as obj
        # bpy.ops.export_scene.obj(
        #     filepath = bpy.path.abspath("//_cgbMeshProcessing/" + "bake_target" + ".obj"),
        #     use_selection = True
        # )

        replace()

        # os.system(util.get_addon_prefs().filepath + " " + util.get_xnormal_config())


        return {'FINISHED'}


def replace():
    fin = open(util.addon_file_to_abs_path("xnormal.xml"), "rt")
    fout = open(util.addon_file_to_abs_path("xnormal_temp.xml"), "wt")

    for line in fin:
        line = line.replace("__TARGET_MESH_PATH", "X:\\cgbookcase\\models\\addon\\blend-test\\_cgbMeshProcessing\\target.obj")
        line = line.replace("__WIDTH", "2048")
        line = line.replace("__HEIGHT", "2048")
        line = line.replace("__ANTIALIAS", "1")
        line = line.replace("__EDGE_PADDING", "16")
        line = line.replace("__MAP_FILE", "X:\\cgbookcase\\models\\addon\\blend-test\\_cgbMeshProcessing\\maps\\bake_.tif")
        line = line.replace("__SOURCE_MESH_PATH", "X:\\cgbookcase\\models\\addon\\blend-test\\_cgbMeshProcessing\\original.obj")
        line = line.replace("__BASE_TEXTURE_PATH", "X:\\cgbookcase\\models\\addon\\blend-test\\_cgbMeshProcessing\\original_color.png")
        fout.write(line)

    fin.close()
    fout.close()
    