class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        r = []

        l1 = len(nums1)
        l2 = len(nums2)

        for i in range(0, len(nums1)):
            for j in range(i, len(nums2)):
                if nums2[j] == nums1[i]:
                    nums1.pop(i)
                    nums2.pop(j)
                    i -= 1
                    j -= 1

        return r