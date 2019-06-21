class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        s = sorted(heights)

        cnt = 0
        for i in range(len(heights)):
            if s[i] != heights[i]:
                cnt += 1

        return cnt