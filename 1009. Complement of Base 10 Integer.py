class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        r = 0
        cnt = 0
        while True:
            r += (0 if N % 2 == 1 else 1) << cnt
            N = N / 2
            cnt += 1

            if N == 0:
                break
        return r


