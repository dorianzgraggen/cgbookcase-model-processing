import bpy
from ..util import base_mesh_exists 

class PANEL_BAKE(bpy.types.Panel):
    bl_label = "Baking"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):  
        layout = self.layout
        
        if base_mesh_exists():
            row = layout.row()
            row.operator("cgb_model.simplify", icon="RENDER_STILL", text="Bake  ")
        else:
            row = layout.row()
            row.label(text='Write base mesh first.')

