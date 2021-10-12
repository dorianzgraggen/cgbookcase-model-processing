import bpy, pymeshlab, os, math
from .. import util

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
    use_base_as_lod_0: bpy.props.BoolProperty(
        name="Use Base Mesh as LOD 0",
        description="",
        default=True
    )

    def execute(self, context):
        print(self.target_face_number)
        print(self.ratio)
        print(self.min_face_number)

            
        num_of_faces = self.target_face_number
        i = 0
        if (self.use_base_as_lod_0):
            i = 1
        
        while self.min_face_number < num_of_faces:
            
            ms = pymeshlab.MeshSet()

            if i == 0 or (i == 1 and self.use_base_as_lod_0):
                path = util.get_mesh_path()
            else:
                path = os.path.join(util.get_mesh_folder(), "lod_"  + str(i - 1) + ".ply")

            print("loading '" + path + "'")
            ms.load_new_mesh(path)

            if (self.use_base_as_lod_0):
                num_of_faces = int(ms.current_mesh().face_number() * self.ratio)

            print("simplifying...")
            ms.simplification_quadric_edge_collapse_decimation(targetfacenum = num_of_faces)

            # for some reason my PC crashes when saving as obj
            print("saving...")
            save_path = os.path.join(util.get_mesh_folder(), "lod_" + str(i) + ".ply")
            ms.save_current_mesh(save_path)
            

            print("importing...")
            bpy.ops.import_mesh.ply(filepath=save_path)
            bpy.ops.object.shade_smooth()
            context.active_object.name = "LOD_" + str(i)
            context.active_object.rotation_euler[0] = math.pi / 2
            # context.active_object.transform_apply(location=True, rotation=True, scale=True)

            i += 1
            num_of_faces = int(num_of_faces * self.ratio)

        print("created all LODs")

        return {'FINISHED'}
