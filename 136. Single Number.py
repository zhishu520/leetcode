class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        for i in range(1, l):
            nums[0] = nums[0] ^ nums[i]

        return nums[0]

