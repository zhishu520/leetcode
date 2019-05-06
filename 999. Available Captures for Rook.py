class Solution(object):
    def numRookCaptures(self, A):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        X = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(0, 8):
            for j in range(0, 8):
                if A[i][j] == 'R':
                    I, J  = i, j

        cnt = 0

        for x in X:
            i, j = I, J
            while i >= 0 and j >= 0 and i < 8 and j < 8:

                if A[i][j] == 'p':
                    cnt += 1
                    break
                elif A[i][j] == 'B':
                    break

                i += x[0]
                j += x[1]

        return cnt


