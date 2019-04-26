class Solution(object):
    def twoSum(self, nums, target):

        s = len(nums)
        for i in range(0, s):
            ret = self.bs(nums, i+1, s-1, target - nums[i])
            if ret != -1:
                return [i+1, ret+1]



    def bs(self, nums, l, r, target):
        if l > r:
            return -1

        m = (l + r) / 2

        if nums[m] == target:
            return m
        elif nums[m] > target:
            return self.bs(nums, l, m - 1, target)
        else:
            return self.bs(nums, m + 1, r, target)



if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([5,25,75], 100))

