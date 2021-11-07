from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
robotArm.grab()
for x in range(7):
    for u in range(8):
         robotArm.moveRight()
    robotArm.drop()
    for u in range(8):
         robotArm.moveLeft()
    robotArm.grab()
robotArm.wait()