import bpy
from ..util import base_mesh_exists 

class PANEL_LOD(bpy.types.Panel):
    bl_label = "Levels of Detail"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        options = context.scene.lodPropertyGroupInstance
        
        if base_mesh_exists():
            col = layout.column(align=True)

            row = col.row()
            row.prop(options, "target_face_number")

            row = col.row()
            row.prop(options, "ratio")

            row = col.row()
            row.prop(options, "min_face_number")

            col = layout.column(align=True)

            row = col.row()
            props = row.operator("cgb_model.create_lods", icon="FORCE_LENNARDJONES")
            props.target_face_number = options.target_face_number
            props.ratio = options.ratio
            props.min_face_number = options.min_face_number
        else:
            row = layout.row()
            row.label(text='Write base mesh first.')