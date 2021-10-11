import bpy

class OP_SIMPLIFY(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "cgb_model.simplify"
    bl_label = "Simplify"

    target_face_number: bpy.props.IntProperty(
        name="Target Face Number",
        default = 5000
    )

    def execute(self, context):
        print(self.target_face_number)

        # ms = pymeshlab.MeshSet()
        # ms.load_new_mesh('"X:/cgbookcase/models/wip/Fruits_01/RedApple01/02_blender/cgbookcase Mesh Processing/original.obj"')

        # ms.simplification_quadric_edge_collapse_decimation(targetfacenum = self.target_face_number)

        # ms.save_current_mesh('simplified.obj')

        return {'FINISHED'}
