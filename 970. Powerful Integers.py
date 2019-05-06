class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """

        if x == 0 and y == 0:
            return []

        import math
        arr = [False] * (bound + 1)

        n, m = 0, 0

        if x > 1:
            t = bound
            while t > 0:
                t = int(t / x)
                n += 1

        if y > 1:
            t = bound
            while t > 0:
                t = int(t / y)
                m += 1
        print(n, m)

        for i in range(0, n + 1):
            for j in range(0, m + 1):
                xx = int(math.pow(x, i) if x > 0 else 0)
                yy = int(math.pow(y, j) if y > 0 else 0)
                print(xx, yy)
                if xx + yy <= bound:
                    arr[xx + yy] = 1

        r = []
        for i in range(0, bound + 1):
            if arr[i]:
                r.append(i)

        return r
