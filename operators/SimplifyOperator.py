from genericpath import getmtime
import bpy, pymeshlab, os, math
from .. import util;

class OP_SIMPLIFY(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "cgb_model.simplify"
    bl_label = "Simplify"

    target_face_number: bpy.props.IntProperty(
        name="Target Face Number",
        default = 5000
    )

    def execute(self, context):
        options = context.scene.simplifyPropertyGroupInstance

        ms = pymeshlab.MeshSet()

        ms.load_new_mesh(util.get_mesh_path())


        if options.use_detail_mask:
            # TODO: save mesh

            print("loading detail...")
            ms.load_new_mesh(util.file_to_abs_path("detail_mask.obj"))
            ms.set_current_mesh(0)

            print("calculating weights...")
            ms.distance_from_reference_mesh(measuremesh=0, refmesh=1)
            ms.per_vertex_quality_function(q="min(max(0, q) * (1 / " + str(0.2) + "), 1)")


        print("simplifying...")
        ms.simplification_quadric_edge_collapse_decimation(
            targetfacenum = self.target_face_number,
            qualityweight = options.use_detail_mask
        )

        # for some reason my PC crashes when saving as obj
        print("saving...")
        ms.save_current_mesh(util.get_simplified_mesh_data())
        

        print("importing...")
        bpy.ops.import_mesh.ply(filepath=util.get_simplified_mesh_data())
        bpy.ops.object.shade_smooth()
        context.active_object.name = "Simplified"
        context.active_object.rotation_euler[0] = math.pi / 2
        # context.active_object.transform_apply(location=True, rotation=True, scale=True)

        print("done")

        return {'FINISHED'}
