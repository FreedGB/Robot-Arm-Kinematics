from math import pi,cos,sin

class linear_joint:
    # I'll consider that max lenght of the part that goes in and out is equal to the fixed part's lenght
    def __init__(self, L_fix:float, L_mob:float, angle:float):
        self.L_fix = L_fix # the lenght of the fixed part
        self.L_mob = L_mob # the lenght of the mobile part at a particular instant
        self.angle = angle # the initial angle of the joints' parts. It would be a constant
        self.end_point_coordinates = [(L_fix + self.L_mob)*cos(angle) , (L_fix + self.L_mob)*sin(angle)]

    def move(self, distance:float):
        self.L_mob += distance

class revo_joint:
    def __init__(self, L_fix:float, max_angle:float):
        self.L_fix = L_fix # the lenght of the two parts. It's a constant
        self.max_angle = max_angle # the max angle the joint can rotate
        self.angle = pi # the initial joint's angle
        self.end_point_coordinates = [L_fix*(1+cos(self.angle)) , L_fix*sin(self.angle)]

    def move_up(self, alpha:float):
        self.angle += alpha

    def move_down(self, alpha:float):
        self.angle -= alpha



'''
class robot_arm:
    def __init__(self,links_lenght:float,joint1_revo:float,joint2_revo:float):
        self.links_lenght = links_lenght
'''

