class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        ret = 1
        for i in nums:
            if i == ret:
                ret += 1

        return ret

