class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        l = len(A)
        if l == 1:
            return 0

        A.sort()

        min = A[0]
        max = A[l - 1]

        if min + k <= max - k:
            return 0
        else:
            return max - k - (min + k)








