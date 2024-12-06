import math

#from scripts.coordinate_generator import coord_handler

def radtodegrees(list):
    for i in range(6):
        list[i]=list[i]*(180/math.pi)
    return(list)




APPROACH_POSE1 = [0.878345251083374, -1.4129328739694138, 1.9044411818133753, -2.091734548608297, -1.4622834364520472, -2.130199734364645]
pick_pose = [0.5217525959014893, -0.8984154027751465, 2.2390645186053675, -2.453958650628561, -0.0081713835345667, -1.974764649068014]

set_pose = [1.2957301139831543, -0.9064623278430481, 1.8208301703082483, -1.1233906608871003, -0.22048646608461553, -2.9866870085345667]
APPROACH_POSE2 = [1.2254915237426758, -1.568632664890476, 2.2014039198504847, -1.0249703091434021, -0.4114111105548304, -2.6641293207751673]

HOME = [1.3364453315734863, -1.4110311430743714, 1.5946815649615687, -1.8614422283568324, -1.4034164587603968, -2.9883862177478235]

new_pose=radtodegrees(HOME)
print(new_pose)


# Define all the cartesian positions used in the task
# (mm,mm,mm,rad,rad,rad) (X,Y,Z,Rx,Ry,Rz)

plane = [-224.46, -271.21, 7.61,0.028, 0.048, 4.749]  # The base calibration plane

# Origin positions for both racks
pick_rack_origin = [94.8, 350, 50, 2.22, -2.223, -0.00]
set_rack_origin = [273.41, 57.5, 50, 2.220, -2.223, -0.00]

# General pounce/approach pos
pick_approach = [146.54, 167.55, 199.42, 3.055, -0.731, 0]
set_approach = []
