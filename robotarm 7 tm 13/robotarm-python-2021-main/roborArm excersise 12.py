from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
robotArm.speed = 2
for o in range(10,1,-1):
    robotArm.grab()
    if robotArm.scan() == "red":
        for k in range(o):
            robotArm.moveRight()
        robotArm.drop()
        for k in range(k-1):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
robotArm.wait()