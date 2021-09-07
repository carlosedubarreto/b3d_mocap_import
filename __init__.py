# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# beta 0.74
# - Update Mediapipe Body pose estimation

bl_info = {
    "name" : "MOCAP Import",
    "author" : "Carlos Barreto",
    "description" : "Addon to import data from Easymocap, Frankmocap, Vibe and Google Mediapipe",
    "blender" : (2, 90, 0),
    "version" : (0, 0, 75),
    "location" : "3dView > Sidebar(N panel)",
    "warning" : "",
    "category" : "Animation"
}
global VERSION
VERSION = 'b 0.75'



import bpy

from bpy.props import (#StringProperty,
                    #    BoolProperty,
                      IntProperty,
                      FloatProperty,
#                       FloatVectorProperty,
#                       EnumProperty,
                       PointerProperty,
                       )

from . load_mocap import Import_Data_easymocap, OT_TestOpenFilebrowser,Import_Data_frankmocap,Import_Data_frankmocap_alter,Import_Data_vibe,Mediapipe_Pose_estimation, \
                        Install_Mediapipe,Install_Joblib,Convert_axis,Reset_location,Reset_rotation,Foot_high,Compensate_Rotation,Smooth_Bone, \
                            Reload_sk_easymocap, Import_SMPL_easymocap,Path_SMPL_FBX_File,Audio2face_Import,Audio2face_Export, Audio2face_Import_to_NLA, Audio2face_delete_action_shapekey_nla, Delete_unused_NLA_SK_tracks
from . panel import Test_PT_Panel, MySettings#, Install_PT_Panel#, Modify_PT_Panel,Debug_PT_Panel
from . mediapipe_new import *

classes = (Import_Data_easymocap, Test_PT_Panel, OT_TestOpenFilebrowser,Import_Data_frankmocap,Import_Data_frankmocap_alter,Import_Data_vibe,Mediapipe_Pose_estimation,
            Install_Mediapipe,Install_Joblib,MySettings,#Install_PT_Panel,Convert_axis,Reset_location,Reset_rotation,Foot_high,
            Compensate_Rotation,Smooth_Bone, Reload_sk_easymocap, Import_SMPL_easymocap, 
            Path_SMPL_FBX_File,Audio2face_Import,Audio2face_Export, 
            Audio2face_Import_to_NLA, Audio2face_delete_action_shapekey_nla, 
            Delete_unused_NLA_SK_tracks,
            MP_preview,Transfer_Angles,update_bone_size,Hand_mocap
            )#,Modify_PT_Panel,Debug_PT_Panel

# register, unregister = bpy.utils.register_classes_factory(classes)
def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    # bpy.types.Scene.my_tool = PointerProperty(type=MySettings)
    bpy.types.Scene.sk_value_prop = PointerProperty(type=MySettings)
    bpy.types.Scene.expand_audio2face = bpy.props.BoolProperty(default=True)
    bpy.types.Scene.mediapipe = bpy.props.BoolProperty(default=True)
    bpy.types.Scene.older_tools = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.install_py = bpy.props.BoolProperty(default=False)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls) 
    del bpy.types.Scene.sk_value_prop




if __name__ == "__main__":
    register()
    # bpy.types.Scene.percentage = PointerProperty(type=MySettingsPerc)    