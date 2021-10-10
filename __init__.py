# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "cgbookcase Model Processing",
    "author" : "Dorian Zgraggen",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
import pymeshlab


# =================================================================
# PROPERTY GROUPS

class SimplifyPropertyGroup(bpy.types.PropertyGroup):
    target_face_number: bpy.props.IntProperty( 
        name="Target Face Number",
        description="",
        default=5000,
        min=1,
    )

class LODPropertyGroup(bpy.types.PropertyGroup):
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
        name="Lowest Face Number",
        description="",
        default=50,
        min=1,
    )
    

# =================================================================
# OPERATORS

class OP_EXPORT_MESH(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "cgb_model.export"
    bl_label = "Export Mesh"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.export_scene.obj(
            filepath = "X:/cgbookcase/models/wip/Fruits_01/RedApple01/02_blender/cgbookcase Mesh Processing/original.obj",
            use_selection = True
        )

        return {'FINISHED'}


class OP_SIMPLIFY(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "cgb_model.simplify"
    bl_label = "Simplify"

    target_face_number: bpy.props.IntProperty(
        name="Target Face Number",
        default = 5000
    )

    def execute(self, context):
        print(self.target_face_number)

        # ms = pymeshlab.MeshSet()
        # ms.load_new_mesh('"X:/cgbookcase/models/wip/Fruits_01/RedApple01/02_blender/cgbookcase Mesh Processing/original.obj"')

        # ms.simplification_quadric_edge_collapse_decimation(targetfacenum = self.target_face_number)

        # ms.save_current_mesh('simplified.obj')

        return {'FINISHED'}


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


# =================================================================
# Panels

class PANEL_PREPARE(bpy.types.Panel):
    bl_label = "Prepare"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()

        if len(context.selected_objects) > 0:
            props = row.operator("cgb_model.export", icon="EXPORT")
        else:
            row.label(text='No active selection')



class PANEL_SIMPLIFY(bpy.types.Panel):
    bl_label = "Simplify"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        options = context.scene.simplifyPropertyGroupInstance
        
        col = layout.column()

        row = col.row()
        row.prop(options, "target_face_number")

        row = col.row()
        props = row.operator("cgb_model.simplify", icon="MOD_SIMPLIFY")
        props.target_face_number = options.target_face_number



class PANEL_LOD(bpy.types.Panel):
    bl_label = "LODs"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        options = context.scene.lodPropertyGroupInstance
        
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
        props.ratio = options.target_face_number
        props.min_face_number = options.target_face_number



class PANEL_BAKE(bpy.types.Panel):
    bl_label = "Bake"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):  
        layout = self.layout
        
        row = layout.row()

        row.operator("cgb_model.simplify", icon="RENDER_STILL")


class PANEL_EXPORT(bpy.types.Panel):
    bl_label = "Export"
    bl_category = "cgbookcase Mesh Processing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()

        row.operator("cgb_model.simplify", icon="MOD_SIMPLIFY")


# =================================================================

classes = (OP_EXPORT_MESH, PANEL_PREPARE, OP_SIMPLIFY, PANEL_SIMPLIFY, OP_LOD, PANEL_LOD, PANEL_BAKE, PANEL_EXPORT, SimplifyPropertyGroup, LODPropertyGroup)

def register():
    for c in classes:
        print(c)
        bpy.utils.register_class(c)

    bpy.types.Scene.simplifyPropertyGroupInstance = bpy.props.PointerProperty(type=SimplifyPropertyGroup)
    bpy.types.Scene.lodPropertyGroupInstance = bpy.props.PointerProperty(type=LODPropertyGroup)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    
    del bpy.types.Scene.simplifyPropertyGroupInstance
    del bpy.types.Scene.lodPropertyGroupInstance
        
if __name__ == "__main__":
    register()