class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        l = len(nums)
        idx = 0
        for i in range(0, l):
            if nums[idx] == 0:
                for j in range(idx, l):
                    if j == l-1:
                        nums[l-1] = 0
                    else:
                        nums[j] = nums[j+1]
            else:
                idx += 1



if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([0,1,0,3,12])

