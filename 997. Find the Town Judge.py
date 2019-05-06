class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """

        A = [0] * (N + 1)

        for i in trust:
            A[i[0]] = i[1]

        judge = 0

        for i in range(1, len(A)):
            if A[i] == 0:
                judge = i

        if judge == 0:
            return -1

        for i in range(1, len(A)):
            a = A[i]
            t = A[i]

        return judge



if __name__ == '__main__':
    s = Solution()
    r = s.findJudge(3, [[1,2], [2,3]])
    print r


