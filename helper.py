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