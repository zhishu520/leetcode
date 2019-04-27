class Solution(object):
    def binaryGap(self, n):
        """
        :type N: int
        :rtype: int
        """

        max = 0
        t = -1
        p = 0
        while n:
            i = n % 2

            if i == 1:
                if t == -1:
                    t = p
                else:
                    if p - t > max:
                        max = p - t
                    t = p

            n = int(n / 2)
            p += 1

        return max



if __name__ == '__main__':
    s = Solution()
    print s.binaryGap(5)
