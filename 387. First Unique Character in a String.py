class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        arr = [0] * 26

        for i in s:
            arr[ord(i) - ord('a')] += 1

        for i in range(len(s)):
            if arr[ord(s[i]) - ord('a')] == 1:
                return i

        return -1
