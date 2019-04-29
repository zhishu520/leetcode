class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        s = list(str)
        for i in range(0, len(s)):
            if s[i].isalpha() and ord(s[i]) < ord('a'):
                s[i] = chr(ord(s[i]) - ord('A') + ord('a'))

        return "".join(s)

