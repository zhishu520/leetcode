class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        ret = []

        nums.sort()

        # print nums
        l = len(nums)
        for i in range(l - 3):
            for j in range(i + 1, l - 2):

                left = j + 1
                right = l - 1

                while left < right:

                    # print(nums[i] , nums[j] , nums[left] , nums[right])
                    if (nums[i] + nums[j] + nums[left] + nums[right] == target):

                        if not ret.__contains__([nums[i], nums[j], nums[left], nums[right]]):
                            ret.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1

                    if target - nums[i] - nums[j] > nums[left] + nums[right]:
                        left += 1
                    else:
                        right -= 1

        return ret