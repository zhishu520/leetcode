
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)

        sum = l * (l - 1) / 2
        
        for i in nums:
            sum -= i

        return sum

