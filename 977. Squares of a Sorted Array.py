class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        r = []
        for i in A:
            r.append(i * i)

        r.sort()
        return r

