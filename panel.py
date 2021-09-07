import bpy
from . import VERSION


class Test_PT_Panel(bpy.types.Panel):
    
    bl_idname = "MOCAP_IMPORT_PT_Panel"
    bl_label = "MOCAP Import "+VERSION
    bl_category = "MOCAP"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        sk_value_prop = context.scene.sk_value_prop
        # percent_render_var = sk_value_prop.sk_value

        row = layout.row()
        rowb = layout.row().box()
        row = rowb.row()
        row.prop(scene, "expand_audio2face",
            icon="TRIA_DOWN" if scene.expand_audio2face else "TRIA_RIGHT",
            icon_only=True, emboss=False
        )
        row.label(text='Nvidia Audio2face')
        if scene.expand_audio2face:
            row = rowb.row(align=True).column(align=True)
            # row = rowb.row()
            # row = layout.row()
            row.operator('mocap.export_audio2face', text="Export Model")
            # row = layout.row()
            row.operator('mocap.import_audio2face_to_nla', text="Import as NLA Strip")
            # row = layout.row()
            row.operator('mocap.import_audio2face', text="Import with Modifier")
            # row = layout.row()
            # row.label(text='----------')

            
            row = rowb.row(align=True).column(align=True)
            # row = rowb.row()
            # row = layout.row()
            row.operator('mocap.delete_action_shapekey_nla', text="Del Action, ShapeKey and NLA")
            # row = layout.row()
            row.operator('mocap.delete_unused_sk_nla_tracks', text="Del Unused ShapeKey NLA Tracks")
            # row = layout.row()
            # row.label(text='----------')

        rowb = layout.row().box()
        row = rowb.row()
        row.prop(scene, "mediapipe",
            icon="TRIA_DOWN" if scene.mediapipe else "TRIA_RIGHT",
            icon_only=True, emboss=False
        )
        # row.label(text='Mediapipe'+sk_value_prop.sk_frame_str)
        row.label(text='Mediapipe')
        if scene.mediapipe:
            row = rowb.row(align=True).column(align=True)

            #####
            ## New mediapipe tools
            # row = layout.row()
            
            # row = layout.row()
            row.operator('view3d.mp_preview_load', text="Load Video or Folder")
            # row = layout.row()
            # row.label(text='Point Name')
            # # row = layout.row()
            # row.prop(sk_value_prop, "sk_point_name")
            # row = layout.row()
            # row.label(text='Bone ajustment')
            # row = layout.row()
            # row.prop(sk_value_prop, "sk_bone_sz")
            # # row = layout.row()
            # row.operator('view3d.update_bone_size', text="Resize Bone")
            
            # row = layout.row()
            # row.label(text='Hand Mocap')
            # # row = layout.row()
            # row.operator('view3d.hand_mocap', text="Load Hand Video")
            
            
            
            # row = layout.row()
            # row.label(text='Retarget Pair of Bones')
            # row = layout.row()
            # row.operator('view3d.retarget_selected', text="Retarget Selected")
            # row = layout.row()
            # row.label(text='Range')
            # row = layout.row()
            # row.prop(sk_value_prop, "sk_start_frame")
            # row.prop(sk_value_prop, "sk_end_frame")

            ## New mediapipe tools  
            #################################


        rowb = layout.row().box()
        row = rowb.row()
        

        row.prop(scene, "older_tools",
            icon="TRIA_DOWN" if scene.older_tools else "TRIA_RIGHT",
            icon_only=True, emboss=False
        )
        row.label(text='Older Tools')
        if scene.older_tools:
            # row = layout.row()
            row = rowb.row(align=True).column(align=True)
            row.prop(sk_value_prop, "sk_raw_bool", text="Raw Import")
            # row = layout.row()
            row.prop(sk_value_prop, "sk_constraint_limit_rotation_bool", text="Constraint Limit Rotation")
            
            # row = layout.row()
            row.prop(sk_value_prop, "sk_debug_bool", text="Debug")
        
            
            
            # row = layout.row()
            # row.label(text='----------')
            # row = layout.row()
            rowb = layout.row().box()
            row = rowb.row()
            row = rowb.row(align=False).column(align=False)
            row.label(text='Easymocap SMPL')
            row.operator('mocap.import_smpl_easymocap', text="Import SMPL EasyMOCAP")
            # row = layout.row()
            row.prop(sk_value_prop, "sk_smpl_path")
            # row = layout.row()
            row.operator('mocap.browse_smpl_file', text="Browse SMPL FBX File")


            row = layout.row()
            row.label(text='Tools with Skeleton Multiplier')            
            rowb = layout.row().box()
            row = rowb.row(align=False).column(align=False)
            row.label(text='Skeleton Multiplier')
            row.prop(sk_value_prop, "sk_value", text="SK Mult")

            row = rowb.row()
            
            row = rowb.row(align=True)
            row.label(text='Easymocap')
            row.operator('mocap.import_easymocap', text="Import")
            row.operator('mocap.import_easymocap_reload', text="Reload Skeleton")
            # row = layout.row()
            # row = rowb.row(align=False).column(align=False)
            row = rowb.row(align=True)
            row.label(text='Frankmocap')
            row.operator('mocap.import_frankmocap', text="Import")
            # row = layout.row()
            row.operator('mocap.import_frankmocap_alter', text="Alternative Import")


            # row.row().separator()
            # row = layout.row()
            row = rowb.row(align=False).column(align=False)
            row = rowb.row(align=True)
            row.label(text='Vibe')
            row.operator('mocap.import_vibe', text="Import")
            # row = layout.row()
            row.prop(sk_value_prop, "vibe_person_id", text="PersonID")
            # layout.row().separator()

            # row = layout.row()
            row = rowb.row(align=False).column(align=False)
            row = rowb.row(align=True)
            row.label(text='Mediapipe')
            row.operator('mocap.mediapipe_pose', text="Import")
            # layout.row().separator()
            

            # Create two columns, by using a split layout.
            # split = layout.split()

            # First column
            # col = split.column()
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


        rowb = layout.row().box()
        row = rowb.row()
        row.prop(scene, "install_py",
            icon="TRIA_DOWN" if scene.install_py else "TRIA_RIGHT",
            icon_only=True, emboss=False
        )
        row.label(text='Install PyPacks')
        if scene.install_py:

            # row = layout.row()
            row = rowb.column(align=True)
            row.operator('install.mediapipe_package', text="Install Mediapipe Package")
            # row = layout.row()
            row.operator('install.joblib_package', text="Install Joblib (Vibe requirement)")


        
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
    ##########
    #start variables for new mediapipe update 
    sk_point_name: StringProperty(name=".",default="Point", description="Name of the point")
    # sk_start_frame: IntProperty(name="Start",default=bpy.context.scene.frame_start, description="Frame Start")
    # sk_end_frame: IntProperty(name="End",default=bpy.context.scene.frame_end, description="Frame End")
    sk_bone_sz: FloatProperty(name="Bone size",default=0.5, description="Size of the bone")
   
    #End variables for new mediapipe update 
    ###########
    sk_frame_str: StringProperty(name="Info about Frames", description="Show frame on screen", default='')

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

