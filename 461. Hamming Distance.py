class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        r = 0
        while x != 0 or y != 0:
            r += (x % 2) ^ (y % 2)
            x /= 2
            y /= 2

        return r
