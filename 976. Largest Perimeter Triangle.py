class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse=True)
        for j in range(0, len(A)-2):
            for i in range(j+2, len(A)):
                if A[i] + A[j+1] > A[j]:
                    return A[i] + A[j+1] + A[j]

        return 0





