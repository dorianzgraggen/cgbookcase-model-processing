from genericpath import getmtime
import bpy, os, math
from .. import util;

class OP_SIMPLIFY(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "cgb_model.bake"
    bl_label = "Simplify"

    target_face_number: bpy.props.IntProperty(
        name="Target Face Number",
        default = 5000
    )

    def execute(self, context):

        return {'FINISHED'}
