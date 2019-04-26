class Solution(object):
    def trailingZeroes(self, n):
        r = 0
        while True:
            n = int(n/5)
            r += n
            if n == 0:
                break
        return r

