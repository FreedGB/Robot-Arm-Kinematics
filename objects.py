from math import pi,cos,sin

class linear_joint:
    # I'll consider that max lenght of the part that goes in and out is equal to the fixed part's lenght
    def __init__(self,L_fix:float,L_mob:float,initial_angle:float):
        self.L_fix = L_fix # the lenght of the fixed part
        self.L_mob = L_mob # the lenght of the mobile part at a particular instant
        self.initial_angle = initial_angle # the initial angle of the joints' parts. It would be a constant
        self.end_point_coordinates = [(L_fix + L_mob)*cos(initial_angle) , (L_fix + L_mob)*sin(initial_angle)]

    def move(self,distance:float):
        self.L_mob += distance



'''
class robot_arm:
    def __init__(self,links_lenght:float,joint1_revo:float,joint2_revo:float):
        self.links_lenght = links_lenght
'''

