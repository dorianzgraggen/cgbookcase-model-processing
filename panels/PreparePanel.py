import bpy

class PANEL_PREPARE(bpy.types.Panel):
    bl_label = "Base Mesh"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        
        col = layout.column(align=True)
        row = col.row()

        if len(context.selected_objects) > 0:
            props = row.operator("cgb_model.write_base_mesh", icon="GREASEPENCIL", text="Write Source Mesh")
            props.file_name = "source"

            row = col.row()
            props = row.operator("cgb_model.write_base_mesh", icon="GREASEPENCIL", text="Write Detail Mask Mesh")
            props.file_name = "detail_mask"

            row = col.row()
            props = row.operator("cgb_model.write_base_mesh", icon="GREASEPENCIL", text="Write LOD0 Mesh")
            props.file_name = "lod0"
        else:
            row.label(text='Select an object to write base mesh.')
