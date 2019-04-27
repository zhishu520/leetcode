class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.s(nums, 0, len(nums)-1, target)

    def s(self, nums, l, r, target):
        print(l, r)
        if l > r:
            return -1
        m = int((l+r)/2)

        if nums[m] == target:
            return m
        elif target < nums[m]:
            return self.s(nums, l, m-1, target)
        else:
            return self.s(nums, m+1, r, target)


if __name__ == '__main__':
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 9))
