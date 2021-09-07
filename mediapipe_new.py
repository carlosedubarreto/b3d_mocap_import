
import bpy
# from bpy import context
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty,PointerProperty, IntProperty,FloatProperty
#from bpy.types import PropertyGroup
# from bpy.types import (Panel,
#                        Operator,
#                        AddonPreferences,
#                        PropertyGroup,
#                        )

import math
from mathutils import Quaternion,Vector
import cv2
import mediapipe as mp
import sys
import os
import glob

def middle_point(p1,p2,p_middle):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[p1].select_set(True)
    bpy.data.objects[p2].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects[p2]
    obs = bpy.context.selected_objects
    n = len(obs)
    #print('n: ',n)
    assert(n)
    #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
    bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n



def get_landmarks(point_name, frame_list):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    # For static images:
    pose = mp_pose.Pose(static_image_mode=True, model_complexity=2)
    for idx, image in enumerate(frame_list):
#        image_height, image_width, _ = image.shape
        # Convert the BGR image to RGB before processing.
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#
#
        x=0
        y=1
        z=2
        scale = 2
        z_depth = 0.5
        print('frame: ',idx)
        try:
            len(results.pose_landmarks.landmark)
            for i in range(len(results.pose_landmarks.landmark)):
#                x_pose = results.pose_landmarks.landmark[i].x
#                y_pose = results.pose_landmarks.landmark[i].y
#                z_pose = results.pose_landmarks.landmark[i].z
                x_pose = (0.5-results.pose_landmarks.landmark[i].x)*scale
                y_pose = (0.5-results.pose_landmarks.landmark[i].y)*scale
                z_pose = results.pose_landmarks.landmark[i].z*z_depth
                bpy.data.objects[point_name+"."+str(1000+i)[1:]].location[x]=x_pose
                bpy.data.objects[point_name+"."+str(1000+i)[1:]].location[y]=z_pose
                bpy.data.objects[point_name+"."+str(1000+i)[1:]].location[z]=y_pose
                if i == 10:
                    middle_point(point_name+'.009',point_name+'.010',point_name+'.033')
                    bpy.data.objects[point_name+"."+str(1000+33)[1:]].keyframe_insert(data_path="location", frame=idx)
                if i == 12:
                    middle_point(point_name+'.011',point_name+'.012',point_name+'.034')
                    bpy.data.objects[point_name+"."+str(1000+34)[1:]].keyframe_insert(data_path="location", frame=idx)
                if i == 24:
                    middle_point(point_name+'.023',point_name+'.024',point_name+'.035')
                    bpy.data.objects[point_name+"."+str(1000+35)[1:]].keyframe_insert(data_path="location", frame=idx)
                bpy.data.objects[point_name+"."+str(1000+i)[1:]].keyframe_insert(data_path="location", frame=idx)
    #
#                print('frame: ',idx,' landmark_id: ',i,'x: ', x_pose, ' - y: ',y_pose,' - z: ',z_pose)
        except:
            print('Error Frame: ',idx)
            bpy.data.objects[point_name+"."+str(1000+i)[1:]].location[x]=0
            bpy.data.objects[point_name+"."+str(1000+i)[1:]].location[y]=0
            bpy.data.objects[point_name+"."+str(1000+i)[1:]].location[z]=0
            bpy.data.objects[point_name+"."+str(1000+i)[1:]].keyframe_insert(data_path="location", frame=idx)
            continue
    pose.close()
    return idx


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



def create_bones(x,y,z):
    ##############################################
    #Bones
    ##############################################
    #===================================
    #creating bones
    #====================================
#    size_bonex=0.0
#    size_boney=0.1
#    size_bonez=0.0
    size_bonex=x
    size_boney=y
    size_bonez=z
    size_radius=0.1
    #
    sb_shoulder_y = size_boney*0.33
    sb_upper_arm_y = size_boney*0.52
    sb_arm_y = size_boney*0.48
    sb_hand_y = size_boney*0.15
    sb_head_y = size_boney*0.19
    sb_neck_y = size_boney*0.33
    sb_spine_y = size_boney*1.05
    sb_pelvis_y = size_boney*0.18
    sb_shin_y = size_boney*0.83
    sb_foot_y = size_boney*0.37
    #Root
    bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', 
        radius=size_radius, location=(0, 0, 0), scale=(1, 1, 1), rotation=(math.radians(-90), 0.0, 0.0))

    #Pelvis_R
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_pelvis_y, size_bonez)})
    #Thigh_R
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney, size_bonez)})
    #Shin_R
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_shin_y, size_bonez)})
    #Foot_R
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_foot_y, size_bonez)})

    obs = []
    for ob in bpy.context.scene.objects:
        if ob.type == 'ARMATURE':
            obs.append(ob)
    #obs
    bpy.ops.armature.select_all(action='DESELECT')
    obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True

    #Pelvis_L
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_pelvis_y, size_bonez)})
    #Thigh_L
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney, size_bonez)})
    #Shin_L
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_shin_y, size_bonez)})
    #Foot_L
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_foot_y, size_bonez)})

    obs = []
    for ob in bpy.context.scene.objects:
        if ob.type == 'ARMATURE':
            obs.append(ob)
    #obs
    bpy.ops.armature.select_all(action='DESELECT')
    obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True

    #Spine
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_spine_y, size_bonez)})
    #Neck
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_neck_y, size_bonez)})
    #Head
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_head_y, size_bonez)})


    obs = []
    for ob in bpy.context.scene.objects:
        if ob.type == 'ARMATURE':
            obs.append(ob)
    #obs
    bpy.ops.armature.select_all(action='DESELECT')
    obs[len(obs)-1].data.edit_bones['Bone.009'].select_tail=True

    #Shoulder_R
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_shoulder_y, size_bonez)})
    #Upperarm_R
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_upper_arm_y, size_bonez)})
    #Forearm_R
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_arm_y, size_bonez)})
    #Hand_R
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_hand_y, size_bonez)})

    obs = []
    for ob in bpy.context.scene.objects:
        if ob.type == 'ARMATURE':
            obs.append(ob)
    #obs
    bpy.ops.armature.select_all(action='DESELECT')
    obs[len(obs)-1].data.edit_bones['Bone.009'].select_tail=True

    #Shoulder_L
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_shoulder_y, size_bonez)})
    #Upperarm_L
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_upper_arm_y, size_bonez)})
    #Forearm_L
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_arm_y, size_bonez)})
    #Hand_L
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, sb_hand_y, size_bonez)})

    bones_list = [['Bone','Root'],
            ['Bone.001','Pelvis_R'],
            ['Bone.002','Thigh_R'],
            ['Bone.003','Shin_R'],
            ['Bone.004','Foot_R'],
            ['Bone.005','Pelvis_L'],
            ['Bone.006','Thigh_L'],
            ['Bone.007','Shin_L'],
            ['Bone.008','Foot_L'],
            ['Bone.009','Spine'],
            ['Bone.010','Neck'],
            ['Bone.011','Head'],
            ['Bone.012','Shoulder_R'],
            ['Bone.013','Upperarm_R'],
            ['Bone.014','Forearm_R'],
            ['Bone.015','Hand_R'],
            ['Bone.016','Shoulder_L'],
            ['Bone.017','Upperarm_L'],
            ['Bone.018','Forearm_L'],
            ['Bone.019','Hand_L']
            ]



    for i in range(len(bones_list)):
        obs[len(obs)-1].data.edit_bones[bones_list[i][0]].name = bones_list[i][1]

    bpy.ops.object.editmode_toggle()

    #Name of Bone, orginal name, point of headbone, point of tailbone

    bones_list = {'Root': ['Bone',35],
            'Pelvis_R': ['Bone.001',35,23],
            'Tigh_R': ['Bone.002',23,25],
            'Shin_R': ['Bone.003',25,27],
            'Foot_R': ['Bone.004',27,31],
            'Pelvis_L': ['Bone.005',35,24],
            'Thigh_L': ['Bone.006',24,26],
            'Shin_L': ['Bone.007',26,28],
            'Foot_L': ['Bone.008',28,32],
            'Spine': ['Bone.009',35,34],
            'Neck': ['Bone.010',34,33],
            'Head': ['Bone.011',33,0],
            'Should_R': ['Bone.012',34,11],
            'Upperarm_R': ['Bone.013',11,13],
            'Forearm_R': ['Bone.014',13,15],
            'Hand_R': ['Bone.015',15,19],
            'Shoulder_L': ['Bone.016',34,12],
            'Upperarm_L': ['Bone.017',12,14],
            'Forearm_L': ['Bone.018',14,16],
            'Hand_L': ['Bone.019',16,20]
            }
        
    #como aplicar look no dict    
#    for b in bones_list:
#        print('conteudo',bones_list[b],'prim:',bones_list[b][0])
    return {'FINISHED'}
        
#This code was created to copy the angle between 2 points
#And transfer it to a Bone


def last_armature():
    obs = []
    for ob in bpy.context.scene.objects:
        if ob.type == 'ARMATURE':
            obs.append(ob)
    return obs[len(obs)-1]


def cp_bone_rot(armature,i,bone_name,point_name,pt1,pt2,prev_rot):
    ptn1 = point_name+'.{0:03d}'.format(pt1)
    ptn2 = point_name+'.{0:03d}'.format(pt2)
    eq1 = bpy.data.objects[ptn1].location
    eq2 = bpy.data.objects[ptn2].location
    #
    pt_ini_x =eq1.x
    pt_ini_y =eq1.y
    pt_ini_z =eq1.z
    #
    eq1.x = eq1.x - pt_ini_x
    #eq1.y = eq1.y - pt_ini_y
    eq1.z = eq1.z - pt_ini_z
    #
    eq2.x = eq2.x - pt_ini_x
    #eq2.y = eq2.y - pt_ini_y
    eq2.z = eq2.z - pt_ini_z   
    #
    #arm = bpy.context.scene.objects['Armature_multi']
#    arm = last_armature()
    arm = armature
    bone = arm.pose.bones[bone_name]
    #
    if eq1.y >=0:
        rot_quaternion = eq1.rotation_difference(eq2-eq1)
    else:
        rot_quaternion = eq1.rotation_difference(eq1-eq2)
    #
    eq1.x = eq1.x + pt_ini_x
    #eq1.y = eq1.y + pt_ini_y
    eq1.z = eq1.z + pt_ini_z
    #
    eq2.x = eq2.x + pt_ini_x
    #eq2.y = eq2.y + pt_ini_y
    eq2.z = eq2.z + pt_ini_z
    #
    if i == 0:
        bone.rotation_quaternion = rot_quaternion
    else:
        rot_qua_ajust = prev_rot.rotation_difference(rot_quaternion)
        bone.rotation_quaternion = rot_qua_ajust
    #rot_quaternion_prev = rot_quaternion
#    print(bone_name," W: %.2f, X: %.2f, Y: %.2f, Z: %.2f" % tuple(math.degrees(a) for a in rot_quaternion))
    #
    return rot_quaternion

########################
### Hand Code

def get_landmarks_hands(vid_name, frame_list):
    left= 0
    right=1
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
#
    # For static images:
#    holistic = mp_holistic.Holistic(static_image_mode=True)
    hands =  mp_hands.Hands(static_image_mode=True,max_num_hands=2,min_detection_confidence=0.5)
    for idx, image in enumerate(frame_list):
#        image_height, image_width, _ = image.shape
        # Read an image, flip it around y-axis for correct handedness output
#        image = cv2.flip(cv2.imread(image), 1)
        # Convert the BGR image to RGB before processing.
#        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        results = hands.process(cv2.cvtColor(cv2.flip(image,0), cv2.COLOR_BGR2RGB))
        print('Handedness:', results.multi_handedness)
        if not results.multi_hand_landmarks:
            continue
#
        x=0
        y=1
        z=2
        scale = 2
        z_depth = 0.5
        print('frame: ',idx)
        for r in range(len(results.multi_handedness)):
            if results.multi_handedness[r].classification[0].index == left:
#                print('len multihand:',len(results.multi_hand_landmarks))
#                len(results.multi_hand_landmarks[0].landmark)
                for i in range(len(results.multi_hand_landmarks[r].landmark)):
                    x_pose = results.multi_hand_landmarks[r].landmark[i].x
                    y_pose = results.multi_hand_landmarks[r].landmark[i].y
                    z_pose = results.multi_hand_landmarks[r].landmark[i].z
#                    x_pose = (0.5-results.multi_hand_landmarks[r].landmark[i].x)*scale
#                    y_pose = (0.5-results.multi_hand_landmarks[r].landmark[i].y)*scale
#                    z_pose = results.multi_hand_landmarks[r].landmark[i].z*z_depth
                    bpy.data.objects["Left."+str(1000+i)[1:]].location[x]=x_pose
                    bpy.data.objects["Left."+str(1000+i)[1:]].location[y]=z_pose
                    bpy.data.objects["Left."+str(1000+i)[1:]].location[z]=y_pose
                    bpy.data.objects["Left."+str(1000+i)[1:]].keyframe_insert(data_path="location", frame=idx)
            else:
#                print('len multihand:',len(results.multi_hand_landmarks))
#                len(results.multi_hand_landmarks[0].landmark)
                for i in range(len(results.multi_hand_landmarks[r].landmark)):
                    x_pose = results.multi_hand_landmarks[r].landmark[i].x
                    y_pose = results.multi_hand_landmarks[r].landmark[i].y
                    z_pose = results.multi_hand_landmarks[r].landmark[i].z
                    bpy.data.objects["Right."+str(1000+i)[1:]].location[x]=x_pose
                    bpy.data.objects["Right."+str(1000+i)[1:]].location[y]=z_pose
                    bpy.data.objects["Right."+str(1000+i)[1:]].location[z]=y_pose
                    bpy.data.objects["Right."+str(1000+i)[1:]].keyframe_insert(data_path="location", frame=idx)
    hands.close()
    return idx

def create_hand_bones(side):
    ##############################################
    #Bones
    ##############################################
    #===================================
    #creating bones
    #====================================
    size_bonex=0.0
    size_boney=0.02
    size_bonez=0.0
    size_radius=0.1
    #
    #Root
    bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', 
        radius=size_radius, location=(0, 0, 0), scale=(1, 1, 1), rotation=(math.radians(-90), 0.0, 0.0))
    #Thumb_cmc
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*1.8, size_bonez)})
    #Thumb_mcp
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*2.1, size_bonez)})
    #Thumb_IP
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*1.5, size_bonez)})
    #Thumb_tip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney, size_bonez)})
    obs = []
    for ob in bpy.context.scene.objects:
        if ob.type == 'ARMATURE':
            obs.append(ob)
    #obs
    bpy.ops.armature.select_all(action='DESELECT')
    obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True
    #Index_mcp
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*4.3, size_bonez)})
    #Index_pip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*2.5, size_bonez)})
    #Index_dip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*1.4, size_bonez)})
    #Index_tip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney, size_bonez)})
    obs = []
    for ob in bpy.context.scene.objects:
        if ob.type == 'ARMATURE':
            obs.append(ob)
    #obs
    bpy.ops.armature.select_all(action='DESELECT')
    obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True
    #Middle_mcp
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*3.7, size_bonez)})
    #Middle_pip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*2.6, size_bonez)})
    #Middle_dip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*1.5, size_bonez)})
    #Middle_tip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney, size_bonez)})
    obs = []
    for ob in bpy.context.scene.objects:
        if ob.type == 'ARMATURE':
            obs.append(ob)
    #obs
    bpy.ops.armature.select_all(action='DESELECT')
    obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True
    #Ring_mcp
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*3.4, size_bonez)})
    #Ring_pip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*2.4, size_bonez)})
    #Ring_dip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*1.5, size_bonez)})
    #Ring_tip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney, size_bonez)})
    obs = []
    for ob in bpy.context.scene.objects:
        if ob.type == 'ARMATURE':
            obs.append(ob)
    #obs
    bpy.ops.armature.select_all(action='DESELECT')
    obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True
    #Pinky_mcp
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*3.4, size_bonez)})
    #Pinky_pip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*2.1, size_bonez)})
    #Pinky_dip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney*1.1, size_bonez)})
    #Pinky_tip
    bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, 
        TRANSFORM_OT_translate={"value":(size_bonex, size_boney, size_bonez)})
    if side == 'L' :
        bones_list = [['Bone','Root_L'],
                ['Bone.001','Thumb_cmc_L'],
                ['Bone.002','Thumb_mcp_L'],
                ['Bone.003','Thumb_IP_L'],
                ['Bone.004','Thumb_tip_L'],
                ['Bone.005','Index_mcp_L'],
                ['Bone.006','Index_pip_L'],
                ['Bone.007','Index_dip_L'],
                ['Bone.008','Index_tip_L'],
                ['Bone.009','Middle_mcp_L'],
                ['Bone.010','Middle_pip_L'],
                ['Bone.011','Middle_dip_L'],
                ['Bone.012','Middle_tip_L'],
                ['Bone.013','Ring_mcp_L'],
                ['Bone.014','Ring_pip_L'],
                ['Bone.015','Ring_dip_L'],
                ['Bone.016','Ring_tip_L'],
                ['Bone.017','Pinky_mcp_L'],
                ['Bone.018','Pinky_pip_L'],
                ['Bone.019','Pinky_dip_L'],
                ['Bone.020','Pinky_tip_L']
                ]
    else:
        bones_list = [['Bone','Root_R'],
            ['Bone.001','Thumb_cmc_R'],
            ['Bone.002','Thumb_mcp_R'],
            ['Bone.003','Thumb_IP_R'],
            ['Bone.004','Thumb_tip_R'],
            ['Bone.005','Index_mcp_R'],
            ['Bone.006','Index_pip_R'],
            ['Bone.007','Index_dip_R'],
            ['Bone.008','Index_tip_R'],
            ['Bone.009','Middle_mcp_R'],
            ['Bone.010','Middle_pip_R'],
            ['Bone.011','Middle_dip_R'],
            ['Bone.012','Middle_tip_R'],
            ['Bone.013','Ring_mcp_R'],
            ['Bone.014','Ring_pip_R'],
            ['Bone.015','Ring_dip_R'],
            ['Bone.016','Ring_tip_R'],
            ['Bone.017','Pinky_mcp_R'],
            ['Bone.018','Pinky_pip_R'],
            ['Bone.019','Pinky_dip_R'],
            ['Bone.020','Pinky_tip_R']
            ]
    for i in range(len(bones_list)):
        obs[len(obs)-1].data.edit_bones[bones_list[i][0]].name = bones_list[i][1]
    bpy.ops.object.editmode_toggle()
    #Name of Bone, orginal name, point of headbone, point of tailbone
    if side == 'L':
        bones_list = {'Root_L': ['Bone',0],
                'Thumb_cmc_L': ['Bone.001',0,1],
                'Thumb_mcp_L': ['Bone.002',1,2],
                'Thumb_IP_L': ['Bone.003',2,3],
                'Thumb_tip_L': ['Bone.004',3,4],
                'Index_mcp_L': ['Bone.005',0,5],
                'Index_pip_L': ['Bone.006',5,6],
                'Index_dip_L': ['Bone.007',6,7],
                'Index_tip_L': ['Bone.008',7,8],
                'Middle_mcp_L': ['Bone.009',0,9],
                'Middle_pip_L': ['Bone.010',9,10],
                'Middle_dip_L': ['Bone.011',10,11],
                'Middle_tip_L': ['Bone.012',11,12],
                'Ring_mcp_L': ['Bone.013',0,13],
                'Ring_pip_L': ['Bone.014',13,14],
                'Ring_dip_L': ['Bone.015',14,15],
                'Ring_tip_L': ['Bone.016',15,16],
                'Pinky_mcp_L': ['Bone.017',0,17],
                'Pinky_pip_L': ['Bone.018',17,18],
                'Pinky_dip_L': ['Bone.019',18,19],
                'Pinky_tip_L': ['Bone.020',19,20]
                }
    else:
        bones_list = {'Root_R': ['Bone',0],
                'Thumb_cmc_R': ['Bone.001',0,1],
                'Thumb_mcp_R': ['Bone.002',1,2],
                'Thumb_IP_R': ['Bone.003',2,3],
                'Thumb_tip_R': ['Bone.004',3,4],
                'Index_mcp_R': ['Bone.005',0,5],
                'Index_pip_R': ['Bone.006',5,6],
                'Index_dip_R': ['Bone.007',6,7],
                'Index_tip_R': ['Bone.008',7,8],
                'Middle_mcp_R': ['Bone.009',0,9],
                'Middle_pip_R': ['Bone.010',9,10],
                'Middle_dip_R': ['Bone.011',10,11],
                'Middle_tip_R': ['Bone.012',11,12],
                'Ring_mcp_R': ['Bone.013',0,13],
                'Ring_pip_R': ['Bone.014',13,14],
                'Ring_dip_R': ['Bone.015',14,15],
                'Ring_tip_R': ['Bone.016',15,16],
                'Pinky_mcp_R': ['Bone.017',0,17],
                'Pinky_pip_R': ['Bone.018',17,18],
                'Pinky_dip_R': ['Bone.019',18,19],
                'Pinky_tip_R': ['Bone.020',19,20]
                }
    #como aplicar look no dict    
    for b in bones_list:
        print('conteudo',bones_list[b],'prim:',bones_list[b][0])
    return {'FINISHED'}

def last_n_armature(n):
    obs = []
    for ob in bpy.context.scene.objects:
        if ob.type == 'ARMATURE':
            obs.append(ob)
    return obs[len(obs)-n]

  
class MP_preview(bpy.types.Operator,ImportHelper):
    bl_idname = "view3d.mp_preview_load"
    bl_label = "Selection Box"
    bl_description = "Goes back to selection box"

    filename_ext = ".mp4"

    filter_glob: StringProperty(
        default="*.mp4",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )


    def execute(self, context):
#        area = [area for area in bpy.context.screen.areas if area.type == "VIEW_3D"][0]
#        override_context = bpy.context.copy()
#        override_context['window'] = bpy.context.window
#        override_context['screen'] = bpy.context.screen
#        override_context['area'] = area
#        override_context['region'] = area.regions[-1]
#        override_context['scene'] = bpy.context.scene
#        override_context['space_data'] = area.spaces.active

#        bpy.ops.wm.tool_set_by_id(override_context, name='builtin.select_box')




        #bone list columns:
        #Bone Name, original bone name, point1, point2, prev_rotation_ref
        bones_list = {
                'Root': ['Bone',35], #rot number: 0
                'Pelvis_R': ['Bone.001',35,23,0], #rot number: 1
                'Thigh_R': ['Bone.002',23,25,1], #rot number:2
                'Shin_R': ['Bone.003',25,27,2], #rot number: 3
                'Foot_R': ['Bone.004',27,31,3],  #rot number: 4
                'Pelvis_L': ['Bone.005',35,24,0], #rot number: 5
                'Thigh_L': ['Bone.006',24,26,5], #rot number: 6
                'Shin_L': ['Bone.007',26,28,6], #rot number: 7
                'Foot_L': ['Bone.008',28,32,7], #rot number: 8
                'Spine': ['Bone.009',35,34,0], #rot number: 9
                'Neck': ['Bone.010',34,33,9], #rot number: 10
                'Head': ['Bone.011',33,0,10], #rot number: 11
                'Shoulder_R': ['Bone.012',34,11,9], #rot number: 12
                'Upperarm_R': ['Bone.013',11,13,12], #rot number: 13
                'Forearm_R': ['Bone.014',13,15,13], #rot number: 14
                'Hand_R': ['Bone.015',15,19,14], #rot number: 15
                'Shoulder_L': ['Bone.016',34,12,9], #rot number: 16
                'Upperarm_L': ['Bone.017',12,14,16], #rot number: 17
                'Forearm_L': ['Bone.018',14,16,17], #rot number: 18
                'Hand_L': ['Bone.019',16,20,18] #rot number: 19
                }


        ###### Change the path to you video on the line below.
        ##########################################
        path =  self.filepath
        #path = r'C:\MOCAP\VIDEOS\wal_stardar_male_side.mp4'
        #path = r'C:\MOCAP\VIDEOS\sit_menor.mp4'
        #path = r'C:\MOCAP\frankmocap\sampledata\single_totalbody.mp4'
        ##########################################


        
        #checks if path is a file
        isFile = os.path.isfile(path)
        #checks if path is a directory
#        isDirectory = os.path.isdir(path)

        if isFile:
            video_files = [path]
        else:
            video_files = glob.glob(os.path.dirname(path)+"/*.mp4")
        
        
        for file in video_files:
            path = file
    #        point_name='Point'
    #        point_name = context.scene.sk_value_prop.sk_point_name
            point_name = os.path.splitext(os.path.basename(path))[0]
            print("name video",point_name)
            bone_sz = context.scene.sk_value_prop.sk_bone_sz

            create_dots(point_name,36)
            frames = get_landmarks(point_name, get_video_frames(path))
            bpy.context.scene.frame_end = frames
            print('Total of Frames: ',frames)
            # context.scene.sk_value_prop.sk_frame_str = 'Total of Frames: '+str(frames)
            create_bones(0.0,bone_sz,0.0)

            ###Map the bones to the points
            arm = last_armature()
            for f in range(frames):
                bpy.context.scene.frame_set(f)
    #            print('Frame: ',f)
                rot_hist_list=[Quaternion((1.0, 0.0, 0.0, 0.0))]
                for i,o in enumerate(bones_list):
                    if len(bones_list[o]) == 2:
                        actual_bone = arm.pose.bones[o]
    #                    print(i,'-',o,'-',bones_list[o][1])
                        pt_obj1 = point_name+'.{0:03d}'.format(bones_list[o][1])
                        actual_bone.location = bpy.data.objects[pt_obj1].location
                        actual_bone.keyframe_insert(data_path='location',frame=f)
                    else:
                        actual_bone = arm.pose.bones[o]
                        point1 = bones_list[o][1]
                        point2 = bones_list[o][2]
                        idx_rot_history = bones_list[o][3]
                        rot_history = rot_hist_list[idx_rot_history]
    #                    print(i,'-',o,'-',point1,'-',point1,'hist: ',rot_history)
                        rot_quat = cp_bone_rot(arm,i,o,point_name,point1,point2,rot_history)
                        rot_hist_list.append(rot_quat)
                        actual_bone.keyframe_insert(data_path='rotation_quaternion',frame=f)


        return{'FINISHED'} 


class update_bone_size(bpy.types.Operator):
    bl_idname = "view3d.update_bone_size"
    bl_label = "Update Bone Size"
    bl_description = "Update Bone Size"


    def execute(self, context):
        point_name = context.scene.sk_value_prop.sk_point_name
        bone_sz = context.scene.sk_value_prop.sk_bone_sz
        
        arm = last_armature()
        arm.select_set(True)
        bpy.ops.object.delete(use_global=False, confirm=False)
        
        create_bones(0.0,bone_sz,0.0)
        arm = last_armature()
        frames =  bpy.context.scene.frame_end
        
        bones_list = {
                'Root': ['Bone',35], #rot number: 0
                'Pelvis_R': ['Bone.001',35,23,0], #rot number: 1
                'Thigh_R': ['Bone.002',23,25,1], #rot number:2
                'Shin_R': ['Bone.003',25,27,2], #rot number: 3
                'Foot_R': ['Bone.004',27,31,3],  #rot number: 4
                'Pelvis_L': ['Bone.005',35,24,0], #rot number: 5
                'Thigh_L': ['Bone.006',24,26,5], #rot number: 6
                'Shin_L': ['Bone.007',26,28,6], #rot number: 7
                'Foot_L': ['Bone.008',28,32,7], #rot number: 8
                'Spine': ['Bone.009',35,34,0], #rot number: 9
                'Neck': ['Bone.010',34,33,9], #rot number: 10
                'Head': ['Bone.011',33,0,10], #rot number: 11
                'Shoulder_R': ['Bone.012',34,11,9], #rot number: 12
                'Upperarm_R': ['Bone.013',11,13,12], #rot number: 13
                'Forearm_R': ['Bone.014',13,15,13], #rot number: 14
                'Hand_R': ['Bone.015',15,19,14], #rot number: 15
                'Shoulder_L': ['Bone.016',34,12,9], #rot number: 16
                'Upperarm_L': ['Bone.017',12,14,16], #rot number: 17
                'Forearm_L': ['Bone.018',14,16,17], #rot number: 18
                'Hand_L': ['Bone.019',16,20,18] #rot number: 19
                }
        
        for f in range(frames):
            bpy.context.scene.frame_set(f)
            print('Frame: ',f)
            rot_hist_list=[Quaternion((1.0, 0.0, 0.0, 0.0))]
            for i,o in enumerate(bones_list):
                if len(bones_list[o]) == 2:
                    actual_bone = arm.pose.bones[o]
#                    print(i,'-',o,'-',bones_list[o][1])
                    pt_obj1 = point_name+'.{0:03d}'.format(bones_list[o][1])
                    actual_bone.location = bpy.data.objects[pt_obj1].location
                    actual_bone.keyframe_insert(data_path='location',frame=f)
                else:
                    actual_bone = arm.pose.bones[o]
                    point1 = bones_list[o][1]
                    point2 = bones_list[o][2]
                    idx_rot_history = bones_list[o][3]
                    rot_history = rot_hist_list[idx_rot_history]
#                    print(i,'-',o,'-',point1,'-',point1,'hist: ',rot_history)
                    rot_quat = cp_bone_rot(arm,i,o,point_name,point1,point2,rot_history)
                    rot_hist_list.append(rot_quat)
                    actual_bone.keyframe_insert(data_path='rotation_quaternion',frame=f)
        
        
  
        return{'FINISHED'} 



class Transfer_Angles(bpy.types.Operator):
    bl_idname = "view3d.retarget_selected"
    bl_label = "Retarget Selected"
    bl_description = "Retarget Selected Pair of Bones"


    def execute(self, context):

        #first(origim) selected bone: s_bones[1]
        #second(last) selected bone: s_bones[0]
        bone_ori = bpy.context.selected_pose_bones[1]
        bone_dest= bpy.context.selected_pose_bones[0]
        #mp_armature = bpy.context.scene.objects['Armature']
        #A ideia e colocar o bone na rodacao desejada e que seja usada
        #como referencia para pegar a diferenca e cplicar no bone destino
        pbone = bone_ori.rotation_quaternion
        scw = pbone.w
        scx = pbone.x
        scy = pbone.y
        scz = pbone.z
        #
        #this will save the rotation not keyfreamed
        quat_ref=Quaternion((scw,scx,scy,scz))
    #    print('bone_orig: ',bone_ori,' Q: ',quat_ref)
        #
        #rigify_armature = bpy.context.scene.objects['metarig']
        #name = 'upper_arm.L'
        #name_end = b[1]
        bpy.context.scene.frame_current = bpy.context.scene.frame_current
        sk_start_frame = context.scene.sk_value_prop.sk_start_frame
        sk_end_frame = context.scene.sk_value_prop.sk_end_frame
        bpy.context.scene.frame_start = sk_start_frame
        bpy.context.scene.frame_end = sk_end_frame
        for f in range(sk_start_frame,sk_end_frame+1):
            bpy.context.scene.frame_set(f)
        #        rigify_armature.pose.bones[name_end].rotation_quaternion = quat_ref[name_ini].rotation_difference(pbone)
        #        rigify_armature.pose.bones[name_end].keyframe_insert(data_path='rotation_quaternion',frame=f)
            bone_dest.rotation_quaternion = quat_ref.rotation_difference(pbone)
            bone_dest.keyframe_insert(data_path='rotation_quaternion',frame=f)
        return {'FINISHED'}
    

class Hand_mocap(bpy.types.Operator,ImportHelper):
    bl_idname = "view3d.hand_mocap"
    bl_label = "Hand Mocap"
    bl_description = "Hand Mocap"

    filename_ext = ".mp4"

    filter_glob: StringProperty(
        default="*.mp4",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )


    def execute(self, context):
        bones_list_l = {'Root_L': ['Bone',0],
                'Thumb_cmc_L': ['Bone.001',0,1,0],
                'Thumb_mcp_L': ['Bone.002',1,2,1],
                'Thumb_IP_L': ['Bone.003',2,3,2],
                'Thumb_tip_L': ['Bone.004',3,4,3],
                'Index_mcp_L': ['Bone.005',0,5,0],
                'Index_pip_L': ['Bone.006',5,6,5],
                'Index_dip_L': ['Bone.007',6,7,6],
                'Index_tip_L': ['Bone.008',7,8,7],
                'Middle_mcp_L': ['Bone.009',0,9,0],
                'Middle_pip_L': ['Bone.010',9,10,9],
                'Middle_dip_L': ['Bone.011',10,11,10],
                'Middle_tip_L': ['Bone.012',11,12,11],
                'Ring_mcp_L': ['Bone.013',0,13,0],
                'Ring_pip_L': ['Bone.014',13,14,13],
                'Ring_dip_L': ['Bone.015',14,15,14],
                'Ring_tip_L': ['Bone.016',15,16,15],
                'Pinky_mcp_L': ['Bone.017',0,17,0],
                'Pinky_pip_L': ['Bone.018',17,18,17],
                'Pinky_dip_L': ['Bone.019',18,19,18],
                'Pinky_tip_L': ['Bone.020',19,20,19]
                }

        bones_list_r = {'Root_R': ['Bone',0],
                'Thumb_cmc_R': ['Bone.001',0,1,0],
                'Thumb_mcp_R': ['Bone.002',1,2,1],
                'Thumb_IP_R': ['Bone.003',2,3,2],
                'Thumb_tip_R': ['Bone.004',3,4,3],
                'Index_mcp_R': ['Bone.005',0,5,0],
                'Index_pip_R': ['Bone.006',5,6,5],
                'Index_dip_R': ['Bone.007',6,7,6],
                'Index_tip_R': ['Bone.008',7,8,7],
                'Middle_mcp_R': ['Bone.009',0,9,0],
                'Middle_pip_R': ['Bone.010',9,10,9],
                'Middle_dip_R': ['Bone.011',10,11,10],
                'Middle_tip_R': ['Bone.012',11,12,11],
                'Ring_mcp_R': ['Bone.013',0,13,0],
                'Ring_pip_R': ['Bone.014',13,14,13],
                'Ring_dip_R': ['Bone.015',14,15,14],
                'Ring_tip_R': ['Bone.016',15,16,15],
                'Pinky_mcp_R': ['Bone.017',0,17,0],
                'Pinky_pip_R': ['Bone.018',17,18,17],
                'Pinky_dip_R': ['Bone.019',18,19,18],
                'Pinky_tip_R': ['Bone.020',19,20,19]
                }
                
    #    path = r'C:\MOCAP\Videos\libras.mp4'
        #path=r'D:\MOCAP\Video\mao_VID_20210725_143957.mp4'
        path =  self.filepath
        
        
        point_name_l = 'Left'
        point_name_r = 'Right'
        create_dots(point_name_l,21)
        create_hand_bones('L')
        create_dots(point_name_r,21)
        create_hand_bones('R')
        frames = get_landmarks_hands('Name', get_video_frames(path))
        bpy.context.scene.frame_end = frames

        #Left side
        arm = last_n_armature(2)
        for f in range(frames):
            bpy.context.scene.frame_set(f)
            print('Frame: ',f)
            rot_hist_list=[Quaternion((1.0, 0.0, 0.0, 0.0))]
            for i,o in enumerate(bones_list_l):
                if len(bones_list_l[o]) == 2:
                    actual_bone = arm.pose.bones[o]
                    print(i,'-',o,'-',bones_list_l[o][1])
                    pt_obj1 = point_name_l+'.{0:03d}'.format(bones_list_l[o][1])
                    actual_bone.location = bpy.data.objects[pt_obj1].location
                    actual_bone.keyframe_insert(data_path='location',frame=f)
                else:
                    actual_bone = arm.pose.bones[o]
                    point1 = bones_list_l[o][1]
                    point2 = bones_list_l[o][2]
                    idx_rot_history = bones_list_l[o][3]
                    rot_history = rot_hist_list[idx_rot_history]
                    print(i,'-',o,'-',point1,'-',point1,'hist: ',rot_history)
                    rot_quat = cp_bone_rot(arm,i,o,point_name_l,point1,point2,rot_history)
                    rot_hist_list.append(rot_quat)
                    actual_bone.keyframe_insert(data_path='rotation_quaternion',frame=f)


        #Right side
        arm = last_n_armature(1)
        for f in range(frames):
            bpy.context.scene.frame_set(f)
            print('Frame: ',f)
            rot_hist_list=[Quaternion((1.0, 0.0, 0.0, 0.0))]
            for i,o in enumerate(bones_list_r):
                if len(bones_list_r[o]) == 2:
                    actual_bone = arm.pose.bones[o]
                    print(i,'-',o,'-',bones_list_r[o][1])
                    pt_obj1 = point_name_r+'.{0:03d}'.format(bones_list_r[o][1])
                    actual_bone.location = bpy.data.objects[pt_obj1].location
                    actual_bone.keyframe_insert(data_path='location',frame=f)
                else:
                    actual_bone = arm.pose.bones[o]
                    point1 = bones_list_r[o][1]
                    point2 = bones_list_r[o][2]
                    idx_rot_history = bones_list_r[o][3]
                    rot_history = rot_hist_list[idx_rot_history]
                    print(i,'-',o,'-',point1,'-',point1,'hist: ',rot_history)
                    rot_quat = cp_bone_rot(arm,i,o,point_name_r,point1,point2,rot_history)
                    rot_hist_list.append(rot_quat)
                    actual_bone.keyframe_insert(data_path='rotation_quaternion',frame=f)



        
        return {'FINISHED'}
        

