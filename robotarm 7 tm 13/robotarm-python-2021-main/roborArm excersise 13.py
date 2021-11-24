from RobotArm import RobotArm
robotArm = RobotArm('exercise 13')
robotArm.randomLevel(1, 7)

l = 1
robotArm.grab()
while robotArm.scan() !="":
        for k in range(l): 
            robotArm.moveRight()
        robotArm.drop()
        for j in range(l):
            robotArm.moveLeft()
        robotArm.grab()
        l += 1
   
robotArm.wait()