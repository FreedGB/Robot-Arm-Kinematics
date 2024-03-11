from math import pi,cos,sin

class robot_2arms:
    def __init__(self,links_lenght:float):
        self.links_lenght = links_lenght
        self.joint1_revo = pi/2
        self.joint2_revo = pi