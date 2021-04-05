import bpy


class Test_PT_Panel(bpy.types.Panel):
    bl_idname = "MOCAP_IMPORT_PT_Panel"
    bl_label = "MOCAP PE Import Data"
    bl_category = "MOCAP"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('mocap.import_easymocap', text="Import EasyMOCAP")
        row = layout.row()
        row.operator('mocap.import_frankmocap', text="Import FrankMocap")
        row = layout.row()
        row.operator('mocap.import_vibe', text="Import VIBE")
        layout.row().separator()

        row = layout.row()
        row.operator('mocap.mediapipe_pose', text="Generate Mocap (MediaPipe)")
        layout.row().separator()

        row = layout.row()
        row.operator('install.mediapipe_package', text="Install python Mediapipe Package")
        row = layout.row()
        row.operator('install.joblib_package', text="Install Joblib (Vibe requirement)")

        

