from objects import *

revo_joint1 = revo_joint(10)
revo_joint2 = revo_joint(5)

robot = robot_arm_1(revo_joint1,revo_joint2)
print(f"Grip coordinates = {robot.grip_coordinates}")

robot.move_to(-1,0)
print(f"Grip coordinates = {robot.grip_coordinates}")

robot.move_to(-15,0)
print(f"Grip coordinates = {robot.grip_coordinates}")

robot.move_to(0,0)
print(f"Grip coordinates = {robot.grip_coordinates}")

robot.move_to(15,0)
print(f"Grip coordinates = {robot.grip_coordinates}")

robot.move_to(0,15)
print(f"Grip coordinates = {robot.grip_coordinates}")

robot.move_to(10,10)
print(f"Grip coordinates = {robot.grip_coordinates}")