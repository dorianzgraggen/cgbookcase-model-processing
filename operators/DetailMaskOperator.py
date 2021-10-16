from genericpath import getmtime
import bpy, pymeshlab, os, math
from .. import util;

class OP_DETAIL_MASK(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "cgb_model.detail_mask"
    bl_label = "Simplify"

    target_face_number: bpy.props.IntProperty(
        name="Target Face Number",
        default = 5000
    )

    def execute(self, context):

        ms = pymeshlab.MeshSet()

        ms.load_new_mesh(util.file_to_abs_path("source.obj"))
        ms.load_new_mesh(util.file_to_abs_path("detail_mask.obj"))

        ms.set_current_mesh(0)

        ms.distance_from_reference_mesh(measuremesh=0, refmesh=1)
        ms.per_vertex_quality_function(q="min(max(0, q) * (1 / " + str(0.2) + "), 1)")

        ms.simplification_quadric_edge_collapse_decimation(targetfacenum = 1000, qualityweight = True)

        ms.save_current_mesh(util.file_to_abs_path("red.ply"))

        print("importing...")
        bpy.ops.import_mesh.ply(filepath=util.file_to_abs_path("red.ply"))
        context.active_object.name = "okok"

        print("done")

        return {'FINISHED'}
