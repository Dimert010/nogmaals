from RobotArm import RobotArm 

robotArm = RobotArm('exercise 7')

for u in range(5):
    for u in range(6):
        robotArm.moveRight(), robotArm.grab(), robotArm.moveLeft(), robotArm.drop()
    for u in range(2):
        robotArm.moveRight()
robotArm.wait()
    
