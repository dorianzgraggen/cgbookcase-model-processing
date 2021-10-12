import bpy
from ..util import base_mesh_exists 

class PANEL_BAKE(bpy.types.Panel):
    bl_label = "Baking"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        root = '.'.join(__package__.split('.')[:-1])
        addon_prefs = context.preferences.addons[root].preferences
        options = context.scene.bakePropertyGroupInstance
        
        if not addon_prefs.filepath and False:
            col = layout.column(align=True)
            col.label(text="xNormal path is not set")
            col.label(text="(Preferences > Addons > cgbModelProcessing")
        elif not base_mesh_exists():
            row = layout.row()
            row.label(text='Write base mesh first.')
        else:

            # Resolution
            col = layout.column()

            row = col.row()
            row.label(text="Resolution")

            row = col.row()
            row.prop(options, "resolution_x")

            row = col.row()
            row.prop(options, "resolution_y")

            col = layout.column()


            # Maps
            row = col.row()
            row.label(text="Maps")
            maps = ["color", "normal", "ao", "height", "thickness", "cavity", "convexity"]

            for m in maps:
                row = col.row()
                row.prop(options, "map_" + m)

            # Run          
            row = layout.row()
            props = row.operator("cgb_model.bake", icon="RENDER_STILL", text="Bake  ")

