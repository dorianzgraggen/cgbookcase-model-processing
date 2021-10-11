import bpy
from ..util import base_mesh_exists 

class PANEL_EXPORT(bpy.types.Panel):
    bl_label = "Export"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        
        if base_mesh_exists():
            column = layout.column(align=True)

            row = column.row()
            row.operator("cgb_model.simplify", icon="EXPORT", text="Export FBX")

            row = column.row()
            row.operator("cgb_model.simplify", icon="EXPORT", text="Export GLTF")

            row = column.row()
            row.operator("cgb_model.simplify", icon="EXPORT", text="Export .blend")

            row = layout.row()
            row.operator("cgb_model.simplify", icon="EXPORT", text="Export all")
        else:
            row = layout.row()
            row.label(text='Write base mesh first.')
