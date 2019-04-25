class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = len(nums)
        arr = [0] * s

        self.step(s, arr)


    def step(self, pos, arr, nums):

        for i in range(0, pos):
            if nums[i] + i >= pos:
                arr[i] += 1
                self.step(i, arr, nums)

        pass








if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,1,4]))
