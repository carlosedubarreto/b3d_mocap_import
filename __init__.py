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

# beta 0.62
# - choose SMPL model Male or female (instead of only the male one)
# - option to choose SMPLX model (with hands and face animation)
# - the SMPLX model with fingers should be generated using this addon https://gitlab.tuebingen.mpg.de/jtesch/smplx_blender_addon and exported the Male character to FBX
# - at the moment easymocap doesnt export hand and finger movement, so it need to apply these changes https://github.com/zju3dv/EasyMocap/issues/25#issuecomment-842266080
# when generating the data from easymocap, the parameters like this "python apps/demo/mv1p.py 0_input/20210505_guitar --out 1_output/20210505_guitar --vis_det --vis_repro --undis --sub_vis 1 2 --body bodyhandface --model smplx --gender male --vis_smpl"

bl_info = {
    "name" : "MOCAP Pose Estimation Data Import",
    "author" : "Carlos Barreto",
    "description" : "",
    "blender" : (2, 90, 0),
    "version" : (0, 0, 62),
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
                        Install_Mediapipe,Install_Joblib,Convert_axis,Reset_location,Reset_rotation,Foot_high,Compensate_Rotation,Smooth_Bone, Reload_sk_easymocap, Import_SMPL_easymocap,Path_SMPL_FBX_File
from . test_panel import Test_PT_Panel, MySettings, Install_PT_Panel, Modify_PT_Panel,Debug_PT_Panel

classes = (Import_Data_easymocap, Test_PT_Panel, OT_TestOpenFilebrowser,Import_Data_frankmocap,Import_Data_vibe,Mediapipe_Pose_estimation,
            Install_Mediapipe,Install_Joblib,MySettings,Modify_PT_Panel,Install_PT_Panel,Convert_axis,Reset_location,Reset_rotation,Foot_high,Compensate_Rotation,Smooth_Bone,Debug_PT_Panel, Reload_sk_easymocap, Import_SMPL_easymocap, Path_SMPL_FBX_File)

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