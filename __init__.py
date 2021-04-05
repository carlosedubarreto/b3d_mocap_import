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

# beta 0.4
# - add mediapipe converter and motion creation seamsly inside blender

bl_info = {
    "name" : "MOCAP Pose Estimation Data Import",
    "author" : "Carlos Barreto",
    "description" : "",
    "blender" : (2, 90, 0),
    "version" : (0, 0, 4),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}
import bpy
# from . load_mocap import Import_Data_easymocap, OT_TestOpenFilebrowser,Import_Data_frankmocap,Import_Data_vibe
from . load_mocap import Import_Data_easymocap, OT_TestOpenFilebrowser,Import_Data_frankmocap,Import_Data_vibe,Mediapipe_Pose_estimation,Install_Mediapipe,Install_Joblib
from . test_panel import Test_PT_Panel

# classes = (Import_Data_easymocap, Test_PT_Panel, OT_TestOpenFilebrowser,Import_Data_frankmocap,Import_Data_vibe)
classes = (Import_Data_easymocap, Test_PT_Panel, OT_TestOpenFilebrowser,Import_Data_frankmocap,Import_Data_vibe,Mediapipe_Pose_estimation,Install_Mediapipe,Install_Joblib)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()