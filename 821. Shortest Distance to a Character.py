class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        pos = []

        l = len(S)

        for i in range(l):
            if S[i] == C:
                pos.append(i)


        rt = []
        for i in range(l):
            rt.append(self.getMin(i, pos))
        return rt

    def getMin(self, n, arr):
        min = 10000
        for i in arr:
            if min > abs(n-i):
                min = abs(n-i)
        return min






