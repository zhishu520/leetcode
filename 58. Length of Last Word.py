class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip()

        r = 0
        l = len(s)
        for i in range(0, l):
            if s[l - 1 - i].isalnum():
                r += 1
            else:
                break


        return r
