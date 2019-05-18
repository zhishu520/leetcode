class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        SA = 0
        for i in A:
            SA += i

        SB = 0
        for i in B:
            SB += i

        B.sort()

        lb = len(B)
        for i in range(len(A)):
            t = (SB - SA + 2 * A[i])/2
            pos = self.s(B, 0, lb-1, t)
            print t
            if pos != -1:
                return [A[i], t]

    def s(self, nums, l, r, target):
        if l > r:
            return -1
        m = int((l+r)/2)

        if nums[m] == target:
            return m
        elif target < nums[m]:
            return self.s(nums, l, m-1, target)
        else:
            return self.s(nums, m+1, r, target)

