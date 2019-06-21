class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        ss = s.split(" ")

        r = ""
        for i in range(len(ss)):
            if i != 0:
                r += " "
            r += ss[i][::-1]

        return r
