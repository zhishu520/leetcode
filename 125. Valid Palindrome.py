class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ret = ""
        for c in s:
            if c.isalnum():
                ret += c.lower()

        l = len(ret)
        for i in range(0, l/2):
            if ret[i] != ret[l - i -1]:
                return False

        return True

