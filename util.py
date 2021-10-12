import bpy, os, pathlib

def base_mesh_exists():
    path = bpy.path.abspath("//_cgbMeshProcessing/original.obj")
    return os.path.isfile(path)

def get_mesh_path():
    return bpy.path.abspath("//_cgbMeshProcessing/original.obj")

def get_written_lod_path():
    return bpy.path.abspath("//_cgbMeshProcessing/lod0.obj")
    
def get_mesh_folder():
    return bpy.path.abspath("//_cgbMeshProcessing/")

def file_to_abs_path(file_name):
    return bpy.path.abspath("//_cgbMeshProcessing/" + file_name)
    
def get_simplified_mesh_data():
    return os.path.join(bpy.path.abspath("//_cgbMeshProcessing/"), "temp.ply")

def get_addon_prefs():
    return bpy.context.preferences.addons[__package__].preferences

def get_addon_path():
    return pathlib.Path(__file__).parent.resolve()

def get_xnormal_config():
    return os.path.join(pathlib.Path(__file__).parent.resolve(), "xnormal.xml")

def addon_file_to_abs_path(filename):
    return os.path.join(pathlib.Path(__file__).parent.resolve(), filename)
