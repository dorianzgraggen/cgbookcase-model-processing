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
import os.path

# Operators
from .operators.WriteBaseMeshOperator import OP_WRITE_BASE_MESH
from .operators.SimplifyOperator import OP_SIMPLIFY
from .operators.LodOperator import OP_LOD

# =================================================================
# FUNCTIONS

def base_mesh_exists():
    path = bpy.path.abspath("//_cgbMeshProcessing/original.obj")
    return os.path.isfile(path)


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
# Panels

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

            row = col.row()
            props = row.operator("cgb_model.simplify", icon="MOD_SIMPLIFY")
            props.target_face_number = options.target_face_number
        else:
            row = layout.row()
            row.label(text='Write base mesh first.')



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
            props.ratio = options.target_face_number
            props.min_face_number = options.target_face_number
        else:
            row = layout.row()
            row.label(text='Write base mesh first.')



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


# =================================================================

classes = (OP_WRITE_BASE_MESH, PANEL_PREPARE, OP_SIMPLIFY, PANEL_SIMPLIFY, OP_LOD, PANEL_LOD, PANEL_BAKE, PANEL_EXPORT, SimplifyPropertyGroup, LODPropertyGroup)

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