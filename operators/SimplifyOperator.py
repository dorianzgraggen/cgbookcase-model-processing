from genericpath import getmtime
import bpy, pymeshlab, os
from .. import util;

class OP_SIMPLIFY(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "cgb_model.simplify"
    bl_label = "Simplify"

    target_face_number: bpy.props.IntProperty(
        name="Target Face Number",
        default = 5000
    )

    def execute(self, context):

        ms = pymeshlab.MeshSet()

        ms.load_new_mesh(util.get_mesh_path())

        print("simplifying...")
        ms.simplification_quadric_edge_collapse_decimation(targetfacenum = self.target_face_number)

        # for some reason my PC crashes when saving as obj
        print("saving...")
        ms.save_current_mesh(util.get_simplified_mesh_data())
        

        print("importing...")
        bpy.ops.import_mesh.ply(filepath=util.get_simplified_mesh_data())
        bpy.ops.object.shade_smooth()
        context.active_object.name = "Simplified"

        print("done")

        return {'FINISHED'}
