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
from .operators.BakeOperator import OP_BAKE

# Panels
from .panels.BakePanel import PANEL_BAKE
from .panels.ExportPanel import PANEL_EXPORT
from .panels.LodPanel import PANEL_LOD
from .panels.PreparePanel import PANEL_PREPARE
from .panels.SimplifyPanel import PANEL_SIMPLIFY

from .preferences import ExampleAddonPreferences

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
    use_base_as_lod_0: bpy.props.BoolProperty(
        name="Use Base Mesh as LOD 0",
        description="",
        default=True
    )

class BakePropertyGroup(bpy.types.PropertyGroup):
    map_normal: bpy.props.BoolProperty( 
        name="Normal (OpenGL)",
        description="",
        default=True,
    )
    map_color: bpy.props.BoolProperty( 
        name="Base Color",
        description="",
        default=True,
    )
    

# =================================================================

classes = (OP_WRITE_BASE_MESH, PANEL_PREPARE, OP_SIMPLIFY, PANEL_SIMPLIFY, OP_LOD, PANEL_LOD, PANEL_BAKE, PANEL_EXPORT, OP_BAKE, SimplifyPropertyGroup, LODPropertyGroup, BakePropertyGroup, ExampleAddonPreferences)

def register():
    for c in classes:
        print(c)
        bpy.utils.register_class(c)

    bpy.types.Scene.simplifyPropertyGroupInstance = bpy.props.PointerProperty(type=SimplifyPropertyGroup)
    bpy.types.Scene.lodPropertyGroupInstance = bpy.props.PointerProperty(type=LODPropertyGroup)
    bpy.types.Scene.bakePropertyGroupInstance = bpy.props.PointerProperty(type=BakePropertyGroup)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    
    del bpy.types.Scene.simplifyPropertyGroupInstance
    del bpy.types.Scene.lodPropertyGroupInstance
    del bpy.types.Scene.bakePropertyGroupInstance
        
if __name__ == "__main__":
    register()