from RobotArm import RobotArm 
robotArm = RobotArm('exercise 9')
robotArm.speed = 2
for q in range(4):
    for q in range(4):
        robotArm.grab()
        [robotArm.moveRight() for movement in range (5)]
        robotArm.drop()
        [robotArm.moveLeft() for movement in range(4)]
    [robotArm.moveLeft() for i in range(4)]

robotArm.wait()