class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.list = []

        l = len(nums)

        sum = 0
        for i in range(0, l):
            sum += nums[i]
            self.list.append(sum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.list[j]
        else:
            return self.list[j] - self.list[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)