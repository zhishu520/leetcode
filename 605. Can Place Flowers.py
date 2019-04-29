class Solution(object):
    def canPlaceFlowers(self, f, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        s = len(f)
        for i in range(0, s):

            l,m,r = False, False, False

            if i - 1 < 0 or f[i-1] == 0:
                l = True

            if i + 1 >= s or f[i+1] == 0:
                r = True

            if f[i] == 0:
                m = True

            if l and r and m:
                f[i] = 1
                n -= 1

        return n <= 0


if __name__ == '__main__':
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1], 2))

