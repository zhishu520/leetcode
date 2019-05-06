class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        A.sort(key=lambda x: abs(x), reverse=True)

        for i in A:
            if i < 0:
                i += 1

        sum = 0
        for i in A:
            if i < 0 and K > 0:
                K -= 1
                sum += -i
            else:
                sum += i

        if K % 2 == 1:
            sum -= 2 * abs(A[len(A) - 1])

        print(sum)
        return sum


if __name__ == '__main__':
    s = Solution()
    s.largestSumAfterKNegations([-8,3,-5,-3,-5,-2], 6)



