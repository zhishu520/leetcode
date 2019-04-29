# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.s(1, n)

    def s(self, l, r):
        m = (l + r) / 2

        p = isBadVersion(m-1)
        c = isBadVersion(m)

        if not p and c:
            return m
        else:
            if c:
                return self.s(l, m - 1)
            else:
                return self.s(m + 1, r)


