class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        a = []
        b = []

        for i in A:
            if i % 2 == 0:
                a.append(i)
            else:
                b.append(i)

        rt = []
        for i in range(len(A) / 2):
            rt.append(a[i])
            rt.append(b[i])
        return rt
