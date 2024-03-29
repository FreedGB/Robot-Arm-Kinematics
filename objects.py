from math import pi,cos,sin

class linear_joint:
    # I'll consider that max lenght of the part that goes in and out is equal to the fixed part's lenght
    def __init__(self, first_point_coordinates:list, L_fix:float, L_mob:float, angle:float):
        self.first_point_coordinates = first_point_coordinates # the coordinates of the first link
        self.L_fix = L_fix # the lenght of the fixed part
        self.L_mob = L_mob # the lenght of the mobile part at a particular instant
        self.angle = angle # the initial angle of the joints' parts. It would be a constant
        self.end_point_coordinates = [(first_point_coordinates[0] + L_fix + self.L_mob)*cos(angle) , (first_point_coordinates[1] + L_fix + self.L_mob)*sin(angle)]

    def move(self, distance:float):
        self.L_mob += distance

class revo_joint:
    def __init__(self, first_point_coordinates:list, initial_angle:float, L_fix:float, max_angle:float):
        self.first_point_coordinates = first_point_coordinates # the coordinates of the first point of the first link
        self.initial_angle = initial_angle # the initial angle of the first link. It's a constant
        self.L_fix = L_fix # the lenght of the two parts. It's a constant
        self.max_angle = max_angle # the max angle the joint can rotate
        self.angle = pi # the initial joint's angle
        self.end_point_coordinates = [L_fix*(cos(initial_angle) + cos(self.angle + initial_angle)) , L_fix*(sin(initial_angle) + sin(self.angle + initial_angle))]

    def move_up(self, alpha:float):
        self.angle += alpha

    def move_down(self, alpha:float):
        self.angle -= alpha



'''
class robot_arm:
    def __init__(self,links_lenght:float,joint1_revo:float,joint2_revo:float):
        self.links_lenght = links_lenght
'''

