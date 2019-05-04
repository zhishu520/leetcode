class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """

        sum = a + b + c
        a, c = min(a, b, c), max(a, b, c)
        b = sum - a - c

        if b - a == 1 and c - b == 1:
            return [0, 0]

        min_step = 1 if b - a <= 2 or c - b <= 2 else 2
        max_step = c - a - 2

        return [min_step, max_step]


if __name__ == '__main__':
    s = Solution()
    r = s.numMovesStones(4,3,2)
    print(r)
