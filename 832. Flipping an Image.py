class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        r = []
        for a in A:
            t = a[::-1]
            for i in range(0, len(t)):
                t[i] = 0 if t[i] == 1 else 1

            print(t)
            r.append(t)

        return r

