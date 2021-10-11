import bpy

class OP_LOD(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "cgb_model.create_lods"
    bl_label = "Create LODs"

    target_face_number: bpy.props.IntProperty( 
        name="Target Face Number",
        description="",
        default=5000,
        min=1,
    )
    ratio: bpy.props.FloatProperty( 
        name="Ratio per step",
        description="",
        default=0.5,
        min=0,
        max=1,
    )
    min_face_number: bpy.props.IntProperty( 
        name="Target Face Number",
        description="",
        default=5000,
        min=1,
    )

    def execute(self, context):
        print(self.target_face_number)
        print(self.ratio)
        print(self.min_face_number)

        return {'FINISHED'}
