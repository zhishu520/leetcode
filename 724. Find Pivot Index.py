class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sums = []
        l = len(nums)

        s = 0
        for i in nums:
            s += i
            sums.append(s)

        for i in range(0, l):

            left = sums[i - 1] if i > 0 else 0
            right = sums[l - 1] - sums[i] if i < l - 1 else 0

            if left == right:
                return i

        return -1






