class Solution:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = None

    def moving(self,cmd):

        return

    def distance(self):
        return abs(self.x)+abs(self.y)


cmd = "F1,R1,B2,L1,B3"
robot = Solution()
robot.moving(cmd)
d = robot.distance()
print(d)