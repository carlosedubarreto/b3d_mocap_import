import json
import os
import bpy
from bpy import context
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator
from bpy.props import StringProperty, BoolProperty, EnumProperty
from . helper import helper_functions
import math


class OT_TestOpenFilebrowser(Operator, ImportHelper):

    bl_idname = "test.open_filebrowser"
    bl_label = "Open the file browser (yay)"


    def execute(self, context):
        
        filename, extension = os.path.splitext(self.filepath)
        
        print('real path', os.path.dirname(self.filepath))
        print('Selected file:', self.filepath)
        print('File name:', filename)
        print('File extension:', extension)
        # print('Some Boolean:', self.some_boolean)

        return {'FINISHED'}


class Import_Data_easymocap(Operator, ImportHelper):

    bl_idname = "mocap.import_easymocap"
    bl_label = "Import data"
    bl_description = "Import EasyMOCAP"


    filename_ext = ".json"

    filter_glob: StringProperty(
        default="*.json",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )




    def execute(self,context):

        

        #========================
        #EASYMOCAP
        #=====================

        import os
        import json
        import bpy
        from bpy import context
        import math 
        # bpy.ops.test.open_filebrowser('INVOKE_DEFAULT')#abrir janela de navegador

        object = []
        for ob in bpy.context.scene.objects:
                object.append(ob)

        if len(object) >0 :
            if bpy.context.mode != 'OBJECT':
                bpy.ops.object.editmode_toggle()

        #path = r'D:\MOCAP\EasyMocap-master\Teste_20210321_1_out\keypoints3d'
        path = os.path.dirname(self.filepath)
        list_dir = os.listdir(path)
        s_list = sorted(list_dir)

        data = []
        for i in s_list:
            with open(path+ os.sep +i,'r') as f: 
                data.append(json.load(f))
                #json.load(f)
                
        len(data)

        #-----------------
        x=0
        y=1
        z=2

        #armature = 'Armature'

        #=====================
        #trecho usado para rotacionar ao redor do cursor 
        def get_override(area_type, region_type):
            for area in bpy.context.screen.areas: 
                if area.type == area_type:             
                    for region in area.regions:                 
                        if region.type == region_type:                    
                            override = {'area': area, 'region': region} 
                            return override
            #error message if the area or region wasn't found
            raise RuntimeError("Wasn't able to find", region_type," in area ", area_type,
                                "\n Make sure it's open while executing script.")





        #===================================
        #creating bones
        #====================================

        # obs = []
        # for ob in bpy.context.scene.objects:
        #     # if ob.type == 'ARMATURE':
        #         obs.append(ob)
        # if len(obs)>0:
        #     if obs[len(obs)-1].mode != 'OBJECT':
        #         bpy.ops.object.editmode_toggle() #try to change to object mode
        #         if obs[len(obs)-1].mode != 'OBJECT':
        #             bpy.ops.object.editmode_toggle() #try again to change to object mode

        bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) #cria armature e primeiro bone
        #bpy.ops.object.editmode_toggle()
        #bpy.data.armatures['Armature'].edit_bones.active = bpy.context.object.data.edit_bones['Bone']


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.armature.select_all(action='DESELECT')
        #bpy.context.object.data.edit_bones['Bone'].select_tail=True
        obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True
        #bpy.ops.armature.extrude_move()#Neck
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        #bpy.ops.armature.extrude_move()#Head_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        bpy.ops.armature.select_all(action='DESELECT')
        bpy.context.object.data.edit_bones['Bone.001'].select_tail=True
        #bpy.ops.armature.extrude_move()#Head_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})



        bpy.ops.armature.bone_primitive_add()#Forearm_L
        #bpy.ops.armature.extrude_move()#Arm_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Forearm_R
        #bpy.ops.armature.extrude_move()#Arm_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_L
        #bpy.ops.armature.extrude_move()#Leg_L
        #bpy.ops.armature.extrude_move()#Foot_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_R
        #bpy.ops.armature.extrude_move()#Leg_R
        #bpy.ops.armature.extrude_move()#Foot_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        #bpy.ops.object.editmode_toggle()
        #bpy.data.objects['Armature'].data.edit_bones['Arm_L'].name = 'Teste'

        #bpy.context.object.data.edit_bones["Bone"].name = 'Spline'
        #bpy.context.object.data.edit_bones["Bone.001"].name = 'Neck'
        #bpy.context.object.data.edit_bones["Bone.002"].name = 'Head_L'
        #bpy.context.object.data.edit_bones["Bone.003"].name = 'Head_R'
        #bpy.context.object.data.edit_bones["Bone.004"].name = 'Forearm_L'
        #bpy.context.object.data.edit_bones["Bone.005"].name = 'Arm_L'
        #bpy.context.object.data.edit_bones["Bone.006"].name = 'Forearm_R'
        #bpy.context.object.data.edit_bones["Bone.007"].name = 'Arm_R'
        #bpy.context.object.data.edit_bones["Bone.008"].name = 'Thigh_L'
        #bpy.context.object.data.edit_bones["Bone.009"].name = 'Leg_L'
        #bpy.context.object.data.edit_bones["Bone.010"].name = 'Foot_L'
        #bpy.context.object.data.edit_bones["Bone.011"].name = 'Thigh_R'
        #bpy.context.object.data.edit_bones["Bone.012"].name = 'Leg_R'
        #bpy.context.object.data.edit_bones["Bone.013"].name = 'Foot_R'



        obs[len(obs)-1].data.edit_bones["Bone"].name = 'Spline'
        obs[len(obs)-1].data.edit_bones["Bone.001"].name = 'Neck'
        obs[len(obs)-1].data.edit_bones["Bone.002"].name = 'Head_L'
        obs[len(obs)-1].data.edit_bones["Bone.003"].name = 'Head_R'
        obs[len(obs)-1].data.edit_bones["Bone.004"].name = 'Forearm_L'
        obs[len(obs)-1].data.edit_bones["Bone.005"].name = 'Arm_L'
        obs[len(obs)-1].data.edit_bones["Bone.006"].name = 'Forearm_R'
        obs[len(obs)-1].data.edit_bones["Bone.007"].name = 'Arm_R'
        obs[len(obs)-1].data.edit_bones["Bone.008"].name = 'Thigh_L'
        obs[len(obs)-1].data.edit_bones["Bone.009"].name = 'Leg_L'
        obs[len(obs)-1].data.edit_bones["Bone.010"].name = 'Foot_L'
        obs[len(obs)-1].data.edit_bones["Bone.011"].name = 'Thigh_R'
        obs[len(obs)-1].data.edit_bones["Bone.012"].name = 'Leg_R'
        obs[len(obs)-1].data.edit_bones["Bone.013"].name = 'Foot_R'

        bpy.ops.object.editmode_toggle()















        #remove Collection
        if bpy.data.collections.find("Points") >= 0:
            collection = bpy.data.collections.get('Points')
            #
            for obj in collection.objects:
                bpy.data.objects.remove(obj, do_unlink=True)
            bpy.data.collections.remove(collection)










        #cria os pontos nuima collection chamada Points
        #=====================================================
        collection = bpy.data.collections.new("Points")
        bpy.context.scene.collection.children.link(collection)

        layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
        bpy.context.view_layer.active_layer_collection = layer_collection

        for point in range(25):
            bpy.ops.mesh.primitive_plane_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
            bpy.ops.mesh.merge(type='CENTER')
            bpy.ops.object.editmode_toggle()
            context.active_object.name = 'Point.'+str(1000+point)[1:]
        #=====================================================





        #colocar cursor no tempo
        #bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
        #bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'




        ## Deselect all objects
        #bpy.ops.object.select_all(action='DESELECT')

        #for o in bpy.data.objects:
        #    # Check for given object names
        #    if o.name in ("Point.000","Point.001","Point.002","Point.003","Point.004","Point.005","Point.006","Point.007","Point.008","Point.009" ,"Point.010" ,"Point.011","Point.012","Point.013","Point.014","Point.015","Point.016","Point.017","Point.018","Point.019","Point.020" ,"Point.021","Point.022","Point.023","Point.024"):
        #        o.select_set(True)

        for item in range(len(data)):
            print("frame: ",item)
            for limb in range(len(data[item][0]['keypoints3d'])):
                # print("limb: ",limb)
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[x]=data[item][0]['keypoints3d'][limb][x]
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[y]=data[item][0]['keypoints3d'][limb][y]
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[z]=data[item][0]['keypoints3d'][limb][z]
                #
                
        #        #we need to override the context of our operator    
        #        override = get_override( 'VIEW_3D', 'WINDOW' )
        #        #rotate about the X-axis by 45 degrees
        #        bpy.ops.transform.rotate(override, value=6.283/2, orient_axis="Y") 
        #        
                #Salva Frame
                bpy.data.objects["Point."+str(1000+limb)[1:]].keyframe_insert(data_path="location", frame=item)






        #==========================================================================================================

        def distance(point1, point2) -> float: 
            #Calculate distance between two points in 3D.
        #    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)
            return math.sqrt((point2.location[0] - point1.location[0]) ** 2 + (point2.location[1] - point1.location[1]) ** 2 + (point2.location[2] - point1.location[2]) ** 2)


        def size_bone(point_name1, point_name2, bone):
            p1 = bpy.data.objects[point_name1]
            p2 = bpy.data.objects[point_name2]
            #edit bones
            if bpy.context.active_object.mode == 'EDIT':
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            else:
                bpy.ops.object.editmode_toggle()
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            bpy.ops.object.editmode_toggle()

        #selecting and making the armature Active
        #selecionando armature

        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        armature = obs[len(obs)-1].name

        #bpy.data.objects[armature].select_set(True)
        obs[len(obs)-1].select_set(True)
        view_layer = bpy.context.view_layer
        #Armature_obj = bpy.context.scene.objects[armature]
        Armature_obj = obs[len(obs)-1]
        view_layer.objects.active = Armature_obj



        size_bone("Point.008", "Point.001", "Spline")
        size_bone("Point.001", "Point.000", "Neck")
        size_bone("Point.000", "Point.016", "Head_L")
        size_bone("Point.000", "Point.015", "Head_R")

        size_bone("Point.005", "Point.006", "Forearm_L")
        size_bone("Point.006", "Point.007", "Arm_L")

        size_bone("Point.002", "Point.003", "Forearm_R")
        size_bone("Point.003", "Point.004", "Arm_R")

        size_bone("Point.012", "Point.013", "Thigh_L")
        size_bone("Point.013", "Point.014", "Leg_L")
        size_bone("Point.014", "Point.019", "Foot_L")

        size_bone("Point.009", "Point.010", "Thigh_R")
        size_bone("Point.010", "Point.011", "Leg_R")
        size_bone("Point.011", "Point.022", "Foot_R")

        #comecando configuração  seguir movimentos pontos
        #colocando em pose mode
        bpy.ops.object.mode_set(mode='POSE')

        #bpy.data.objects[armature].pose.bones["Spine"]
        #bpy.data.objects[armature].pose.bones["Spine"].bone

        actual_bone = 'Spline'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True

        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.008"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.001"]
        #=====
        actual_bone = 'Neck'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.001"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.000"]
        #=====
        actual_bone = 'Head_L'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.000"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.016"]
        #=====
        actual_bone = 'Head_R'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.000"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.015"]
        #=====


        actual_bone = 'Forearm_L'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.005"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.006"]
        #=====
        actual_bone = 'Arm_L'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.006"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.007"]
        #=====


        actual_bone = 'Forearm_R'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.002"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.003"]
        #=====
        actual_bone = 'Arm_R'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.003"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.004"]
        #=====




        actual_bone = 'Thigh_L'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.012"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.013"]
        #=====
        actual_bone = 'Leg_L'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.013"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.014"]
        #=====
        actual_bone = 'Foot_L'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.014"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.019"]
        #=====




        actual_bone = 'Thigh_R'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.009"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.010"]
        #=====
        actual_bone = 'Leg_R'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.010"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.011"]
        #=====
        actual_bone = 'Foot_R'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.011"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.022"]
        #=====

        #bpy.data.objects['Armature'].pose.bones.items()
        #[('Bone', bpy.data.objects['Armature'].pose.bones["Bone"]), ('Thigh_L', bpy.data.objects['Armature'].pose.bones["Thigh_L"]), ('Leg_L', bpy.data.objects['Armature'].pose.bones["Leg_L"]), ('Foot_L', bpy.data.objects['Armature'].pose.bones["Foot_L"]), ('Spine', bpy.data.objects['Armature'].pose.bones["Spine"]), ('Neck', bpy.data.objects['Armature'].pose.bones["Neck"]), ('Head_L', bpy.data.objects['Armature'].pose.bones["Head_L"]), ('Head_R', bpy.data.objects['Armature'].pose.bones["Head_R"]), ('Forearm_L', bpy.data.objects['Armature'].pose.bones["Forearm_L"]), ('Arm_L', bpy.data.objects['Armature'].pose.bones["Arm_L"]), ('Thigh_R', bpy.data.objects['Armature'].pose.bones["Thigh_R"]), ('Leg_R', bpy.data.objects['Armature'].pose.bones["Leg_R"]), ('Foot_R', bpy.data.objects['Armature'].pose.bones["Foot_R"]), ('Forearm_R', bpy.data.objects['Armature'].pose.bones["Forearm_R"]), ('Arm_R', bpy.data.objects['Armature'].pose.bones["Arm_R"])]

        print(len(data))
        bpy.context.scene.frame_end = len(data)

        bpy.ops.nla.bake(frame_start=1, frame_end=len(data), visual_keying=True, clear_constraints=True, clear_parents=True, bake_types={'POSE'})
        bpy.ops.object.mode_set(mode='OBJECT')




        #apagar collection points criada
        collection = bpy.data.collections.get('Points')
        #
        for obj in collection.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(collection)


        return{'FINISHED'}


class Import_Data_frankmocap(Operator, ImportHelper):
    bl_idname = "mocap.import_frankmocap"
    bl_label = "Import data from Frankmocap"
    bl_description = "Import FrankMocap"


    filename_ext = ".pkl"

    filter_glob: StringProperty(
        default="*.pkl",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )




    def execute(self,context):

        #"""
        #Frnakmocap
        #==========================
        
        import math
        import bpy
        import os
        import pickle
        import numpy as np
        from bpy import context
        import joblib

        multiplier = context.scene.sk_value_prop.sk_value
        raw_bool = context.scene.sk_value_prop.sk_raw_bool

        def middle_point(p1,p2,p_middle):
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[p1].select_set(True)
            bpy.data.objects[p2].select_set(True)
            bpy.context.view_layer.objects.active = bpy.data.objects[p2]
            obs = bpy.context.selected_objects
            n = len(obs)
        #    print('n: ',n)
            assert(n)
            #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
            bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n


        def create_dots(name, amount):
            #remove Collection
            if bpy.data.collections.find(name) >= 0:
                collection = bpy.data.collections.get(name)
                #
                for obj in collection.objects:
                    bpy.data.objects.remove(obj, do_unlink=True)
                bpy.data.collections.remove(collection)
            #cria os pontos nuima collection chamada Points
            #=====================================================
            collection = bpy.data.collections.new(name)
            bpy.context.scene.collection.children.link(collection)
        #
            layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
            bpy.context.view_layer.active_layer_collection = layer_collection
        #
            for point in range(amount):
                bpy.ops.mesh.primitive_plane_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                bpy.ops.mesh.merge(type='CENTER')
                bpy.ops.object.editmode_toggle()
                bpy.context.active_object.name = name+'.'+str(1000+point)[1:]
            #=====================================================

        #==============================
        #codes to size the bones
        #==============================

        def distance(point1, point2) -> float:
            #Calculate distance between two points in 3D.
        #    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)
            return math.sqrt((point2.location[0] - point1.location[0]) ** 2 + (point2.location[1] - point1.location[1]) ** 2 + (point2.location[2] - point1.location[2]) ** 2)


        def size_bone(point_name1, point_name2, bone):
            p1 = bpy.data.objects[point_name1]
            p2 = bpy.data.objects[point_name2]
            #edit bones
            if bpy.context.active_object.mode == 'EDIT':
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            else:
                bpy.ops.object.editmode_toggle()
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            bpy.ops.object.editmode_toggle()



        create_dots('Point',49)


        # pkl_path=r'C:\MOCAP\frankmocap\mocap_output\mocap\temp'
        pkl_path = os.path.dirname(self.filepath)
        list_dir = os.listdir(pkl_path)
        s_list = sorted(list_dir)

        len(s_list)

        x=0
        y=1
        z=2
        multi=100
        #armature = 'Armature'


        #exemplo
        file = open(pkl_path+ os.sep +s_list[0],'rb')

        pic = pickle.load(file)
        file.close()

        nppic = np.load(pkl_path+ os.sep +s_list[0], allow_pickle=True)

        for item in range(len(s_list)-1):
            nppic = np.load(pkl_path+ os.sep +s_list[item], allow_pickle=True)
        #    nppic['pred_output_list'][0]['pred_body_joints_img'] #todos os limbs
            print("frame: ",item)
            for limb in range(len(nppic['pred_output_list'][0]['pred_body_joints_img'])):
        #        print("limb: ",limb)
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[z]=nppic['pred_output_list'][0]['pred_body_joints_img'][limb][x]/multi
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[y]=nppic['pred_output_list'][0]['pred_body_joints_img'][limb][y]/multi
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[x]=nppic['pred_output_list'][0]['pred_body_joints_img'][limb][z]/multi
                bpy.data.objects["Point."+str(1000+limb)[1:]].keyframe_insert(data_path="location", frame=item)


        len(nppic['pred_output_list'][0]['pred_body_joints_img'])



        import bpy


        #===========
        # selectign Scene Collection
        scene_collection = bpy.context.view_layer.layer_collection
        bpy.context.view_layer.active_layer_collection = scene_collection


        #===================================
        #creating bones
        #====================================

        bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) #cria armature e primeiro bone
        #bpy.ops.object.editmode_toggle()
        #bpy.data.armatures['Armature'].edit_bones.active = bpy.context.object.data.edit_bones['Bone']


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs


        bpy.ops.armature.select_all(action='DESELECT')
        #bpy.context.object.data.edit_bones['Bone'].select_tail=True
        obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True

        bpy.ops.armature.bone_primitive_add()#Spine
        #bpy.ops.armature.extrude_move()#Neck
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        ##bpy.ops.armature.extrude_move()#Face
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        bpy.ops.armature.bone_primitive_add()#Arm_L
        #bpy.ops.armature.extrude_move()#Forearm_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Arm_R
        #bpy.ops.armature.extrude_move()#Forearm_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_L
        #bpy.ops.armature.extrude_move()#Leg_L
        #bpy.ops.armature.extrude_move()#Foot_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_R
        #bpy.ops.armature.extrude_move()#Leg_R
        #bpy.ops.armature.extrude_move()#Foot_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        obs[len(obs)-1].data.edit_bones["Bone"].name = 'Root'
        obs[len(obs)-1].data.edit_bones["Bone.001"].name = 'Spine'
        obs[len(obs)-1].data.edit_bones["Bone.002"].name = 'Neck'
        obs[len(obs)-1].data.edit_bones["Bone.003"].name = 'Face'
        obs[len(obs)-1].data.edit_bones["Bone.004"].name = 'Arm_L'
        obs[len(obs)-1].data.edit_bones["Bone.005"].name = 'Forearm_L'
        obs[len(obs)-1].data.edit_bones["Bone.006"].name = 'Arm_R'
        obs[len(obs)-1].data.edit_bones["Bone.007"].name = 'Forearm_R'
        obs[len(obs)-1].data.edit_bones["Bone.008"].name = 'Thigh_L'
        obs[len(obs)-1].data.edit_bones["Bone.009"].name = 'Leg_L'
        obs[len(obs)-1].data.edit_bones["Bone.010"].name = 'Foot_L'
        obs[len(obs)-1].data.edit_bones["Bone.011"].name = 'Thigh_R'
        obs[len(obs)-1].data.edit_bones["Bone.012"].name = 'Leg_R'
        obs[len(obs)-1].data.edit_bones["Bone.013"].name = 'Foot_R'


        #Hierarquia
        bpy.context.object.data.edit_bones["Spine"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Arm_L"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Arm_R"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Thigh_L"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Thigh_R"].parent = bpy.context.object.data.edit_bones["Root"]

        bpy.ops.object.editmode_toggle()



        from mathutils import Vector
        import bpy

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Point.001'].select_set(True)
        bpy.data.objects['Point.008'].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects['Point.034']
        obs = bpy.context.selected_objects
        n = len(obs)
        #    print('n: ',n)
        assert(n)
        #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
        #bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n



        x_subtract = abs(obs[0].matrix_world.translation.x - obs[1].matrix_world.translation.x)
        y_subtract = abs(obs[0].matrix_world.translation.y - obs[1].matrix_world.translation.y)
        z_subtract = abs(obs[0].matrix_world.translation.z - obs[1].matrix_world.translation.z)

        max(x_subtract, y_subtract, z_subtract) #maior das medidas
        unit = max(x_subtract, y_subtract, z_subtract)/3
        unit = unit*multiplier

        root_sz    =unit/10
        spine_sz   =unit*3.5
        neck_sz    =unit
        face_sz    =unit
        thigh_sz    =unit*3
        leg_sz     =unit*2.5
        foot_sz    =unit #inclinado 45 graud pra frente
        arm_sz     =unit*1.5
        forearm_sz =unit*1.5



        #if bpy.context.active_object.mode != 'EDIT':
        #    bpy.ops.object.editmode_toggle()
        #==========================================
        #selecting and making the armature Active
        #selecionando armature
        #==========================================
        bpy.ops.object.select_all(action='DESELECT')
        #bpy.ops.armature.select_all(action='DESELECT')

        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        armature = obs[len(obs)-1].name

        #bpy.data.objects[armature].select_set(True)
        obs[len(obs)-1].select_set(True)
        view_layer = bpy.context.view_layer
        #Armature_obj = bpy.context.scene.objects[armature]
        Armature_obj = obs[len(obs)-1]
        view_layer.objects.active = Armature_obj


        #converting to euler rotation
        order = 'XYZ'
        context = bpy.context
        rig_object = context.active_object
        for pb in rig_object.pose.bones:
            pb.rotation_mode = order



        bpy.ops.object.editmode_toggle()

        #changing location
        #resetting
        bpy.context.object.data.edit_bones["Spine"].head.xy=0
        bpy.context.object.data.edit_bones["Neck"].head.xy=0
        bpy.context.object.data.edit_bones["Face"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_L"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_R"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_L"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_L"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_R"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_R"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].head.xy=0
        #tail
        bpy.context.object.data.edit_bones["Face"].tail.xy=0
        bpy.context.object.data.edit_bones["Neck"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].tail.xy=0




        bpy.context.object.data.edit_bones["Root"].length = root_sz

        bpy.context.object.data.edit_bones["Spine"].head.z = unit/2
        bpy.context.object.data.edit_bones["Spine"].tail.z = spine_sz

        bpy.context.object.data.edit_bones["Neck"].tail.z =  spine_sz + neck_sz
        bpy.context.object.data.edit_bones["Neck"].tail.y = neck_sz/3
        bpy.context.object.data.edit_bones["Face"].tail.z = spine_sz + neck_sz
        bpy.context.object.data.edit_bones["Face"].tail.y = face_sz*-1

        bpy.context.object.data.edit_bones["Arm_L"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Forearm_L"].head.z=  spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].head.x= unit + arm_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.x= unit + arm_sz + forearm_sz

        bpy.context.object.data.edit_bones["Arm_R"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_R"].head.x= (unit*3/4)*-1
        bpy.context.object.data.edit_bones["Forearm_R"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].head.x= (unit + arm_sz) *-1
        bpy.context.object.data.edit_bones["Forearm_R"].tail.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].tail.x= (unit + arm_sz + forearm_sz) *-1

        bpy.context.object.data.edit_bones["Thigh_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Thigh_L"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Leg_L"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.y= foot_sz/2*-1

        bpy.context.object.data.edit_bones["Thigh_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Thigh_R"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.y= foot_sz/2*-1

        bpy.ops.object.editmode_toggle()



        import bpy

        #comecando configuração  seguir movimentos pontos
        #colocando em pose mode


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.object.mode_set(mode='POSE')


        actual_bone = 'Root'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.008"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.039"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.001"]
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.037"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.001"]
        bpy.context.object.pose.bones[actual_bone].constraints[2].target = bpy.data.objects["Point.027"]
        bpy.context.object.pose.bones[actual_bone].constraints[2].track_axis = 'TRACK_X'


        #====
        actual_bone = 'Spine'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.001"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.037"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x  = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.349066
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = -0.698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0.698132
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.174533

        #=====
        actual_bone = 'Neck'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.000"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.042"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.0472
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0.523599
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.349066
        #=====
        actual_bone = 'Face'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.044"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.872665
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.523599
        #=====
        actual_bone = 'Arm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.006"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.032"]
        #=====
        actual_bone = 'Forearm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.007"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.031"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -2.53073
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = -0.191986
        #=====
        actual_bone = 'Arm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.003"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.035"]
        #=====
        actual_bone = 'Forearm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.004"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.036"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = False
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = False
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0.191986
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 2.53073
        #=====
        actual_bone = 'Thigh_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.013"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.026"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.785398
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.174533
        #=====
        actual_bone = 'Leg_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.014"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.025"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Foot_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.019"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.022"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Thigh_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.010"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.029"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.785398

        actual_bone = 'Leg_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.011"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.030"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        actual_bone = 'Foot_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.022"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.019"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        print(len(s_list))
        bpy.context.scene.frame_end = len(s_list)

        bpy.ops.nla.bake(frame_start=1, frame_end=len(s_list), visual_keying=True, clear_constraints=True, clear_parents=True, bake_types={'POSE'})
        bpy.ops.object.mode_set(mode='OBJECT')



        #apagar collection points criada
        collection = bpy.data.collections.get('Point')
        #
        for obj in collection.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(collection)


        sk_value_prop = context.scene.sk_value_prop
        if raw_bool == True:
            print('raw_bool True - ',raw_bool)

            x_original, y_original, z_original = helper_functions.get_rotations()
            sk_value_prop.sk_root_rot_x = math.degrees(x_original)
            sk_value_prop.sk_root_rot_y = math.degrees(y_original)
            sk_value_prop.sk_root_rot_z = math.degrees(z_original)

            #in this case both original and actual is the same, because there was no alteration on the angle
            x_actual_deg = math.degrees(x_original)
            y_actual_deg = math.degrees(y_original)
            z_actual_deg = math.degrees(z_original)

            sk_value_prop.sk_root_actual_rot_x = x_actual_deg
            sk_value_prop.sk_root_actual_rot_y = y_actual_deg
            sk_value_prop.sk_root_actual_rot_z = z_actual_deg
        else:
            print('raw_bool False - ',raw_bool)
            x_deg, y_deg, z_deg = helper_functions.anim_to_origin()
            #take the information of the rotation to the panel
            print('result x: ',x_deg)
            print('result y: ',y_deg)
            print('result z: ',z_deg)
            sk_value_prop.sk_root_rot_x = x_deg
            sk_value_prop.sk_root_rot_y = y_deg
            sk_value_prop.sk_root_rot_z = z_deg


        #"""
        return{'FINISHED'}
        #"""


class Import_Data_vibe(Operator, ImportHelper):
    bl_idname = "mocap.import_vibe"
    bl_label = "Import data from Vibe (needs joblib install)"
    bl_description = "Import Vibe"


    filename_ext = ".pkl"

    filter_glob: StringProperty(
        default="*.pkl",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    def execute(self,context):



        #==========================
        #======VIBE

        #instalar joblib
        #D:\Blender\blender-2.92.0-windows64\2.92\python\bin\python.exe D:\Blender\blender-2.92.0-windows64\2.92\python\lib\site-packages\pip install joblib
        
   
        import math
        import bpy
        import os
        import pickle
        import numpy as np
        from bpy import context
        import joblib

        multiplier = context.scene.sk_value_prop.sk_value
        raw_bool = context.scene.sk_value_prop.sk_raw_bool

        def middle_point(p1,p2,p_middle):
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[p1].select_set(True)
            bpy.data.objects[p2].select_set(True)
            bpy.context.view_layer.objects.active = bpy.data.objects[p2]
            obs = bpy.context.selected_objects
            n = len(obs)
        #    print('n: ',n)
            assert(n)
            #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
            bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n


        def create_dots(name, amount):
            #remove Collection
            if bpy.data.collections.find(name) >= 0:
                collection = bpy.data.collections.get(name)
                #
                for obj in collection.objects:
                    bpy.data.objects.remove(obj, do_unlink=True)
                bpy.data.collections.remove(collection)
            #cria os pontos nuima collection chamada Points
            #=====================================================
            collection = bpy.data.collections.new(name)
            bpy.context.scene.collection.children.link(collection)
        #
            layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
            bpy.context.view_layer.active_layer_collection = layer_collection
        #
            for point in range(amount):
                bpy.ops.mesh.primitive_plane_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                bpy.ops.mesh.merge(type='CENTER')
                bpy.ops.object.editmode_toggle()
                bpy.context.active_object.name = name+'.'+str(1000+point)[1:]
            #=====================================================
            
        #==============================
        #codes to size the bones
        #==============================

        def distance(point1, point2) -> float: 
            #Calculate distance between two points in 3D.
        #    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)
            return math.sqrt((point2.location[0] - point1.location[0]) ** 2 + (point2.location[1] - point1.location[1]) ** 2 + (point2.location[2] - point1.location[2]) ** 2)


        def size_bone(point_name1, point_name2, bone):
            p1 = bpy.data.objects[point_name1]
            p2 = bpy.data.objects[point_name2]
            #edit bones
            if bpy.context.active_object.mode == 'EDIT':
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            else:
                bpy.ops.object.editmode_toggle()
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            bpy.ops.object.editmode_toggle()




        #path = r'D:\MOCAP\EasyMocap-master\demo_test\videos\1.mp4'
        #path = r'D:\Video_editing\running e brack dance para mocap.mp4'
        create_dots('Point',49)



        # pkl_path=r'D:\MOCAP\VIBE\output\sample_video\vibe_output.pkl'
        pkl_path=self.filepath
        pic = joblib.load(pkl_path)

        x=0
        y=1
        z=2


        person_id=1

        for item in range(len(pic[person_id]['pose'])):
            print("frame: ",item)
            final_limbs = int(len(pic[person_id]['pose'][item])/3)
            for limb in range(final_limbs):
                # print("limb: ",limb)
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[x]=pic[person_id]['joints3d'][item][limb][x]
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[y]=pic[person_id]['joints3d'][item][limb][y]
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[z]=pic[person_id]['joints3d'][item][limb][z]
                bpy.data.objects["Point."+str(1000+limb)[1:]].keyframe_insert(data_path="location", frame=item)



        import bpy


        #===========
        # selectign Scene Collection
        scene_collection = bpy.context.view_layer.layer_collection
        bpy.context.view_layer.active_layer_collection = scene_collection


        #===================================
        #creating bones
        #====================================

        bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) #cria armature e primeiro bone
        #bpy.ops.object.editmode_toggle()
        #bpy.data.armatures['Armature'].edit_bones.active = bpy.context.object.data.edit_bones['Bone']


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs


        bpy.ops.armature.select_all(action='DESELECT')
        #bpy.context.object.data.edit_bones['Bone'].select_tail=True
        obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True

        bpy.ops.armature.bone_primitive_add()#Spine
        #bpy.ops.armature.extrude_move()#Neck
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        ##bpy.ops.armature.extrude_move()#Face
        #bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        bpy.ops.armature.bone_primitive_add()#Arm_L
        #bpy.ops.armature.extrude_move()#Forearm_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Arm_R
        #bpy.ops.armature.extrude_move()#Forearm_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_L
        #bpy.ops.armature.extrude_move()#Leg_L
        #bpy.ops.armature.extrude_move()#Foot_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_R
        #bpy.ops.armature.extrude_move()#Leg_R
        #bpy.ops.armature.extrude_move()#Foot_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        obs[len(obs)-1].data.edit_bones["Bone"].name = 'Root'
        obs[len(obs)-1].data.edit_bones["Bone.001"].name = 'Spine'
        obs[len(obs)-1].data.edit_bones["Bone.002"].name = 'Neck'
        #obs[len(obs)-1].data.edit_bones["Bone.003"].name = 'Face'
        obs[len(obs)-1].data.edit_bones["Bone.003"].name = 'Arm_L'
        obs[len(obs)-1].data.edit_bones["Bone.004"].name = 'Forearm_L'
        obs[len(obs)-1].data.edit_bones["Bone.005"].name = 'Arm_R'
        obs[len(obs)-1].data.edit_bones["Bone.006"].name = 'Forearm_R'
        obs[len(obs)-1].data.edit_bones["Bone.007"].name = 'Thigh_L'
        obs[len(obs)-1].data.edit_bones["Bone.008"].name = 'Leg_L'
        obs[len(obs)-1].data.edit_bones["Bone.009"].name = 'Foot_L'
        obs[len(obs)-1].data.edit_bones["Bone.010"].name = 'Thigh_R'
        obs[len(obs)-1].data.edit_bones["Bone.011"].name = 'Leg_R'
        obs[len(obs)-1].data.edit_bones["Bone.012"].name = 'Foot_R'


        #Hierarquia
        bpy.context.object.data.edit_bones["Spine"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Arm_L"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Arm_R"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Thigh_L"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Thigh_R"].parent = bpy.context.object.data.edit_bones["Root"]

        bpy.ops.object.editmode_toggle()




        from mathutils import Vector
        import bpy

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Point.001'].select_set(True)
        bpy.data.objects['Point.008'].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects['Point.034']
        obs = bpy.context.selected_objects
        n = len(obs)
        #    print('n: ',n)
        assert(n)
        #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
        #bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n



        x_subtract = abs(obs[0].matrix_world.translation.x - obs[1].matrix_world.translation.x)
        y_subtract = abs(obs[0].matrix_world.translation.y - obs[1].matrix_world.translation.y)
        z_subtract = abs(obs[0].matrix_world.translation.z - obs[1].matrix_world.translation.z)

        max(x_subtract, y_subtract, z_subtract) #maior das medidas
        unit = max(x_subtract, y_subtract, z_subtract)/3
        unit = unit*multiplier

        root_sz    =unit/10
        spine_sz   =unit*3.5
        neck_sz    =unit
        face_sz    =unit
        thigh_sz    =unit*3
        leg_sz     =unit*2.5
        foot_sz    =unit #inclinado 45 graud pra frente
        arm_sz     =unit*1.5
        forearm_sz =unit*1.5



        #if bpy.context.active_object.mode != 'EDIT':
        #    bpy.ops.object.editmode_toggle()
        #==========================================
        #selecting and making the armature Active
        #selecionando armature
        #==========================================
        bpy.ops.object.select_all(action='DESELECT')
        #bpy.ops.armature.select_all(action='DESELECT')

        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        armature = obs[len(obs)-1].name

        #bpy.data.objects[armature].select_set(True)
        obs[len(obs)-1].select_set(True)
        view_layer = bpy.context.view_layer
        #Armature_obj = bpy.context.scene.objects[armature]
        Armature_obj = obs[len(obs)-1]
        view_layer.objects.active = Armature_obj

        #converting to euler rotation
        order = 'XYZ'
        context = bpy.context
        rig_object = context.active_object
        for pb in rig_object.pose.bones:
            pb.rotation_mode = order


        bpy.ops.object.editmode_toggle()

        #changing location
        #resetting
        bpy.context.object.data.edit_bones["Spine"].head.xy=0
        bpy.context.object.data.edit_bones["Neck"].head.xy=0
        #bpy.context.object.data.edit_bones["Face"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_L"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_R"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_L"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_L"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_R"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_R"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].head.xy=0
        #tail
        #bpy.context.object.data.edit_bones["Face"].tail.xy=0
        bpy.context.object.data.edit_bones["Neck"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].tail.xy=0




        bpy.context.object.data.edit_bones["Root"].length = root_sz

        bpy.context.object.data.edit_bones["Spine"].head.z = unit/2
        bpy.context.object.data.edit_bones["Spine"].tail.z = spine_sz

        bpy.context.object.data.edit_bones["Neck"].tail.z =  spine_sz + neck_sz
        bpy.context.object.data.edit_bones["Neck"].tail.y = neck_sz/3
        #bpy.context.object.data.edit_bones["Face"].tail.z = spine_sz + neck_sz
        #bpy.context.object.data.edit_bones["Face"].tail.y = face_sz*-1

        bpy.context.object.data.edit_bones["Arm_L"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Forearm_L"].head.z=  spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].head.x= unit + arm_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.x= unit + arm_sz + forearm_sz

        bpy.context.object.data.edit_bones["Arm_R"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_R"].head.x= (unit*3/4)*-1
        bpy.context.object.data.edit_bones["Forearm_R"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].head.x= (unit + arm_sz) *-1
        bpy.context.object.data.edit_bones["Forearm_R"].tail.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].tail.x= (unit + arm_sz + forearm_sz) *-1

        bpy.context.object.data.edit_bones["Thigh_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Thigh_L"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Leg_L"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.y= foot_sz/2*-1

        bpy.context.object.data.edit_bones["Thigh_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Thigh_R"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.y= foot_sz/2*-1

        bpy.ops.object.editmode_toggle()




        import bpy

        #comecando configuração  seguir movimentos pontos
        #colocando em pose mode


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.object.mode_set(mode='POSE')


        actual_bone = 'Root'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.008"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.001"]

        #====
        actual_bone = 'Spine'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.001"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x  = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.349066
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = -0.698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0.698132
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.174533

        #=====
        actual_bone = 'Neck'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.000"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.0472
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0.523599
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.349066
        #=====
        #actual_bone = 'Face'
        #obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        #obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        #bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.000"]
        #bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        #bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        ##x
        #bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        #bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        #bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.872665
        ##y
        #bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        #bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        #bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        ##z
        #bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        #bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.523599
        #bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.523599
        #=====
        actual_bone = 'Arm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.006"]
        #=====
        actual_bone = 'Forearm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.007"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -2.53073
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = -0.191986
        #=====
        actual_bone = 'Arm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.003"]
        #=====
        actual_bone = 'Forearm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.004"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = False
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = False
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0.191986
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 2.53073
        #=====
        actual_bone = 'Thigh_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.013"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.785398
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.174533
        #=====
        actual_bone = 'Leg_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.014"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Foot_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.019"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Thigh_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.010"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.785398

        actual_bone = 'Leg_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.011"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        actual_bone = 'Foot_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.022"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        bpy.context.scene.frame_end = len(pic[person_id]['pose'])

        bpy.ops.nla.bake(frame_start=1, frame_end=len(pic[person_id]['pose']), visual_keying=True, clear_constraints=True, clear_parents=True, bake_types={'POSE'})
        bpy.ops.object.mode_set(mode='OBJECT')

        #apagar collection points criada
        collection = bpy.data.collections.get('Point')
        #
        for obj in collection.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(collection)

        sk_value_prop = context.scene.sk_value_prop
        if raw_bool == True:
            print('raw_bool True - ',raw_bool)

            x_original, y_original, z_original = helper_functions.get_rotations()
            sk_value_prop.sk_root_rot_x = math.degrees(x_original)
            sk_value_prop.sk_root_rot_y = math.degrees(y_original)
            sk_value_prop.sk_root_rot_z = math.degrees(z_original)

            #in this case both original and actual is the same, because there was no alteration on the angle
            x_actual_deg = math.degrees(x_original)
            y_actual_deg = math.degrees(y_original)
            z_actual_deg = math.degrees(z_original)

            sk_value_prop.sk_root_actual_rot_x = x_actual_deg
            sk_value_prop.sk_root_actual_rot_y = y_actual_deg
            sk_value_prop.sk_root_actual_rot_z = z_actual_deg
        else:
            print('raw_bool False - ',raw_bool)
            x_deg, y_deg, z_deg = helper_functions.anim_to_origin()
            #take the information of the rotation to the panel
            print('result x: ',x_deg)
            print('result y: ',y_deg)
            print('result z: ',z_deg)
            sk_value_prop.sk_root_rot_x = x_deg
            sk_value_prop.sk_root_rot_y = y_deg
            sk_value_prop.sk_root_rot_z = z_deg


        
        

        return{'FINISHED'}

        
class Mediapipe_Pose_estimation(Operator, ImportHelper):
    bl_idname = "mocap.mediapipe_pose"
    bl_label = "Generate Pose using MediaPipe"
    bl_description = "Generate Mocap data with MediaPipe"


    filename_ext = ".mp4"

    filter_glob: StringProperty(
        default="*.mp4",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

        
    def execute(self,context):

        import cv2
        import mediapipe as mp
        import bpy
        import sys
        from mathutils import Vector
        import math

        multiplier = context.scene.sk_value_prop.sk_value
        raw_bool = context.scene.sk_value_prop.sk_raw_bool

        def middle_point(p1,p2,p_middle):
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[p1].select_set(True)
            bpy.data.objects[p2].select_set(True)
            bpy.context.view_layer.objects.active = bpy.data.objects[p2]
            obs = bpy.context.selected_objects
            n = len(obs)
        #    print('n: ',n)
            assert(n)
            #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
            bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n



        def get_landmarks(vid_name, frame_list):
            mp_drawing = mp.solutions.drawing_utils
            mp_holistic = mp.solutions.holistic
        #
            # For static images:
            holistic = mp_holistic.Holistic(static_image_mode=True)
            for idx, image in enumerate(frame_list):
        #        image_height, image_width, _ = image.shape
                # Convert the BGR image to RGB before processing.
                results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        #
        #
                x=0
                y=1
                z=2
                i=0
                print('frame: ',idx)
                try:
                    len(results.pose_landmarks.landmark)
                    for i in range(len(results.pose_landmarks.landmark)):
                        x_pose = results.pose_landmarks.landmark[i].x
                        y_pose = results.pose_landmarks.landmark[i].y
                        z_pose = results.pose_landmarks.landmark[i].z
                        bpy.data.objects["Point."+str(1000+i)[1:]].location[x]=x_pose
                        bpy.data.objects["Point."+str(1000+i)[1:]].location[y]=y_pose
                        bpy.data.objects["Point."+str(1000+i)[1:]].location[z]=z_pose
                        if i == 10:
                            middle_point('Point.009','Point.010','Point.033')
                            bpy.data.objects["Point."+str(1000+33)[1:]].keyframe_insert(data_path="location", frame=idx)
                        if i == 12:
                            middle_point('Point.011','Point.012','Point.034')
                            bpy.data.objects["Point."+str(1000+34)[1:]].keyframe_insert(data_path="location", frame=idx)
                        if i == 24:
                            middle_point('Point.023','Point.024','Point.035')
                            bpy.data.objects["Point."+str(1000+35)[1:]].keyframe_insert(data_path="location", frame=idx)
                        bpy.data.objects["Point."+str(1000+i)[1:]].keyframe_insert(data_path="location", frame=idx)
            #
        #                print('frame: ',idx,' landmark_id: ',i,'x: ', x_pose, ' - y: ',y_pose,' - z: ',z_pose)
                except:
                    print('Error Frame: ',idx)
                    bpy.data.objects["Point."+str(1000+i)[1:]].location[x]=0
                    bpy.data.objects["Point."+str(1000+i)[1:]].location[y]=0
                    bpy.data.objects["Point."+str(1000+i)[1:]].location[z]=0
                    bpy.data.objects["Point."+str(1000+i)[1:]].keyframe_insert(data_path="location", frame=idx)
                    continue
            holistic.close()


        def get_video_frames(file_url):
            vidcap = cv2.VideoCapture(file_url)
            success, image = vidcap.read()
            # array of objects with class 'numpy.ndarray'
            frames = []
            while success:
                frames.append(image)
                success, image = vidcap.read()
        #
            return frames

        def create_dots(name, amount):
            #remove Collection
            if bpy.data.collections.find(name) >= 0:
                collection = bpy.data.collections.get(name)
                #
                for obj in collection.objects:
                    bpy.data.objects.remove(obj, do_unlink=True)
                bpy.data.collections.remove(collection)
            #cria os pontos nuima collection chamada Points
            #=====================================================
            collection = bpy.data.collections.new(name)
            bpy.context.scene.collection.children.link(collection)
        #
            layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
            bpy.context.view_layer.active_layer_collection = layer_collection
        #
            for point in range(amount):
                bpy.ops.mesh.primitive_plane_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                bpy.ops.mesh.merge(type='CENTER')
                bpy.ops.object.editmode_toggle()
                bpy.context.active_object.name = name+'.'+str(1000+point)[1:]
            #=====================================================
            
        #==============================
        #codes to size the bones
        #==============================

        def distance(point1, point2) -> float: 
            #Calculate distance between two points in 3D.
        #    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)
            return math.sqrt((point2.location[0] - point1.location[0]) ** 2 + (point2.location[1] - point1.location[1]) ** 2 + (point2.location[2] - point1.location[2]) ** 2)


        def size_bone(point_name1, point_name2, bone):
            p1 = bpy.data.objects[point_name1]
            p2 = bpy.data.objects[point_name2]
            #edit bones
            if bpy.context.active_object.mode == 'EDIT':
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            else:
                bpy.ops.object.editmode_toggle()
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            bpy.ops.object.editmode_toggle()




        #path = r'D:\MOCAP\EasyMocap-master\demo_test\videos\1.mp4'
        # path = r'D:\Video_editing\running e brack dance para mocap.mp4'
        path = self.filepath
        create_dots('Point',36)
        get_landmarks('Name', get_video_frames(path))


        import bpy


        #===========
        # selectign Scene Collection
        scene_collection = bpy.context.view_layer.layer_collection
        bpy.context.view_layer.active_layer_collection = scene_collection


        #===================================
        #creating bones
        #====================================

        bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) #cria armature e primeiro bone
        #bpy.ops.object.editmode_toggle()
        #bpy.data.armatures['Armature'].edit_bones.active = bpy.context.object.data.edit_bones['Bone']


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs


        bpy.ops.armature.select_all(action='DESELECT')
        #bpy.context.object.data.edit_bones['Bone'].select_tail=True
        obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True

        bpy.ops.armature.bone_primitive_add()#Spine
        #bpy.ops.armature.extrude_move()#Neck
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        #bpy.ops.armature.extrude_move()#Face
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        bpy.ops.armature.bone_primitive_add()#Arm_L
        #bpy.ops.armature.extrude_move()#Forearm_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Arm_R
        #bpy.ops.armature.extrude_move()#Forearm_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_L
        #bpy.ops.armature.extrude_move()#Leg_L
        #bpy.ops.armature.extrude_move()#Foot_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_R
        #bpy.ops.armature.extrude_move()#Leg_R
        #bpy.ops.armature.extrude_move()#Foot_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        obs[len(obs)-1].data.edit_bones["Bone"].name = 'Root'
        obs[len(obs)-1].data.edit_bones["Bone.001"].name = 'Spine'
        obs[len(obs)-1].data.edit_bones["Bone.002"].name = 'Neck'
        obs[len(obs)-1].data.edit_bones["Bone.003"].name = 'Face'
        obs[len(obs)-1].data.edit_bones["Bone.004"].name = 'Arm_L'
        obs[len(obs)-1].data.edit_bones["Bone.005"].name = 'Forearm_L'
        obs[len(obs)-1].data.edit_bones["Bone.006"].name = 'Arm_R'
        obs[len(obs)-1].data.edit_bones["Bone.007"].name = 'Forearm_R'
        obs[len(obs)-1].data.edit_bones["Bone.008"].name = 'Thigh_L'
        obs[len(obs)-1].data.edit_bones["Bone.009"].name = 'Leg_L'
        obs[len(obs)-1].data.edit_bones["Bone.010"].name = 'Foot_L'
        obs[len(obs)-1].data.edit_bones["Bone.011"].name = 'Thigh_R'
        obs[len(obs)-1].data.edit_bones["Bone.012"].name = 'Leg_R'
        obs[len(obs)-1].data.edit_bones["Bone.013"].name = 'Foot_R'


        #Hierarquia
        bpy.context.object.data.edit_bones["Spine"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Arm_L"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Arm_R"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Thigh_L"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Thigh_R"].parent = bpy.context.object.data.edit_bones["Root"]

        bpy.ops.object.editmode_toggle()




        from mathutils import Vector
        import bpy

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Point.034'].select_set(True)
        bpy.data.objects['Point.035'].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects['Point.034']
        obs = bpy.context.selected_objects
        n = len(obs)
        #    print('n: ',n)
        assert(n)
        #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
        #bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n



        x_subtract = abs(obs[0].matrix_world.translation.x - obs[1].matrix_world.translation.x)
        y_subtract = abs(obs[0].matrix_world.translation.y - obs[1].matrix_world.translation.y)
        z_subtract = abs(obs[0].matrix_world.translation.z - obs[1].matrix_world.translation.z)

        max(x_subtract, y_subtract, z_subtract) #maior das medidas
        unit = max(x_subtract, y_subtract, z_subtract)/3
        unit = unit*multiplier

        root_sz    =unit/10
        spine_sz   =unit*3.5
        neck_sz    =unit
        face_sz    =unit
        thigh_sz    =unit*3
        leg_sz     =unit*2.5
        foot_sz    =unit #inclinado 45 graud pra frente
        arm_sz     =unit*1.5
        forearm_sz =unit*1.5



        #if bpy.context.active_object.mode != 'EDIT':
        #    bpy.ops.object.editmode_toggle()
        #==========================================
        #selecting and making the armature Active
        #selecionando armature
        #==========================================
        bpy.ops.object.select_all(action='DESELECT')
        #bpy.ops.armature.select_all(action='DESELECT')

        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        armature = obs[len(obs)-1].name

        #bpy.data.objects[armature].select_set(True)
        obs[len(obs)-1].select_set(True)
        view_layer = bpy.context.view_layer
        #Armature_obj = bpy.context.scene.objects[armature]
        Armature_obj = obs[len(obs)-1]
        view_layer.objects.active = Armature_obj


        #converting to euler rotation
        order = 'XYZ'
        context = bpy.context
        rig_object = context.active_object
        for pb in rig_object.pose.bones:
            pb.rotation_mode = order



        bpy.ops.object.editmode_toggle()

        #changing location
        #resetting
        bpy.context.object.data.edit_bones["Spine"].head.xy=0
        bpy.context.object.data.edit_bones["Neck"].head.xy=0
        bpy.context.object.data.edit_bones["Face"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_L"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_R"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_L"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_L"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_R"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_R"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].head.xy=0
        #tail
        bpy.context.object.data.edit_bones["Face"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].tail.xy=0




        bpy.context.object.data.edit_bones["Root"].length = root_sz

        bpy.context.object.data.edit_bones["Spine"].head.z = unit/2
        bpy.context.object.data.edit_bones["Spine"].tail.z = spine_sz

        bpy.context.object.data.edit_bones["Neck"].tail.z =  spine_sz + neck_sz
        bpy.context.object.data.edit_bones["Neck"].tail.y = neck_sz/3
        bpy.context.object.data.edit_bones["Face"].tail.z = spine_sz + neck_sz
        bpy.context.object.data.edit_bones["Face"].tail.y = face_sz*-1

        bpy.context.object.data.edit_bones["Arm_L"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_L"].head.x= unit/2
        bpy.context.object.data.edit_bones["Forearm_L"].head.z=  spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].head.x= unit + arm_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.x= unit + arm_sz + forearm_sz

        bpy.context.object.data.edit_bones["Arm_R"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_R"].head.x= (unit/2)*-1
        bpy.context.object.data.edit_bones["Forearm_R"].head.z= unit/2 + spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].head.x= (unit + arm_sz) *-1
        bpy.context.object.data.edit_bones["Forearm_R"].tail.z= unit/2 + spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].tail.x= (unit + arm_sz + forearm_sz) *-1

        bpy.context.object.data.edit_bones["Thigh_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Thigh_L"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Leg_L"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.y= foot_sz/2*-1

        bpy.context.object.data.edit_bones["Thigh_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Thigh_R"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.y= foot_sz/2*-1

        bpy.ops.object.editmode_toggle()

        import bpy

        #comecando configuração  seguir movimentos pontos
        #colocando em pose mode


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.object.mode_set(mode='POSE')


        actual_bone = 'Root'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.035"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.011"]

        #====
        actual_bone = 'Spine'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.011"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.012"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[2].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[2].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[2].min_x  = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[2].max_x = 0.349066
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[2].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[2].min_y = -0.698132
        bpy.context.object.pose.bones[actual_bone].constraints[2].max_y = 0.698132
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[2].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[2].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[2].max_z = 0.174533

        #=====
        actual_bone = 'Neck'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.033"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.0472
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0.523599
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.349066
        #=====
        actual_bone = 'Face'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.000"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.872665
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.523599
        #=====
        actual_bone = 'Arm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.013"]
        #=====
        actual_bone = 'Forearm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.015"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -2.53073
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = -0.191986
        #=====
        actual_bone = 'Arm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.014"]
        #=====
        actual_bone = 'Forearm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.016"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = False
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = False
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0.191986
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 2.53073
        #=====
        actual_bone = 'Thigh_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.025"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.785398
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.174533
        #=====
        actual_bone = 'Leg_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.027"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Foot_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.031"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Thigh_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.026"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.785398

        actual_bone = 'Leg_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.028"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        actual_bone = 'Foot_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.032"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        frames = len(get_video_frames(path))

        bpy.context.scene.frame_end = frames

        bpy.ops.nla.bake(frame_start=1, frame_end=frames, visual_keying=True, clear_constraints=True, clear_parents=True, bake_types={'POSE'})
        bpy.ops.object.mode_set(mode='OBJECT')



        #apagar collection points criada
        collection = bpy.data.collections.get('Point')
        #
        for obj in collection.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(collection)

        sk_value_prop = context.scene.sk_value_prop
        if raw_bool == True:
            print('raw_bool True - ',raw_bool)

            x_original, y_original, z_original = helper_functions.get_rotations()
            sk_value_prop.sk_root_rot_x = math.degrees(x_original)
            sk_value_prop.sk_root_rot_y = math.degrees(y_original)
            sk_value_prop.sk_root_rot_z = math.degrees(z_original)

            #in this case both original and actual is the same, because there was no alteration on the angle
            x_actual_deg = math.degrees(x_original)
            y_actual_deg = math.degrees(y_original)
            z_actual_deg = math.degrees(z_original)

            sk_value_prop.sk_root_actual_rot_x = x_actual_deg
            sk_value_prop.sk_root_actual_rot_y = y_actual_deg
            sk_value_prop.sk_root_actual_rot_z = z_actual_deg
        else:
            print('raw_bool False - ',raw_bool)
            x_deg, y_deg, z_deg = helper_functions.anim_to_origin()
            #take the information of the rotation to the panel
            print('result x: ',x_deg)
            print('result y: ',y_deg)
            print('result z: ',z_deg)
            sk_value_prop.sk_root_rot_x = x_deg
            sk_value_prop.sk_root_rot_y = y_deg
            sk_value_prop.sk_root_rot_z = z_deg



        return{'FINISHED'}


class Install_Mediapipe(bpy.types.Operator):
    bl_idname = "install.mediapipe_package"
    bl_label = "Install python Mediapipe Package"
    bl_description = "Install python Mediapipe Package"

    def execute(self,context):

        import subprocess
        import sys
        import os
        
        # path to python.exe
        python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
        
        # upgrade pip
        subprocess.call([python_exe, "-m", "ensurepip"])
        subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
        
        # install required packages
        subprocess.call([python_exe, "-m", "pip", "install", "mediapipe"])

        return{'FINISHED'}


class Install_Joblib(bpy.types.Operator):
    bl_idname = "install.joblib_package"
    bl_label = "Install python JobLib Package"
    bl_description = "Install python JobLib Package"

    def execute(self,context):

        import subprocess
        import sys
        import os
        
        # path to python.exe
        python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
        
        # upgrade pip
        subprocess.call([python_exe, "-m", "ensurepip"])
        subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
        
        # install required packages
        subprocess.call([python_exe, "-m", "pip", "install", "joblib"])

        return{'FINISHED'}

class Convert_axis(Operator):
    bl_idname = "mocap.convert_axis"
    bl_label = "Convert animation axis"
    bl_description = "Convert Axis"

    def execute(self,context):
        
        skvalue = context.scene.sk_value_prop

        print('from: ',skvalue.sk_from_axis,' ','to: ',skvalue.sk_to_axis)
        print('from simplified: ',skvalue.sk_from_axis[-1:],' ','to: ',skvalue.sk_to_axis[-1:])

        helper_functions.rotate_orientation(skvalue.sk_from_axis[-1:],skvalue.sk_to_axis[-1:])
        
        #send actual rotations
        x_actual_deg, y_actual_deg, z_actual_deg = helper_functions.get_rotations()
        skvalue.sk_root_actual_rot_x = math.degrees(x_actual_deg)
        skvalue.sk_root_actual_rot_y = math.degrees(y_actual_deg)
        skvalue.sk_root_actual_rot_z = math.degrees(z_actual_deg)
        return{'FINISHED'}

class Reset_location(Operator):
    bl_idname = "mocap.reset_location"
    bl_label = "Move animation to origin"
    bl_description = "Center Location"
    
    def execute(sel,context):
        helper_functions.reset_loc()
        return{'FINISHED'}

class Reset_rotation(Operator):
    bl_idname = "mocap.reset_rotation"
    bl_label = "Reset rotation, to the Rest rotatio position"
    bl_description = "Reset Rotation"
    
    def execute(sel,context):
        helper_functions.reset_rot()

        sk_value_prop = context.scene.sk_value_prop
        x_actual_deg, y_actual_deg, z_actual_deg = helper_functions.get_rotations()
        sk_value_prop.sk_root_actual_rot_x = math.degrees(x_actual_deg)
        sk_value_prop.sk_root_actual_rot_y = math.degrees(y_actual_deg)
        sk_value_prop.sk_root_actual_rot_z = math.degrees(z_actual_deg)
        return{'FINISHED'}

class Foot_high(Operator):
    bl_idname = "mocap.foot_high"
    bl_label = "Move the animation so the feet touch the floor"
    bl_description = "Move the feet to touch the floor"
    
    def execute(sel,context):
        helper_functions.foot_high()
        return{'FINISHED'}

class Compensate_Rotation(Operator):
    bl_idname = "mocap.compensate_rotation"
    bl_label = "compensate rotation"
    bl_description = "Compensate rotatio acording to value inserted"
    
    def execute(sel,context):
        skvalue = context.scene.sk_value_prop

        helper_functions.compensate_rot(skvalue.sk_rot_compens_x,skvalue.sk_rot_compens_y,skvalue.sk_rot_compens_z)
        return{'FINISHED'}