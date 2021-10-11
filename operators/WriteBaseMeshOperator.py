import bpy
from pathlib import Path


class OP_WRITE_BASE_MESH(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "cgb_model.write_base_mesh"
    bl_label = "Write Base Mesh"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        Path(bpy.path.abspath("//_cgbMeshProcessing/")).mkdir(parents=True, exist_ok=True)
        bpy.ops.export_scene.obj(
            filepath = bpy.path.abspath("//_cgbMeshProcessing/original.obj"),
            use_selection = True
        )

        return {'FINISHED'}