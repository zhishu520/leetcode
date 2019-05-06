class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        r = []
        for i in range(left, right + 1):
            if self.isDividingNumber(i):
                r.append(i)

        return r

    def isDividingNumber(self, n):
        if n == 0:
            return False

        if n < 10:
            return True

        t = n
        while t > 0:
            i = t % 10

            if i == 0 or n % i != 0:
                return False

            t /= 10

        return True
