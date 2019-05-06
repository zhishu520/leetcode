class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        cnt = 0
        for i in nums:
            if i == 1:
                cnt += 1
            elif i == 0:
                if cnt > max:
                    max = cnt
                cnt = 0

        if cnt > max:
            max = cnt

        return max



