class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        if l == 0:
            return 0

        cnts = [0] * 50000

        for i in nums:
            cnts[i] += 1

        max = 0
        cis = []
        for i in range(50000):
            if cnts[i] > max:
                max = cnts[i]
                cis = [i]
            elif cnts[i] == max:
                cis.append(i)

        if max == 1:
            return 1

        min = 50000
        for i in cis:
            t = self.dis(nums, i, l)
            if min > t:
                min = t
        return min

    def dis(self, nums, ci, l):
        l, r = 0, l - 1
        while nums[l] != ci:
            l += 1
        while nums[r] != ci:
            r -= 1
        return r - l + 1

