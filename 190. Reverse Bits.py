class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r = 0
        while n:
            r *= 2
            r += n % 2
            n = int(n/2)
        return r
