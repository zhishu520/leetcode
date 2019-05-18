class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        i = j = 0

        while j < n:
            if i >= m:
                nums1[i] = nums2[j]
                j += 1
                m += 1
            elif nums1[i] > nums2[j]:
                for t in range(len(nums1)-2, i-1, -1):
                    nums1[t+1] = nums1[t]
                nums1[i] = nums2[j]
                j += 1
                m += 1
                i -= 1

            i += 12

        print nums1



