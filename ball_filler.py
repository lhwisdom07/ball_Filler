import math
numberofB =int(input ("How many bowling balls will be manufactured? "))
ballD = float(input ("What is the diameter of each ball in inches? "))
ballR = float(ballD / 2)
coreV = int(input("What is the core volume in inches cubed? "))
fillerA = (4/3) * (math.pi * (ballR ** 3))- coreV

print("You will need",fillerA * numberofB,"inches in cubed filler")
# import the math library


