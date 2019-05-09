class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        l1 = len(grid)
        l2 = len(grid[0])

        step = [[0,1],[1,0],[0,-1],[-1,0]]

        cnt = 0

        for i in range(l1):
            for j in range(l2):
                for k in range(4):

                    if grid[i][j] == 0:
                        continue

                    newi = i + step[k][0]
                    newj = j + step[k][1]

                    if newi >= l1 or newj >= l2 or newi < 0 or newj < 0:
                        cnt += 1
                    else:
                        if grid[newi][newj] == 0:
                            cnt += 1

        return cnt
