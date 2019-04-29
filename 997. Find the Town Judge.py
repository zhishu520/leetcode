class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """

        l = len(trust)

        if l != N - 1:
            return -1

        judge = trust[0][1]

        for i in trust:
            if i[1] != judge:
                return -1

        return judge







