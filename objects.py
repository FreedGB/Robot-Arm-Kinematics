from math import sqrt,pi,cos,sin,atan2


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
        self.end_point_coordinates = [round(self.first_point_coordinates[0] + self.link_lenght*cos(self.angle),3) , round(self.first_point_coordinates[1] + self.link_lenght*sin(self.angle),3)]

    def calculate_coordinates(self):
        self.end_point_coordinates = self.end_point_coordinates = [round(self.first_point_coordinates[0] + self.link_lenght*cos(self.angle),3) , round(self.first_point_coordinates[1] + self.link_lenght*sin(self.angle),3)]


    def rotate_to(self, alpha:float):
        # Negative alpha to go down and positive to go up
        self.angle = alpha
        self.calculate_coordinates()

    def move_to(self, xn:float, yn:float):
        # This method will allow us to calculate, for every given coordinates, the angle that the moveable link have to rotate
        x_center = self.first_point_coordinates[0]
        y_center = self.first_point_coordinates[1]
        new_angle =  atan2(yn - y_center, xn - x_center)
        self.rotate_to(new_angle)
        

            



# A robot with two revolution joints. The two joints must be defined first
class robot_arm_1:
    def __init__(self, revo_joint1:revo_joint, revo_joint2:revo_joint):
        revo_joint2.first_point_coordinates = revo_joint1.end_point_coordinates
        revo_joint2.calculate_coordinates()

        self.revo_joint1 = revo_joint1
        self.revo_joint2 = revo_joint2

        self.grip_coordinates = self.revo_joint2.end_point_coordinates


    def move_to(self, x:float, y:float):

        if y<0:
            print("\ny must be positive or nul.")
            return
        
        L1 = self.revo_joint1.link_lenght
        L2 = self.revo_joint2.link_lenght

        if (x**2 + y**2) < (L1-L2)**2 or (x**2 + y**2) > (L1+L2)**2:
            print("\nOut of domain.")
            return
        
        if x == 0 and y == 0:
            if L1 != L2:
                print("\nOut of domain.")
                return
            
            x0 = L1*cos(pi/4)
            y0 = L1*sin(pi/4)



        if x == 0 and y != 0:
            y0 = (L1**2 -L2**2 + y**2)/(2*y)
            x0 = sqrt(L1**2 - y0**2)

        
        if x != 0:
            
            A = L1**2 - L2**2 + x**2 + y**2

            a = 1 + (y/x)**2
            b = -(A*y)/(x**2)
            c = ( (A**2)/(4*x**2) ) - L1**2
            delta = b**2 - 4*a*c

            if delta >= 0:
                y0 = (-b -sqrt(delta))/(2*a)
                x0 = ((A/2) - y*y0)/x


        self.revo_joint1.move_to(x0,y0)
        self.revo_joint1.calculate_coordinates()
        self.revo_joint2.first_point_coordinates = self.revo_joint1.end_point_coordinates
        self.revo_joint2.move_to(x,y)
        self.revo_joint1.calculate_coordinates()
        self.grip_coordinates = self.revo_joint2.end_point_coordinates