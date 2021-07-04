import bpy


class Test_PT_Panel(bpy.types.Panel):
    bl_idname = "MOCAP_IMPORT_PT_Panel"
    bl_label = "MOCAP PE Import Data"
    bl_category = "MOCAP"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    
    def draw(self, context):
        layout = self.layout

        sk_value_prop = context.scene.sk_value_prop
        # percent_render_var = sk_value_prop.sk_value

        row = layout.row()
        row.label(text='Nvidia Audio2face')
        row = layout.row()
        row.operator('mocap.export_audio2face', text="Export Model")
        row = layout.row()
        row.operator('mocap.import_audio2face_to_nla', text="Import as NLA Strip")
        row = layout.row()
        row.operator('mocap.import_audio2face', text="Import with Modifier")
        row = layout.row()
        row.label(text='----------')
        row = layout.row()
        row.operator('mocap.delete_action_shapekey_nla', text="Delete Action, Shapekey and NLA")
        row = layout.row()
        row.operator('mocap.delete_unused_sk_nla_tracks', text="Delete Unused ShapeKey NLA Tracks")
        row = layout.row()
        row.label(text='----------')
        row = layout.row()
        row.prop(sk_value_prop, "sk_raw_bool", text="Raw Import")
        row = layout.row()
        row.prop(sk_value_prop, "sk_constraint_limit_rotation_bool", text="Constraint Limit Rotation")
        
        row = layout.row()
        row.prop(sk_value_prop, "sk_debug_bool", text="Debug")
       
       
        row = layout.row()
        row.operator('mocap.import_easymocap', text="Import EasyMOCAP")
        row.operator('mocap.import_easymocap_reload', text="Reload Skeleton")
        row = layout.row()
        row.label(text='----------')
        row = layout.row()
        row.operator('mocap.import_smpl_easymocap', text="Import SMPL EasyMOCAP")
        row = layout.row()
        row.prop(sk_value_prop, "sk_smpl_path")
        row = layout.row()
        row.operator('mocap.browse_smpl_file', text="Browse SMPL FBX File")
        row = layout.row()
        row.label(text='----------')


        layout.row().separator()
        
        layout.prop(sk_value_prop, "sk_value", text="SK Mult")
        row = layout.row()
        row.operator('mocap.import_frankmocap', text="SK Import FrankMocap")
        row = layout.row()
        row.operator('mocap.import_frankmocap_alter', text="SK Import FrankMocap Alter")


        layout.row().separator()
        row = layout.row()
        row.operator('mocap.import_vibe', text="SK Import VIBE")
        row = layout.row()
        row.prop(sk_value_prop, "vibe_person_id", text="Vibe Person ID")
        layout.row().separator()

        row = layout.row()
        row.operator('mocap.mediapipe_pose', text="SK Generate Mocap (MediaPipe)")
        layout.row().separator()
        

        # Create two columns, by using a split layout.
        split = layout.split()

        # First column
        col = split.column()
        # col.label(text="Column One:")
        # layout.label(text='Original angles')
        # layout.label(text='x: '+ '%.2f' %sk_value_prop.sk_root_rot_x)
        # layout.label(text='y: '+ '%.2f' %sk_value_prop.sk_root_rot_y)
        # layout.label(text='z: '+ '%.2f' %sk_value_prop.sk_root_rot_z)

        """
        col.label(text='Original angles')
        col.label(text='x: '+ '%.2f' %sk_value_prop.sk_root_rot_x)
        col.label(text='y: '+ '%.2f' %sk_value_prop.sk_root_rot_y)
        col.label(text='z: '+ '%.2f' %sk_value_prop.sk_root_rot_z)

        # Second column, aligned
        col = split.column(align=True)
        col.label(text="Actual Angle:")
        col.label(text='x: '+ '%.2f' %sk_value_prop.sk_root_actual_rot_x)
        col.label(text='y: '+ '%.2f' %sk_value_prop.sk_root_actual_rot_y)
        col.label(text='z: '+ '%.2f' %sk_value_prop.sk_root_actual_rot_z)
        """


        
"""
class Modify_PT_Panel(bpy.types.Panel):
    bl_idname = "MODIFY_PT_Panel"
    bl_label = "Modify Data"
    bl_category = "MOCAP"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    
    def draw(self, context):
        layout = self.layout

        sk_value_prop = context.scene.sk_value_prop
        # percent_render_var = sk_value_prop.sk_value

        layout.label(text=" Convert axis")
        row = layout.row()
        row.prop(sk_value_prop, "sk_from_axis", text="From")
        row.prop(sk_value_prop, "sk_to_axis", text="To")
        row = layout.row()
        row.operator('mocap.convert_axis', text='Convert')
        row = layout.row()
        row.label(text='----------')
        row = layout.row()
        row.operator('mocap.reset_location', text='Reset loc')
        row.operator('mocap.reset_rotation', text='Reset rot')
        row.operator('mocap.foot_high', text='Foot')
        # row = layout.row()
        # row.operator('mocap.smooth_bones', text='Smooth Curves')
        row = layout.row()
        row.label(text='----------')
        row = layout.row()
        row.label(text='Compensate Rotation')
        row = layout.row()
        row.prop(sk_value_prop, "sk_rot_compens_x", text="x")
        row.prop(sk_value_prop, "sk_rot_compens_y", text="y")
        row.prop(sk_value_prop, "sk_rot_compens_z", text="z")
        row = layout.row()
        row.operator('mocap.compensate_rotation', text='Rotate')

"""

class Install_PT_Panel(bpy.types.Panel):
    bl_idname = "INSTALL_PT_Panel"
    bl_label = "Install PyPacks"
    bl_category = "MOCAP"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator('install.mediapipe_package', text="Install python Mediapipe Package")
        row = layout.row()
        row.operator('install.joblib_package', text="Install Joblib (Vibe requirement)")

"""
class Debug_PT_Panel(bpy.types.Panel):
    bl_idname = "Debug_PT_Panel"
    bl_label = "Debug Panel"
    bl_category = "MOCAP"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    
    def draw(self, context):
        layout = self.layout
        sk_value_prop = context.scene.sk_value_prop

        row = layout.row()
        row.label(text='Debug skeleton size')
        row = layout.row()
        row.label(text='Main Structure')
        row = layout.row()
        row.prop(sk_value_prop, "sk_spine_mulitplier", text="Spine: ")
        row.prop(sk_value_prop, "sk_neck_mulitplier", text="Neck")
        row = layout.row()
        row.prop(sk_value_prop, "sk_head_mulitplier", text="Head")

        layout.row().separator()
        row = layout.row()
        
        row.label(text='Arms')
        row = layout.row()
        row.prop(sk_value_prop, "sk_forearm_mulitplier", text="Forearm: ")
        row.prop(sk_value_prop, "sk_arm_mulitplier", text="Arm: ")

        layout.row().separator()
        row = layout.row()
        row.label(text='Legs')
        row = layout.row()
        row.prop(sk_value_prop, "sk_tigh_mulitplier", text="Tigh: ")
        row.prop(sk_value_prop, "sk_leg_mulitplier", text="Leg: ")
        row = layout.row()
        row.prop(sk_value_prop, "sk_foot_mulitplier", text="Foot: ")
"""

from bpy.props import (StringProperty,
                       BoolProperty,
                      IntProperty,
                      FloatProperty,
#                       FloatVectorProperty,
                      EnumProperty,
                    #    PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )


class MySettings(PropertyGroup):
    sk_value: FloatProperty(name="multiplier", description="Multiplier for base proportion of the bones", default=0.9)
    sk_rot_compens_x: IntProperty(name="Rotation_compensate_x", description="Value to compensate Roation X", default=0)
    sk_rot_compens_y: IntProperty(name="Rotation_compensate_y", description="Value to compensate Roation Y", default=0)
    sk_rot_compens_z: IntProperty(name="Rotation_compensate_z", description="Value to compensate Roation Z", default=0)
    
    sk_rot_original: StringProperty(name="rotation", description="rotation")
    
    sk_root_rot_x: FloatProperty(name="original rotation x", description="original rotation of root bone x")
    sk_root_rot_y: FloatProperty(name="original rotation y", description="original rotation of root bone y")
    sk_root_rot_z: FloatProperty(name="original rotation z", description="original rotation of root bone z")

    sk_root_actual_rot_x: FloatProperty(name="Actual rotation x", description="Actual rotation of root bone x")
    sk_root_actual_rot_y: FloatProperty(name="Actual rotation y", description="Actual rotation of root bone y")
    sk_root_actual_rot_z: FloatProperty(name="Actual rotation z", description="Actual rotation of root bone z")

    sk_raw_bool: BoolProperty(name='raw_bool', default=True)
    sk_debug_bool: BoolProperty(name='debug_bool', default=False)
    # sk_reload_skeleton_bool: BoolProperty(name='Reload_skeleton_bool', default=False)
    sk_constraint_limit_rotation_bool: BoolProperty(name='Limit_rotation_bool', default=True)

    vibe_person_id: IntProperty(name="Vibe Person ID", description="Person to import pose estimation", default=1)
    ############
    sk_spine_mulitplier: FloatProperty(name="Spine size multiplier", description="Ajust the Spine size", default=1)
    sk_neck_mulitplier: FloatProperty(name="Neck size multiplier", description="Ajust the Neck size", default=1)
    sk_head_mulitplier: FloatProperty(name="Head size multiplier", description="Ajust the Head size", default=1)

    sk_forearm_mulitplier: FloatProperty(name="Forearm size multiplier", description="Ajust the Forearm size", default=1)
    sk_arm_mulitplier: FloatProperty(name="Arm size multiplier", description="Ajust the Arm size", default=1)

    sk_tigh_mulitplier: FloatProperty(name="Thigh size multiplier", description="Ajust the Thigh size", default=1)
    sk_leg_mulitplier: FloatProperty(name="Leg size multiplier", description="Ajust the Leg size", default=1)
    sk_foot_mulitplier: FloatProperty(name="Foot size multiplier", description="Ajust the Foot size", default=1)

    sk_smpl_path: StringProperty(name="Path to SMPL FBX file", description="Path to SMPL FBX file")

    sk_from_axis: EnumProperty(
        name= "From Axis",
        description="From specific axis of animation",
        items= [('from_x', "x","Choose origin x axis"),
                ('from_y', "y","Choose origin y axis"),
                ('from_z', "z","Choose origin z axis")
        ], 
        default = 'from_y'
    )
    sk_to_axis: EnumProperty(
        name= "To Axis",
        description="To specific axis of animation",
        items= [('to_x', "x","Choose destination x axis"),
                ('to_y', "y","Choose destination y axis"),
                ('to_z', "z","Choose destination z axis")
        ],
        default = 'to_z'
    )

