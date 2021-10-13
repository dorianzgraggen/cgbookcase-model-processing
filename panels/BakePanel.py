import bpy
from ..util import base_mesh_exists 


class PANEL_PARENT(bpy.types.Panel):
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    

class PANEL_BAKE(PANEL_PARENT):
    bl_label = "Baking"
    bl_idname = "LOLLOL"

    def draw(self, context):
        layout = self.layout
        root = '.'.join(__package__.split('.')[:-1])
        addon_prefs = context.preferences.addons[root].preferences
        options = context.scene.bakePropertyGroupInstance
        
        if not addon_prefs.filepath and True:
            col = layout.column(align=True)
            col.label(text="xNormal path is not set")
            col.label(text="(Preferences > Addons > cgbModelProcessing")
        elif not base_mesh_exists():
            row = layout.row()
            row.label(text='Write base mesh first.')
        else:

            # Run          
            row = layout.row()
            props = row.operator("cgb_model.bake", icon="RENDER_STILL", text="Bake  ")

        



class PANEL_BAKE_MAPS(PANEL_PARENT):
    bl_label = "Maps"
    bl_parent_id = "LOLLOL"

    def draw(self, context):
        options = context.scene.bakePropertyGroupInstance
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column()

        maps = ["color", "normal", "ao", "height", "thickness", "cavity", "convexity"]
        for m in maps:
            row = col.row()
            row.prop(options, "map_" + m)



class PANEL_BAKE_QUALITY(PANEL_PARENT):
    bl_label = "Quality"
    bl_parent_id = "LOLLOL"

    def draw(self, context):
        options = context.scene.bakePropertyGroupInstance
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column()

        row = col.row()
        row.prop(options, "antialias")

        col.separator(factor=1)

        row = col.row()
        row.prop(options, "resolution_x")

        row = col.row()
        row.prop(options, "resolution_y")


        col.separator(factor=1)

        row = col.row()
        row.prop(options, "img_format")


