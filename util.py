import bpy, os

def base_mesh_exists():
    path = bpy.path.abspath("//_cgbMeshProcessing/original.obj")
    return os.path.isfile(path)