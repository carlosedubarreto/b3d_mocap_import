import bpy
import math

class helper_functions(object):
    def anim_to_origin():
        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        bpy.context.scene.frame_current=f_start

        #==========================================
        #selecting and making the armature Active
        #selecionando armature
        #==========================================
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')


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

        #############################################################################
        ##found that to move the animation to the center, 
        ##I just have to subtract the inicial frame loc and rot from the other frames
        #########
        x_dif = bpy.context.object.pose.bones["Root"].rotation_euler[0] * -1
        y_dif = bpy.context.object.pose.bones["Root"].rotation_euler[1] * -1
        z_dif = bpy.context.object.pose.bones["Root"].rotation_euler[2] * -1


        x_loc_dif = bpy.context.object.pose.bones["Root"].location[0] * -1
        y_loc_dif = bpy.context.object.pose.bones["Root"].location[1] * -1
        z_loc_dif = bpy.context.object.pose.bones["Root"].location[2] * -1

        bpy.ops.object.mode_set(mode='EDIT')
        z_high_to_add = bpy.context.object.data.edit_bones["Foot_L"].tail.z
        bpy.ops.object.mode_set(mode='POSE')

        range(f_start,f_end+1)

        for f in range(f_start,f_end+1):
            print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()
        #    print('rot orig x: ',bpy.context.object.pose.bones["Root"].rotation_euler[0])
        #    print('rot x: ',bpy.context.object.pose.bones["Root"].rotation_euler[0] + x_dif)
            bpy.context.object.pose.bones["Root"].rotation_euler[0] = bpy.context.object.pose.bones["Root"].rotation_euler[0] + x_dif 
            bpy.context.object.pose.bones["Root"].rotation_euler[1] = bpy.context.object.pose.bones["Root"].rotation_euler[1] + y_dif 
            bpy.context.object.pose.bones["Root"].rotation_euler[2] = bpy.context.object.pose.bones["Root"].rotation_euler[2] + z_dif 
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='rotation_euler',frame=f)
            #################
            ## location to origin
            ##
            bpy.context.object.pose.bones["Root"].location[0] = bpy.context.object.pose.bones["Root"].location[0] + x_loc_dif
            bpy.context.object.pose.bones["Root"].location[1] = bpy.context.object.pose.bones["Root"].location[1] + y_loc_dif
            bpy.context.object.pose.bones["Root"].location[2] = bpy.context.object.pose.bones["Root"].location[2] + z_loc_dif
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='location',frame=f)


        #Check if need to transpose axis
        if abs(abs(math.degrees(x_dif))-90) < 45 or abs(abs(math.degrees(x_dif))-270) < 45:
        # if 1==1:
            #############################
            #rotate oprientation z por y
            for f in range(f_start,f_end+1):
                print('frame: ',f)
                bpy.context.scene.frame_current = f
                bpy.context.view_layer.update()   
                #changing location
                bone_root_loc_x = bpy.context.object.pose.bones["Root"].location[0]
                bone_root_loc_y = bpy.context.object.pose.bones["Root"].location[1]
                bone_root_loc_z = bpy.context.object.pose.bones["Root"].location[2]
                #changing orientation from z to y
                #z=y
                bpy.context.object.pose.bones["Root"].location[2] = bone_root_loc_y
                #y=z
                bpy.context.object.pose.bones["Root"].location[1] = bone_root_loc_z
                bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='location',frame=f)
                #######################
                ## rotation orientation change
                ##
                #rotation the rotation z to y
                bone_root_rot_x = bpy.context.object.pose.bones["Root"].rotation_euler[0]
                bone_root_rot_y = bpy.context.object.pose.bones["Root"].rotation_euler[1]
                bone_root_rot_z = bpy.context.object.pose.bones["Root"].rotation_euler[2]
                #changing orientation from z to y
                #z=y
                bpy.context.object.pose.bones["Root"].rotation_euler[2] = bone_root_rot_y
                #y=z
                bpy.context.object.pose.bones["Root"].rotation_euler[1] = bone_root_rot_z
                bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='rotation_euler',frame=f)
            


        ###############################
        ## adjust the foot to z=0
        for f in range(f_start,f_end+1):
        #    print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()
            bpy.context.object.pose.bones["Root"].location[1] = bpy.context.object.pose.bones["Root"].location[1] + abs(z_high_to_add)
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='location',frame=f)


        
        # print('org x: ', math.degrees(x_dif), 'orig y: ', math.degrees(y_dif), 'orig_z: ', math.degrees(z_dif)) 
        rot_original = 'x: ', math.degrees(x_dif), ' y: ', math.degrees(y_dif), ' z: ', math.degrees(z_dif)
        print(rot_original)
        bpy.ops.object.mode_set(mode='OBJECT')
        
        return (math.degrees(x_dif),math.degrees(y_dif),math.degrees(z_dif))


    def compensate_rot(x,y,z):
        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        #just to compensate grad
        x_grad_compensate = x
        y_grad_compensate = y
        z_grad_compensate = z
        for f in range(f_start,f_end+1):
            print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()
            print('rot orig x: ',bpy.context.object.pose.bones["Root"].rotation_euler[0])
            print('rot x: ',bpy.context.object.pose.bones["Root"].rotation_euler[0]  +math.radians(x_grad_compensate))
            bpy.context.object.pose.bones["Root"].rotation_euler[0] = bpy.context.object.pose.bones["Root"].rotation_euler[0]  +math.radians(x_grad_compensate)
            bpy.context.object.pose.bones["Root"].rotation_euler[1] = bpy.context.object.pose.bones["Root"].rotation_euler[1]  +math.radians(y_grad_compensate)
            bpy.context.object.pose.bones["Root"].rotation_euler[2] = bpy.context.object.pose.bones["Root"].rotation_euler[2]  +math.radians(z_grad_compensate)
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='rotation_euler',frame=f)


        return True

    def rotate_orientation(from_axis,to_axis):
        #############################
        #rotate oprientation acording to choice on menu

        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        if from_axis == 'x':
            from_ax = 0
        elif from_axis == 'y':
            from_ax = 1
        elif from_axis == 'z':
            from_ax = 2

        if to_axis == 'x':
            to_ax = 0
        elif to_axis == 'y':
            to_ax = 1
        elif to_axis == 'z':
            to_ax = 2

        if (from_axis == 'x' and to_axis == 'y') or (to_axis == 'x' and from_axis == 'y'):
            rotate_axis = 'z'
        elif (from_axis == 'y' and to_axis == 'z') or (to_axis == 'y' and from_axis == 'z'):
            rotate_axis = 'x'
        elif (from_axis == 'z' and to_axis == 'x') or (to_axis == 'z' and from_axis == 'x'):
            rotate_axis = 'y'

        if 'rotate_axis' in locals():
            if rotate_axis == 'x':
                rot_ax = 0
            elif rotate_axis == 'y':
                rot_ax = 1
            elif rotate_axis == 'z':
                rot_ax = 2
        
            if from_axis != rot_ax:
                for f in range(f_start,f_end+1):
                    print('frame: ',f)
                    bpy.context.scene.frame_current = f
                    bpy.context.view_layer.update()   

                    ##################
                    #changing location

                    bone_root_loc = []
                    bone_root_loc.append(bpy.context.object.pose.bones["Root"].location[0])
                    bone_root_loc.append(bpy.context.object.pose.bones["Root"].location[1])
                    bone_root_loc.append(bpy.context.object.pose.bones["Root"].location[2])
                    # bone_root_loc_x = bpy.context.object.pose.bones["Root"].location[0]
                    # bone_root_loc_y = bpy.context.object.pose.bones["Root"].location[1]
                    # bone_root_loc_z = bpy.context.object.pose.bones["Root"].location[2]
                    
                    #from-to
                    # bpy.context.object.pose.bones["Root"].location[2] = bone_root_loc_y
                    bpy.context.object.pose.bones["Root"].location[from_ax] = bone_root_loc[to_ax]
                    
                    #to-from
                    # bpy.context.object.pose.bones["Root"].location[1] = bone_root_loc_z
                    bpy.context.object.pose.bones["Root"].location[to_ax] = bone_root_loc[from_ax]
                    bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='location',frame=f)
                    

                    #######################
                    ## rotation orientation change
                    ##
                    bone_root_rot=[]

                    bone_root_rot.append(bpy.context.object.pose.bones["Root"].rotation_euler[0])
                    bone_root_rot.append(bpy.context.object.pose.bones["Root"].rotation_euler[1])
                    bone_root_rot.append(bpy.context.object.pose.bones["Root"].rotation_euler[2])

                    # bone_root_rot_x = bpy.context.object.pose.bones["Root"].rotation_euler[0]
                    # bone_root_rot_y = bpy.context.object.pose.bones["Root"].rotation_euler[1]
                    # bone_root_rot_z = bpy.context.object.pose.bones["Root"].rotation_euler[2]
                    
                    #from-to
                    bpy.context.object.pose.bones["Root"].rotation_euler[from_ax] = bone_root_rot[to_ax]
                    #to-from
                    bpy.context.object.pose.bones["Root"].rotation_euler[to_ax] = bone_root_rot[from_ax]

                    #convert adding 90 degrees
                    bpy.context.object.pose.bones["Root"].rotation_euler[rot_ax] = bpy.context.object.pose.bones["Root"].rotation_euler[rot_ax] + math.radians(-90)

                    bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='rotation_euler',frame=f)


        return True

    def reset_loc(): #make the animation start from where the boneas are located
        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        x_loc_dif = bpy.context.object.pose.bones["Root"].location[0] * -1
        y_loc_dif = bpy.context.object.pose.bones["Root"].location[1] * -1
        z_loc_dif = bpy.context.object.pose.bones["Root"].location[2] * -1

        for f in range(f_start,f_end+1):
            print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()

            #################
            ## location to origin
            ##
            bpy.context.object.pose.bones["Root"].location[0] = bpy.context.object.pose.bones["Root"].location[0] + x_loc_dif
            bpy.context.object.pose.bones["Root"].location[1] = bpy.context.object.pose.bones["Root"].location[1] + y_loc_dif
            bpy.context.object.pose.bones["Root"].location[2] = bpy.context.object.pose.bones["Root"].location[2] + z_loc_dif
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='location',frame=f)

        return True

    def reset_rot():
        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        x_dif = bpy.context.object.pose.bones["Root"].rotation_euler[0] * -1
        y_dif = bpy.context.object.pose.bones["Root"].rotation_euler[1] * -1
        z_dif = bpy.context.object.pose.bones["Root"].rotation_euler[2] * -1

        for f in range(f_start,f_end+1):
            print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()

            bpy.context.object.pose.bones["Root"].rotation_euler[0] = bpy.context.object.pose.bones["Root"].rotation_euler[0] + x_dif 
            bpy.context.object.pose.bones["Root"].rotation_euler[1] = bpy.context.object.pose.bones["Root"].rotation_euler[1] + y_dif 
            bpy.context.object.pose.bones["Root"].rotation_euler[2] = bpy.context.object.pose.bones["Root"].rotation_euler[2] + z_dif 
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='rotation_euler',frame=f)

        return True

    def foot_high():
        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        bpy.ops.object.mode_set(mode='EDIT')
        z_high_to_add = bpy.context.object.data.edit_bones["Foot_L"].tail.z
        bpy.ops.object.mode_set(mode='POSE')

        for f in range(f_start,f_end+1):
        #    print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()
            bpy.context.object.pose.bones["Root"].location[1] = bpy.context.object.pose.bones["Root"].location[1] + abs(z_high_to_add)
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='location',frame=f)

        bpy.ops.object.mode_set(mode='OBJECT')
        return True

    def compensate_rot(x,y,z):
        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        #just to compensate grad
        x_grad_compensate = x
        y_grad_compensate = y
        z_grad_compensate = z
        for f in range(f_start,f_end+1):
            print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()
            print('rot orig x: ',bpy.context.object.pose.bones["Root"].rotation_euler[0])
            print('rot x: ',bpy.context.object.pose.bones["Root"].rotation_euler[0]  +math.radians(x_grad_compensate))
            bpy.context.object.pose.bones["Root"].rotation_euler[0] = bpy.context.object.pose.bones["Root"].rotation_euler[0]  +math.radians(x_grad_compensate)
            bpy.context.object.pose.bones["Root"].rotation_euler[1] = bpy.context.object.pose.bones["Root"].rotation_euler[1]  +math.radians(y_grad_compensate)
            bpy.context.object.pose.bones["Root"].rotation_euler[2] = bpy.context.object.pose.bones["Root"].rotation_euler[2]  +math.radians(z_grad_compensate)
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='rotation_euler',frame=f)

        return True

    def get_rotations():

        bpy.context.scene.frame_current = 1
        bpy.context.view_layer.update()
        actual_rot_x = bpy.context.object.pose.bones["Root"].rotation_euler[0]
        actual_rot_y = bpy.context.object.pose.bones["Root"].rotation_euler[1]
        actual_rot_z = bpy.context.object.pose.bones["Root"].rotation_euler[2]

        return (actual_rot_x, actual_rot_y, actual_rot_z)

    # types = {'VIEW_3D', 'TIMELINE', 'GRAPH_EDITOR', 'DOPESHEET_EDITOR', 'NLA_EDITOR', 'IMAGE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'TEXT_EDITOR', 'NODE_EDITOR', 'LOGIC_EDITOR', 'PROPERTIES', 'OUTLINER', 'USER_PREFERENCES', 'INFO', 'FILE_BROWSER', 'CONSOLE'}

    def smooth_curves(o):
        current_area = bpy.context.area.type
        layer = bpy.context.view_layer

        # select all (relevant) bones
        for b in o.data.bones:
            b.select = False
        o.data.bones[0].select = True
        layer.update()

        # change to graph editor
        bpy.context.area.type = "GRAPH_EDITOR"

        # # lock or unlock the respective fcurves
        # for fc in o.animation_data.action.fcurves:
        #     print(fc.data_path)
        #     if "location" in fc.data_path:
        #         fc.lock = False
        #     else:
        #         fc.lock = True

        layer.update()
        # smooth curves of all selected bones
        bpy.ops.graph.smooth()

        # switch back to original area
        bpy.context.area.type = current_area

        # deselect all (relevant) bones
        for b in o.data.bones:
            b.select = False
        layer.update()

        return True

class skeleton_import(object):
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

    def remove_dots(name):    
        #apagar collection points criada
        collection = bpy.data.collections.get(name)
        #
        for obj in collection.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(collection)

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

    def create_bones(bones_list):
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
        obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True


        
        bpy.ops.armature.bone_primitive_add()#Spine
        #Neck
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
        #Face
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})


        bpy.ops.armature.bone_primitive_add()#Arm_L
        #Forearm_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
        
        bpy.ops.armature.bone_primitive_add()#Arm_R
        #Forearm_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
        
        bpy.ops.armature.bone_primitive_add()#Thigh_L
        #Leg_L
        #Foot_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
        
        bpy.ops.armature.bone_primitive_add()#Thigh_R
        #Leg_R
        #Foot_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
    
        for i in range(len(bones_list)):
            obs[len(obs)-1].data.edit_bones[bones_list[i][0]].name = bones_list[i][1]


        #Hierarquia
        bpy.context.object.data.edit_bones["Spine"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Arm_L"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Arm_R"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Thigh_L"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Thigh_R"].parent = bpy.context.object.data.edit_bones["Root"]

        bpy.ops.object.editmode_toggle()

    def distance(point1, point2) -> float: 
        #Calculate distance between two points in 3D.
        #return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)
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

    def size_ref_bone(p1,p2,p_final):
        from mathutils import Vector
        import bpy

        ## size of the reference bone (spine)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[p1].select_set(True)
        bpy.data.objects[p2].select_set(True)
        # bpy.context.view_layer.objects.active = bpy.data.objects['Point.034']
        bpy.context.view_layer.objects.active = bpy.data.objects[p2]
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
        unit_def = max(x_subtract, y_subtract, z_subtract)/3
        #end of size of reference bone Spine
        return unit_def

    def size_of_bones(unit, root_size, spine_size, neck_size, face_size, thigh_size, leg_size, foot_size, arm_size, forearm_size):
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




        bpy.context.object.data.edit_bones["Root"].length = root_size

        bpy.context.object.data.edit_bones["Spine"].head.z = unit/2
        bpy.context.object.data.edit_bones["Spine"].tail.z = spine_size

        bpy.context.object.data.edit_bones["Neck"].tail.z =  spine_size + neck_size
        bpy.context.object.data.edit_bones["Neck"].tail.y = neck_size/3
        bpy.context.object.data.edit_bones["Face"].tail.z = spine_size + neck_size
        bpy.context.object.data.edit_bones["Face"].tail.y = face_size*-1

        bpy.context.object.data.edit_bones["Arm_L"].head.z= spine_size
        bpy.context.object.data.edit_bones["Arm_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Forearm_L"].head.z=  spine_size
        bpy.context.object.data.edit_bones["Forearm_L"].head.x= unit + arm_size
        bpy.context.object.data.edit_bones["Forearm_L"].tail.z= spine_size
        bpy.context.object.data.edit_bones["Forearm_L"].tail.x= unit + arm_size + forearm_size

        bpy.context.object.data.edit_bones["Arm_R"].head.z= spine_size
        bpy.context.object.data.edit_bones["Arm_R"].head.x= (unit*3/4)*-1
        bpy.context.object.data.edit_bones["Forearm_R"].head.z= spine_size
        bpy.context.object.data.edit_bones["Forearm_R"].head.x= (unit + arm_size) *-1
        bpy.context.object.data.edit_bones["Forearm_R"].tail.z= spine_size
        bpy.context.object.data.edit_bones["Forearm_R"].tail.x= (unit + arm_size + forearm_size) *-1

        bpy.context.object.data.edit_bones["Thigh_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Thigh_L"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Leg_L"].head.z= (unit/5 + thigh_size)*-1
        bpy.context.object.data.edit_bones["Foot_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].head.z= (unit/5 + thigh_size + leg_size)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].tail.z= (unit/5 + thigh_size + leg_size + foot_size/2)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.y= foot_size/2*-1

        bpy.context.object.data.edit_bones["Thigh_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Thigh_R"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.z= (unit/5 + thigh_size)*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.z= (unit/5 + thigh_size + leg_size)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.z= (unit/5 + thigh_size + leg_size + foot_size/2)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.y= foot_size/2*-1

        bpy.ops.object.editmode_toggle()

    def add_constraints(constraints, limit_rotation):
        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.object.mode_set(mode='POSE')

        for i in range(len(constraints)):
            print('processar: ',constraints[i])
            if  constraints[i][1] == 'COPY_LOCATION' or constraints[i][1] == 'DAMPED_TRACK':
        #        print('in 1 j: ',j,' - name: ',constraints[i][0],' constraint: ',constraints[i][1])
                obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[constraints[i][0]].bone
                obs[len(obs)-1].pose.bones[constraints[i][0]].bone.select = True
                #
                bpy.ops.pose.constraint_add(type=constraints[i][1])
                qtd_constraint = len(bpy.context.object.pose.bones[constraints[i][0]].constraints)
                bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].target = bpy.data.objects[constraints[i][2]]
                if constraints[i][1] == 'DAMPED_TRACK' and len(constraints[i])==4:
                    bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].track_axis = constraints[i][3]
                #
            if constraints[i][1] == 'LIMIT_ROTATION' and limit_rotation == True :
                qtd_constraint = len(bpy.context.object.pose.bones[constraints[i][0]].constraints)
                if constraints[i][2] == 'LOCAL':
                    bpy.ops.pose.constraint_add(type=constraints[i][1])
                    qtd_constraint = len(bpy.context.object.pose.bones[constraints[i][0]].constraints)
                    bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].owner_space = constraints[i][2]
                if constraints[i][2] == 'X':
                    if constraints[i][3] == True:
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].use_limit_x = constraints[i][3]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].min_x  = constraints[i][4]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].max_x = constraints[i][5]
                if constraints[i][2] == 'Y':
                    if constraints[i][3] == True:
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].use_limit_y = constraints[i][3]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].min_y  = constraints[i][4]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].max_y = constraints[i][5]
                if constraints[i][2] == 'Z':
                    if constraints[i][3] == True:
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].use_limit_z = constraints[i][3]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].min_z  = constraints[i][4]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].max_z = constraints[i][5]

    def add_constraints_track_X(constraints,limit_rotation):
        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.object.mode_set(mode='POSE')

        for i in range(len(constraints)):
            print('processar: ',constraints[i])
            if  constraints[i][1] == 'COPY_LOCATION' or constraints[i][1] == 'DAMPED_TRACK':
        #        print('in 1 j: ',j,' - name: ',constraints[i][0],' constraint: ',constraints[i][1])
                obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[constraints[i][0]].bone
                obs[len(obs)-1].pose.bones[constraints[i][0]].bone.select = True
                #
                bpy.ops.pose.constraint_add(type=constraints[i][1])
                qtd_constraint = len(bpy.context.object.pose.bones[constraints[i][0]].constraints)
                bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].target = bpy.data.objects[constraints[i][2]]
                if constraints[i][1] == 'DAMPED_TRACK' and len(constraints[i])>=4:
                    bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].track_axis = constraints[i][3]
                    bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].influence = constraints[i][4]
                #
            if constraints[i][1] == 'LIMIT_ROTATION' and limit_rotation == True:
                qtd_constraint = len(bpy.context.object.pose.bones[constraints[i][0]].constraints)
                if constraints[i][2] == 'LOCAL':
                    bpy.ops.pose.constraint_add(type=constraints[i][1])
                    qtd_constraint = len(bpy.context.object.pose.bones[constraints[i][0]].constraints)
                    bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].owner_space = constraints[i][2]
                if constraints[i][2] == 'X':
                    if constraints[i][3] == True:
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].use_limit_x = constraints[i][3]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].min_x  = constraints[i][4]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].max_x = constraints[i][5]
                if constraints[i][2] == 'Y':
                    if constraints[i][3] == True:
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].use_limit_y = constraints[i][3]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].min_y  = constraints[i][4]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].max_y = constraints[i][5]
                if constraints[i][2] == 'Z':
                    if constraints[i][3] == True:
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].use_limit_z = constraints[i][3]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].min_z  = constraints[i][4]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].max_z = constraints[i][5]

