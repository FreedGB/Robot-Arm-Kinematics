from objects import *

revo_joint1 = revo_joint(10,pi/2)
revo_joint2 = revo_joint(5)

robot = robot_arm_1(revo_joint1,revo_joint2)
print(robot.grip_coordinates)