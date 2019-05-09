class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r = 0

        i = 0
        while i < 32:
            r *= 2
            r += n % 2
            n = int(n / 2)

            i += 1
        return r
