class Solution(object):
    def sumEvenAfterQueries(self, A, Q):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        r = []

        sum = self.getSum(A)
        for i in Q:

            if A[i[1]] % 2 == 0 and i[0] % 2 == 0:
                sum += i[0]
            elif A[i[1]] % 2 == 1 and i[0] % 2 == 1:
                sum += A[i[1]] + i[0]
            elif A[i[1]] % 2 == 0:
                sum -= A[i[1]]

            A[i[1]] += i[0]
            r.append(sum)

        return r

    def getSum(self, A):
        sum = 0
        for i in A:
            if i % 2 == 0:
                sum += i
        return sum