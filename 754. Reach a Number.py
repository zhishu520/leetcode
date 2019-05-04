class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """

        import math
        r = (-1 + math.sqrt(1 + 8 * target)) / 2
        print(r)

        if int(r) != r:
            r += 1

        return int(r)



if __name__ == '__main__':
    s = Solution()
    print(s.reachNumber(2))