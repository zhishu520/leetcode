class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """


        arr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        flag = 0

        x,y = 0,0

        for k in range(4):
            for i in instructions:
                if i == "G":
                    x += arr[flag][0]
                    y += arr[flag][1]
                elif i == "L":
                    flag = (flag + 4 - 1) % 4
                elif i == "R":
                    flag = (flag + 1) % 4

        return x == 0 and y == 0
