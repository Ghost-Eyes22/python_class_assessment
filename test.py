from os import system 
system("clear") # clears the terminal before running the tests

from module import Robot

print("Robot class test running...")
print() # Skip line

print("Creating Test Bot, Color: Black")
robot = Robot("Test Bot", "Black")
print()

print("Testing status method...")
print(robot.status())
print()

print("Testing charge method...")
print(robot.charge(40))
print()

print("Testing work method...")
print(robot.work(3))
print()


print("Testing repair method...")
print(robot.repair())
print()

print("Displaying final status...")
print(robot.status())
print()