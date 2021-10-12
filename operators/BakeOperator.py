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

        os.system(util.get_addon_prefs().filepath + " " + util.get_xnormal_config())


        return {'FINISHED'}
