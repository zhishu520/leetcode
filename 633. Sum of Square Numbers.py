class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        import math

        for i in range(int(math.sqrt(c) + 1)):
            t = c - i * i
            t1 = int(math.sqrt(t))
            if t1 * t1 == t:
                return True

        return False
