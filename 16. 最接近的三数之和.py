class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        c = 10000
        ret = 0

        nums.sort()

        print nums

        l = len(nums)
        for i in range(l - 2):

            left = i + 1
            right = l - 1

            while left < right:
                m = abs(nums[i] + nums[left] + nums[right] - target)
                if m < c:
                    c = m
                    ret = nums[i] + nums[left] + nums[right]

                if target - nums[i] > nums[left] + nums[right]:
                    left += 1
                else:
                    right -= 1

        return ret