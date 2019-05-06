class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        return self.s(num, 0)

    def s(self, num, count):
        r = 0

        while num != 0:
            r += num % 10
            num = num / 10

        if r > 10:
            return self.s(r, count+1)
        else:
            return count
