from math import sqrt,atan,pi,cos,sin


class linear_joint:
    # I'll consider that max lenght of the mobile part as unlimited for now
    def __init__(self, link_lenght:float, angle:float = 0, first_point_coordinates:list = [0,0]):
        self.first_point_coordinates = first_point_coordinates # the coordinates of the joint without the link
        self.link_lenght = link_lenght # the lenght of the link at a particular instant
        self.angle = angle # the angle of the joint+link with the x-axis
        self.end_point_coordinates = [self.first_point_coordinates[0] + self.link_lenght*cos(self.angle) , self.first_point_coordinates[1] + self.link_lenght*sin(self.angle)]

    def calculate_coordinates(self):
        self.end_point_coordinates = [self.first_point_coordinates[0] + self.link_lenght*cos(self.angle) , self.first_point_coordinates[1] + self.link_lenght*sin(self.angle)]


    def move(self, distance:float):
        # Negative distance to go back and positive to go out
        self.L_mob += distance
        self.calculate_coordinates()

    def move_to(self, x:float, y:float):
        # This method will allow us to calculate, for every given coordinates, the lenght that the mobile part has to have
        x0 = self.first_point_coordinates[0]
        y0 = self.first_point_coordinates[1]
        new_link_lenght = sqrt(((x - x0)**2) + ((y - y0)**2))
        if new_link_lenght >= 0:
            self.move(new_link_lenght - self.link_lenght)
        else:
            print("\nOut of range")




class revo_joint:
    def __init__(self, link_lenght:float, angle:float = 0, first_point_coordinates:list = [0,0]):
        self.first_point_coordinates = first_point_coordinates # the coordinates of the joint without the link
        self.link_lenght = link_lenght # the lenght of the link at a particular instant
        self.angle = angle # the angle of the joint+link with the x-axis
        self.end_point_coordinates = [self.first_point_coordinates[0] + self.link_lenght*cos(self.angle) , self.first_point_coordinates[1] + self.link_lenght*sin(self.angle)]

    def calculate_coordinates(self):
        self.end_point_coordinates = [self.first_point_coordinates[0] + self.link_lenght*cos(self.angle) , self.first_point_coordinates[1] + self.link_lenght*sin(self.angle)]


    def move(self, alpha:float):
        # Negative alpha to go down and positive to go up
        self.angle += alpha
        self.calculate_coordinates()

    def move_to(self, x:float, y:float):
        # This method will allow us to calculate, for every given coordinates, the angle that the moveable link have to rotate
        x0 = self.first_point_coordinates[0]
        y0 = self.first_point_coordinates[1]
        if ((x-x0)**2) + ((y-y0)**2) == (self.link_lenght)**2:
            new_angle = atan((y - y0) / (x - x0))
            self.move(new_angle - self.angle)
        else:
            print("\nOut of range")
