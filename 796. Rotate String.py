class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        lb = len(B)
        la = len(A)
        if lb != la:
            return False

        if len(A) == 0:
            return True

        for i in range(1, lb):
            flag = True
            for j in range(0, lb):
                if A[j] != B[(i + j) % lb]:
                    flag = False
                    break

            if flag:
                return True

