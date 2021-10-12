import bpy

class ExampleAddonPreferences(bpy.types.AddonPreferences):
    # this must match the add-on name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __package__

    filepath: bpy.props.StringProperty(
        name="xNormal executable",
        subtype='FILE_PATH',
    )
    def draw(self, context):
        layout = self.layout
        layout.label(text="This is a preferences view for our add-on")
        layout.prop(self, "filepath")