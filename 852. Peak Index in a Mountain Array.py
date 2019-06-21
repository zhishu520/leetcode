class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l,r = 0,len(A)-1
        while (l<=r):
            if A[l]<A[r]: l+=1
            else: r-=1
        return l