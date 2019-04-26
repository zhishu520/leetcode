class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dict = {}


        for i in nums:
            if dict.has_key(i):
                dict[i] += 1
            else:
                dict.setdefault(i, 1)

        maxI, maxJ = 0, 0
        for obj in dict:
            i = object
            if j > maxJ:
                maxJ, maxI = j, i

        return maxI
