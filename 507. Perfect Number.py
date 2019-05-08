class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num < 0:
            num = - num


        import math

        s = 0
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                s += i
                s += num / i
                print i, num / i
        return s + 1 == num


if __name__ == '__main__':
    s = Solution()
    r = s.checkPerfectNumber(6)
    print r