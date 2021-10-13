import bpy
from ..util import base_mesh_exists, lod_mesh_exists 

class PANEL_LOD(bpy.types.Panel):
    bl_label = "Levels of Detail"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        options = context.scene.lodPropertyGroupInstance
        
        col = layout.column(align=True)


        row = col.row()
        row.prop(options, "use_base_as_lod_0")

        if not options.use_base_as_lod_0:
            row = col.row()
            row.prop(options, "target_face_number")

        row = col.row()
        row.prop(options, "ratio")

        row = col.row()
        row.prop(options, "min_face_number")


        col = layout.column(align=True)

        row = col.row()

        if (options.use_base_as_lod_0 and lod_mesh_exists()) or (not options.use_base_as_lod_0 and base_mesh_exists()):
            props = row.operator("cgb_model.create_lods", icon="FORCE_LENNARDJONES")
            props.target_face_number = options.target_face_number
            props.ratio = options.ratio
            props.min_face_number = options.min_face_number
            props.use_base_as_lod_0 = options.use_base_as_lod_0
            
        elif options.use_base_as_lod_0:
            row = layout.row()
            row.label(text='Write LOD mesh first.')
        else:
            row = layout.row()
            row.label(text='Write base mesh first.')
