import bpy


class Test_PT_Panel(bpy.types.Panel):
    bl_idname = "MOCAP_IMPORT_PT_Panel"
    bl_label = "MOCAP PE Import Data"
    bl_category = "MOCAP"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    global percent_render_var
    def draw(self, context):
        layout = self.layout

        global percent_render_var
        percentage = context.scene.percentage
        percent_render_var = percentage.percentage

        row = layout.row()
        row.operator('mocap.import_easymocap', text="Import EasyMOCAP")

        layout.row().separator()
        
        layout.prop(percentage, "percentage", text="SK Multiplier")
        row = layout.row()
        row.operator('mocap.import_frankmocap', text="SK Import FrankMocap")
        row = layout.row()
        row.operator('mocap.import_vibe', text="SK Import VIBE")
   
        row = layout.row()
        row.operator('mocap.mediapipe_pose', text="SK Generate Mocap (MediaPipe)")
        layout.row().separator()

        layout.row().separator()

        row = layout.row()
        row.operator('install.mediapipe_package', text="Install python Mediapipe Package")
        row = layout.row()
        row.operator('install.joblib_package', text="Install Joblib (Vibe requirement)")


from bpy.props import (#StringProperty,
                       BoolProperty,
                      IntProperty,
                      FloatProperty,
#                       FloatVectorProperty,
#                       EnumProperty,
                    #    PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )



class MySettingsPerc(PropertyGroup):
    percentage: FloatProperty(name="miltiplier", description="Multiplier", default=0.9)
