class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

<<<<<<< HEAD
        if n <= 2:
            return 0

        arr = [True] * n

        for i in range(2, n):
            for j in range(2, n / i + 1):
                arr[i * j - 1] = False

        cnt = 0
        for i in range(1, n - 1):
            if arr[i]:
                cnt += 1

        return cnt
=======
    def isPrimes(self, n):
        pass

>>>>>>> 467b66627953119b23eb205ab876260e8bbf6502
