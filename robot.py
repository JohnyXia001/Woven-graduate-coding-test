class Solution:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0 # degree from 0-360

    def process(self, cmd):
        cmd = cmd.split(",")
        for pair in cmd:
            action = pair[0]
            number = int(pair[1:])
            print(action, number)
            self.command(action, number)

    def command(self, action, number):
        # turn direction
        if action == "R":
            self.direction = (self.direction-90*number)%360
            return
        elif action == "L":
            self.direction = (self.direction+90*number)%360
            return

        # move
        if action == "F":
            cur_dir = self.direction
        elif action == "B":
            cur_dir = (self.direction+180)%360

        if cur_dir == 0:
            self.x += number
        elif cur_dir == 90:
            self.y += number
        elif cur_dir == 180:
            self.x -= number
        elif cur_dir == 270:
            self.y -= number

    def distance(self):
        return abs(self.x)+abs(self.y)

# cmd
cmd = "F1,R1,B2,L2,B3"
robot = Solution()
robot.process(cmd)
d = robot.distance()
print(d)