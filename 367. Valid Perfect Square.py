class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        import math
        x = int(math.sqrt(num))
        return x * x == num