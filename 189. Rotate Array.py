class Solution(object):
    def rotate(self, nums, k):
        l = len(nums)
        k = k % l
        t = nums[:]
        for i in range(0, l):
            nums[i] = t[(i+k+1)%l]








