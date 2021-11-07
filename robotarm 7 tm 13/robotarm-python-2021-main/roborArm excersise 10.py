from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
move = 9
robotArm.grab()
for a in range(5):
    for a in range(move):
        robotArm.moveRight()
    robotArm.drop()
    for a in range(move -1):
        robotArm.moveLeft()
    robotArm.grab()
    move = move-2
robotArm.drop()
robotArm.wait()