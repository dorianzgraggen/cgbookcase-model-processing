import bpy, os

def base_mesh_exists():
    path = bpy.path.abspath("//_cgbMeshProcessing/original.obj")
    return os.path.isfile(path)

def get_mesh_path():
    return bpy.path.abspath("//_cgbMeshProcessing/original.obj")

    
def get_mesh_folder():
    return bpy.path.abspath("//_cgbMeshProcessing/")

def get_simplified_mesh_data():
    return os.path.join(bpy.path.abspath("//_cgbMeshProcessing/"), "temp.ply")