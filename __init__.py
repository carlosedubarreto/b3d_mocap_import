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

# Alpha 0.1
# - Realtime with mediapipe
# Alpha 0.11
# - Better installation of Mediapipe


bl_info = {
    "name" : "MOCAP Pose Estimation Data Import ALPHA",
    "author" : "Carlos Barreto",
    "description" : "",
    "blender" : (2, 90, 0),
    "version" : (0, 0, 11),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}
import bpy

from bpy.props import (#StringProperty,
                    #    BoolProperty,
                      IntProperty,
                      FloatProperty,
#                       FloatVectorProperty,
#                       EnumProperty,
                       PointerProperty,
                       )

from . load_mocap import Import_Data_easymocap, OT_TestOpenFilebrowser,Import_Data_frankmocap,Import_Data_vibe,Mediapipe_Pose_estimation, \
                        Install_Mediapipe,Install_Joblib,Convert_axis,Reset_location,Reset_rotation,Foot_high,Compensate_Rotation,Smooth_Bone,Mediapipe_Pose_estimation_RT, Mediapipe_Pose_Prepare_Skeleton_RT, Reload_sk_Mediapipe
from . test_panel import Test_PT_Panel, MySettings, Install_PT_Panel, Modify_PT_Panel, Debug_PT_Panel

classes = (Import_Data_easymocap, Test_PT_Panel, OT_TestOpenFilebrowser,Import_Data_frankmocap,Import_Data_vibe,Mediapipe_Pose_estimation,
            Install_Mediapipe,Install_Joblib,MySettings,Modify_PT_Panel,Install_PT_Panel,Convert_axis,Reset_location,Reset_rotation,Foot_high,Compensate_Rotation,Smooth_Bone,Mediapipe_Pose_estimation_RT,Mediapipe_Pose_Prepare_Skeleton_RT, 
            Reload_sk_Mediapipe, Debug_PT_Panel)

# register, unregister = bpy.utils.register_classes_factory(classes)
def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    # bpy.types.Scene.my_tool = PointerProperty(type=MySettings)
    bpy.types.Scene.sk_value_prop = PointerProperty(type=MySettings)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls) 
    del bpy.types.Scene.sk_value_prop




if __name__ == "__main__":
    register()
    # bpy.types.Scene.percentage = PointerProperty(type=MySettingsPerc)    