from math import sqrt,atan,pi,cos,sin


class linear_joint:
    # I'll consider that max lenght of the mobile part as unlimited for now
    def __init__(self, first_point_coordinates:list, L_fix:float, L_mob:float, angle:float):
        self.first_point_coordinates = first_point_coordinates # the coordinates of the first link
        self.L_fix = L_fix # the lenght of the fixed part
        self.L_mob = L_mob # the lenght of the mobile part at a particular instant
        self.angle = angle # the initial angle of the joint's parts.
        self.end_point_coordinates = [self.first_point_coordinates[0] + (self.L_fix + self.L_mob)*cos(self.angle) , self.first_point_coordinates[1] + (self.L_fix + self.L_mob)*sin(self.angle)]

    def calculate_coordinates(self):
        self.end_point_coordinates = [self.first_point_coordinates[0] + (self.L_fix + self.L_mob)*cos(self.angle) , self.first_point_coordinates[1] + (self.L_fix + self.L_mob)*sin(self.angle)]


    def move(self, distance:float):
        # Negative distance to go back and positive to go out
        self.L_mob += distance
        self.calculate_coordinates()

    def move_to(self, x:float, y:float):
        # This method will allow us to calculate, for every given coordinates, the lenght that the mobile part has to have
        x0 = self.first_point_coordinates[0]
        y0 = self.first_point_coordinates[1]
        new_L_mob = sqrt(((x - x0)**2) + ((y - y0)**2)) - self.L_fix
        self.move(new_L_mob - self.L_mob)




class revo_joint:
    def __init__(self, first_point_coordinates:list, initial_angle:float, L_fix:float):
        self.first_point_coordinates = first_point_coordinates # the coordinates of the first point of the first link
        self.initial_angle = initial_angle # the initial angle of the first link.
        self.L_fix = L_fix # the lenght of the two parts. It's a constant
        self.angle = pi # the initial joint's angle
        self.end_point_coordinates = [self.first_point_coordinates[0] + self.L_fix*cos(self.initial_angle) + self.L_mob*cos(self.angle + self.initial_angle) , self.first_point_coordinates[1] + self.L_fix*sin(self.initial_angle) + self.L_mob*sin(self.angle + self.initial_angle)]

    def calculate_coordinates(self):
        self.end_point_coordinates = [self.first_point_coordinates[0] + self.L_fix*cos(self.initial_angle) + self.L_mob*cos(self.angle + self.initial_angle) , self.first_point_coordinates[1] + self.L_fix*sin(self.initial_angle) + self.L_mob*sin(self.angle + self.initial_angle)]


    def move(self, alpha:float):
        # Negative alpha to go down and positive to go up
        self.angle += alpha
        self.calculate_coordinates()

    def move_to(self, x:float, y:float):
        # This method will allow us to calculate, for every given coordinates, the angle that the moveable link have to rotate
        x0 = self.first_point_coordinates[0]
        y0 = self.first_point_coordinates[1]
        new_angle = atan((y - y0 - self.L_fix*sin(self.initial_angle)) / (x - x0 - self.L_fix*cos(self.initial_angle)) ) - self.initial_angle
        self.move(new_angle - self.angle)