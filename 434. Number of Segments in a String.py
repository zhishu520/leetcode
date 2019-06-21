class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        arr = s.split(" ")

        cnt = 0
        for i in arr:
            if len(i) > 0:
                cnt += 1

        return cnt