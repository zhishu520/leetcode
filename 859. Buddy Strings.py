class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """


        if len(A) != len(B):
            return False

        l = len(A)
        diff = 0

        for i in range(l):
            if A[i] != B[i]:
                diff += 1

        if diff == 2:
            return True

        if diff == 0:
            if len(set(A)) < l:
                return True

        return False

if __name__ == '__main__':
    print Solution().buddyStrings("ab", "ba")
