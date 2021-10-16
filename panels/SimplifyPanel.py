import bpy
from ..util import base_mesh_exists 

class PANEL_SIMPLIFY(bpy.types.Panel):
    bl_label = "Simplification"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        if base_mesh_exists():
            options = context.scene.simplifyPropertyGroupInstance
            
            col = layout.column()

            row = col.row()
            row.prop(options, "target_face_number")

            col.separator(factor=.1)

            col = layout.column()

            row = col.row()
            row.prop(options, "use_detail_mask")

            if options.use_detail_mask:
                row = col.row()
                row.prop(context.scene, "cgb_detail_mask")

                row = col.row()
                row.prop(options, "detail_mask_influence")

                row = col.row()
                row.prop(options, "border_smoothness")



            col.separator(factor=.1)
            
            col = layout.column()

            row = col.row()
            props = row.operator("cgb_model.simplify", icon="MOD_SIMPLIFY")
            props.target_face_number = options.target_face_number
        else:
            row = layout.row()
            row.label(text='Write base mesh first.')