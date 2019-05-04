class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        r = []
        for i in range(0, R):
            for j in range(0, C):
                r.append([i, j])


        import math
        r.sort(key=lambda x: math.fabs(x[0]-r0) + math.fabs(x[1]-c0))
        return r


