class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """


        li = len(A)
        lj = len(A[0])


        rt = []

        for i in range(lj):
            new = []
            for j in range(li):
                new.append(A[j][i])
            rt.append(new)

        return rt
