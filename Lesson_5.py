class Robot:
    position = 0
    armPosition = 0
    haveCube = False
    Score = 0

    def __init__(self, position, armPosition, haveCube, Score):
        self.position = position
        self.armPosition = armPosition
        self.haveCube = haveCube
        self.Score = Score
    def move(self, moveTo):
        self.position = moveTo 

    def raiseArm(self, moveArm):
        self.armPosition = moveArm
    def getCube(self, position, armPosition, haveCube):
        if self.position == 3 and self.armPosition == 0 and haveCube == False:
            self.haveCube = True
    def scoreCube(self):
        if self.position == 7 and self.armPosition == 10 and self.haveCube == True:
            self.Score += 1

theRobot = Robot(0,0,False,0)
theRobot.move(3)
theRobot.raiseArm(0)
theRobot.getCube(theRobot.position,theRobot.armPosition, theRobot.haveCube)
theRobot.move(7)
theRobot.raiseArm(10)
theRobot.scoreCube()
print(theRobot.Score)
    
