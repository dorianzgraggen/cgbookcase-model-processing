import bpy

class PANEL_PREPARE(bpy.types.Panel):
    bl_label = "Base Mesh"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()

        if len(context.selected_objects) > 0:
            props = row.operator("cgb_model.write_base_mesh", icon="GREASEPENCIL")
        else:
            row.label(text='Select an object to write base mesh.')
