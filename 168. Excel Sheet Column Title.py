class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        s = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        r = ""

        while True:
            r += s[(n - 1) % 26 + 1]
            n = int((n - 1) / 26)
            if n == 0:
                break

        r = r[::-1]
        return r
